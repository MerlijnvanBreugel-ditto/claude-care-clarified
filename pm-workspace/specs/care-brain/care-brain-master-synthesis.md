# The Care Brain: Master Synthesis

**An open assistant for health — specialized, not general-purpose.**

**Date**: 2026-04-15
**Status**: Strategic synthesis, flat (no timing)
**Author**: Mewtwo
**Horizon**: 24 months (full vision)
**Role**: Master synthesis. Consolidates the Care Brain corpus into a single canonical "what we're building and why" document. Supersedes the roadmap-and-sequencing sections of prior docs. Execution-level specs (delivery schedule, sprint structure, feature specs) remain in their existing homes.

**Parent docs** (referenced, not repeated):
- [Unicorn Strategy](unicorn-strategy.md) — virtual founding team, moat thesis
- [Magic Experience Vision](magic-experience-vision.md) — contrarian experience crunch, 7 wow moments, architecture-for-magic
- [Care Brain Strategy](care-brain-strategy.md) — approved strategic framing
- [Direction C: Nervous System](direction-c-nervous-system.md) — canonical architecture, pipelines, workers, schemas
- [Care Brain MVP Spec](care-brain-mvp-spec.md) — delivery spec, slices, gates
- [Phase 1 Smart Suggestions](care-brain-phase1-smart-suggestions.md) — Q&A feature spec
- [Business Case](business-case.md) — unit economics, TAM, moat math
- [Competitive Analysis](competitive-analysis.md) — positioning

---

## 1. Context & Thesis

### The one-line positioning

**Ditto is the open assistant for health — specialized, serious, and present for the people who love you. Not a general-purpose chatbot. Not a summarizer. A care companion that feels like Claude Code or OpenCode, tuned to healthcare instead of the terminal.**

Every other consumer health AI is building a general-purpose chatbot with a medical skin. ChatGPT Health (OpenAI, launched Jan 2026, backed by the Torch Health acquisition), Copilot Health (Microsoft, March 2026), Claude for Healthcare (Anthropic, March 2026), Apple Health AI (scaled back from Project Mulberry in Feb 2026). Same shape, same limits, same ceiling. They answer your questions. They don't know you. They don't know the people who love you. They don't carry the weight of a cancer diagnosis across six appointments and three family members and a Turkish-speaking mother. Nobody is building that product. Ditto is.

### Why this doc exists

Seven+ canonical Care Brain docs exist. They're aligned but fragmented. Yuri's architecture conversation (Granola: *Ditto Brain - architecture*) and Karpathy's [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) added two architectural pieces that weren't in any prior doc. The magic-experience crunch produced a new experience reframe and a different answer on the moat. The corpus needs a single master synthesis that answers: *if we were to build this fully, what does the specification look like?*

This doc does three things that no existing doc does:

1. Articulates the **pipeline plugin architecture** as the fundamental build decision — not an afterthought, not a Phase-N detail, but the keystone that makes everything else affordable.
2. Maps **40+ jobs-to-be-done** (Yuri's "assistant's checklist") across the full patient journey — not just the ones we're building first.
3. Expands the **wow moments** from 7 to 20+ — the full catalogue of what magic looks like when the architecture is in place.

Everything here is flat. No weeks. No phases. No delivery schedule. Merlijn will handle execution planning separately. This is the strategic layer: *the spec, if we were to build it.*

### What's new vs. existing docs

| New here | Why it wasn't there before |
|---|---|
| Pipeline plugin framework as the keystone architecture | Prior docs locked in 8 fixed pipelines; this generalises them into a plugin contract for N future pipelines |
| LLM wiki projection layer (Yuri-corrected Karpathy pattern) | The Karpathy gist arrived after the nervous-system doc was written |
| Three-mode retrieval explicitly ranked (fact → filter → similarity) | Prior docs assumed retrieval; this names the discipline that prevents RAG default-to-slop |
| 40+ JTBD organized as an assistant's checklist | Prior docs described 7 features; this describes the 40 jobs an actual health assistant would hold |
| 20+ wow moments across 8 emotional types | Prior magic-vision doc had 7; this catalogues the full emotional surface |
| Capability tier map (not time-based) | Prior docs sequenced by phase/week; this sequences by unlock dependencies |
| Founder panel as a structured section (not just inline) | Prior docs embedded founder voices; this gives each a structured one-paragraph reaction to the full plan |

### The thesis, compressed

1. **The AI is commoditizing.** Summarization is shelf-life-quarters, not years. ChatGPT Health has 40M daily health queries. Apple Intelligence will summarize voice recordings natively. The raw model capability is no longer defensible.
2. **The moat is not intelligence. It is relationship.** Who cares about whom. What each person needs to know. The longitudinal memory of a patient's journey. The Care Graph.
3. **The product surface is not a chat window.** It is a growing catalogue of specialized pipelines, each one doing a specific high-value job brilliantly, orchestrated by a thin agentic layer, exposed through composed surfaces that don't feel like AI.
4. **The architecture is the unlock.** A pipeline plugin framework + typed health graph + LLM wiki projection + three-mode retrieval makes the 40th job-to-be-done cheap to add. Without this, the team drowns at job number 12.
5. **The emotional peak is audience-adapted sharing.** The share-that-writes-itself is the only feature that simultaneously produces "I cannot live without this" and grows the care graph. It is the keystone experience.
6. **The window is 18–24 months before Big Tech notices the gap.** The only way to win in that window is to make the architecture cheap and ship pipelines faster than incumbents can rebuild their surface area.

---

## 2. The Architectural Foundation

### The fundamental decision

**Ditto is not an app with AI features. Ditto is a plugin framework for specialized health pipelines, backed by a typed health graph, projected to an LLM as a living wiki, and composed into surfaces that don't feel like AI.**

This is the decision everything else rests on. Every prior doc hinted at pieces of this. Direction C's nervous-system architecture is the event bus + stateless workers substrate. Yuri's conversation named the plugin pattern explicitly: *"each checklist item = a specialized, validated pipeline, triggered by events, operating on typed data, emitting typed data back into the graph."* Karpathy's wiki pattern named the context layer. This synthesis stitches them together into one non-negotiable architecture.

### Five architectural principles

| # | Principle | What it means | What it rules out |
|---|---|---|---|
| 1 | **Checklist, not features** | The product surface is the union of pipelines the assistant runs. Each pipeline is one item on the assistant's internal checklist. | Feature-driven PM thinking. "What page does the user go to?" is the wrong question. |
| 2 | **Typed everything** | Every event, input, output, and data item has a type. Every pipeline declares its input filter and output schema. | Free-form string plumbing. Opaque JSON blobs. Untyped LLM in/out. |
| 3 | **Source of truth is relational, projection is markdown** | The health graph lives in a structured relational/JSONB DB. The LLM's working memory is an auto-generated markdown wiki projected from the DB. Users see structured UI. The LLM sees prose. | Markdown-as-database. RAG-over-raw-documents as default. Schemaless vector stores as canonical. |
| 4 | **Two retrieval modes + a review loop. Similarity is rare.** | Fact (deterministic DB query) and typed filter (categorical navigation of the wiki). Similarity/RAG is a crutch for a poorly-maintained wiki — if the wiki is good, it's vestigial. The review loop (PR-style, human or LLM-as-reviewer, scheduled lint) is what keeps the wiki correct, not a similarity fallback. | Defaulting to embeddings for deterministic queries. Using RAG as a patch for knowledge-graph rot. Treating similarity as the safety net. |
| 5 | **Eval-first pipeline contract** | No pipeline ships without an eval suite, a retirement criterion, and a declared tier (free/premium/partner). Pipelines are disposable. | One-off prompts that nobody monitors. Pipeline sprawl without quality gates. Pipelines that can't be retired. |

### The pipeline contract

Every pipeline in the Care Brain declares:

| Field | Type | Example |
|---|---|---|
| `name` | identifier | `check_medication_interactions` |
| `trigger` | event type(s) | `profile.updated` where `changed_fields` includes medications |
| `input_filter` | typed query over the health graph | "current medications; prescriptions in last 30 days; known allergies" |
| `context_mode` | fact / filter / similarity | fact (deterministic lookup) |
| `processor` | deterministic / LLM / hybrid | hybrid — deterministic drug-interaction DB + LLM to compose explanation |
| `output_type` | typed schema | `InteractionFlag { severity, explanation, sources, suggested_question_for_doctor }` |
| `tier` | free / premium / partner | premium |
| `eval_suite` | reference to eval set | `evals/medication_interactions/*.yaml` |
| `retirement_criterion` | when to sunset | "replaced by EHDS native interaction service" |

This is a skill/tool contract, not an ML-model contract. Pipelines can be swapped, versioned, and composed without touching the orchestrator or UI.

### Retrieval: two modes, plus a review loop (not three modes with RAG as last resort)

Most "AI-native health app" attempts dump everything into embeddings and hope. Ditto does the opposite — and goes further than ranking similarity last. **With a well-maintained wiki projection, similarity is rarely needed at all.** Queries resolve via fact lookups in the DB or by navigating the wiki's entity/concept pages and backlinks. Similarity/RAG is a symptom of a knowledge graph that isn't being maintained.

| Mode | What it is | When to use | Example |
|---|---|---|---|
| **Fact (deterministic)** | SQL/structured query over the health graph. No inference. | Any question with a canonical answer in the graph. | "Current medications." "Last scan date." "Who are the doctors on this journey?" |
| **Typed filter (via wiki)** | Navigate the wiki by entity, concept, tag, or backlink. Read the relevant pages into context. | Any question that maps to entities/concepts the wiki already indexes. | "Everything about this diabetes diagnosis." "All conversations about medication changes." |
| ~~**Similarity (RAG)**~~ | ~~Vector search over text chunks~~ | **Demoted.** Only allowed as an explicit escape hatch when both fact and filter fail AND the wiki is known to have a coverage gap. Every use is logged and should trigger a lint task to close the gap. | Open-ended prose search over truly unstructured user-generated content that hasn't been categorized yet. |

**The quality loop (in place of RAG as a crutch)**:

Borrowed from Karpathy's lint pattern, adapted: the wiki is reviewed on a cadence — by the LLM itself (scheduled self-lint) and, for high-stakes pages (conditions, medications, care team), by a reviewer. PR-style: diffs to the wiki are reviewable, not silent. Contradictions get flagged. Orphan pages get surfaced. Stale claims get updated. This is the mechanism that keeps the wiki trustworthy — and it's what makes similarity unnecessary.

Every pipeline declares its mode(s). Every log line records the mode used. When a pipeline reaches for similarity, it creates a backlog item to extend the wiki schema so next time the query resolves via fact or filter. The goal is to monotonically reduce similarity's usage over time.

### The wiki projection layer

The structured health graph is the source of truth. The LLM does not read the graph directly. It reads a **living markdown wiki** that is auto-generated and incrementally updated from the graph.

Why both layers?

| Layer | Consumers | Mutability | Purpose |
|---|---|---|---|
| **Health graph (DB)** | Pipelines, app UI, user edits, partners (via API) | Mutable via pipelines and user actions; versioned; audit-logged | Canonical, queryable, UI-bindable |
| **LLM wiki (projection)** | LLM pipelines (as context) | Auto-regenerated or incrementally patched; never user-edited | Dense, readable prose; cross-referenced; compounds over time |

The wiki has entity pages (one per doctor, one per condition, one per medication), concept pages (one per major treatment decision), a timeline/log, and an index. When a pipeline runs, the orchestrator assembles context by pulling the relevant wiki pages plus fact-mode queries. The LLM reads the wiki. It does not re-derive the patient's story from raw transcripts every time.

This is Karpathy's pattern, corrected for a consumer product: **Yuri was right that markdown cannot be the source of truth — users and deterministic logic modify data.** The wiki is a projection. The DB is canonical.

### Data flow diagram

```
                         Inputs
     ┌────────────────────────────────────────────────┐
     │  recordings · documents · voice notes · labs   │
     │  sensor data · messages · calendar · shares    │
     └────────────────────────────────────────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │    Event Bus             │  ← typed events
              │    (14 event types)      │
              └─────────────────────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
         Pipeline A    Pipeline B    Pipeline N
        (plugin)       (plugin)     (plugin)
          │              │              │
          │  each: trigger, input_filter, processor,
          │  output_type, tier, eval_suite
          │              │              │
          └──────────────┼──────────────┘
                         ▼
              ┌──────────────────────────┐
              │   Health Graph (DB)       │  ← source of truth
              │   versioned + audit log   │
              └──────────────────────────┘
                         │
                         ▼
              ┌──────────────────────────┐
              │   LLM Wiki Projection     │  ← living markdown
              │   entity/concept/log      │
              │   auto-maintained         │
              └──────────────────────────┘
                         │
                         ▼
              ┌──────────────────────────┐
              │  Composed Surfaces        │
              │  summary · timeline ·     │
              │  share preview · prep     │
              │  briefing · dashboard     │
              └──────────────────────────┘
```

### What becomes cheap that was expensive

| Historically expensive | With this architecture | Consequence |
|---|---|---|
| Adding a new AI job (prompt, plumbing, eval, UI glue) | One new pipeline definition + eval suite + optional surface card | 40th job-to-be-done is cheap, not prohibitive |
| Maintaining context across sessions | Wiki projection compounds automatically per pipeline run | Longitudinal memory is free |
| A/B testing prompts | Pipeline version swap in config | Prompt eng iteration is hours, not days |
| Adding new input modality | New event type + new input filter | Voice, wearable, EHDS data ingest all slot in |
| Monetization changes | `tier` field on each pipeline | Premium unlocks are config, not code |
| Audience adaptation (partner, daughter, friend) | `adapt_worker` with `viewer_role` | No new pipeline per audience — one pipeline with role parameter |

### What's already canonical in direction-c-nervous-system.md

The following is locked in and not re-derived here. This synthesis respects it and builds on it.

**Events (14 types)**: `recording.completed`, `document.uploaded`, `voice_input.received`, `summary.viewed`, `suggestion.tapped`, `question.asked`, `appointment.approaching`, `profile.updated`, `circle_member.added`, `summary.created`, `answer.generated`, `circle.notified`, `profile.conflict_detected`, `prep.generated`.

**Pipelines (8)**: Process Recording, Answer Question, Process Document, Process Voice Input, Generate Viewer Suggestions, Generate Appointment Prep, Generate Circle Welcome, Detect Profile Changes.

**Workers (9)**: `summarize_worker`, `extract_worker`, `explain_worker`, `suggest_worker`, `answer_worker`, `adapt_worker`, `prep_worker`, `detect_changes_worker`, `translate_worker`. Model assignments (Sonnet for reasoning, Haiku for extraction/translation) as specified.

**Health Profile Store**: versioned JSON schema with audit log, conflict resolution, deterministic merge rules.

**The additions this synthesis proposes**:
- Generalize the 8 fixed pipelines into a plugin framework that supports N future pipelines (Tier 2–4 pipelines in Section 5 are the growth)
- Add the wiki projection layer as a first-class component
- Add the three-mode retrieval discipline as a design rule
- Formalize the pipeline contract (including the `tier` and `retirement_criterion` fields)

Jan Koum would approve: this is the minimum architecture that supports the maximum product surface. Not ambitious for a 10-person team when done right. Catastrophic when done wrong.

---

## 3. The Assistant's Checklist — 40+ Jobs-To-Be-Done

### Framing

From the Yuri conversation: *"Stop thinking in features. Think as the personal assistant. What's on my internal checklist?"*

If you hired a brilliant, tireless assistant dedicated to one patient and the people who love them, this is what would be on their clipboard. Each item is a job-to-be-done. Each one maps to a pipeline (or set of pipelines). The architecture of Section 2 is what makes all 40+ of these affordable to run concurrently for a million users.

Pain level: 1 (mild annoyance) to 5 (existential). Frequency: rare / event-based / weekly / daily / always. Complexity: XS (a prompt) / S (a simple pipeline) / M (a pipeline + data schema) / L (multi-pipeline orchestration).

### Theme 1: In-the-moment (during/just-after the appointment)

*Whose pain? Mara (68, oncology) the hardest. She is overwhelmed and exhausted when she walks out of the room.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 1 | Capture everything the doctor said, in the patient's language | Nobody (memory) | 5 | event | summarize_worker | free | S |
| 2 | Surface what the patient missed in the moment | Nobody | 4 | event | prioritize_deltas_vs_history (new) | premium | M |
| 3 | Anticipate the 3 questions the patient is already wondering | Patient (internally, often unresolved) | 4 | event | suggest_worker | free | S |
| 4 | Give grounded answers without re-Googling | Patient (ChatGPT, Google) | 4 | event | answer_worker | free | S |
| 5 | Name the action items the doctor mentioned | Patient (hopefully) | 4 | event | extract_worker | free | S |
| 6 | Flag anything the patient needs to do in the next 24 hours | Nobody | 4 | event | extract_worker + urgency_tagger (new) | free | S |

### Theme 2: Memory & continuity (across visits, years)

*Whose pain? Jan (74, multi-condition) the hardest. Five doctors, no one holds the whole picture.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 7 | Keep the patient's medication list current, sourced, and correctable | Patient (poorly) | 5 | always | extract_worker + Health Graph | free | M |
| 8 | Track every doctor on the patient's care team | Nobody | 3 | always | extract_worker + Health Graph | free | S |
| 9 | Maintain a timeline of the patient's health journey | Patient (fragmented) | 4 | always | journey_timeline_worker (new) | premium | M |
| 10 | Remember what the patient mentioned but the doctor didn't address | Nobody | 4 | event-based | unresolved_concerns_worker (new) | premium | M |
| 11 | Detect recurring symptoms across visits that the patient may not see | Nobody | 5 | weekly | scan_recurring_symptoms (new) | premium | L |
| 12 | Carry open questions from last visit into prep for the next | Patient (forgets) | 4 | event-based | prep_worker | free | M |
| 13 | Track which labs / scans are overdue | Nobody (except GP's notebook) | 4 | weekly | overdue_tasks_worker (new) | premium | M |

### Theme 3: Cross-doctor coordination (fragmentation repair)

*Whose pain? Pieter (45, caregiver for wife with MS) the hardest. Multiple specialists, no one coordinates.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 14 | Detect drug interactions across prescriptions from different doctors | Pharmacist (sometimes) | 5 | event-based | check_medication_interactions (new) | premium | L |
| 15 | Flag when two specialists give conflicting advice | Nobody | 4 | rare | detect_care_conflicts (new) | premium | L |
| 16 | Generate a cross-doctor summary for the GP | Patient (verbal) | 4 | event-based | gp_briefing_worker (new) | premium | M |
| 17 | Notice when a specialist referral wasn't followed up | Nobody | 4 | event-based | referral_tracking_worker (new) | premium | M |
| 18 | Catch when a medication was supposed to stop but is still being taken | Patient / pharmacist | 4 | rare | medication_lifecycle_worker (new) | premium | M |

### Theme 4: Relational (care circle, family sync)

*Whose pain? Aysel (52, managing own care + Turkish-speaking mother) and Corrie's son Henk (Corrie 81, cognitive decline).*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 19 | Write a partner-appropriate update of today's news | Patient (manually) | 5 | event | adapt_worker (partner mode) | premium | M |
| 20 | Write a daughter-appropriate update (different detail, softer framing) | Patient (manually) | 5 | event | adapt_worker (adult-child mode) | premium | M |
| 21 | Write a friend-appropriate one-liner | Patient (if at all) | 3 | event | adapt_worker (friend mode) | premium | S |
| 22 | Give each circle member a living dashboard of the patient's status | Nobody (WhatsApp chaos) | 5 | always | circle_view_worker (new) | premium | L |
| 23 | Let a circle member set "notify me if X changes" preferences | Nobody | 3 | always | circle_preference_worker (new) | premium | M |
| 24 | Translate the adapted update into a family member's language | Patient (manually) | 4 | event | translate_worker | premium | S |
| 25 | Coordinate who's going to which appointment | Group chat | 3 | event-based | appointment_coordination_worker (new) | free | M |

### Theme 5: Emotional & dignity

*Whose pain? All personas, in different forms. Especially Mara (after bad news) and Corrie's son (dignity for his mother).*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 26 | Detect when the appointment carried hard news and adjust tone | Nobody | 5 | event-based | emotional_context_worker (new) | free | M |
| 27 | Offer a "call someone" prompt after hard news | Nobody | 4 | event-based | support_prompt_worker (new) | free | S |
| 28 | Keep a record of the patient's own values and preferences | Nobody (sometimes advance directive) | 4 | always | preference_profile_worker (new) | premium | M |
| 29 | Give a cognitively declining patient a simpler surface | Family (manually) | 5 | always | cognitive_adaptation_worker (new) | premium | L |
| 30 | Advocate for the patient when they can't speak for themselves | Partner (sometimes) | 5 | rare | advocate_briefing_worker (new) | premium | L |

### Theme 6: Administrative & operational

*Whose pain? Everyone, but Aysel the working caregiver carries the most of it.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 31 | Remind the patient of upcoming appointments with prep | Patient (calendar) | 3 | weekly | appointment.approaching + prep_worker | free | M |
| 32 | Handle prior authorization paperwork | Patient + doctor's office | 5 | event-based | prior_auth_worker (new, agentic) | premium | L |
| 33 | Schedule follow-up labs / scans | Patient | 3 | event-based | booking_assistant_worker (new, agentic) | premium | L |
| 34 | Explain a lab result or scan report in patient language | Patient (Googles) | 4 | event-based | explain_worker | free | S |
| 35 | Navigate insurance questions | Patient (calls) | 4 | rare | insurance_navigator_worker (new) | premium | M |
| 36 | Track co-pays, receipts, claim submissions | Patient (poorly) | 3 | weekly | financial_tracker_worker (new) | premium | M |

### Theme 7: Preventive & self-education

*Whose pain? Not the hardest pain, but the highest leverage — preventing the next crisis.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 37 | Maintain a "what this condition means for me" page that grows with the journey | Patient (never) | 3 | weekly | condition_page_worker (new) | premium | M |
| 38 | Follow up proactively on doctor recommendations (diet, exercise, sleep) | Nobody | 3 | weekly | lifestyle_followup_worker (new, agentic) | premium | M |
| 39 | Explain what a newly prescribed medication does in context of existing ones | Pharmacist (briefly) | 4 | event-based | medication_explainer_worker (new) | free | S |
| 40 | Offer questions to ask based on what the patient seems confused about | Nobody | 4 | event-based | suggest_worker (extended) | free | S |
| 41 | Connect to evidence / guidelines without giving clinical advice | Patient (Googles, gets scared) | 4 | event-based | evidence_pointer_worker (new) | premium | M |

### Theme 8: Data rights & sovereignty

*Whose pain? Low today, high in 18 months as EHDS goes live. Positions Ditto ahead.*

| # | Job | Who does it today | Pain | Freq | Pipeline(s) | Tier | Complexity |
|---|---|---|---|---|---|---|---|
| 42 | Pull the patient's health record from any EU provider (EHDS) | Nobody (not possible today) | 4 | rare | ehds_ingest_worker (new) | premium | L |
| 43 | Let the patient correct errors in their own record | Patient (in theory) | 4 | rare | correction_request_worker (new) | premium | M |
| 44 | Let the patient export their Ditto data | Nobody | 3 | rare | export_worker (new) | free | S |
| 45 | Let the patient share their record with a new provider | Patient (manually) | 4 | event-based | provider_share_worker (new) | premium | M |

**Total: 45 jobs.** Not 40. Not 50. Forty-five, across the full adult patient journey. Each one is a pipeline declaration plus an eval suite plus optional surfaces. Each one becomes cheap to add when the foundation in Section 2 is in place.

### The shape this implies

- Of the 45, only **~12 are free tier.** The rest form the premium/partner moat.
- Of the 45, **~20 require the wiki projection layer** (longitudinal memory) to be meaningful.
- Of the 45, **~7 are agentic** (follow-through, booking, paperwork) — these are the Sam Altman unlock.
- **~30 are currently done by nobody.** Ditto's TAM is not "better than ChatGPT at summarization." It is "doing jobs nobody is doing for a person who needs them done."

---

## 4. The Magic Map — 20+ Wow Moments

### The magic formula

From magic-experience-vision.md, re-stated here because it governs every moment below:

1. **Removal** — remove a step the user assumed was their job
2. **Articulation** — put language on a vague feeling the user already had
3. **Anticipation** — happen before the user asks

Every wow moment in this catalogue can be explained as one or more of these three ingredients. If you can't explain a moment in those terms, it's not magic. It's a feature.

### The 22 moments, by category

#### Category A: In-the-moment (during or just after the appointment)

**1. The Share That Writes Itself** *(the keystone)*

Scene: Leila, 55, just heard her MS is progressing to secondary progressive. She needs to tell her husband, her daughter in London, and her employer. She taps Share. Three preview cards: full detail for husband, softer framing for daughter, one-liner for employer. Three taps.
- Ingredients: removal (no message composition), anticipation (knows the relationships)
- Pipelines: `adapt_worker` (per viewer_role), `translate_worker` if needed
- JTBD: 19, 20, 21
- What must be removed: detail-level dropdown, checkbox lists, "edit message" friction
- Missionary line: *"It wrote the message to my daughter better than I could have. It even knew not to scare her."*

**2. The Summary That Caught What You Missed**

Scene: Mara leaves her oncology appointment. She opens Ditto in the lobby. The summary is already there. The third bullet: "Dr. de Jong mentioned switching from capecitabine to oxaliplatin due to Tuesday's scan results." Mara didn't hear that in the room. She was focused on whether the tumor grew.
- Ingredients: anticipation + articulation
- Pipelines: `summarize_worker` + `prioritize_deltas_vs_history` (new)
- JTBD: 1, 2
- What must be removed: the loading screen, the "processing" state, the tooltips — summary is just there
- Missionary line: *"It caught a medication change I completely missed. I didn't even hear the doctor say it."*

**3. The Question You Were Afraid to Ask**

Scene: Henk, 72, reads his diabetes summary. Below: a chip reading "What happens if I miss a dose?" He'd been wondering this for three appointments but felt embarrassed to ask his GP. He taps.
- Ingredients: anticipation, removal (no formulation)
- Pipelines: `suggest_worker` + `answer_worker`
- JTBD: 3, 4
- What must be removed: the text input as primary interaction — chips are the shape, text is the escape
- Missionary line: *"It knew exactly what I was worried about. I didn't have to ask."*

#### Category B: Anticipatory (before the user thinks to check)

**4. The Living Briefing Before Every Visit**

Scene: Rina has a follow-up with her oncologist tomorrow. Ditto opens directly to a prep card — unprompted. "For your appointment with Dr. Visser: your last scan showed improvement. Two open questions from last time weren't answered. Your medication changed in February. Here are three questions you might want to ask."
- Ingredients: anticipation + articulation
- Pipelines: `prep_worker` triggered by `appointment.approaching`
- JTBD: 12, 31
- What must be removed: any button labeled "Prepare for appointment"
- Missionary line: *"I walked in prepared instead of panicked. It reminded me of a question from two months ago."*

**5. The Pre-Visit Pre-Brief to the Doctor** *(ambitious, Tier 3)*

Scene: Anna walks into her rheumatologist's clinic. The doctor glances at a structured update Ditto sent via the clinic's integration — not the transcript, a one-page brief: what changed since last visit, side effects reported, physio progress. The conversation starts two steps ahead.
- Ingredients: anticipation + removal (of the doctor's ramp-up time)
- Pipelines: `gp_briefing_worker` + provider integration
- JTBD: 16
- What must be removed: the friction of sending a PDF, the doctor's fear of patient-authored documents
- Missionary line: *"My doctor already knew what to ask. The whole appointment was more productive."*

#### Category C: Cross-doctor (the fragmentation repair)

**6. The Cross-Doctor Catch**

Scene: "Your cardiologist prescribed a beta-blocker on April 3. Your pulmonologist today mentioned starting you on something that interacts. They may not know about each other. Here's a summary to bring to your next appointment."
- Ingredients: articulation + anticipation
- Pipelines: `check_medication_interactions` + `gp_briefing_worker`
- JTBD: 14, 16
- What must be removed: anything that looks like a diagnosis — this is coordination, not medicine
- Missionary line: *"Ditto caught a drug interaction my doctors didn't. My pharmacist later confirmed it was real."*

**7. The Referral That Didn't Get Lost**

Scene: Eight weeks after a GP referral to a dermatologist, Ditto surfaces: "Your GP referred you to Dr. X in February. You haven't booked the appointment yet. Here are three slots near you next week."
- Ingredients: articulation + anticipation + removal (of scheduling friction)
- Pipelines: `referral_tracking_worker` + `booking_assistant_worker`
- JTBD: 17, 33
- What must be removed: the assumption that scheduling is the patient's job
- Missionary line: *"I forgot about that referral entirely. Ditto booked it for me."*

**8. The Medication That Should Have Stopped**

Scene: After 10 days on an antibiotic, Ditto notices the prescription's end date has passed. "You finished amoxicillin on April 10. Are you still taking it? If not, great — we'll mark it stopped in your profile."
- Ingredients: articulation + anticipation
- Pipelines: `medication_lifecycle_worker`
- JTBD: 18
- What must be removed: the assumption that the patient will update anything themselves
- Missionary line: *"It noticed I was still taking a pill I shouldn't have been."*

#### Category D: Relational (care circle)

**9. The Family Dashboard**

Scene: Sanne (daughter) opens Ditto. She doesn't receive a summary. She sees a living dashboard of her father's care: last visit, current meds, upcoming appointments, open action items, "things to ask next time." She stops calling him at 9 PM to interrogate.
- Ingredients: removal (the 9 PM call) + articulation
- Pipelines: `circle_view_worker`
- JTBD: 22
- What must be removed: the assumption that circle members are passive recipients of shares
- Missionary line: *"I stopped calling my dad to ask what the doctors said. I just open the app."*

**10. The Grandchild Who Got the Right Words**

Scene: Anna's 8-year-old granddaughter Liv gets a kid-friendly message: "Grandma's heart medicine is working well. She's doing great. She might be a bit tired this weekend, so extra hugs." The grandparents' shared care circle now includes children appropriately.
- Ingredients: removal (the "how do I tell a kid" pain)
- Pipelines: `adapt_worker` (child_mode — a new viewer_role)
- JTBD: 20
- What must be removed: any friction in adding a child to the circle safely
- Missionary line: *"Even my granddaughter gets an update she understands. And it's not scary."*

**11. The Translation That Didn't Scare Mom**

Scene: Aysel's mother (Turkish-only, 76) receives an adapted update about Aysel's scan results. The Turkish version is medically accurate AND gentle — not clinical, not alarming. Aysel, who has always translated everything herself, is relieved.
- Ingredients: removal (of the translation labor) + articulation (tone, not just words)
- Pipelines: `adapt_worker` + `translate_worker`
- JTBD: 20, 24
- What must be removed: the "raw translation" default — adaptation happens before translation
- Missionary line: *"I stopped being the translator in our family. Ditto does it better than I do."*

**12. The Circle-Member Signup Moment**

Scene: Sanne receives an adapted summary. It's so clearly written for her, without logos or "Powered by Ditto" branding, that she thinks: "I want this for myself." She taps "Want to stay updated on your father's journey?" → account created → two weeks later she records her own GP visit.
- Ingredients: removal (of the "health app" feeling in the shared message)
- Pipelines: `adapt_worker` + circle onboarding flow
- JTBD: 19, 22
- What must be removed: any branding that screams health tech
- Missionary line: *"I wasn't looking for a health app. But after seeing what my dad's looked like, I wanted one for myself."*

#### Category E: Reflective (looking back across time)

**13. The Pattern Nobody Saw**

Scene: After four GP visits over six months, a gentle card appears: "You've mentioned fatigue in your last three appointments. Each doctor prescribed something different. Worth raising whether these are connected."
- Ingredients: articulation (puts language on a vague feeling) + anticipation
- Pipelines: `scan_recurring_symptoms`
- JTBD: 11
- What must be removed: any hint of diagnosis — the restraint is the magic
- Missionary line: *"Three different doctors missed this. The app connected the dots."*

**14. The Journey Page**

Scene: Mara opens her "Journey" tab. A chronological, narrative page — generated, not templated — tells the story of her cancer journey to date: diagnosis, treatment decisions, medication changes, key moments. Her own story, back to her, in her voice.
- Ingredients: articulation (her life organized into meaning)
- Pipelines: `journey_timeline_worker`
- JTBD: 9
- What must be removed: the form feel — this is prose, warm, with her doctors named
- Missionary line: *"It gave me back my own story. I can hand this to any new doctor."*

**15. The "I've Been Heard" Moment**

Scene: Jan mentioned vertigo to his cardiologist. The cardiologist didn't address it. Two weeks later, Ditto surfaces: "You mentioned vertigo on April 2. Dr. Bakker didn't address it. Here's how to raise it next time."
- Ingredients: articulation + removal (patient doesn't carry the unaddressed concern in silence)
- Pipelines: `unresolved_concerns_worker`
- JTBD: 10
- What must be removed: the assumption that unaddressed = unimportant
- Missionary line: *"I thought I was imagining it being ignored. Ditto noticed too."*

#### Category F: Proactive / agentic (the AI that does, not just answers)

**16. The Follow-Up That Remembered**

Scene: Two weeks after a GP visit, Ditto sends: "Dr. Jansen asked you to reduce salt intake and check your blood pressure. Have you been able to measure it? If you share a reading, I can tell you if it's trending right."
- Ingredients: anticipation + removal (the "did I actually do that" anxiety)
- Pipelines: `lifestyle_followup_worker`
- JTBD: 38
- What must be removed: any feeling of being nagged — it's a caring colleague, not a reminder app
- Missionary line: *"It checked in on me two weeks later. I felt like it actually cared."*

**17. The Prior Authorization That Handled Itself**

Scene: Anna's rheumatologist wants to start a biologic. Ditto says: "Your insurance covers adalimumab with prior auth. I can start that process now if you like." She taps yes. Ditto handles the paperwork.
- Ingredients: removal (of the paperwork burden)
- Pipelines: `prior_auth_worker` (agentic)
- JTBD: 32
- What must be removed: the assumption that paperwork is the patient's job
- Missionary line: *"Ditto did the paperwork my doctor's office used to do. It arrived approved in a week."*

**18. The Appointment That Booked Itself**

Scene: Dr. Visser said "bloodwork in four weeks." Ditto, four weeks later: "You need bloodwork. Here are three labs near you with slots available this week. Want me to book one?"
- Ingredients: anticipation + removal
- Pipelines: `booking_assistant_worker` (agentic)
- JTBD: 33
- What must be removed: any "go to booking page" flow
- Missionary line: *"It booked my labs before I remembered I needed them."*

#### Category G: Self-educational

**19. The Condition Page That Grew With You**

Scene: Mara opens her "Colon Cancer" page. It's not a WebMD article. It's a page Ditto maintains for HER — her stage, her treatment plan, her medications, what her doctors have said across six visits, what questions she's asked, what remains open. A living wiki of her illness.
- Ingredients: articulation (her illness, organized) + removal (no Googling scary things)
- Pipelines: `condition_page_worker` (continuously maintained via wiki projection layer)
- JTBD: 37
- What must be removed: the generic medical info — this is her specific story
- Missionary line: *"There's a page about my cancer that only applies to me. Not the internet version."*

**20. The "What My Lab Result Means For Me"**

Scene: Jan's HbA1c came back at 7.2. He uploads the result. Ditto says: "This is slightly above your target of 7.0. It's up from 6.9 in January. In the context of the metformin dose increase, this isn't surprising yet. Dr. Bakker will likely want to discuss at your next visit."
- Ingredients: articulation + anticipation (the question he didn't know to ask)
- Pipelines: `explain_worker` with journey context from wiki
- JTBD: 34
- What must be removed: the generic "HbA1c = blood sugar average" explanation
- Missionary line: *"It explained my lab result the way my endocrinologist would, but with my history."*

#### Category H: Dignity & presence (the moments that matter most)

**21. The Cognitive Decline Companion**

Scene: Corrie, 81, opens Ditto on her iPad. The interface is extraordinarily simple — one card, one action, her son's name at the top. Her questions are pre-surfaced. Her answers are read aloud. Her son Henk sees the "full" dashboard.
- Ingredients: removal (of everything that confuses her)
- Pipelines: `cognitive_adaptation_worker` (UI generation for reduced cognitive load)
- JTBD: 29
- What must be removed: everything that isn't the one next action
- Missionary line: *"My mother can use this. Nothing else I've tried meets her where she is."*

**22. The Advocate When You Can't Speak**

Scene: Pieter's wife Lisa is hospitalized. She can't advocate for herself. Pieter opens Ditto and shows the staff a one-page brief — her current medications, known allergies, her documented treatment preferences, her neurologist's direct line. It's not a legal document. It's a care document. It's treated as one.
- Ingredients: articulation (her voice when she can't speak)
- Pipelines: `advocate_briefing_worker` using `preference_profile_worker` data
- JTBD: 28, 30
- What must be removed: the ambiguity about who Ditto speaks for — it speaks for the patient
- Missionary line: *"When my wife couldn't speak, Ditto did."*

### If we could ship only one

**#1: The Share That Writes Itself.** The argument is already laid out in magic-experience-vision.md. The three reasons hold: highest emotional leverage at lowest cognitive cost, only feature that makes one user into three, only moment that Big Tech cannot replicate in 12 months because it requires the care graph.

---

## 5. The Capability Milestone Map (NOT time-based)

Merlijn asked for no weeks, no sprints. This map is organized by **what unlocks what**. A team could sprint these in any order that respects the dependency graph. Timing is a separate decision.

### Tier 0: Foundation

**What this unlocks**: Nothing user-facing yet. Everything user-facing later.

**What must exist**:
- Pipeline plugin framework (Section 2 contract)
- Typed Health Graph (DB + schema + versioning + audit log)
- LLM Wiki projection layer (auto-maintained markdown from graph)
- Event bus + worker framework (Direction C already specifies this)
- Eval harness (shared infrastructure, reusable per pipeline)
- Three-mode retrieval utilities (fact, filter, similarity — ranked)
- Brand voice guide (the "Ditto voice" — one consistent tone)

**Proof of capability**: A new pipeline can be added end-to-end (trigger → filter → processor → output → eval) in under three days of engineering. Before this proof point, no Tier 1+ work should be committed to a roadmap.

**Whose problem is this**: Jan Koum's architecture discipline lens. The temptation is to skip Tier 0 because nothing ships to users. The discipline is to refuse to do so.

### Tier 1: Magic activation (the first wave of visible pipelines)

**What this unlocks**: The first real "oh wow" reactions. The initial care graph loop.

**What must exist**:
- Summary voice upgrade (no new pipeline, but a prompt-level investment in the `summarize_worker` to produce warm, doctor-attributed, emotionally honest summaries) — the first impression heartbeat
- `adapt_worker` (partner, daughter, friend modes)
- `circle_view_worker` (Family Dashboard)
- `translate_worker` (NL → EN, TR, AR, Papiamentu)
- `suggest_worker` + `answer_worker` (the Q&A loop from Phase 1 smart-suggestions)
- `extract_worker` + Health Profile Store (the foundation of memory)
- `prep_worker` (the Living Briefing)
- `check_medication_interactions` (the Cross-Doctor Catch)

**Wow moments unlocked**: #1, #2, #3, #4, #6, #9, #10, #11, #12

**JTBD covered**: ~15 of the 45

**Proof of capability**: Suggestion tap rate ≥ 20%. Adapted sharing uptake ≥ 15% of summaries shared. Circle Member Dashboard active users ≥ 30% of invited circle members. At least one cross-doctor interaction caught per 500 active patients in the first month.

**Whose problem is this**: Andy Puddicombe's first-impression lens. If the summary voice doesn't land, nothing else compensates.

### Tier 2: Compounding intelligence (the pipelines that use memory)

**What this unlocks**: The product starts to feel like it knows you. Switching cost becomes real.

**What must exist**:
- `journey_timeline_worker` (Moment #14)
- `scan_recurring_symptoms` (Moment #13)
- `unresolved_concerns_worker` (Moment #15)
- `condition_page_worker` (Moment #19)
- `medication_lifecycle_worker` (Moment #8)
- `referral_tracking_worker` (Moment #7 partial)
- `lifestyle_followup_worker` (Moment #16)
- `overdue_tasks_worker`
- Wiki projection layer mature (Tier 0 deepens here — entity pages become cross-referenced, log becomes query-able)

**Wow moments unlocked**: #7, #13, #14, #15, #16, #19

**JTBD covered**: +10 of the 45 (cumulative ~25)

**Proof of capability**: 90%+ profile accuracy after 3+ recordings. Patients with 6+ recordings show measurably higher retention than patients with ≤2. The Journey Page is the most-visited tab after Summary.

**Whose problem is this**: Daniel Ek's Discover Weekly lens. This is where the product becomes the reason to come back between appointments.

### Tier 3: Network & platform (the care graph activated, the partner channel)

**What this unlocks**: Real network effects. The B2B2C revenue model. The first non-NL market.

**What must exist**:
- Circle Member Dashboard mature (Tier 1 foundation extended to be a primary daily-active surface)
- `circle_preference_worker` (each member tunes what they get)
- `appointment_coordination_worker` (who's going where)
- Insurer partner surfaces (white-labeled or co-branded views for Menzis members, then replicated per insurer)
- B2B2C pipeline templates (onboarding, activation, outcomes reporting — all as pipelines on the same framework)
- Localization infrastructure (beyond translation — care system terminology, local insurance logic, local provider directory)
- First non-NL market pilot (Belgium or Germany)

**Wow moments unlocked**: #5 (doctor pre-brief, if provider integration is in scope), #17, #18

**JTBD covered**: +10 of the 45 (cumulative ~35)

**Proof of capability**: CNIS (circle-net-invitation-success) ≥ 40%. Circle-to-patient conversion ≥ 10%. Second insurer LOI signed. First non-NL market pilot live with measurable activation metrics.

**Whose problem is this**: Daniel Ek (network effects) + Sarah (B2B2C replication) + Sam Altman (agentic pipelines #17, #18 are unlocked at this tier).

### Tier 4: Data sovereignty layer (EHDS + provider integrations + portability)

**What this unlocks**: The TAM expansion. "Your health data is finally yours" becomes literal.

**Reality check on EHDS timing** *(validated April 2026)*: The EHDS Regulation entered into force 26 March 2025. Most provisions apply 24 months later — roughly H2 2026 — but this is the *certification and national-authority setup* phase. The actual cross-border exchange of priority health data (Patient Summaries, ePrescriptions) goes live in **March 2029** across all Member States. So Tier 4 is a readiness play for 2027–2029, not a 2026–2027 sprint. The strategic move is to be the first consumer-facing product certified to ingest EHDS data the moment national health data access services open, country by country, ahead of the 2029 cross-border milestone. Some national rollouts (NL, DE, FR) will precede the EU-wide deadline.

**What must exist**:
- `ehds_ingest_worker` (ingest patient's records from any EU provider, via national health data access services as they go live)
- `correction_request_worker` (patient corrections flow back to providers via EHDS)
- `provider_share_worker` (share record with any new provider in an EHDS-compliant format)
- `export_worker` (data portability)
- EHDS compliance + audit infrastructure
- Provider-facing brief surface (the "doctor pre-brief" receiver)

**Wow moments unlocked**: #5 (fully realized), #20 (deeper), plus a new class of "Ditto IS my health record" moments

**JTBD covered**: +10 of the 45 (cumulative 45/45)

**Proof of capability**: Ditto is one of the first consumer apps certified for EHDS patient data access in ≥2 EU markets (expect NL pilot first, DE to follow). ≥25% of patients have pulled at least one non-Ditto health record into their Ditto account.

**Whose problem is this**: Peter Thiel's "what's the secret?" lens. The secret is that EHDS will create a right without a product. The first consumer-facing product owns a generational opportunity — but the opportunity window opens gradually between late 2026 and 2029, not in one big bang.

### Dependency graph (what requires what)

```
Tier 0 ──► Tier 1 ──► Tier 2 ──► Tier 3 ──► Tier 4
  │          │          │          │          │
  │          │          │          └─► needs EHDS infra + second market
  │          │          └─► needs wiki projection mature
  │          └─► needs Health Profile Store populated
  └─► keystone; nothing else works without it
```

No tier can be sprinted before its dependencies are in place. Within a tier, pipelines can be parallelized. Some Tier 2 pipelines can begin in parallel with late Tier 1 (e.g., `journey_timeline_worker` can start as soon as the Health Profile Store has ~3 recordings per patient in the test cohort).

---

## 6. Founder Panel Commentary

Ten voices. Each reacts to the full synthesis above. What they love. What worries them. Their one prescription.

### Kevin Systrom — Product Vision (Instagram)

**Loves**: The keystone identification. Sharing-that-writes-itself as the filter moment. This is the photo-and-filter equivalent — one tap, the thing that makes it worth the app. **Worries**: Tier 1 still has eight pipelines. That's 8x more to launch than Instagram had on day one (one action: post a photo). Even this synthesis risks being too many things to too many people. **Prescription**: Inside Tier 1, pick the ONE pipeline that ships first in production. Not eight in parallel. One. The rest queue up behind the filter moment. Make that first pipeline so good it would embarrass us if any other team tried it.

### Andy Puddicombe — Trust & Brand Voice (Headspace)

**Loves**: The voice upgrade being explicit in Tier 1 before anything else. The cognitive decline moment (#21) and the advocate moment (#22). The word "AI" appearing nowhere in the user surface. **Worries**: The 45 JTBD list will tempt the team to ship quantity. But the first summary every new user sees is the entire relationship. Ship 10 pipelines with a mediocre voice and you have built 10 reasons for a cancer patient to distrust you. **Prescription**: The Ditto voice guide cannot be an afterthought in Tier 0. It's a deliverable, owned by one person, reviewed on every pipeline's output. Nothing ships if it doesn't sound like us.

### Jan Koum — Engineering Philosophy (WhatsApp)

**Loves**: The pipeline plugin contract. The explicit ranking of retrieval modes. The refusal to default to RAG. Privacy-native architecture. **Worries**: The 45-pipeline horizon is breathtaking for a 10-person team. Each pipeline carries maintenance cost forever. The eval harness had better be as good as the framework, or Tier 2 kills the company. **Prescription**: Before Tier 1 ships one pipeline, the shared eval harness must run end-to-end with a regression suite. No pipeline ships without evals. No pipeline ships without a retirement criterion. Say no to 30 of the 45 until the framework proves itself on 8.

### Daniel Ek — Platform & Growth (Spotify)

**Loves**: The care graph as the Discover Weekly. The Circle Member Dashboard as the daily-active surface. The tier mapping (premium = more pipelines unlocked). This is the right monetization architecture. **Worries**: The care graph is still mostly broadcast today — 50 invites/day on 35K users is not a network effect yet. Tier 3 assumes the network works. What if it doesn't? **Prescription**: Before Tier 2 ships in full, run the Circle Member Dashboard as a clickable prototype with 5 real caregivers. If the reaction is "I want this" then Tier 3 is validated. If it's "meh" then we have a graph problem, not a feature problem, and we reconsider before investing in Tier 2 memory work.

### Anton Osika — AI-Native Builder (Lovable)

**Loves**: The wiki projection layer. The generated-UI implication for the cognitive decline moment. Build-in-public potential for the adapted-share demos (Moment #1 is inherently shareable). **Worries**: The synthesis still respects the existing 8 pipelines as the starting point. That's conservative. A from-scratch 2026 product would not look like this. **Prescription**: Do a parallel experiment: a from-scratch, AI-native, no-legacy Ditto 2.0 prototype by one engineer + one designer for one week. Don't ship it. Just see what it teaches you about what the 10-person team is leaving on the table.

### Sarah (Composite Healthcare VC)

**Loves**: The capability tiers map clean to Series A proof points. Tier 1 done = product proven. Tier 3 proof-of-capability = Series A narrative. The unit economics still work. **Worries**: The doc is internal-facing and light on defensibility claims. For a Series A, the moat section needs to be bulletproof. Also: the kill list is good but too short for a VC's taste. **Prescription**: An external-facing derivative doc for the raise. Same spine, but the moat argument (care graph + longitudinal memory + regulatory moat) carries 30% of the weight. Include the EHDS opportunity explicitly as the Tier 4 land-grab story.

### Jony Ive — Emotional Object Design

**Loves**: The advocacy moment (#22). The grandchild moment (#10). The "what must be removed" field on every wow moment — that discipline is the difference between a feature and a product. **Worries**: Many of the magical moments risk being reduced to "card plus toast" in implementation. The visual language has to carry the emotion the prose promises. **Prescription**: Pick three wow moments — #1, #2, #22 — and design them as complete emotional objects, down to the microcopy, the haptic, the typography, the timing of the card appearing. Let that design language propagate. Don't ship a single moment that hasn't been held to that standard.

### Peter Thiel — The Contrarian Secret

**Loves**: The rejection of the general-purpose chatbot surface. The naming of the 30+ jobs that nobody is doing. The framing of Ditto as the open assistant for health, not "health app with AI." **Worries**: The synthesis is still patient-first in framing. The contrarian secret I identified earlier — that the caregiver is the underserved customer — is present in Tier 3 but not prioritized in Tier 1. **Prescription**: Treat Tier 1's Circle Member Dashboard as the keystone alongside adapted sharing. The secret is that the daughter pacing in the hallway pays first, stays longest, and recruits the most. Build for her with the same intensity as for the patient.

### Sam Altman — AI-Native Horizon

**Loves**: The agentic pipelines (#17, #18, #16) as Tier 2/3. The wiki projection compounding. The retreat from "AI as crude oil, we're the refinery" in favor of "AI is a brain, we're building its memory and agency for healthcare." **Worries**: The capability map underestimates how fast the underlying models will collapse current assumptions. Some pipelines you're planning to build will be a single API call in 12 months. **Prescription**: Set a quarterly ritual: for each planned pipeline, ask "what does the best frontier model do out of the box now?" Retire anything that's been commoditized. Move the engineering budget to the pipelines that remain genuinely defensible — which will almost always be the ones that depend on the care graph or the longitudinal wiki.

### Yuri — Pragmatic Engineer (Granola conversation)

**Loves**: The plugin contract explicitly. The fact/filter/similarity ranking. The explicit acknowledgment that DB is source of truth and wiki is projection. **Worries**: Two pipelines already consume meaningful team time. Forty-five pipelines without disciplined infrastructure is a death spiral. The synthesis should not be read as "we will build 45 pipelines." **Prescription**: Publish a ceiling — the team never maintains more than N active pipelines at once, where N is a function of team size. Retire old ones when new ones ship. The 45-JTBD list is the horizon, not the backlog. The backlog is 8–12 at any given time.

### Andy Grove (Composite — the sober operator)

*(An extra voice, not part of the original panel, added because the others are strategy-heavy and this synthesis needs an execution reality-check.)*

**Loves**: The flat, non-timed structure of the synthesis. The refusal to over-plan delivery. **Worries**: Strategy-without-execution documents rot on shelves. This one needs a companion that names one person as accountable for each Tier 0 foundational piece, and a weekly rhythm to review whether Tier 0 is still on track. **Prescription**: Produce a one-pager, adjacent to this doc, that names: (a) the person accountable for each of the seven Tier 0 components, (b) the review cadence, (c) what "done" looks like for each. Don't let the strategy be the thing that feels done.

---

## 7. Cross-Cutting Concerns

These apply across every pipeline and every tier. They're not sections of the product — they're the shape of everything.

### Eval-first discipline

Every pipeline ships with: an eval suite (synthetic test cases with ground truth), a regression test (runs on every prompt change), a monitoring dashboard (accuracy, latency, cost per call), and a retirement criterion. The shared eval harness is built once in Tier 0. Every new pipeline inherits it. A pipeline that would slow the eval suite below CI speed is refactored, not shipped.

### Trust architecture

Source attribution on every artifact ("From your appointment with Dr. Jansen on April 4"). Confirmation flows before any profile mutation. Medical humility in every answer ("For medical advice, contact your care team"). The word "AI" appears nowhere user-facing. The voice is consistent across 45 pipelines because the voice guide is a living document owned by one person.

### Privacy, GDPR, EHDS as strategic asset

EU-born compliance is a moat. Data never leaves the EU. Every pipeline has a declared data-minimization spec. Every circle share has explicit consent. EHDS compliance is designed in from Tier 4 architecture, not retrofitted. This is marketing copy, not just compliance: *"Your health data stays in Europe. Your doctor's words stay between you and the people you choose to share them with."*

### Brand voice consistency

The "Ditto voice" guide covers: pronouns, medical disclaimer phrasing, emotional register (warm, clear, never cheerful in a hard moment), the rule against single em dashes, the rule that the word "AI" never appears, the rule that every claim is sourced, the rule that treatment advice is always deferred to the care team. Every pipeline's output is reviewed against this guide before the pipeline is promoted.

### Monetization tier mapping

Free tier: the first 3 recordings/month, basic summary, basic Q&A, basic sharing, basic health profile. Premium (EUR 7.99/mo): unlimited recordings, cross-doctor checks, pattern detection, proactive follow-up, adapted sharing per audience, family dashboard, condition pages. Family (EUR 12.99/mo): premium + multi-patient (follow multiple journeys). Partner tier (B2B2C, €0.50-1.00 PMPM): insurer-white-labeled access for all their members to premium-equivalent functionality, revenue-shared with Ditto.

Every pipeline declares its tier. Changing tiers is config, not code.

### Accessibility & elderly usability

The heuristics from the MVP spec remain canonical: 16pt+ body, 44pt+ tap targets, one primary action per screen, plain language (Flesch ≥ 60), no gesture beyond tap and scroll, VoiceOver compatibility. Every pipeline's output surface passes the 10-point heuristic checklist. The Corrie test (Moment #21) is the compass: if she can't use it, redesign.

### Offline and degraded mode

Every pipeline declares its degraded behavior. If `summarize_worker` fails, the raw transcript is saved and the user sees "We're still processing your recording." If `adapt_worker` fails for one circle member, the others still go. If the model API is down, the app shows the last good state. The system never hides failures silently.

### Multi-language

NL (Dutch) is the home language. EN for international users. TR (Turkish) and AR (Arabic) for significant NL immigrant communities. Papiamentu for Dutch Caribbean. Each language has its own eval set for medical term accuracy. `adapt_worker` is language-aware, and adaptation happens before translation, not after — so the adapted tone is preserved across languages.

---

## 8. Kill List & Non-Goals

What Ditto is explicitly NOT building. Every item includes: what it is, why we're not, what would have to change for us to reconsider.

| Not building | What it is | Why not | Reconsider if... |
|---|---|---|---|
| **General-purpose health chatbot wrapper** | A "Ditto Assistant" that answers any health question | That's ChatGPT Health. We lose on distribution and model capability. Our ceiling is specificity, not generality. | Never. This is structurally wrong for us. |
| **Clinical decision support** | Telling the doctor what to do, flagging diagnoses, suggesting treatment | Regulatory/liability bomb. Also not the patient's job. Also not our moat. | Never within our current risk posture. |
| **Real-time in-appointment coaching** | Live AI intervention during the doctor-patient conversation | Destroys the doctor-patient relationship. Consent minefield. Not magic — invasive. | If multiple care partners and regulators independently validate a narrow use case, maybe. Not for v1 or v2. |
| **US market entry** | Consumer Ditto in the US | Crowded (ChatGPT Health, Copilot Health, Hippocratic). US healthcare is structurally different. EU market is empty and has EHDS tailwinds. | If EU expansion to 3+ markets succeeds AND a clear US partnership (insurer, health system) emerges. |
| **B2B SaaS to providers** | Clinical documentation tool for doctors' offices | That's Ambience, Abridge, Nuance DAX. They have $3B+ funding. We lose. Also: different product entirely. | Never in the core product. A separate product line, maybe, but not now. |
| **Wearable hardware** | Ditto-branded devices | We are a software company. Hardware is a distraction that will consume 3x the engineering headcount. | Never. Could partner with Apple/Oura/Whoop for data ingest. |
| **Early home-monitoring integrations** | Ingesting continuous glucose monitors, blood pressure cuffs, etc. | Not yet. Tier 4 or later. The first-order JTBD list doesn't need this, and it's engineering-heavy. | When 5+ Tier 2 pipelines are mature and partner ingest is validated through EHDS. |
| **Open API for third-party pipelines** | Letting external developers build pipelines on our platform | Security and brand nightmare. Every external pipeline could speak in our voice, leak patient data, or hallucinate. | After 3+ years of internal pipeline discipline and a carefully selected partner program. |
| **Generic medical information content** | Publishing health education articles | Not our game. Our content is specific to the patient. Generic content is ChatGPT Health / WebMD territory. | Never as a primary product. |
| **Social feed / community features** | Patient discussion forums, comment threads | Different product. Different moderation burden. Different trust model. | Never in the core product. |
| **Appointment prep as a standalone primary feature** *(reversing magic-vision's earlier kill)* | *(Note: magic-vision recommended killing prep. This synthesis keeps it but demotes it — it lives in Tier 1 as a pipeline, not a banner feature. The kill decision was too strong.)* | Prep has real value but is not top-tier magic. Don't market it. Build it. Let it surface contextually. | — |

---

## 9. Risks & Mitigations

### Strategic

| Risk | Probability | Magnitude | Leading indicator | Mitigation |
|---|---|---|---|---|
| Summarization commoditizes before Tier 1 ships | H | H | Apple or Google announces native voice summarization in Health app | Speed. Tier 1's sharing moment is the defensive move. The summary itself stops being our moat the day it becomes native. |
| Big Tech adds care circle features | L in 18 mo, M in 24 mo, H in 36 mo | Extreme | Apple or Google shipping a "share health with family" primitive | Ditto's care graph density is the defense. If we own the graph before they build the primitive, the primitive is a feature; our graph is still a moat. |
| **Anthropic's Claude for Healthcare evolves toward consumer** | L-M in 12 mo, M in 24 mo | H | Anthropic ships patient-facing UI or EU integration on top of Claude for Healthcare | Claude for Healthcare launched March 2026 as a foundation/API play, not a consumer product. The risk is if Anthropic pivots toward direct-to-patient. Our defense is the same as against other Big Tech: care graph + EU compliance + specificity. Uniquely awkward if we use Claude models for our pipelines — consider hedging with multi-model strategy. |
| Menzis activation fails | M | H | Menzis member conversion to active users <1% after 6 months of promotion | B2C growth becomes the pull. Prove product-market fit with patient-paid channel before relying on B2B2C. |
| Care graph stays theoretical (never becomes a true network effect) | M | H | Circle-to-patient conversion <5% after Tier 1 ships | Circle Member Dashboard is the mechanism that converts broadcast to graph. If it fails, the moat thesis is wrong. Circle Dashboard prototype must be validated before Tier 3. |
| Second EU market pilot stalls | M | M | Belgium or Germany pilot at <10% activation of targeted insurer partner's members | Halve the country scope (one region, not whole country). Partner with one insurer, not a regulator. Learn before scaling. |

### Execution

| Risk | Probability | Magnitude | Leading indicator | Mitigation |
|---|---|---|---|---|
| Pipeline maintenance cost scales linearly and kills velocity | H if no discipline | H | Eval run time > 1 hour. New pipeline delivery time > 2 weeks. Bug count per pipeline growing. | Shared eval harness as Tier 0 non-negotiable. Pipeline retirement criterion. Ceiling of N active pipelines per team size. |
| Eval debt accumulates | M | H | Eval coverage ratio dropping. Regression catches dropping. Team treating evals as optional. | Eval-first rule is cultural, not optional. No pipeline ships without evals. Merlijn or CTO blocks merges that violate. |
| Team burnout | M | H | Sprint velocity dropping. Ticket-to-PR time rising. Morale complaints in 1:1s. | The 45-JTBD list is the horizon, not the backlog. At any time, 8–12 pipelines are active. Say no clearly. |
| Voice drift across pipelines | M | M | User feedback says "sounds different lately." Brand team flags inconsistency. | Voice guide owner reviews every new pipeline's output. Voice is evaluated in every eval suite. |
| Scope creep via stakeholder requests | H | M | Ad-hoc pipeline requests hitting the team without going through the JTBD list | Requests must map to a JTBD or be rejected. The JTBD list is the surface area. |

### Product

| Risk | Probability | Magnitude | Leading indicator | Mitigation |
|---|---|---|---|---|
| Adapted sharing flops | M | Very H | Share preview generated but not sent. Circle member tap-through <30%. | Wizard-of-Oz test with 20 real patients before shipping. If reaction isn't "missionary," rework the adaptation prompt. |
| Summary voice misses the emotional target | M | Very H | NPS on summary screen stagnant. Qualitative feedback neutral ("it's fine"). | Tier 0 includes voice guide. Tier 1 summary voice upgrade is a dedicated investment, not a side effect. A/B test voice variants. |
| Suggestion tap rate stays below 20% | M | H | Engagement instrumentation shows flat tap rate after 2 weeks of production | Suggestion generation prompt is the highest-leverage tuning target. Weekly iteration on the prompt + eval suite. |
| Patients don't trust cross-doctor pipelines | M | H | Cross-doctor catch fires but users don't act on it. "This isn't my doctor's job" feedback. | The messaging frames Ditto as bringing the patient information, not intervening. Restraint is the discipline. |
| Translation quality degrades in sensitive contexts (cancer, palliative) | M | Very H | Native-speaker reviewer flags emotional or medical errors in TR, AR outputs | Language-specific eval sets with native reviewers. Sensitive-context detection triggers extra review. |

### Regulatory

| Risk | Probability | Magnitude | Leading indicator | Mitigation |
|---|---|---|---|---|
| Medical hallucination incident gets publicized | M (decreasing with discipline) | Extreme | Any eval-suite regression on grounding. Any user-reported hallucination. | Grounding rules in every prompt. Source attribution mandatory. Eval suite checks grounding on every change. Crisis comms plan ready. |
| GDPR enforcement action | L | H | Regulator inquiry on a specific pipeline or data flow | EU-first compliance posture. DPA with every partner. Data-minimization spec per pipeline. |
| EU AI Act reclassifies a pipeline as high-risk | M | H | Regulatory consultation on medical AI | Our framing (understanding what was said, not medical advice) is positioned to stay outside high-risk category. Legal review per new pipeline if it moves toward advice. |
| EHDS timeline slips | H | M | Official EU communications on timeline | Don't bet Tier 4 on specific dates. Build for when it goes live. Be ready within 60 days of go-live. |

### The biggest risk nobody is watching

**The team ships it, and it works, and it doesn't feel different enough.** The summary is better. The Q&A is useful. The sharing works. But the user reaction is "nice" rather than "I can't live without this." This is the failure mode where every execution metric passes and the thesis fails. The discipline against it is the "missionary line" on every wow moment: if a user couldn't say it, the moment isn't there yet. Don't ship magic that doesn't move someone.

---

## 10. Open Questions

Strategic forks that remain unresolved. Each has: what's unknown, what would resolve it, who decides.

**Q1 — Keystone for Tier 1**
What's unknown: Inside Tier 1, which pipeline ships first in production? Adapted sharing (emotional peak) or the Q&A/summary voice upgrade (first-impression foundation)?
What would resolve it: Kevin's prescription — pick the one that would embarrass us if another team did it better. Validate with a 10-patient wizard-of-Oz test of adapted sharing.
Who decides: Merlijn + CPO (if any).

**Q2 — Circle Dashboard timing**
What's unknown: Does the Circle Member Dashboard ship inside Tier 1 (alongside adapted sharing) or wait for Tier 3? Earlier means more engineering spend on a non-core-user; later risks the graph staying broadcast.
What would resolve it: 5-caregiver prototype test. If reaction is "I want this now," ship in Tier 1.
Who decides: Merlijn + design.

**Q3 — EHDS as product or platform**
What's unknown: When EHDS goes live, do we build consumer-facing EHDS integration (Tier 4 ingest_worker) as our own consumer app, or expose it as a platform API for others?
What would resolve it: EHDS pilot data (who's ingesting from where, what friction points exist). Early 2027 decision.
Who decides: Merlijn + CEO-level.

**Q4 — Premium tier anchor**
What's unknown: Which wow moment is the premium conversion trigger? Cross-doctor catch? Adapted sharing? Follow-up agentic loop?
What would resolve it: A/B test: show three free users a teaser of each premium moment at the 3rd recording. Measure conversion intent.
Who decides: Product + growth.

**Q5 — Caregiver as primary customer**
What's unknown: Do we make the caregiver (daughter, partner) a first-class product design audience, or keep them as an adjacent user who shares with the patient?
What would resolve it: Peter Thiel's prescription. Explicit caregiver-first product test: one pipeline built with the caregiver as the primary user (e.g., `circle_view_worker` Tier 1). Measure caregiver-driven activation rate.
Who decides: Merlijn.

**Q6 — Provider-facing brief**
What's unknown: Moment #5 (doctor pre-brief) requires provider integration. Do we build for NL providers first (few integrations, trust-native) or wait for EHDS (standardized, but later)?
What would resolve it: Direct conversation with 3–5 Dutch specialists. If they'd receive a Ditto brief willingly, build. If not, wait for EHDS.
Who decides: Merlijn + partnerships.

**Q7 — Agentic boundary**
What's unknown: How far does Ditto go in Moment #17 (prior auth) and Moment #18 (booking)? "Draft the form and ask to send" or "send on the patient's behalf autonomously"?
What would resolve it: Risk/liability review. User preference research.
Who decides: Legal + product + Merlijn.

**Q8 — B2B2C pipeline surface area**
What's unknown: When Menzis (or another insurer) offers Ditto to their members, do they get the same free/premium tiers? A white-labeled branded surface? A lighter "insurer-lite" product?
What would resolve it: Menzis partnership evolution. Probably we ship white-labeled first, learn, then adjust.
Who decides: Partnerships + Merlijn.

**Q9 — Localization depth**
What's unknown: In Tier 3, do we prioritize Germany (biggest market, language barrier) or Belgium (small, similar healthcare, bilingual)?
What would resolve it: Commercial traction. BE is faster to prove; DE has more upside.
Who decides: Strategy + Sarah.

**Q10 — Voice guide owner**
What's unknown: Who owns the Ditto voice as a living, cross-pipeline artifact? Design? Content? Merlijn?
What would resolve it: Naming one person. Full stop. Otherwise it drifts.
Who decides: Merlijn.

---

## 11. What's Handled Later

This synthesis is intentionally the strategic layer. The following are explicitly out of scope here and handled in existing or future docs:

- **Delivery schedule** (week-by-week, sprint-by-sprint) → `care-brain-mvp-spec.md` handles the first 12 weeks; future execution plans handle beyond.
- **Feature-level UX specs** (screen flows, micro-copy, interaction patterns) → per-feature spec docs (e.g., `care-brain-phase1-smart-suggestions.md` is the template).
- **Prompt engineering details** (specific prompts, few-shot examples, evals) → `direction-c-nervous-system.md` has the current set; each pipeline's owner maintains the prompt + eval pair.
- **Team structure and hiring plan** → operational planning owned by CEO/founders.
- **Partnership commercial terms** → legal/partnerships.
- **Investor deck** → a derivative of this doc, tuned for Series A narrative.
- **Specific user research findings** → NotebookLM notebook + user-researcher agent.

If it's not in this doc and not in an adjacent doc, it's not yet canonical — flag it as a new Open Question.

---

## Final note

This synthesis is a thinking artifact, not a plan. The plan comes later. The value of this document is to ensure that when the plan is written, it's written against a coherent, contrarian, architecturally-sound vision — not against the default of "keep shipping summary features and hope the Series A reads like a unicorn."

The one line, one more time:

**Ditto is the open assistant for health — specialized, serious, and present for the people who love you.** Not a chatbot. Not a summarizer. An assistant with a 45-item checklist and the architecture to run it forever.

---

## Appendix: Validated Sources

Key external claims in this synthesis have been checked against public sources (April 2026). Where a claim in this doc is grounded in a prior internal doc (business-case.md, competitive-analysis.md) but not independently validated here, it's flagged with "◻" below.

| Claim | Source |
|---|---|
| OpenCode: open-source terminal AI agent, sst/anomalyco, 95K+ GitHub stars, Claude Code alternative | [opencode.ai](https://opencode.ai/) · [GitHub: anomalyco/opencode](https://github.com/anomalyco/opencode) · [DataCamp comparison](https://www.datacamp.com/blog/opencode-vs-claude-code) |
| Karpathy's LLM Wiki pattern, April 2026, 5K+ stars | [Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · [Karpathy on X](https://x.com/karpathy/status/2039805659525644595) · [VentureBeat summary](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) |
| Apple Project Mulberry scaled back Feb 2026, features to ship in iOS 26.4 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-05/apple-is-scaling-back-plans-for-new-ai-based-health-coach-service) · [9to5Mac](https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/) |
| ChatGPT Health launched Jan 2026, 40M daily / 230M weekly health queries | [OpenAI](https://openai.com/index/introducing-chatgpt-health/) · [TechCrunch](https://techcrunch.com/2026/01/07/openai-unveils-chatgpt-health-says-230-million-users-ask-about-health-each-week/) |
| OpenAI acquired Torch Health Jan 12, 2026 for $60-100M | [TechCrunch](https://techcrunch.com/2026/01/12/openai-buys-tiny-health-records-startup-torch-for-reportedly-100m/) · [CNBC](https://www.cnbc.com/2026/01/12/open-ai-torch-health-care-technology.html) |
| Microsoft Copilot Health launched March 12, 2026 (US first, 50+ wearables, 50K+ providers) | [Microsoft AI](https://microsoft.ai/news/introducing-copilot-health/) · [Fortune](https://fortune.com/2026/03/12/microsoft-copilot-health-ai-medical-personal-health-data/) |
| Anthropic Claude for Healthcare launched same week as Copilot Health (March 2026) | [SiliconAngle (via Microsoft Copilot Health coverage)](https://siliconangle.com/2026/03/12/microsoft-launches-copilot-health-help-consumers-understand-medical-data/) |
| Hippocratic AI $126M Series C at $3.5B, Nov 2025 | [BusinessWire](https://www.businesswire.com/news/home/20251103432446/en/) · [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-lands-126m-series-c-expand-patient-facing-ai-agents-fuel-ma) |
| EHDS Regulation entered into force 26 March 2025; most provisions apply H2 2026; cross-border Patient Summary exchange March 2029 | [EU Commission](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en) · [EY Greece](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds) |
| Menzis ~2M members, #3 insurer in Netherlands | [Dacadoo / Menzis partnership](https://www.dacadoo.com/news/dutch-health-insurer-menzis-launches-a-new-health-platform-including-apps-powered-by-dacadoo/) · [Menzis corporate site](https://www.menzis.nl/englishwebsite/) |
| Ambience Healthcare $243M Series C, ~$3B+ valuation (provider-facing) ◻ | Cited from [competitive-analysis.md](competitive-analysis.md); not independently re-validated here |
| b.well bailey (health AI SDK, used by OpenAI and Samsung, 350+ data sources) ◻ | Cited from [competitive-analysis.md](competitive-analysis.md); not independently re-validated here |
| CaringBridge ~900K patients, non-AI, broadcast format ◻ | Cited from [competitive-analysis.md](competitive-analysis.md); not independently re-validated here |

**What was corrected in this validation pass**:

1. Added **Anthropic's Claude for Healthcare** (launched March 2026) as a named competitor in Section 1 and as a distinct risk in Section 9. Previously missing.
2. **EHDS timing sharpened**: earlier language implied Tier 4 go-live in late 2026. The accurate picture is certification/national authority setup in H2 2026, actual cross-border exchange in **March 2029**, with national rollouts (NL, DE, FR) potentially preceding. Tier 4 repositioned as a readiness play for 2027–2029.
3. **Retrieval architecture simplified**: demoted similarity/RAG from first-class third mode to "explicit escape hatch." Added the wiki quality loop (PR-style review, human or LLM-as-reviewer) as the mechanism that makes similarity unnecessary. Per user's insight, and consistent with Karpathy's lint pattern.
4. **OpenCode confirmed as the correct reference** (the Granola transcript rendered it as "OpenClaw" / "OpenClob" — speech-to-text artifact). Real product: sst/anomalyco, 95K+ stars. Framing held.

**What remains unverified** and is worth a second pass:
- Ambience Healthcare's current valuation/funding state (competitive-analysis.md claimed $3B+)
- b.well bailey's actual partnership stack (claimed OpenAI + Samsung usage)
- CaringBridge's current user count (claimed ~900K)
- The claim that "nobody else is building audience-adapted health sharing for care circles" should be revalidated quarterly — this is the central differentiation claim.

---

Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
