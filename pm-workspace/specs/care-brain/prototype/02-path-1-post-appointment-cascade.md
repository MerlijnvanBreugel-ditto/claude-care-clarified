# 02 · Path 1 — Post-Appointment One-Click Cascade

**Prereq**: `01-core-architecture.md` must be implemented. Schemas in `05-data-schemas.md`.

**Purpose**: Implement the keystone Tier 1 magic path. One screen after every recorded appointment with everything pre-arranged: follow-up appointments, action items, pre-prepared questions matched, adapted share previews. 90 seconds from recording to everything handled.

**This is the anchor demo for the prototype.** If only one path works perfectly, this is the one.

---

## User story

A patient (Mara, 68, oncology) records an appointment with her oncologist. She uploads it to Ditto. Seconds later, when she opens the app, she sees a single "Post-Appointment Cascade" screen with four cards:

1. **Follow-up appointments**: extracted from the conversation, with bookable time slots where available
2. **Your plan**: action items from the appointment (medications to start, things to watch for, etc.), each sourced
3. **Your questions**: her pre-prepared questions with checkmarks next to the ones the doctor addressed; unanswered ones flagged and carried forward to the next appointment's prep
4. **Share**: preview cards per circle member (full detail for her partner; softer for her daughter; one-liner for her friends group)

Each card is a single tap from commit. Nothing silently executes.

---

## End-to-end flow

```
1. Patient (or mobile app) POST /recordings
   Body: { patient_id, audio_url or transcript, appointment_context? }

2. API validates, stores raw Recording, emits `recording.completed`

3. Event bus dispatches to:
   - summarize_worker (existing)
   - extract_worker (existing, extended — see below)
   - appointment_detector_worker (new)
   - action_items_structured_worker (new)
   - pre_question_matcher_worker (new)

4. Each pipeline writes to the health graph:
   - Summary → Recording.summary_md
   - Medications → Medication entities (proposed → review flow)
   - Appointments → Appointment entities (status: suggested)
   - Actions → ActionItem entities
   - Questions → PrePreparedQuestion.resolved_with / .unresolved

5. On graph updates, wiki_render_worker updates relevant pages
   (timeline entry, medications, appointments/pending, plan/active, open_questions)

6. `profile.updated` emits → adapt_worker runs per circle member (existing)
   - Produces draft adapted-share previews per viewer_role
   - Does NOT auto-send (drafts only)

7. Patient opens app → GET /patients/{patient_id}/cascade/{recording_id}
   - API returns a structured response (see API Shape below)
   - Cascade surface renders the four cards from this JSON

8. Patient taps "Book" on an appointment → POST /appointments/{id}/book
   - Appointment moves from suggested → booked
9. Patient taps "Add to my plan" → POST /action-items/{id}/accept
10. Patient taps "Send" on an adapted share → POST /shares/{id}/send
    - Triggers circle delivery (out of scope for prototype: just mark as sent and store the payload)
```

---

## Pipelines required

### Existing pipelines (extended)

**`summarize_worker`** — baseline patient-friendly summary of the recording. No changes to its core contract. Uses Claude Sonnet. Prompt in `/prompts/summarize_worker/summarize.md`.

**`extract_worker`** — extract structured data (medications, conditions, care team updates) from the transcript. For Path 1, ensure it also emits appointment references and action-item candidates (may be extended or split into specialized pipelines below).

**`adapt_worker`** — audience adaptation. Already in the architecture for Path 3. For Path 1, it produces draft share previews (one per circle member with auto-share enabled, or a fixed set if none configured).

### New pipelines (Path 1)

**`appointment_detector_worker`**
- **Trigger**: `recording.completed`
- **Input**: transcript, current patient appointments, care team entities
- **Context mode**: filter (navigate the care team and recent appointments wiki pages)
- **Processor**: LLM-based (Sonnet). Prompt that extracts references like "come back in four weeks" or "I'll see you in May" into structured `(suggested_date, provider, reason, confidence)` triples. Resolves doctor references against known care team; flags unknown doctors.
- **Output**: `Appointment` entities with `status: suggested`, `source_event_id`
- **Side effects**: `graph_write`, emits `appointment.suggested`
- **Eval criteria**: given 10 annotated transcripts, detects ≥90% of appointment references with correct provider and within ±3 days of expected date
- **Open question**: whether to call external booking APIs in the prototype. Default: no — surface suggested slots from a mock calendar in `/fixtures/mock_slots.json`.

**`action_items_structured_worker`**
- **Trigger**: `recording.completed`
- **Input**: transcript, current medications, patient profile
- **Context mode**: fact + filter
- **Processor**: LLM-based (Sonnet). Extracts action items with `(action_text, trigger, timing, urgency, source_excerpt, category)` where category ∈ {medication, lifestyle, monitoring, call_if, other}.
- **Output**: `ActionItem` entities
- **Side effects**: `graph_write`
- **Eval criteria**: given 10 transcripts, extracts all mandatory actions (medication starts/stops, urgent call-triggers). Over-extraction of generic lifestyle advice is penalized.
- **Discipline**: every action must be grounded in a transcript excerpt. No generic medical advice.

**`pre_question_matcher_worker`**
- **Trigger**: `recording.completed` (only fires if patient had pre-prepared questions for this appointment)
- **Input**: pre-prepared questions from the patient's wiki's `open_questions.md` / `PrePreparedQuestion` entities scoped to this appointment, plus the transcript
- **Context mode**: fact
- **Processor**: LLM-based (Sonnet). For each pre-prepared question, determine: was it answered? If yes, find the excerpt. If no, mark unresolved and queue for next appointment's prep.
- **Output**: updates to `PrePreparedQuestion` with `resolved`, `resolved_with_excerpt`, `unresolved_carried_forward` fields
- **Side effects**: `graph_write`
- **Eval criteria**: given transcripts with known pre-questions and annotated resolution, ≥85% correct resolved/unresolved classification

**`share_list_suggester_worker`**
- **Trigger**: `summary.created`
- **Input**: care circle members with their sharing permissions; the summary; this appointment's significance (inferred from the summary)
- **Context mode**: fact
- **Processor**: deterministic rule engine. Suggests per-circle-member share levels (full / abridged / one-liner). High-stakes appointments default everyone to higher detail; routine to lower.
- **Output**: `ShareSuggestion` entities (one per circle member)
- **Side effects**: `graph_write`
- **Note**: adapt_worker uses these suggestions to compose the actual preview content.

---

## The Cascade API endpoint

**`GET /patients/{patient_id}/cascade/{recording_id}`**

Returns a structured JSON document with four sections. This is the endpoint the demo frontend hits to render the Cascade screen.

**Response shape (example)**:

```json
{
  "recording_id": "...",
  "appointment": {
    "date": "2026-04-04",
    "provider": "Dr. de Jong",
    "summary_preview": "Dr. de Jong discussed switching...",
    "summary_full_url": "/recordings/{id}/summary"
  },
  "appointments_suggested": [
    {
      "id": "...",
      "suggested_date": "2026-05-02",
      "provider": "Dr. de Jong",
      "reason": "Follow-up on new medication",
      "confidence": 0.92,
      "source_excerpt": "Let's see you in four weeks...",
      "available_slots": [
        {"datetime": "2026-05-02T10:30:00Z", "location": "UMCG"},
        ...
      ],
      "actions": ["book", "remind_later"]
    }
  ],
  "action_items": [
    {
      "id": "...",
      "text": "Start oxaliplatin on Monday",
      "category": "medication",
      "urgency": "normal",
      "source_excerpt": "...",
      "actions": ["add_to_plan", "dismiss"]
    },
    {
      "id": "...",
      "text": "Call clinic if nausea above 7/10",
      "category": "call_if",
      "urgency": "watch",
      "source_excerpt": "...",
      "actions": ["add_to_plan", "dismiss"]
    }
  ],
  "pre_prepared_questions": {
    "resolved": [
      {
        "question": "Why the switch?",
        "answer_excerpt": "Based on scan results from Tuesday..."
      }
    ],
    "unresolved": [
      {
        "question": "How long until I know it's working?",
        "actions": ["carry_forward_to_next_appointment", "ask_ditto"]
      }
    ]
  },
  "shares": [
    {
      "circle_member": {"name": "Hans", "role": "partner"},
      "preview_text": "Full summary...",
      "detail_level": "full",
      "actions": ["send", "edit", "skip"]
    },
    {
      "circle_member": {"name": "Sanne", "role": "adult_child"},
      "preview_text": "Softer version...",
      "detail_level": "abridged",
      "actions": ["send", "edit", "skip"]
    },
    {
      "circle_member": {"name": "Friends Group", "role": "friends"},
      "preview_text": "Quick update...",
      "detail_level": "one_liner",
      "actions": ["send", "edit", "skip"]
    }
  ],
  "missed_callout": null
}
```

**Notes**:
- `missed_callout` (nullable) surfaces items from the recording the patient visibly didn't register — e.g., if extraction suggests a medication change was discussed but the patient has not acknowledged it. Optional for prototype; include the field even if always null.
- Every entity has an `id` so action endpoints can reference it.
- Every claim has `source_excerpt` — the trust architecture requires provenance everywhere.

---

## Action endpoints

For each item in the cascade, there's a commit endpoint. These are the taps. The prototype implements them as:

| Action | Endpoint | Effect |
|---|---|---|
| Book appointment | `POST /appointments/{id}/book` | Appointment status → `booked` |
| Add action item to plan | `POST /action-items/{id}/accept` | ActionItem status → `active`, added to `plan/active.md` |
| Carry question to next prep | `POST /pre-questions/{id}/carry-forward` | Flag set; will appear in next prep pipeline |
| Send an adapted share | `POST /shares/{id}/send` | Share payload logged; marked sent; event emitted |
| Dismiss an item | `POST /{item_type}/{id}/dismiss` | Item → `dismissed` (audit-logged, reversible) |

All action endpoints are audit-logged with the patient's action.

---

## Eval suite

Location: `/evals/cascade/`

Three test scenarios minimum:

1. **The happy path**: Mara's oncology appointment fixture. Expected: correct medication extraction (oxaliplatin replaces capecitabine), one appointment suggested (~4 weeks out), 2–3 action items, 2 pre-questions resolved + 1 unresolved, 3 adapted shares produced.

2. **An ambiguous transcript**: appointment reference is vague ("see you in spring"). Expected: appointment suggested with low confidence; patient asked to confirm.

3. **Safety-critical adversarial**: transcript contains a medication change the patient visibly doesn't acknowledge. Expected: medication extracted with `review_required: high`; appears in `missed_callout`.

Each eval case is a fixture (sample recording + annotated expected outputs). Pipeline runs end-to-end; harness asserts the Cascade endpoint returns the expected structure.

---

## Success criteria for Path 1

- [ ] `POST /recordings` accepts a transcript fixture, emits events, pipelines run
- [ ] All four new pipelines registered and passing their eval thresholds
- [ ] `GET /cascade/{recording_id}` returns the full JSON structure above
- [ ] Each action endpoint works and the graph is mutated with an audit entry
- [ ] At least one demo frontend view renders the four cards from the JSON (can be trivial HTML)
- [ ] The three test scenarios in the eval suite all pass

---

## What you choose

- How `appointment_detector_worker` resolves unknown doctors (create stub entity? flag for confirmation?)
- How to render the preview text in shares (keep it simple; full LLM composition is fine, but so is templated on a summary)
- Whether to include voice-input symptom data in the action items (not required for Path 1)
- How to handle a patient with no care circle configured (default: still produce a "share with yourself" preview, or skip the shares card entirely with an empty-state message — either is fine)

---

## What you do NOT have latitude on

- Every appointment suggestion, action item, pre-question match, and share preview must be **grounded in a source transcript excerpt**. No fabrication. If the pipeline can't ground a claim, it doesn't include it.
- Medication changes are high-stakes: they must go through the review flow from `01-core-architecture.md` §7 before appearing as a confirmed entity.
- The Cascade endpoint must return all four sections in a **single request** (no polling, no streaming split). If a pipeline is still running, return the best partial state with clear status indicators.
- No item may silently auto-execute. Every commit requires an explicit action endpoint call.

---

## Out of scope for Path 1

- Real external calendar API integration (mock calendar is fine)
- Real delivery of shares to circle members (Path 3 handles inbound; Path 1 just marks shares as sent)
- Multi-recording context (Path 1 handles one recording at a time; longitudinal memory via wiki is provided by the architecture, not reimplemented here)
- Voice input as a source (Path 2 owns voice input)
- Non-NL/EN language handling
