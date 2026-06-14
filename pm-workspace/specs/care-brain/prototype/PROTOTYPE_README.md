# Care Brain Prototype — Implementation Guide

**Audience**: Managed engineering agents (Claude Code, OpenCode, Devin, etc.) tasked with building a working prototype of the Care Brain's AI architecture and its three core magic paths.

**Goal**: A functional prototype demonstrating the plugin-pipeline architecture, typed health graph, LLM wiki projection, and three end-to-end magic paths (Post-Appointment Cascade, Symptom Tracking via Voice, Inbound Reaction Loop). Good enough to demo to the Ditto team and to investors. Not production.

**Scope**: Backend pipelines, data models, HTTP APIs, wiki projection, review loop, eval harness. Minimal frontend sufficient to demo the paths. No production mobile UI. No partner integrations. No EHDS.

---

## Strategic context (10-second version)

Ditto is the care-journey assistant for families facing cancer and neurodegenerative disease. Not a chatbot. Not a summarizer. An assistant built as a catalog of specialized pipelines ("plugins"), each doing one high-value job brilliantly. The source of truth is a typed health graph. The LLM reads an auto-maintained markdown wiki projected from that graph. Retrieval is ranked fact → filter; similarity is an escape hatch.

For the full strategic thesis, see:
- `/pm-workspace/specs/care-brain/care-brain-one-pager.md` (spec-017 — the canonical one-pager, read first)
- `/pm-workspace/specs/care-brain/care-brain-master-synthesis.md` (spec-013 — deep context)
- `/pm-workspace/specs/care-brain/care-brain-magic-paths.md` (spec-018 — the three paths mapped)
- `/pm-workspace/specs/care-brain/care-brain-wiki-architecture.md` (spec-014 — the wiki layer)

**You do not need to re-read the whole corpus.** These prototype docs are self-contained enough to build from. Refer to the strategic docs only when a choice feels ambiguous.

---

## Document map

| File | Read when |
|---|---|
| `PROTOTYPE_README.md` | Start here (this file) |
| `01-core-architecture.md` | Before implementing anything — the architecture everything else rests on |
| `02-path-1-post-appointment-cascade.md` | When implementing Path 1 (the Tier 1 anchor) |
| `03-path-2-symptom-tracking.md` | When implementing Path 2 |
| `04-path-3-reaction-loop.md` | When implementing Path 3 |
| `05-data-schemas.md` | Referenced from all other docs — the canonical schemas |

**Reading order**: README → 01 → 05 → 02 → 03 → 04. Paths 2, 3, 4 can be implemented in any order once the core architecture (01) is in place.

---

## Technology choices — suggested, not mandated

| Concern | Suggestion | Why | Flexibility |
|---|---|---|---|
| Language | Python 3.11+ | Fits the team, fits LLM-heavy code, good ecosystem | Open — TypeScript/Node acceptable if the agent prefers and stays consistent |
| HTTP framework | FastAPI | Typed, async, good docs | Any modern async framework fine |
| Database | PostgreSQL with JSONB | Supports structured + semi-structured data; needed for health graph | SQLite acceptable for prototype if simpler |
| Event bus | In-process asyncio dispatcher | Prototype scope; no Kafka/Redis required | Must be typed; must preserve correlation_ids |
| LLM client | Anthropic SDK (Claude Sonnet for reasoning, Haiku for extraction/translation) | Ditto's preferred stack; align with production direction | Abstract behind a client interface so providers can be swapped (OpenAI, Gemini) via config |
| Prompt storage | Versioned markdown files under `/prompts/<pipeline_name>/` | Editable without code changes; diffable | Any convention that separates prompts from code |
| Testing | pytest | Standard | Any equivalent is fine |
| Frontend (for demo) | Minimal — static HTML/JS, or a small Next.js page | It's a demo, not a product | Agent chooses; not the focus |
| Eval harness | See `01-core-architecture.md` section on evals | Non-negotiable architecture choice | Agent picks the implementation |

Where the spec says **must** or **never**, it's a constraint. Where it says **suggest**, **recommend**, or **default**, you have freedom. When in doubt, favor simplicity for the prototype.

---

## What "done" looks like

The prototype is done when:

1. **Core architecture is running**:
   - Event bus dispatches typed events with correlation_ids.
   - Health graph persists entities with versioning and audit log.
   - At least 8 pipelines registered via the plugin contract.
   - Wiki projection renders at least 5 page types and updates on graph changes.
   - Review state machine works end-to-end for at least one high-stakes page type (medications).
   - Eval harness is implemented and runs against at least 3 pipelines.

2. **Path 1 (Post-Appointment Cascade) works end-to-end**:
   - POST a recording (transcript) → events fire → summary, actions, appointments, pre-question matches, adapted shares all produced.
   - GET the cascade endpoint returns a structured JSON response with all four card sections populated.
   - One sample demo recording is included in `/fixtures/`.

3. **Path 2 (Symptom Tracking) works**:
   - POST a voice-input transcript → symptom extracted → logged to health graph and wiki.
   - GET symptom timeline returns time-series data ready for visualization.
   - A pattern detection pipeline runs on demand and emits detected patterns.

4. **Path 3 (Inbound Reaction Loop) works**:
   - POST a reaction from a circle member (with optional help offer and optional call request) → routed into patient's inbox.
   - GET the patient's inbox returns curated, structured reactions.
   - Scheduling assistant handles at least one "call me" end-to-end with mock calendars.

5. **Evals pass** for all implemented pipelines at their specified thresholds.

6. A **top-level README** at the prototype root describes:
   - How to run it locally
   - How to load the sample fixtures
   - How to hit each endpoint with example curl commands
   - How to run evals

---

## Non-goals (explicitly out of scope)

The prototype is not trying to be production. Skip:

- Production-grade mobile UI
- Multi-tenant performance optimization
- EHDS integration
- B2B2C insurer partner surfaces
- Advanced access control (basic patient-id isolation is sufficient)
- Real third-party calendar integrations (mock calendar APIs are fine)
- Real translation to Turkish/Arabic/Papiamentu (EN + NL only)
- Cross-region data replication
- Sophisticated caching infrastructure (in-memory cache is fine)
- Full conflict resolution UI for review_required states (a stub endpoint that auto-confirms is fine for the demo)
- Rate limiting, abuse protection, billing, tier enforcement
- Real authentication (a patient_id query parameter is fine; do not ship this to production)

If you find yourself building for scale, you're over-investing. Get the primitives right, get the three paths working end-to-end, move on.

---

## Prototype repository layout (suggested)

```
/prototype/
├── README.md                    # how to run
├── pyproject.toml               # or requirements.txt
├── /app/
│   ├── main.py                  # HTTP API entry
│   ├── event_bus.py             # in-process dispatcher
│   ├── pipelines/               # one module per pipeline
│   ├── workers/                 # the wiki workers + the review worker
│   ├── graph/                   # health graph models + DB access
│   ├── wiki/                    # wiki renderer + page templates
│   ├── retrieval/               # fact + filter helpers
│   ├── review/                  # review state machine
│   ├── llm/                     # LLM client abstraction
│   └── schemas/                 # Pydantic models for events and entities
├── /prompts/
│   └── <pipeline_name>/         # versioned markdown prompts
├── /evals/
│   └── <pipeline_name>/*.yaml   # eval sets
├── /fixtures/
│   └── sample_recording.json    # canned demo data
│   └── sample_voice_input.json
│   └── sample_reaction.json
├── /frontend/                   # minimal demo UI (optional)
└── /tests/
```

This is a suggestion. Structure in the way that works for your implementation, but **keep pipelines, prompts, evals, and schemas as first-class directories** — they are the primitives of the architecture.

---

## Working with these specs

- **Read `01-core-architecture.md` before any implementation.** The paths depend on it.
- **Refer to `05-data-schemas.md` for every data contract.** Do not invent new schemas; extend existing ones.
- **The paths (02–04) can be built in parallel** once 01 is done. They share the architecture but have independent pipelines.
- **Every pipeline needs an eval suite** before it's considered complete.
- **If a spec is ambiguous, err toward simpler** and note the decision in the repo's `README.md` under "Design decisions made during implementation."
- **If a spec seems wrong, flag it** — open a GitHub issue or write to `/prototype/OPEN_QUESTIONS.md`. Do not silently diverge.

---

## Success criteria summary

- Plugin architecture clearly works (add a new pipeline in under 100 lines)
- Wiki projection updates live as the graph changes
- All three paths demonstrable end-to-end from a single API call each
- Evals passing
- Code review-ready (not polished production code, but not slapdash)
- README clear enough that a new engineer can run it in under 15 minutes

Good luck.
