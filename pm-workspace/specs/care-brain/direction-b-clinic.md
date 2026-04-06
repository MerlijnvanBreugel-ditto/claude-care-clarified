# Direction B: The Clinic — Multi-Agent Specialist Network

**Author**: Merlijn van Breugel / Mewtwo
**Date**: 2026-04-04
**Status**: Architecture spec (prototype-ready)
**Parent**: [Care Brain Strategy](care-brain-strategy.md)
**Classification**: Explore (prototype direction for evaluation)

---

## 1. Architecture Overview

The Clinic treats the Care Brain as a coordinated team of specialist agents, each tuned for one domain, orchestrated by a routing layer that decides who does what and combines the results. The mobile app talks only to the orchestrator. It never knows how many agents exist behind it.

```
                        ┌───────────────┐
                        │   Mobile App  │
                        └───────┬───────┘
                                │ REST / WebSocket
                        ┌───────▼───────┐
                        │  Orchestrator │
                        │    Agent      │
                        └──┬──┬──┬──┬──┘
              ┌────────────┤  │  │  ├────────────┐
              │     ┌──────┘  │  └──────┐        │
              ▼     ▼         ▼         ▼        ▼
         ┌────────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
         │Summary │ │Extrac│ │ Q&A  │ │Share │ │ Prep │
         │ Agent  │ │tion  │ │Agent │ │Agent │ │Agent │
         └────┬───┘ │Agent │ └──┬───┘ └──┬───┘ └──┬───┘
              │     └──┬───┘    │        │        │
              │        │        │        │        │
              └────────┴────────┴────┬───┴────────┘
                                     │
                              ┌──────▼──────┐
                              │   Profile   │
                              │   Agent     │
                              └──────┬──────┘
                                     │
                              ┌──────▼──────┐
                              │   Health    │
                              │   Profile   │
                              │   Store     │
                              └─────────────┘
```

### Agents

| Agent | Responsibility | Model |
|---|---|---|
| **Orchestrator** | Routes requests, manages execution order, combines outputs, streams to app | Sonnet |
| **Summary Agent** | Conversation transcript to structured patient-friendly summary | Sonnet |
| **Extraction Agent** | Any input to structured health profile data (medications, conditions, care team, etc.) | Haiku |
| **Q&A Agent** | Question + context to grounded answer with citations | Opus (complex) / Sonnet (standard) |
| **Sharing Agent** | Content + audience profile to audience-adapted version | Sonnet |
| **Profile Agent** | Manages health profile: validates writes, resolves conflicts, detects changes | Sonnet |
| **Prep Agent** | Upcoming appointment + journey context to personalized preparation | Sonnet |

### Communication

Agents communicate through the orchestrator. No direct agent-to-agent calls. The orchestrator passes outputs from one agent as inputs to the next. This keeps the graph simple and debuggable.

Exception: Profile Agent has exclusive write access to the Health Profile Store. All other agents read from it, but writes go through Profile Agent for validation.

---

## 2. Orchestrator Design

### System prompt

```
You are the Care Brain Orchestrator for Ditto Care, a healthcare app that transforms
medical conversations into patient-friendly understanding.

Your job: receive requests from the app, determine which specialist agents to invoke,
in what order, and how to combine their outputs into a single coherent response.

RULES:
1. Never generate medical content yourself. Always delegate to specialist agents.
2. When multiple agents can run independently, run them in parallel.
3. When one agent's output is needed as input for another, run them sequentially.
4. Always include the Profile Agent when extracted data needs to be written to the
   health profile. Never let other agents write directly.
5. If a specialist agent fails, return a partial result with the available outputs
   and flag what failed. Never block the entire response for one failing agent.
6. For streaming responses, begin streaming as soon as the first relevant agent
   produces output. Don't wait for all agents to complete.
7. Every response to the app must conform to the CareBrainResponse schema.
8. Log every agent invocation with: agent_name, input_hash, latency_ms, token_count,
   success/failure.

ROUTING LOGIC:
Given a request type, invoke agents as follows:

- "process_conversation": Summary Agent + Extraction Agent (parallel) → Profile Agent
  (sequential, with extraction output) → Sharing Agent (sequential, with summary +
  profile) → return combined
- "ask_question": Q&A Agent (with appropriate context scope) → return streamed
- "voice_update": Extraction Agent → Profile Agent (validate + confirm) → return
  confirmation or conflict
- "prepare_appointment": Prep Agent (with journey context from Profile Store) → return
- "share_summary": Sharing Agent (with summary + audience profile) → return adapted
  versions
- "get_suggestions": Q&A Agent in suggestion-generation mode → return suggestion array

If the request type is ambiguous, classify it first based on the input content before
routing.
```

### Routing logic

The orchestrator receives a `CareBrainRequest` and uses the `request_type` field to determine the execution plan:

```typescript
type RequestType =
  | "process_conversation"   // Full pipeline: summarize + extract + profile + share
  | "ask_question"           // Single Q&A call
  | "voice_update"           // Extract from voice input, update profile
  | "prepare_appointment"    // Generate appointment prep
  | "share_summary"          // Adapt content for audience
  | "get_suggestions"        // Generate suggestion chips for a summary
```

### Parallel vs sequential execution

| Request type | Parallel | Sequential |
|---|---|---|
| `process_conversation` | Summary + Extraction | Profile (needs extraction output), then Sharing (needs summary + profile) |
| `ask_question` | None (single agent) | Q&A Agent only |
| `voice_update` | None | Extraction, then Profile |
| `prepare_appointment` | None | Prep Agent only (reads profile store directly) |
| `share_summary` | Per-audience-member Sharing calls | None |
| `get_suggestions` | None | Q&A Agent in suggestion mode |

### Combining outputs

The orchestrator merges agent outputs into a single `CareBrainResponse`:

```typescript
interface CareBrainResponse {
  request_id: string;
  request_type: RequestType;
  status: "complete" | "partial" | "error";
  summary?: SummaryOutput;
  profile_updates?: ProfileUpdate[];
  suggestions?: SuggestionChip[];
  answer?: QAAnswer;
  shared_versions?: AudienceAdaptedContent[];
  prep?: AppointmentPrep;
  errors?: AgentError[];
  metadata: {
    total_latency_ms: number;
    agents_invoked: AgentInvocation[];
    total_tokens: { input: number; output: number };
    total_cost_usd: number;
  };
}

interface AgentInvocation {
  agent: string;
  model: string;
  latency_ms: number;
  tokens: { input: number; output: number };
  status: "success" | "failure" | "timeout";
  error_message?: string;
}
```

### Error handling

| Failure | Behavior |
|---|---|
| Summary Agent fails | Return error. Summary is critical. Retry once. |
| Extraction Agent fails | Return summary without profile updates. Log for retry. |
| Q&A Agent fails | Return error for `ask_question`. For suggestions, return empty array. |
| Profile Agent fails | Return summary + extraction results, but skip profile write. Queue for retry. |
| Sharing Agent fails | Return summary without adapted versions. Patient version is the fallback. |
| Orchestrator timeout (30s) | Return whatever agents have completed. Flag incomplete agents. |

---

## 3. Specialist Agent Specifications

### 3.1 Summary Agent

**Model**: Sonnet

**System prompt**:
```
You are the Summary Agent for Ditto Care. You transform medical conversation
transcripts into patient-friendly summaries.

RULES:
1. Write in the patient's language (Dutch or English, matching the transcript).
2. Use plain language. Replace medical jargon with everyday explanations, but keep
   the medical term in parentheses: "bloedverdunners (anticoagulantia)".
3. Structure every summary into these sections:
   - Main topics discussed (what the appointment was about)
   - Key decisions (what was decided)
   - Medications (any changes, new prescriptions, or confirmations)
   - Action items (what the patient needs to do)
   - Next appointment (when, what for)
4. If a section has no content, omit it. Never pad with filler.
5. Quote the doctor when it adds clarity: 'Dr. van der Berg: "We'll keep a close
   eye on it for now."'
6. Never add medical information not present in the transcript.
7. If the conversation references previous appointments, note the connection but
   don't fabricate history.
8. Keep summaries between 200-600 words. Shorter conversations get shorter summaries.
9. Tone: warm, clear, reassuring. Like a knowledgeable friend explaining, not a
   medical textbook.
```

**Input schema**:
```typescript
interface SummaryInput {
  conversation_id: string;
  transcript: string;                    // Full conversation transcript
  language: "nl" | "en";                 // Detected language
  previous_summaries?: PreviousSummary[];// For cross-appointment context
  health_profile?: HealthProfile;        // Current patient profile for context
}

interface PreviousSummary {
  summary_id: string;
  date: string;                          // ISO date
  title: string;                         // One-line summary title
  content: string;                       // Full summary text
  doctor_name?: string;
  specialty?: string;
}
```

**Output schema**:
```typescript
interface SummaryOutput {
  summary_id: string;
  title: string;                         // "Oncology appointment with Dr. van der Berg"
  content: string;                       // Full summary text (markdown)
  sections: SummarySection[];            // Structured breakdown
  doctor_name?: string;
  specialty?: string;
  appointment_date?: string;
  word_count: number;
  language: "nl" | "en";
  cross_references?: CrossReference[];   // Links to previous summaries
}

interface SummarySection {
  type: "main_topics" | "decisions" | "medications" | "action_items" | "next_appointment";
  content: string;
}

interface CrossReference {
  previous_summary_id: string;
  reference_text: string;                // "In January, Dr. X mentioned..."
}
```

**Tools**: Read from Health Profile Store (read-only).

**Quality guardrails**:
- Hallucination check: every claim must trace to a transcript segment
- Length check: reject summaries under 100 or over 800 words
- Section check: must include at least "main_topics" and one other section
- Language check: output language must match input language


### 3.2 Extraction Agent

**Model**: Haiku (fast, cheap, structured output is its strength)

**System prompt**:
```
You are the Extraction Agent for Ditto Care. You extract structured health data
from any input: conversation transcripts, voice updates, document photos.

RULES:
1. Extract ONLY what is explicitly stated. Never infer or assume.
2. For each extracted item, include a confidence score (0.0-1.0):
   - 1.0: directly and unambiguously stated ("We're switching you to metformin 500mg")
   - 0.7-0.9: clearly implied but not word-for-word ("They mentioned a new blood
     pressure medication" without naming it)
   - 0.5-0.6: ambiguous, needs user confirmation
   - Below 0.5: don't extract, too uncertain
3. Extract into these categories: medications, conditions, allergies, care_team,
   vitals, lab_results, action_items, appointments.
4. For medication changes, always capture: name, dosage, frequency, change_type
   (new/changed/stopped/continued).
5. For conditions, capture: name, status (active/resolved/monitoring), severity if
   mentioned.
6. Always note the source: which part of the input the extraction came from.
7. Handle Dutch medical terminology and common abbreviations (bijv., mg, 2dd1, etc.).
8. When multiple items of the same type are mentioned, extract all of them.
```

**Input schema**:
```typescript
interface ExtractionInput {
  source_id: string;                     // conversation_id or voice_update_id
  source_type: "transcript" | "voice_update" | "document_photo" | "text_note";
  content: string;                       // The text to extract from
  language: "nl" | "en";
  existing_profile?: HealthProfile;      // For detecting changes vs. confirmations
}
```

**Output schema**:
```typescript
interface ExtractionOutput {
  source_id: string;
  extractions: Extraction[];
  extraction_count: number;
}

interface Extraction {
  id: string;                            // Unique extraction ID
  category: "medication" | "condition" | "allergy" | "care_team" | "vital"
            | "lab_result" | "action_item" | "appointment";
  data: MedicationData | ConditionData | AllergyData | CareTeamData
        | VitalData | LabResultData | ActionItemData | AppointmentData;
  confidence: number;                    // 0.0-1.0
  source_quote: string;                  // Exact text that supports this extraction
  change_type: "new" | "changed" | "confirmed" | "stopped" | "unknown";
}

interface MedicationData {
  name: string;
  dosage?: string;
  frequency?: string;
  route?: string;                        // oral, injection, etc.
  reason?: string;
  previous_medication?: string;          // If this replaces something
}

interface ConditionData {
  name: string;
  status: "active" | "resolved" | "monitoring";
  severity?: "mild" | "moderate" | "severe";
  diagnosed_date?: string;
}

interface AllergyData {
  allergen: string;
  reaction?: string;
  severity?: "mild" | "moderate" | "severe";
}

interface CareTeamData {
  name: string;
  role: string;                          // "oncologist", "huisarts", etc.
  institution?: string;
}

interface VitalData {
  type: string;                          // "blood_pressure", "weight", "temperature"
  value: string;
  unit: string;
  date?: string;
}

interface LabResultData {
  test_name: string;
  value?: string;
  unit?: string;
  reference_range?: string;
  date?: string;
}

interface ActionItemData {
  description: string;
  due_date?: string;
  assigned_to: "patient" | "doctor" | "other";
}

interface AppointmentData {
  date?: string;
  time?: string;
  doctor_name?: string;
  specialty?: string;
  purpose?: string;
  location?: string;
}
```

**Tools**: None. Pure extraction, no side effects.

**Quality guardrails**:
- Confidence threshold: discard anything below 0.5
- Source quote required: every extraction must cite the input text
- Duplicate detection: don't extract the same medication twice from repeated mentions


### 3.3 Q&A Agent

**Model**: Opus for complex multi-summary reasoning. Sonnet for single-summary questions.

The orchestrator decides which model to use based on: does the question reference previous appointments or require cross-summary reasoning? If yes, Opus. If it's about the current summary only, Sonnet.

**System prompt**:
```
You are the Q&A Agent for Ditto Care. You answer patient questions about their
medical conversations and health journey. You also generate contextual suggestion
questions.

MODES:
1. ANSWER mode: Given a question and context, produce a grounded answer.
2. SUGGEST mode: Given a summary, generate 2-3 questions a patient would likely
   want answered.

RULES FOR ANSWER MODE:
1. Answer ONLY from the provided context (conversation transcripts, summaries,
   health profile). Never use general medical knowledge.
2. If the answer isn't in the context, say so clearly: "This wasn't discussed in
   your appointment with Dr. [name]. You could ask about it at your next visit."
3. Quote the doctor when it supports the answer: 'Dr. van der Berg mentioned:
   "[exact quote]"'
4. Cite the source: "Based on your appointment on [date]" or "From your health
   profile."
5. Never provide medical advice, diagnoses, or treatment recommendations.
6. End every answer with: "This is based on your conversation with [doctor name].
   For medical advice, please contact your care team."
7. Keep answers 100-300 words. Clear, warm, reassuring.
8. If the patient asks something that requires medical judgment ("Should I worry
   about this?"), redirect: "That's an important question for Dr. [name]. Based on
   your conversation, here's what was discussed: [relevant info]."
9. In Dutch when the summary is Dutch. In English when the summary is English.

RULES FOR SUGGEST MODE:
1. Generate exactly 2-3 questions. No more, no fewer.
2. Questions must be specific to THIS conversation. Not generic ("What is cancer?")
   but contextual ("What does the change from capecitabine to oxaliplatin mean for
   side effects?").
3. At least one question should address the most significant medical decision or
   information in the summary.
4. If previous summaries are available, include one question that bridges
   appointments: "How does today's result compare to your January scan?"
5. Frame questions from the patient's perspective, using "my" and "I": "What does
   this mean for my daily routine?" not "What are the implications?"
6. For circle member context: frame from their perspective: "What does this mean for
   daily care?" "What can I do to help?"
```

**Input schema**:
```typescript
interface QAInput {
  mode: "answer" | "suggest";
  // For ANSWER mode
  question?: string;
  // For SUGGEST mode (no question needed)
  summary: SummaryOutput;
  transcript?: string;                   // Full transcript for grounding
  previous_summaries?: PreviousSummary[];
  health_profile?: HealthProfile;
  viewer_context: {
    is_patient: boolean;
    is_circle_member: boolean;
    circle_member_role?: string;         // "partner", "child", "friend"
    shared_data_scope?: string[];        // What data this viewer can see
  };
}
```

**Output schema**:
```typescript
// ANSWER mode
interface QAAnswer {
  answer: string;                        // The answer text (markdown)
  citations: Citation[];
  disclaimer: string;                    // Always present
  answerable: boolean;                   // False if question can't be answered from context
  word_count: number;
}

interface Citation {
  source_type: "transcript" | "summary" | "profile";
  source_id: string;
  source_date?: string;
  quote?: string;                        // Relevant quote from source
}

// SUGGEST mode
interface SuggestionChip {
  question: string;
  category: "decision" | "medication" | "next_steps" | "cross_appointment" | "general";
  priority: number;                      // 1 = most relevant
  target_audience: "patient" | "circle_member";
}
```

**Tools**: Read from Health Profile Store (read-only).

**Quality guardrails**:
- Grounding check: every answer must include at least one citation
- Disclaimer check: every answer must end with the medical disclaimer
- Scope check: circle member answers must only reference data within their shared scope
- Hallucination check: reject answers that introduce information not in the provided context


### 3.4 Sharing Agent

**Model**: Sonnet

**System prompt**:
```
You are the Sharing Agent for Ditto Care. You adapt medical summaries for different
audiences in a patient's Care Circle.

Your job: take a patient summary and create a version tailored to a specific circle
member's relationship, needs, and comprehension level.

RULES:
1. Never add medical information not in the original summary.
2. Adapt tone, detail level, and framing based on the audience:
   - Partner/spouse: full detail, action items, emotional support framing
   - Adult child: key decisions, what to monitor, "how can I help" framing
   - Friend: high-level status, emotional tone, "things are okay" or "could use
     support" framing
   - Healthcare proxy: clinical detail preserved, action items, legal relevance
3. Respect sharing permissions. If the patient excluded certain sections, they must
   not appear in any form in the adapted version.
4. Always include: what the appointment was about, key outcome, what happens next.
5. Keep adapted versions shorter than the patient summary. Partners get ~70% length.
   Friends get ~40% length.
6. Match the language of the original summary.
7. Tone: warm, human, never clinical. This is one person telling another person
   about a medical appointment.
8. If the summary contains emotionally sensitive content (bad prognosis, treatment
   failure), handle with care. Don't minimize, but frame with the doctor's plan
   and next steps.
```

**Input schema**:
```typescript
interface SharingInput {
  summary: SummaryOutput;
  health_profile: HealthProfile;         // For journey context
  audience: AudienceProfile;
  sharing_permissions: SharingPermissions;
}

interface AudienceProfile {
  circle_member_id: string;
  relationship: "partner" | "child" | "parent" | "friend" | "healthcare_proxy" | "other";
  name: string;
  language_preference?: "nl" | "en";     // May differ from patient
  previous_shares_count: number;         // How many summaries they've received before
}

interface SharingPermissions {
  included_sections: string[];           // Which summary sections to share
  excluded_topics?: string[];            // Specific topics patient excluded
  detail_level: "full" | "standard" | "minimal";
}
```

**Output schema**:
```typescript
interface AudienceAdaptedContent {
  circle_member_id: string;
  adapted_summary: string;               // The adapted text (markdown)
  relationship: string;
  word_count: number;
  language: "nl" | "en";
  action_items_for_member?: string[];    // "You could help by..."
  tone: "informative" | "supportive" | "brief";
}
```

**Tools**: Read from Health Profile Store (read-only, for journey context).

**Quality guardrails**:
- Permission check: output must not contain any excluded topics or sections
- Length check: adapted version must be shorter than original summary
- Tone check: never clinical language in friend-level shares
- Completeness check: must include appointment topic, key outcome, and next steps


### 3.5 Profile Agent

**Model**: Sonnet

**System prompt**:
```
You are the Profile Agent for Ditto Care. You are the gatekeeper of the patient's
health profile. Only you can write to the Health Profile Store.

Your job: receive extracted data from the Extraction Agent (or other sources),
validate it, resolve conflicts with existing profile data, and commit changes.

RULES:
1. Before writing any data, compare it with the existing profile.
2. Conflict resolution priority:
   a. Most recent source wins (newer appointment > older appointment)
   b. Higher confidence wins when sources are from the same date
   c. If truly ambiguous, flag for user confirmation. Never silently overwrite.
3. For medication changes:
   a. "Stopped" requires explicit statement ("We're discontinuing X")
   b. A new medication doesn't automatically stop the old one unless stated
   c. Dosage changes update the existing entry, don't create duplicates
4. For condition status changes:
   a. Only change to "resolved" if explicitly stated
   b. "Monitoring" is the safe default for ambiguous status
5. Track provenance for every field: which agent wrote it, from which source,
   at what confidence level, on what date.
6. When conflicts are detected, return a ConflictReport instead of auto-resolving.
   The orchestrator will route this to the user for confirmation.
7. Maintain version history. Every write creates a new version. Old versions are
   kept for 12 months.
8. Validate data consistency: if a medication is listed as "stopped" but appears
   in a newer summary as active, flag the inconsistency.
```

**Input schema**:
```typescript
interface ProfileUpdateInput {
  patient_id: string;
  extractions: Extraction[];             // From Extraction Agent
  source_id: string;                     // conversation_id, voice_update_id, etc.
  source_date: string;                   // ISO date
  source_type: "transcript" | "voice_update" | "document_photo" | "manual_edit";
}
```

**Output schema**:
```typescript
interface ProfileUpdateResult {
  updates_applied: ProfileFieldUpdate[];
  conflicts_detected: ConflictReport[];
  confirmations_needed: UserConfirmation[];
  profile_version: number;
}

interface ProfileFieldUpdate {
  field_path: string;                    // e.g., "medications[3].dosage"
  old_value: any;
  new_value: any;
  change_type: "added" | "updated" | "removed";
  confidence: number;
  source_id: string;
  source_agent: string;
}

interface ConflictReport {
  field_path: string;
  existing_value: any;
  new_value: any;
  existing_source: string;
  new_source: string;
  existing_confidence: number;
  new_confidence: number;
  suggested_resolution: "keep_existing" | "accept_new" | "ask_user";
  reason: string;
}

interface UserConfirmation {
  confirmation_id: string;
  question: string;                      // "Did your doctor switch you from X to Y?"
  extracted_data: Extraction;
  options: ConfirmationOption[];
}

interface ConfirmationOption {
  label: string;                         // "Yes, that's correct"
  action: "accept" | "reject" | "modify";
}
```

**Tools**: Read + Write to Health Profile Store.

**Quality guardrails**:
- No silent overwrites: conflicting data always generates a ConflictReport
- Provenance required: every field must have source attribution
- Version integrity: profile version increments on every write
- Consistency checks: cross-field validation (stopped medication can't have future dosage change)


### 3.6 Prep Agent

**Model**: Sonnet

**System prompt**:
```
You are the Prep Agent for Ditto Care. You help patients prepare for upcoming
medical appointments by generating personalized preparation based on their health
journey.

RULES:
1. Pull context from: health profile, previous summaries, unresolved action items,
   medication list, condition timeline.
2. Structure prep into:
   - What happened since your last visit with this doctor
   - Unresolved items from previous appointments
   - Changes to report (new medications, symptoms, other doctor visits)
   - Suggested questions to ask (based on gaps in previous conversations)
   - Practical reminders (bring medication list, insurance card, etc.)
3. Suggested questions must be specific and grounded: "Ask about the blood work
   results from March" not "Ask if you have any concerns."
4. Keep prep concise. Maximum 400 words. Patients read this in the waiting room.
5. If there's no prior history with this doctor/specialty, provide a general
   first-visit prep focused on what information to bring.
6. Match the language of the patient's profile.
7. Tone: practical, encouraging, empowering. "You're prepared."
```

**Input schema**:
```typescript
interface PrepInput {
  patient_id: string;
  upcoming_appointment: AppointmentData;
  health_profile: HealthProfile;
  previous_summaries_with_doctor?: PreviousSummary[];  // Same doctor/specialty
  recent_summaries?: PreviousSummary[];                // Last 3 months, any doctor
  unresolved_action_items?: ActionItemData[];
}
```

**Output schema**:
```typescript
interface AppointmentPrep {
  appointment_id: string;
  title: string;                         // "Preparing for your oncology appointment"
  sections: PrepSection[];
  word_count: number;
  language: "nl" | "en";
}

interface PrepSection {
  type: "since_last_visit" | "unresolved" | "changes_to_report"
        | "suggested_questions" | "practical_reminders";
  content: string;                       // Markdown
  items?: string[];                      // Bullet points for lists
}
```

**Tools**: Read from Health Profile Store (read-only).

**Quality guardrails**:
- Grounding check: every suggested question must trace to a real gap or unresolved item
- Length check: max 400 words
- Completeness: must include at least "changes_to_report" and "suggested_questions"
- No fabricated history: if no prior visits with this doctor, say so and adapt

---

## 4. Health Profile Store

### Schema

```typescript
interface HealthProfile {
  patient_id: string;
  version: number;
  last_updated: string;                  // ISO datetime
  created: string;

  // Core data
  demographics: {
    name?: string;
    date_of_birth?: string;
    language: "nl" | "en";
  };

  medications: MedicationRecord[];
  conditions: ConditionRecord[];
  allergies: AllergyRecord[];
  care_team: CareTeamRecord[];
  vitals: VitalRecord[];
  lab_results: LabResultRecord[];
  action_items: ActionItemRecord[];
  appointments: AppointmentRecord[];

  // Journey
  timeline: TimelineEvent[];

  // Metadata
  profile_metadata: {
    total_conversations_processed: number;
    total_extractions: number;
    last_conflict_date?: string;
    pending_confirmations: number;
  };
}
```

### Record with provenance

Every record in the profile carries provenance metadata:

```typescript
interface ProvenanceMetadata {
  created_by_agent: string;              // "extraction_agent", "profile_agent", "manual"
  created_from_source: string;           // conversation_id, voice_update_id, etc.
  created_at: string;                    // ISO datetime
  confidence: number;                    // 0.0-1.0
  last_modified_by_agent?: string;
  last_modified_at?: string;
  last_modified_reason?: string;         // "dosage_update", "conflict_resolution"
  version_history: VersionEntry[];
}

interface VersionEntry {
  version: number;
  timestamp: string;
  agent: string;
  change_type: "added" | "updated" | "removed";
  previous_value?: any;
  new_value: any;
  source_id: string;
  confidence: number;
}

// Example: a medication record with full provenance
interface MedicationRecord extends ProvenanceMetadata {
  id: string;
  name: string;
  dosage?: string;
  frequency?: string;
  route?: string;
  reason?: string;
  status: "active" | "stopped" | "changed";
  started_date?: string;
  stopped_date?: string;
  replaced_by?: string;                  // ID of replacement medication
}
```

### Conflict detection

The Profile Agent runs these checks before every write:

| Check | Trigger | Action |
|---|---|---|
| **Duplicate medication** | Same medication name, different dosage | Create `ConflictReport` with both values |
| **Stopped but active** | Medication marked stopped in profile but mentioned as active in new source | Flag for user confirmation |
| **Condition status change** | Condition changes from "active" to "resolved" | Accept only if confidence >= 0.8 and source is explicit |
| **Care team conflict** | Same specialty, different doctor name | Add new, don't remove old (patient might see multiple) |
| **Temporal inconsistency** | New data is older than existing data for same field | Keep newer data, log the older source |
| **Low confidence overwrite** | New extraction (confidence 0.6) tries to overwrite high-confidence existing (0.9) | Keep existing, flag for review |

### Conflict resolution protocol

```
1. Profile Agent receives Extraction Agent output
2. For each extraction, compare with existing profile:
   a. No existing data → write with provenance
   b. Existing data matches → update "confirmed" timestamp
   c. Existing data conflicts:
      i.  If new source is more recent AND confidence >= 0.8 → accept new, archive old
      ii. If confidences are close (within 0.2) → create ConflictReport, ask user
      iii. If new confidence < existing confidence → keep existing, log new as alternative
3. Return ProfileUpdateResult with all changes, conflicts, and confirmation requests
4. Orchestrator presents confirmations to user via app
5. User response feeds back to Profile Agent for final resolution
```

### Profile Store API

```typescript
interface ProfileStoreAPI {
  // Read operations (available to all agents)
  getProfile(patient_id: string): Promise<HealthProfile>;
  getField(patient_id: string, field_path: string): Promise<any>;
  getHistory(patient_id: string, field_path: string, limit?: number): Promise<VersionEntry[]>;
  search(patient_id: string, query: string): Promise<SearchResult[]>;

  // Write operations (Profile Agent only)
  applyUpdate(patient_id: string, update: ProfileFieldUpdate): Promise<void>;
  resolveConflict(patient_id: string, conflict_id: string, resolution: "keep_existing" | "accept_new"): Promise<void>;
  applyUserConfirmation(patient_id: string, confirmation_id: string, option: ConfirmationOption): Promise<void>;

  // Version operations
  getVersion(patient_id: string, version: number): Promise<HealthProfile>;
  diff(patient_id: string, version_a: number, version_b: number): Promise<ProfileFieldUpdate[]>;
}
```

### Storage (prototype)

For the prototype, the Health Profile Store is a JSON file per patient:

```
health-profiles/
  patient_001.json       # Current profile
  patient_001.history/   # Version history
    v1.json
    v2.json
    ...
```

Production: PostgreSQL with JSONB columns for flexible schema + proper versioning table.

---

## 5. Communication Patterns

### Agent invocation

The orchestrator calls each specialist agent as a function. Using the Anthropic SDK pattern:

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function invokeAgent(
  agentConfig: AgentConfig,
  input: any
): Promise<AgentResult> {
  const startTime = Date.now();

  const response = await client.messages.create({
    model: agentConfig.model,
    max_tokens: agentConfig.maxTokens,
    system: agentConfig.systemPrompt,
    messages: [
      {
        role: "user",
        content: JSON.stringify(input),
      },
    ],
    // Tool definitions if the agent has tools
    ...(agentConfig.tools && { tools: agentConfig.tools }),
  });

  return {
    agent: agentConfig.name,
    output: parseAgentOutput(response),
    latency_ms: Date.now() - startTime,
    tokens: {
      input: response.usage.input_tokens,
      output: response.usage.output_tokens,
    },
    status: "success",
  };
}
```

### Parallel execution

```typescript
async function processConversation(request: CareBrainRequest): Promise<CareBrainResponse> {
  const profile = await profileStore.getProfile(request.patient_id);

  // Phase 1: Parallel — Summary + Extraction
  const [summaryResult, extractionResult] = await Promise.all([
    invokeAgent(SUMMARY_AGENT, {
      conversation_id: request.conversation_id,
      transcript: request.transcript,
      language: request.language,
      previous_summaries: request.previous_summaries,
      health_profile: profile,
    }),
    invokeAgent(EXTRACTION_AGENT, {
      source_id: request.conversation_id,
      source_type: "transcript",
      content: request.transcript,
      language: request.language,
      existing_profile: profile,
    }),
  ]);

  // Phase 2: Sequential — Profile update (needs extraction output)
  const profileResult = await invokeAgent(PROFILE_AGENT, {
    patient_id: request.patient_id,
    extractions: extractionResult.output.extractions,
    source_id: request.conversation_id,
    source_date: request.appointment_date,
    source_type: "transcript",
  });

  // Phase 3: Sequential — Sharing (needs summary + updated profile)
  const updatedProfile = await profileStore.getProfile(request.patient_id);
  const sharingResults = await Promise.all(
    request.circle_members.map((member) =>
      invokeAgent(SHARING_AGENT, {
        summary: summaryResult.output,
        health_profile: updatedProfile,
        audience: member,
        sharing_permissions: member.permissions,
      })
    )
  );

  // Phase 4: Parallel with sharing — Generate suggestions
  const suggestionsResult = await invokeAgent(QA_AGENT, {
    mode: "suggest",
    summary: summaryResult.output,
    transcript: request.transcript,
    previous_summaries: request.previous_summaries,
    viewer_context: { is_patient: true, is_circle_member: false },
  });

  return buildResponse(summaryResult, extractionResult, profileResult, sharingResults, suggestionsResult);
}
```

### Context sharing

Agents do NOT share a memory space. The orchestrator explicitly passes data between agents:

| From | To | Data passed |
|---|---|---|
| App | Orchestrator | Raw request (transcript, patient_id, etc.) |
| Orchestrator | Summary Agent | Transcript + previous summaries + profile snapshot |
| Orchestrator | Extraction Agent | Transcript + existing profile (for change detection) |
| Extraction Agent (via Orchestrator) | Profile Agent | Extracted data array |
| Summary Agent (via Orchestrator) | Sharing Agent | Summary output |
| Profile Store | Any Agent (read) | Profile snapshot at time of request |
| Orchestrator | Q&A Agent | Summary + transcript + profile + viewer context |

This explicit passing is intentional. It makes the data flow debuggable and auditable. Every agent invocation log includes the exact input it received.

### Streaming

For `ask_question` requests, the orchestrator streams the Q&A Agent's response directly to the app:

```typescript
async function streamAnswer(request: CareBrainRequest): Promise<ReadableStream> {
  const profile = await profileStore.getProfile(request.patient_id);

  const stream = client.messages.stream({
    model: selectQAModel(request),        // Opus or Sonnet based on complexity
    max_tokens: 1024,
    system: QA_AGENT.systemPrompt,
    messages: [
      {
        role: "user",
        content: JSON.stringify({
          mode: "answer",
          question: request.question,
          summary: request.summary,
          transcript: request.transcript,
          previous_summaries: request.previous_summaries,
          health_profile: profile,
          viewer_context: request.viewer_context,
        }),
      },
    ],
  });

  return stream;
}
```

---

## 6. Request Flow Scenarios

### Scenario 1: Patient records oncologist appointment

```
Timeline: 0s ────────────────────────────────────────── ~45s

[0s]   App sends "process_conversation" request to Orchestrator
       Input: transcript (12,000 tokens), patient_id, 3 previous summaries

[0.1s] Orchestrator reads health profile from store
       Orchestrator dispatches IN PARALLEL:
       ├── Summary Agent (Sonnet): transcript + profile + previous summaries
       └── Extraction Agent (Haiku): transcript + existing profile

[3s]   Extraction Agent completes (Haiku is fast)
       Output: 8 extractions (2 medications, 1 condition update, 1 care team,
               2 action items, 1 appointment, 1 lab result)

[8s]   Summary Agent completes
       Output: 450-word summary with 4 sections, 2 cross-references to previous visits

[8.1s] Orchestrator dispatches SEQUENTIALLY:
       Profile Agent receives 8 extractions
       Profile Agent compares with existing profile:
       - Medication change detected: capecitabine → oxaliplatin (confidence 0.95)
       - Existing capecitabine entry conflict: was "active", needs "stopped"
       - New action item: blood work in 2 weeks
       Profile Agent writes updates, generates 1 confirmation request
       (medication change, high confidence but significant)

[12s]  Profile Agent completes
       Output: 6 updates applied, 1 confirmation needed, 0 unresolved conflicts

[12.1s] Orchestrator dispatches IN PARALLEL:
        ├── Sharing Agent (partner): summary + updated profile + full permissions
        ├── Sharing Agent (daughter): summary + updated profile + standard permissions
        └── Q&A Agent (suggest mode): summary + transcript + previous summaries

[16s]  All three complete
       Sharing Agent (partner): 320-word adapted version with action items
       Sharing Agent (daughter): 180-word adapted version, supportive tone
       Q&A Agent: 3 suggestion chips:
         1. "What does switching from capecitabine to oxaliplatin mean for side effects?"
         2. "How does today's scan compare to your January results?"
         3. "What should you do if you experience nausea with the new medication?"

[16.1s] Orchestrator assembles CareBrainResponse, returns to app

       Total: ~16 seconds, 6 agent invocations, ~25K input tokens, ~3K output tokens
```

### Scenario 2: Circle member taps suggestion on shared summary

```
Timeline: 0s ──────────────────────── ~3s

[0s]   App sends "ask_question" request to Orchestrator
       Input: question (from suggestion chip), summary_id, circle_member_id
       Circle member: daughter, "standard" permissions, 5 previous shares

[0.1s] Orchestrator loads:
       - Summary and transcript for this conversation
       - Circle member's sharing permissions (excluded: mental health discussion)
       - Circle member's audience profile
       Orchestrator selects model: Sonnet (single-summary question, no cross-appointment)

[0.2s] Orchestrator dispatches Q&A Agent with scoped context:
       - Summary included
       - Transcript included BUT mental health section redacted per permissions
       - Viewer context: is_circle_member=true, role="child"

[0.5s] Q&A Agent begins streaming response
       Orchestrator pipes stream directly to app via WebSocket

[2.5s] Q&A Agent completes
       Output: 180-word answer, 1 citation, disclaimer
       Answer framed for daughter: "For your mom's daily routine, the medication
       change means..." (not clinical framing)

       Total: ~2.5 seconds, 1 agent invocation, ~8K input tokens, ~250 output tokens
```

### Scenario 3: Voice input "They changed my medication to X"

```
Timeline: 0s ──────────────────────────── ~8s

[0s]   App sends "voice_update" request to Orchestrator
       Input: transcribed text "Ze hebben mijn medicatie veranderd naar metformine
              500mg, twee keer per dag" + patient_id

[0.1s] Orchestrator reads current health profile
       Orchestrator dispatches Extraction Agent

[1.5s] Extraction Agent completes
       Output: 1 extraction:
       {
         category: "medication",
         data: { name: "metformine", dosage: "500mg", frequency: "2x per dag" },
         confidence: 0.92,
         source_quote: "Ze hebben mijn medicatie veranderd naar metformine 500mg,
                        twee keer per dag",
         change_type: "changed"
       }

[1.6s] Orchestrator dispatches Profile Agent with extraction

[3.5s] Profile Agent compares with existing profile:
       - Finds existing medication "gliclazide 80mg" (for diabetes)
       - Extraction says "changed to" but doesn't name what was replaced
       - Confidence high (0.92) for the new medication
       - Ambiguity: which medication was replaced?
       - Decision: add metformine as new, flag gliclazide as "possibly replaced"
       - Generate user confirmation: "Is metformine replacing your gliclazide?"

[3.6s] Orchestrator returns to app:
       - Profile update: metformine 500mg 2x/dag added (pending confirmation)
       - Confirmation needed: "Is metformine replacing your gliclazide 80mg?"
       - Options: "Yes, replacing gliclazide" / "No, it's an additional medication" /
                  "I'm not sure"

[User responds "Yes, replacing gliclazide"]

[4s]   App sends confirmation response to Orchestrator

[4.1s] Orchestrator dispatches Profile Agent with confirmation

[5s]   Profile Agent:
       - Marks gliclazide as "stopped" with source "voice_update, patient confirmed"
       - Marks metformine as "active", replaced gliclazide
       - Updates version history

[5.1s] Orchestrator checks: are there circle members who should be notified?
       - Partner has "medication_changes" notification preference
       - Orchestrator dispatches Sharing Agent:
         Input: medication change summary + partner profile

[7s]   Sharing Agent completes
       Output: "Merlijn's medicatie is veranderd: metformine 500mg vervangt
               gliclazide. Dit is bevestigd door Merlijn."

[7.1s] Orchestrator returns final status + queues circle notification

       Total: ~7 seconds active processing, 3 agent invocations + 1 confirmation round
```

---

## 7. Interface Integration

### API contract

The mobile app sees one endpoint. It does not know about internal agents:

```typescript
// POST /api/v1/care-brain
interface CareBrainRequest {
  request_id: string;
  request_type: RequestType;
  patient_id: string;

  // For process_conversation
  conversation_id?: string;
  transcript?: string;
  language?: "nl" | "en";
  appointment_date?: string;

  // For ask_question
  question?: string;
  summary_id?: string;

  // For voice_update
  voice_text?: string;

  // For prepare_appointment
  appointment_id?: string;

  // For share_summary
  circle_members?: AudienceProfile[];

  // For get_suggestions
  // (uses summary_id)

  // Context
  viewer_context?: {
    is_patient: boolean;
    is_circle_member: boolean;
    circle_member_id?: string;
    circle_member_role?: string;
  };
}

// Response: CareBrainResponse (defined in section 2)
```

### Streaming

For `ask_question` requests, the response is streamed via WebSocket or Server-Sent Events:

```
Client: POST /api/v1/care-brain { request_type: "ask_question", ... }
Server: 200 OK, Content-Type: text/event-stream

data: {"type": "start", "request_id": "abc123"}
data: {"type": "token", "text": "Dr. "}
data: {"type": "token", "text": "van der "}
data: {"type": "token", "text": "Berg "}
data: {"type": "token", "text": "mentioned..."}
...
data: {"type": "done", "metadata": { "tokens": { "input": 8000, "output": 250 }, "latency_ms": 2500 }}
```

### Async processing

For `process_conversation` (takes 15-45 seconds), the app uses async polling or push:

```
Client: POST /api/v1/care-brain { request_type: "process_conversation", ... }
Server: 202 Accepted, { "job_id": "xyz789", "status": "processing" }

# Option A: Polling
Client: GET /api/v1/care-brain/jobs/xyz789
Server: 200 OK, { "status": "processing", "progress": { "summary": "complete", "extraction": "complete", "profile": "in_progress", "sharing": "pending" } }

# Option B: Push notification when done
Server → Push: { "job_id": "xyz789", "status": "complete", "summary_id": "sum_001" }
```

### Smart Suggestions integration

Same interface as described in the [Phase 1 spec](care-brain-phase1-smart-suggestions.md). The only difference is internal: suggestions are generated by the dedicated Q&A Agent in suggest mode rather than a general-purpose prompt.

---

## 8. Smart Suggestions Interface Spec

User-facing behavior is identical to Phase 1:
- 2-3 suggestion chips below the summary
- Inline expansion on tap
- Grounded answers with citations
- Medical disclaimer on every answer
- "Ask something else" for custom questions

### Architectural difference from Direction A

| Aspect | Direction A (Monolith) | Direction B (Clinic) |
|---|---|---|
| Suggestion generation | Single LLM call with multi-task prompt | Dedicated Q&A Agent in suggest mode |
| Answer generation | Single LLM call with answer prompt | Q&A Agent in answer mode, model selected per complexity |
| Context | Everything in one context window | Orchestrator scopes context per agent |
| Circle member suggestions | Same prompt, different context | Same Q&A Agent, different viewer_context |

### Quality advantage

The Q&A Agent has one job: questions and answers. Its system prompt is tuned for grounding, citation, and appropriate medical disclaimers. In Direction A, these instructions compete for attention with summarization, extraction, and other tasks in a single system prompt.

Expected improvement: fewer hallucinations, better citations, more specific suggestions. Measurable via the same quality eval (manual review of 50 samples) defined in Phase 1.

### Circle member suggestions

When a circle member views a shared summary, the orchestrator calls the Q&A Agent with:
- `mode: "suggest"`
- `viewer_context: { is_circle_member: true, circle_member_role: "child" }`
- Scoped data (respecting sharing permissions)

The Q&A Agent generates suggestions framed for the circle member's perspective: "What does this mean for daily care?" instead of "What does this mean for my treatment?"

---

## 9. Trade-offs

### Pros

| Advantage | Detail |
|---|---|
| **Modularity** | Test and tune each agent independently. Fix Q&A quality without touching summarization. |
| **Model optimization** | Haiku for extraction (fast, cheap), Opus for complex Q&A (high quality), Sonnet for everything else. Direction A uses one model for all tasks. |
| **Scalability** | Scale extraction independently from Q&A. Different concurrency limits per agent. |
| **Debuggability** | Each agent invocation is logged with exact input and output. Trace any issue to the specific agent. |
| **Extensibility** | Adding a new capability (e.g., medication interaction checking) = adding a new agent. No changes to existing agents. |
| **Prompt focus** | Each agent's system prompt is short and focused. Less prompt confusion than a monolith with 2,000-word instructions. |

### Cons

| Disadvantage | Detail |
|---|---|
| **Complexity** | More moving parts. Orchestrator logic, agent configs, inter-agent data flow. |
| **Latency** | Sequential agent chains add overhead. `process_conversation` takes 15-45s vs. Direction A's single-pass approach. |
| **Context fragmentation** | Each agent sees its slice of data, not the full picture. The Summary Agent doesn't know what the Extraction Agent found unless the Orchestrator bridges them. |
| **Token overhead** | Same data (transcript, profile) gets sent to multiple agents. Total tokens per request are higher. |
| **Orchestrator bottleneck** | All routing logic lives in one place. Bugs in the orchestrator affect everything. |
| **Debugging distributed flows** | Tracing a bug across 4 agent invocations is harder than reading one prompt-response pair. |

### When to choose Direction B

- **Production architecture**: when you need independent scaling, monitoring, and tuning per capability
- **Different models per task**: when cost optimization matters (Haiku for extraction saves 90% vs. Opus)
- **Team growth**: when different engineers own different agents
- **Capability expansion**: when you plan to add new agents regularly

### When NOT to choose Direction B

- **Prototype phase**: over-engineered for validating the core concept
- **Current scale**: 10 people, 35K users. Multi-agent coordination overhead isn't justified yet
- **Speed-to-learn**: Direction A gives the same user-facing result in less time to build

### Risk

The biggest risk is over-engineering. At Ditto's current scale, the modular advantages of Direction B don't compound. There's no team of 5 engineers each owning an agent. There's no traffic spike requiring independent scaling. The complexity cost is real; the benefits are theoretical until the team and user base grow.

---

## 10. Cost Model

### Token estimates per operation

| Operation | Agent | Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|---|---|
| Summarization | Summary | Sonnet | ~12,000 | ~800 | $0.042 |
| Extraction | Extraction | Haiku | ~12,000 | ~500 | $0.010 |
| Profile update | Profile | Sonnet | ~3,000 | ~400 | $0.014 |
| Q&A (answer) | Q&A | Sonnet | ~8,000 | ~400 | $0.028 |
| Q&A (answer, complex) | Q&A | Opus | ~8,000 | ~400 | $0.128 |
| Suggestion generation | Q&A | Sonnet | ~6,000 | ~200 | $0.020 |
| Audience adaptation | Sharing | Sonnet | ~4,000 | ~300 | $0.015 |
| Orchestrator overhead | Orchestrator | Sonnet | ~1,000 | ~200 | $0.005 |

Model pricing (April 2026 estimates, per 1M tokens):
- Haiku: $0.25 input / $1.25 output
- Sonnet: $3 input / $15 output
- Opus: $15 input / $75 output

### Cost per "full brain" processing of one appointment

Full pipeline: summary + extraction + profile + 2 sharing versions + suggestions + orchestrator.

| Component | Cost |
|---|---|
| Summary Agent (Sonnet) | $0.042 |
| Extraction Agent (Haiku) | $0.010 |
| Profile Agent (Sonnet) | $0.014 |
| Sharing Agent x2 (Sonnet) | $0.030 |
| Suggestion generation (Sonnet) | $0.020 |
| Orchestrator overhead (Sonnet) | $0.005 |
| **Total per appointment** | **$0.121** |

Add 2 Q&A answer calls per summary (average user engagement):

| With Q&A | Cost |
|---|---|
| Full pipeline | $0.121 |
| 2x Q&A answers (Sonnet) | $0.056 |
| **Total per appointment with Q&A** | **$0.177** |

### Monthly cost at scale

Assumptions: ~15% of users generate a summary per month. Average 1.5 summaries per active user. 2 circle members notified per summary. 2 Q&A interactions per summary.

| Users | Active users/mo | Summaries/mo | Full pipeline cost | Q&A cost | Total/mo |
|---|---|---|---|---|---|
| 5,000 | 750 | 1,125 | $136 | $63 | **$199** |
| 50,000 | 7,500 | 11,250 | $1,361 | $630 | **$1,991** |
| 500,000 | 75,000 | 112,500 | $13,613 | $6,300 | **$19,913** |

### Comparison with Direction A

Direction A runs the same tasks in fewer, larger LLM calls. Estimated Direction A cost per appointment: $0.08-0.12 (single large Sonnet call handles summary + extraction + suggestions).

| Scale | Direction A (est.) | Direction B | Difference |
|---|---|---|---|
| 5,000 users | $120-160/mo | $199/mo | +25-65% |
| 50,000 users | $1,200-1,600/mo | $1,991/mo | +25-65% |
| 500,000 users | $12,000-16,000/mo | $19,913/mo | +25-65% |

Direction B costs ~25-65% more due to:
1. Duplicate context: transcript sent to both Summary and Extraction agents
2. Orchestrator overhead: routing calls add tokens
3. Profile Agent: separate validation step that Direction A handles inline

The cost difference is modest in absolute terms. At 50K users, the delta is $400-800/month. The question is whether better quality per agent justifies it.

---

## 11. Prototype Scope

### What to build

A CLI tool that takes a conversation transcript and runs the full multi-agent pipeline. No mobile app, no API server, no database. Just the agent orchestration working end-to-end.

### Components

```
care-brain-prototype/
  orchestrator.ts          # Main entry, routing logic
  agents/
    summary.ts             # Summary Agent config + prompt
    extraction.ts          # Extraction Agent config + prompt
    qa.ts                  # Q&A Agent config + prompt (both modes)
  profile/
    store.ts               # JSON file-based health profile store
    schema.ts              # TypeScript interfaces for all schemas
  cli.ts                   # CLI entry point
  eval/
    conversations/         # 10 test conversations
    results/               # Output per conversation per direction
    compare.ts             # Side-by-side quality comparison
```

### Prototype agents (3 of 6)

Build only Summary, Extraction, and Q&A for the prototype. Skip Sharing, Profile, and Prep. Rationale: these three cover the core pipeline and produce the outputs most comparable to Direction A.

For the prototype, the Profile Agent's job is simplified to "write extractions directly to the JSON store with provenance metadata." No conflict resolution yet.

### CLI interface

```bash
# Process a conversation
$ care-brain-b process --input conversation_001.txt --patient patient_001

# Output:
# ✓ Summary Agent (Sonnet): 450 words, 8.2s, $0.042
# ✓ Extraction Agent (Haiku): 6 extractions, 1.5s, $0.010
# ✓ Profile updated: 6 fields written
# ✓ Suggestions generated: 3 chips
#
# Total: 12.1s, $0.072
# Output: results/patient_001/conversation_001/

# Ask a question about a processed conversation
$ care-brain-b ask --patient patient_001 --conversation conversation_001 \
  --question "What does the medication change mean?"

# Output:
# [Streaming answer...]
# Dr. van der Berg mentioned switching from capecitabine to oxaliplatin...
#
# Source: Conversation with Dr. van der Berg, 2026-03-15
# ⚕️ This is based on your conversation. For medical advice, contact your care team.
#
# Latency: 2.3s, Cost: $0.028

# Generate suggestions for a processed conversation
$ care-brain-b suggest --patient patient_001 --conversation conversation_001

# Compare Direction A vs B on same conversation
$ care-brain-b compare --input conversation_001.txt --patient patient_001
```

### Evaluation criteria

Run both Direction A and Direction B on the same 10 conversations. Compare:

| Criterion | How to measure |
|---|---|
| **Summary quality** | Blind review: which summary is more accurate, clear, complete? |
| **Extraction accuracy** | Count correct extractions vs. missed vs. hallucinated per direction |
| **Suggestion relevance** | Rate each suggestion 1-5 for specificity and usefulness |
| **Answer grounding** | Check: does every claim in the answer trace to the transcript? |
| **Latency** | End-to-end time for full pipeline |
| **Cost** | Total tokens and cost per conversation |
| **Consistency** | Run same conversation 3 times. How much does output vary? |

### Build estimate

| Component | Effort |
|---|---|
| Schemas + types | 2 hours |
| Agent configs + prompts | 3 hours |
| Orchestrator (routing, parallel execution) | 4 hours |
| Profile store (JSON file) | 2 hours |
| CLI | 2 hours |
| Eval harness + comparison tool | 3 hours |
| Run eval on 10 conversations | 2 hours |
| **Total** | **~18 hours** |

### Success criteria for prototype

The prototype succeeds if:
1. All 3 agents produce valid, well-structured output for all 10 conversations
2. Quality is comparable to or better than Direction A on blind review
3. Extraction accuracy is measurably better (hypothesis: focused agent = better extraction)
4. Total cost per conversation is within 2x of Direction A
5. The orchestration pattern is clean enough that adding a 4th agent is trivial

If extraction quality is NOT measurably better with a focused agent, the complexity argument for Direction B weakens significantly. That's the key signal.

---

## References

- [Care Brain Strategy](care-brain-strategy.md) — parent strategic spec
- [Smart Suggestions Phase 1](care-brain-phase1-smart-suggestions.md) — user-facing spec
- [ZeroClaw JTBD Discovery](../ideas/health-agent/zeroclaw-jtbd-discovery.md) — original job discovery
- [Unicorn Thesis](../ideas/activation-and-audience/unicorn-thesis-consumer-layer-healthcare.md) — strategic positioning
