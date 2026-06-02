# The Care Wiki: A Fork of Karpathy's LLM Wiki for Healthcare

**Date**: 2026-04-15
**Status**: Architectural spec (companion to the master synthesis)
**Author**: Mewtwo
**Parent**: [Master Synthesis](care-brain-master-synthesis.md), [Direction C: Nervous System](direction-c-nervous-system.md)
**Reference**: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · [VentureBeat writeup](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)

**Purpose**: Specify how Ditto adapts (forks) Karpathy's LLM Wiki pattern into the Care Brain architecture — as the LLM-facing projection layer that sits on top of the Health Profile Store and makes longitudinal memory cheap for every pipeline.

---

## 1. Why a fork, not a copy

Karpathy's pattern is elegant and close to what we need. But healthcare has constraints that his personal-knowledge-base use case doesn't address. Three are load-bearing:

1. **Users modify their own data.** Karpathy's wiki is LLM-owned end-to-end. The patient doesn't edit the Obsidian files. In Ditto, the patient corrects their medication list, confirms voice-input, tombstones wrong data. So the source of truth cannot be markdown — it must be a structured, relational, mutable-via-UI health graph. The markdown wiki is a **projection** of that graph.
2. **Multi-tenant and privacy-critical.** Karpathy runs one wiki for himself on his disk. Ditto runs one wiki per patient, with hard isolation, audit logs, right-to-erasure, EU data residency. The fork has to account for tenant boundaries everywhere.
3. **Multiple audiences for the same patient.** The patient sees one thing. The daughter sees a different thing. The GP (eventually, via EHDS) sees a different thing again. The wiki can't be a single artifact — it must support multiple per-viewer projections composed from the same canonical graph.

This doc specifies what we keep from Karpathy, what we fork, and how the Care Wiki slots into the nervous-system architecture already defined in [direction-c-nervous-system.md](direction-c-nervous-system.md).

---

## 2. The Karpathy pattern in 30 seconds

Three layers:
- **Raw sources** (immutable): articles, notes, PDFs. LLM reads but never modifies.
- **The wiki** (LLM-owned): auto-generated, interlinked markdown. Entity pages, concept pages, overview, log, index. LLM creates, updates, maintains cross-references.
- **The schema** (CLAUDE.md / AGENTS.md): conventions and workflows. Co-evolved by human and LLM.

Three operations:
- **Ingest**: new source arrives → LLM reads it → updates 10–15 wiki pages in one pass → appends to log.
- **Query**: question arrives → LLM reads relevant pages → synthesizes an answer → files the answer back as a new wiki page.
- **Lint**: periodic health-check → flag contradictions, stale claims, orphans, missing cross-references.

Two special files: **`index.md`** (content catalog) and **`log.md`** (chronological append-only record).

The core insight: **the tedious part of maintaining a knowledge base is bookkeeping, not reading or thinking.** Humans abandon wikis because maintenance grows faster than value. LLMs don't get bored, don't forget cross-references, can touch 15 files in one pass.

---

## 3. What we keep

Eight elements of the pattern carry over unchanged:

| Kept | Why it still applies |
|---|---|
| Three-layer architecture (raw / wiki / schema) | Still the right separation of concerns |
| LLM does the bookkeeping; no humans maintaining markdown manually | Our team will not scale maintaining 40 pipelines + patient wikis; the LLM does it or it dies |
| Incremental ingest (not batch re-build on every change) | Per-pipeline-event updates fit the nervous-system's event-driven model perfectly |
| Entity pages, concept pages, timeline, overview | The right primitives for a patient journey |
| `index.md` + `log.md` | Both have direct equivalents in the Care Wiki |
| Cross-references / backlinks | How the LLM navigates without needing similarity search |
| Lint as a first-class operation | Quality gate that makes similarity/RAG unnecessary (see [master synthesis](care-brain-master-synthesis.md) Section 2) |
| Answers get filed back as new wiki pages | Explorations compound — same idea applies to patient Q&A |

---

## 4. What we fork (and why)

Nine material forks. These are the modifications that make the Care Wiki work for Ditto's constraints.

| Fork | Karpathy's default | Our version | Why |
|---|---|---|---|
| **Source of truth** | Markdown wiki IS the source of truth | **Health Graph (structured DB) is source of truth; wiki is a projection** | Users edit data. Deterministic logic queries it. Partners (via API) consume it. Markdown can't carry that. |
| **Ownership of wiki edits** | LLM writes freely via agent tools | **Only pipelines write, via a typed contract. All writes are reviewable diffs.** | Audit + safety + multi-tenant isolation require it. |
| **Wiki scope** | One global wiki for the user | **One wiki per patient (multi-tenant), strictly isolated** | Healthcare data is per-person. Cross-patient leakage is unacceptable. |
| **Projection per audience** | Single wiki, one viewer (the user) | **Multiple projections per patient: for-patient, for-partner, for-daughter, for-gp** | Audience adaptation is Ditto's keystone moat (see Magic Moment #1 — Share That Writes Itself). |
| **Ingest trigger** | User runs the agent and says "ingest this" | **Events on the bus trigger wiki updates automatically (`recording.completed`, `document.uploaded`, `voice_input.received`, etc.)** | Patients don't run ingest commands. The nervous-system event model handles this. |
| **Edit review** | LLM writes, user reads the diff later | **PR-style review for high-stakes pages (medications, conditions, care team) — either LLM-as-reviewer or patient-in-the-loop confirmation** | Silent wrong updates to medications are the #1 failure mode we must prevent. |
| **Storage** | Filesystem (Obsidian) | **DB-backed virtual filesystem, rendered on demand + cached** | Multi-tenant performance, easy deletion for GDPR right-to-erasure, regulatory audit. |
| **Language** | English (implicit) | **Canonical language per patient (usually NL); per-viewer projections may be translated via `translate_worker`** | Multi-language EU user base. |
| **Retrieval mode** | Primary: wiki navigation. RAG as alternative. | **Primary: fact (DB) + filter (wiki navigation). Similarity explicitly demoted to escape hatch; each use creates a wiki-schema-extension backlog item.** | Per the master synthesis architecture principle: if you reach for similarity, you have a wiki coverage gap to fix. |

---

## 5. The adapted architecture

### Three layers, redefined

```
┌────────────────────────────────────────────────────────────┐
│  RAW SOURCES (immutable, per patient)                       │
│  transcripts · documents · voice notes · labs · sensor data │
│  messages · calendar events · EHDS imports                  │
└────────────────────────────────────────────────────────────┘
                            │  (ingested via events)
                            ▼
┌────────────────────────────────────────────────────────────┐
│  HEALTH GRAPH (DB) — source of truth                        │
│  structured JSONB · versioned · audit log · user-editable   │
│  per patient; hard isolation; EU-only storage               │
└────────────────────────────────────────────────────────────┘
                            │  (rendered into markdown by
                            │   the wiki_render_worker)
                            ▼
┌────────────────────────────────────────────────────────────┐
│  CARE WIKI PROJECTION (LLM-facing, per patient)             │
│  entity pages · concept pages · timeline · index · log      │
│  per-viewer projections: for-patient, for-partner, ...      │
└────────────────────────────────────────────────────────────┘
                            │  (read by pipelines for context)
                            ▼
┌────────────────────────────────────────────────────────────┐
│  PIPELINES (from direction-c: summarize, extract, suggest,  │
│  answer, adapt, translate, prep, detect_changes, etc.       │
│  + new: wiki_render, wiki_lint, reviewer)                   │
└────────────────────────────────────────────────────────────┘
```

### The schema layer

Equivalent to Karpathy's `CLAUDE.md`. For Care Wiki, it's a template document called `wiki-schema.md` that travels with the Care Brain codebase (not per-patient). It specifies:

- Page types and their required frontmatter
- Naming conventions for entity slugs (`doctors/dr-de-jong.md`, `medications/oxaliplatin.md`)
- Cross-reference syntax (`[[medications/oxaliplatin]]`)
- Which pipelines write which pages
- High-stakes pages that require review
- Lint rules (what the wiki_lint_worker checks)
- Projection rules (how per-viewer projections differ)
- Language conventions (canonical vs. projected)

The schema is versioned in the Care Brain repo. Per-patient wikis reference the schema by version.

### Directory structure (per patient)

```
/patients/<patient_id>/wiki/
├── index.md                             — catalog of all pages, auto-maintained
├── log.md                               — chronological append-only event log
├── overview.md                          — narrative summary of the journey
├── open_questions.md                    — things the patient has asked but not yet resolved
├── unresolved_concerns.md               — things the patient mentioned that weren't addressed by their doctors
│
├── entities/
│   ├── doctors/
│   │   ├── dr-de-jong.md
│   │   └── dr-bakker.md
│   ├── conditions/
│   │   ├── colon-cancer.md
│   │   └── diabetes-type-2.md
│   ├── medications/
│   │   ├── oxaliplatin.md
│   │   └── metformin-500mg.md
│   └── care_circle/
│       ├── hans-partner.md
│       └── sanne-daughter.md
│
├── concepts/
│   ├── treatment-plan-2026.md
│   ├── side-effects-discussion.md
│   └── family-impact.md
│
├── timeline/
│   ├── 2024-01-15-diagnosis.md
│   ├── 2024-02-08-first-oncology.md
│   └── 2026-04-04-oncology-medication-change.md
│
└── projections/                         — per-viewer projections
    ├── for-patient/                     — the default projection
    ├── for-partner-hans/                — adapted for partner context
    ├── for-daughter-sanne/              — adapted tone, less detail
    └── for-gp/                          — clinical summary for GP (future, with EHDS)
```

Projections are **not** separately maintained. They are re-rendered from the canonical `entities/`, `concepts/`, `timeline/` when (a) those change, or (b) a pipeline that uses a projection is about to run.

---

## 6. Page templates

Every page has YAML frontmatter. Frontmatter is how lint rules and projection rules work.

### Entity page: a medication

```markdown
---
type: entity
entity_kind: medication
slug: medications/oxaliplatin
canonical_name: Oxaliplatin
current_dose: 85 mg/m² IV every 2 weeks
status: active
started: 2026-04-04
replaced: medications/capecitabine
sources:
  - event_id: evt_a7f9c (recording.completed, 2026-04-04)
  - event_id: evt_b4d01 (profile.updated, 2026-04-04)
last_updated: 2026-04-04T14:22:10Z
review_status: patient_confirmed
tier: core
languages: [nl, en]
---

# Oxaliplatin

Oxaliplatin is a chemotherapy medication Mara started on April 4, 2026, prescribed by
[[entities/doctors/dr-de-jong]]. It replaces [[entities/medications/capecitabine]], which she
had been taking since February 2024.

## Why it was prescribed

From Mara's appointment on 2026-04-04 with Dr. de Jong: the decision to switch was based on
scan results from 2026-04-02 which showed the tumor responding less well than hoped to
capecitabine. Dr. de Jong explained the trade-off: oxaliplatin is more effective for her
specific situation but carries different side effects.

## Related

- Condition: [[entities/conditions/colon-cancer]]
- Replaced: [[entities/medications/capecitabine]]
- Appointments: [[timeline/2026-04-04-oncology-medication-change]]
- Concept: [[concepts/side-effects-discussion]] (Dr. de Jong walked through side-effect profile)

## Source attribution

Every claim on this page is grounded in events Mara or Dr. de Jong created.
See frontmatter `sources` for the event IDs.
```

### Concept page: a treatment discussion

```markdown
---
type: concept
slug: concepts/side-effects-discussion
participants: [entities/doctors/dr-de-jong, patient]
discussed_on: 2026-04-04
related_medications: [entities/medications/oxaliplatin]
related_conditions: [entities/conditions/colon-cancer]
sources:
  - event_id: evt_a7f9c (recording.completed, 2026-04-04)
last_updated: 2026-04-04T14:22:10Z
review_status: pipeline_generated
---

# Side-effects discussion (2026-04-04)

During the April 4 appointment, Dr. de Jong walked Mara through the side-effect profile
of [[entities/medications/oxaliplatin]]. Key points discussed:

- Peripheral neuropathy (numbness/tingling in hands and feet, often triggered by cold)
- Fatigue, particularly in the week after infusion
- Nausea (manageable with prescribed anti-nausea medication)

Dr. de Jong noted that Mara's existing tolerance of [[entities/medications/capecitabine]]
doesn't necessarily predict how she'll tolerate oxaliplatin — different mechanism.

## Open questions (for Mara's next appointment)

- How long do the neuropathy symptoms typically persist?
- If side effects are severe, what's the off-ramp?

(See [[open_questions]] for the master list.)
```

### Timeline entry

```markdown
---
type: timeline
date: 2026-04-04
event_kind: appointment
provider: entities/doctors/dr-de-jong
location: UMCG oncology clinic
sources:
  - event_id: evt_a7f9c (recording.completed, 2026-04-04)
concepts: [concepts/side-effects-discussion, concepts/treatment-plan-2026]
significance: high
---

# April 4, 2026 — Oncology appointment (medication change)

Mara met with Dr. de Jong for her scheduled follow-up. Scan results from April 2 were
the focus. Tumor response to capecitabine has been less than targeted, so Dr. de Jong
proposed switching to oxaliplatin.

## What changed after this visit

- Medication: [[entities/medications/capecitabine]] → [[entities/medications/oxaliplatin]]
- Next appointment: 2026-05-02 (scheduled)
- Action items for Mara: begin oxaliplatin on 2026-04-11; monitor for neuropathy symptoms
  particularly with cold exposure

## Related

- Concepts discussed: [[concepts/side-effects-discussion]]
- What Hans received (adapted for partner): [[projections/for-partner-hans/2026-04-04]]
- What Sanne received (adapted for daughter): [[projections/for-daughter-sanne/2026-04-04]]
```

### `index.md`

```markdown
---
type: index
last_updated: 2026-04-04T14:23:00Z
entity_count: 18
concept_count: 7
timeline_count: 23
---

# Index for Mara (patient_id: p_0a3f...)

## Conditions
- [[entities/conditions/colon-cancer]] (stage 3b, diagnosed 2024-01-15)
- [[entities/conditions/hypertension]] (well-controlled)

## Active medications
- [[entities/medications/oxaliplatin]] (since 2026-04-04)
- [[entities/medications/metformin-500mg]] (since 2024-02-08)

## Historical medications
- [[entities/medications/capecitabine]] (2024-02 – 2026-04-04)

## Care team
- [[entities/doctors/dr-de-jong]] (medical oncology, UMCG)
- [[entities/doctors/dr-bakker]] (GP, Rotterdam)

## Care circle
- [[entities/care_circle/hans-partner]] (full access, auto-share)
- [[entities/care_circle/sanne-daughter]] (summary access, manual share)

## Recent timeline entries
- [[timeline/2026-04-04-oncology-medication-change]]
- [[timeline/2026-03-08-routine-oncology-follow-up]]
- [[timeline/2026-02-02-pet-scan]]

## Active concepts
- [[concepts/treatment-plan-2026]]
- [[concepts/side-effects-discussion]]

## Open questions: 2
## Unresolved concerns: 1
```

### `log.md`

```markdown
---
type: log
last_entry: 2026-04-04T14:22:10Z
---

# Log for Mara

## [2026-04-04T14:22:10Z] ingest | evt_a7f9c | recording.completed
Processed oncology appointment with Dr. de Jong.
- Updated: medications (oxaliplatin added, capecitabine marked replaced)
- Updated: concepts/side-effects-discussion (new)
- Updated: timeline/2026-04-04-oncology-medication-change (new)
- Updated: overview.md, index.md
- 12 wiki pages touched in this pass.

## [2026-04-04T14:25:45Z] review_required | medications/oxaliplatin
Page flagged for patient confirmation: new medication added. Confirmation card shown
in app. Awaiting patient action.

## [2026-04-04T14:38:12Z] review_resolved | medications/oxaliplatin
Mara confirmed. review_status advanced to patient_confirmed.

## [2026-04-04T14:40:02Z] projection_refresh
Regenerated projections for: for-partner-hans, for-daughter-sanne.
for-gp not applicable (no active provider integration yet).

## [2026-04-04T14:41:18Z] lint_pass | scheduled
0 contradictions. 0 orphans. 1 suggested new concept page (treatment-plan-2026 lacks
explicit stance on end-of-treatment markers). Backlog item created.
```

---

## 7. How pipelines interact with the wiki

### On ingest (a new event arrives)

1. Event arrives on the bus (e.g., `recording.completed`).
2. The recording pipeline runs as specified in direction-c — produces summary, extracts structured data, updates the Health Profile Store (DB).
3. The DB emits `profile.updated`, which triggers the **`wiki_render_worker`** (a new worker this doc adds).
4. `wiki_render_worker` reads the DB delta, regenerates or patches affected wiki pages, updates `index.md` and appends to `log.md`.
5. High-stakes pages (medications, conditions, care team) go into `review_required` state until confirmed.
6. Projection refresh: `for-patient`, `for-partner-*`, `for-daughter-*`, `for-gp` are re-rendered as needed (only projections whose source entities changed).

### On query (a pipeline needs context)

A pipeline like `answer_worker` or `prep_worker` needs patient context. Instead of loading raw transcripts, it assembles context from the wiki:

1. Read `index.md` to locate relevant pages by entity/concept.
2. Read those pages (e.g., the current medication list, the condition page, the last 3 timeline entries).
3. Augment with fact-mode DB queries for anything not in the wiki (e.g., "what's the scheduled time of the next appointment?").
4. Compose the prompt. Never re-read raw transcripts unless the wiki has a known gap (logged).

This replaces the "stuff the whole history into the context window" pattern with "navigate the wiki like a competent human researcher."

### On lint (scheduled)

`wiki_lint_worker` runs on a cadence (nightly + on-demand):

| Lint rule | What it catches |
|---|---|
| Contradiction between pages | Medication listed as active on one page but historical on another |
| Stale claim | A concept page references a medication that's been replaced |
| Orphan page | An entity page with no inbound links from timeline/concepts |
| Missing cross-reference | A timeline entry mentions "Dr. Visser" but no entity page exists |
| Dangling source | A frontmatter source event_id that can no longer be resolved |
| Coverage gap | A pipeline reached for similarity retrieval — the wiki schema needs extension |
| Review backlog | A page in `review_required` state for >48 hours |

Lint output: a list of findings, each with a severity and a proposed fix. High-severity findings become `profile.conflict_detected` events (already in the event taxonomy) and surface to the patient via the existing conflict-resolution UI.

### On query result → file-back

If `answer_worker` generates an answer that adds new synthesis (not just restating existing wiki content), the answer is filed back as a new concept page. Over time, the patient's Q&A compounds into the wiki just like ingested sources do. This is a direct port of Karpathy's pattern.

---

## 8. The review loop (PR-style)

The review loop is what makes the wiki trustworthy enough to be read by other pipelines. It's the discipline that keeps the wiki's quality high so similarity/RAG stays unnecessary.

### Three review modes

| Mode | What it is | When |
|---|---|---|
| **LLM-as-reviewer** | A separate `wiki_reviewer_worker` with a different prompt reads the proposed change and checks: consistency with other pages, grounding in source events, adherence to schema rules | All pipeline-generated edits to high-stakes pages (medications, conditions, care team, care circle). Fast, cheap. |
| **Patient-in-the-loop** | The existing confirmation flow from direction-c. Patient sees a card: "We noticed you started oxaliplatin. Is that right?" | When LLM-as-reviewer flags low confidence or when schema mandates explicit patient consent (voice input, new medications, condition changes). |
| **Clinical reviewer** | A clinician reviews the wiki delta | Reserved for B2B2C enterprise tier (insurer, hospital partner). Not in MVP. |

### Review state machine

```
proposed → review_required → {patient_confirmed, patient_rejected, reviewer_approved, reviewer_rejected}
              │                                                      │
              │                                          reviewer_rejected: revert
              │                                          patient_rejected: revert + log for prompt tuning
              ▼
       timeout after 48h → auto-apply as provisional + surface banner
```

### PR-style diffs

Every proposed wiki edit is expressed as a diff:
- Which pages change
- Frontmatter updates
- Content additions/deletions
- Source attribution (which event, which worker, which prompt version)

Diffs are stored (DB or git-backed blob) and queryable. The patient can go back and see: when did Ditto first learn I was on oxaliplatin, which pipeline wrote it, what did I confirm.

This is the audit trail that compliance and trust both require.

---

## 9. Per-viewer projections

This is the Care Wiki's largest departure from Karpathy. Instead of one wiki, one viewer, we have **one canonical wiki per patient + N projections per viewer role**.

### Projection types

| Projection | Audience | What changes |
|---|---|---|
| `for-patient/` | The patient themselves | Full detail. Direct second-person voice. Native language. |
| `for-partner-<name>/` | A partner with auto-share enabled | Full detail. Emotional register adjusted (e.g., "Mara is doing well with the transition"). Language matched to partner's preference. |
| `for-daughter-<name>/` | An adult child with summary access | Abridged. Softer framing. Fewer technical terms. Focus on what she can do to help. |
| `for-friend-<name>/` | A friend with one-liner access | Very abridged. No technical detail. Focus on reassurance and major updates. |
| `for-gp/` | The patient's GP, via EHDS once available | Clinical summary. Structured. Minimal narrative. (Tier 4 only.) |

### How projections are generated

Projections are **never** maintained as separate wikis. They are re-rendered from the canonical wiki by `adapt_worker` (already defined in direction-c) whenever:
- A source entity/concept/timeline page changes
- A new share is requested (on-demand refresh just before send)

The projection pipeline:
1. Read the canonical page + the viewer's role + the viewer's sharing permissions
2. `adapt_worker` generates the projected version, preserving source attribution but adapting detail, tone, and length
3. If the viewer's language differs, `translate_worker` adapts language
4. The projection is stored (cached) with a pointer back to the canonical page
5. When the canonical page changes, the projection is invalidated and re-rendered lazily (next read) or eagerly (if the viewer is about to receive a share)

### Why this matters

Moment #1 in the master synthesis (The Share That Writes Itself) is an emergent property of this projection model. The patient doesn't compose three messages — the wiki's projections already exist, and the "share" action is just "send this specific projection now."

The grandchild-friendly version in Moment #10 is another projection role. A kid-mode projection of the wiki.

The GP brief in Moment #5 is the `for-gp/` projection.

Once the projection mechanism exists, every new viewer role is a config + prompt change, not a new pipeline.

---

## 10. Storage, performance, caching

### Storage model

Recommendation: **DB-backed virtual filesystem, rendered on demand, with a cache layer**.

Not a real filesystem per patient (hard to scale multi-tenant, slow for right-to-erasure).
Not a git repo per patient (git doesn't love millions of small repos).

Instead:
- Each "page" is a row in a `wiki_pages` table: `(patient_id, page_path, frontmatter_json, content_md, rendered_at, source_event_ids[])`
- Rendering (regenerating the markdown from the Health Graph) is a pipeline task
- Cached rendered content is served to pipeline context-assembly
- Cache invalidation: when any source event that touches this page fires, the page is marked stale and re-rendered before next read

### Performance targets

| Operation | Target |
|---|---|
| Read a single page from cache | <20ms p95 |
| Re-render a page from Health Graph on cache miss | <500ms p95 |
| Pipeline context-assembly (read 5–10 pages) | <200ms p95 when cached |
| Full wiki regeneration after big event | <5s for a typical patient (100 pages) |
| Lint pass over one patient's wiki | <30s |

### Version control

Every page edit is a diff, stored in a `wiki_edits` append-only table: `(edit_id, page_path, before_hash, after_hash, diff, source_event_id, worker_id, review_status)`. The diff is the unit of audit, review, and rollback.

For GDPR right-to-erasure: deleting a patient tombstones the wiki (marks for purge); a scheduled job purges the tombstoned patient's `wiki_pages` and `wiki_edits` rows within the legally required window.

---

## 11. Security, privacy, compliance

### Isolation

No pipeline can read another patient's wiki. Enforced at the query layer: every wiki read requires a `patient_id` scope, and `wiki_pages` is partitioned by `patient_id`. Tested by the security review pipeline.

### Audit

Every wiki read and write is logged with `(patient_id, worker_id, event_id, timestamp, pages_touched)`. Retained for the compliance window. Queryable by the patient upon request (right of access under GDPR Article 15).

### Data sovereignty

All wiki data (DB rows, cache, rendered markdown) is stored in EU regions. No US replication, no US-region backups. This is already the case for the Health Profile Store per direction-c; the Care Wiki inherits.

### Right to erasure

A patient's `DELETE` request:
1. Marks the patient's wiki and Health Graph as tombstoned (soft-delete).
2. Invalidates all cached projections.
3. Within the compliance window, scheduled purge removes raw sources, graph rows, wiki pages, wiki edits, projection cache entries. Audit log entries retained in redacted form as required by law.

### Consent for projections

A circle member receiving a projection does not automatically gain read access to the canonical wiki. They only see their projection. The projection is generated under the patient's consent record, which is queryable and revocable.

---

## 12. Pipeline additions required

To support the Care Wiki, direction-c's worker inventory needs three additions:

| Worker | Purpose | Model suggestion | Trigger |
|---|---|---|---|
| `wiki_render_worker` | Render / patch wiki pages from Health Graph deltas | Sonnet for narrative pages, Haiku for structured pages | `profile.updated` |
| `wiki_reviewer_worker` | LLM-as-reviewer for high-stakes page edits | Sonnet with a review-focused prompt | `wiki.edit_proposed` (new event type) |
| `wiki_lint_worker` | Periodic wiki health check | Haiku + deterministic rules | Scheduled (nightly + on-demand) |

Two new event types need adding:
- `wiki.edit_proposed` (a pipeline produced a page diff; awaiting review)
- `wiki.edit_applied` (diff committed to canonical wiki)

The existing `profile.conflict_detected` event handles lint findings that surface contradictions.

---

## 13. Migration from current state

### Current state (per direction-c)

- Event bus and worker framework exist
- Health Profile Store (structured JSON, versioned) exists as planned
- Pipelines load context by reading summaries + Profile Store directly

### Migration sequence (order of dependencies, not time)

1. Add `wiki_pages`, `wiki_edits`, `wiki_projections` tables to the DB
2. Implement `wiki_render_worker` for entity pages (medications, conditions, care team) — the simplest pages
3. Add `wiki.edit_proposed` and `wiki.edit_applied` events to the bus
4. Implement `wiki_reviewer_worker`; route high-stakes edits through review; low-stakes commit directly
5. Implement `wiki_lint_worker` with an initial rule set (contradictions, orphans, stale claims)
6. Update pipeline context-assembly helpers so workers read from the wiki cache, not from raw transcripts. Start with `answer_worker` and `prep_worker` — they benefit most.
7. Implement projection generation: `for-patient`, `for-partner`, `for-daughter`. Leverage existing `adapt_worker`.
8. Instrument: track which pipelines use which retrieval mode; every similarity call logs a wiki-schema-extension suggestion
9. Scale: add remaining entity types (lab results, imaging, concepts), add `for-gp` projection when EHDS provider integration arrives

Each step is independently testable and reversible (the wiki layer is additive; removing it reverts pipelines to reading raw data).

---

## 14. Fork summary (what's different, compressed)

| # | Element | Karpathy | Care Wiki |
|---|---|---|---|
| 1 | Source of truth | Markdown | Relational health graph (markdown is projection) |
| 2 | Who edits | LLM freely | Pipelines only, typed contract, PR-style reviews |
| 3 | Tenancy | Single user | Multi-tenant, strict per-patient isolation |
| 4 | Viewers | One | Many — patient / partner / daughter / GP per wiki |
| 5 | Ingest trigger | User-initiated | Event-driven via nervous-system bus |
| 6 | Review | Informal | Three-tier: LLM-reviewer / patient-in-the-loop / (future) clinical |
| 7 | Storage | Filesystem | DB-backed virtual FS, render-on-demand + cache |
| 8 | Language | English default | Canonical per-patient language + per-viewer translation |
| 9 | Retrieval | Wiki navigation + RAG alternative | Fact + filter (wiki). Similarity is an explicit escape hatch that triggers schema extension |

---

## 15. Open questions

1. **Git-backed or DB-backed version control for wiki edits?** DB is simpler for multi-tenant and right-to-erasure. Git would give free diffing + branching. Lean DB-backed, but revisit when scale demands.
2. **How often do we regenerate projections?** Eager (on every canonical change, pre-cache every projection) is simple but expensive. Lazy (on read) saves cost but adds latency. Recommend: eager for active viewers (last 30 days), lazy otherwise.
3. **Projection scope — page-level or wiki-level?** I.e., does `for-daughter-sanne/` include a projection of the timeline, or only of summaries? Start with summaries + a digest of the timeline. Expand if daughters ask for more.
4. **When a canonical page is corrected, how do we treat already-sent projections?** Option A: send an update ("correction: we learned this was actually X"). Option B: silently update the projection. Probably A for medication-level corrections, B for minor copy tweaks.
5. **LLM-as-reviewer model choice.** Same model as author (reviewer finds its own mistakes less reliably) vs. different model (cross-check). Recommend a different family (e.g., if author is Claude, reviewer is Gemini or GPT) for high-stakes pages.
6. **Do we let the patient edit wiki pages directly?** I.e., a "correct" button on a medication page that rewrites the canonical entity. Answer: yes, but the correction flows through the Health Graph first, not the markdown. The markdown is regenerated.
7. **Lint cadence: nightly or continuous?** Nightly is simple. Continuous (debounced per patient, ~5 min after latest write settles) is more responsive. Start nightly.
8. **Do we expose the wiki as a user-facing artifact?** The master synthesis's Moment #14 ("The Journey Page") effectively IS the canonical overview rendered for the patient. So yes — eventually, some wiki pages are shown directly (formatted) in the app. Others remain internal.
9. **How do we handle Karpathy's "answers filed back" for healthcare?** If `answer_worker` generates a synthesis ("here's why your medication changed"), we file the synthesis as a new concept page. But the patient might not want a wiki page for every question they asked. Rule: only file-back if the answer required new synthesis that other pipelines can benefit from. Otherwise just cache the answer tied to the source event.
10. **Wiki schema versioning — how do existing patients migrate when the schema changes?** Every wiki page has a `schema_version` in frontmatter. Migrations are write jobs that re-render pages to the latest schema. Old schemas are supported read-only for some window.

---

## 16. What this unlocks

Once the Care Wiki exists:

- **Magic Moment #14 (Journey Page)** is the canonical overview rendered for the patient
- **Moment #19 (Condition Page That Grew With You)** is a rendered entity page for a condition
- **Every pipeline's context assembly becomes faster and smarter** because it reads pre-synthesized, cross-referenced prose instead of raw transcripts
- **Longitudinal memory becomes free** — adding the 40th JTBD doesn't cost more context engineering, because the context is already maintained
- **Audience adaptation is cheap** — a new viewer role is a new projection template, not a new pipeline
- **Similarity/RAG becomes genuinely rare** — because the wiki covers what the LLM needs to know, and lint closes coverage gaps over time
- **EHDS readiness (Tier 4)** — when external health records arrive via EHDS, they become new raw sources that the wiki ingests just like any other, without rearchitecting

This is the architectural unlock that makes the 45-JTBD horizon affordable for a 10-person team.

---

## 17. References

- [Karpathy, LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the pattern we fork
- [Karpathy on X](https://x.com/karpathy/status/2039805659525644595) — original post
- [VentureBeat: LLM Knowledge Base Architecture](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) — public summary
- [Direction C: Nervous System](direction-c-nervous-system.md) — the event/worker/Profile Store substrate the wiki layers onto
- [Master Synthesis](care-brain-master-synthesis.md) — strategic context, particularly Sections 2 (architecture) and 4 (wow moments)
- [Granola: Ditto Brain architecture](https://notes.granola.ai/t/df15831e-b0f1-41bb-9e47-570d804a3330) — the conversation with Yuri that established "DB is source of truth, wiki is projection"

---

Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
