# Onboarding: Persona + Intent Mapping

> Status: Draft v3 — 2026-03-24
> Related: DPMA-2190, BIGB-330
> Validated against: prior intent survey (n=64, see below)

## Flow

**Screen 1: Persona** — "What describes your situation?" (max 2)
**Screen 2: Intent** — "What would help you most?" (multi-select, no limit)

Screen 2 shows the **union** of all intents mapped to the selected persona(s), deduplicated. If someone picks two personas, they see everything that maps to either.

Tags `[core]` `[near]` `[explore]` are internal only — never shown to users.

---

## Personas (Screen 1)

| ID | Label | Hint |
|---|---|---|
| `expecting` | We're expecting a baby or are new parents | |
| `own_diagnosis` | I've been diagnosed with something serious | Cancer, heart condition, or another illness |
| `loved_one` | Someone I love has a serious diagnosis | |
| `caregiver` | I look after someone who needs more help day to day | A parent, partner, or someone close to me |
| `hcp` | I'm a healthcare professional | Doctor, nurse, midwife, or similar |
| `skip` | I'd rather not say | |

---

## Intents (Screen 2)

### Consumer intents

| # | ID | Label | Type | Personas | Survey ref |
|---|---|---|---|---|---|
| 1 | `appointment_summaries` | Have a clear summary of my medical conversations | core | expecting, own_diagnosis, loved_one, caregiver | 76.5% |
| 2 | `share_with_family` | Share updates with my partner or family | core | expecting, own_diagnosis, loved_one, caregiver | 42.1% |
| 3 | `track_documents` | Keep track of lab results and medical documents | core | own_diagnosis, loved_one, caregiver | 39% |
| 4 | `track_symptoms` | Track symptoms or side effects over time | near | own_diagnosis, loved_one, caregiver | 53.1% |
| 5 | `prep_questions` | Prepare questions before appointments | near | expecting, loved_one, caregiver | — |
| 6 | `health_fitness_data` | Track health and fitness data like sleep, steps, or weight | explore | expecting, own_diagnosis, loved_one, caregiver | 23.4% + 21.8% |
| 7 | `explain_medical_letters` | Get an explanation of complex medical letters | explore | own_diagnosis, loved_one | — |
| 8 | `medical_overview` | Have one clear overview of my medical history | explore | own_diagnosis, loved_one, caregiver | — |
| 9 | `coordinate_care` | Coordinate care between multiple people | explore | loved_one, caregiver | — |
| 10 | `understand_condition` | Understand a medical condition better | explore | own_diagnosis, loved_one | — |
| 11 | `medication_reminders` | Get reminders for medication or check-ups | explore | caregiver | — |
| 12 | `child_milestones` | Track pregnancy or child health milestones | explore | expecting | — |
| 13 | `vaccination_reminders` | Get reminders for vaccinations or screenings | explore | expecting | — |

### HCP intents

HCPs are not the core user base. These intents are designed to understand how they actually use Ditto without overpromising.

| # | ID | Label | Type | Personas |
|---|---|---|---|---|
| 14 | `hcp_patient_summaries` | Give patients a clear summary of our conversation | core | hcp |
| 15 | `hcp_family_sharing` | Help patients share updates with their family | core | hcp |
| 16 | `hcp_translate_documents` | Help patients understand complex medical letters | explore | hcp |
| 17 | `hcp_validate_quality` | Check the quality of Ditto's summaries | explore | hcp |
| 18 | `hcp_reduce_documentation` | Reduce time I spend on documentation | explore | hcp |
| 19 | `hcp_recommend` | Recommend Ditto to my patients | explore | hcp |

Type key: `core` = Ditto does this today, `near` = on roadmap or partially exists, `explore` = doesn't exist yet (roadmap signal)

---

## Prior survey validation (n=64)

| Survey option (Dutch) | % | Mapped to | Notes |
|---|---|---|---|
| Voorbereiding op medische gesprekken | 76.5% | `appointment_summaries` | #1 demand signal — confirmed core |
| Symptomen bijhouden | 53.1% | `track_symptoms` | Strong demand, currently near-term |
| Medische updates delen met naasten | 42.1% | `share_with_family` | Care Circle signal |
| Labresultaten bijhouden | 39% | `track_documents` | Label updated to include lab results explicitly |
| Gezondheidsdata bijhouden (slaap, stappen) | 23.4% | `health_fitness_data` | Combined with fitness below |
| Beweging / fitness bijhouden | 21.8% | `health_fitness_data` | Combined — 23.4% + 21.8% likely overlap, ~30-35% unique |

---

## What each persona sees on Screen 2

| Persona | Intents shown (by #) | Count |
|---|---|---|
| `expecting` | 1, 2, 5, 6, 12, 13 | 6 |
| `own_diagnosis` | 1, 2, 3, 4, 6, 7, 8, 10 | 8 |
| `loved_one` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 10 |
| `caregiver` | 1, 2, 3, 4, 5, 6, 8, 9, 11 | 9 |
| `hcp` | 14, 15, 16, 17, 18, 19 | 6 |
| `skip` | → straight to "Get started" | 0 |

### Multi-select combinations (examples)

| Combo | Intents shown | Count |
|---|---|---|
| `own_diagnosis` + `caregiver` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | 11 |
| `expecting` + `loved_one` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13 | 12 |
| `own_diagnosis` + `loved_one` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 10 |
| `expecting` + `caregiver` | 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13 | 11 |
| `own_diagnosis` + `hcp` | 1, 2, 3, 4, 6, 7, 8, 10, 14, 15, 16, 17, 18, 19 | 14 |

Note: HCP combined with any consumer persona creates a long list. Consider making HCP exclusive.

---

## Per-persona copy variants

Generic labels work across personas. When only one persona is selected, the app can adapt wording:

| Intent ID | Generic | Expecting | Own diagnosis | Loved one / Caregiver |
|---|---|---|---|---|
| `appointment_summaries` | Have a clear summary of my medical conversations | Have a summary of my conversation with the midwife or doctor | Have a clear summary of my hospital appointments | Keep track of what happens at their appointments |
| `share_with_family` | Share updates with my partner or family | Share updates with my partner or family | Keep my family in the loop about my care | Share updates with siblings or other family |
| `health_fitness_data` | Track health and fitness data like sleep, steps, or weight | Track health data like sleep, weight, or steps | Track general health like sleep and activity | Track their health data like sleep and activity |

When two personas are selected → use generic wording.

---

## Inferred signals (for Customer.io / Mixpanel)

Derived automatically from selections, not asked directly:

| Signal | Derived when |
|---|---|
| `care_circle_warm_lead` | share_with_family OR coordinate_care OR hcp_family_sharing selected |
| `appointment_recorder_primary` | appointment_summaries OR hcp_patient_summaries selected |
| `wants_reminders` | medication_reminders OR vaccination_reminders selected |
| `wants_appointment_prep` | prep_questions selected |
| `wants_health_timeline` | medical_overview OR track_documents selected |
| `wants_letter_explanation` | explain_medical_letters OR hcp_translate_documents selected |
| `wants_health_fitness_tracking` | health_fitness_data selected |
| `solo_user_likely` | share_with_family AND coordinate_care both NOT selected |

---

## Data model

**Mixpanel event:** `onboarding_profile_completed`
```json
{
  "personas": ["own_diagnosis", "caregiver"],
  "intents": ["appointment_summaries", "share_with_family", "medical_overview"],
  "intents_shown": ["appointment_summaries", "share_with_family", "track_documents", "track_symptoms", "prep_questions", "health_fitness_data", "explain_medical_letters", "medical_overview", "coordinate_care", "understand_condition", "medication_reminders"],
  "intent_count": 3,
  "persona_count": 2
}
```

**User properties** (set once, updatable from profile):
```json
{
  "onboarding_personas": ["own_diagnosis", "caregiver"],
  "onboarding_intents": ["appointment_summaries", "share_with_family", "medical_overview"],
  "care_circle_warm_lead": true,
  "appointment_recorder_primary": true,
  "wants_health_timeline": true,
  "solo_user_likely": false
}
```

---

## Open questions

1. **Should HCP be exclusive?** If someone picks HCP, block the second persona slot? Combined list reaches 14 intents.
2. **Shuffle order?** DPMA-2190 says yes for intent options. Persona order probably fixed (most common first).
3. **"Other" free text?** DPMA-2190 had it. Worth adding for intent? Adds friction but captures surprises.
