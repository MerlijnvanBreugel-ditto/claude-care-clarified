# Direction A: The Concierge — Single Orchestrator Agent

**Date**: 2026-04-04
**Status**: Architecture spec (prototype-ready)
**Parent**: [Care Brain Strategy](care-brain-strategy.md)
**Purpose**: Complete technical specification for the simplest Care Brain architecture. One agent, one prompt, one brain. Detailed enough for a Claude Code agent to build a working prototype.

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     MOBILE APP                          │
│                                                         │
│  Summary View │ Q&A │ Profile │ Circle │ Prep │ Voice  │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTPS
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    API GATEWAY                          │
│                                                         │
│  POST /brain/process    POST /brain/ask                 │
│  POST /brain/voice      POST /brain/adapt               │
│  POST /brain/prep       GET  /brain/suggestions/:id     │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CARE BRAIN ORCHESTRATOR                     │
│                                                         │
│  Single Claude agent instance per request                │
│  System prompt + health profile + tools                  │
│  Stateless: full context injected per call               │
└───────┬───────────┬──────────┬──────────┬───────────────┘
        │           │          │          │
        ▼           ▼          ▼          ▼
   ┌─────────┐ ┌────────┐ ┌───────┐ ┌──────────┐
   │ Health   │ │ Summary│ │ Event │ │ Transcript│
   │ Profile  │ │ Store  │ │ Store │ │ Store     │
   │ (JSON)   │ │        │ │       │ │           │
   └─────────┘ └────────┘ └───────┘ └──────────┘
        │
        └── PostgreSQL (or equivalent)
```

**Core principle**: One Claude agent handles every brain operation. The agent receives the full health profile + relevant context on every call. It uses tools to structure its output. The app is the memory layer; the agent is the intelligence layer.

**Model**: Claude Sonnet for fast operations (suggestions, Q&A answers). Claude Opus for heavy reasoning (full summarization + extraction pipeline, pattern detection).

**Stateless by design**: No conversation memory between API calls. The health profile IS the memory. Every call gets the current profile state injected as context.

---

## 2. System Prompt

This is the core artifact of Direction A. The prompt defines what the brain is.

```
You are the Care Brain for Ditto Care, a healthcare app that transforms medical
conversations into patient-friendly understanding. You are the intelligence layer
that powers every surface of the app. You are not a chatbot. You are the brain.

## Identity

You work for Ditto Care B.V. (Rotterdam, Netherlands). Mission: "Care. Clarified."
Your users are patients navigating healthcare journeys (primarily oncology and
cardiology) and their care circle members (family, friends, caregivers).

Your primary audience is 45-75 years old. Many are dealing with serious diagnoses.
They are anxious, overwhelmed, and often forgotten by the healthcare system between
appointments. You exist to make their health journey understandable and shareable.

## What You Do

You have access to the patient's Health Profile (a structured JSON document) and
their conversation transcripts. Using these, you:

1. Summarize medical conversations in patient-friendly language
2. Extract structured health data (medications, conditions, care team, action items)
3. Generate contextual suggestions (questions a patient would want answered)
4. Answer follow-up questions grounded in the patient's actual data
5. Adapt content for different audiences in the patient's care circle
6. Generate appointment prep from journey context
7. Detect patterns across the patient's health timeline
8. Translate content while preserving medical accuracy

## Health Profile

You will receive the patient's Health Profile as a JSON object. This is your primary
context. It contains:

- Patient demographics and preferences
- Active conditions with source attribution
- Current medications with dosage and prescriber
- Care team members and their specialties
- Care circle members with relationship, language, and access level
- Journey events (appointments, changes, milestones) in chronological order
- Previous summary references with dates and key extractions

The Health Profile schema:

{
  "patient": {
    "id": "string (UUID)",
    "name": "string",
    "date_of_birth": "string (ISO 8601)",
    "preferred_language": "string (ISO 639-1, e.g. 'nl')",
    "additional_languages": ["string"],
    "created_at": "string (ISO 8601)"
  },
  "conditions": [
    {
      "id": "string (UUID)",
      "name": "string",
      "status": "active | resolved | monitoring",
      "diagnosed_date": "string (ISO 8601) | null",
      "source": {
        "type": "conversation | document | voice_input | manual",
        "reference_id": "string",
        "date": "string (ISO 8601)",
        "provider": "string | null"
      },
      "notes": "string | null"
    }
  ],
  "medications": [
    {
      "id": "string (UUID)",
      "name": "string",
      "dose": "string",
      "frequency": "string",
      "prescriber": "string | null",
      "start_date": "string (ISO 8601) | null",
      "end_date": "string (ISO 8601) | null",
      "status": "active | discontinued | changed",
      "source": {
        "type": "conversation | document | voice_input | manual",
        "reference_id": "string",
        "date": "string (ISO 8601)",
        "provider": "string | null"
      }
    }
  ],
  "care_team": [
    {
      "id": "string (UUID)",
      "name": "string",
      "specialty": "string",
      "institution": "string | null",
      "last_visit": "string (ISO 8601) | null",
      "source": {
        "type": "conversation | document | voice_input | manual",
        "reference_id": "string",
        "date": "string (ISO 8601)"
      }
    }
  ],
  "care_circle": [
    {
      "id": "string (UUID)",
      "name": "string",
      "relationship": "string (e.g. 'partner', 'daughter', 'friend', 'neighbor')",
      "access_level": "full | summary | minimal",
      "preferred_language": "string (ISO 639-1)",
      "detail_preference": "clinical | standard | simplified",
      "notification_preference": "immediate | daily_digest | manual"
    }
  ],
  "journey_events": [
    {
      "id": "string (UUID)",
      "type": "appointment | medication_change | diagnosis | lab_result | procedure | milestone | voice_update",
      "date": "string (ISO 8601)",
      "title": "string",
      "description": "string",
      "provider": "string | null",
      "related_condition": "string (condition ID) | null",
      "source": {
        "type": "conversation | document | voice_input | manual",
        "reference_id": "string"
      }
    }
  ],
  "summaries": [
    {
      "id": "string (UUID)",
      "date": "string (ISO 8601)",
      "provider": "string",
      "specialty": "string",
      "title": "string",
      "key_topics": ["string"],
      "extracted_medications": ["string (medication IDs)"],
      "extracted_conditions": ["string (condition IDs)"],
      "extracted_action_items": ["string"],
      "transcript_id": "string"
    }
  ]
}

## Grounding Rules (CRITICAL)

1. ONLY answer from the patient's data. Your knowledge comes from:
   - The conversation transcript(s) provided
   - The Health Profile
   - Previous summaries referenced in the profile
   You do NOT have general medical knowledge. You do NOT know things the doctor
   did not say. If the answer is not in the data, say: "This wasn't discussed in
   your conversations with [doctor]. You could ask about this at your next
   appointment."

2. ALWAYS attribute information to its source. Say "Dr. van der Berg mentioned..."
   or "In your appointment on [date]..." Never present information without
   attribution.

3. NEVER provide medical advice. You explain what was discussed. You do not
   recommend, diagnose, suggest treatments, or assess urgency. If a user asks
   "Should I be worried?" respond with what the doctor said about prognosis or
   next steps, and add: "For medical advice, contact your care team."

4. NEVER perform triage. If a user describes symptoms that sound urgent, always
   respond: "If you're concerned about your health, please contact your GP or
   call 112. I can help you review what was discussed with your doctor, but I'm
   not able to assess medical situations."

5. NEVER fill gaps with assumptions. If the doctor mentioned a medication but not
   the dosage, say "The dosage wasn't mentioned in the conversation." Do not
   guess.

6. When extracting health data, flag uncertainty. If you're 80%+ confident, extract
   it. If you're 50-80% confident, extract it with a "needs_confirmation": true
   flag. Below 50%, skip it and log it as unextracted.

## Audience Adaptation Rules

When generating content for care circle members, adapt based on three dimensions:

### Access Level
- full: Include all clinical details, medication names, test results, action items
- summary: Include key outcomes, next steps, emotional tone. Omit specific dosages,
  detailed test values, clinical terminology
- minimal: "The appointment went well. Next appointment is [date]." Only share
  what the patient has explicitly approved.

### Detail Preference
- clinical: Use medical terminology. Include specific values. Structured format.
  For: partners who attend appointments, medically trained circle members
- standard: Plain language but complete. Default for most circle members.
- simplified: Short sentences. Essential information only. No medical terms.
  For: elderly parents, children, friends who want the headline.

### Language
- Generate in the circle member's preferred_language
- Preserve medical terms that don't translate well (add explanation in parentheses)
- For Dutch medical terms in non-Dutch output: keep the Dutch term if the care
  happens in NL ("Your echografie (ultrasound) results were normal")

### Adaptation examples

Same information, three audiences:

Patient (clinical, nl):
"Dr. de Vries heeft de capecitabine gestopt en je overgeschakeld naar oxaliplatine
(85mg/m², elke 2 weken). Reden: onvoldoende respons op de laatste CT-scan. Volgende
scan over 6 weken om de respons te beoordelen."

Partner (standard, nl):
"De oncoloog heeft besloten om over te stappen op een ander type chemotherapie
(oxaliplatine) omdat de huidige behandeling niet genoeg werkte. De komende weken
kan [patiënt] last hebben van tintelingen in handen en voeten. Over 6 weken is
er een scan om te zien hoe de nieuwe behandeling werkt."

Elderly parent (simplified, nl):
"[Patiënt] is vandaag bij de oncoloog geweest. De dokter heeft de medicijnen
aangepast. Over 6 weken is er weer een controle. [Patiënt] voelt zich goed."

Friend (minimal, en):
"[Patient] had their oncology appointment today. Treatment plan has been adjusted.
Next check-up in 6 weeks. They're doing okay."

## Tone

- Warm but not patronizing. You speak to adults navigating difficult situations.
- Clear without being simplistic. Linguistic precision matters.
- Calm. Never alarming, never dismissive.
- Use "your doctor" or the doctor's name, never "we" (you are not part of the
  care team).
- In Dutch: use "u" (formal), not "je", unless the patient's profile indicates
  informal preference.
- Never use emoji in medical content. Emoji are acceptable only in care circle
  notifications where the tone is casual.

## Safety Guardrails

1. If the user mentions suicidal thoughts or self-harm, respond:
   "Als je in nood bent, neem contact op met 113 Zelfmoordpreventie (0900-0113)
   of bel 112. Ik ben er om je te helpen met je gezondheidsgegevens, maar dit
   gesprek verdient professionele hulp."
   (Adapt language to user's preference. Always provide the Dutch crisis number.)

2. If the user asks about drug interactions, respond with what the doctor
   discussed. Add: "For questions about how your medications interact, contact
   your pharmacist or prescribing doctor. I can only share what was discussed
   in your appointments."

3. If the user asks you to interpret symptoms, lab values, or scans beyond what
   the doctor said, respond: "I can share what Dr. [name] said about your
   results. For interpretation beyond what was discussed, your care team is the
   best source."

4. Never generate content that could be mistaken for a prescription, referral,
   or medical order.

## Output Language

Default to the patient's preferred_language from the Health Profile. If the request
specifies a different language (e.g., generating content for a circle member), use
that language instead. Medical terms should be in the language of the healthcare
system (usually Dutch for NL-based care) with translations where needed.
```

---

## 3. Tool Definitions

Each tool is a structured function the agent can call. The agent decides which tools to invoke based on the request. Tools return structured JSON that the orchestrator stores and routes to the app.

### 3.1 `summarize_conversation`

Transforms a raw medical conversation transcript into a patient-friendly summary.

```json
{
  "name": "summarize_conversation",
  "description": "Generate a patient-friendly summary from a medical conversation transcript. The summary should be structured, scannable, and reference the patient's journey context where relevant.",
  "parameters": {
    "type": "object",
    "required": ["transcript", "health_profile"],
    "properties": {
      "transcript": {
        "type": "string",
        "description": "The full conversation transcript (speaker-labeled)"
      },
      "health_profile": {
        "type": "object",
        "description": "The patient's current Health Profile JSON"
      },
      "previous_summaries": {
        "type": "array",
        "items": { "type": "object" },
        "description": "Array of previous summary objects for cross-appointment context (optional, most recent 5)"
      },
      "language": {
        "type": "string",
        "description": "ISO 639-1 language code for the summary output. Defaults to patient's preferred_language."
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "summary_id": { "type": "string" },
      "title": { "type": "string", "description": "Short title, e.g. 'Oncologie controle — Dr. de Vries'" },
      "date": { "type": "string" },
      "provider": { "type": "string" },
      "specialty": { "type": "string" },
      "sections": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "heading": { "type": "string" },
            "content": { "type": "string" },
            "source_quotes": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Direct quotes from the transcript supporting this section"
            }
          }
        }
      },
      "key_topics": { "type": "array", "items": { "type": "string" } },
      "action_items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "description": { "type": "string" },
            "due_date": { "type": "string", "description": "ISO 8601 or null" },
            "owner": { "type": "string", "description": "'patient' | 'provider' | 'care_circle'" }
          }
        }
      },
      "cross_appointment_references": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "reference_summary_id": { "type": "string" },
            "connection": { "type": "string", "description": "What connects this appointment to the referenced one" }
          }
        }
      },
      "language": { "type": "string" }
    }
  }
}
```

### 3.2 `extract_health_data`

Extracts structured health profile updates from any text input (transcript, document, voice transcription).

```json
{
  "name": "extract_health_data",
  "description": "Extract structured health data from text. Returns proposed updates to the patient's Health Profile. All extractions include confidence scores and source attribution.",
  "parameters": {
    "type": "object",
    "required": ["text", "health_profile", "source_type"],
    "properties": {
      "text": {
        "type": "string",
        "description": "The text to extract from (transcript, document text, voice transcription)"
      },
      "health_profile": {
        "type": "object",
        "description": "The patient's current Health Profile (needed to detect changes vs. known data)"
      },
      "source_type": {
        "type": "string",
        "enum": ["conversation", "document", "voice_input", "manual"],
        "description": "The type of source this text came from"
      },
      "source_reference_id": {
        "type": "string",
        "description": "ID of the source record (transcript ID, document ID, etc.)"
      },
      "source_date": {
        "type": "string",
        "description": "ISO 8601 date of the source"
      },
      "source_provider": {
        "type": "string",
        "description": "Name of the healthcare provider if applicable"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "conditions": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "action": { "type": "string", "enum": ["add", "update", "resolve"] },
            "existing_id": { "type": "string", "description": "ID of existing condition if update/resolve" },
            "data": { "type": "object", "description": "Condition object per Health Profile schema" },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "needs_confirmation": { "type": "boolean" },
            "evidence_quote": { "type": "string" }
          }
        }
      },
      "medications": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "action": { "type": "string", "enum": ["add", "update", "discontinue"] },
            "existing_id": { "type": "string" },
            "data": { "type": "object" },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "needs_confirmation": { "type": "boolean" },
            "evidence_quote": { "type": "string" }
          }
        }
      },
      "care_team": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "action": { "type": "string", "enum": ["add", "update"] },
            "existing_id": { "type": "string" },
            "data": { "type": "object" },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "evidence_quote": { "type": "string" }
          }
        }
      },
      "journey_events": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "data": { "type": "object" },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "evidence_quote": { "type": "string" }
          }
        }
      },
      "action_items": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "description": { "type": "string" },
            "due_date": { "type": "string" },
            "owner": { "type": "string" },
            "confidence": { "type": "number" }
          }
        }
      },
      "unextracted": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "text_segment": { "type": "string" },
            "reason": { "type": "string", "description": "Why it wasn't extracted (ambiguous, low confidence, etc.)" }
          }
        }
      }
    }
  }
}
```

### 3.3 `generate_suggestions`

Generates contextual follow-up questions for a summary. The primary user-facing brain feature.

```json
{
  "name": "generate_suggestions",
  "description": "Generate 2-3 contextual suggestion questions that a patient (or circle member) would likely want answered after reading a summary. Questions must be specific to THIS conversation, grounded in the data, and answerable from the available context.",
  "parameters": {
    "type": "object",
    "required": ["summary", "health_profile"],
    "properties": {
      "summary": {
        "type": "object",
        "description": "The generated summary object"
      },
      "health_profile": {
        "type": "object",
        "description": "The patient's Health Profile"
      },
      "transcript": {
        "type": "string",
        "description": "The conversation transcript (for depth of suggestion generation)"
      },
      "viewer_type": {
        "type": "string",
        "enum": ["patient", "circle_member"],
        "description": "Who will see these suggestions"
      },
      "circle_member": {
        "type": "object",
        "description": "Care circle member object (if viewer_type is circle_member)"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "suggestions": {
        "type": "array",
        "minItems": 2,
        "maxItems": 3,
        "items": {
          "type": "object",
          "properties": {
            "id": { "type": "string" },
            "question": { "type": "string", "description": "The suggestion text shown to the user" },
            "category": {
              "type": "string",
              "enum": ["treatment", "medication", "next_steps", "cross_appointment", "lifestyle", "care_circle"],
              "description": "Question category for analytics"
            },
            "answerable_confidence": {
              "type": "number",
              "minimum": 0,
              "maximum": 1,
              "description": "How confident the brain is that it can answer this from available context"
            },
            "requires_context": {
              "type": "array",
              "items": { "type": "string" },
              "description": "What context sources are needed to answer (e.g., 'current_transcript', 'previous_summary:abc-123')"
            }
          }
        }
      }
    }
  }
}
```

### 3.4 `answer_question`

Generates a grounded answer to a question (either from a suggestion or user-typed).

```json
{
  "name": "answer_question",
  "description": "Answer a question about the patient's health journey. The answer MUST be grounded in the provided context (transcript, summary, profile). Never use general medical knowledge.",
  "parameters": {
    "type": "object",
    "required": ["question", "health_profile"],
    "properties": {
      "question": {
        "type": "string",
        "description": "The question to answer"
      },
      "health_profile": {
        "type": "object",
        "description": "The patient's Health Profile"
      },
      "transcript": {
        "type": "string",
        "description": "The relevant conversation transcript"
      },
      "summary": {
        "type": "object",
        "description": "The summary this question relates to"
      },
      "previous_summaries": {
        "type": "array",
        "items": { "type": "object" },
        "description": "Previous summaries for cross-appointment context"
      },
      "viewer_type": {
        "type": "string",
        "enum": ["patient", "circle_member"]
      },
      "circle_member": {
        "type": "object",
        "description": "If viewer is a circle member, their profile (for access level and language)"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "answer": {
        "type": "string",
        "description": "The answer text (200-400 words, patient-friendly)"
      },
      "sources": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": { "type": "string", "enum": ["transcript_quote", "summary_reference", "profile_data"] },
            "content": { "type": "string" },
            "date": { "type": "string" },
            "provider": { "type": "string" }
          }
        },
        "description": "Source attributions for the answer"
      },
      "disclaimer": {
        "type": "string",
        "description": "Medical disclaimer, always present"
      },
      "confidence": {
        "type": "number",
        "minimum": 0,
        "maximum": 1,
        "description": "How well the question could be answered from available data"
      },
      "unanswered_aspects": {
        "type": "array",
        "items": { "type": "string" },
        "description": "Parts of the question that couldn't be answered from available data"
      },
      "language": { "type": "string" }
    }
  }
}
```

### 3.5 `adapt_for_audience`

Transforms content for a specific care circle member based on their profile.

```json
{
  "name": "adapt_for_audience",
  "description": "Adapt content (summary, update, answer) for a specific care circle member. Respects their access level, detail preference, and language.",
  "parameters": {
    "type": "object",
    "required": ["content", "content_type", "circle_member", "health_profile"],
    "properties": {
      "content": {
        "type": "string",
        "description": "The original content to adapt"
      },
      "content_type": {
        "type": "string",
        "enum": ["summary", "update", "answer", "notification"],
        "description": "What kind of content is being adapted"
      },
      "circle_member": {
        "type": "object",
        "description": "The target care circle member's profile"
      },
      "health_profile": {
        "type": "object",
        "description": "The patient's Health Profile (for context)"
      },
      "patient_note": {
        "type": "string",
        "description": "Optional personal note from the patient to include"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "adapted_content": { "type": "string" },
      "language": { "type": "string" },
      "access_level_applied": { "type": "string" },
      "detail_level_applied": { "type": "string" },
      "omitted_categories": {
        "type": "array",
        "items": { "type": "string" },
        "description": "What was removed due to access level (e.g., 'medication_dosages', 'lab_values')"
      },
      "tone": { "type": "string", "description": "Description of tone used (e.g., 'warm and reassuring', 'factual and complete')" }
    }
  }
}
```

### 3.6 `generate_appointment_prep`

Creates a prep summary for an upcoming appointment based on the patient's journey.

```json
{
  "name": "generate_appointment_prep",
  "description": "Generate a personalized appointment prep summary. Covers: what happened since last visit with this provider, current medications, unresolved items, and suggested questions.",
  "parameters": {
    "type": "object",
    "required": ["health_profile", "upcoming_appointment"],
    "properties": {
      "health_profile": {
        "type": "object",
        "description": "The patient's full Health Profile"
      },
      "upcoming_appointment": {
        "type": "object",
        "properties": {
          "provider": { "type": "string" },
          "specialty": { "type": "string" },
          "date": { "type": "string" },
          "institution": { "type": "string" }
        }
      },
      "previous_transcripts": {
        "type": "array",
        "items": { "type": "string" },
        "description": "Transcripts from previous visits with this provider (most recent 3)"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "prep_summary": {
        "type": "object",
        "properties": {
          "since_last_visit": {
            "type": "string",
            "description": "Narrative of what happened since last appointment with this provider"
          },
          "current_medications": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "dose": { "type": "string" },
                "changed_since_last": { "type": "boolean" }
              }
            }
          },
          "unresolved_items": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Action items or questions from previous visits that weren't completed/answered"
          },
          "suggested_questions": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "question": { "type": "string" },
                "reason": { "type": "string", "description": "Why this question is relevant based on journey context" }
              }
            },
            "maxItems": 5
          },
          "provider_context": {
            "type": "string",
            "description": "Brief note about this provider's role in the care journey"
          }
        }
      },
      "language": { "type": "string" }
    }
  }
}
```

### 3.7 `detect_patterns`

Analyzes the patient's journey history for patterns (symptom trends, correlations, recurring themes).

```json
{
  "name": "detect_patterns",
  "description": "Analyze the patient's journey events, summaries, and voice updates for patterns. Returns observations, not diagnoses. All patterns must be sourced from recorded data.",
  "parameters": {
    "type": "object",
    "required": ["health_profile"],
    "properties": {
      "health_profile": {
        "type": "object",
        "description": "The patient's full Health Profile with journey events"
      },
      "focus_area": {
        "type": "string",
        "description": "Optional: specific area to focus pattern detection on (e.g., 'fatigue', 'medication_side_effects', 'mood')"
      },
      "time_range": {
        "type": "object",
        "properties": {
          "start": { "type": "string" },
          "end": { "type": "string" }
        },
        "description": "Optional: limit pattern detection to a time range"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "patterns": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "description": { "type": "string", "description": "Plain-language description of the pattern" },
            "type": { "type": "string", "enum": ["symptom_trend", "medication_correlation", "appointment_pattern", "treatment_progression", "lifestyle_pattern"] },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "data_points": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "event_id": { "type": "string" },
                  "date": { "type": "string" },
                  "description": { "type": "string" }
                }
              }
            },
            "suggested_action": {
              "type": "string",
              "description": "What the patient might want to discuss with their doctor"
            }
          }
        }
      },
      "insufficient_data": {
        "type": "array",
        "items": { "type": "string" },
        "description": "Areas where there isn't enough data for pattern detection yet"
      }
    }
  }
}
```

### 3.8 `translate_content`

Translates content while preserving medical accuracy and appropriate tone.

```json
{
  "name": "translate_content",
  "description": "Translate content to a target language. Preserves medical term accuracy, adjusts cultural context where needed. Dutch medical terms are kept with parenthetical translation when the healthcare context is NL-based.",
  "parameters": {
    "type": "object",
    "required": ["content", "target_language"],
    "properties": {
      "content": {
        "type": "string",
        "description": "The content to translate"
      },
      "target_language": {
        "type": "string",
        "description": "ISO 639-1 language code"
      },
      "content_type": {
        "type": "string",
        "enum": ["summary", "answer", "notification", "prep"],
        "description": "Type of content (affects formality and medical term handling)"
      },
      "healthcare_country": {
        "type": "string",
        "default": "NL",
        "description": "Country where healthcare is provided (affects which medical terms to keep in original)"
      }
    }
  },
  "returns": {
    "type": "object",
    "properties": {
      "translated_content": { "type": "string" },
      "source_language": { "type": "string" },
      "target_language": { "type": "string" },
      "preserved_terms": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "original": { "type": "string" },
            "explanation": { "type": "string" }
          }
        },
        "description": "Medical terms kept in original language with translation"
      }
    }
  }
}
```

---

## 4. Health Profile Schema

The full JSON Schema for the Health Profile. This is the structured memory of the brain. Stored in the database, passed as context on every agent call.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "DittoCareHealthProfile",
  "description": "Patient health profile maintained by the Care Brain. Updated after every interaction.",
  "type": "object",
  "required": ["patient", "conditions", "medications", "care_team", "care_circle", "journey_events", "summaries"],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "1.0.0"
    },
    "patient": {
      "type": "object",
      "required": ["id", "name", "preferred_language"],
      "properties": {
        "id": { "type": "string", "format": "uuid" },
        "name": { "type": "string" },
        "date_of_birth": { "type": "string", "format": "date" },
        "preferred_language": { "type": "string", "pattern": "^[a-z]{2}$" },
        "additional_languages": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[a-z]{2}$" }
        },
        "formality_preference": {
          "type": "string",
          "enum": ["formal", "informal"],
          "default": "formal",
          "description": "In Dutch: 'u' vs 'je'"
        },
        "created_at": { "type": "string", "format": "date-time" },
        "updated_at": { "type": "string", "format": "date-time" }
      }
    },
    "conditions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "status", "source"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "name": { "type": "string" },
          "icd10_code": { "type": "string", "description": "Optional ICD-10 code if identifiable" },
          "status": {
            "type": "string",
            "enum": ["active", "resolved", "monitoring"]
          },
          "diagnosed_date": { "type": ["string", "null"], "format": "date" },
          "resolved_date": { "type": ["string", "null"], "format": "date" },
          "related_conditions": {
            "type": "array",
            "items": { "type": "string", "format": "uuid" },
            "description": "IDs of related conditions (e.g., metastasis related to primary cancer)"
          },
          "source": { "$ref": "#/$defs/source_attribution" },
          "notes": { "type": ["string", "null"] }
        }
      }
    },
    "medications": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "status", "source"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "name": { "type": "string" },
          "generic_name": { "type": ["string", "null"] },
          "dose": { "type": "string" },
          "frequency": { "type": "string", "description": "e.g., '2x daily', 'every 2 weeks IV'" },
          "route": {
            "type": "string",
            "enum": ["oral", "iv", "subcutaneous", "topical", "inhaled", "other"],
            "description": "Route of administration"
          },
          "prescriber": { "type": ["string", "null"] },
          "prescriber_id": { "type": ["string", "null"], "format": "uuid", "description": "Reference to care_team member" },
          "start_date": { "type": ["string", "null"], "format": "date" },
          "end_date": { "type": ["string", "null"], "format": "date" },
          "status": {
            "type": "string",
            "enum": ["active", "discontinued", "changed", "paused"]
          },
          "reason_for_change": { "type": ["string", "null"] },
          "replaced_by": { "type": ["string", "null"], "format": "uuid", "description": "ID of medication that replaced this one" },
          "source": { "$ref": "#/$defs/source_attribution" }
        }
      }
    },
    "care_team": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "specialty", "source"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "name": { "type": "string" },
          "specialty": { "type": "string" },
          "institution": { "type": ["string", "null"] },
          "department": { "type": ["string", "null"] },
          "role": {
            "type": "string",
            "description": "e.g., 'primary oncologist', 'GP', 'surgeon'"
          },
          "last_visit": { "type": ["string", "null"], "format": "date" },
          "next_visit": { "type": ["string", "null"], "format": "date" },
          "source": { "$ref": "#/$defs/source_attribution" }
        }
      }
    },
    "care_circle": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "relationship", "access_level"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "name": { "type": "string" },
          "relationship": {
            "type": "string",
            "description": "e.g., 'partner', 'daughter', 'son', 'friend', 'neighbor', 'colleague'"
          },
          "access_level": {
            "type": "string",
            "enum": ["full", "summary", "minimal"],
            "description": "How much health data this person can see"
          },
          "preferred_language": { "type": "string", "pattern": "^[a-z]{2}$" },
          "detail_preference": {
            "type": "string",
            "enum": ["clinical", "standard", "simplified"]
          },
          "notification_preference": {
            "type": "string",
            "enum": ["immediate", "daily_digest", "manual"]
          },
          "user_id": {
            "type": ["string", "null"],
            "format": "uuid",
            "description": "Ditto user ID if this circle member has their own account"
          }
        }
      }
    },
    "journey_events": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "type", "date", "title", "source"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "type": {
            "type": "string",
            "enum": [
              "appointment",
              "medication_change",
              "diagnosis",
              "lab_result",
              "procedure",
              "milestone",
              "voice_update",
              "hospitalization",
              "referral"
            ]
          },
          "date": { "type": "string", "format": "date" },
          "title": { "type": "string" },
          "description": { "type": "string" },
          "provider": { "type": ["string", "null"] },
          "provider_id": { "type": ["string", "null"], "format": "uuid" },
          "related_condition": { "type": ["string", "null"], "format": "uuid" },
          "related_medications": {
            "type": "array",
            "items": { "type": "string", "format": "uuid" }
          },
          "significance": {
            "type": "string",
            "enum": ["routine", "notable", "major"],
            "description": "How significant this event is in the care journey"
          },
          "source": { "$ref": "#/$defs/source_attribution" }
        }
      }
    },
    "summaries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "date", "title", "transcript_id"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "date": { "type": "string", "format": "date" },
          "provider": { "type": "string" },
          "provider_id": { "type": ["string", "null"], "format": "uuid" },
          "specialty": { "type": "string" },
          "institution": { "type": ["string", "null"] },
          "title": { "type": "string" },
          "key_topics": { "type": "array", "items": { "type": "string" } },
          "extracted_medications": {
            "type": "array",
            "items": { "type": "string", "format": "uuid" }
          },
          "extracted_conditions": {
            "type": "array",
            "items": { "type": "string", "format": "uuid" }
          },
          "extracted_action_items": {
            "type": "array",
            "items": { "type": "string" }
          },
          "transcript_id": { "type": "string" },
          "suggestion_ids": {
            "type": "array",
            "items": { "type": "string" },
            "description": "IDs of generated suggestions for this summary"
          }
        }
      }
    }
  },
  "$defs": {
    "source_attribution": {
      "type": "object",
      "required": ["type", "reference_id", "date"],
      "properties": {
        "type": {
          "type": "string",
          "enum": ["conversation", "document", "voice_input", "manual"]
        },
        "reference_id": { "type": "string" },
        "date": { "type": "string", "format": "date" },
        "provider": { "type": ["string", "null"] }
      }
    }
  }
}
```

**Key design decisions**:

| Decision | Rationale |
|---|---|
| Every data point has `source` attribution | The brain never presents information without knowing where it came from. Grounding rule #2. |
| Medications track `replaced_by` chains | "They changed my medication" is the #1 extraction scenario. The chain shows treatment progression. |
| Journey events have `significance` levels | Enables smart filtering. Routine check-ups don't clutter the prep screen. Major events always surface. |
| Care circle has `detail_preference` separate from `access_level` | A partner might have `full` access but prefer `standard` detail. A nurse-daughter might have `summary` access but prefer `clinical` detail. These are independent dimensions. |
| Summaries store `key_topics` and `extracted_*` IDs | Enables cross-appointment reasoning without loading full summary text every time. |

---

## 5. Request Flow Scenarios

### Scenario 1: Patient records oncologist appointment

**Trigger**: Patient presses stop on the recording. Transcript is ready.

```
Mobile App                    API Gateway               Care Brain Agent
    │                              │                           │
    │  POST /brain/process         │                           │
    │  { transcript,               │                           │
    │    patient_id }              │                           │
    │─────────────────────────────>│                           │
    │                              │  Load health_profile      │
    │                              │  from DB                  │
    │                              │                           │
    │                              │  Invoke agent with:       │
    │                              │  - system prompt           │
    │                              │  - health_profile          │
    │                              │  - transcript              │
    │                              │  - last 5 summaries        │
    │                              │──────────────────────────>│
    │                              │                           │
    │                              │        Agent chain:        │
    │                              │                           │
    │                              │  1. summarize_conversation │
    │                              │     → structured summary   │
    │                              │                           │
    │                              │  2. extract_health_data    │
    │                              │     → profile updates      │
    │                              │     (meds, conditions,     │
    │                              │      care team, events)    │
    │                              │                           │
    │                              │  3. generate_suggestions   │
    │                              │     → 2-3 question chips   │
    │                              │                           │
    │                              │<──────────────────────────│
    │                              │                           │
    │                              │  Store results:            │
    │                              │  - summary → summary_store │
    │                              │  - profile updates → apply │
    │                              │    to health_profile       │
    │                              │  - suggestions → cache     │
    │                              │                           │
    │  Response (async callback    │                           │
    │  or polling):                │                           │
    │  { summary, suggestions,     │                           │
    │    profile_updates_pending } │                           │
    │<─────────────────────────────│                           │
    │                              │                           │
    │  Display summary +           │                           │
    │  suggestion chips            │                           │
```

**API call details**:

```
POST /brain/process
Content-Type: application/json

{
  "patient_id": "abc-123",
  "transcript_id": "txn-456",
  "transcript": "Doctor: Goedemorgen mevrouw Jansen...",
  "processing_mode": "full"
}
```

**Response** (returned via webhook or polling, since processing takes 15-45 seconds):

```json
{
  "status": "completed",
  "summary": {
    "summary_id": "sum-789",
    "title": "Oncologie controle — Dr. de Vries",
    "date": "2026-04-04",
    "provider": "Dr. de Vries",
    "specialty": "Oncologie",
    "sections": [
      {
        "heading": "Scan resultaten",
        "content": "De CT-scan van vorige week laat zien dat de tumor kleiner is geworden...",
        "source_quotes": ["De scan ziet er goed uit, de tumor is duidelijk kleiner geworden"]
      }
    ],
    "key_topics": ["CT-scan resultaten", "medicatie wijziging", "volgende controle"],
    "action_items": [
      {
        "description": "Bloedonderzoek over 3 weken bij huisarts",
        "due_date": "2026-04-25",
        "owner": "patient"
      }
    ]
  },
  "suggestions": [
    {
      "id": "sug-001",
      "question": "Wat betekent het dat de tumor kleiner is geworden voor uw behandelplan?",
      "category": "treatment"
    },
    {
      "id": "sug-002",
      "question": "Wat zijn de mogelijke bijwerkingen van oxaliplatine waar u op moet letten?",
      "category": "medication"
    },
    {
      "id": "sug-003",
      "question": "Hoe verhoudt dit resultaat zich tot uw eerdere scan in januari?",
      "category": "cross_appointment"
    }
  ],
  "profile_updates": {
    "medications": [
      {
        "action": "discontinue",
        "existing_id": "med-111",
        "confidence": 0.95,
        "evidence_quote": "We stoppen met de capecitabine"
      },
      {
        "action": "add",
        "data": {
          "name": "oxaliplatine",
          "dose": "85mg/m²",
          "frequency": "elke 2 weken",
          "route": "iv",
          "prescriber": "Dr. de Vries"
        },
        "confidence": 0.92,
        "needs_confirmation": false,
        "evidence_quote": "We gaan over op oxaliplatine, 85 milligram per vierkante meter"
      }
    ],
    "journey_events": [
      {
        "data": {
          "type": "medication_change",
          "date": "2026-04-04",
          "title": "Overschakeling naar oxaliplatine",
          "description": "Capecitabine gestopt wegens onvoldoende respons. Oxaliplatine gestart.",
          "significance": "major"
        },
        "confidence": 0.95
      }
    ]
  }
}
```

**Total tokens**: ~8K in (transcript ~5K + profile ~2K + summaries ~1K), ~3K out. Single agent call.

---

### Scenario 2: Circle member taps a suggestion on shared summary

**Trigger**: Patient's partner opens the app, sees the shared summary, taps "What does this medication change mean for daily care?"

```
Mobile App                    API Gateway               Care Brain Agent
    │                              │                           │
    │  POST /brain/ask             │                           │
    │  { question,                 │                           │
    │    summary_id,               │                           │
    │    viewer_type: "circle",    │                           │
    │    circle_member_id }        │                           │
    │─────────────────────────────>│                           │
    │                              │  Load:                    │
    │                              │  - health_profile         │
    │                              │  - summary (sum-789)      │
    │                              │  - transcript (txn-456)   │
    │                              │  - circle_member profile  │
    │                              │                           │
    │                              │  Check: does circle member│
    │                              │  have access to this data?│
    │                              │                           │
    │                              │  Invoke agent:            │
    │                              │  answer_question(         │
    │                              │    question,              │
    │                              │    health_profile,        │
    │                              │    transcript,            │
    │                              │    summary,               │
    │                              │    viewer_type: "circle", │
    │                              │    circle_member          │
    │                              │  )                        │
    │                              │──────────────────────────>│
    │                              │                           │
    │   SSE stream starts          │       Agent generates     │
    │   (answer tokens stream)     │       answer adapted for  │
    │<─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │       circle member's     │
    │                              │       access + detail +   │
    │   Answer renders inline      │       language prefs      │
    │   below the suggestion chip  │                           │
    │                              │<──────────────────────────│
    │                              │                           │
    │   Full answer + disclaimer   │  Cache answer             │
    │<─────────────────────────────│                           │
```

**API call**:

```
POST /brain/ask
Content-Type: application/json

{
  "patient_id": "abc-123",
  "summary_id": "sum-789",
  "question": "Wat betekent deze medicatiewijziging voor de dagelijkse zorg?",
  "viewer_type": "circle_member",
  "circle_member_id": "cc-partner-001",
  "suggestion_id": "sug-001",
  "stream": true
}
```

**Response** (streamed via SSE, then cached):

```json
{
  "answer": "Dr. de Vries heeft besloten om de behandeling aan te passen. In plaats van capecitabine (tabletten die [patiënt] thuis innam) krijgt zij nu oxaliplatine via een infuus in het ziekenhuis, elke twee weken.\n\nVoor de dagelijkse zorg betekent dit:\n\n- De dagelijkse tabletten stoppen. Dat scheelt in het thuisschema.\n- Elke twee weken een ziekenhuisbezoek van enkele uren voor het infuus.\n- Mogelijke bijwerkingen waar u op kunt letten: tintelingen in handen en voeten, en gevoeligheid voor kou. Dr. de Vries noemde dit specifiek als iets om in de gaten te houden.\n- Het bloedonderzoek over 3 weken bij de huisarts is belangrijk. Dit moet voor het volgende infuus plaatsvinden.\n\nDe reden voor de overschakeling is dat de huidige behandeling onvoldoende werkte. De CT-scan liet wel verbetering zien, maar de oncoloog wil een sterker resultaat.",
  "sources": [
    {
      "type": "transcript_quote",
      "content": "We gaan over op oxaliplatine, 85 milligram per vierkante meter, elke twee weken via een infuus",
      "date": "2026-04-04",
      "provider": "Dr. de Vries"
    },
    {
      "type": "transcript_quote",
      "content": "Let op tintelingen in de handen en voeten, en gevoeligheid voor kou",
      "date": "2026-04-04",
      "provider": "Dr. de Vries"
    }
  ],
  "disclaimer": "Dit is gebaseerd op het gesprek met Dr. de Vries op 4 april 2026. Voor medisch advies kunt u contact opnemen met het zorgteam.",
  "confidence": 0.93,
  "language": "nl"
}
```

**Total tokens**: ~7K in (transcript + summary + profile + circle member context), ~500 out. Streamed, first token <1.5s.

---

### Scenario 3: Patient says "They changed my medication" via voice

**Trigger**: Patient taps the microphone on the home screen and says: "De dokter heeft vandaag mijn medicijn veranderd. Ik neem nu letrozol in plaats van tamoxifen, 2.5 milligram per dag."

```
Mobile App                    API Gateway               Care Brain Agent
    │                              │                           │
    │  [Audio captured by app]     │                           │
    │  [STT: Whisper/Deepgram]     │                           │
    │  [Text ready]                │                           │
    │                              │                           │
    │  POST /brain/voice           │                           │
    │  { transcription,            │                           │
    │    patient_id }              │                           │
    │─────────────────────────────>│                           │
    │                              │  Load health_profile      │
    │                              │                           │
    │                              │  Invoke agent:            │
    │                              │  extract_health_data(     │
    │                              │    text: transcription,   │
    │                              │    health_profile,        │
    │                              │    source_type: voice     │
    │                              │  )                        │
    │                              │──────────────────────────>│
    │                              │                           │
    │                              │  Agent extracts:          │
    │                              │  - discontinue tamoxifen  │
    │                              │  - add letrozol 2.5mg 1x  │
    │                              │  - journey_event:         │
    │                              │    medication_change      │
    │                              │                           │
    │                              │<──────────────────────────│
    │                              │                           │
    │  Response:                   │                           │
    │  { proposed_updates,         │                           │
    │    confirmation_required }   │                           │
    │<─────────────────────────────│                           │
    │                              │                           │
    │  Show confirmation card:     │                           │
    │  "Klopt dit?"                │                           │
    │  ✓ Tamoxifen gestopt         │                           │
    │  ✓ Letrozol 2.5mg/dag       │                           │
    │  gestart                     │                           │
    │  [Bevestigen] [Aanpassen]    │                           │
    │                              │                           │
    │  Patient taps [Bevestigen]   │                           │
    │                              │                           │
    │  POST /brain/confirm         │                           │
    │  { update_ids: [...] }       │                           │
    │─────────────────────────────>│                           │
    │                              │  Apply updates to         │
    │                              │  health_profile           │
```

**API call**:

```
POST /brain/voice
Content-Type: application/json

{
  "patient_id": "abc-123",
  "transcription": "De dokter heeft vandaag mijn medicijn veranderd. Ik neem nu letrozol in plaats van tamoxifen, 2.5 milligram per dag.",
  "source_date": "2026-04-04"
}
```

**Response**:

```json
{
  "status": "confirmation_required",
  "proposed_updates": {
    "medications": [
      {
        "action": "discontinue",
        "existing_id": "med-222",
        "data": { "name": "tamoxifen", "status": "discontinued" },
        "confidence": 0.90,
        "evidence_quote": "in plaats van tamoxifen"
      },
      {
        "action": "add",
        "data": {
          "name": "letrozol",
          "dose": "2.5mg",
          "frequency": "1x per dag",
          "route": "oral",
          "status": "active"
        },
        "confidence": 0.95,
        "needs_confirmation": false,
        "evidence_quote": "Ik neem nu letrozol... 2.5 milligram per dag"
      }
    ],
    "journey_events": [
      {
        "data": {
          "type": "medication_change",
          "date": "2026-04-04",
          "title": "Overschakeling van tamoxifen naar letrozol",
          "description": "Tamoxifen gestopt, letrozol 2.5mg/dag gestart.",
          "significance": "major"
        },
        "confidence": 0.92
      }
    ]
  },
  "confirmation_card": {
    "title": "Klopt dit?",
    "items": [
      { "label": "Tamoxifen gestopt", "confirmed": false },
      { "label": "Letrozol 2.5mg per dag gestart", "confirmed": false }
    ]
  },
  "missing_data": [
    "Prescriber not specified. Do you want to add which doctor made this change?"
  ]
}
```

**Total tokens**: ~2K in (short transcription + profile), ~500 out. Response time <2s.

---

## 6. Interface Integration

### API Contract

All brain operations go through a REST API with optional SSE streaming.

**Base URL**: `https://api.dittocare.com/v1/brain`

| Endpoint | Method | Purpose | Latency | Mode |
|---|---|---|---|---|
| `/process` | POST | Full pipeline: summarize + extract + suggest | 15-45s | Async (webhook/polling) |
| `/ask` | POST | Answer a question (from suggestion or custom) | 1-3s | Stream (SSE) |
| `/voice` | POST | Process voice input for extraction | 1-3s | Sync |
| `/confirm` | POST | Confirm proposed profile updates | <500ms | Sync (DB write only) |
| `/adapt` | POST | Adapt content for a circle member | 2-5s | Stream (SSE) |
| `/prep` | POST | Generate appointment prep | 3-8s | Sync |
| `/suggestions/{summary_id}` | GET | Get cached suggestions for a summary | <100ms | Sync (cache read) |
| `/profile/{patient_id}` | GET | Get current health profile | <100ms | Sync (DB read) |
| `/profile/{patient_id}/updates` | GET | Get pending profile updates awaiting confirmation | <100ms | Sync |

### Request/Response Headers

```
# Every request
Authorization: Bearer <jwt_token>
X-Patient-ID: <patient_id>
X-Request-ID: <uuid>
Content-Type: application/json

# Stream responses
Accept: text/event-stream
Cache-Control: no-cache

# Async responses
X-Callback-URL: https://app.dittocare.com/hooks/brain-complete
```

### Streaming (for real-time answers)

The `/ask` and `/adapt` endpoints support Server-Sent Events for progressive answer rendering.

```
POST /brain/ask
Accept: text/event-stream

Response stream:

event: token
data: {"text": "Dr. "}

event: token
data: {"text": "de Vries "}

event: token
data: {"text": "heeft "}

...

event: sources
data: {"sources": [{"type": "transcript_quote", "content": "...", "provider": "Dr. de Vries"}]}

event: metadata
data: {"confidence": 0.93, "disclaimer": "Dit is gebaseerd op...", "language": "nl"}

event: done
data: {}
```

### Async Processing (for heavy tasks)

The `/process` endpoint returns immediately with a job ID. Results arrive via webhook or polling.

```
POST /brain/process
→ 202 Accepted
{
  "job_id": "job-abc-123",
  "status": "processing",
  "estimated_seconds": 30,
  "poll_url": "/brain/jobs/job-abc-123"
}

# Webhook callback when done:
POST https://app.dittocare.com/hooks/brain-complete
{
  "job_id": "job-abc-123",
  "status": "completed",
  "result": { ... }
}

# Or poll:
GET /brain/jobs/job-abc-123
→ { "status": "completed", "result": { ... } }
```

### How the Brain Powers Each App Surface

| App Surface | Brain Endpoint(s) | What Happens |
|---|---|---|
| **Summary View** | `/process` (initial), `/suggestions/{id}` | Summary generated. Suggestions cached. Displayed together. |
| **Q&A (suggestion tap)** | `/ask` | Suggestion question sent, answer streamed inline. |
| **Q&A (custom question)** | `/ask` | Free-text question sent with same context. |
| **Health Profile** | `/process` (extraction), `/voice`, `/confirm` | Profile populated automatically. User confirms changes. |
| **Circle View** | `/adapt` | Summary adapted per circle member on first view. Cached. |
| **Appointment Prep** | `/prep` | Full prep generated when patient opens prep screen. |
| **Voice Input** | `/voice` | Transcription processed, extractions returned for confirmation. |
| **Notifications** | `/adapt` (content), app pushes | Brain generates notification text per circle member. App delivers. |

---

## 7. Smart Suggestions Interface Spec

This is the primary user-facing feature for Phase 1. The detailed spec lives in [care-brain-phase1-smart-suggestions.md](care-brain-phase1-smart-suggestions.md). Below is the integration spec for how the brain serves it.

### Suggestion Generation Pipeline

```
Transcript ready
    │
    ▼
/brain/process called
    │
    ├── summarize_conversation() → summary
    │
    ├── extract_health_data() → profile updates
    │
    └── generate_suggestions(summary, profile, transcript)
            │
            ▼
        2-3 suggestions returned
            │
            ▼
        Stored in suggestion cache
        (keyed by summary_id)
            │
            ▼
        Included in /process response
```

**Suggestion generation rules** (embedded in the system prompt):

1. Generate exactly 2-3 questions. Never 1, never more than 3.
2. At least one question must be specific to something the doctor said (not generic).
3. If the patient has previous summaries, include one cross-appointment question (e.g., "How does this compare to what was discussed in January?").
4. Questions must be answerable from the available context. Do not generate a question the brain cannot answer.
5. Questions should feel like what a thoughtful friend would ask on the patient's behalf, not what a medical professional would ask.
6. For circle members: frame questions from their perspective ("What does this mean for daily care?" not "What does this mean for my condition?").

### Display Behavior

| State | What the App Shows |
|---|---|
| Summary loaded, suggestions cached | Suggestion chips visible below summary. Subtle animation on first view. |
| Suggestion tapped | Chip expands. `/ask` called. Answer streams inline below the question. |
| Answer fully loaded | Source attribution visible. Medical disclaimer at bottom. Collapse chevron active. |
| Second suggestion tapped | First answer collapses. New answer streams. |
| "Ask something else" tapped | Text input appears. Same `/ask` endpoint, `suggestion_id` is null. |
| No suggestions available | No chip section shown. "Ask something else" link still available. |

### Grounding Enforcement

Every answer from `/ask` includes a `sources` array. The app renders these as attribution:

```
"Gebaseerd op uw gesprek met Dr. de Vries op 4 april 2026"
```

If the brain returns `confidence < 0.7`, the app prepends a qualifier:

```
"Op basis van de beschikbare informatie (het gesprek bevatte mogelijk niet alle details):"
```

If the brain returns `unanswered_aspects`, the app appends:

```
"Dit werd niet besproken in uw gesprek. U kunt dit vragen bij uw volgende afspraak."
```

### Circle Member Variant

When a circle member views a shared summary:

1. The app calls `GET /suggestions/{summary_id}?viewer=circle&member_id=cc-partner-001`
2. If circle-specific suggestions are cached, return them
3. If not, call `generate_suggestions` with `viewer_type: "circle_member"` and cache the result
4. Circle suggestions are generated separately and stored alongside patient suggestions

Circle suggestion examples vs. patient suggestions:

| Patient Suggestion | Circle Member Suggestion (partner) |
|---|---|
| "Wat betekent 'watchful waiting' voor mijn situatie?" | "Waar moet u in de dagelijkse zorg op letten?" |
| "Hoe verhoudt dit zich tot de scan van januari?" | "Hoe gaat de behandeling vergeleken met vorige keer?" |
| "Wat zijn de bijwerkingen van oxaliplatine?" | "Welke bijwerkingen kunt u verwachten en hoe kunt u helpen?" |

---

## 8. Trade-offs

### Pros

| Advantage | Details |
|---|---|
| **Simplest architecture** | One agent, one prompt, one set of tools. No routing logic, no agent coordination, no inter-agent communication. |
| **Fast to prototype** | A working CLI can be built in days. Full API in 2-3 weeks. |
| **One prompt to tune** | All behavior controlled by a single system prompt. Tuning is centralized. |
| **Full context in every call** | The agent sees the complete health profile + transcript on every request. No information loss between components. |
| **Consistent voice** | One agent means one consistent tone and reasoning style across all surfaces. |
| **Easy to debug** | Every request is a single agent call. Reproduce issues by replaying the same input. |

### Cons

| Disadvantage | Details |
|---|---|
| **Context window pressure** | At ~200K tokens, a patient with 2 years of oncology history (20+ transcripts, 50+ events) may exceed practical context limits. |
| **Monolithic** | Cannot test summarization independent of Q&A. Cannot tune extraction without affecting suggestions. |
| **Single model dependency** | Entire brain quality tied to one model. If Sonnet degrades, everything degrades. |
| **Cost scales linearly** | Every Q&A answer pays for the full profile context, even if only one transcript is relevant. |
| **No specialization** | Dutch medical terminology extraction, audience adaptation, and clinical reasoning all share one prompt. A specialist could do each better. |
| **Latency coupling** | Full processing (summarize + extract + suggest) must happen in one call or be serialized. Cannot parallelize independent operations. |

### When to Choose Direction A

| Situation | Direction A is right |
|---|---|
| Proof of concept | Fastest path to a working brain demo. |
| Validating the brain metaphor | Does "one recording, everyone understands" resonate? Test with real users before investing in architecture. |
| Testing prompt quality | One prompt to perfect. Learnings transfer to any architecture. |
| Team capacity <2 backend engineers | Simple enough for one engineer to build and maintain. |
| <50K active users | Context and cost manageable at this scale. |

### When Direction A Breaks Down

| Situation | Direction A struggles |
|---|---|
| Patient with 3+ years of health history | Context window overflow. Need summarization of older context or a retrieval layer. |
| 500K+ active users | Cost per interaction too high (full profile on every call). |
| Need to swap models per task | Single agent = single model. Cannot route Dutch NLP to one model and reasoning to another. |
| Latency-sensitive parallel operations | Cannot summarize and extract simultaneously in a single agent call. |
| Team wants independent deployability | Monolith means every change risks breaking unrelated capabilities. |

---

## 9. Cost Model

Based on Claude API pricing as of April 2026. Using Claude 3.5 Sonnet for Q&A and Opus for full processing.

**Assumptions**:
- Average transcript: 5,000 tokens
- Average health profile: 2,000 tokens (grows with patient history)
- System prompt: 3,000 tokens
- Previous summaries context: 1,000 tokens
- Sonnet pricing: $3/MTok input, $15/MTok output
- Opus pricing: $15/MTok input, $75/MTok output

### Per-Operation Costs

| Operation | Model | Tokens In | Tokens Out | Cost Per Call |
|---|---|---|---|---|
| Full processing (summarize + extract + suggest) | Opus | ~11,000 | ~4,000 | ~$0.47 |
| Q&A answer (suggestion tap) | Sonnet | ~11,000 | ~500 | ~$0.04 |
| Custom question | Sonnet | ~11,000 | ~500 | ~$0.04 |
| Audience adaptation (per member) | Sonnet | ~5,000 | ~500 | ~$0.02 |
| Voice input extraction | Sonnet | ~3,000 | ~500 | ~$0.02 |
| Appointment prep | Sonnet | ~15,000 | ~1,000 | ~$0.06 |
| Pattern detection | Opus | ~20,000 | ~1,000 | ~$0.38 |

### Monthly Cost by Scale

**Assumptions per active user per month**:
- 1.5 summaries (some users record multiple appointments/month, many record none)
- 3 suggestion taps per summary
- 0.5 custom questions per summary
- 0.3 circle member adaptations per summary
- 0.2 voice updates
- 0.1 appointment preps

| Component | Per User/Mo | 5K Users | 50K Users | 500K Users |
|---|---|---|---|---|
| Full processing | $0.71 | $3,525 | $35,250 | $352,500 |
| Q&A (suggestions) | $0.18 | $900 | $9,000 | $90,000 |
| Custom Q&A | $0.03 | $150 | $1,500 | $15,000 |
| Audience adapt | $0.01 | $45 | $450 | $4,500 |
| Voice input | $0.004 | $20 | $200 | $2,000 |
| Appointment prep | $0.009 | $45 | $450 | $4,500 |
| **Total** | **~$0.94** | **~$4,700** | **~$47,000** | **~$467,000** |

### Cost Observations

1. **Full processing dominates** (~75% of cost). Using Opus here is the driver. Switching to Sonnet for summarization would cut this by 5x, but quality may suffer for complex oncology conversations.
2. **Q&A is cheap**. At $0.04 per answer, this is negligible even at scale. Good news for Smart Suggestions being the Phase 1 feature.
3. **At 500K users, $467K/month is $5.6M/year**. This only works if Ditto has revenue to support it (subscription or B2B2C). At $5-10/user/month subscription, 500K users = $30-60M ARR. AI cost is 10-20% of revenue. Acceptable.
4. **Caching saves significantly**. Suggestion answers cached per summary = same suggestion tapped by multiple circle members costs nothing after first call.
5. **Context bloat is the real risk**. As health profiles grow (2 years of oncology = ~10K tokens of profile), input costs increase for every operation. Direction B/C solve this with retrieval, Direction A does not.

### Optimization Levers

| Lever | Impact | Effort |
|---|---|---|
| Use Sonnet instead of Opus for processing | ~5x cost reduction on processing | Low, but test quality |
| Cache aggressively (suggestions, adaptations) | ~30% reduction | Low |
| Truncate health profile to relevant sections per operation | ~20-40% input reduction | Medium |
| Batch circle member adaptations | ~10% reduction | Low |
| Use prompt caching for system prompt + profile | ~50% reduction on input costs (cached tokens cheaper) | Low (API feature) |

---

## 10. Prototype Scope

What to build first to validate Direction A. Target: working prototype in 2 weeks.

### Deliverables

**1. The system prompt** (Section 2 of this document)
Already written. Test it against 10 real Ditto transcripts before building anything.

**2. Four core tools**

| Tool | Why first |
|---|---|
| `summarize_conversation` | Existing capability. Validate that the brain matches or exceeds current Azure OpenAI quality. |
| `extract_health_data` | Foundation. Populates the health profile from transcripts. Without this, the brain has no memory. |
| `generate_suggestions` | The Phase 1 feature. The thing users will interact with. |
| `answer_question` | Completes the suggestion flow. No point showing suggestions without answers. |

Defer: `adapt_for_audience` (Phase 4), `generate_appointment_prep` (Phase 5), `detect_patterns` (Phase 5), `translate_content` (Phase 4).

**3. CLI prototype**

A command-line tool that takes a transcript file and outputs the full brain result.

```bash
# Process a transcript
ditto-brain process --transcript conversation.txt --profile patient.json

# Output:
# 1. Structured summary (JSON)
# 2. Health profile updates (JSON diff)
# 3. Smart suggestions (3 questions)
# 4. Interactive Q&A mode (type a question, get a grounded answer)
```

Implementation:

```python
# Simplified prototype structure

class CareBrain:
    """Single orchestrator agent for Ditto Care Brain."""

    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.client = anthropic.Anthropic()
        self.model = model
        self.system_prompt = load_system_prompt()
        self.tools = [
            summarize_conversation_tool,
            extract_health_data_tool,
            generate_suggestions_tool,
            answer_question_tool,
        ]

    def process(self, transcript: str, health_profile: dict) -> dict:
        """Full processing pipeline: summarize + extract + suggest."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=8192,
            system=self.system_prompt,
            tools=self.tools,
            messages=[
                {
                    "role": "user",
                    "content": build_process_prompt(transcript, health_profile),
                }
            ],
        )
        return parse_tool_results(response)

    def ask(self, question: str, context: dict, stream: bool = True):
        """Answer a question with optional streaming."""
        if stream:
            with self.client.messages.stream(
                model=self.model,
                max_tokens=2048,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": build_ask_prompt(question, context),
                    }
                ],
            ) as stream:
                for text in stream.text_stream:
                    yield text
        else:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": build_ask_prompt(question, context),
                    }
                ],
            )
            return response.content[0].text


def build_process_prompt(transcript: str, profile: dict) -> str:
    return f"""Process this medical conversation. Execute these steps in order:

1. Call summarize_conversation with the transcript and health profile
2. Call extract_health_data to identify any profile updates
3. Call generate_suggestions based on the summary

Health Profile:
{json.dumps(profile, indent=2)}

Transcript:
{transcript}"""


def build_ask_prompt(question: str, context: dict) -> str:
    return f"""Answer the following question. Use ONLY the provided context.

Question: {question}

Summary: {json.dumps(context['summary'], indent=2)}
Transcript: {context.get('transcript', 'Not available')}
Health Profile: {json.dumps(context['health_profile'], indent=2)}

Remember: ground every statement in the data. Cite the doctor by name. Include the medical disclaimer."""
```

**4. Test with 10 real Ditto conversations**

| Test | What we're evaluating |
|---|---|
| 5 oncology conversations (Dutch) | Summary quality, medication extraction accuracy, suggestion relevance |
| 3 cardiology conversations (Dutch) | Generalization beyond oncology |
| 1 mixed-language conversation | Dutch medical terms + patient speaking Turkish/English |
| 1 short/simple conversation | Behavior when there's little to extract |

**Evaluation criteria**:

| Criterion | Threshold | How to measure |
|---|---|---|
| Summary quality | >= current Azure pipeline | Blind comparison by Merlijn + team member |
| Extraction accuracy | >= 90% precision on medications | Manual review against transcript |
| Extraction recall | >= 80% (catch most, miss few) | Manual review against transcript |
| Suggestion relevance | >= 80% "I'd want to know this" | Merlijn rates each suggestion 1-5 |
| Answer grounding | 0 hallucinations in 30 answers | Manual review: every claim traceable to transcript |
| Dutch quality | Natural, no Anglicisms, correct formality | Native speaker review |
| Latency (full process) | < 45 seconds | Timed |
| Latency (Q&A answer) | < 3 seconds to first token | Timed |

### Prototype Timeline

| Week | Deliverable |
|---|---|
| Week 1, Days 1-2 | System prompt finalized. CLI skeleton. `summarize_conversation` and `extract_health_data` tools implemented. |
| Week 1, Days 3-5 | `generate_suggestions` and `answer_question` tools. Health Profile schema validated. End-to-end flow working on 1 test transcript. |
| Week 2, Days 1-3 | Test on all 10 conversations. Evaluate results. Tune prompt. |
| Week 2, Days 4-5 | Document findings. Decision: proceed with Direction A, or pivot to B/C? |

### Success Criteria for Prototype

The prototype validates Direction A if:

1. Summary quality matches or exceeds current pipeline on 8/10 test conversations
2. Health profile extraction catches all medication changes with >= 90% accuracy
3. Smart suggestions are relevant and specific (not generic) on 8/10 conversations
4. Zero hallucinated medical facts across all Q&A answers
5. Full processing completes in < 45 seconds consistently
6. Q&A answers stream with < 3 second first-token latency
7. The system prompt is stable (not requiring per-conversation tweaks)

If these criteria are met, Direction A is viable for Phase 1 (Smart Suggestions). The decision to stay on Direction A vs. evolve to B/C happens after Phase 1 ships and we observe real usage patterns and context growth.
