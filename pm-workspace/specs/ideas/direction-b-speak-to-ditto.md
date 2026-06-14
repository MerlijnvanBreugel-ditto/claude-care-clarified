# Direction B: "Speak to Ditto" — Feature Considerations

**Parent**: [Onboarding to Aha](onboarding-to-aha.md) (BIGB-335)
**Date**: 2026-02-26
**Goal**: Define what it takes to make this a killer feature, not just a demo trick.

---

## The Big Idea

User speaks freely → Ditto extracts structured health facts → those facts populate a living health profile → the profile unlocks personalized content and connections across the app.

This is not a one-time onboarding gimmick. It's Ditto's intelligence layer — the mechanism through which the app learns who you are and becomes useful *before* you ever see a doctor.

---

## 1. Comparable Solutions (Cross-Domain)

The "speak freely → structured extraction → content unlocks" pattern exists across multiple domains. Here's what works, what doesn't, and what Ditto can steal.

| Product | Domain | What They Do | The Magic Moment | What Ditto Can Learn |
|---|---|---|---|---|
| **Fantastical** | Calendar | Type "Lunch with Sarah Tuesday at noon at Cafe Central" → all fields auto-populate in real-time as you type | Watching fields fill *as you speak/type* — instant proof the AI understands you | **Real-time visual feedback during extraction is critical.** Users need to SEE facts appearing as they talk. |
| **Noom** | Health/Wellness | 15-min onboarding questionnaire → produces a personalized weight loss plan. Every answer visibly changes the plan. | "This plan is for ME" — because every input visibly shaped the output | **Show causality.** Don't just extract — show the user HOW their words shaped their profile. |
| **Flo** | Women's Health | Structured onboarding questions → unlocks cycle predictions, symptom tracking, personalized content feed. Drove 20% conversion lift to subscription. | The first prediction that's eerily accurate because it used YOUR data | **Extraction must unlock something immediately useful** — not just store data for later. |
| **Ada Health** | Health | Conversational symptom checker: dynamic questions adapt based on your answers → produces assessment with possible conditions | Questions adapt in real-time based on what you say — feels like talking to someone who listens | **Adaptive follow-ups** after initial extraction make the user feel heard, not processed. |
| **Hinge** | Dating | Prompts + answers create a profile that's more personality than form-filling. The profile IS the product. | Your profile feels like YOU, not a bureaucratic form | **The output should feel personal and human**, not clinical or database-like. |
| **Retell AI / Logistics voice agents** | Logistics | Caller says "Pick up 10 crates from 2450 Industrial Parkway on Friday at 9 AM" → backend form fills automatically | Zero-effort data entry — just talk naturally | **The extraction must handle natural speech**, not require users to speak in structured ways. |
| **Woebot** (pre-shutdown) | Mental Health | Conversational CBT intake → builds psychological profile → personalizes therapy content | Content adapts to YOUR situation from session one | **Cautionary tale**: shut down consumer product. Value extraction alone isn't enough — the downstream experience must be compelling. |
| **HealthifyMe Ria Voice** | Health coaching | Voice-first health coaching in 50+ languages, builds nutritional/fitness profile from conversations | Speak in your language, get a plan | **Voice-first is especially powerful for elderly users** (Ditto's primary segment). Removes literacy/tech barriers. |

### Pattern Synthesis

The winning formula across all of these:

1. **Input feels effortless** — speak naturally, no forms, no structure required
2. **Extraction is visible** — users SEE the system understanding them in real-time
3. **Output is immediately useful** — not "we'll use this later" but "look what we made for you NOW"
4. **Downstream content changes** — the profile isn't a dead artifact, it actively reshapes the experience

---

## 2. Reliability of Extraction

This is your #1 concern, and rightly so. The entire feature's credibility lives or dies on extraction quality.

### What We're Extracting

| Entity Type | Example from Speech | Extraction Difficulty | Confidence Needed |
|---|---|---|---|
| **Conditions / Diagnoses** | "I have type 2 diabetes and high blood pressure" | Low — well-defined medical terms | High (wrong = trust-breaking) |
| **Medications** | "I take metformin twice a day and something for my blood pressure, I think lisinopril" | Medium — brand/generic names, dosage, uncertainty | High for names, medium for dosage |
| **Allergies** | "I'm allergic to penicillin" | Low | Very high (safety-critical) |
| **Care journeys** | "I've been seeing a cardiologist at Erasmus MC for about two years" | Medium — requires understanding of specialty + institution + duration | Medium |
| **Current symptoms** | "My knees have been hurting a lot lately, especially in the morning" | Medium — subjective, vague language | Medium (it's self-reported anyway) |
| **Hospitals / Providers** | "I go to Erasmus MC and my GP is Dr. van den Berg" | Medium — Dutch names, abbreviations | Medium |
| **Past appointments** | "I had surgery last March" | Medium — relative dates, vague references | Low-medium |
| **Upcoming appointments** | "I have an appointment with my oncologist next Thursday" | Low-medium — relative dates | Medium |

### Research on Extraction Quality

Academic studies on NLP extraction from patient-generated health data show:
- **Medication name recognition**: Precision ~0.8, highest-performing entity type
- **Symptom extraction**: Precision ~0.7, more variable due to informal language
- **Modern LLMs (GPT-4/Claude-level)**: Dramatically outperform older NER models on freeform text, especially with Dutch/multilingual input

### Reliability Strategy: Confirm, Don't Assume

**The Fantastical principle**: Don't silently extract and store. Show what you extracted and let the user confirm.

```
User speaks for 90 seconds about their health situation.

Ditto shows:
┌─────────────────────────────────────┐
│  Here's what I understood:          │
│                                     │
│  Conditions                         │
│  ✓ Type 2 diabetes                  │
│  ✓ High blood pressure              │
│                                     │
│  Medications                        │
│  ✓ Metformin (twice daily)          │
│  ✓ Lisinopril                       │
│                                     │
│  Allergies                          │
│  ✓ Penicillin                       │
│                                     │
│  Your care team                     │
│  ✓ Cardiologist — Erasmus MC        │
│  ✓ GP — Dr. van den Berg            │
│                                     │
│  [ Looks good ✓ ]  [ Let me fix → ] │
└─────────────────────────────────────┘
```

**Why this works:**
- Incorrect extraction is caught immediately (trust preserved)
- Correct extraction feels magical ("It understood me!")
- The confirmation step itself IS the aha moment — seeing your health laid out clearly
- Editable corrections improve the model's output over time

### Must-Have Reliability Rules

1. **Never infer what wasn't said.** If the user doesn't mention allergies, the allergy field stays empty — don't guess.
2. **Flag uncertainty.** "Lisinopril (did you mean lisinopril?)" with a tap to confirm. Hedging is better than wrong confidence.
3. **Dutch medical terminology.** The AI must handle Dutch drug names, hospital names, and casual Dutch health language (e.g., "suikerziekte" = diabetes, "bloeddrukverlager" = blood pressure medication).
4. **Graceful degradation.** If speech is too short or vague, don't produce a garbage profile. Say: "Tell me a bit more about your medications or conditions so I can help you better."
5. **No extraction is better than wrong extraction.** The threshold for adding something to the profile should be high. Missed entities can be added later; wrong entities break trust.

---

## 3. The Downstream Magic: Profile → Content → Value

This is where the feature goes from "cool demo" to "I can't live without this." The extracted profile must DO something immediately.

### Content Mapping Architecture

```
Speech → Extraction → Profile Fields → Content Triggers
                                          ↓
                              ┌──────────────────────┐
                              │ Personalized content  │
                              │ Relevant tips         │
                              │ Appointment prep      │
                              │ Care Circle prompts   │
                              │ Medication reminders  │
                              │ Condition explainers  │
                              └──────────────────────┘
```

### What Each Profile Field Unlocks

| Profile Field | Immediate Content Unlock | Why It Feels Worth It |
|---|---|---|
| **Conditions** | Condition-specific card: "Living with Type 2 Diabetes — 3 questions to ask your endocrinologist" | Instantly relevant. Not generic health tips — YOUR health tips. |
| **Medications** | Medication overview with plain-language explanations: "Metformin helps control blood sugar levels. Common side effects: [list]" | Ditto explains your meds better than the pharmacy pamphlet. |
| **Allergies** | Safety badge on profile: "Ditto knows your allergies and will flag them in future summaries" | Peace of mind. The app is watching out for you. |
| **Care journeys** | Timeline view: "Your care journey with Erasmus MC Cardiology — 2 years" + "What to expect at your next cardiology visit" | Makes the invisible visible. Shows Ditto understands your life, not just your data. |
| **Hospitals / Providers** | Provider cards with practical info: department, how to reach them, typical visit structure | Immediately useful, especially for elderly users managing multiple specialists. |
| **Current symptoms** | "You mentioned knee pain. Here's what your GP might want to know about it" + suggested questions for next visit | Bridges to the core use case: preparing for the conversation Ditto will record. |
| **Upcoming appointments** | Appointment card with countdown + "3 things to prepare" + reminder to bring Ditto | This is the bridge to the real aha. The profile primes the real use. |

### The Cascade Effect

The magic isn't any single unlock — it's the cascade:

1. **Speak** → "I have diabetes, I take metformin, I see Dr. van den Berg, and I have a cardiologist appointment next week"
2. **Extract** → 4 profile fields populated
3. **Immediate unlock** → Diabetes explainer card + metformin overview + provider card for Dr. van den Berg + appointment prep for cardiology visit
4. **User reaction** → "Wait, it actually understood all of that? And it's already showing me useful stuff?"
5. **Bridge to real use** → "Imagine what Ditto does when it records your actual cardiologist appointment next week"
6. **Care Circle trigger** → "Share your health profile with family so they know what's going on"

This turns a 90-second monologue into 4+ pieces of personalized content, a reason to return next week, and a prompt to invite family. That's the killer.

---

## 4. Must-Have Specifications

### Core Experience

| Spec | Requirement | Rationale |
|---|---|---|
| **Input mode** | Voice-first, with text fallback | Primary users are elderly — voice is lowest friction. But some users will be in public or prefer typing. |
| **Language** | Dutch primary, English secondary | 95%+ of user base is Dutch. Must handle code-switching (Dutch with English medical terms). |
| **Minimum input** | 30 seconds of speech produces a useful profile | Below this, the extraction is too thin to feel magical. |
| **Maximum input** | No hard cap, but prompt after 3 minutes: "I have a good picture — shall I show you what I found?" | Prevents rambling without cutting people off. |
| **Processing time** | < 10 seconds from end of speech to showing extracted profile | The wait is the tension — too long and it feels broken. Show a progress animation ("Ditto is thinking..."). |
| **Confirmation UX** | Extracted facts shown as editable cards — tap to confirm, tap to edit, swipe to remove | User must feel in control. This is THEIR data. |
| **Accuracy target** | >90% precision on conditions/medications, >80% on other entities | Precision over recall. Missing something is fine; getting it wrong is not. |

### Profile as Living Document

| Spec | Requirement | Rationale |
|---|---|---|
| **Continuous enrichment** | Every real summary adds to the profile (new meds mentioned, new conditions, new providers) | The profile gets smarter over time without the user doing anything. |
| **Speak again anytime** | "Tell Ditto more" — always available from profile screen | Not locked to onboarding. Life changes, health changes. |
| **Conflict resolution** | If a new summary contradicts the profile (e.g., medication discontinued), flag it: "It sounds like you stopped taking metformin — should I update your profile?" | The profile must stay accurate, and the user must stay in control. |
| **Correlation engine** | Surface connections: "You mentioned knee pain started around the time you began taking [medication] — this could be related" | This is the "connecting the dots" intelligence. Requires multiple data points over time. |
| **Share via Care Circle** | Health profile is shareable — family members see conditions, medications, providers | Immediate viral loop: "Mom shared her health profile with me on Ditto." |

### Onboarding Integration

| Spec | Requirement | Rationale |
|---|---|---|
| **Placement** | After the value explanation, before the home screen. Not the very first screen. | User needs to understand WHAT Ditto is before being asked to speak. But it must come before they hit an empty home screen. |
| **Skippable** | Yes — but with a compelling reason not to: "Set up your profile now and Ditto will be ready for your next appointment" | Don't force. But make skipping feel like missing out. |
| **Re-entry** | If skipped, prompt on second open: "Ready to set up your health profile?" | Don't nag, but don't forget. |
| **Completion reward** | After profile is populated, show a "Your Ditto is ready" screen with all unlocked content visible | The reward must be visible and immediate. |

---

## 5. Open Questions (For You)

Before this can move to functional scoping, I need clarity on a few things:

| # | Question | Why It Matters |
|---|---|---|
| 1 | **Does the current AI pipeline support entity extraction from freeform monologue, or do we need a separate extraction step?** | Determines build complexity. If we need a new extraction pipeline, this is M-L effort, not S-M. |
| 2 | **What content exists today that we could map to profile fields?** Do we have condition explainers, medication info, or provider directories — or does ALL content need to be generated? | If content must be AI-generated on-the-fly (likely), that's a different architecture than mapping to a content library. |
| 3 | **How does this relate to the Voice Health Check-in (idea-004)?** That spec already explored a similar direction. Should this subsume it, or are they complementary? | Risk of duplicate effort. The voice health check-in has mockups and panel reviews already done. |
| 4 | **Privacy/storage model for the health profile.** Where does extracted health data live? On-device only? Server-side? How does this interact with GDPR consent flows? | Health profile is more sensitive than a summary (it's persistent, editable, shareable). Needs explicit consent design. |
| 5 | **Correlation engine scope.** You mentioned "find correlations and connect the dots." Is this a v1 must-have or a v2 feature? | Correlation requires multiple data points over time. In onboarding, you only have the initial monologue. Real correlations come after 2-3 real summaries. |
| 6 | **Content generation approach.** Should unlocked content be pre-authored (curated library) or AI-generated per user? | Pre-authored = more reliable, less scalable. AI-generated = more personal, needs quality guardrails. My instinct: AI-generated with medical review templates. |

---

## 6. Risk Assessment

| Risk | Severity | Mitigation |
|---|---|---|
| **Wrong extraction breaks trust** | High | Confirmation UX (never silently add to profile). Precision > recall. |
| **User speaks too little** | Medium | Guided prompts: "Tell me about any medications you take" as fallback if initial speech is thin. |
| **Sets wrong expectation** ("Ditto is a chatbot") | Medium | Clear framing: "Ditto listens and organizes" — not a conversation partner (yet). Direction C is the future. |
| **Content feels generic despite profile** | High | Content must reference the user's specific conditions/meds by name. "Your diabetes" not "About diabetes." |
| **Dutch NLP quality** | Medium | Test with 50+ Dutch health monologues before building UI. If extraction quality < 80%, this approach doesn't work. |
| **Elderly users uncomfortable with voice recording** | Medium | Explicit consent + "This stays on your phone / is only shared with people you choose." Text fallback. |
| **Profile becomes stale** | Low (long-term) | Continuous enrichment from real summaries + periodic "Has anything changed?" prompts. |

---

## 7. Success Criteria

If we build this, here's how we know it worked:

| Metric | Target | Measurement |
|---|---|---|
| **Profile completion rate** (users who speak + confirm) | >40% of new installs | Analytics: onboarding funnel |
| **Extraction accuracy** (user-confirmed vs. auto-extracted) | >90% precision | Compare extracted entities to user-confirmed profile |
| **Content engagement** (users who tap on at least one unlocked content piece) | >60% of users who complete profile | Analytics: content card taps |
| **Time to first content interaction** | <5 minutes from install | Analytics: first content tap timestamp |
| **7-day retention lift** (profile users vs. non-profile users) | +30% relative | Cohort comparison |
| **Care Circle share rate** (users who share profile) | >15% of profile completers | Analytics: share events |
| **NPS/qualitative** | "Ditto understood me" sentiment in feedback | User interviews / in-app survey |

---

*This doc is a thinking tool, not a spec. If the answers to the open questions hold up, this moves to functional scoping via the standard workflow.*
