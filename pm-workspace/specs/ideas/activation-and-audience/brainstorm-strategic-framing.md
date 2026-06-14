# Activation & Audience — Strategic Brainstorm

**Date**: 2026-03-20
**Status**: In progress — strategic framing phase
**Participants**: Merlijn + Mewtwo

---

## The Problem (Two Faces)

1. **Acquisition mismatch** — Performance marketing acquires too broad a group. Many users are "too healthy" to feel the pain. Not in a life moment window.
2. **Activation dependency** — Even for the right users, the aha moment (getting a summary) requires an external event (a doctor appointment) that Ditto doesn't control.

### Funnel data (from 2026-03-06 meeting)

| Step | Users | Drop-off |
|---|---|---|
| Started activation | 1,251 | -- |
| Set appointment (trackable) | 124 (10%) | 90% lost |
| Completed next step | 51 (4%) | 59% of previous |
| Started Geert's video | 28 (2.2%) | 45% of previous |

Benchmark: ~17% trial start rate in comparable apps (audiobook app, Nick's prior company).

### What we know about who activates

- Cancer is the most dominant group among active users
- People who activate tend to do so within a week
- If acquisition is done well (targeting life moments), most users SHOULD have appointments
- The "no appointment" group may shrink if acquisition improves, but currently it's large

---

## Strategic Frame: Life Moments

From [Focus on Life Moments in Healthcare](https://dittocare.atlassian.net/wiki/spaces/DG/pages/873496592):

Ditto targets **teachable moments** — windows opened by life events when someone is unusually receptive. Three conditions: it feels personal, routines break down, something is at stake.

### Three life moments

| Life moment | Characteristics | Care circle activation |
|---|---|---|
| **Becoming parents** | Most appointment-dense period; both partners open to new habits; health = gain, not threat | Fully activated |
| **Facing serious illness** | Cancer, heart attack, chronic escalation. Cognitively intact but fear suppresses recall | Immediate — partner, adult children, close family |
| **Losing cognitive capacity** | Dementia, Alzheimer's, Parkinson's. Progressive trajectory, family member takes over cognitive work | Gradual takeover by caregiver |

~95-98% of Dutch adults pass through at least one. ~20% are actively in a window at any time.

### Strategic decision: Go deep on cancer first

Cancer has the strongest natural pull:
- High appointment frequency (2-4/month across specialists)
- Information overload (treatment plans, second opinions, scan results)
- Care circle activates immediately
- Emotional stakes are highest — fear suppresses recall
- Long journey (months to years) = structural retention
- Largest current active user group (product-market pull already exists)

Flo analogy: They started with one life moment (menstrual cycle), nailed it, then expanded to pregnancy, fertility, menopause. Each moment built on trust earned in the first.

---

## Three Pillars + Layered Sequencing

### Ditto's product pillars

| Pillar | What | Patient promise |
|---|---|---|
| **Clarity** | Understanding what's happening | You understand what was said, what it means, what's next |
| **Convenience** | Making it easy to navigate | Everything in one place — journey, questions, decisions |
| **Connection** | Informing others | The people who care about you stay informed and can help |

### How the pillars sequence (layers)

```
Layer 3: Shared understanding — circle sees, helps, supports     (Connection)
Layer 2: Sharing — patient pushes context outward, zero effort   (Connection)
Layer 1.5: Habit — everything organized, reasons to return       (Convenience)
Layer 1: Patient clarity — I understand what's happening to me   (Clarity)
```

Build bottom-up. Clarity creates trust. Convenience creates habit. Connection creates the growth loop.

### Mapping to Antonovsky's Sense of Coherence

Research-backed framework for coping with serious illness. Maps cleanly:

| Sense of Coherence | Ditto pillar | Patient experience |
|---|---|---|
| **Comprehensibility** — I can understand what's happening | Clarity | Plain language summaries, explained terms, organized information |
| **Manageability** — I have resources to deal with this | Convenience | Prepared for appointments, everything in one place, trusted resources |
| **Meaningfulness** — This matters, I matter | Connection + Identity | I'm the narrator of my journey, my circle understands, I'm not alone |

---

## Four Layers of Patient Need

Most health tech only addresses layer 1. Ditto's opportunity is to go deeper.

### Layer 1: Informational (surface)
"I need to know what the doctor said."
- 35-80% of cancer patients experience significant psychological distress
- Table stakes — necessary but not differentiating

### Layer 2: Psychological
"I need to feel less anxious, less overwhelmed, more in control."
- 58% of cancer patients feel emotional needs get less attention than physical needs
- Strengthening sense of coherence directly improves resilience and quality of life
- Ditto's role: comprehensibility (plain language) + manageability (organized, prepared)

### Layer 3: Relational
"I need to not be alone, but I also don't want to be a burden."
- Core tension: patients need connection but feel guilty about the burden
- Caregivers suffer from information deficits, helplessness, psychological strain — not because they don't care but because they don't know enough to help
- Ditto's role: share without retelling, circle can act without asking

### Layer 4: Existential (deepest)
"Who am I now? Do I still matter? Am I still me?"
- Two drivers of existential distress: self-discontinuity + loss of personal autonomy
- Patients want to affirm aspects of their lives unrelated to illness
- Ditto's role: the patient is the author of their care story, not a passive recipient

### Emotional promises per pillar

| Pillar | Functional promise | Existential promise |
|---|---|---|
| **Clarity** | You understand what's happening | You're not lost in your own care journey |
| **Convenience** | You're prepared for what's next | You're in the driver's seat, not a passenger |
| **Connection** | Your people are informed and can help | You're not carrying this alone — and they're not helpless |

### Overarching statement

> Ditto helps you face your care journey as yourself — informed, prepared, and surrounded by people who understand.

Or compressed: **Understand. Prepare. Share.**

---

## Three Workstreams

| # | Workstream | What it solves | Pillar | Horizon |
|---|---|---|---|---|
| **1** | Fix the funnel for cancer patients | Right people still don't activate — diagnose and remove blockers | Clarity | Now (weeks) |
| **2** | Deepen the cancer journey | Beyond recording: letters, symptoms, journey overview, appointment prep | Convenience | Next (months) |
| **3** | Make sharing effortless and valuable | Care Circle as distribution + emotional support layer | Connection | Parallel with CC v2 |

---

## Decision Tree: Why People Don't Activate

Diagnostic tree for understanding drop-off (from Merlijn's draft):

```
Inflow ──> Activation funnel ──> Has appointment?
  |                                    |
  "Who are these people?"         ┌────┼──────────────────┐
  (life moment? channel?)         |    |                  |
                                  v    v                  v
                              Yes   Unknown            No
                               |      |                 |
                               v      v                 v
                          Planned   "How to know?" -> Follow-up via
                          in Ditto?  Customer.io +     Customer.io for
                               |     Typeform          upcoming appt
                               v
                          Actually recorded?
                           |            |
                           v            v
                          Yes          No -> "Why not?"
                           |           (fear? forgot? friction?)
                           v
                      Follow-up appt     DO: Calendar integration
                      planned?           with deeplink to record
                           |
                           v
                      Care Circle activation
                           |
                           v
                      Follow/following request sent?
                           |            |
                           v            v
                          Yes          No -> "Why not?"
```

### Missing branch: "No appointment" path

Currently the tree dead-ends into "follow up later." Needs an alternative value path — what can Ditto give this person right now? (Voice profile, letter explanation, appointment prep, content)

---

## Existing Ideas (Activation-Relevant)

Cross-referenced from idea board and prior work:

| Idea | Status | Activation relevance |
|---|---|---|
| Voice-first profile building ("Speak to Ditto") | Draft — strong energy | Removes timing dependency; demonstrates AI immediately |
| Smart appointment questions | Discussed in meetings | Pre-appointment value; end-of-conversation Q&A |
| Care Circle timing A/B | Proposed experiment | Tests follower-first vs appointment-first |
| Ditto Chat (contextual AI) | New — not yet on board | Guided capabilities, pinnable components |
| Health integrations (Apple Health) | Built (Apple), planned (Google) | Signal layer — interpretation of health data |
| Intent question in onboarding | BIGB-2190, designed | Segments users by intent at entry |
| Calendar integration with deeplink | On decision tree | Bridges planned → actually recorded |
| Recording permission support | Draft, RISCE 540 | Reduces fear barrier for elderly |
| "Understand your letter" | From Onboarding-to-Aha spec | Micro-value between appointments |

---

## Open Questions (to resolve in next phase)

1. What's the actual split between "has appointment soon" vs "no appointment" among new users?
2. What specific blockers prevent cancer patients who HAVE appointments from recording?
3. If acquisition targets cancer patients specifically, does the "no appointment" problem mostly disappear?
4. What's the minimum viable "between appointments" value that creates a reason to return?
5. How does the existential layer (identity, agency) translate into concrete product decisions?

---

## Sources

- [The Psychosocial Needs of Cancer Patients - NCBI](https://www.ncbi.nlm.nih.gov/books/NBK4011/)
- [Existential Suffering in Palliative Care - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8471755/)
- [Kindness, Listening, and Connection - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9008851/)
- [Cancer patients' sense of coherence - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11604166/)
- [Addressing Patient Emotional and Existential Needs - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0885392417303329)
- [Global unmet psychosocial needs in cancer care - The Lancet](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00521-2/fulltext)
- [Health Literacy and Cancer Outcomes](https://ace.amegroups.org/article/view/6259/html)
- [Emotional indicators in healthcare management - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9854301/)
