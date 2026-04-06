# Ditto's AI Brain: From Summarization Tool to Care Intelligence Platform

**Date**: 2026-04-04
**Status**: Strategic spec (approved)
**Context**: What does Ditto become when you treat the LLM as the brain of the entire product, not a summarization endpoint? This supersedes the ZeroClaw JTBD Discovery as the strategic framing.

---

## Why Now

- AI costs crashed 40-80% YoY. Long-context surcharges eliminated.
- Apple scaled back Health+ AI Coach (Feb 2026). Consumer health AI field more open than expected.
- EHDS first elements (Patient Summaries, ePrescriptions) go live Fall 2026.
- Voice-first healthcare going mainstream by Q4 2026.
- Only 3% of healthcare orgs have agentic AI in production. First-mover window exists.
- Summarization is commoditizing (Ambience at $3B+, Epic AI, every EHR adding it). Staying "AI summarization" = slow death.

---

## Critical Review of ZeroClaw

### Strong

1. **"AI as connective tissue" is the right positioning.** Dodges direct competition with $T companies building general-purpose health AI.
2. **The care graph thesis is genuinely differentiated.** Big Tech builds individual health AI. None build the social layer of care.
3. **JTBD discovery is thorough.** 37 jobs, capability-assessed, priority-tiered.
4. **Hard limits honestly acknowledged.** No triage, no diagnosis, drug safety needs verified databases.

### Weak

1. **37 jobs is a wish list, not a strategy.** The ONE thing that proves the thesis is missing.
2. **No connection to current reality.** Team fighting AI quality regression, CC V2 low adoption, activation is #1 priority.
3. **Claude-specific dependency contradicted by engineering.** Team actively integrating Gemini 3 Flash. Zero Claude work exists.
4. **Living health profile is foundational but undesigned.** No data model, no extraction strategy, no conflict resolution.
5. **Cost modeling absent.** Not quantified at 35K users, let alone at scale.
6. **Care graph moat is theoretical.** CC V2 organic adoption is low. Network effects unproven.
7. **No validation of demand.** JTBD list from logic, not user interviews.
8. **Interface question unresolved.** "Not a chatbot" but doesn't say what it IS.

---

## Market Intelligence (April 2026)

### Competitive landscape

| Player | Status | Implication |
|---|---|---|
| **Apple** | Scaled back Health+ AI Coach. Shipping features individually. | Biggest threat retreated. Window open. |
| **OpenAI** | Acquired Torch Health. Building "unified medical memory." 40M health queries/day. | Most aggressive threat. Building for individuals, not circles. |
| **Microsoft** | Copilot Health launched March 2026. 50K+ US providers. | US-focused, enterprise-adjacent. |
| **Google** | Incremental. Fitbit upgrades, clinical AI, research. | Long game, not consumer companion. |
| **b.well** | "bailey" white-label AI assistant. 350+ data sources. Used by OpenAI and Samsung. | Infrastructure play. Could be partner or competitor. |
| **Hippocratic AI** | $3.5B valuation. Patient-facing agents for chronic care. | Most analogous, but US-only and provider-facing. |

### By October 2026

1. EHDS first elements operational. First consumer app to ingest Patient Summaries wins.
2. Voice-first is table stakes. Ditto must have voice beyond recording.
3. AI costs continue dropping. 1M context windows economically viable.
4. EU AI Act enforcement begins (August 2026). Compliance = moat.
5. Agentic AI still limited. Being early in production is possible.
6. Summarization fully commoditized.

### Takeaway

Summarization got Ditto to 35K users. It won't get to 350K. The next phase requires something that can't be replicated by adding a "summarize" button to a hospital portal.

---

## Strategic Approach: LLM as Brain, Not Feature

### Current

```
Input (recording) --> AI (summarize) --> Output (summary card)
```

### Target: The Care Brain

```
               ┌─────────────────────────────────┐
               │          CARE BRAIN              │
               │                                  │
               │  Memory + Reasoning + Actions    │
               └──────┬──────────────┬────────────┘
                      │              │
             ┌────────┴───┐   ┌─────┴──────────┐
             │ Input Layer │   │ Surface Layer   │
             │             │   │                 │
             │ Recording   │   │ Living Summary  │
             │ Doc photo   │   │ Journey Timeline│
             │ Voice update│   │ Circle Views    │
             │ EHDS data   │   │ Prep Screens    │
             │ Lab results │   │ Health Profile  │
             │ Quick text  │   │ Q&A Interface   │
             └─────────────┘   │ Nudge System    │
                               └─────────────────┘
```

The AI powers EVERY surface. Every screen the user sees has been touched by intelligence that knows their full context.

### Brain vs. Chatbot

| Chatbot | Brain |
|---|---|
| User asks, gets answer | Every screen already intelligent |
| Explicit interaction | Ambient, often invisible |
| Competes with ChatGPT Health | New category |
| AI is the product | AI powers the product |
| One interface paradigm | Many bespoke surfaces |
| "Talk to your health AI" | "Ditto just knows" |

### Concrete example

Patient records oncologist appointment. Within 60 seconds, WITHOUT doing anything:

1. Summary appears referencing what was discussed 3 appointments ago
2. Medication list auto-updates (brain detected "switching from capecitabine to oxaliplatin")
3. Follow-up questions surface from gaps in conversation + unresolved items from previous visits
4. Partner gets notification with their version: full context + action items
5. Elderly parent gets simplified notification in their preferred language
6. Calendar event for next appointment with prep reminder
7. Journey timeline marks treatment change milestone

One button press. That's the brain.

### Model-agnostic, not model-specific

- **Orchestration layer** routes tasks to best model
- Long-context reasoning: best long-context model (currently Claude Opus)
- Fast summarization: cheapest fast model (Gemini Flash)
- Extraction: best structured output (varies)
- Translation: best multilingual (varies)

The brain is the ARCHITECTURE. Models are swappable. Care graph + journey memory + orchestration = moat.

---

## Bespoke Interface: Contextual Intelligence Surfaces

Not a chatbot. Many specialized surfaces, each powered by the brain:

**1. Living Summary** -- Dynamic document. Tap any sentence for explanation. See connections to previous visits. Highlighted changes. Tappable action items.

**2. Journey Timeline** -- Visual care journey. Auto-detected milestones. Brain connects events across time.

**3. Health Profile Card** -- Auto-populated from every interaction. Medications, conditions, care team. Not a form. A living document the brain maintains.

**4. Circle View** -- Each circle member sees THEIR view. Partner: full detail + actions. Friend: "how things are going" + "what would help." Auto-generated.

**5. Prep Screen** -- Before appointments: what happened since last visit, suggested questions, unresolved items. Generated from journey context.

**6. Ask Surface** -- Conversational but constrained. "Ask about this summary." Context-bound Q&A. Useless without Ditto's data. Uncopiable.

**7. Nudge System** -- Proactive, minimal. Appointment prep. Symptom patterns. Not notification spam.

**Design principle: Magic, not AI.** For the 50+ audience: "Ditto just understands me." Never "I'm using AI."

---

## 6-Month Plan

### Starting position (honest)

- AI quality regressed (98% to 95%). Must fix first.
- CC V2 organic adoption low. Care graph unproven.
- Activation: 10.5%. Funnel breaks at recording step.
- Team: 10 people. Doing CC V2, activation, Customer.io, AI quality.
- Active AI: Gemini fallback, guardrail calibration. No health profile. No voice input.

### Sequence

**Phase 0: Fix Foundation (Weeks 1-4)**
- AI quality to 98%+ (DP-45, DP-34, DP-59, DP-60, DP-61)
- Ship CC V2 P1 items
- Validate: do CC V2 users invite circle members? At what rate?

**Phase 1: Contextual Q&A (Weeks 5-10)**
The smallest move that proves the brain.

After every summary, users ask follow-up questions answered from FULL conversation context + previous summaries. Not general knowledge. YOUR data.

Interface: Smart suggestions paradigm, NOT chatbot. Contextual suggestion chips below summary sections: "Want to know more about this medication change?" Tap -> answer expands inline. AI suggests, user confirms. Optional "Ask something else" for power users. Feels interactive and intelligent, not like "using AI."

Metric: 20%+ of summary viewers engage with Q&A within 4 weeks.

**Phase 2: Living Health Profile (Weeks 8-14)**
The foundation.

Brain extracts structured data from every interaction: medications, conditions, care team, action items, timeline events. Zero user effort.

Interface: "Profile" tab. What the brain knows about you. User corrects. Brain maintains.

Metric: 50%+ of patients with 2+ conditions and 3+ medications after 8 weeks.

**Phase 3: Voice Input (Weeks 12-18)**
"Tell Ditto."

Voice for quick health updates between appointments. "They changed my medication to X." "Feeling nauseous this week." STT -> brain extracts -> confirms.

Interface: Microphone button on home screen. Tap, talk, done. 10-second interaction.

Metric: 15% of active users use voice in 30 days.

**Phase 4: Smart Sharing (Weeks 16-22)**
The care graph comes alive.

Brain auto-generates audience-adapted updates for circle members. Patient reviews, one-tap send.

Interface: "Share" screen with preview cards per circle member, each adapted.

Metric: CNIS uplift within 8 weeks.

**Phase 5: Proactive Intelligence (Weeks 20-26)**

- Appointment prep from journey context
- Pattern detection v1 ("You've reported fatigue 3 weeks running")
- Proactive nudges tied to Care Circle events

---

## Multi-Perspective Review

### a16z VC

- 🟢 Care graph thesis is fundable. TAM real. EHDS tailwind. Network effects story.
- 🔴 "Show me the graph is real." CC V2 adoption is low. Prove it.
- 🟡 Core product commoditizing. Pivot to care intelligence is existential.
- 🟡 "Where's the 10x?" Currently pitching a future, not a present.
- Verdict: Series A-ready if 6-month plan produces (1) validated care graph growth, (2) Q&A engagement proving brain > chatbot, (3) EHDS readiness.

### Steve Jobs

- Loves: One button, seven things happen. AI invisible. Voice in, visual out.
- Kills: 37 JTBD (pick ONE). Health profile as spreadsheet. Sharing as transaction. Architecture jargon.
- Reframe: "Ditto turns one conversation into understanding for everyone who cares."
- Verdict: Vision right. Packaging wrong. Strip technical language. Frame as human experience.

### 60-year-old cancer patient

- Needs: Understand the doctor. Show my daughter. Questions at 11pm. Don't make me learn.
- Hates: "AI." Forms. Too many notifications. Sharing without asking.
- Wow: Summary that knows my journey. Partner who gets their own update. Appointment prep that remembers what I forgot.
- Verdict: Every feature passes one test: would my mom use this without my help?

---

## The Unicorn Feature

**One recording. Everyone understands.**

Patient presses record. Every person in their care circle receives a personalized, audience-adapted understanding. The partner knows what to do. The child knows how mom is feeling. The friend knows things are okay. The patient's questions are answered before they think to ask.

No other product does this. Big Tech builds for one person. Ditto builds for the circle.

---

## Open Questions (Resolved 2026-04-04)

1. **Contextual Q&A demand**: Not THE most requested, but heavily requested and a very common pattern. Confirmed as Phase 1.
2. **CC V2 invitation rate**: ~50 users/day sending invitations. Significant growth. Care graph thesis validated.
3. **Model economics**: Most users are followers with episodic usage. Heavy users (oncology) are minority. Economics acceptable at scale even with high MAU.
4. **EHDS**: Deprioritized. Won't be feasible for 2 years. Don't build dependencies on it. Remove from Phase 5; replace with proactive intelligence only.
5. **Interface paradigm (critical)**: NOT chat. Smart suggestions. "Do you want to know more about this?" -> tap -> answer. AI suggests, user confirms. Seamless, trustworthy, guided. User doesn't need to understand AI. Interaction feels interactive and intelligent, not like "using a chatbot."

---

## Verification

Per phase:
1. **Quantitative**: Mixpanel engagement, retention, CNIS
2. **Qualitative**: 5 user interviews per phase (JTBD format)
3. **Technical**: AI quality SLO 98%+, latency <3s Q&A, <60s full processing
4. **Strategic**: Does this compound toward the care graph moat?
