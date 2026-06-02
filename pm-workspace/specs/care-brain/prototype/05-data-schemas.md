# 05 · Data Schemas

**Purpose**: Canonical schema reference for the prototype. Every other doc in this directory references these definitions. When in doubt about a field name, type, or shape, this file wins.

**Implementation note**: These are logical schemas (what must exist and what it means), not SQL DDL or ORM code. You choose the implementation (Pydantic models, SQLAlchemy, raw SQL, whatever fits). The fields, types, and constraints below are the contract.

---

## 1. Event Envelope

Every event on the bus uses this envelope.

```
Event {
  event_id:        UUID          # globally unique
  event_type:      string        # from the canonical list below
  patient_id:      UUID          # isolation boundary — every event belongs to one patient
  correlation_id:  UUID          # traces a causal chain across pipeline hops
  timestamp:       ISO8601       # when the event was emitted
  source:          string        # which pipeline/worker/endpoint emitted it
  payload:         dict          # typed per event_type — see below
}
```

---

## 2. Canonical Event Types

### Core events (from direction-c, kept)

| Event type | Payload fields | Emitted by |
|---|---|---|
| `recording.completed` | `transcript_id`, `transcript_text`, `recording_duration_s`, `detected_language`, `appointment_context?` | Recording upload endpoint |
| `document.uploaded` | `document_id`, `doc_type`, `image_url?`, `ocr_text?` | Document upload endpoint |
| `voice_input.received` | `input_id`, `transcript_text`, `duration_s` | Voice input endpoint |
| `summary.created` | `summary_id`, `summary_text`, `suggestion_ids[]` | `summarize_worker` |
| `profile.updated` | `changed_fields[]`, `source_event_id`, `worker_id` | Any pipeline that writes to the graph |
| `suggestion.tapped` | `summary_id`, `suggestion_id`, `question_text`, `viewer_id`, `viewer_role` | App action |
| `question.asked` | `summary_id`, `question_text`, `viewer_id`, `viewer_role` | App action |
| `appointment.approaching` | `appointment_id`, `appointment_type`, `provider_name`, `hours_until` | Scheduler |
| `circle_member.added` | `member_id`, `member_role`, `member_name`, `sharing_permissions` | App action |
| `profile.conflict_detected` | `field`, `existing_value`, `new_value`, `source_a`, `source_b` | `wiki_lint_worker` or merge logic |

### New events (added by the magic paths)

| Event type | Payload fields | Emitted by | Path |
|---|---|---|---|
| `appointment.suggested` | `suggested_date`, `provider_id`, `reason`, `confidence`, `source_excerpt` | `appointment_detector_worker` | 1 |
| `action_item.created` | `text`, `category`, `urgency`, `trigger?`, `timing?`, `source_excerpt` | `action_items_structured_worker` | 1 |
| `pre_question.matched` | `question_id`, `resolved: bool`, `resolved_with_excerpt?` | `pre_question_matcher_worker` | 1 |
| `symptom.logged` | `symptom_type`, `severity`, `qualifiers[]`, `body_region?`, `source_input_id` | `symptom_extractor_worker` | 2 |
| `pattern.detected` | `pattern_type`, `description`, `data_points[]`, `severity`, `grounding_ids[]` | `symptom_pattern_worker` | 2 |
| `circle.reaction_received` | `sender_id`, `source_share_id`, `message_text`, `has_help_offer`, `has_call_request` | Reaction endpoint | 3 |
| `help_offer.received` | `offer_id`, `sender_id`, `category`, `scope?`, `when?` | `help_offer_worker` | 3 |
| `help_offer.accepted` | `offer_id`, `accepted_at` | Patient action endpoint | 3 |
| `help_offer.declined` | `offer_id`, `declined_at` | Patient action endpoint | 3 |
| `call.scheduled` | `call_id`, `participants[]`, `datetime`, `duration_min` | `scheduling_assistant_worker` | 3 |
| `wiki.edit_proposed` | `edit_id`, `page_path`, `stakes`, `proposing_pipeline` | `wiki_render_worker` | Core |
| `wiki.edit_applied` | `edit_id`, `page_path`, `review_status` | Review state machine | Core |
| `review.required` | `entity_type`, `entity_id`, `reason`, `proposing_pipeline` | Any high-stakes pipeline | Core |
| `reaction.inbox_updated` | `reaction_count`, `help_offer_count`, `call_request_count` | `reaction_inbox_worker` | 3 |

---

## 3. Health Graph Entities

### Shared fields (every entity has these)

```
BaseEntity {
  id:                UUID
  patient_id:        UUID          # isolation boundary
  created_at:        ISO8601
  updated_at:        ISO8601
  version:           int           # monotonic, for optimistic concurrency
  source_event_ids:  UUID[]        # provenance — which events caused this state
  review_status:     enum          # proposed | auto_approved | reviewer_approved |
                                   # patient_confirmed | rejected | provisional
  tombstoned_at:     ISO8601?      # null = active; set = soft-deleted for GDPR
}
```

### Patient

```
Patient extends BaseEntity {
  name:              string
  date_of_birth:     date?
  primary_language:  string        # e.g. "nl", "en"
  timezone:          string        # e.g. "Europe/Amsterdam"
}
```

### Doctor

```
Doctor extends BaseEntity {
  name:              string
  specialty:         string?       # e.g. "medical oncology", "cardiology"
  institution:       string?
  contact_info:      string?       # optional, for the patient's reference
  first_seen_at:     ISO8601?      # first recording where this doctor appeared
}
```

### Condition

```
Condition extends BaseEntity {
  name:              string        # e.g. "Colon cancer", "Diabetes type 2"
  stage:             string?       # e.g. "stage 3b" — nullable, condition-dependent
  status:            enum          # active | in_remission | resolved | monitoring
  diagnosed_at:      date?
  diagnosing_doctor_id: UUID?
}
```

### Medication

```
Medication extends BaseEntity {
  name:              string        # generic name
  dose:              string?       # e.g. "500mg twice daily", "85 mg/m² IV every 2 weeks"
  status:            enum          # active | historical | suggested
  started_at:        date?
  stopped_at:        date?
  prescribing_doctor_id: UUID?
  replaced_by_id:    UUID?         # if this medication was replaced by another
  replaces_id:       UUID?         # if this medication replaced another
  reason:            string?       # why prescribed, sourced from transcript
}
```

### CareCircleMember

```
CareCircleMember extends BaseEntity {
  name:              string
  role:              enum          # partner | adult_child | parent | sibling |
                                   # friend | colleague | neighbor | other
  language:          string?       # preferred language for adapted shares
  sharing_level:     enum          # full | abridged | one_liner | none
  auto_share:        bool          # true = automatically receive adapted shares
  contact_method:    string?       # placeholder for future comms
}
```

### Recording

```
Recording extends BaseEntity {
  transcript_text:   text
  summary_md:        text?         # set after summarize_worker runs
  duration_s:        int?
  detected_language: string?
  appointment_date:  date?
  doctor_id:         UUID?         # resolved after extraction
  recording_url:     string?       # pointer to raw audio (if stored)
}
```

### Appointment

```
Appointment extends BaseEntity {
  date:              ISO8601?      # null if only vaguely referenced ("in spring")
  date_precision:    enum          # exact | week | month | vague
  provider_id:       UUID?
  reason:            string?
  status:            enum          # past | upcoming | suggested | booked | cancelled
  source_excerpt:    text?         # the transcript excerpt that prompted this
  location:          string?
  confidence:        float?        # extraction confidence (0-1)
}
```

### ActionItem

```
ActionItem extends BaseEntity {
  text:              string
  category:          enum          # medication | lifestyle | monitoring | call_if | follow_up | other
  urgency:           enum          # immediate | this_week | normal | low
  trigger:           string?       # "if nausea above 7/10"
  timing:            string?       # "starting Monday", "daily for 2 weeks"
  status:            enum          # pending | active | completed | dismissed
  source_excerpt:    text?
  source_recording_id: UUID?
}
```

### PrePreparedQuestion

```
PrePreparedQuestion extends BaseEntity {
  question_text:     string
  target_appointment_id: UUID?     # which appointment this question is for
  resolved:          bool          # was it answered in the appointment?
  resolved_with_excerpt: text?     # the doctor's response, if resolved
  carried_forward_to: UUID?        # next appointment ID, if unresolved
}
```

### Symptom

```
Symptom extends BaseEntity {
  type:              string        # from the symptom ontology (see §4)
  severity:          float         # 0-10 scale (or mapped from qualitative input)
  qualifiers:        string[]      # e.g. ["morning", "positional", "triggered_by_cold"]
  body_region:       string?       # e.g. "left_hip", "hands_and_feet"
  input_method:      enum          # voice | quick_tap | extracted_from_recording
  source_input_id:   UUID?         # voice_input or recording ID
  captured_at:       ISO8601       # when the patient reported it (may differ from created_at)
}
```

### Reaction

```
Reaction extends BaseEntity {
  sender_id:         UUID          # CareCircleMember ID
  source_share_id:   UUID?         # the adapted share that prompted this
  message_text:      text
  tone:              string?       # warm | supportive | helpful | concerned | other
  has_help_offer:    bool
  has_call_request:  bool
  thanked:           bool          # patient has acknowledged
  archived:          bool
  received_at:       ISO8601
}
```

### HelpOffer

```
HelpOffer extends BaseEntity {
  reaction_id:       UUID          # parent reaction
  sender_id:         UUID
  category:          enum          # transport | meals | company | childcare | errands | other
  scope:             string?       # "rides this month", "dinner Thursday"
  when:              string?       # scheduling hint
  where:             string?
  notes:             text?
  status:            enum          # pending | accepted | declined | completed
  accepted_at:       ISO8601?
  declined_at:       ISO8601?
}
```

### ScheduledCall

```
ScheduledCall extends BaseEntity {
  reaction_id:       UUID?         # parent reaction (nullable if scheduled independently)
  sender_id:         UUID
  datetime:          ISO8601
  duration_min:      int
  status:            enum          # scheduled | completed | cancelled | no_show
  meeting_link:      string?       # placeholder for prototype
  patient_confirmed: bool
  sender_confirmed:  bool
}
```

---

## 4. Symptom Ontology (starter set)

A versioned, finite list. New types require a schema change, not runtime extension.

| Type slug | Display name | Default severity scale | Common qualifiers |
|---|---|---|---|
| `fatigue` | Fatigue | 0-10 | morning, afternoon, all_day, post_activity |
| `pain` | Pain | 0-10 | sharp, dull, throbbing, constant, intermittent |
| `nausea` | Nausea | 0-10 | morning, post_meal, medication_related |
| `dizziness` | Dizziness / Vertigo | 0-10 | positional, standing, constant |
| `headache` | Headache | 0-10 | tension, migraine, cluster |
| `insomnia` | Sleep difficulty | 0-10 | falling_asleep, staying_asleep, early_waking |
| `appetite_loss` | Appetite loss | 0-10 | complete, partial, nausea_related |
| `mood_low` | Low mood | 0-10 | anxious, sad, irritable, flat |
| `numbness` | Numbness / Tingling | 0-10 | hands, feet, face, cold_triggered |
| `shortness_of_breath` | Shortness of breath | 0-10 | exertion, rest, lying_down |
| `swelling` | Swelling | 0-10 | legs, ankles, face, hands |
| `skin_reaction` | Skin reaction | 0-10 | rash, itching, injection_site |
| `cognitive` | Brain fog / Confusion | 0-10 | memory, concentration, word_finding |
| `joint_stiffness` | Joint stiffness | 0-10 | morning, all_day, specific_joint |
| `other` | Other (freeform) | 0-10 | *(capture in notes)* |

Extend this list as test cases demand. Every extension is a schema version bump.

---

## 5. Pipeline Contract Schema

```
PipelineContract {
  name:                string        # unique identifier
  trigger:             TriggerSpec   # see below
  input_filter:        string        # human-readable description of what context is fetched
  context_mode:        enum          # fact | filter | similarity
  output_type:         string        # reference to a typed schema (e.g., "Medication", "ActionItem[]")
  side_effects:        enum[]        # graph_write | wiki_write | event_emit | external_call
  tier:                enum          # free | premium | internal
  eval_suite:          string        # path to eval directory
  retirement_criterion: string       # human-readable
}

TriggerSpec {
  event_types:         string[]      # list of event types that activate this pipeline
  filter_predicate:    string?       # optional: only fire if payload matches (human-readable)
}
```

---

## 6. Wiki Page Schema (Frontmatter)

Every wiki page has YAML frontmatter. The content body is markdown.

### Shared frontmatter (all page types)

```yaml
type: entity | concept | timeline | symptoms | inbox | index | log | plan | overview
page_path: string                   # e.g. "entities/medications/oxaliplatin.md"
last_updated: ISO8601
source_event_ids: UUID[]            # which events produced/updated this page
schema_version: int                 # for migration
review_status: pipeline_generated | patient_confirmed | reviewer_approved
```

### Entity page frontmatter (extends shared)

```yaml
entity_kind: doctor | condition | medication | care_circle_member
slug: string                        # unique within kind
canonical_name: string
status: active | historical | monitoring
```

### Timeline page frontmatter (extends shared)

```yaml
date: ISO8601
event_kind: appointment | medication_change | diagnosis | lab_result | milestone
provider: string?                   # entity reference
significance: low | medium | high
concepts: string[]                  # related concept page paths
```

### Symptom timeline page frontmatter (extends shared)

```yaml
window: { from: date, to: date }
symptom_types: string[]
entry_count: int
```

### Inbox page frontmatter (extends shared)

```yaml
inbox_type: reactions | help_offers | scheduled_calls
item_count: int
unread_count: int
```

---

## 7. Wiki Edit Diff

Every proposed wiki change is typed.

```
WikiEdit {
  edit_id:             UUID
  patient_id:          UUID
  page_path:           string
  before_hash:         string       # hash of content before edit
  after_hash:          string       # hash of content after edit
  frontmatter_diff:    dict         # changed frontmatter fields
  content_diff:        text         # unified diff or structured
  proposing_pipeline:  string       # which pipeline proposed this
  source_event_ids:    UUID[]
  stakes:              enum         # low | high
  review_status:       enum         # proposed | auto_approved | reviewer_approved |
                                    # patient_confirmed | rejected | provisional
  proposed_at:         ISO8601
  resolved_at:         ISO8601?
}
```

---

## 8. Audit Log Entry

```
AuditEntry {
  id:                  UUID
  patient_id:          UUID
  entity_type:         string       # "Medication", "Appointment", "WikiPage", etc.
  entity_id:           UUID
  action:              enum         # created | updated | deleted | tombstoned | reviewed
  before_snapshot:     JSON?        # null for creates
  after_snapshot:      JSON
  source_event_id:     UUID
  actor:               string       # pipeline name, user action, system
  timestamp:           ISO8601
}
```

---

## 9. API Response Shapes (Summary)

The full API response shapes live in each path doc. This section lists only the entity shapes that appear in multiple paths.

### SharePreview (used in Path 1 cascade + Path 3 reactions)

```json
{
  "id": "UUID",
  "circle_member": {
    "id": "UUID",
    "name": "string",
    "role": "partner | adult_child | friend | ..."
  },
  "detail_level": "full | abridged | one_liner",
  "preview_text": "string",
  "language": "nl | en | ...",
  "source_recording_id": "UUID",
  "actions": ["send", "edit", "skip"]
}
```

### CircleMemberSummary (used in inbox + cascade)

```json
{
  "id": "UUID",
  "name": "string",
  "role": "string",
  "language": "string?",
  "sharing_level": "full | abridged | one_liner | none",
  "auto_share": true
}
```

### SourceAttribution (used everywhere)

```json
{
  "source_event_id": "UUID",
  "source_type": "recording | voice_input | document | manual",
  "date": "ISO8601",
  "excerpt": "string?"
}
```

Every claim in every API response should carry a `source` field using this shape.

---

## 10. Fixture Data

The prototype should include at least these fixtures in `/fixtures/`:

| Fixture | Purpose |
|---|---|
| `sample_patient_mara.json` | Mara, 68, oncology — the canonical test patient |
| `sample_patient_jan.json` | Jan, 74, multi-condition — symptom tracking test patient |
| `sample_recording_oncology.json` | Mara's oncology appointment with medication change — drives Path 1 |
| `sample_voice_inputs_jan.json` | 14 days of Jan's voice check-ins — drives Path 2 |
| `sample_reactions.json` | 5 reactions from circle members to Mara's adapted share — drives Path 3 |
| `mock_calendar_mara.json` | Mara's availability for scheduling test |
| `mock_calendar_sanne.json` | Sanne's proposed slots for call scheduling test |
| `mock_appointment_slots.json` | Available clinic slots near Mara — for appointment booking test |

Each fixture should be a self-contained JSON file that can be loaded to seed the health graph. Pipeline evals in `/evals/` reference these fixtures.

---

## 11. Schema Versioning

Every entity and wiki page carries a `schema_version` (int). When the schema changes:

1. Bump the version number in this doc.
2. Write a migration that reads old-version entities and writes new-version equivalents.
3. Old versions are readable (backward-compat) for one version window.
4. Wiki pages with old schema versions are re-rendered by `wiki_render_worker` on next access.

For the prototype: start at `schema_version: 1`. If you need to change a schema during development, increment and document the change in this file.

---

## Notes for the implementing agent

- These schemas are **logical contracts**. You implement them in whatever ORM or data layer you choose. The field names and types must match.
- Where a field is `UUID?` (nullable), it's optional — but document when it would be null.
- Where a field is `string[]`, implement as a JSON array column or equivalent. PostgreSQL JSONB handles this well.
- The `source_event_ids[]` field is critical for provenance. Every entity and wiki page must trace back to the events that created or updated it. Do not skip this.
- Patient isolation (`patient_id` scoping) is a hard constraint at the data-access layer. A query that touches entities across patients is a bug, not a feature.
