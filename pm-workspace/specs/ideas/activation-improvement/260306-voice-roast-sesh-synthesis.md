# Activation Improvement — Voice & Roast Sesh Synthesis

**Source**: [Granola: Voice & Roast Sesh](https://notes.granola.ai/d/6a6603ef-7555-4eb4-816f-6919e233f137) (2026-03-06)
**Participants**: Merlijn + Nick
**Status**: Raw synthesis — needs idea board comparison

---

## The Core Problem

Growth is not sustainable with the current activation funnel. Acquisition spend (performance channels, Volkskrant ad) doesn't convert because the gap between install and first value is too large. Brand awareness is positive, but if 90% of starters abandon activation, nothing downstream works — not monetization, not referrals, not viral loops.

**Activation funnel data shared in meeting:**

| Step | Users | Drop-off |
|---|---|---|
| Started activation | 1,251 | — |
| Set appointment (trackable) | 124 (10%) | 90% lost |
| Completed next step | 51 (4%) | 59% of previous |
| Started Geert's video | 28 (2.2%) | 45% of previous |

Note: 124 is a tracking floor — actual completions are higher but unmeasured.

**Benchmark**: Nick's previous company saw ~17% trial start rate, but that's with a clear immediate payoff (listen to an audiobook). Even there, 50% listened <5 min and 30% became passive subscribers.

---

## Two Activation Philosophies Discussed

| Approach | Mechanism | Risk |
|---|---|---|
| **Investment tricks** | Behavioral psychology — get users to invest early so sunk cost keeps them | Works but feels manipulative; doesn't build real engagement |
| **Immediate value delivery** | Show what Ditto can do for you *right now*, build trust through quality | Harder to execute but creates genuine retention |

**Consensus**: Prefer immediate value. The "aha moment" — the app understands me, this is personal, this is smart — is more powerful than commitment devices.

---

## Concrete Ideas Discussed

### 1. Voice-First Profile Building (highest energy in conversation)

User talks naturally about their health situation. Ditto extracts facts in real-time (streaming voice + fact extraction). A validation step follows: tappable facts ("You take metformin" — confirm/edit) that populate the health profile.

**Why this is powerful:**
- Reusable flow: same mechanic for onboarding, appointment prep, document processing, journaling
- Demonstrates AI capability immediately — "it understands my voice, it knows what I said"
- Removes typing friction for elderly users
- Profile becomes the foundation for all downstream personalization

**Open question**: What's the minimum the voice extraction must handle to feel impressive rather than broken?

**Connects to**: [Direction B: Speak to Ditto](../direction-b-speak-to-ditto.md), [Onboarding to Aha](../onboarding-to-aha.md)

### 2. Smart Appointment Questions

During a medical conversation, Ditto generates dynamic questions based on context. Two modes discussed:

- **Pre-appointment**: User gets smart questions based on their profile + upcoming appointment type
- **End-of-conversation**: Doctor asks "any questions?" — Ditto shows 5 relevant questions extracted from what was discussed but not fully answered

The Q&A becomes a component of the summary, not the summary itself. Questions with answers extracted from the conversation.

**Why this matters for activation**: Even before a user records a full conversation, preparing smart questions for an upcoming appointment delivers value and demonstrates intelligence.

**Technical note from Merlijn**: Question checking (are they already answered?) and dynamic generation are feasible. UX challenge: you don't want people staring at their phone during the conversation.

### 3. Care Circle Timing Experiment

**Hypothesis**: Some users have no personal appointment but DO have someone they'd follow. Moving "add a loved one" earlier could activate a different segment.

**Proposed experiment**: Feature flag A/B test — 50% start with appointment setup, 50% start with "add a loved one."

**Risk acknowledged**: Care Circle v1 didn't land. V2 is better but unproven. Also: empty profile = chicken-and-egg problem (why fill in profile if no followers? why follow someone with empty profile?).

### 4. Ditto Chat — Contextual AI Interface

A chat interface where users can:
- Upload documents (briefs, letters) as context
- Reference past conversations or summaries
- Do voice journaling
- Query health data ("how was my sleep this week?" → visual component)
- Get guided insights (not open-ended)

**Critical design constraint**: This is NOT a general-purpose ChatGPT clone. Open-ended chat competes with tools Ditto will never beat. Instead: guided capabilities with clear value paths. "We can do 10 things well — pick one to start."

**Pinnable components**: User asks about their headache pattern → gets a visualized component → pins it to home screen. Personalized dashboard emerges from usage.

**Connects to**: Health integrations (Apple Health built, Google Fit planned), symptom tracking

### 5. Health Integrations as Signal Layer

Apple Health integration is built. Google Fit coming. The value isn't just data — it's the signal function: "Where do I see how I'm doing health-wise?"

Nobody owns this well today. Apple Health is too raw. Wearable apps are too narrow. Ditto could be the *interpretation layer* that makes health data meaningful in context.

### 6. Intent Question in Onboarding

Ticket BIGB-2190 — bringing back the "what do you want to use Ditto for?" question. Already designed.

**Tension**: Onboarding is getting long with new additions. Solution: not everyone needs all steps — completing even one is better than nothing. Could be one-time or toggled.

**Action**: Merlijn pulling this into current sprint.

---

## Strategic Threads

### Brand Building Pivot
Nick met with Mieke (branding). Performance marketing channels aren't working for Ditto's audience. Shifting to:
- Local/Netherlands-first brand building
- Press-first then product advertising (sequenced, like "de koffiejongens")
- Deals with publishers (DPG, RCF) at ~90% discount
- Need: creative director type, 1 day/week freelance, pragmatic storytelling

### Speed of Building as Strategic Advantage
Strong agreement: the team can build faster than they can decide. Engineering is ahead of design in velocity. The old "decide what NOT to build" wisdom is partially outdated when build cost approaches zero and experiments are truly zero-loss.

**Implication**: Lean toward building and testing over extended deliberation, as long as experiments are lightweight and reversible.

### Team Gaps
- **Mobile engineer** (Rotterdam, on-site) — job posting going live this week
- **Brand/creative** — freelance 1 day/week, not an agency or expensive branding exercise
- **Product owner gap** — nobody is full-time PO, things fall through cracks. Could be solved by agent/automation (Slack bot with daily digest of open items)
- Nick expressed interest in shifting more toward product (from marketing) once brand/creative work is delegated

### Tooling Discussion
Linear + Notion migration considered (Bart de Stegen proposed). Conclusion: it's not about the tool, it's about workflows. Current Jira/Confluence works with discipline but things still get lost. Non-technical team members struggle with complex tooling (Notion sandboxing problem). Agent-assisted workflows may solve more than a tool switch.

---

## Comparison Points for Idea Board

These emerged from the conversation and should be cross-referenced:

| Topic | Existing Artifact | New Signal from Meeting |
|---|---|---|
| Voice profile building | [Direction B: Speak to Ditto](../direction-b-speak-to-ditto.md) | Strong endorsement; prototype planned for Friday demo; reusable flow confirmed |
| Activation funnel fix | [Onboarding to Aha](../onboarding-to-aha.md) (BIGB-335) | Hard data on 90% drop-off; benchmark from Nick's prior company |
| Care Circle timing | [Care Circle v2](../care-circle-v2/) | A/B test proposed; acknowledged as risky bet |
| Smart appointment questions | [Voice Health Check-in](../voice-health-checkin/) | Refined thinking: end-of-conversation Q&A, not mid-conversation phone staring |
| Chat + context interface | New — not yet in idea board | Modulair chat with guided capabilities, pinnable components, health data queries |
| Health integrations | New — not yet in idea board | Apple Health built, signal layer framing, pinnable health components |
| Intent onboarding question | BIGB-2190 | Already designed, pulling into sprint |

---

## Next Steps (from meeting)

1. **Friday demo**: Merlijn hacking voice + fact extraction prototype in iOS
2. **Activation A/B**: Design experiment for appointment-first vs care-circle-first
3. **Survicate on drop-off**: Add survey at activation abandonment point to understand WHY
4. **Intent question**: Ship BIGB-2190 this sprint
5. **Mobile engineer job post**: Live this week
6. **Brand strategy**: Nick continuing conversations with Mieke + koffiejongens network
7. **Prototype voice profile setup**: Define minimum viable extraction scope
