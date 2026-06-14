# ZeroClaw — Claude-Powered Health Assistant JTBD Discovery

**Date**: 2026-03-29
**Status**: Discovery / ideation
**Context**: What if Ditto runs on Claude, applies ZeroClaw/NanoClaw agent principles (persistent memory, scheduled tasks, agent specialization, tool use), and becomes a full personal health assistant?

---

## Principles Borrowed from ZeroClaw/NanoClaw

These aren't about WhatsApp delivery — they're architectural principles that change what Ditto can do inside the app.

| Principle | What it means for Ditto |
|---|---|
| **Persistent memory** | Claude holds your full care journey in context (1M tokens). Every interaction gets smarter. Not "start from scratch" like a chatbot — remembers your meds, your doctors, your worries. |
| **Scheduled proactive tasks** | Ditto doesn't wait for you to open the app. Sends medication reminders, appointment prep, check-in nudges. Claude decides WHAT and WHEN; app infrastructure delivers. |
| **Agent specialization** | Different capabilities for different jobs — medication agent, appointment prep agent, sharing agent — each tuned to its domain but sharing your health context. |
| **Tool use** | Claude can call external services: drug databases for interaction checking, translation APIs, calendar integrations, terminology databases for Dutch medical terms. |
| **Conversational intelligence** | Natural language in, structured value out. Voice or text input → Claude extracts, structures, explains, acts. No forms, no dropdowns, no "select your symptom from a list of 200." |

---

## The 37 Jobs To Be Done

Organized by capability cluster. Each job assessed against Claude's capabilities.

### Claude Fit Legend

| Symbol | Meaning |
|---|---|
| ✅ | Claude does this natively — API call + context is enough |
| 🔧 | Claude is the brain, but needs app infrastructure (STT, push notifications, storage, external APIs) |
| ⚠️ | Claude can assist but should NOT be sole source — needs verified external data or human oversight |
| 🚫 | Hard limit — Claude should not do this (regulatory, safety, or technical impossibility) |

---

### Cluster 1: Understanding & Explaining

The core of what makes healthcare overwhelming is that nobody explains things in your language. Claude is exceptional at this.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 1 | **Summarize my doctor conversation in plain language** | ✅ | Already doing this. Claude's summarization is best-in-class. 1M context means it can reference previous appointments while summarizing. |
| 2 | **Explain medical terms in the context of MY condition** | ✅ | Not "what is metastasis" generically — "what metastasis means for YOUR stage 3b colon cancer." Requires journey context. Claude + persistent memory = personalized medical dictionary. |
| 3 | **Explain my lab results — what changed, what it means for me** | ✅ | Compare against previous results if available. "Your HbA1c went from 7.2 to 6.8 — that means your diabetes management is improving." |
| 4 | **Explain medical letters and documents in plain language** | ✅ | Already doing this. Extend with contextual awareness: "This letter refers to the scan they discussed in your October appointment." |
| 5 | **Explain what to expect from an upcoming procedure** | ✅ | "You're having a colonoscopy next week. Here's what typically happens, what to prepare, and what questions patients in your situation often ask." |
| 6 | **Simplify my medication leaflet into what I actually need to know** | ✅ | Strip the legal boilerplate. "Take with food. Common side effect: nausea first 2 weeks. Call your doctor if you see blood in stool." |
| 7 | **Explain my diagnosis to my child in age-appropriate language** | ✅ | Claude excels at audience adaptation. "Mama has something in her tummy that the doctors are helping to fix. She might feel tired sometimes." |

**Cluster verdict**: Claude's strongest territory. Personalized explanation is where 1M context + care journey history creates a fundamentally different experience than generic chatbot answers.

---

### Cluster 2: Conversing & Answering

The follow-up questions people are too afraid, too confused, or too late to ask.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 8 | **Answer follow-up questions about what the doctor said** | ✅ | Most-requested user feature. "What did she mean by 'we'll monitor the markers'?" — answered from the actual conversation context, not general knowledge. This is care-graph-native Q&A. |
| 9 | **Let me ask "dumb questions" I'm too embarrassed to ask the doctor** | ✅ | "Is it normal to feel this tired?" "Can I still drink wine?" Safe space, no judgment. Claude's tone is a strength here. |
| 10 | **Help me process emotionally difficult health news** | ✅ | Not therapy. Not medical advice. Just: "That's a lot to take in. Many people feel overwhelmed when they first hear this. Would it help to go through what the doctor said step by step?" |
| 11 | **Answer my care circle member's questions about my condition** | ✅ | Partner asks: "What does stage 3b actually mean?" Answered from the patient's journey context, with the patient's sharing permissions. Drives Care Circle value. |
| 12 | **Have a conversation about a health concern before seeing a doctor** | ⚠️ | Helpful for organizing thoughts, NOT for triage. Hard guardrail: "I can help you think through your questions, but I'm not a doctor. If you're worried, please contact your GP." Regulatory risk if positioned as pre-diagnosis. |

**Cluster verdict**: Strong Claude fit for jobs 8-11. Job 12 needs careful positioning — useful but legally sensitive.

---

### Cluster 3: Extracting & Structuring

Turning chaos (voice, photos, documents, conversations) into structured, usable health data.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 13 | **Extract health facts from my freeform voice narrative** | 🔧 | "I've been taking lisinopril for two years, I have diabetes, and my oncologist at Erasmus MC said..." → structured profile cards. Needs STT layer (Whisper/Deepgram) before Claude processes. Claude's extraction is strong. |
| 14 | **Extract medication names, dosages, and schedules from a conversation** | ✅ | "She said to switch from 10mg to 20mg of atorvastatin, take it in the evening." → structured medication record. High accuracy needed — validate against drug database. |
| 15 | **Extract action items and follow-ups from a doctor conversation** | ✅ | "Blood test in 3 weeks." "Schedule MRI before next appointment." "Increase walking to 30 min/day." → actionable task list with dates. |
| 16 | **Extract health data from a photo of my medication box** | 🔧 | Claude vision can read packaging, but Dutch medication packaging varies widely. Needs validation step: "I see Metformine 500mg — is that correct?" |
| 17 | **Build and maintain a living health profile from all my inputs** | 🔧 | THE foundational job. Every conversation, document, voice note enriches the profile. Claude does the extraction + conflict resolution ("You were on lisinopril but this new summary says enalapril — did your medication change?"). App stores the profile. |
| 18 | **Auto-organize health events into care journeys** | 🔧 | "This appointment is related to your colon cancer journey, not your diabetes follow-up." Claude classifies; app maintains the timeline structure. |
| 19 | **Extract key information from EHR screenshots or portal messages** | 🔧 | Photo of hospital portal screen → OCR → Claude extracts and explains. Needs vision/OCR pipeline. |

**Cluster verdict**: Claude is the intelligence layer, but every job needs app infrastructure for storage, STT, or vision. The living health profile (#17) is the single most important enabler — almost everything else improves when it exists.

---

### Cluster 4: Preparing & Planning

The night before the appointment, staring at the ceiling, trying to remember what you wanted to ask.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 20 | **Generate personalized questions for my next appointment** | ✅ | Based on: what happened last time, current symptoms/concerns, medication changes, what was left unresolved. Claude with full journey context produces questions a generic tool never could. |
| 21 | **Create an appointment prep summary** | ✅ | "Since your last visit on Feb 12: medication changed to X, you reported increased fatigue, lab results showed Y. Open questions: Z." One page, doctor-ready. |
| 22 | **Prepare a doctor-ready health overview I can show on my phone** | 🔧 | Needs formatted output the patient can literally hand their phone to the doctor. Claude generates content; app renders the view. |
| 23 | **Help me rehearse a difficult conversation with my doctor** | ✅ | "I want to ask about stopping treatment. How do I bring this up?" Claude can roleplay the conversation, suggest framing, anticipate doctor responses. |
| 24 | **Tell me what to bring and prepare for a specific procedure** | ✅ | "For your colonoscopy: stop blood thinners 5 days before (check with your doctor), clear liquid diet the day before, bring comfortable clothes, someone to drive you home." General + personalized. |

**Cluster verdict**: High-value, high Claude fit. Appointment prep is where persistent memory shines — Claude knows your full journey, not just "you have a doctor appointment tomorrow."

---

### Cluster 5: Monitoring & Alerting

The proactive layer. Ditto doesn't wait for you to ask — it notices things and acts.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 25 | **Flag when my medication changed between appointments** | 🔧 | Claude detects the change in a new summary: "Your oncologist switched you from capecitabine to oxaliplatin. This is different from what your GP had on file." App stores medication state; Claude compares. |
| 26 | **Flag potential medication interactions** | ⚠️ | Claude has general knowledge but MUST cross-reference with a verified drug interaction database (e.g., KNMP G-Standaard for NL). Claude interprets the result for the patient; database provides the safety data. Never Claude alone. |
| 27 | **Remind me to take my medication** | 🔧 | Claude determines schedule from extracted data. App handles the actual push notification delivery. Claude can personalize the reminder: "Time for your evening metformin. Remember, take it with food." |
| 28 | **Detect patterns in my symptoms over time** | 🔧 | "You've reported nausea on 4 of the last 5 Tuesdays — all the day after chemo. Worth mentioning to your oncologist." Needs accumulated symptom data (from voice check-ins or manual input). Claude analyzes the pattern. |
| 29 | **Proactively check in on how I'm feeling** | 🔧 | Scheduled: "Hi, how are you doing today? Anything worth noting?" → voice or text response → extracted into timeline. Claude designs the check-in; app triggers it. |
| 30 | **Alert me when something contradicts previous medical advice** | ⚠️ | "Your new GP says to stop taking aspirin, but your cardiologist specifically prescribed it. You may want to clarify this." Valuable but high-risk — contradiction detection must be accurate. |
| 31 | **Remind me of upcoming appointments with a prep nudge** | 🔧 | "You have an oncology appointment in 2 days. Want me to prepare your questions?" Calendar integration + Claude's prep capability. |
| 32 | **Alert my care circle when something important changes** | 🔧 | Medication change, new diagnosis, upcoming surgery — auto-generate an appropriate update per circle member's access level. Claude generates; app delivers through Care Circle. |

**Cluster verdict**: This is where ZeroClaw principles matter most. Claude is the brain that decides what to flag, when to remind, what patterns matter. The app is the body that delivers it. Neither works without the other.

---

### Cluster 6: Translating & Adapting

Same information, different audiences. This is the care graph in action.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 33 | **Translate my summary to another language** | ✅ | Dutch → Turkish, Arabic, English, Papiamentu for NL's diverse population. Claude handles this natively. Medical terminology accuracy needs validation per language. |
| 34 | **Adapt the same update for different audiences** | ✅ | Partner gets full clinical detail + action items. Friend gets "Mom had her scan, results look stable, she's feeling okay." Elderly parent gets simplified version. Claude's strongest differentiator for Care Circle. |
| 35 | **Convert clinical language to emotionally appropriate language** | ✅ | "Pathology shows poorly differentiated adenocarcinoma with lymphovascular invasion" → "The lab results show the cancer is an aggressive type that has started to spread to nearby tissue. Your doctor will discuss treatment options with you." Tone matters as much as accuracy. |
| 36 | **Adapt communication for my employer** | ✅ | "I need to explain to my boss why I'll be out for 6 weeks." → Professional, appropriately vague, legally sound. Claude can draft this. |

**Cluster verdict**: This is where Claude + care graph = something nobody else can build. Big Tech builds "translate this text." Ditto builds "translate this health update for my specific mom who worries too much." Context makes the difference.

---

### Cluster 7: Sharing & Distributing

Getting the right information to the right person at the right time.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 37 | **Generate a shareable "what happened at the doctor" update** | ✅ | One-tap: "Share update with Care Circle." Claude generates a summary tailored to sharing — less clinical, more "here's what you need to know." |
| 38 | **Create a caregiver handoff document** | ✅ | When caregiving shifts change: "Current medications, today's mood, what the doctor said yesterday, what to watch for tonight." Structured, practical, actionable. |
| 39 | **Let me control exactly what I share with whom** | 🔧 | Claude generates multiple versions; app handles the permission layer. "Share medication changes with partner and sister. Share mood updates only with partner." Privacy infrastructure is app-side. |
| 40 | **Help me tell multiple people at once without repeating myself** | ✅ | The "phone tree" killer. "Generate updates for my 5 circle members, each in their preferred level of detail." Claude generates all five; user reviews and sends. |

**Cluster verdict**: Sharing is where the care graph moat compounds. Every shared update = a circle member getting value = potential new user. Claude makes multi-audience sharing effortless.

---

### Cluster 8: Navigating & Guiding

The healthcare system is a maze. Claude can help you find your way — within limits.

| # | Job To Be Done | Claude Fit | Notes |
|---|---|---|---|
| 41 | **Help me understand what questions to ask** (guided discovery) | ✅ | Not "here are 50 questions." Instead: "Based on your stage and treatment plan, these 3 questions would give you the most useful information at your next appointment." |
| 42 | **Help me understand my patient rights** | ⚠️ | Jurisdiction-specific (NL: WGBO). Claude has general knowledge but should link to authoritative sources, not generate legal advice. |
| 43 | **Help me navigate the referral process** | ⚠️ | "Your GP said you need a referral to a neurologist. Here's typically how that works in the Netherlands..." General guidance, not specific institutional processes. |
| 44 | **Help me decide if I should seek urgent care** | 🚫 | Hard no. This is medical triage. Claude should ALWAYS say: "If you're concerned, call your GP or 112. I'm not a medical professional." Anything else is a regulatory and safety red line. |
| 45 | **Help me understand what my insurance covers** | ⚠️ | Generic: "In the Dutch system, specialist care after GP referral is typically covered under basisverzekering." Specific policy questions need insurer data integration (Menzis API?). |

**Cluster verdict**: Claude is a compass, not a map. It can orient you and suggest directions, but should never replace professional navigation for urgent, legal, or insurance-specific questions.

---

## Priority Tiers

Scored on: **User Pain** (from research evidence) × **Claude Fit** (can it actually deliver?) × **Strategic Value** (does it build the care graph moat?)

### P1 — Build First: High value, strong Claude fit, strategic

These are the core of what makes ZeroClaw transformative. Most have strong user evidence.

| # | Job | Why P1 |
|---|---|---|
| 1 | Summarize doctor conversation | Already core. Claude upgrade = quality jump + cross-appointment awareness. |
| 8 | Answer follow-up questions (contextual Q&A) | Most-requested feature. Care-graph-native — useless without Ditto's data. Uncopiable. |
| 4 | Explain medical documents/letters | Already exists. Extend with journey context. |
| 34 | Adapt updates for different audiences | THE Care Circle differentiator. Drives sharing, drives growth. |
| 17 | Build a living health profile | Foundation for everything. Every other job improves when this exists. |
| 20 | Generate personalized appointment questions | Strong user evidence. High wow factor. Persistent memory makes this magical. |
| 15 | Extract action items from conversations | Immediately actionable. "Here's what you need to do" after every appointment. |
| 37 | Generate shareable "what happened" updates | Drives Care Circle adoption. Reduces "phone tree" burden. |
| 14 | Extract medication data from conversations | Feeds the living profile. Foundation for medication jobs. |
| 3 | Explain lab results in my context | High pain. Personalization via journey context is the differentiator. |

### P2 — Build Next: High value, needs infrastructure

High user demand but requires app-side systems beyond Claude.

| # | Job | Infrastructure needed |
|---|---|---|
| 27 | Medication reminders | Push notification system, medication schedule storage |
| 13 | Voice narrative extraction | STT pipeline (Whisper/Deepgram) → Claude |
| 28 | Symptom pattern detection | Symptom data accumulation from check-ins or manual input |
| 21 | Appointment prep summary | Calendar integration + living health profile |
| 29 | Proactive check-ins | Scheduled task system, notification delivery |
| 25 | Medication change flagging | Medication state diff engine |
| 33 | Translate to other languages | Validation pipeline for medical terminology per language |
| 18 | Auto-organize into care journeys | Journey data model + classification engine |
| 32 | Alert care circle on important changes | Change detection + Care Circle permission layer + notification |
| 31 | Appointment reminders with prep nudge | Calendar integration + scheduling |

### P3 — Easy Wins: Medium value, strong Claude fit, low effort

Can deliver value quickly because Claude handles them natively.

| # | Job | Why easy |
|---|---|---|
| 6 | Simplify medication leaflets | Text in → simplified text out. No infrastructure. |
| 10 | Help process difficult health news | Claude's empathetic tone. No external dependencies. |
| 9 | Safe space for "dumb questions" | Pure conversational. Context makes it personal. |
| 5 | Explain upcoming procedure | General + personalized knowledge. |
| 7 | Explain diagnosis to my child | Audience adaptation — Claude's sweet spot. |
| 35 | Clinical → emotionally appropriate language | Tone transformation. |
| 23 | Rehearse difficult doctor conversation | Conversational roleplay. |
| 36 | Draft message for employer | Professional adaptation. |
| 38 | Caregiver handoff document | Structured generation from profile data. |
| 41 | Guided discovery — what to ask | Contextual question curation. |
| 40 | Multi-person update generation | Scale of #34. |
| 11 | Answer circle member's questions | Extension of #8 with permission layer. |
| 24 | Procedure preparation guide | General + context. |

### P4 — Explore With Caution: High value, hard limits or high risk

Worth investigating but Claude alone can't deliver safely.

| # | Job | Risk / Limitation |
|---|---|---|
| 26 | Medication interaction flagging | Hallucination risk unacceptable for drug safety. MUST use verified database (KNMP G-Standaard). Claude interprets results, never generates them. |
| 30 | Contradictory advice detection | Must be very accurate. False positive ("your doctors disagree!") could cause patient panic. Needs high-confidence threshold. |
| 44 | Medical urgency triage | 🚫 Absolute hard limit. This is a medical device function. Regulatory red line. |
| 12 | Pre-doctor health conversation | Positioning risk. Must never feel like pre-diagnosis. Careful UX framing required. |
| 45 | Insurance coverage guidance | Needs insurer-specific data. Generic NL system info is safe; specific policy guidance needs Menzis API. |
| 42 | Patient rights guidance | Jurisdiction-specific. Link to authoritative sources, don't generate legal advice. |
| 43 | Referral navigation | Institutional variation. Keep general; don't promise specific processes. |
| 19 | Extract data from EHR screenshots | Privacy concerns (photographing hospital systems). OCR accuracy variable. Needs careful positioning. |
| 16 | Extract data from medication photos | Dutch packaging variation. Validation step mandatory. |
| 39 | Granular sharing permissions | Not a Claude problem — this is pure app infrastructure. Claude generates the content variants; app handles access control. |

---

## What Claude Fundamentally Cannot Do

These are hard architectural limits, not "needs improvement" items.

| Hard Limit | Why | Implication for Ditto |
|---|---|---|
| **Cannot send push notifications** | Claude is an API, not a running process. It responds when called, it doesn't initiate. | App must own the scheduling + delivery layer. Claude decides what/when during planning calls; app executes on schedule. |
| **Cannot access EHR/hospital systems** | No API integration with Dutch hospital systems (yet). EHDS 2029 changes this. | Until EHDS: recording + documents + voice = the input layer. Claude processes what users bring in. |
| **Cannot diagnose or triage** | Not a medical device. Regulatory and safety red line in EU (MDR). | Always deflect: "Contact your GP or 112." Never assess severity. This must be hardcoded, not prompt-engineered. |
| **Cannot guarantee drug safety information** | LLM knowledge of drug interactions is incomplete and may hallucinate. | Use verified pharmaceutical databases (KNMP G-Standaard, DrugBank) as tool calls. Claude explains the results; database provides the truth. |
| **Cannot persist memory between API calls** | Claude has no built-in memory. Every call starts fresh. | App must manage the health profile, conversation history, and context injection. ZeroClaw principle: app IS the memory layer. |
| **Cannot access real-time vitals** | No wearable integration. | Needs Apple HealthKit / Google Fit bridge feeding data to Claude. Claude interprets; it doesn't collect. |
| **Cannot guarantee Dutch medical NLP at 100%** | Dutch medical terminology, abbreviations, code-switching, dialect variation. | Build a medical terminology database as a tool Claude can reference. Validate extraction accuracy before trusting it for medication names. |
| **Cannot replace human emotional support** | Good at empathy, not a therapist. | Position as "helps you organize your thoughts and feelings" not "provides emotional support." Always suggest professional resources for mental health concerns. |

---

## Key Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Medical hallucination** | 🔴 Critical | Never present Claude's medical knowledge as authoritative. Always: "based on your conversation with Dr. X" or "according to your lab results." Ground in data, not general knowledge. |
| **Over-trust** | 🔴 Critical | Users may treat Ditto as a medical authority. Clear disclaimers + design patterns that reinforce "I'm organizing YOUR health info, not providing medical advice." |
| **Dutch NLP accuracy** | 🟡 High | Medication names are the highest-risk category. Validation step mandatory. Build terminology DB. Test extensively before launch. |
| **Privacy / GDPR** | 🟡 High | Health data is special category (GDPR Art. 9). Claude API calls send data to Anthropic. Evaluate: data processing agreement, EU data residency, patient consent. |
| **Anthropic API dependency** | 🟡 Medium | Single vendor risk. Claude goes down = Ditto's intelligence goes down. Consider: fallback model, graceful degradation, SLA requirements. |
| **Cost at scale** | 🟡 Medium | 1M context window per user interaction is expensive. 35K users × multiple daily interactions = significant API cost. Need: smart context management, caching, tiered usage. |
| **Setting wrong expectations** | 🟡 Medium | "Ditto understands my health" → user expects medical competence. Design must reinforce: "Ditto organizes and explains. Doctors decide." |
| **Latency** | 🟡 Medium | Claude responses take seconds. For real-time conversation (voice check-in, Q&A), latency must feel acceptable. Streaming responses help. |

---

## Open Questions for Validation

1. **Data residency**: Does Anthropic offer EU-based Claude API endpoints? Required for GDPR health data compliance.
2. **Dutch medical NLP quality**: What's Claude's extraction accuracy on Dutch medical conversations? Needs a benchmark test against current Azure OpenAI pipeline.
3. **Cost model**: What's the per-user cost of Claude API calls at Ditto's usage patterns? How does 1M context pricing compare to current Azure costs?
4. **KNMP G-Standaard integration**: Can we get API access to the Dutch pharmaceutical reference database for medication safety?
5. **Apple HealthKit / Google Fit**: What health signals are accessible and useful for contextual intelligence?
6. **Context management strategy**: How do we fit a patient's full care journey into context efficiently? What's the compression/summarization strategy for older events?
7. **Graceful degradation**: What happens when Claude is unavailable? What features still work?

---

## What This Unlocks vs. Current State

| Capability | Current (Azure OpenAI) | With Claude + ZeroClaw Principles |
|---|---|---|
| Summarization | Single conversation → summary | Cross-appointment awareness, references previous visits, accumulates context |
| Q&A | None | Follow-up questions grounded in your specific journey data |
| Proactive intelligence | None — user must open app | Scheduled check-ins, medication reminders, appointment prep nudges |
| Personalized sharing | One summary, share as-is | Multiple audience-adapted versions generated automatically |
| Health profile | None | Living profile built from every interaction, conflicts detected |
| Document understanding | Single document → explanation | Document understood in context of full journey history |
| Extraction | Conversation → structured summary | Voice, photos, documents, screenshots → structured profile data |
| Multi-language | None | Summary translated + adapted for non-Dutch family members |
| Pattern detection | None | "Your nausea correlates with chemo Tuesdays" |
| Appointment prep | None | Personalized questions + summary of what happened since last visit |

---

## Next Steps

1. **Benchmark Claude vs. Azure OpenAI** on Dutch medical conversation summarization (quality + accuracy + cost)
2. **Prototype contextual Q&A** (#8) — lowest-infrastructure, highest-impact job. Needs only existing summary data + Claude API.
3. **Design the living health profile data model** (#17) — this is the foundation everything else builds on
4. **Investigate GDPR/data residency** — can we send Dutch patient health data to Claude's API?
5. **Cost modeling** — project Claude API costs at current and projected usage
