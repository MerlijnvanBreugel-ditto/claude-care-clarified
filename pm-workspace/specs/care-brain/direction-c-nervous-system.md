# Direction C: The Nervous System — Event-Driven Reactive Architecture

**Date**: 2026-04-04
**Status**: Prototype-ready spec
**Parent**: [Care Brain Strategy](care-brain-strategy.md)
**Classification**: Architecture prototype (1 of 3 directions)

---

No central orchestrator. Events trigger processing pipelines. The Health Profile Store is the nervous system. Agents are stateless workers that respond to events by reading from and writing to the store. The "intelligence" lives in three places: event routing rules, accumulated profile state, and pipeline definitions. The agents themselves are just Claude API calls with focused prompts.

This is the most production-ready direction. Most aligned with microservices. Most observable.

---

## 1. Architecture Overview

```
                        ┌─────────────────────────────┐
                        │         EVENT BUS            │
                        │  (pub/sub message system)    │
                        └──────┬──────────┬────────────┘
                               │          │
              ┌────────────────┤          ├────────────────┐
              │                │          │                │
              ▼                ▼          ▼                ▼
     ┌────────────┐  ┌────────────┐ ┌─────────┐  ┌───────────┐
     │  Pipeline:  │  │  Pipeline:  │ │Pipeline:│  │ Pipeline:  │
     │  Recording  │  │  Question   │ │  Voice  │  │   Prep    │
     │  Processing │  │  Answering  │ │  Input  │  │           │
     └──────┬─────┘  └─────┬──────┘ └────┬────┘  └─────┬─────┘
            │              │             │              │
            ▼              ▼             ▼              ▼
     ┌─────────────────────────────────────────────────────────┐
     │                 AGENT WORKERS                            │
     │  (stateless Claude API calls, one per pipeline step)    │
     └──────────────────────┬──────────────────────────────────┘
                            │
                            ▼
     ┌─────────────────────────────────────────────────────────┐
     │              HEALTH PROFILE STORE                        │
     │  (persistent structured patient data — the brain state) │
     └─────────────────────────────────────────────────────────┘
```

### Components

**Event Bus**: Central pub/sub message system. Every action in the product emits an event. Pipelines subscribe to event types. Events are immutable, ordered, and durable. In the prototype: an in-process event emitter. In production: Redis Streams, AWS EventBridge, or Google Pub/Sub.

**Health Profile Store**: Persistent structured patient data. This IS the brain's memory. Every worker reads from it for context and writes back to it with new extractions. Versioned, auditable, conflict-aware. In the prototype: SQLite with JSON columns. In production: PostgreSQL with JSONB.

**Processing Pipelines**: Named sequences of steps triggered by specific events. Each step invokes one agent worker with defined inputs and outputs. Steps can run in parallel (marked with `||`) or sequentially. Pipelines emit new events on completion, enabling cascading pipelines.

**Agent Workers**: Stateless functions. Each wraps a single Claude API call with a focused system prompt, defined input schema, and defined output schema. Workers are the smallest unit. They read from the profile store and write back to it. They don't know about each other or the pipeline they're part of.

**Results Feed**: Processed outputs published back to the event bus as new events. Enables pipeline chaining: `recording.completed` triggers the recording pipeline, which emits `profile.updated`, which triggers the change detection pipeline.

---

## 2. Event Taxonomy

| Event | Trigger | Payload | Pipelines Activated |
|---|---|---|---|
| `recording.completed` | Conversation recording finishes processing | `{ transcript_id, patient_id, transcript_text, recording_duration_s, detected_language }` | Process Recording |
| `document.uploaded` | Patient photographs a letter/lab result | `{ document_id, patient_id, doc_type, image_url, ocr_text }` | Process Document |
| `voice_input.received` | Patient uses "Tell Ditto" voice input | `{ input_id, patient_id, transcript_text, duration_s }` | Process Voice Input |
| `summary.viewed` | Patient or circle member views a summary | `{ summary_id, viewer_id, viewer_role, patient_id, is_first_view }` | Generate Viewer Suggestions |
| `suggestion.tapped` | User taps a suggestion chip | `{ summary_id, suggestion_id, question_text, viewer_id, viewer_role }` | Answer Question |
| `question.asked` | User types a custom question | `{ summary_id, question_text, viewer_id, viewer_role, patient_id }` | Answer Question |
| `appointment.approaching` | Calendar event within 48 hours | `{ appointment_id, patient_id, appointment_type, provider_name, hours_until }` | Generate Appointment Prep |
| `profile.updated` | Health profile data changed | `{ patient_id, changed_fields[], source_event_id, worker_id }` | Detect Profile Changes |
| `circle_member.added` | New member joins care circle | `{ patient_id, member_id, member_role, member_name, sharing_permissions }` | Generate Circle Welcome |
| `summary.created` | New summary stored after recording pipeline | `{ summary_id, patient_id, summary_text, suggestion_ids[] }` | (consumed by mobile app) |
| `answer.generated` | Answer produced for a question | `{ answer_id, summary_id, question_text, answer_text, viewer_id }` | (consumed by mobile app) |
| `circle.notified` | Circle update sent | `{ patient_id, member_ids[], summary_id, update_type }` | (consumed by notification service) |
| `profile.conflict_detected` | Two data sources disagree | `{ patient_id, field, existing_value, new_value, source_a, source_b }` | (queued for user resolution) |
| `prep.generated` | Appointment prep ready | `{ patient_id, appointment_id, prep_summary, suggested_questions[] }` | (consumed by mobile app) |

### Event Envelope Schema

Every event wraps its payload in a standard envelope:

```json
{
  "event_id": "evt_a1b2c3d4",
  "event_type": "recording.completed",
  "timestamp": "2026-04-04T14:30:00Z",
  "patient_id": "pat_x1y2z3",
  "source": "mobile_app",
  "correlation_id": "corr_m1n2o3",
  "payload": { ... }
}
```

The `correlation_id` traces an event through all downstream pipelines. Every child event inherits the parent's `correlation_id`.

---

## 3. Pipeline Definitions

### Pipeline: Process Recording

Trigger: `recording.completed`

```
recording.completed
  ├─ Step 1a: Summarize       (Claude Sonnet)  ─┐
  │                                               ├─ parallel
  └─ Step 1b: Extract Health   (Claude Haiku)   ─┘
  → Step 2: Update Profile     (deterministic merge)
  → Step 3: Generate Suggestions (Claude Sonnet)
  → Step 4: Detect Changes     (deterministic diff)
  ├─ Step 5a: Generate Circle Updates (Claude Sonnet, per member) ─┐
  │                                                                 ├─ parallel, conditional
  └─ Step 5b: Translate Summary (Claude Haiku, if non-Dutch members)┘
  → Emit: summary.created, profile.updated, circle.notified
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1a | `summarize_worker` | transcript, patient profile, previous summary titles/dates | summary text | Retry 2x. If failed: store transcript, emit `pipeline.failed`, skip remaining steps. Summary is critical path. |
| 1b | `extract_worker` | transcript, current profile | structured health data (medications, conditions, action items, care team, dates) | Retry 2x. If failed: continue pipeline without extraction. Profile update skipped. Log for manual review. |
| 2 | (deterministic) | extracted data, current profile | updated profile | Apply merge rules (see Section 5). If conflict: emit `profile.conflict_detected`, store both values, continue with existing value. |
| 3 | `suggest_worker` | summary, patient profile, previous summaries | 2-3 suggestion questions | Retry 1x. If failed: summary ships without suggestions. Suggestions are enhancement, not critical. |
| 4 | (deterministic) | previous profile snapshot, new profile | list of changes with significance scores | Pure comparison. Cannot fail unless data corrupted. |
| 5a | `adapt_worker` | summary, circle member profile, sharing permissions | adapted summary per member | Per-member. If one fails, others still send. Failed member gets generic notification. |
| 5b | `translate_worker` | summary or adapted summary, target language | translated text | If failed: send in original language with note. |

### Pipeline: Answer Question

Trigger: `suggestion.tapped` or `question.asked`

```
suggestion.tapped / question.asked
  → Step 1: Load Context      (deterministic)
  → Step 2: Generate Answer    (Claude Sonnet, streamed)
  → Step 3: Cache Answer       (deterministic)
  → Emit: answer.generated
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | (deterministic) | summary_id, patient_id | summary + transcript + profile + up to 5 previous summaries | If context load fails: return error to user. Cannot answer without context. |
| 2 | `answer_worker` | question, assembled context, viewer_role | grounded answer text (streamed) | Retry 1x. If failed: "We couldn't generate an answer right now. Try again in a moment." |
| 3 | (deterministic) | question, answer, summary_id, viewer_id | cached entry | If cache write fails: answer still delivered, just not cached. Log warning. |

### Pipeline: Process Document

Trigger: `document.uploaded`

```
document.uploaded
  → Step 1: Explain Document   (Claude Sonnet, with vision if image)
  → Step 2: Extract Health     (Claude Haiku)
  → Step 3: Update Profile     (deterministic merge)
  → Step 4: Detect Changes     (deterministic diff)
  → Emit: profile.updated
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | `explain_worker` | document text/image, patient profile | plain-language explanation | Retry 2x. If failed: store document, notify user "We're still processing your document." |
| 2 | `extract_worker` | document text + explanation, current profile | structured health data | Retry 2x. If failed: explanation still delivered, extraction skipped. |
| 3 | (deterministic) | extracted data, current profile | updated profile | Same merge rules as recording pipeline. |
| 4 | (deterministic) | previous profile, new profile | changes list | Pure comparison. |

### Pipeline: Process Voice Input

Trigger: `voice_input.received`

```
voice_input.received
  → Step 1: Extract Data       (Claude Haiku)
  → Step 2: Validate           (deterministic comparison)
  → Step 3: Present for Confirmation (return to user)
  → [user confirms]
  → Step 4: Update Profile     (deterministic merge)
  → Emit: profile.updated
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | `extract_worker` | voice transcript, current profile | structured update candidates | Retry 2x. If failed: "I couldn't understand that. Could you try again?" |
| 2 | (deterministic) | extracted data, current profile | validated data with conflict flags | Compare each extracted field against existing profile. Flag conflicts. |
| 3 | (deterministic) | validated data | confirmation cards returned to mobile app | User sees: "I heard you say your medication changed to metformin 500mg. Is that correct?" |
| 4 | (deterministic) | confirmed data | updated profile | Only runs after user confirms. Merge rules apply. |

Note: This pipeline has a human-in-the-loop step (Step 3 to Step 4). The pipeline pauses after Step 3. A new event `voice_input.confirmed` resumes at Step 4.

### Pipeline: Generate Viewer Suggestions

Trigger: `summary.viewed` (only on first view by a circle member)

```
summary.viewed [where viewer_role != 'patient' AND is_first_view]
  → Step 1: Check Cache        (deterministic)
  → Step 2: Generate Circle Suggestions (Claude Sonnet) [only if not cached]
  → Step 3: Cache Suggestions   (deterministic)
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | (deterministic) | summary_id, viewer_role | cached suggestions or null | If cached: return immediately, skip pipeline. |
| 2 | `suggest_worker` | summary, patient profile (scoped to sharing permissions), viewer_role | 2-3 role-appropriate suggestions | If failed: show no suggestions for this viewer. Not critical. |
| 3 | (deterministic) | suggestions, summary_id, viewer_role | cache entry | If cache fails: suggestions still returned, just regenerated on next view. |

Patient suggestions are generated during the recording pipeline (Step 3) and cached with the summary. Circle member suggestions are generated lazily on first view.

### Pipeline: Generate Appointment Prep

Trigger: `appointment.approaching`

```
appointment.approaching
  → Step 1: Load Journey Context (deterministic)
  → Step 2: Generate Prep       (Claude Sonnet)
  → Emit: prep.generated
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | (deterministic) | patient_id, appointment_type | profile + all summaries since last appointment of same type + action items + unresolved questions | If no previous data: prep still generated with minimal context. |
| 2 | `prep_worker` | journey context, appointment type, provider name | prep summary + 3-5 suggested questions | Retry 2x. If failed: no prep delivered. Not critical enough to block user flow. |

### Pipeline: Generate Circle Welcome

Trigger: `circle_member.added`

```
circle_member.added
  → Step 1: Load Shared Context  (deterministic)
  → Step 2: Generate Catch-up    (Claude Sonnet)
  → Emit: circle.notified
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | (deterministic) | patient_id, member_id, sharing_permissions | patient profile (scoped) + recent summaries (scoped) | If patient has no data yet: skip catch-up, send welcome only. |
| 2 | `adapt_worker` | shared context, member role, member name | welcome message + catch-up summary adapted for this member | If failed: send generic welcome without catch-up. |

### Pipeline: Detect Profile Changes

Trigger: `profile.updated`

```
profile.updated
  → Step 1: Evaluate Significance (deterministic)
  → Step 2: Generate Notifications (Claude Haiku) [only for significant changes]
  → Emit: circle.notified [conditional]
```

| Step | Worker | Input | Output | Failure behavior |
|---|---|---|---|---|
| 1 | (deterministic) | changed_fields, change significance rules | significant changes list (or empty) | Significance rules: medication change = high, new condition = high, care team change = medium, action item update = low. If no significant changes: pipeline ends. |
| 2 | `detect_changes_worker` | significant changes, patient profile, circle members with auto-share | notification messages per member | If failed: log changes, skip notifications. User can still see changes in profile. |

---

## 4. Agent Worker Specifications

Every worker is a stateless function wrapping a Claude API call. No worker knows about the pipeline it belongs to or other workers.

### `summarize_worker`

**Purpose**: Transform a medical conversation transcript into a patient-friendly summary.

**Model**: Claude Sonnet 4. Best balance of quality and speed for summarization. Sonnet handles Dutch medical conversations well and produces structured output reliably. Opus is overkill for summarization; Haiku lacks the nuance for patient-friendly rewriting.

**System prompt**:
```
You are a medical conversation summarizer for Ditto Care, a Dutch healthcare app.

Your job: transform a doctor-patient conversation transcript into a clear, patient-friendly summary in the same language as the transcript.

Rules:
- Write in the patient's language (Dutch or English, matching the transcript)
- Use plain language. Replace medical jargon with explanations.
- Structure: What was discussed → What was decided → What happens next
- Include specific names, dates, medications, and dosages mentioned
- If the transcript references previous appointments, note the connection
- Never add information not in the transcript
- Never provide medical advice or interpretation beyond what the doctor said
- Keep it scannable: short paragraphs, bold key terms, bullet lists for action items

Output format: Markdown string. No JSON wrapping.
```

**Input schema**:
```json
{
  "transcript": "string (full conversation text)",
  "patient_profile": {
    "conditions": ["string"],
    "medications": [{"name": "string", "dosage": "string"}],
    "care_team": [{"name": "string", "role": "string"}]
  },
  "previous_summaries": [
    {"date": "ISO date", "title": "string", "provider": "string"}
  ],
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "summary_text": "string (markdown)",
  "title": "string (short, e.g. 'Oncology follow-up with Dr. van der Berg')",
  "key_topics": ["string"],
  "action_items": [
    {"description": "string", "due_date": "ISO date or null", "assigned_to": "patient|provider"}
  ]
}
```

**Grounding rules**: Only information from the transcript. If patient_profile or previous_summaries are provided, use them for context (e.g., "This is your third appointment with Dr. X") but never inject profile data into the summary as if the doctor said it.

**Error handling**: Retry 2x with exponential backoff (1s, 3s). On final failure, return `{ error: "summarization_failed", transcript_id }`. Pipeline halts.

---

### `extract_worker`

**Purpose**: Extract structured health data from unstructured text (transcript, document, or voice input).

**Model**: Claude Haiku 3.5. Extraction is a structured output task that doesn't need creative reasoning. Haiku is 10x cheaper than Sonnet and handles schema-constrained extraction reliably. Speed matters because extraction runs in parallel with summarization.

**System prompt**:
```
You are a medical data extractor for Ditto Care. Extract structured health data from the provided text.

Rules:
- Extract ONLY what is explicitly stated. Never infer or assume.
- For medications: extract exact name, dosage, frequency, and whether it's new, changed, or continuing
- For conditions: extract exact terminology used, whether it's a new diagnosis or existing
- For care team: extract names and roles
- For action items: extract with dates if mentioned
- For dates: use ISO 8601 format
- If something is ambiguous, set confidence to "low" and include the original quote
- Dutch medication names: use the brand name as stated, add generic name if mentioned

Output must conform exactly to the provided JSON schema. Return empty arrays for categories with no data.
```

**Input schema**:
```json
{
  "text": "string (transcript, document text, or voice transcript)",
  "text_type": "transcript | document | voice_input",
  "current_profile": {
    "medications": [{"name": "string", "dosage": "string", "frequency": "string"}],
    "conditions": [{"name": "string", "status": "string"}],
    "care_team": [{"name": "string", "role": "string", "facility": "string"}]
  },
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "medications": [
    {
      "name": "string",
      "generic_name": "string or null",
      "dosage": "string",
      "frequency": "string",
      "status": "new | changed | discontinued | continuing",
      "previous_value": "string or null (if changed/discontinued)",
      "confidence": "high | medium | low",
      "source_quote": "string"
    }
  ],
  "conditions": [
    {
      "name": "string",
      "status": "new_diagnosis | existing | resolved",
      "details": "string or null",
      "confidence": "high | medium | low",
      "source_quote": "string"
    }
  ],
  "care_team": [
    {
      "name": "string",
      "role": "string",
      "facility": "string or null",
      "is_new": true
    }
  ],
  "action_items": [
    {
      "description": "string",
      "due_date": "ISO date or null",
      "assigned_to": "patient | provider",
      "source_quote": "string"
    }
  ],
  "appointments": [
    {
      "type": "string",
      "date": "ISO date or null",
      "provider": "string or null",
      "notes": "string or null"
    }
  ],
  "vitals": [
    {
      "type": "string (e.g., blood_pressure, weight, HbA1c)",
      "value": "string",
      "unit": "string",
      "date": "ISO date or null"
    }
  ]
}
```

**Grounding rules**: Every extracted item must have a `source_quote` with the verbatim text it was extracted from. If no data exists for a category, return an empty array. Never fill in "likely" values.

**Error handling**: Retry 2x. On failure, pipeline continues without extraction (non-critical for summary delivery). Log the failure for manual review.

---

### `explain_worker`

**Purpose**: Transform a medical document (letter, lab result, discharge report) into a patient-friendly explanation.

**Model**: Claude Sonnet 4. Documents require nuanced rewriting and contextual awareness (connecting this document to the patient's known journey). Haiku is too terse for the explanatory depth patients need.

**System prompt**:
```
You are a medical document explainer for Ditto Care. Transform medical documents into clear, patient-friendly explanations.

Rules:
- Write in the same language as the document
- Explain what the document IS first (e.g., "This is a letter from your oncologist to your GP about your recent scan results")
- Explain each section in plain language
- Highlight what matters most to the patient: results, changes, next steps
- If the patient has a known health profile, connect the document to their journey (e.g., "This scan is the follow-up to your treatment that started in January")
- Never add medical interpretation beyond what the document states
- For lab results: explain what each value means in context, whether it's normal/abnormal, and what the trend is if previous values are available
- Flag anything that seems urgent or requires action

Output format: Markdown string with clear headings.
```

**Input schema**:
```json
{
  "document_text": "string (OCR text or typed content)",
  "doc_type": "letter | lab_result | discharge | prescription | referral | other",
  "patient_profile": {
    "conditions": ["string"],
    "medications": [{"name": "string", "dosage": "string"}],
    "recent_summaries": [{"date": "ISO date", "title": "string"}]
  },
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "explanation_text": "string (markdown)",
  "document_type_detected": "string",
  "key_findings": ["string"],
  "action_items": [
    {"description": "string", "urgency": "routine | soon | urgent"}
  ],
  "connections_to_journey": ["string (references to known profile data)"]
}
```

**Grounding rules**: Only explain what the document says. If the document references tests or results not included, note "this references a test result that isn't in the document" rather than guessing.

**Error handling**: Retry 2x. On failure, store raw document and notify user that processing is pending.

---

### `suggest_worker`

**Purpose**: Generate 2-3 contextual suggestion questions a user would likely want answered after reading a summary.

**Model**: Claude Sonnet 4. Suggestion quality directly impacts engagement. The questions must feel specific and personally relevant, not generic. Sonnet's reasoning ability produces better questions than Haiku. The cost is negligible (one call per summary, short output).

**System prompt**:
```
You are generating follow-up questions for a patient who just read their medical summary on Ditto Care.

Rules:
- Generate exactly 2-3 questions
- Questions must be specific to THIS conversation, not generic medical questions
- Questions should address things the patient likely wants to understand better
- If the patient has previous summaries, include at least one question that connects appointments (e.g., "How does this relate to what was discussed in January?")
- Frame questions from the viewer's perspective:
  - For patients: "What does [specific term] mean for my situation?"
  - For care circle partners: "What does this mean for daily care?"
  - For care circle friends/family: "How is [patient] doing compared to last time?"
- Questions must be answerable from the conversation transcript and patient journey data
- Keep questions under 60 characters when possible
- Write in the same language as the summary

Output: JSON array of question strings. Nothing else.
```

**Input schema**:
```json
{
  "summary_text": "string",
  "patient_profile": {
    "conditions": ["string"],
    "medications": [{"name": "string", "dosage": "string"}]
  },
  "previous_summaries": [
    {"date": "ISO date", "title": "string", "key_topics": ["string"]}
  ],
  "viewer_role": "patient | partner | child | friend | caregiver",
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "suggestions": [
    {
      "question": "string",
      "reasoning": "string (why this question is relevant, for logging only)"
    }
  ]
}
```

**Grounding rules**: Questions must be answerable from available data. If there are no previous summaries, don't generate cross-appointment questions. If the summary is very short (under 200 words), generate only 2 questions.

**Error handling**: Retry 1x. On failure, summary displays without suggestions. Suggestions are an enhancement.

---

### `answer_worker`

**Purpose**: Generate a grounded answer to a patient's question about their medical conversation.

**Model**: Claude Sonnet 4. Answers require careful reasoning over long context (transcript + profile + previous summaries), precise grounding, and empathetic tone. Sonnet balances quality with latency (must stream first token in under 3 seconds). Opus would be higher quality but too slow for interactive Q&A. Haiku is too shallow for nuanced medical explanations.

**System prompt**:
```
You are answering a patient's question about their medical conversation on Ditto Care.

Rules:
- Answer ONLY using information from the provided conversation transcript, summary, and patient journey data
- Quote the doctor when relevant: "Dr. [name] mentioned that..."
- If the question cannot be answered from available data, say so clearly: "This wasn't discussed in your conversation with Dr. [name]. You might want to ask about this at your next appointment."
- Never provide medical advice. Never say "you should" about treatment decisions.
- Connect to previous appointments when relevant and available
- Write in the same language as the question
- Be warm but precise. This is a patient who may be anxious.
- Keep answers between 100-300 words. Longer only if the question genuinely requires it.
- End with source attribution: "Based on your conversation with [doctor] on [date]."
- Include the safety note: "For medical advice, always contact your care team."

Audience adaptation:
- For patients: personal, empathetic, focused on "what this means for you"
- For care circle members: informative, practical, focused on "what this means for [patient] and what you can do"
```

**Input schema**:
```json
{
  "question": "string",
  "summary_text": "string",
  "transcript_text": "string",
  "patient_profile": {
    "conditions": ["string"],
    "medications": [{"name": "string", "dosage": "string"}],
    "care_team": [{"name": "string", "role": "string"}]
  },
  "previous_summaries": [
    {"date": "ISO date", "title": "string", "summary_text": "string"}
  ],
  "viewer_role": "patient | partner | child | friend | caregiver",
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "answer_text": "string (markdown)",
  "sources_referenced": [
    {"type": "transcript | previous_summary", "date": "ISO date", "quote": "string"}
  ],
  "could_not_answer": false,
  "disclaimer": "string"
}
```

**Grounding rules**: Strict. If the information isn't in the provided context, don't fill the gap with general medical knowledge. The only exception: explaining a term in plain language (e.g., "A colonoscopy is a procedure where...") when the term was used in the conversation but not explained.

**Error handling**: Retry 1x. On failure, show user-facing error: "We couldn't generate an answer right now. Please try again." Stream responses for perceived speed.

---

### `adapt_worker`

**Purpose**: Transform a summary into an audience-adapted version for a specific care circle member.

**Model**: Claude Sonnet 4. Audience adaptation requires understanding the relationship dynamics, what matters to each role, and how to adjust tone and detail level. This is a creative rewriting task that Haiku handles poorly.

**System prompt**:
```
You are adapting a medical summary for a specific care circle member on Ditto Care.

The patient has shared this summary with a member of their care circle. Your job is to rewrite it for that person's perspective and needs.

Adaptation rules by role:
- Partner/spouse: Full detail. Emphasize action items, medication changes, what they can help with. Practical tone.
- Adult child: Clear but not clinical. Focus on "how is mom/dad doing" and "what should I know." Reassuring when appropriate, honest when not.
- Friend: High-level. "Here's how things are going." No clinical detail unless the patient shared it. Supportive tone.
- Caregiver: Professional detail. Medication schedules, care instructions, next appointments. Structured for handoff.
- Parent (of adult patient): Simplified. Focus on wellbeing and next steps. Minimize alarming detail unless critical.

General rules:
- Only include information the patient has permission-shared
- Write in the target language (may differ from summary language)
- Keep it shorter than the original summary
- Include "What you can do" section when relevant
- Never include information not in the original summary
- Attribute: "From [patient]'s appointment with [doctor] on [date]"
```

**Input schema**:
```json
{
  "summary_text": "string",
  "patient_name": "string",
  "member_name": "string",
  "member_role": "partner | child | friend | caregiver | parent",
  "sharing_permissions": {
    "share_medications": true,
    "share_conditions": true,
    "share_action_items": true,
    "share_full_summary": true
  },
  "target_language": "string (nl/en/tr/ar)",
  "doctor_name": "string",
  "appointment_date": "ISO date"
}
```

**Output schema**:
```json
{
  "adapted_text": "string (markdown)",
  "what_you_can_do": ["string (action items for circle member)"],
  "tone_used": "string (brief description for logging)"
}
```

**Grounding rules**: If `sharing_permissions.share_medications` is false, never mention medications even if they're in the summary. Respect every permission flag. When in doubt about what's shared, omit.

**Error handling**: Retry 1x. On failure, send generic notification to circle member ("New summary shared from [patient]") without the adapted content.

---

### `prep_worker`

**Purpose**: Generate an appointment preparation package: what happened since last visit, suggested questions, unresolved items.

**Model**: Claude Sonnet 4. Prep requires synthesizing across multiple summaries and the health profile to produce a coherent narrative. The output must feel like a knowledgeable assistant briefing you before a meeting. Haiku can't maintain coherence across this much context.

**System prompt**:
```
You are preparing a patient for an upcoming medical appointment on Ditto Care.

Your job: create a concise prep document the patient can review the night before or morning of their appointment.

Structure:
1. "Since your last visit" — what changed (medications, symptoms, test results, life events)
2. "Open items" — things left unresolved from previous appointments
3. "Suggested questions" — 3-5 questions personalized to this patient's situation and this appointment type
4. "Bring with you" — practical reminders (medication list, test results, referral letter)

Rules:
- Only reference information from the patient's actual journey data
- Questions should be specific, not generic ("Ask about the nausea you've been experiencing since starting metformin" not "Ask about side effects")
- If this is a first appointment with a new provider, adjust: include a brief health overview instead of "since last visit"
- Write in the patient's language
- Keep the entire prep under 500 words
- Tone: supportive, practical, like a knowledgeable friend helping you prepare
```

**Input schema**:
```json
{
  "appointment_type": "string (oncology | cardiology | gp | specialist | other)",
  "provider_name": "string",
  "patient_profile": {
    "conditions": ["string"],
    "medications": [{"name": "string", "dosage": "string"}],
    "action_items": [{"description": "string", "status": "open | done"}]
  },
  "summaries_since_last_appointment": [
    {"date": "ISO date", "title": "string", "summary_text": "string", "action_items": ["string"]}
  ],
  "previous_appointment_with_provider": {
    "date": "ISO date or null",
    "summary_text": "string or null"
  },
  "language": "string (nl/en)"
}
```

**Output schema**:
```json
{
  "prep_text": "string (markdown)",
  "suggested_questions": [
    {"question": "string", "reason": "string (why this question matters, for logging)"}
  ],
  "items_to_bring": ["string"],
  "is_first_visit_with_provider": false
}
```

**Grounding rules**: Questions must come from the patient's actual data. "Ask about your HbA1c trend" only if HbA1c values exist in the profile. Never generate generic appointment tips.

**Error handling**: Retry 2x. On failure, no prep is delivered. Patient gets a push notification about the upcoming appointment without the AI-generated prep content.

---

### `detect_changes_worker`

**Purpose**: Generate human-readable notifications about significant profile changes for care circle members.

**Model**: Claude Haiku 3.5. The change detection itself is deterministic (diff engine). This worker only formats the notification text, which is a simple templated generation task. Haiku is sufficient and fast.

**System prompt**:
```
You are generating a notification message about a health profile change for a care circle member on Ditto Care.

Input: a list of significant changes and the relationship of the recipient to the patient.

Rules:
- Be clear and factual about what changed
- Adapt tone to the recipient's role (partner: direct; child: gentle; friend: brief)
- Never editorialize or interpret the medical significance of changes
- Keep under 100 words per notification
- Include: what changed, when it changed, and where the full summary is
- Write in the recipient's language
```

**Input schema**:
```json
{
  "changes": [
    {
      "field": "string (medication | condition | care_team | action_item)",
      "description": "string",
      "significance": "high | medium"
    }
  ],
  "patient_name": "string",
  "member_name": "string",
  "member_role": "partner | child | friend | caregiver",
  "target_language": "string"
}
```

**Output schema**:
```json
{
  "notification_text": "string",
  "notification_title": "string (short, for push notification)"
}
```

**Grounding rules**: Only describe changes provided in input. Never add context or medical explanation.

**Error handling**: Retry 1x. On failure, send generic "Profile updated" notification.

---

### `translate_worker`

**Purpose**: Translate a summary or adapted text to a target language while preserving medical accuracy.

**Model**: Claude Haiku 3.5. Translation is a well-defined task that Haiku handles competently for the language pairs Ditto needs (NL, EN, TR, AR, Papiamentu). The key risk is medical terminology accuracy, handled by the grounding rules. Using Sonnet would be 10x more expensive with marginal quality improvement for translation.

**System prompt**:
```
You are translating a medical summary for Ditto Care.

Rules:
- Translate the full text to the target language
- Preserve all medical terms accurately. When in doubt, keep the Dutch/English medical term in parentheses alongside the translation
- Maintain the same structure, formatting, and emphasis as the original
- Do not add, remove, or interpret any content
- For medication names: keep the brand/generic name as-is (do not translate medication names)
- For doctor names and facility names: keep as-is
- Preserve markdown formatting
```

**Input schema**:
```json
{
  "text": "string (markdown)",
  "source_language": "string (nl/en)",
  "target_language": "string (nl/en/tr/ar/pap)",
  "text_type": "summary | adapted_summary | notification | prep"
}
```

**Output schema**:
```json
{
  "translated_text": "string (markdown)",
  "untranslated_terms": ["string (medical terms kept in original language)"]
}
```

**Grounding rules**: Never translate medication names, doctor names, or facility names. If a medical term has no established equivalent in the target language, keep the original in parentheses.

**Error handling**: Retry 1x. On failure, deliver content in original language with a note: "Translation unavailable. Showing in [original language]."

---

## 5. Health Profile Store

The profile store is the brain's memory. Every worker reads from it for context and writes back with new extractions.

### Full JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "patient_id": { "type": "string" },
    "version": { "type": "integer", "description": "Monotonically increasing version number" },
    "last_updated": { "type": "string", "format": "date-time" },
    "created_at": { "type": "string", "format": "date-time" },

    "demographics": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "date_of_birth": { "type": "string", "format": "date" },
        "language_primary": { "type": "string" },
        "language_secondary": { "type": ["string", "null"] }
      }
    },

    "conditions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "status": { "type": "string", "enum": ["active", "resolved", "monitoring"] },
          "diagnosed_date": { "type": ["string", "null"], "format": "date" },
          "resolved_date": { "type": ["string", "null"], "format": "date" },
          "notes": { "type": "string" },
          "source_event_id": { "type": "string" },
          "confidence": { "type": "string", "enum": ["high", "medium", "low"] },
          "last_mentioned": { "type": "string", "format": "date-time" }
        },
        "required": ["id", "name", "status", "source_event_id", "confidence"]
      }
    },

    "medications": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "generic_name": { "type": ["string", "null"] },
          "dosage": { "type": "string" },
          "frequency": { "type": "string" },
          "status": { "type": "string", "enum": ["active", "discontinued", "paused"] },
          "prescribed_date": { "type": ["string", "null"], "format": "date" },
          "discontinued_date": { "type": ["string", "null"], "format": "date" },
          "prescribed_by": { "type": ["string", "null"] },
          "reason": { "type": ["string", "null"] },
          "source_event_id": { "type": "string" },
          "confidence": { "type": "string", "enum": ["high", "medium", "low"] },
          "last_mentioned": { "type": "string", "format": "date-time" }
        },
        "required": ["id", "name", "dosage", "status", "source_event_id", "confidence"]
      }
    },

    "care_team": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "role": { "type": "string" },
          "facility": { "type": ["string", "null"] },
          "first_seen": { "type": "string", "format": "date" },
          "last_seen": { "type": "string", "format": "date" },
          "source_event_id": { "type": "string" }
        },
        "required": ["id", "name", "role", "source_event_id"]
      }
    },

    "action_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "status": { "type": "string", "enum": ["open", "done", "cancelled"] },
          "due_date": { "type": ["string", "null"], "format": "date" },
          "assigned_to": { "type": "string", "enum": ["patient", "provider"] },
          "source_event_id": { "type": "string" },
          "created_at": { "type": "string", "format": "date-time" },
          "completed_at": { "type": ["string", "null"], "format": "date-time" }
        },
        "required": ["id", "description", "status", "source_event_id"]
      }
    },

    "vitals_history": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": { "type": "string" },
          "value": { "type": "string" },
          "unit": { "type": "string" },
          "date": { "type": "string", "format": "date" },
          "source_event_id": { "type": "string" }
        },
        "required": ["type", "value", "unit", "date", "source_event_id"]
      }
    },

    "appointments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "type": { "type": "string" },
          "date": { "type": "string", "format": "date-time" },
          "provider_id": { "type": ["string", "null"] },
          "status": { "type": "string", "enum": ["scheduled", "completed", "cancelled"] },
          "summary_id": { "type": ["string", "null"] },
          "source_event_id": { "type": "string" }
        },
        "required": ["id", "type", "date", "status", "source_event_id"]
      }
    },

    "journey_events": {
      "type": "array",
      "description": "Timeline of significant health events auto-detected from summaries",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "date": { "type": "string", "format": "date" },
          "type": { "type": "string", "enum": ["diagnosis", "treatment_start", "treatment_change", "treatment_end", "procedure", "milestone", "other"] },
          "description": { "type": "string" },
          "related_condition_id": { "type": ["string", "null"] },
          "source_event_id": { "type": "string" }
        },
        "required": ["id", "date", "type", "description", "source_event_id"]
      }
    },

    "circle_members": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "member_id": { "type": "string" },
          "name": { "type": "string" },
          "role": { "type": "string", "enum": ["partner", "child", "parent", "friend", "caregiver"] },
          "language": { "type": "string" },
          "auto_share": { "type": "boolean" },
          "sharing_permissions": {
            "type": "object",
            "properties": {
              "share_medications": { "type": "boolean" },
              "share_conditions": { "type": "boolean" },
              "share_action_items": { "type": "boolean" },
              "share_full_summary": { "type": "boolean" }
            }
          },
          "added_at": { "type": "string", "format": "date-time" }
        },
        "required": ["member_id", "name", "role", "language", "auto_share", "sharing_permissions"]
      }
    }
  },
  "required": ["patient_id", "version", "last_updated", "created_at"]
}
```

### Read/Write API

```
GET  /profiles/{patient_id}                    → full profile (latest version)
GET  /profiles/{patient_id}?version={n}        → profile at specific version
GET  /profiles/{patient_id}/medications         → medications array only
GET  /profiles/{patient_id}/conditions          → conditions array only
GET  /profiles/{patient_id}/care_team           → care team array only
GET  /profiles/{patient_id}/action_items        → action items (filterable by status)
GET  /profiles/{patient_id}/journey             → journey events (timeline)
GET  /profiles/{patient_id}/history             → audit log of all changes
GET  /profiles/{patient_id}/diff?from={v1}&to={v2} → diff between two versions

POST /profiles/{patient_id}/merge              → apply extracted data (merge operation)
     Body: { extracted_data, source_event_id, worker_id }
     Returns: { new_version, changes[], conflicts[] }

PUT  /profiles/{patient_id}/{section}/{item_id} → manual update (user correction)
     Body: { field, new_value, reason: "user_correction" }
     Returns: { new_version }

POST /profiles/{patient_id}/resolve-conflict    → resolve a detected conflict
     Body: { conflict_id, chosen_value, reason }
     Returns: { new_version }
```

### Change Detection (Diff Engine)

The diff engine compares two profile versions and produces a structured changeset:

```json
{
  "from_version": 12,
  "to_version": 13,
  "changes": [
    {
      "field": "medications",
      "change_type": "added",
      "item": { "name": "metformin", "dosage": "500mg" },
      "significance": "high"
    },
    {
      "field": "medications",
      "change_type": "modified",
      "item_id": "med_abc",
      "before": { "dosage": "10mg" },
      "after": { "dosage": "20mg" },
      "significance": "high"
    },
    {
      "field": "action_items",
      "change_type": "added",
      "item": { "description": "Blood test in 3 weeks" },
      "significance": "medium"
    }
  ]
}
```

**Significance scoring**:

| Change type | Significance |
|---|---|
| New medication | high |
| Medication dosage change | high |
| Medication discontinued | high |
| New condition/diagnosis | high |
| Condition status change | high |
| New care team member | medium |
| New action item | medium |
| Action item completed | low |
| Vital recorded | low |
| Appointment scheduled | medium |

### Conflict Resolution Rules

Conflicts occur when extracted data disagrees with existing profile data.

| Scenario | Rule |
|---|---|
| New medication extracted, no match in profile | Add with `confidence` from extraction. No conflict. |
| Medication dosage differs from profile | If source is more recent: auto-update, log change. If source is older: flag conflict for user resolution. |
| Medication extracted with `confidence: low` | Never auto-update. Present as confirmation card to user. |
| Two workers update the same field simultaneously | Last-write-wins with both writes logged. In practice, this is rare because pipelines run sequentially within a patient scope. |
| Contradictory conditions from different appointments | Store both. Flag as `profile.conflict_detected`. Present to user: "Your oncologist mentioned [X] but your GP said [Y]. Which is current?" |
| User manually corrects a field | User correction always wins. Mark the field as `user_verified: true`. Future extractions with conflicting data trigger a confirmation rather than auto-update. |

### Audit Log

Every write to the profile store is logged:

```json
{
  "log_id": "log_a1b2c3",
  "patient_id": "pat_x1y2z3",
  "timestamp": "2026-04-04T14:30:05Z",
  "action": "merge",
  "worker_id": "extract_worker",
  "source_event_id": "evt_d4e5f6",
  "correlation_id": "corr_m1n2o3",
  "version_before": 12,
  "version_after": 13,
  "changes": [ ... ],
  "conflicts_detected": [ ... ]
}
```

### Versioning

Every mutation increments the version counter. The full profile at any version can be reconstructed by replaying the audit log from version 0 (creation) through version N. This enables:

- Debugging: "What did the profile look like when this summary was generated?"
- Rollback: User disputes a change. Revert to previous version.
- Compliance: GDPR right of access. Show exactly what data was held at any point.

Implementation: Store the current profile as-is (for fast reads). Store each changeset in the audit log (for reconstruction). Periodically snapshot full profiles to avoid replaying long chains.

---

## 6. Request Flow Scenarios

### Scenario 1: Patient records oncologist appointment

Patient Mara (pat_001) finishes recording a 12-minute oncology appointment with Dr. van der Berg at Erasmus MC.

**Step 0: Event emitted**

Mobile app emits:

```json
{
  "event_id": "evt_rec_001",
  "event_type": "recording.completed",
  "timestamp": "2026-04-04T14:30:00Z",
  "patient_id": "pat_001",
  "source": "mobile_app",
  "correlation_id": "corr_rec_001",
  "payload": {
    "transcript_id": "trx_001",
    "patient_id": "pat_001",
    "transcript_text": "Dr. van der Berg: Goedemiddag Mara, hoe gaat het? Mara: Goed, een beetje zenuwachtig voor de uitslag... [full 12-minute transcript, ~4000 words]...",
    "recording_duration_s": 720,
    "detected_language": "nl"
  }
}
```

**Step 1a: Summarize (parallel)**

Pipeline dispatches `summarize_worker`:

```json
// Input
{
  "transcript": "[full transcript]",
  "patient_profile": {
    "conditions": ["Darmkanker stadium 3b"],
    "medications": [
      {"name": "Capecitabine", "dosage": "1500mg 2x daags"}
    ],
    "care_team": [
      {"name": "Dr. van der Berg", "role": "Oncoloog"}
    ]
  },
  "previous_summaries": [
    {"date": "2026-01-15", "title": "Oncologie controle - Dr. van der Berg", "provider": "Dr. van der Berg"},
    {"date": "2025-11-20", "title": "Start chemotherapie - Dr. van der Berg", "provider": "Dr. van der Berg"}
  ],
  "language": "nl"
}

// Output (Claude Sonnet, ~3 seconds)
{
  "summary_text": "## Oncologie controle — Dr. van der Berg, Erasmus MC\n\n**Scanresultaten zijn positief.** De CT-scan van vorige week laat zien dat de tumor kleiner is geworden na drie rondes chemotherapie. Dr. van der Berg noemt dit een \"goede respons op de behandeling.\"\n\n**Medicatie wijziging.** Je stopt met capecitabine en gaat over op oxaliplatin infusen, elke drie weken. De eerste infuus is gepland op 18 april. Dit is een verandering ten opzichte van de tabletbehandeling die je sinds november volgt.\n\n**Wat je kunt verwachten.** Oxaliplatin kan tintelingen in handen en voeten veroorzaken, vooral bij kou. Dr. van der Berg raadt aan om handschoenen te dragen bij het openen van de koelkast.\n\n**Volgende stappen**\n- Eerste oxaliplatin infuus: 18 april 2026\n- Bloedonderzoek: 15 april (3 dagen voor infuus)\n- Volgende controle bij Dr. van der Berg: 9 mei 2026",
  "title": "Oncologie controle — Dr. van der Berg",
  "key_topics": ["scan_resultaten", "medicatie_wijziging", "oxaliplatin", "bijwerkingen"],
  "action_items": [
    {"description": "Bloedonderzoek laten doen", "due_date": "2026-04-15", "assigned_to": "patient"},
    {"description": "Eerste oxaliplatin infuus", "due_date": "2026-04-18", "assigned_to": "provider"},
    {"description": "Controle afspraak", "due_date": "2026-05-09", "assigned_to": "patient"}
  ]
}
```

**Step 1b: Extract (parallel with 1a)**

Pipeline dispatches `extract_worker`:

```json
// Input
{
  "text": "[full transcript]",
  "text_type": "transcript",
  "current_profile": {
    "medications": [{"name": "Capecitabine", "dosage": "1500mg 2x daags", "frequency": "dagelijks"}],
    "conditions": [{"name": "Darmkanker stadium 3b", "status": "active"}],
    "care_team": [{"name": "Dr. van der Berg", "role": "Oncoloog", "facility": "Erasmus MC"}]
  },
  "language": "nl"
}

// Output (Claude Haiku, ~1.5 seconds)
{
  "medications": [
    {
      "name": "Capecitabine",
      "generic_name": null,
      "dosage": "1500mg 2x daags",
      "frequency": "dagelijks",
      "status": "discontinued",
      "previous_value": null,
      "confidence": "high",
      "source_quote": "We stoppen met de capecitabine tabletten"
    },
    {
      "name": "Oxaliplatin",
      "generic_name": null,
      "dosage": "infuus",
      "frequency": "elke 3 weken",
      "status": "new",
      "previous_value": null,
      "confidence": "high",
      "source_quote": "We gaan over op oxaliplatin infusen, elke drie weken"
    }
  ],
  "conditions": [
    {
      "name": "Darmkanker stadium 3b",
      "status": "existing",
      "details": "Goede respons op behandeling, tumor is kleiner geworden",
      "confidence": "high",
      "source_quote": "De CT-scan laat zien dat de tumor kleiner is geworden"
    }
  ],
  "care_team": [],
  "action_items": [
    {
      "description": "Bloedonderzoek laten doen",
      "due_date": "2026-04-15",
      "assigned_to": "patient",
      "source_quote": "Drie dagen voor het infuus even bloed laten prikken"
    }
  ],
  "appointments": [
    {
      "type": "treatment",
      "date": "2026-04-18",
      "provider": "Dr. van der Berg",
      "notes": "Eerste oxaliplatin infuus"
    },
    {
      "type": "follow_up",
      "date": "2026-05-09",
      "provider": "Dr. van der Berg",
      "notes": "Controle afspraak"
    }
  ],
  "vitals": []
}
```

**Step 2: Update Profile (deterministic)**

Merge engine processes extracted data against current profile (version 12):

```json
// Merge result
{
  "new_version": 13,
  "changes": [
    {
      "field": "medications",
      "change_type": "modified",
      "item_id": "med_cap_001",
      "before": {"status": "active"},
      "after": {"status": "discontinued", "discontinued_date": "2026-04-04"},
      "significance": "high"
    },
    {
      "field": "medications",
      "change_type": "added",
      "item": {"id": "med_oxa_001", "name": "Oxaliplatin", "dosage": "infuus", "frequency": "elke 3 weken", "status": "active"},
      "significance": "high"
    },
    {
      "field": "appointments",
      "change_type": "added",
      "item": {"id": "apt_001", "type": "treatment", "date": "2026-04-18"},
      "significance": "medium"
    },
    {
      "field": "appointments",
      "change_type": "added",
      "item": {"id": "apt_002", "type": "follow_up", "date": "2026-05-09"},
      "significance": "medium"
    },
    {
      "field": "action_items",
      "change_type": "added",
      "item": {"id": "act_001", "description": "Bloedonderzoek laten doen", "due_date": "2026-04-15"},
      "significance": "medium"
    }
  ],
  "conflicts": []
}
```

**Step 3: Generate Suggestions**

Pipeline dispatches `suggest_worker`:

```json
// Input
{
  "summary_text": "[summary from step 1a]",
  "patient_profile": {
    "conditions": ["Darmkanker stadium 3b"],
    "medications": [{"name": "Oxaliplatin", "dosage": "infuus"}]
  },
  "previous_summaries": [
    {"date": "2026-01-15", "title": "Oncologie controle — Dr. van der Berg", "key_topics": ["bloedwaarden", "chemotherapie_voortgang"]},
    {"date": "2025-11-20", "title": "Start chemotherapie — Dr. van der Berg", "key_topics": ["capecitabine", "behandelplan"]}
  ],
  "viewer_role": "patient",
  "language": "nl"
}

// Output (Claude Sonnet, ~2 seconds)
{
  "suggestions": [
    {
      "question": "Waarom wordt er overgestapt van tabletten naar infusen?",
      "reasoning": "Major treatment change from capecitabine tablets to oxaliplatin infusions. Patient likely wants to understand why."
    },
    {
      "question": "Wat kan ik verwachten bij de tintelingen?",
      "reasoning": "Doctor mentioned neuropathy side effect. Patients worry about new side effects."
    },
    {
      "question": "Hoe verhouden deze scanresultaten zich tot januari?",
      "reasoning": "Cross-appointment question. Patient had a scan discussed in January. Connecting the two helps understand trajectory."
    }
  ]
}
```

**Step 4: Detect Changes (deterministic)**

Diff engine identifies 2 high-significance changes (medication discontinued, new medication added). This triggers downstream notification.

**Step 5a: Generate Circle Updates**

Mara's partner Hans has auto-share enabled. Pipeline dispatches `adapt_worker`:

```json
// Input
{
  "summary_text": "[summary from step 1a]",
  "patient_name": "Mara",
  "member_name": "Hans",
  "member_role": "partner",
  "sharing_permissions": {
    "share_medications": true,
    "share_conditions": true,
    "share_action_items": true,
    "share_full_summary": true
  },
  "target_language": "nl",
  "doctor_name": "Dr. van der Berg",
  "appointment_date": "2026-04-04"
}

// Output (Claude Sonnet, ~2 seconds)
{
  "adapted_text": "## Update van Mara's afspraak met Dr. van der Berg\n\nGoed nieuws: de scan laat zien dat de tumor kleiner is geworden. De chemotherapie werkt.\n\n**Medicatie verandering.** Mara stopt met de capecitabine tabletten en gaat over op oxaliplatin infusen. Het eerste infuus is op 18 april. Ze kan tintelingen in handen en voeten krijgen, vooral bij kou.\n\n**Wat er komt**\n- 15 april: bloedonderzoek\n- 18 april: eerste infuus (Erasmus MC)\n- 9 mei: volgende controle",
  "what_you_can_do": [
    "Rijd mee naar het eerste infuus op 18 april (duurt enkele uren)",
    "Let op tintelingen in handen en voeten, en houd handschoenen in de buurt",
    "Herinner Mara aan het bloedonderzoek op 15 april"
  ],
  "tone_used": "partner: direct, practical, reassuring where data supports it"
}
```

**Step 5b**: Skipped. Hans speaks Dutch.

**Events emitted**:

```json
[
  {
    "event_type": "summary.created",
    "patient_id": "pat_001",
    "correlation_id": "corr_rec_001",
    "payload": { "summary_id": "sum_001", "suggestion_ids": ["sug_001", "sug_002", "sug_003"] }
  },
  {
    "event_type": "profile.updated",
    "patient_id": "pat_001",
    "correlation_id": "corr_rec_001",
    "payload": { "changed_fields": ["medications", "appointments", "action_items"], "source_event_id": "evt_rec_001" }
  },
  {
    "event_type": "circle.notified",
    "patient_id": "pat_001",
    "correlation_id": "corr_rec_001",
    "payload": { "member_ids": ["mem_hans_001"], "summary_id": "sum_001", "update_type": "auto_share" }
  }
]
```

**Total pipeline time**: ~5-7 seconds (steps 1a and 1b parallel, rest sequential). Patient sees summary within 5 seconds. Suggestions attached. Hans gets notification within 7 seconds.

---

### Scenario 2: Circle member taps suggestion on shared summary

Hans (partner) opens the notification and views Mara's summary. The `summary.viewed` event fires.

**Event**:
```json
{
  "event_type": "summary.viewed",
  "patient_id": "pat_001",
  "payload": {
    "summary_id": "sum_001",
    "viewer_id": "mem_hans_001",
    "viewer_role": "partner",
    "is_first_view": true
  }
}
```

Since `viewer_role != 'patient'` and `is_first_view == true`, the Generate Viewer Suggestions pipeline fires. The `suggest_worker` generates partner-specific suggestions:

```json
{
  "suggestions": [
    {
      "question": "Wat houdt de overstap naar infusen praktisch in?",
      "reasoning": "Partner needs to understand logistics: how long does an infusion take, how often, transport."
    },
    {
      "question": "Hoe kan ik helpen met de bijwerkingen?",
      "reasoning": "Partner's primary concern is caregiving. Practical support for neuropathy."
    }
  ]
}
```

Hans taps "Wat houdt de overstap naar infusen praktisch in?" The `suggestion.tapped` event fires.

**Answer pipeline Step 1: Load Context**

Context is scoped to sharing permissions. Hans has full access (`share_full_summary: true`), so the answer worker gets:
- Mara's summary (the adapted version Hans sees)
- Original transcript (shared because `share_full_summary: true`)
- Mara's profile (scoped: medications, conditions, action items)
- Up to 5 previous summaries

If Hans only had `share_medications: true`, the context would be limited to medication-related portions of the transcript and summary.

**Answer pipeline Step 2: Generate Answer**

```json
// Input to answer_worker
{
  "question": "Wat houdt de overstap naar infusen praktisch in?",
  "summary_text": "[adapted summary Hans sees]",
  "transcript_text": "[full transcript]",
  "patient_profile": { "conditions": [...], "medications": [...] },
  "previous_summaries": [...],
  "viewer_role": "partner",
  "language": "nl"
}

// Output (Claude Sonnet, streamed, first token in ~1.5s)
{
  "answer_text": "Dr. van der Berg legde uit dat de oxaliplatin behandeling via een infuus gaat in het ziekenhuis, elke drie weken. Elk infuus duurt doorgaans twee tot drie uur.\n\nVoor Mara betekent dit concreet:\n- **18 april**: eerste infuus in Erasmus MC\n- Daarna elke drie weken een infuusdag\n- Drie dagen voor elk infuus moet bloed geprikt worden\n\nDr. van der Berg noemde ook dat oxaliplatin tintelingen kan veroorzaken in handen en voeten, vooral bij koude temperaturen. Hij adviseerde Mara om handschoenen te gebruiken bij het openen van de koelkast.\n\nAls partner kun je helpen door mee te rijden naar de infuusdagen (Mara kan zich moe voelen na het infuus) en door te letten op de tintelingen.\n\n*Op basis van Mara's gesprek met Dr. van der Berg op 4 april 2026. Neem voor medisch advies contact op met het behandelteam.*",
  "sources_referenced": [
    {"type": "transcript", "date": "2026-04-04", "quote": "We gaan over op oxaliplatin infusen, elke drie weken"}
  ],
  "could_not_answer": false,
  "disclaimer": "Op basis van Mara's gesprek met Dr. van der Berg op 4 april 2026. Neem voor medisch advies contact op met het behandelteam."
}
```

**Step 3: Cache Answer**

Answer cached with key `(sum_001, sug_hans_001, mem_hans_001)`. If Hans taps again or reopens, the cached answer loads instantly.

---

### Scenario 3: Patient says "They changed my medication to metformin 500mg"

Patient Jan (pat_002, diabetes) uses the "Tell Ditto" voice input.

**Event**:
```json
{
  "event_type": "voice_input.received",
  "patient_id": "pat_002",
  "correlation_id": "corr_voice_001",
  "payload": {
    "input_id": "vi_001",
    "patient_id": "pat_002",
    "transcript_text": "Ze hebben mijn medicijn veranderd naar metformine 500 milligram, twee keer per dag.",
    "duration_s": 5
  }
}
```

**Step 1: Extract Data**

```json
// extract_worker input
{
  "text": "Ze hebben mijn medicijn veranderd naar metformine 500 milligram, twee keer per dag.",
  "text_type": "voice_input",
  "current_profile": {
    "medications": [
      {"name": "Gliclazide", "dosage": "80mg", "frequency": "1x daags"}
    ],
    "conditions": [{"name": "Diabetes type 2", "status": "active"}],
    "care_team": [{"name": "Dr. Jansen", "role": "Huisarts", "facility": "Huisartsenpraktijk Kralingen"}]
  },
  "language": "nl"
}

// Output (Claude Haiku, ~1s)
{
  "medications": [
    {
      "name": "Metformine",
      "generic_name": "metformin",
      "dosage": "500mg",
      "frequency": "2x daags",
      "status": "new",
      "previous_value": null,
      "confidence": "high",
      "source_quote": "metformine 500 milligram, twee keer per dag"
    }
  ],
  "conditions": [],
  "care_team": [],
  "action_items": [],
  "appointments": [],
  "vitals": []
}
```

**Step 2: Validate (deterministic)**

Comparison engine detects:
- Jan currently takes Gliclazide 80mg (also a diabetes medication)
- New extraction: Metformine 500mg
- Both are diabetes medications. Likely a switch, not an addition.
- Ambiguity: Did they replace Gliclazide with Metformine, or add Metformine alongside it?

Validation result:
```json
{
  "extracted_items": [
    {
      "type": "medication",
      "item": {"name": "Metformine", "dosage": "500mg", "frequency": "2x daags"},
      "validation_status": "needs_clarification",
      "reason": "You currently take Gliclazide 80mg for diabetes. Is metformine replacing gliclazide, or taking it alongside?"
    }
  ],
  "conflicts": [
    {
      "field": "medications",
      "existing": {"name": "Gliclazide", "dosage": "80mg"},
      "new": {"name": "Metformine", "dosage": "500mg"},
      "question": "replacement_or_addition"
    }
  ]
}
```

**Step 3: Present for Confirmation**

Mobile app shows confirmation cards:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ✏️  I heard you say:                       │
│                                             │
│  ┌────────────────────────────────────────┐ │
│  │  💊 New medication                     │ │
│  │  Metformine 500mg, 2x daags            │ │
│  └────────────────────────────────────────┘ │
│                                             │
│  ❓ You currently take Gliclazide 80mg.     │
│     Did metformine replace gliclazide?      │
│                                             │
│  [ Yes, I stopped gliclazide ]              │
│  [ No, I take both now ]                    │
│  [ Edit details ]                           │
│  [ Cancel ]                                 │
│                                             │
└─────────────────────────────────────────────┘
```

Jan taps "Yes, I stopped gliclazide."

**Step 4: Update Profile**

New event `voice_input.confirmed`:
```json
{
  "event_type": "voice_input.confirmed",
  "patient_id": "pat_002",
  "correlation_id": "corr_voice_001",
  "payload": {
    "confirmed_actions": [
      {"type": "add_medication", "item": {"name": "Metformine", "dosage": "500mg", "frequency": "2x daags"}},
      {"type": "discontinue_medication", "item_id": "med_glic_001"}
    ]
  }
}
```

Profile update (version 8 to 9):
```json
{
  "new_version": 9,
  "changes": [
    {
      "field": "medications",
      "change_type": "modified",
      "item_id": "med_glic_001",
      "before": {"status": "active"},
      "after": {"status": "discontinued", "discontinued_date": "2026-04-04"},
      "significance": "high"
    },
    {
      "field": "medications",
      "change_type": "added",
      "item": {"id": "med_met_001", "name": "Metformine", "dosage": "500mg", "frequency": "2x daags", "status": "active"},
      "significance": "high"
    }
  ],
  "conflicts": []
}
```

Emits `profile.updated`, which triggers Detect Profile Changes. High-significance medication change detected. If Jan has circle members with auto-share, they receive a notification generated by `detect_changes_worker`.

---

## 7. Interface Integration

The mobile app never sees the internal pipeline architecture. It interacts with a clean API layer.

### REST API

```
POST   /api/v1/recordings          → Uploads transcript, triggers recording.completed
POST   /api/v1/documents           → Uploads document, triggers document.uploaded
POST   /api/v1/voice-input         → Submits voice transcript, triggers voice_input.received
POST   /api/v1/voice-input/confirm → Confirms voice extraction, triggers voice_input.confirmed
GET    /api/v1/summaries/{id}      → Returns summary + suggestions (pre-generated)
POST   /api/v1/summaries/{id}/ask  → Submits question (suggestion tap or custom), triggers pipeline
GET    /api/v1/profile             → Returns patient's health profile
PUT    /api/v1/profile/{section}/{id} → Manual profile correction
GET    /api/v1/prep/{appointment_id} → Returns appointment prep (pre-generated or triggers pipeline)
GET    /api/v1/circle/updates      → Returns pending circle updates for the authenticated member
POST   /api/v1/circle/members      → Adds circle member, triggers circle_member.added
```

### WebSocket / SSE for Streaming

Answer generation streams via Server-Sent Events:

```
GET /api/v1/summaries/{id}/ask/stream?question={text}

// SSE events:
event: answer.started
data: {"answer_id": "ans_001"}

event: answer.chunk
data: {"text": "Dr. van der Berg legde uit dat "}

event: answer.chunk
data: {"text": "de oxaliplatin behandeling via een infuus gaat..."}

event: answer.complete
data: {"answer_id": "ans_001", "sources": [...], "disclaimer": "..."}
```

Real-time pipeline progress (for summary generation):

```
GET /api/v1/recordings/{id}/status

// SSE events:
event: pipeline.step
data: {"step": "summarizing", "progress": 0.3}

event: pipeline.step
data: {"step": "extracting", "progress": 0.5}

event: pipeline.complete
data: {"summary_id": "sum_001", "suggestion_count": 3}
```

### Webhook Callbacks

For async pipelines that the app doesn't wait for (circle updates, appointment prep):

```
POST {app_webhook_url}/callbacks

{
  "event_type": "circle_update.ready",
  "patient_id": "pat_001",
  "member_id": "mem_hans_001",
  "summary_id": "sum_001",
  "adapted_summary_id": "asum_001"
}
```

The app uses this to trigger push notifications to circle members.

### API Authentication

All endpoints require a Bearer token. Profile data is scoped to the authenticated user. Circle members access shared data through their own token with permissions enforced server-side.

---

## 8. Smart Suggestions Interface Spec

Same user-facing behavior as defined in [Smart Suggestions Phase 1 spec](care-brain-phase1-smart-suggestions.md), implemented through the event-driven architecture.

### Generation Flow

Suggestions are pre-computed, not generated on view:

1. `recording.completed` triggers recording pipeline
2. Step 3 of pipeline: `suggest_worker` generates 2-3 patient suggestions
3. Suggestions stored alongside summary in the database
4. When patient views summary (`summary.viewed`): suggestions loaded from cache. No LLM call.
5. When circle member views summary (first view): `summary.viewed` event with `viewer_role != 'patient'` triggers Generate Viewer Suggestions pipeline. Lazy generation because circle member suggestions are role-specific and can't all be pre-computed.
6. After first view, circle member suggestions are cached per `(summary_id, viewer_role)`.

### Answer Flow

1. User taps a suggestion chip: app calls `POST /api/v1/summaries/{id}/ask`
2. Backend emits `suggestion.tapped` event
3. Answer Question pipeline runs
4. Answer streams back via SSE
5. Answer cached. Subsequent taps on same question return cached answer instantly.

### Circle Member Differentiation

| Viewer Role | Suggestion Style | Example |
|---|---|---|
| Patient | Personal, inward-looking | "Waarom wordt er overgestapt van tabletten naar infusen?" |
| Partner | Practical, caregiving-focused | "Hoe kan ik helpen met de bijwerkingen?" |
| Adult child | Wellbeing-focused, gentle | "Hoe gaat het met mama vergeleken met vorige keer?" |
| Friend | High-level, supportive | "Wat zijn de volgende stappen?" |
| Caregiver | Clinical, handoff-focused | "Zijn er veranderingen in het medicatieschema?" |

Detection happens via `viewer_role` in the `summary.viewed` event. The `suggest_worker` receives the role and adjusts its output accordingly.

### Performance Targets

| Action | Target | How achieved |
|---|---|---|
| Summary loads with suggestions visible | <500ms after summary text loads | Suggestions pre-computed. Loaded from database alongside summary. |
| First token of answer appears | <3 seconds | Claude Sonnet streaming. Context pre-assembled on tap. |
| Full answer rendered | <8 seconds | Streaming prevents perceived wait. |
| Repeat tap on same suggestion | <100ms | Cached answer served directly from database. |
| Circle member first view with suggestions | <4 seconds | Lazy generation via fast pipeline (single suggest_worker call). |

---

## 9. Trade-offs

### Pros

| Advantage | Detail |
|---|---|
| **Most production-ready** | Each pipeline is an independent, testable, deployable unit. Standard microservices patterns apply. |
| **Independent scaling** | The Answer Question pipeline can scale to 10x the recording pipeline without touching other code. |
| **Fault-tolerant** | If `suggest_worker` fails, the summary still ships. If `adapt_worker` fails for one circle member, others still get updates. Failures are isolated. |
| **Easy to extend** | Adding a new feature = define a new event type + new pipeline + new worker(s). No existing code changes. |
| **Optimal model per task** | Summarization uses Sonnet. Extraction uses Haiku. Translation uses Haiku. Each worker uses the cheapest model that meets its quality bar. |
| **Observable** | Every event has a correlation_id. Trace any user action through every pipeline step. Latency per step is measurable. Bottlenecks are visible. |
| **Audit-friendly** | Every profile mutation is logged. GDPR compliance is built into the architecture. |
| **Cacheable** | Suggestions and answers are deterministic per input. Cache aggressively, regenerate rarely. |

### Cons

| Disadvantage | Detail |
|---|---|
| **Most complex to set up** | Event bus, pipeline orchestrator, worker runtime, profile store, cache layer, API layer. That's six infrastructure components before the first LLM call. |
| **Requires event infrastructure** | In-process event emitter works for prototype. Production needs a real message bus with durability, ordering, and retry guarantees. |
| **Harder cross-cutting reasoning** | No single agent sees the full picture. If a feature needs "look at all summaries and find a pattern," it needs a new pipeline with broad context loading. The orchestrator model (Direction A) handles this more naturally. |
| **Cold-start problem** | New patients with one summary have a sparse profile. Suggestions and prep are less intelligent until 2-3 interactions accumulate context. |
| **Debugging distributed flows** | When something goes wrong, the cause may span multiple pipeline steps. Requires good tracing tooling. |
| **Over-engineering risk** | A 10-person team could spend months building infrastructure before shipping product value. This architecture earns its complexity at scale. At 35K users, a simpler approach might deliver faster. |

### When to Choose This Direction

- When reliability and observability are primary concerns
- When the team expects to scale specific features independently (e.g., Q&A gets 10x more load than summarization)
- When different features have different latency requirements (streaming answers vs. batch circle updates)
- When you need to A/B test individual workers (swap summarize_worker prompt without touching anything else)
- When GDPR audit requirements demand traceable data flows

### When NOT to Choose

- For a quick prototype where speed-to-learn matters more than architecture quality
- When the team is < 5 engineers and infrastructure overhead would consume capacity
- When cross-cutting reasoning (full-journey analysis) is the primary use case

---

## 10. Cost Model

### Per-Operation Costs

Token estimates based on Claude API pricing (April 2026 rates). Assumes average 4,000-word Dutch medical conversation transcript (~6,000 tokens).

**Full Recording Pipeline**

| Step | Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|---|
| Summarize | Sonnet 4 | ~8,000 (transcript + profile + prev summaries) | ~800 (summary + metadata) | $0.028 |
| Extract | Haiku 3.5 | ~7,000 (transcript + profile) | ~400 (structured data) | $0.006 |
| Suggest | Sonnet 4 | ~2,000 (summary + profile + prev titles) | ~200 (3 suggestions) | $0.007 |
| Adapt (per member) | Sonnet 4 | ~1,500 (summary + member info) | ~300 (adapted text) | $0.006 |
| **Total (1 circle member)** | | | | **$0.047** |
| **Total (3 circle members)** | | | | **$0.059** |

**Single Q&A Answer**

| Step | Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|---|
| Answer | Sonnet 4 | ~12,000 (transcript + summary + profile + prev summaries) | ~400 (answer) | $0.040 |
| **Total** | | | | **$0.040** |

**Voice Input Processing**

| Step | Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|---|
| Extract | Haiku 3.5 | ~1,500 (voice transcript + profile) | ~200 (structured data) | $0.002 |
| **Total** | | | | **$0.002** |

**Appointment Prep**

| Step | Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|---|
| Prep | Sonnet 4 | ~10,000 (profile + summaries since last visit) | ~500 (prep document) | $0.034 |
| **Total** | | | | **$0.034** |

### Monthly Cost at Scale

Assumptions:
- Each active user generates ~1.5 summaries/month (some months 0, some months 3)
- 30% of summary viewers tap at least 1 suggestion (average 1.5 questions)
- Average 1.5 circle members per patient with auto-share
- 10% of active users use voice input (average 2x/month)
- 20% of active users have appointment prep triggered (1x/month)

| Active Users | Summaries/mo | Q&A/mo | Voice/mo | Prep/mo | LLM cost/mo | Per-user/mo |
|---|---|---|---|---|---|---|
| 5,000 | 7,500 | 3,375 | 1,000 | 1,000 | $620 | $0.124 |
| 50,000 | 75,000 | 33,750 | 10,000 | 10,000 | $6,200 | $0.124 |
| 500,000 | 750,000 | 337,500 | 100,000 | 100,000 | $62,000 | $0.124 |

### Infrastructure Cost (Production)

| Component | Service | Monthly cost (50K users) |
|---|---|---|
| Event bus | Redis Streams on managed instance | $50-100 |
| Profile store | PostgreSQL (managed, e.g., Supabase, Neon) | $50-200 |
| Answer cache | Redis (same instance as event bus) | included |
| Compute (worker runtime) | Serverless functions (Vercel, AWS Lambda) | $100-300 |
| API layer | Included in compute | included |
| Monitoring/tracing | Datadog or similar | $100-200 |
| **Total infrastructure** | | **$300-800/mo** |

### Comparison with Direction A and B

| Dimension | Direction A (Orchestrator) | Direction B (Agent Swarm) | Direction C (Nervous System) |
|---|---|---|---|
| LLM cost per recording | Higher (orchestrator overhead adds ~$0.01/call) | Highest (agents converse, token-heavy) | **Lowest** (model-per-task optimization) |
| Infrastructure cost | Low (single service) | Medium (agent coordination) | Higher (event bus + store + workers) |
| Cost at 50K users | ~$8,000/mo | ~$12,000/mo | ~$7,000/mo |
| Cost predictability | Medium (orchestrator decisions vary) | Low (agent conversation length varies) | **High** (fixed pipeline steps, predictable tokens) |

Direction C wins on LLM cost because each worker uses the cheapest sufficient model. Haiku for extraction and translation ($0.002/call) vs. Sonnet for everything in Direction A ($0.028/call for the same extraction task).

---

## 11. Prototype Scope

Build the minimal system that demonstrates the architecture's value. Target: 2-3 days for a single developer.

### Components to Build

**1. Event Emitter** (TypeScript or Python)

Simple in-process pub/sub. No external dependencies.

```typescript
// event-bus.ts
type EventHandler = (event: Event) => Promise<void>;

class EventBus {
  private handlers: Map<string, EventHandler[]> = new Map();

  subscribe(eventType: string, handler: EventHandler): void { ... }
  emit(event: Event): Promise<void> { ... }  // calls all handlers sequentially
}
```

**2. Health Profile Store** (SQLite with JSON)

Single table. Profile is a JSON column. Audit log is a second table.

```sql
CREATE TABLE profiles (
  patient_id TEXT PRIMARY KEY,
  version INTEGER NOT NULL DEFAULT 1,
  profile JSON NOT NULL,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id TEXT NOT NULL,
  version INTEGER NOT NULL,
  worker_id TEXT,
  source_event_id TEXT,
  changes JSON NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE summaries (
  summary_id TEXT PRIMARY KEY,
  patient_id TEXT NOT NULL,
  summary_text TEXT NOT NULL,
  suggestions JSON,
  transcript_text TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE answer_cache (
  cache_key TEXT PRIMARY KEY,  -- hash of (summary_id, question, viewer_role)
  answer JSON NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**3. Four Core Workers**

Implement as plain functions. Each wraps a Claude API call using the Anthropic SDK.

```typescript
// workers/summarize.ts
async function summarizeWorker(input: SummarizeInput): Promise<SummarizeOutput> {
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 2000,
    system: SUMMARIZE_SYSTEM_PROMPT,
    messages: [{ role: "user", content: formatSummarizeInput(input) }]
  });
  return parseSummarizeOutput(response);
}

// workers/extract.ts   (Claude Haiku)
// workers/suggest.ts   (Claude Sonnet)
// workers/answer.ts    (Claude Sonnet, with streaming)
```

**4. Main Pipeline: Process Recording**

Wire the four workers into the recording pipeline with the event bus.

```typescript
// pipelines/process-recording.ts
eventBus.subscribe("recording.completed", async (event) => {
  const { transcript_text, patient_id } = event.payload;
  const profile = await profileStore.get(patient_id);
  const previousSummaries = await summaryStore.getRecent(patient_id, 5);

  // Step 1a + 1b: parallel
  const [summary, extracted] = await Promise.all([
    summarizeWorker({ transcript: transcript_text, patient_profile: profile, previous_summaries: previousSummaries, language: "nl" }),
    extractWorker({ text: transcript_text, text_type: "transcript", current_profile: profile, language: "nl" })
  ]);

  // Step 2: merge
  const mergeResult = await profileStore.merge(patient_id, extracted, event.event_id, "extract_worker");

  // Step 3: suggest
  const suggestions = await suggestWorker({ summary_text: summary.summary_text, patient_profile: profile, previous_summaries: previousSummaries, viewer_role: "patient", language: "nl" });

  // Store
  await summaryStore.save({ summary_id: generateId(), patient_id, ...summary, suggestions, transcript_text });

  // Emit
  await eventBus.emit({ event_type: "summary.created", patient_id, payload: { ... } });
  if (mergeResult.changes.length > 0) {
    await eventBus.emit({ event_type: "profile.updated", patient_id, payload: { changed_fields: mergeResult.changes.map(c => c.field) } });
  }
});
```

**5. Answer Pipeline**

```typescript
// pipelines/answer-question.ts
eventBus.subscribe("suggestion.tapped", async (event) => {
  const { summary_id, question_text, viewer_id, viewer_role } = event.payload;

  // Check cache
  const cached = await answerCache.get(summary_id, question_text, viewer_role);
  if (cached) return cached;

  // Load context
  const summary = await summaryStore.get(summary_id);
  const profile = await profileStore.get(summary.patient_id);
  const previousSummaries = await summaryStore.getRecent(summary.patient_id, 5);

  // Generate
  const answer = await answerWorker({
    question: question_text,
    summary_text: summary.summary_text,
    transcript_text: summary.transcript_text,
    patient_profile: profile,
    previous_summaries: previousSummaries,
    viewer_role,
    language: "nl"
  });

  // Cache
  await answerCache.set(summary_id, question_text, viewer_role, answer);

  return answer;
});
```

**6. CLI Interface**

```bash
# Run full pipeline on a conversation
$ node cli.js process-recording --transcript ./sample-transcripts/oncology-01.txt --patient pat_001

# Output:
# [Pipeline] recording.completed emitted
# [Step 1a] Summarizing... done (3.2s)
# [Step 1b] Extracting... done (1.4s)
# [Step 2]  Profile updated: v1 → v2 (2 medications, 1 condition, 2 appointments)
# [Step 3]  Generated 3 suggestions (2.1s)
# [Event]   summary.created emitted
# [Event]   profile.updated emitted
#
# === SUMMARY ===
# [formatted summary text]
#
# === SUGGESTIONS ===
# 1. Waarom wordt er overgestapt van tabletten naar infusen?
# 2. Wat kan ik verwachten bij de tintelingen?
# 3. Hoe verhouden deze scanresultaten zich tot januari?
#
# === PROFILE (v2) ===
# Conditions: Darmkanker stadium 3b (active)
# Medications: Oxaliplatin infuus elke 3 weken (active), Capecitabine 1500mg (discontinued)
# Action items: Bloedonderzoek (2026-04-15), Eerste infuus (2026-04-18)
#
# === CHANGES ===
# [HIGH] Medication discontinued: Capecitabine
# [HIGH] Medication added: Oxaliplatin

# Ask a question
$ node cli.js ask --summary sum_001 --question "Waarom stoppen we met capecitabine?"

# Output:
# [Pipeline] suggestion.tapped emitted
# [Step 1]  Loading context... done
# [Step 2]  Generating answer... (streaming)
#
# Dr. van der Berg legde uit dat de overstap van capecitabine naar oxaliplatin...
```

### Test Protocol

Run all three direction prototypes (A, B, C) against the same 10 sample conversations:

| Conversation | Type | Complexity |
|---|---|---|
| 1 | Oncology follow-up | High (medication change, scan results) |
| 2 | GP routine check | Low (blood pressure, cholesterol) |
| 3 | Cardiology first visit | Medium (new diagnosis, medication start) |
| 4 | Oncology with caregiver present | High (treatment decision, emotional) |
| 5 | Diabetes follow-up | Medium (HbA1c results, medication adjustment) |
| 6 | Neurology referral | Medium (new symptoms, referral) |
| 7 | Short phone consultation | Low (test results only) |
| 8 | Multi-specialist discussion | High (oncology + surgery, complex plan) |
| 9 | First appointment after diagnosis | High (new patient, lots of information) |
| 10 | Follow-up with good news | Medium (scan clear, reduced monitoring) |

**Evaluation criteria**:

| Criterion | Weight | How measured |
|---|---|---|
| Summary quality | 30% | Manual review: accuracy, completeness, patient-friendliness |
| Extraction accuracy | 20% | Compare extracted data against manually labeled ground truth |
| Suggestion relevance | 15% | Would a patient actually want to know this? (1-5 scale) |
| Answer quality | 15% | Grounded? Accurate? Helpful? (1-5 scale) |
| Total cost | 10% | Sum of all API calls per conversation |
| Total latency | 10% | Time from event to all outputs ready |

---

## 12. Migration Path from Current Architecture

Ditto currently runs Azure OpenAI for summarization. This migration adds the event-driven architecture incrementally, never requiring a big-bang switch.

### Phase 1: Add Extraction (Weeks 1-4)

**What changes**: After the existing summarization pipeline produces a summary, a new `extract_worker` runs on the same transcript. Extracted data goes into a new Health Profile Store. Nothing in the existing flow changes.

```
[EXISTING] Recording → Azure OpenAI → Summary
                            ↓
[NEW]              transcript → extract_worker → Profile Store
```

**Why safe**: Purely additive. If extraction fails, nothing breaks. Profile Store accumulates data silently. Engineers can validate extraction quality offline.

**Deliverables**:
- `extract_worker` deployed (Claude Haiku)
- Profile Store (PostgreSQL table)
- Background job that runs extraction on new summaries
- Dashboard showing extraction results vs. manual review

### Phase 2: Replace Summarization (Weeks 5-8)

**What changes**: New `summarize_worker` (Claude Sonnet) runs alongside existing Azure OpenAI summarization. A/B test: 50% of users get the new summarizer. Compare quality metrics.

```
[A/B] Recording → Feature flag → Azure OpenAI (50%) → Summary
                               → Claude Sonnet (50%) → Summary
```

**Why safe**: A/B testable. If Claude quality is worse, flip the flag back. Both paths produce the same output format. Mobile app doesn't know the difference.

**Deliverables**:
- `summarize_worker` deployed
- Feature flag for A/B routing
- Quality comparison dashboard
- Decision: switch fully to Claude or keep Azure

### Phase 3: Add Suggestion Pipeline (Weeks 9-14)

**What changes**: New feature. After summary generation, `suggest_worker` generates suggestions. Answer pipeline handles taps. This is the Smart Suggestions feature from the Phase 1 spec.

```
[EXISTING] Recording → Summarize → Summary
                                       ↓
[NEW]                          suggest_worker → Suggestions stored
[NEW]                     User taps → answer_worker → Answer (streamed)
```

**Why safe**: New feature, no changes to existing flows. Feature-flagged for gradual rollout. If suggestions are bad, disable the flag.

**Deliverables**:
- Event bus (simple, in-process initially)
- `suggest_worker` and `answer_worker` deployed
- Mobile UI for suggestion chips and inline answers
- Tracking events per [Smart Suggestions spec](care-brain-phase1-smart-suggestions.md)

### Phase 4: Add Sharing Pipeline (Weeks 15-20)

**What changes**: Connects to Care Circle V2. When a patient shares a summary, `adapt_worker` generates audience-adapted versions per circle member. `translate_worker` handles non-Dutch members.

```
[EXISTING] Patient shares summary → Circle member sees original summary
                                        ↓
[NEW]     Patient shares → adapt_worker (per member) → Circle member sees adapted version
```

**Why safe**: Can be feature-flagged per patient. Fall back to sharing the original summary (current behavior) if adaptation fails.

**Deliverables**:
- `adapt_worker` deployed
- `translate_worker` deployed
- Updated sharing flow in mobile app
- Circle member suggestion generation (lazy, on first view)

### Phase 5: Add Voice Input and Appointment Prep (Weeks 21-26)

**What changes**: Two new pipelines. Voice input ("Tell Ditto") processes spoken updates into profile data. Appointment prep generates pre-appointment briefings.

```
[NEW] Voice input → extract_worker → validate → confirm → profile update
[NEW] Calendar trigger → prep_worker → prep document → push notification
```

**Why safe**: Both are new features with no dependencies on existing flows. Voice input has a human-in-the-loop confirmation step.

**Deliverables**:
- Voice input pipeline with confirmation UI
- `prep_worker` deployed
- Calendar integration for appointment detection
- Push notification for prep delivery

### Migration Architecture Summary

```
Phase 1: ──[extract]──────────────────────────────────────→ Profile Store accumulates
Phase 2: ──[new summarizer]──────────────────────────────→ Quality validated
Phase 3: ──[suggestions + answers]───────────────────────→ Smart Suggestions live
Phase 4: ──[adapt + translate]───────────────────────────→ Smart Sharing live
Phase 5: ──[voice + prep]───────────────────────────────→ Full Nervous System
```

Each phase ships independently. Each phase is reversible. At no point does the existing product break.
