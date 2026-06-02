# 01 · Core Architecture

**Read first**: `PROTOTYPE_README.md`. Schemas referenced here live in `05-data-schemas.md`.

**Purpose**: Specify the core AI architecture every magic path rests on. Five principles, eight components, and a clear boundary between WHAT you must build and HOW you choose to build it.

---

## The keystone decision

Ditto is **not an app with AI features**. Ditto is **a registry of specialized pipelines** that react to typed events, read and write a typed health graph, and update an LLM-facing markdown wiki projection. The orchestrator is thin. The intelligence lives in the pipelines + the graph + the wiki, together.

---

## Five principles (non-negotiable)

1. **Checklist, not features.** Every job is a pipeline. The product surface is the union of what its pipelines do.
2. **Typed everything.** Events, inputs, outputs, entities. No opaque JSON blobs. No untyped LLM in/out.
3. **Source of truth is relational. The wiki is a projection.** Users modify data; deterministic logic queries it; LLMs read a projection of it.
4. **Two retrieval modes: fact + filter. Similarity is an escape hatch.** Every retrieval call declares its mode. Similarity creates a backlog item to extend the schema so next time the query resolves via fact or filter.
5. **Eval-first pipeline contract.** No pipeline ships without an eval suite and a retirement criterion.

---

## Component 1: Event Bus

An in-process async dispatcher. Typed events. Pipelines subscribe to event types. When an event is emitted, every subscribed pipeline runs (potentially in parallel).

**Requirements**:
- Must support async dispatch without blocking the caller
- Must propagate `correlation_id` across pipeline chains so a full causal trace is reconstructable
- Must log every event emission (type, patient_id, correlation_id, timestamp)
- Idempotency: processing `(event_id, pipeline_name)` more than once must not double-apply writes
- Subscription must be declarative (a pipeline declares its `trigger`; the bus wires it up)

**What you choose**:
- Exact implementation (asyncio loop, queue library, etc.)
- Whether to persist events (recommended for replay, but in-memory acceptable for prototype)
- How to handle pipeline failures (retries, dead-letter)

For the prototype, do NOT use Kafka, RabbitMQ, or Redis. The overhead isn't justified at this scale.

See `05-data-schemas.md` for the full event envelope and the canonical event types.

---

## Component 2: Pipeline Contract

Every pipeline declares:

| Field | Type | Purpose |
|---|---|---|
| `name` | string, unique | Identifier used everywhere (logs, evals, registry) |
| `trigger` | event_type or list, optionally with a filter predicate | What kicks this pipeline off |
| `input_filter` | typed query over the health graph/wiki | What context this pipeline needs |
| `context_mode` | `fact` / `filter` / (rarely) `similarity` | Declares which retrieval mode is used |
| `processor` | callable | The actual work. May be deterministic, LLM-based, or hybrid |
| `output_type` | Pydantic or equivalent typed schema | What this pipeline produces/writes |
| `side_effects` | enum list: `graph_write`, `wiki_write`, `event_emit`, `external_call` | What the pipeline changes |
| `tier` | `free` / `premium` / `internal` | Monetization and access mapping |
| `eval_suite` | path to eval config | Where the quality gate lives |
| `retirement_criterion` | string | Human-readable: under what condition this pipeline should be removed |

Pipelines should be **idempotent** keyed on `(event_id, pipeline_name)`.

**Pipelines can be**:
- **Pure / deterministic**: no LLM. E.g., drug-interaction check against a known formulary.
- **LLM-backed**: one or more LLM calls.
- **Hybrid**: deterministic lookup + LLM to compose prose. Encouraged for safety-critical work.

**Registration mechanism**: your choice — decorator, registry class, module-scan. Must be explicit and introspectable (you should be able to list all registered pipelines and their contracts).

**Example (illustrative, pseudo-Python)**:

```python
@pipeline(
    name="check_medication_interactions",
    trigger=[("profile.updated", lambda e: "medications" in e.payload["changed_fields"])],
    input_filter=lambda p: p.medications(status="active"),
    context_mode="fact",
    output_type=InteractionFlag,
    side_effects=["graph_write", "event_emit"],
    tier="premium",
    eval_suite="/evals/check_medication_interactions/",
    retirement_criterion="replaced by EHDS native interaction service",
)
async def check_medication_interactions(ctx, event):
    ...
```

The exact decorator/registration pattern is yours to design. The contract fields are not.

---

## Component 3: Health Graph (Source of Truth)

A typed, versioned, audit-logged persistence layer. PostgreSQL with JSONB is recommended; SQLite acceptable for prototype.

**Core entity types** (full schemas in `05-data-schemas.md`):
- `Patient`
- `Doctor`
- `Condition`
- `Medication`
- `CareCircleMember`
- `Recording`
- `Appointment` (past / pending / suggested)
- `ActionItem`
- `Symptom`
- `Reaction` (inbound from circle)
- `HelpOffer`
- `ScheduledCall`
- `PrePreparedQuestion`

**Every entity supports**:
- `id` (UUID)
- `patient_id` (foreign key — isolation boundary)
- `created_at`, `updated_at`
- `version` (monotonic counter for optimistic concurrency)
- `source_event_ids[]` (provenance — which events caused this state)
- `review_status` (`proposed`, `auto_approved`, `reviewer_approved`, `patient_confirmed`, `rejected`, `provisional`)
- `tombstoned_at` (nullable — soft delete for GDPR right-to-erasure)

**Audit log table**: every entity mutation writes `(patient_id, entity_type, entity_id, before_snapshot, after_snapshot, source_event_id, actor, timestamp)`. Append-only.

**Isolation rule (critical)**: every read and write must be scoped by `patient_id`. The data-access layer should enforce this — a query without a patient_id scope should error. No pipeline, no matter what, reads or writes across patient boundaries.

---

## Component 4: LLM Wiki Projection

A per-patient markdown wiki auto-generated and auto-maintained from the health graph. **The LLM reads this, not the graph directly.** Users do not edit the wiki; they edit the graph (via the app), and the wiki re-renders.

**Storage**: a DB-backed virtual filesystem — a `wiki_pages` table with:
```
(patient_id, page_path, frontmatter_json, content_md, rendered_at, source_event_ids[], schema_version)
```

Markdown is rendered from the graph on a change, cached, and served to pipelines on read.

**Page types** (see `05-data-schemas.md` for templates):
- `entities/doctors/*.md`
- `entities/conditions/*.md`
- `entities/medications/*.md`
- `entities/care_circle/*.md`
- `concepts/*.md`
- `timeline/YYYY-MM-DD-*.md`
- `symptoms/timeline.md`
- `inbox/reactions/*.md`
- `inbox/help_offers.md`
- `inbox/scheduled_calls.md`
- `plan/active.md`
- `appointments/pending.md`
- `open_questions.md`
- `unresolved_concerns.md`
- `overview.md`
- `index.md` (catalog, auto-maintained)
- `log.md` (append-only event record)

**Per-viewer projections**: for Path 3 and others, per-viewer views (patient / partner / adult-child / friend) are re-rendered from canonical pages on-demand via the `adapt_worker` pipeline. Projections are NOT maintained independently; they are cached derivations of the canonical wiki.

---

## Component 5: Wiki Workers (Three new workers)

Three workers make the wiki layer live:

### `wiki_render_worker`
- Triggered by: `profile.updated` and similar graph-change events
- Reads the graph delta, regenerates or patches affected wiki pages
- Updates `index.md` and appends to `log.md`
- Structured entity pages (medications, doctors) use deterministic templates
- Narrative pages (overview, timeline entries, condition pages, journey) use LLM composition with grounding to source events
- Output: `wiki.edit_proposed` events (or direct apply for low-stakes pages)

### `wiki_reviewer_worker`
- Triggered by: `wiki.edit_proposed` events for high-stakes pages (medications, conditions, care team)
- LLM-as-reviewer: reads the proposed diff + existing pages, checks consistency, grounding, schema adherence
- Outputs: approval (→ apply) or concerns (→ patient-in-the-loop confirmation)
- Should use a different prompt/flow than `wiki_render_worker` so it's not rubber-stamping

### `wiki_lint_worker`
- Scheduled (nightly per patient is fine; on-demand endpoint also available)
- Scans the wiki for: contradictions between pages, stale claims, orphan pages, dangling source references, coverage gaps
- Emits `profile.conflict_detected` events for severe findings
- Produces a lint report queryable via API

---

## Component 6: Retrieval (Two modes + escape hatch)

When a pipeline needs patient context, it uses a retrieval helper that supports:

### Fact mode
- Structured queries against the health graph (SQL, ORM, etc.)
- No inference. No LLM. No embeddings.
- Examples: "list current medications", "last appointment date with Dr. de Jong", "circle members with auto-share enabled"
- Returns structured data

### Filter mode
- Navigate the wiki by entity / concept / tag / backlinks
- Read the relevant pages; return rendered markdown + metadata
- Examples: "everything about this diabetes diagnosis", "all conversations about the current medication"
- Returns composed context as markdown

### Similarity mode (escape hatch — use rarely)
- Vector search over text chunks
- Allowed only when fact and filter both fail AND it's declared in the pipeline contract
- **Every similarity call must log a "wiki schema extension proposal"** — what entity/concept/tag would resolve this query via filter next time?
- Goal: monotonically reduce similarity usage over time

**Logging requirement**: every retrieval call writes `(pipeline_name, mode, patient_id, query_summary, result_size_tokens, latency_ms, source_event_correlation_id)`. This is how you know whether the "similarity is rare" discipline is working.

---

## Component 7: Review Loop

Every pipeline-proposed wiki edit is a typed diff.

**Diff envelope**:
```
WikiEdit {
  edit_id: UUID
  patient_id: UUID
  page_path: str
  before_hash: str
  after_hash: str
  frontmatter_diff: dict
  content_diff: str  # or structured
  proposing_pipeline: str
  source_event_ids: UUID[]
  stakes: "low" | "high"
  review_status: "proposed" | "auto_approved" | "reviewer_approved" | "patient_confirmed" | "rejected" | "provisional"
  proposed_at: ISO8601
  resolved_at: ISO8601 | null
}
```

**Stakes classification**:
- **High**: edits to `medications`, `conditions`, `care_circle` entities, and any page flagged as safety-critical in the page template
- **Low**: timeline entries, concept pages, `log.md`, `index.md`

**State machine**:

```
proposed ─► auto_approved ─► applied        (low-stakes)
proposed ─► review_required ─► reviewer_approved ─► applied
proposed ─► review_required ─► patient_confirmed ─► applied
proposed ─► review_required ─► rejected ─► discarded
review_required ─► timeout (48h) ─► provisional applied (with banner)
```

**Prototype scope**: implement the full state machine for at least one high-stakes page type (recommend: medications). Low-stakes pages can auto-apply. The patient confirmation UI can be a simple endpoint that returns pending items.

All edits are audit-logged and reversible (revert = apply inverse diff).

---

## Component 8: Eval Harness

Non-negotiable. Every pipeline ships with evals. A shared harness runs them; each pipeline registers its suite.

**An eval suite is**:
- A directory of YAML files under `/evals/<pipeline_name>/`
- Each YAML is one test case: input (event payload or graph state), expected outputs (structured assertions or LLM-judged criteria), tags (happy path, edge, adversarial)
- Minimum: 10 cases per pipeline, covering at least 3 happy paths, 3 edge cases, 3 adversarial cases

**Evaluation types**:
- **Structured comparison**: deterministic. The pipeline's output matches expected fields (e.g., medication extracted with correct name, dose, status).
- **LLM-judged**: for narrative outputs (summaries, adapted shares). Use a judge prompt that checks specific criteria (grounding, tone, accuracy, audience-fit). Emit a score 1–5 and a pass/fail based on threshold.

**The harness must**:
- Run evals per pipeline or across all pipelines
- Report pass rate, regressions, and failing cases
- Be callable from CI and from a local command

**Thresholds** (minimum to "pass" for the prototype):
- Extraction pipelines: 90% of test cases pass on structured fields
- Summarization / narrative pipelines: 85% of test cases score ≥4 on LLM-judged criteria
- Safety-critical (drug interactions, pattern detection): 100% of adversarial "should not fire" cases correctly don't fire; 90% of "should fire" cases do fire

Regression policy: a pipeline whose eval pass rate drops from a previous baseline must not ship. The harness should be runnable against a stored baseline.

---

## Component 9: LLM Client Abstraction

All LLM calls go through a unified client. Default to Anthropic Claude but abstract provider and model behind a config.

**Client contract**:
- `complete(prompt, model, max_tokens, temperature, stream=False, tools=None) -> Response`
- `Response` includes content, usage (tokens in/out), latency, model used, request_id
- Every call is logged with `(patient_id, pipeline_name, model, prompt_tokens, completion_tokens, latency_ms, cost_estimate_usd)`

**Model assignment defaults** (override per pipeline if needed):
- Reasoning / narrative / review: Claude Sonnet (latest)
- Extraction / structured / translation: Claude Haiku (latest)
- Embeddings (only if similarity escape hatch is used): pick a standard (OpenAI text-embedding-3-small or Anthropic equivalent)

**Prompt storage**: all prompts live in `/prompts/<pipeline_name>/*.md`. Versioned (git). NEVER inline prompts in Python code for production pipelines — for prototype, brief inline is OK for scaffolding but move to files before merging.

**Prompt template**: agent's choice. Jinja-style, f-strings, whatever. Must support parameter substitution and be readable without running the code.

---

## Minimum viable architecture (checklist)

The prototype's core architecture is done when:

- [ ] Event bus dispatches typed events with correlation_ids; ≥5 event types implemented
- [ ] Health graph persists ≥10 core entity types with versioning + audit log + patient isolation
- [ ] Pipeline registration + contract; ≥8 pipelines registered
- [ ] Wiki projection renders ≥5 page types; updates on graph changes; cached and invalidated correctly
- [ ] `wiki_render_worker`, `wiki_reviewer_worker`, `wiki_lint_worker` all working
- [ ] Retrieval helper with fact + filter modes; similarity escape hatch logged when used
- [ ] Review state machine working end-to-end for medications
- [ ] Eval harness with ≥3 pipelines covered
- [ ] LLM client abstracted; prompts externalized to `/prompts/`
- [ ] HTTP API surfaces the endpoints each path spec requires (see 02–04)

---

## What you choose (not specified here)

- Language and framework specifics (within the suggestions above)
- Exact DB schema SQL (within the constraints on what must be tracked)
- Serialization format for event payloads (JSON recommended; MsgPack or Protobuf acceptable)
- Caching strategy for the wiki (in-process, Redis, whatever fits)
- Retry / dead-letter policy for failed pipelines
- Logging and observability tooling
- Package / project structure (suggestion in `PROTOTYPE_README.md`, but flexible)
- Prompt template syntax
- Eval YAML schema (define it once, use it everywhere — but the schema is your call)

When in doubt, favor simplicity. It's a prototype.

---

## What you do NOT have latitude on

- The five principles above
- The event envelope structure (in `05-data-schemas.md`)
- The pipeline contract fields (above)
- The state machine for review
- Patient isolation (every query scoped by patient_id; no exceptions)
- The ranking of retrieval modes (fact → filter → similarity, in that order of preference)
- The requirement that every pipeline has an eval suite
- The requirement that prompts are externalized
- The requirement that every mutation is audited

If any of these seem wrong to you, flag it in `/prototype/OPEN_QUESTIONS.md`. Do not silently diverge.

---

## Handover to paths

Once the architecture above is running, the three magic paths each add specific pipelines, endpoints, and wiki page types. Each path is independently implementable. See:

- `02-path-1-post-appointment-cascade.md` — the Tier 1 anchor. Start here if picking a path.
- `03-path-2-symptom-tracking.md`
- `04-path-3-reaction-loop.md`
