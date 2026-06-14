# Care Brain MVP: The Nervous System

**Date**: 2026-04-08
**Status**: Design complete, pending review
**Author**: Merlijn van Breugel / Mewtwo
**Parent**: [Care Brain Strategy](care-brain-strategy.md) (approved)
**Architecture basis**: [Direction C: The Nervous System](direction-c-nervous-system.md)
**Timeline**: 12 weeks (6 sprints of 2 weeks)
**Approach**: Vertical slices with AI-first development and human review gates

---

## Product Vision

Build Ditto's AI backbone as an event-driven nervous system where every patient interaction feeds a living health profile, and every screen the patient sees has been touched by intelligence that knows their full context.

**One recording. The brain understands.** Patient records an appointment. Within seconds: a patient-friendly summary, contextual follow-up suggestions, an updated health profile, and the ability to ask grounded questions about what the doctor said. Between appointments: voice updates, document processing, appointment preparation. The brain accumulates knowledge and anticipates needs.

**For the patient, none of this is "AI."** It's Ditto understanding them. The interface feels like a knowledgeable friend who was at every appointment, not a chatbot they have to figure out.

---

## Scope

### In scope

| Pipeline | What it does | Existing work |
|---|---|---|
| **Process Recording** | Transcript → summary + health extraction + contextual suggestions | Existing summarization, Claude agent, fact extraction |
| **Answer Question** | Tap suggestion or type question → grounded answer from conversation context | New |
| **Process Voice Input** | "Tell Ditto" → extract health data → confirm with patient → update profile | Existing voice input prototype |
| **Process Document** | Photo of letter/lab result → plain-language explanation + extract to profile | New |
| **Appointment Prep** | Manual trigger → prep briefing with suggested questions + open items | New |
| **Sharing Adaptation** | Summary → audience-adapted preview per recipient role (patient-side only) | New |

### Out of scope

- Care Circle receiving end (no delivery infrastructure, no circle member app experience)
- Push notification delivery
- Calendar integrations (appointments entered manually)
- EHDS data ingestion
- Multi-language app UI (content translation only)
- End-to-end encryption for sharing

### Sharing clarification

The brain's adaptation capability is fully built. Patients can preview "What your partner would see" and "What your mother would see" in different languages. The adaptation and translation workers run for real. What's NOT built is the infrastructure to actually deliver these adapted messages to recipients. Patient-side only.

---

## Technical Architecture

### System overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        iOS App (SwiftUI)                        │
│  Summary View │ Profile Tab │ Voice Input │ Doc Capture │ Prep  │
└───────────────────────────┬─────────────────────────────────────┘
                            │ REST API + SSE
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Python Backend (FastAPI)                     │
│                                                                 │
│  ┌──────────┐  ┌──────────────┐  ┌───────────────────────────┐ │
│  │ Event Bus │  │ Pipeline     │  │ REST API Layer            │ │
│  │ (pub/sub) │  │ Orchestrator │  │ /recordings, /summaries,  │ │
│  │           │  │              │  │ /profile, /voice-input,   │ │
│  └─────┬────┘  └──────┬───────┘  │ /documents, /prep         │ │
│        │              │          └───────────────────────────┘ │
│        ▼              ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Worker Framework                        │  │
│  │  @worker(model="sonnet")  @worker(model="haiku")         │  │
│  │                                                           │  │
│  │  summarize │ extract │ suggest │ answer │ explain │ prep  │  │
│  │  adapt │ translate │ detect_changes                       │  │
│  └──────────────────────────┬───────────────────────────────┘  │
│                             │                                   │
│  ┌──────────────────────────▼───────────────────────────────┐  │
│  │              Health Profile Store (PostgreSQL)             │  │
│  │  profiles │ audit_log │ summaries │ answer_cache          │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
              ┌──────────────────────────┐
              │  Anthropic API (Claude)   │
              │  Sonnet 4 │ Haiku 3.5    │
              └──────────────────────────┘
```

### Key technical decisions

| Decision | Choice | Rationale |
|---|---|---|
| **Event bus** | In-process Python pub/sub | No external dependency for MVP. Production-ready interface so it can be swapped to Redis Streams later without code changes. |
| **Database** | PostgreSQL with JSONB | Profile store needs versioning, JSONB queries, and audit trail. SQLite for local dev, Postgres for deployed prototype. |
| **API framework** | FastAPI | Python ecosystem, native async, SSE support, auto-generated OpenAPI docs. |
| **LLM SDK** | Anthropic Python SDK | Direct, typed, streaming support. |
| **Model pinning** | Specific model versions | Prevents behavior changes from model updates. Pin in config, not in code. |
| **Caching** | In-memory dict for prototype, Redis interface for production | Answers and suggestions are deterministic per input. Cache aggressively. |
| **Image processing** | Claude Vision (no separate OCR) | Sonnet handles document photos directly. Simpler pipeline, one fewer dependency. |
| **Voice transcription** | Existing STT in prototype | Brain receives text, doesn't do STT. Integrate what's already built. |

### Event taxonomy

| Event | Trigger | Pipelines activated |
|---|---|---|
| `recording.completed` | Recording finishes processing | Process Recording |
| `document.uploaded` | Patient photographs a document | Process Document |
| `voice_input.received` | Patient uses "Tell Ditto" | Process Voice Input |
| `voice_input.confirmed` | Patient confirms voice extraction | Profile Update (step 4 of voice pipeline) |
| `summary.viewed` | Patient views a summary | (consumed by app) |
| `suggestion.tapped` | User taps a suggestion chip | Answer Question |
| `question.asked` | User types a custom question | Answer Question |
| `appointment.approaching` | Manual trigger (patient enters appointment) | Generate Appointment Prep |
| `summary.share_preview_requested` | Patient taps "Share" on a summary | Generate Sharing Preview |
| `profile.updated` | Health profile data changed | Detect Profile Changes |

Every event wraps its payload in a standard envelope with `event_id`, `event_type`, `timestamp`, `patient_id`, `source`, and `correlation_id`. The correlation_id traces an event through all downstream pipelines.

### Pipeline definitions

**Process Recording** (trigger: `recording.completed`)

```
recording.completed
  ├─ Step 1a: summarize_worker (Sonnet)    ─┐
  │                                          ├─ parallel
  └─ Step 1b: extract_worker (Haiku)       ─┘
  → Step 2: Profile merge (deterministic)
  → Step 3: suggest_worker (Sonnet)
  → Step 4: Detect changes (deterministic diff)
  → Emit: summary.created, profile.updated
```

| Step | Worker | Model | Failure behavior |
|---|---|---|---|
| 1a | summarize_worker | Sonnet 4 | Retry 2x. If failed: store transcript, emit pipeline.failed. Summary is critical path. |
| 1b | extract_worker | Haiku 3.5 | Retry 2x. If failed: continue without extraction. Profile update skipped. |
| 2 | (deterministic) | — | Merge rules apply. Conflicts flagged, not auto-resolved. |
| 3 | suggest_worker | Sonnet 4 | Retry 1x. If failed: summary ships without suggestions. |
| 4 | (deterministic) | — | Pure comparison. Log significant changes. |

**Answer Question** (trigger: `suggestion.tapped` or `question.asked`)

```
suggestion.tapped / question.asked
  → Step 1: Check cache (deterministic)
  → Step 2: Load context (summary + transcript + profile + previous summaries)
  → Step 3: answer_worker (Sonnet, streamed)
  → Step 4: Cache answer (deterministic)
  → Emit: answer.generated
```

**Process Voice Input** (trigger: `voice_input.received`)

```
voice_input.received
  → Step 1: extract_worker (Haiku)
  → Step 2: Validate against current profile (deterministic)
  → Step 3: Return confirmation cards to app
  → [patient confirms]
voice_input.confirmed
  → Step 4: Profile merge (deterministic)
  → Emit: profile.updated
```

Human-in-the-loop between Steps 3 and 4. The brain never updates medical data without patient confirmation.

**Process Document** (trigger: `document.uploaded`)

```
document.uploaded
  → Step 1: explain_worker (Sonnet, with vision)
  → Step 2: extract_worker (Haiku)
  → Step 3: Profile merge (deterministic)
  → Step 4: Detect changes (deterministic)
  → Emit: profile.updated
```

**Appointment Prep** (trigger: `appointment.approaching`)

```
appointment.approaching
  → Step 1: Load journey context (profile + summaries since last appointment)
  → Step 2: prep_worker (Sonnet)
  → Emit: prep.generated
```

**Sharing Adaptation** (trigger: `summary.share_preview_requested`)

```
summary.share_preview_requested
  → Step 1: adapt_worker (Sonnet, per recipient role)
  → Step 2: translate_worker (Haiku, if target language differs)
  → Return adapted preview to app
```

### Worker catalog

| Worker | Purpose | Model | Why this model |
|---|---|---|---|
| `summarize_worker` | Transcript → patient-friendly summary | Sonnet 4 | Nuanced rewriting, Dutch medical quality |
| `extract_worker` | Any text → structured health data | Haiku 3.5 | Structured output task, 10x cheaper, fast |
| `suggest_worker` | Summary → 2-3 contextual questions | Sonnet 4 | Question quality drives engagement |
| `answer_worker` | Question + context → grounded answer | Sonnet 4 | Long-context reasoning, empathetic tone |
| `explain_worker` | Document → plain-language explanation | Sonnet 4 | Contextual awareness, explanatory depth |
| `prep_worker` | Journey context → prep document | Sonnet 4 | Cross-summary synthesis |
| `adapt_worker` | Summary → role-adapted version | Sonnet 4 | Tone and detail calibration per role |
| `translate_worker` | Text → translated text | Haiku 3.5 | Well-defined translation task |
| `detect_changes_worker` | Profile changes → notification text | Haiku 3.5 | Simple templated generation |

Full system prompts, input/output schemas, grounding rules, and error handling per worker are defined in [Direction C: The Nervous System](direction-c-nervous-system.md), Sections 4-5.

### Health Profile Store

Full JSON schema defined in [Direction C](direction-c-nervous-system.md), Section 5. Key sections:

- `demographics` (name, DOB, languages)
- `conditions[]` (with status, confidence, source attribution)
- `medications[]` (with status, dosage, frequency, confidence, source)
- `care_team[]` (name, role, facility)
- `action_items[]` (with status, due date, assigned to)
- `vitals_history[]` (type, value, unit, date)
- `appointments[]` (type, date, provider, status)
- `journey_events[]` (auto-detected milestones from summaries)

Every item has `source_event_id` (what event created it) and `confidence` (high/medium/low). Low-confidence items require user confirmation before becoming permanent. User corrections are marked `user_verified: true` and survive future conflicting extractions.

**Versioning**: Every mutation increments the version counter. Full profile at any version can be reconstructed from the audit log. Enables debugging, rollback, and GDPR compliance.

**Conflict resolution**: When extracted data disagrees with existing profile data, the brain flags the conflict for the patient to resolve. It never silently overwrites. See [Direction C](direction-c-nervous-system.md), Section 5 for detailed merge rules.

### API contract

```
# Recording pipeline
POST   /api/v1/recordings                    → triggers recording.completed
GET    /api/v1/recordings/{id}/status         → SSE: pipeline progress

# Summaries
GET    /api/v1/summaries/{id}                → summary + suggestions
GET    /api/v1/summaries/{id}/ask/stream     → SSE: streamed answer
POST   /api/v1/summaries/{id}/ask            → submit custom question

# Health Profile
GET    /api/v1/profile                       → full profile (latest)
GET    /api/v1/profile?version={n}           → profile at version
GET    /api/v1/profile/medications            → medications only
GET    /api/v1/profile/conditions             → conditions only
GET    /api/v1/profile/action-items           → action items (filterable)
GET    /api/v1/profile/history                → audit log
PUT    /api/v1/profile/{section}/{id}         → manual correction

# Voice Input
POST   /api/v1/voice-input                   → triggers voice_input.received
POST   /api/v1/voice-input/{id}/confirm      → triggers voice_input.confirmed

# Documents
POST   /api/v1/documents                     → triggers document.uploaded
GET    /api/v1/documents/{id}                → explanation + extracted data

# Appointment Prep
POST   /api/v1/prep                          → triggers appointment.approaching
GET    /api/v1/prep/{id}                     → prep document

# Sharing (preview only)
POST   /api/v1/sharing/preview               → adapted preview for a role
GET    /api/v1/sharing/preview/{id}          → cached preview
```

---

## Team Model: AI-First with Human Gates

| Role | Who | Responsibility |
|---|---|---|
| **Product Owner** | Merlijn | Vision, priorities, final sign-off at gates |
| **Architect** | Senior engineer (human) | Sets patterns in Slice 1, reviews all architecture decisions, owns API contracts |
| **AI Engineering Agents** | Claude Code agents | Build pipelines, workers, infrastructure, tests. Operate in isolated worktrees per task. |
| **Human Code Reviewer** | 1-2 engineers | Review AI agent output at PR level. Integration testing. |
| **UX Researcher** | AI agent + human validation | Synthetic patient studies, usability heuristics, persona walkthroughs |
| **Product Designer** | 1 designer (human) | UX/UI for all patient-facing surfaces. Works 1 sprint ahead of engineering. |
| **QA** | AI agents + human spot-checks | Automated test suites, prompt regression testing, edge case generation |

### How AI agents work in this model

- Each task gets a detailed ticket with acceptance criteria, relevant file paths, and architectural constraints
- AI agents work in isolated worktrees (no merge conflicts between parallel work)
- Every PR requires human review before merge
- Prompt engineering (system prompts) is human-authored, AI-tested against eval sets
- AI agents generate synthetic test conversations for QA
- AI agents write unit and integration tests alongside implementation

### Development cadence

2-week sprints. 6 sprints total. Gate reviews at slice boundaries.

---

## Delivery Plan: Vertical Slices

### Slice 1: The Core Brain (Weeks 1-4, Sprints 1-2)

**What the user experiences**: Patient records an appointment. Within 10 seconds: summary appears with 2-3 contextual suggestion chips. Patient taps "Why are they switching me from tablets to infusions?" and a grounded answer streams in, referencing what the doctor actually said. The health profile has silently been populated.

#### Sprint 1 (Weeks 1-2): Foundation + Recording Pipeline

**Infrastructure (architect-led, sets patterns for everything)**
- `[L]` INFRA-01: Event bus (typed events, correlation IDs, subscribe/emit, error handling)
- `[L]` INFRA-02: Worker framework (@worker decorator, retry, logging, model routing)
- `[L]` INFRA-03: Health Profile Store (PostgreSQL schema, JSONB, versioning, merge endpoint)
- `[M]` INFRA-04: FastAPI skeleton (auth stubs, CORS, SSE support, error responses)
- `[S]` INFRA-05: Config management (model versions, API keys, feature flags)

**Pipelines**
- `[L]` PIPE-01: Recording pipeline orchestration (event sub, parallel 1a/1b, sequential 2-3)
- `[M]` PIPE-02: summarize_worker implementation
- `[M]` PIPE-03: extract_worker implementation
- `[S]` PIPE-04: Profile merge logic (deterministic, conflict detection, significance scoring)

**Prompt engineering**
- `[M]` PROMPT-01: Author summarize_worker system prompt + test on 3 conversations
- `[M]` PROMPT-02: Author extract_worker system prompt + test on 3 conversations
- `[L]` PROMPT-03: Create 10 synthetic Dutch medical conversations with ground truth

**Mobile (iOS)**
- `[M]` IOS-01: Summary view refactor (support suggestion chips area below content)
- `[M]` IOS-02: API client (recordings endpoint, SSE pipeline status)
- `[S]` IOS-03: Loading state ("Ditto is working on your summary...")

**UX Research**
- `[M]` UXR-01: Define 5 synthetic patient personas with care journeys
- `[M]` UXR-02: Elderly usability heuristic framework
- `[S]` UXR-03: Trust signals checklist

**Design**
- `[M]` DES-01: Summary view with suggestion chips (Figma)
- `[M]` DES-02: Q&A answer expansion (Figma)
- `[S]` DES-03: Typography and color system for elderly readability

#### Sprint 2 (Weeks 3-4): Q&A + Gate 1

**Pipelines**
- `[L]` PIPE-05: Answer pipeline (event sub, context loading, streaming, caching)
- `[M]` PIPE-06: answer_worker implementation (streaming via Anthropic SDK)
- `[M]` PIPE-07: suggest_worker implementation
- `[S]` PIPE-08: Answer caching layer

**Prompt engineering**
- `[M]` PROMPT-04: Author answer_worker system prompt
- `[M]` PROMPT-05: Author suggest_worker system prompt
- `[L]` PROMPT-06: Eval harness (all 10 conversations, scored per worker)

**Mobile (iOS)**
- `[L]` IOS-04: Suggestion chips UI (tap → expand, visual design per spec)
- `[L]` IOS-05: Inline answer with SSE streaming
- `[M]` IOS-06: Source attribution + medical disclaimer
- `[M]` IOS-07: "Ask something else" text input

**UX Research**
- `[L]` UXR-04: Persona walkthroughs of Slice 1 outputs (all 5 personas, scored)
- `[M]` UXR-05: Document findings, create design recommendations for Slice 2

**QA**
- `[L]` QA-01: Gate 1 evaluation

#### Gate 1 (end of week 4)

| Criterion | Target | Method |
|---|---|---|
| Summary quality | ≥95% accuracy on 10 conversations | Manual review by product owner |
| Suggestion specificity | 80%+ conversation-specific | Manual review |
| Answer grounding | 100% reference source material | Automated + manual |
| Answer hallucination | 0 hallucinated medical claims | Manual review |
| End-to-end latency | Summary <10s, answer first token <3s | Automated |
| Profile extraction | Correct medications/conditions in 8/10 conversations | Manual comparison |
| Event tracing | Every step logged with correlation ID | Log inspection |

**Gate 1 is pass/fail.** If answer grounding or hallucination criteria fail, Slice 2 does not start until prompts are fixed.

---

### Slice 2: Living Memory (Weeks 5-8, Sprints 3-4)

**What the user experiences**: Profile tab shows auto-populated health overview. Voice input ("They changed my medication to metformin") extracts, shows confirmation card, updates profile on confirm. Photographed lab results get explained in plain language and update the profile. Suggestions now reference previous visits.

#### Sprint 3 (Weeks 5-6): Health Profile + Voice Input

**Infrastructure**
- `[L]` INFRA-06: Profile versioning + audit log + diff engine
- `[M]` INFRA-07: Conflict detection + resolution API endpoint
- `[S]` INFRA-08: Voice input event types

**Pipelines**
- `[L]` PIPE-09: Voice input pipeline (extract → validate → confirm → merge)
- `[M]` PIPE-10: Change detection pipeline
- `[M]` PIPE-11: Upgrade recording pipeline (pass full profile + previous summaries as context)

**Prompt engineering**
- `[M]` PROMPT-07: Tune extract_worker for voice input
- `[L]` PROMPT-08: Create 10 synthetic voice input test cases
- `[M]` PROMPT-09: Tune suggest_worker for cross-appointment questions

**Mobile (iOS)**
- `[L]` IOS-08: Profile tab (conditions, medications, care team, action items, vitals)
- `[M]` IOS-09: Manual profile correction flow
- `[L]` IOS-10: Voice input UI (mic button, transcription, confirmation cards)
- `[M]` IOS-11: Profile change indicator

**Design**
- `[L]` DES-04: Profile tab layout (card-based, source attribution per item)
- `[M]` DES-05: Voice input flow
- `[M]` DES-06: Confirmation card design

**UX Research**
- `[L]` UXR-06: Voice input persona walkthroughs (Jan and Corrie)

#### Sprint 4 (Weeks 7-8): Document Processing + Gate 2

**Pipelines**
- `[L]` PIPE-12: Document pipeline (upload → explain → extract → merge → detect)
- `[M]` PIPE-13: explain_worker implementation (vision-capable)

**Prompt engineering**
- `[M]` PROMPT-10: Author explain_worker system prompt
- `[L]` PROMPT-11: Create 8 synthetic documents with ground truth
- `[L]` PROMPT-12: Full regression eval (conversations + voice + documents)

**Mobile (iOS)**
- `[L]` IOS-12: Document capture UI
- `[M]` IOS-13: Document explanation view
- `[M]` IOS-14: Profile source attribution
- `[M]` IOS-15: Conflict resolution UI

**Infrastructure**
- `[M]` INFRA-09: Image upload endpoint + storage
- `[S]` INFRA-10: Profile scoped queries

**UX Research**
- `[L]` UXR-07: Heuristic audit of Slice 1+2 (10-point checklist per screen)

**QA**
- `[L]` QA-02: Gate 2 evaluation + Slice 1 regression

#### Gate 2 (end of week 8)

| Criterion | Target | Method |
|---|---|---|
| Profile accuracy | ≥90% correct after 3+ recordings | Automated comparison |
| Voice extraction | Correct in 8/10 voice test cases | Manual review |
| Voice confirmation | Ambiguous inputs trigger clarification | Manual edge case testing |
| Document explanation | Patient-friendly, accurate for 7/8 doc types | Manual review |
| Profile versioning | Audit log captures every mutation | Automated test |
| Conflict detection | Contradictory data flagged | Manual test |
| Cross-appointment Q&A | Answers reference previous visits when relevant | Manual review |
| User correction | user_verified fields survive future extractions | Automated test |
| Regression | All Slice 1 gate criteria still pass | Re-run eval suite |

**Gate 2 safety rule**: If voice input confirms data without asking when it should ask, the feature does not ship.

---

### Slice 3: Proactive Intelligence (Weeks 9-11, Sprints 5-6a)

**What the user experiences**: Two days before oncology follow-up, a Prep screen appears with suggested questions grounded in the patient journey. After a recording, tapping "Share with Hans" shows what Hans would see (practical, caregiver-focused) and what Mama would see (simpler, in Turkish).

#### Sprint 5 (Weeks 9-10): Appointment Prep + Sharing Adaptation

**Pipelines**
- `[L]` PIPE-14: Appointment prep pipeline
- `[L]` PIPE-15: Sharing adaptation (adapt_worker + translate_worker)

**Prompt engineering**
- `[M]` PROMPT-13: Author prep_worker system prompt
- `[M]` PROMPT-14: Author adapt_worker system prompt (5 role variations)
- `[M]` PROMPT-15: Author translate_worker system prompt (NL, EN, TR)
- `[L]` PROMPT-16: Create eval sets (5 prep, 4 adaptation scenarios)

**Mobile (iOS)**
- `[L]` IOS-16: Prep screen
- `[M]` IOS-17: Manual appointment entry
- `[L]` IOS-18: Sharing preview flow (select role → see adapted version)
- `[M]` IOS-19: Language switching on sharing preview

**Design**
- `[M]` DES-07: Prep screen layout
- `[L]` DES-08: Sharing preview with role badges

**UX Research**
- `[L]` UXR-08: Prep + sharing persona walkthroughs (Aysel for translation, Pieter for caregiver)

#### Sprint 6a (Week 11): Integration + Gate 3

**Engineering**
- `[L]` INTEG-01: Full journey integration test (1 patient, 3 recordings, 2 voice, 1 doc, 1 prep)
- `[L]` INTEG-02: Edge case fixes from all slices
- `[M]` INTEG-03: Performance optimization
- `[L]` INTEG-04: Prompt regression suite (all workers, full eval set)

**Mobile**
- `[M]` IOS-20: Navigation polish
- `[M]` IOS-21: Empty states
- `[M]` IOS-22: Error states

#### Gate 3 (end of week 11)

| Criterion | Target | Method |
|---|---|---|
| Prep relevance | Suggested questions reference actual patient data in 4/5 scenarios | Manual review |
| Prep grounding | Zero prep items not derivable from patient journey | Manual review |
| Adaptation differentiation | Partner and friend versions meaningfully different | Blind comparison |
| Translation accuracy | Medical terms preserved, meaning intact (NL, EN, TR) | Native speaker review |
| Elderly usability | 8/10 heuristic items pass per screen | UX researcher evaluation |
| Full journey test | End-to-end synthetic journey completes without errors | Automated + manual |
| Regression | All Slice 1 + 2 gate criteria still pass | Re-run eval suites |
| Pipeline observability | Any event traceable via correlation_id | Manual trace of 5 events |

---

### Polish & Ship (Week 12, Sprint 6b)

Nothing new gets built. Focus:

- `[L]` IOS-23: Accessibility pass (VoiceOver, Dynamic Type, contrast ratios)
- `[M]` INTEG-05: Performance tuning (cold start, cache effectiveness)
- `[M]` INTEG-06: Error handling audit (every failure path has a user message)
- `[M]` DOC-01: API documentation (OpenAPI spec complete)
- `[M]` DOC-02: Worker catalog (prompts, schemas, model choices documented)
- `[M]` DOC-03: Architecture decision records
- `[L]` UXR-09: Final usability audit (all screens, all 5 personas)
- `[M]` UXR-10: Full journey walkthrough documentation
- `[L]` QA-03: Final regression + ship criteria
- `[M]` QA-04: Demo preparation (scripted walkthrough)

---

## UX Research Plan

### Methodology: Synthetic Patient Testing

All research uses 5 synthetic personas with simulated care journeys. No access to real patients during MVP.

**Process per sprint:**

1. Create journey data (synthetic transcripts, voice inputs, documents) matching each persona
2. Run the brain against the data
3. UX researcher role-plays as persona, walks through brain outputs
4. Score comprehension, trust, utility, emotional fit on rubric
5. Document findings with specific recommendations
6. Feed into next sprint's design and prompt work

### Synthetic Patient Personas

**Mara (68)** — Colon cancer, stage 3b. Retired teacher. Lives with partner Hans. Moderate smartphone use. Anxious about treatment changes. Forgets after appointments. Hans handles logistics.
Tags: oncology, elderly, partner-involved

**Jan (74)** — Diabetes type 2 + cardiac conditions. Widower, lives alone. Daughter checks in weekly. Minimal tech. Multiple medications, multiple specialists. Needs things simple and big.
Tags: chronic multi, low-tech, solo

**Aysel (52)** — Breast cancer, remission monitoring. Turkish-Dutch, bilingual. Mother (76) speaks only Turkish. Aysel translates everything currently. Works full-time, dual care coordination.
Tags: multilingual, dual-care, working

**Pieter (45)** — Caregiver for wife Lisa (43) with relapsing MS. Tech-savvy. Attends appointments, coordinates care. Wants structured data. Two young kids.
Tags: caregiver, tech-savvy, complex-meds

**Corrie (81)** — Early cognitive decline + hip replacement. Assisted living. Son manages everything. iPad with large text. Maximum simplicity. Doesn't know what AI is.
Tags: cognitive, assisted, max-simple

### Research cadence

| Sprint | Activity | Feeds into |
|---|---|---|
| 1 | Persona definition, heuristic framework, trust signals | Sprint 2 design |
| 2 | Persona walkthroughs of Slice 1 (summaries, suggestions, Q&A) | Sprint 3 design + prompts |
| 3 | Voice input walkthroughs (Jan, Corrie) | Sprint 4 design |
| 4 | Heuristic audit of Slice 1+2 build | Sprint 5 design + fixes |
| 5 | Prep + sharing walkthroughs (Aysel, Pieter) | Sprint 6 polish |
| 6 | Final usability audit, full journey with all personas | Ship criteria |

### Synthetic conversation guidelines

- Written in Dutch with realistic code-switching (English medical terms)
- Vary in length: 5-minute GP check to 20-minute oncology discussion
- Include at least one ambiguity per conversation
- Manually labeled ground truth (medications, conditions, action items)
- Cover: oncology, cardiology, GP, diabetes, neurology, surgery, phone consult

### Existing market research (no new research needed)

- Competitive analysis: `competitive-analysis.md`
- Business case: `business-case.md`
- User insights: `pm-workspace/data/research/feature-ideas-user-insights.md`
- Style guide: `pm-workspace/data/references/warm-human-style-guide.md`

---

## Design Principles: Magic, Not AI

The interface must feel like "Ditto understands me," never "I'm using artificial intelligence."

### 1. Intelligence is Invisible

The AI never announces itself. No "AI-generated," no robot icons, no loading spinners that say "AI is thinking."

- Do: "Ditto prepared this for you" / "Based on your conversation"
- Don't: "Our AI analyzed your transcript" / "Generated by Claude"

### 2. Suggest, Don't Demand

The brain offers. The patient chooses. Suggestion chips are invitations, not obligations. Nothing happens without the patient's tap. No auto-actions on medical data.

- Do: Suggestion chips below content / Confirmation cards for voice input
- Don't: Auto-updating medications / Chat-style "How can I help?"

### 3. Source Everything

Every piece of intelligence traces back to a real source. Trust comes from attribution, not capability.

- Do: "From your appointment on April 4" / Doctor name + date on every answer
- Don't: Floating medical facts with no origin / Generic health information

### 4. Big, Clear, Calm

Minimum 16pt body text. High contrast. Generous whitespace. One primary action per screen. Calm colors.

- Do: Card-based layouts / Single-column / Large tap targets (min 44pt)
- Don't: Dense tables / Small toggles / Multi-column / Hamburger menus

### 5. Progressive Depth

Surface is simple. Detail is one tap away. Summary scannable in 15 seconds. Tap to go deeper.

- Do: Summary → tap for explanation → tap for source quote
- Don't: Everything visible at once / Expandable sections with no visual cue

### 6. Familiar Patterns Only

Only tap and scroll. No swipe-to-dismiss, no long-press, no drag. If Corrie (81) can't figure it out in 3 seconds, redesign it.

- Do: Tap buttons / Scroll lists / Back arrow / Clear labels
- Don't: Swipe actions / Floating action buttons / Gesture-driven navigation

### Trust signals for 65+ users

1. **Doctor attribution**: Every summary, answer, and suggestion names the doctor and date
2. **Your data, your control**: Profile shows exactly what Ditto knows. Patient can correct anything.
3. **Medical humility**: Every answer ends with "For medical advice, contact your care team."
4. **Confirmation before action**: Voice input shows what it heard before updating. Document extraction asks "Is this right?"
5. **Source transparency**: Every profile item shows its source event
6. **Consistent tone**: Warm, clear, never clinical. Same voice across all surfaces.

---

## Elderly Usability Heuristics

10-point checklist applied at every gate review. Each item scored pass/fail per screen.

| # | Heuristic | Test method |
|---|---|---|
| 1 | Text ≥ 16pt body, ≥ 20pt headings | Automated scan |
| 2 | Contrast ratio ≥ 4.5:1 (WCAG AA) | Automated scan |
| 3 | Tap targets ≥ 44x44pt with ≥ 8pt spacing | Layout inspection |
| 4 | One primary action per screen | Design review |
| 5 | No gesture beyond tap and scroll | Interaction audit |
| 6 | Loading state visible within 500ms | Performance test |
| 7 | Error messages in plain language with next step | Error state review |
| 8 | Always clear where I am and how to go back | 3-second test with persona |
| 9 | Medical content readable without domain knowledge | Flesch reading ease ≥ 60 |
| 10 | VoiceOver announces all interactive elements | Screen reader test |

---

## Prompt Engineering Strategy

### Principles

1. **Prompts are product decisions.** Product owner reviews every prompt before ship.
2. **One prompt per worker.** No dynamic assembly. Input schema provides context; prompt defines behavior.
3. **Grounding above all.** Every prompt includes explicit grounding rules. "Only use provided context. Say 'I don't know' otherwise."
4. **Eval before merge.** Every prompt change runs against full eval harness.
5. **Version control.** Prompts in repo alongside code. Model versions pinned.

### Prompt development flow

```
Author draft → test on 3 samples manually → refine → full eval harness (10+ items, scored) → product owner review → merge → regression in CI
```

### Eval harness

10 synthetic conversations + 10 voice inputs + 8 documents = core eval set. Each has manually labeled ground truth.

**Scoring per worker:**

| Worker | Metrics | Pass threshold |
|---|---|---|
| summarize_worker | Accuracy (0-5), completeness (0-5), patient-friendliness (0-5), no fabrication (binary) | Avg ≥ 4.0, zero fabrication |
| extract_worker | Precision, recall, F1 per entity type | F1 ≥ 0.85 per type |
| suggest_worker | Specificity (0-5), relevance (0-5), answerability (binary) | Avg ≥ 3.5, 100% answerable |
| answer_worker | Grounding (binary), accuracy (0-5), helpfulness (0-5), no hallucination (binary) | 100% grounded, zero hallucination, avg ≥ 4.0 |
| explain_worker | Accuracy (0-5), readability (0-5), key findings (binary) | Avg ≥ 4.0 |
| prep_worker | Relevance (0-5), grounding (binary), question quality (0-5) | Avg ≥ 3.5, 100% grounded |
| adapt_worker | Role differentiation (0-5), tone (0-5), permission compliance (binary) | Avg ≥ 3.5, 100% compliant |

---

## Risk Register

| Risk | Severity | Likelihood | Mitigation | Detection |
|---|---|---|---|---|
| **Medical hallucination** | Critical | Medium | Strict grounding in every prompt. Source attribution required. "Cannot answer" fallback. Eval harness on every prompt change. | Automated grounding check. Manual review of 50 random answers/week post-launch. |
| **Silent wrong profile update** | Critical | Low | All voice/document extractions require user confirmation. Low-confidence items flagged. user_verified survives extraction. | Audit log review. No profile mutation without confirmation event. |
| **Extraction accuracy degrades** | High | High (edges) | Diverse eval set. Confidence scoring. Low-confidence requires confirmation. | Weekly eval run. Accuracy dashboard per entity type. |
| **Model API downtime** | High | Low | Graceful degradation: recording saved, retry queue. "Processing, we'll notify you." | Health check endpoint. Alert on >5s latency or >1% errors. |
| **Prompt regression** | High | Medium | Regression eval in CI. Version-controlled prompts. Model pinning. | CI pipeline: prompt change triggers full eval. No merge without pass. |
| **Over-reliance on brain** | Medium | Low | Medical disclaimer on every answer. "Contact your care team." Never imperative about treatment. | Track "could not answer" ratio. Near 0% = grounding too loose. |
| **Scope creep** | Medium | High | Slice boundaries are hard cuts. Gate criteria pass/fail. Unplanned work to post-MVP backlog. | Weekly scope review against plan. |
| **Timeline too aggressive** | Medium | Medium | Slices priority-ordered. Slice 3 is cut candidate. Slice 1+2 = viable product. | Gate reviews include timeline assessment. Late Gate 1 → re-scope Slice 3. |

---

## Success Metrics

### Primary (non-negotiable)

| Metric | Target | Why it matters |
|---|---|---|
| **Suggestion tap rate** | 20%+ of summary viewers tap ≥1 suggestion | Proves brain adds value beyond summarization |
| **Profile accuracy** | 90%+ correct medications/conditions after 3+ recordings | Brain's memory must be trustworthy |
| **Answer grounding** | 100% of answers reference source material | Zero hallucination is non-negotiable for medical trust |

### Secondary

| Metric | Target | Why it matters |
|---|---|---|
| Summary latency | <10s from recording complete to summary visible | Brain must be fast enough to feel magic |
| Answer speed | <3s to first token | Streaming helps, but first token matters most |
| Elderly usability | 8/10 heuristic items pass per screen | Primary audience is 50+, design must serve them |
| Summary revisits | +15% revisit rate within 7 days | Brain gives reason to come back |
| Voice adoption | 15% of active users use voice input in 30 days | Second input channel for the brain |
| Prep utility | 70%+ rated "helpful" by internal testers | Prep must be personalized, not templated |

### Guardrails (must not decrease)

- Existing summary generation quality
- Existing summary generation latency
- App performance (suggestion generation is async, must not slow summary display)

---

## Tracking Events

Each pipeline has associated tracking events. The full tracking plan for Smart Suggestions (Slice 1) is defined in [Smart Suggestions Phase 1](care-brain-phase1-smart-suggestions.md#tracking-plan). Additional pipelines follow the same pattern:

| Event | Trigger | Key properties |
|---|---|---|
| `Smart Suggestions - Displayed` | Suggestions visible on summary | summary_id, suggestion_count, has_previous_summaries |
| `Smart Suggestions - Tapped` | User taps a suggestion | summary_id, suggestion_index, suggestion_text_preview |
| `Smart Suggestions - Answer Viewed` | Answer fully loaded | summary_id, answer_length, load_time_ms |
| `Smart Suggestions - Ask Custom` | User taps "Ask something else" | summary_id, suggestion_count_viewed |
| `Smart Suggestions - Custom Answer` | Custom question answered | summary_id, question_length, load_time_ms |
| `Profile - Viewed` | Patient opens Profile tab | profile_version, item_count |
| `Profile - Corrected` | Patient manually edits a field | field_type, was_auto_extracted |
| `Voice Input - Started` | Patient taps mic | source_screen |
| `Voice Input - Submitted` | Transcription complete | transcript_length, duration_s |
| `Voice Input - Confirmed` | Patient confirms extraction | items_confirmed, items_edited, had_conflict |
| `Voice Input - Cancelled` | Patient cancels | stage_cancelled_at |
| `Document - Uploaded` | Patient photographs document | doc_type_detected |
| `Document - Explanation Viewed` | Explanation loaded | doc_type, load_time_ms |
| `Prep - Viewed` | Patient opens prep screen | appointment_type, days_until, questions_count |
| `Prep - Question Tapped` | Patient taps a suggested question | question_index |
| `Sharing - Preview Requested` | Patient taps "Share" | summary_id, recipient_role |
| `Sharing - Role Switched` | Patient previews different role | from_role, to_role |
| `Sharing - Language Switched` | Patient switches language | from_language, to_language |

Each event includes standard properties: `user_id`, `timestamp`, `app_version`, `session_id`.

---

## Definition of Done

Applies to every ticket:

1. Code passes automated tests
2. Human code reviewer approved PR
3. If prompt change: eval harness passes, product owner reviewed prompt text
4. If UI change: matches approved design, passes relevant heuristic items
5. API changes documented in OpenAPI spec
6. Event tracing works (correlation_id traces through pipeline)

---

## References

- [Care Brain Strategy](care-brain-strategy.md) — approved strategic framing
- [Direction C: The Nervous System](direction-c-nervous-system.md) — full architecture spec with system prompts, schemas, scenarios
- [Smart Suggestions Phase 1](care-brain-phase1-smart-suggestions.md) — detailed feature spec for core Q&A
- [Business Case](business-case.md) — financial model, TAM, moat analysis
- [Competitive Analysis](competitive-analysis.md) — 7 competitors, market positioning
- [Warm/Human Style Guide](../data/references/warm-human-style-guide.md) — design aesthetic reference
