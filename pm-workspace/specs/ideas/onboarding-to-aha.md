# Onboarding to Aha — Bridging the Gap Between Install and First Value

**Jira**: BIGB-335 | **Linked Epic**: DPMA-2047 (Mission: Activation Fix - Phase 3)
**Status**: Refined — Awaiting Approval
**Date**: 2026-02-25
**Mode**: Explore

---

## 1. Idea Capture

**Source**: Jira BIGB-335 (Merlijn) + expert input (SpringTide, Bupa) + Lenny frameworks
**Raw input**: Only a small fraction of installs activate. Main hypothesis: users don't experience the core value (conversation → summary) because either the timing isn't right or they never have an "aha moment." Current proxies (explainer videos, infographic with simulated conversation) describe value but don't deliver it.

**Core tension**: Ditto's aha requires a real medical conversation. But the user has no conversation at install time — and we can't control appointment timing. The gap between install and first real use is where we lose people.

---

## 2. Problem Validation

### Is this a real problem?

**Yes — and it's likely the biggest lever we have.**

| Signal | Evidence |
|---|---|
| Low install → activation rate | Mentioned as main blocker in BIGB-335; exact % is a key open question |
| Proxies don't convert | Videos, explainers, simulated conversations already exist and haven't solved it |
| Expert validation (SpringTide) | Time-to-aha is the #1 predictor of retention in health apps — if users don't experience core value in first session, most never come back |
| Expert validation (Bupa) | Scribe-to-agent evolution — pure transcription tools lose to products that deliver immediate AI value without requiring a specific trigger event |
| Episodic product design | User research confirms: "no need yet" / "when applicable" — the app is structurally tied to events users don't control |

### Who does this affect?

**Every single user who installs Ditto.** This isn't a segment problem — it's the activation funnel itself.

- ~100% of users face a gap between install and first real use
- Document scan covers ~1/3 of usage, but conversation recording is the star feature
- Users who install via Menzis or word-of-mouth may have no appointment for weeks/months

### What do users do today?

1. Install → see onboarding explainers → close app → forget
2. Install → watch video → think "cool" → no reason to open again until appointment
3. Install → try simulated conversation → understand concept → still haven't experienced real value
4. A few: install before a known appointment → use it → activate (the happy path we can't force)

### Is this OUR problem to solve?

Absolutely. This is the activation funnel — there's no one else who can solve it. And without solving it, growth investments (Menzis, marketing) leak through a broken sieve.

### Key unknowns to quantify

| Question | Why it matters | How to get it |
|---|---|---|
| What % of installs never generate a first summary? | Sizes the problem | Mixpanel funnel analysis |
| What's the median time between install and first real use? | Shows the gap length | Mixpanel cohort analysis |
| What % of installs have a known appointment within 7 days? | Tells us how many people CAN experience aha quickly | Would need survey or calendar data |
| How does activation rate differ by entry channel (Menzis vs organic vs referral)? | Identifies if some channels self-select for readiness | Mixpanel segmentation |

---

## 3. Creative Solution Exploration

The plan was to go beyond the obvious. Here are 6 directions, ranging from proxies to fundamentally rethinking what the aha moment IS.

### Direction A: Better Proxy / Simulation

**Make the "try before you buy" experience feel real, not fake.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **Interactive summary explorer** | Pre-built realistic summary from an anonymized real patient — user taps through, sees explanations, experiences the output quality | Shows WHAT they'll get; low effort | Still a proxy; no personalization |
| **"Experience a journey"** | 3-minute guided walkthrough: play a real (anonymized) recording snippet → show Ditto processing → reveal the summary | Emotional; shows the magic | Legal complexity of real recordings; still passive |
| **Demo conversation** | User role-plays as patient in a simulated doctor conversation; Ditto processes it and creates a real summary | Active participation; uses real tech | Awkward; contrived; people won't do it |

**Verdict**: Low-hanging fruit but limited ceiling. These help users *understand* the value but don't make them *feel* it personally. Worth doing as a baseline improvement, not as the primary strategy.

### Direction B: Make the Core Action Available NOW

**Don't wait for a doctor visit. Let users experience AI-powered conversation → summary with whatever they have right now.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **"Tell Ditto about your health"** | User speaks freely about their health situation — current conditions, medications, concerns. Ditto creates a structured personal health overview using the same AI pipeline. | Uses core tech; instant; personal; shareable via Care Circle; genuinely useful output | Not the "real" use case; might set wrong expectations |
| **"Record any conversation"** | Let users record a non-medical conversation (with a friend, family member) to see the AI in action | Proves the tech works | Output isn't useful; wasted effort feeling |
| **Medication scan → health profile** | Scan medication boxes → Ditto identifies them, explains interactions, creates medication overview | Tangible; uses AI; immediately useful | Different tech stack; not the conversation→summary magic |

**Verdict**: "Tell Ditto about your health" is the most promising option in this direction. It's the only approach that (a) uses the core technology, (b) produces a genuinely useful output, and (c) creates something personal the user cares about. The health overview becomes their first artifact — and it can be shared with Care Circle, creating a secondary aha for followers.

### Direction C: AI-Assisted Aha

**Instead of waiting for a doctor to have a conversation with, Ditto IS the conversation partner.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **Health intake interview** | Ditto's AI asks the user structured questions about their health (conditions, medications, concerns, goals). Produces a comprehensive health summary. Mimics the doctor-conversation flow. | Closest to the real aha; conversational; personal; the output IS the value | Needs conversational AI capability; medical safety concerns; higher build complexity |
| **"Explain this to me"** | Paste or speak any medical term, diagnosis, or doctor's letter → Ditto gives a clear, patient-friendly explanation | Instant value; low friction; demonstrates AI capability | Small value unit; doesn't show the full summary magic |
| **Appointment prep AI** | "What should I ask my doctor about [condition]?" → AI generates personalized question list based on user's health profile | Useful; forward-looking; bridges to the real use case | Requires health context first; chicken-and-egg |

**Verdict**: The health intake interview is the most transformative option. It flips the script: instead of waiting for the aha, Ditto creates it. The "explain this to me" feature is a great micro-value complement (Direction F territory). Appointment prep depends on having health context first, so it's a downstream feature.

### Direction D: Social/Network Aha (Care Circle First)

**The aha for followers IS the product value — seeing a real summary from someone they love.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **Follower-first activation** | When a patient shares a summary, invited followers see the REAL output before they even install. Their first experience IS the aha. | Most authentic aha possible; zero effort for new user; viral | Depends on existing active users sharing; doesn't help users who install independently |
| **Caregiver invitation with preview** | Invitation includes a preview of what summaries look like + a personal message from the patient | Better than cold invite; shows value | Still a proxy for the follower |
| **"See what [name] shared"** | Deep link from share → app store → install → immediately see the shared summary | Removes all friction between invite and value | Technical: requires deferred deep linking |

**Verdict**: This is the highest-quality aha possible — but only works for users who come through Care Circle invitations. For organic/Menzis installs (likely the majority), this doesn't help. Should be optimized as a channel-specific strategy, not the primary solution.

### Direction E: Timing-Aware Activation

**If we can't control when appointments happen, we can at least prepare for them.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **"When is your next appointment?"** | Ask during onboarding → drip reminders as date approaches → "Don't forget to use Ditto!" | Simple; respects natural timing; low effort | Still waiting; users may forget the app exists by then |
| **Calendar integration** | Detect medical appointments from calendar → proactive nudges | Seamless; situation-aware | Privacy-sensitive; not all users add appointments to calendar; platform permissions |
| **Smart re-engagement** | If user hasn't activated after 7 days, trigger campaign: "Got an appointment coming up? Here's how to use Ditto" | Catches users before they churn completely | Email/push fatigue; low response rates |

**Verdict**: Useful as a retention safety net but fundamentally doesn't solve the problem — it accepts the gap and tries to survive it. Good complement, not a primary strategy.

### Direction F: Micro-Value Before Macro-Value

**Build trust and engagement through small, instant wins that lead to the full aha.**

| Approach | Description | Pros | Cons |
|---|---|---|---|
| **Medical term explainer** | "What does [term] mean?" → instant clear explanation | Immediate value; zero setup; demonstrates AI | Small; may not drive retention alone |
| **"Understand your letter"** | Photo/paste a doctor's letter → Ditto explains it in plain language | High value; common pain point; uses AI | Document-focused, not conversation-focused |
| **Health question answerer** | "Is [symptom] normal after [treatment]?" → AI gives contextual, clear answer | Personally relevant; feels like the AI "knows" you | Medical liability concerns; needs careful framing |
| **Progressive profiling** | Each micro-interaction builds the user's health profile, making the eventual real summary richer | Creates accumulating value; each use makes Ditto smarter about you | Slow payoff; requires patience |

**Verdict**: Excellent lubricant strategy. These features lower the barrier to engagement and build the habit of turning to Ditto for health clarity. "Understand your letter" is especially strong because ~1/3 of current usage is document scanning — this extends that capability to letters and results patients receive at home.

---

## 4. Strategic Fit Scoring

Scored against Ditto's RISCE dimensions + strategic priorities.

| Direction | R (Reach) | I (Impact) | S (Strategic) | C (Confidence) | E (Effort) | RISCE | Notes |
|---|---|---|---|---|---|---|---|
| **A. Better proxy** | 5 | 2 | 3 | 4 | 5 | 600 | High reach, low impact — polishing what we have |
| **B. "Tell Ditto about your health"** | 5 | 4 | 5 | 3 | 3 | 900 | Core tech, personal output, but unproven concept |
| **C. Health intake interview** | 5 | 5 | 5 | 2 | 2 | 500 | Highest potential, lowest confidence, highest effort |
| **D. Follower-first aha** | 2 | 5 | 5 | 4 | 3 | 600 | Best aha, but limited to Care Circle channel |
| **E. Timing-aware activation** | 4 | 2 | 3 | 4 | 4 | 384 | Safety net, not a solution |
| **F. Micro-value ("Understand your letter")** | 4 | 3 | 4 | 4 | 4 | 768 | Quick win, builds trust, extends existing behavior |

**Gut check**: The RISCE numbers put B and F on top, which feels right. C scores lower because effort and confidence drag it down — but it has the highest potential ceiling. D scores lower on reach because it only works for Care Circle invites, but where it works, it's unbeatable.

**Delight x Effort quick filter**:

| | Low Effort | High Effort |
|---|---|---|
| **High Delight** | F: Micro-value (ship soon) | B: Health overview (Explore bet) |
| **Low Delight** | A: Better proxy (batch) | C: Intake interview (Explore later) |

---

## 5. Recommendation

### Primary bet: Direction B — "Tell Ditto About Your Health"

**What**: During onboarding, after explaining what Ditto does, invite the user to speak about their health situation for 1-2 minutes. Ditto processes it using the same AI pipeline and produces a personal health overview — structured, clear, shareable.

**Why this wins**:
1. **Uses the core technology** — users experience the REAL AI, not a simulation
2. **Produces something personal and useful** — their health overview, not a demo artifact
3. **Available immediately** — no appointment needed, no timing dependency
4. **Creates a shareable first artifact** — "Share your health overview with your Care Circle" = secondary aha for followers
5. **Bridges to the real use case** — "Imagine what Ditto does with your actual doctor conversation"
6. **Situation-independent** — works regardless of when their next appointment is

**Why not C (health intake interview)?** C is the more ambitious version of B. B lets the user talk freely; C has the AI ask structured questions. C is better but significantly harder to build and has more medical safety implications. Start with B, graduate to C if B validates.

### Quick win: Direction F — "Understand Your Letter"

**What**: Add ability to photograph/paste a doctor's letter, lab result, or discharge note → Ditto explains it in plain language.

**Why**: ~1/3 of users already use document scan. This extends that capability to something users receive at home and need help understanding *right now*. It's the micro-value play that builds trust and creates an immediate reason to open the app.

### Channel-specific: Direction D — Follower-First Aha

**What**: Ensure that Care Circle invitations include (or lead to) a real summary preview, so the follower's first experience IS the aha moment.

**Why**: For users who arrive through Care Circle, this is the highest-quality aha possible. Requires deferred deep linking and invitation flow optimization — work that's likely already adjacent to Care Circle v2.

---

## 6. Standard Refinement Output

### Problem

Users who install Ditto can't experience the core value (conversation → summary) until they have a real doctor visit — which might be days, weeks, or months away. Current proxies (videos, explainers, simulated conversations) describe value but don't deliver it. This gap is the primary cause of low activation rates.

### Proposed Solution

**"Tell Ditto About Your Health"** — a voice-first health overview feature in the onboarding flow. Users speak about their health situation, Ditto produces a structured personal health overview using the real AI pipeline. This creates a genuine aha moment without requiring a doctor visit.

Complemented by:
- "Understand Your Letter" as a micro-value feature for home use
- Follower-first aha optimization for Care Circle invitations
- Timing-aware nudges as a retention safety net

### Expected Impact

| Metric | Current (estimated) | Target | Mechanism |
|---|---|---|---|
| Install → first summary | Low (unknown %) | +50% relative | Removes timing dependency |
| Time to first value | Days/weeks | <5 minutes | Immediate voice interaction |
| Care Circle invitation conversion | Unknown | +25% relative | Shareable first artifact |
| 7-day retention | Unknown | +30% relative | Users have a personal artifact + reason to return |

### Open Questions

| # | Question | Priority | How to answer |
|---|---|---|---|
| 1 | What's the current install → first summary conversion rate? | Critical | Mixpanel funnel |
| 2 | What's the median time between install and first use? | Critical | Mixpanel cohort |
| 3 | Can the existing AI pipeline handle freeform health narratives (not doctor-patient conversation)? | High | Technical spike (1-2 days) |
| 4 | What should the health overview output look like? Sections? Detail level? | High | Design exploration + 5 user tests |
| 5 | Does creating a health overview set wrong expectations about what Ditto normally does? | Medium | User interviews post-prototype |
| 6 | What's the minimum speech duration needed to produce a useful output? | Medium | Technical testing |
| 7 | How do we handle users who don't want to speak / are in public? | Medium | UX exploration (text fallback?) |

### Cheapest Validation

**Week 1 — Analytics baseline**:
- Pull Mixpanel data: install → activation funnel, time-to-first-use, channel segmentation
- This tells us the exact size of the problem

**Week 1-2 — Concierge test**:
- Recruit 10 users (mix of new installs and dormant users)
- Voice call: "Tell me about your health situation" (2-3 minutes)
- Manually run through AI pipeline, produce health overview
- Send to user, ask: "Is this useful? Would this make you want to use Ditto more? Would you share this?"
- Measure: perceived value, surprise/delight, sharing intent

**Week 2-3 — Technical spike**:
- Feed 5-10 freeform health narratives into the existing pipeline
- Assess: Does it produce quality output? What breaks?

**Total cost**: ~2 weeks, no engineering build, answers the three critical questions: (1) how big is the problem, (2) do users value the output, (3) can our tech handle it.

### Dependencies

| Dependency | Type | Status | Risk |
|---|---|---|---|
| AI pipeline handles freeform input | Technical | Unknown — needs spike | Medium |
| Onboarding flow can accommodate new step | Product/Design | Assumed feasible | Low |
| Care Circle sharing works for non-summary artifacts | Technical | Unknown | Low |
| Mixpanel instrumentation for activation funnel | Analytics | Likely exists partially | Low |

### Size Estimate

| Component | Size |
|---|---|
| Analytics baseline | S (days) |
| Concierge validation | S (1-2 weeks) |
| "Tell Ditto" MVP (if validated) | M (3-4 weeks) |
| "Understand Your Letter" | S-M (2-3 weeks) |
| Follower-first aha optimization | S (1-2 weeks, depends on CC v2) |

**Total if all validated and built**: L (6-10 weeks, phased)

### Backlog Placement

**Now**: Analytics baseline + concierge validation (zero build cost, answers critical questions)
**Next**: "Tell Ditto About Your Health" MVP (if concierge validates)
**Next**: "Understand Your Letter" (quick win, parallel track)
**Later**: Health intake interview (Direction C — the ambitious evolution of B)
**Later**: Follower-first aha (depends on Care Circle v2 shipping)

---

## Multi-Perspective Review

**User** 🟢
This directly addresses the #1 pain point: "I installed it but have nothing to use it for right now." Letting users speak about their health is intuitive and low-friction. The output (health overview) is genuinely useful — something they'd want to keep and share. Risk: some users might feel awkward talking to their phone about health without a clear structure.

**Mobile Dev** 🟡
The voice recording and AI processing pipeline largely exists. Key question: does the AI produce quality output from unstructured health monologues vs. doctor-patient dialogues it was trained on? Freeform input might need prompt engineering or a new processing template. The "Understand Your Letter" feature is more straightforward (document → text → AI explanation). No major new infrastructure needed.

**CPO/Strategy** 🟢
This is exactly what "Activation Fix Phase 3" should be. It tackles the fundamental problem (timing dependency) rather than another proxy. The concierge-first validation approach means we learn before we build. If B works, it could redefine what Ditto IS — not just a doctor-visit tool but a personal health companion.

**Growth** 🟢
The sharable first artifact is the growth unlock. If a new user creates a health overview and shares it with 3 family members → those 3 see real AI output → that's 3 potential activations from 1 onboarding session. This turns the activation moment into a referral moment. Combined with Care Circle v2, this could be the engine.

**Business** 🟢
Solves the Menzis ROI problem: if we can't activate their users, the partnership value drops. This makes every install more likely to convert, regardless of appointment timing. No revenue model change needed — this is about fixing the funnel, not monetizing a new feature.

**Privacy/GDPR** 🟡
Users voluntarily sharing health information via voice is already within Ditto's consent model. However: the health overview is a new data artifact that needs proper storage, deletion rights, and sharing consent flows. The "Understand Your Letter" feature processes medical documents — similar to existing document scan but potentially with more sensitive content (lab results, diagnoses). No red flags, but needs the standard GDPR review.

---

*Feedback? (optional)*
1. *Yes, let me share*
2. *Not now / later*
3. *Not needed — you were perfect*
