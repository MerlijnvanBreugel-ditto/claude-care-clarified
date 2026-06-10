# MAU Gap Strategy — Merlijn's Notes
*Working document. Prepared May 21, 2026 following founders meeting.*
*Status: IN PROGRESS — will be extended.*

---

## What the document gets right

- The funnel gap data (55% appointment→summary, 72% summary→2nd) is credible and gives us real anchors for the conversation.
- The sequencing logic ("fix the bucket before you pour") is correct. Spending on acquisition now is wasteful given current activation rates.
- The park-international recommendation is directionally right.
- The KR-by-KR analysis is a good forcing function for the team.

---

## Observations & Concerns

### On the 55% appointment→summary gap
We don't know what intent actually looks like in this population. Possible explanations we can't yet distinguish:
- User tested the product with a past or fake appointment
- It was someone else's appointment (e.g., a reminder for a partner)
- Appointment was at the dentist or another setting where recording isn't appropriate
- They weren't allowed to record (e.g., specialist explicitly said no)
- They genuinely forgot or didn't activate in time

**Implication:** Before we build solutions (calendar sync, reminders), we need to know which of these is actually happening. Intent-mismatch is a fundamentally different problem than friction-mismatch.

### On the 50K target
The target is investor-committed. It's not something we can just reframe internally. We need to be honest about the path required and what it would take to get there — but the target itself stays.

### On the growth stagnation model
The "70% effective retention" figure deserves scrutiny. M1 cohort retention is closer to 40%, not 37% as stated for creation. The 70% effective retention is a blended number that mixes cohort stacking and reactivation, which can mask what's actually happening at the user level. We should be careful about using this as an input to the growth model — it could make things look more stable than they are.

### On the care circle k-factor (k=0.35)
Skeptical that this is real organic virality. We are actively pushing invites during onboarding/activation, which inflates the number. The questions we still need to answer:
- Do followers who get added actually return and view summaries?
- Do followers ever invite *other* people (second-order compounding)?
- Is there any evidence of organic k — invites sent without in-app prompting?

Until we can answer these, the viral loop assumption in the model is speculative.

### On care circle as a retention/growth strategy
Even if we get the CC invite funnel working (28% → 60%), it doesn't matter if patient retention stays at 28% M1. Followers come back to see new summaries. If patients stop creating, followers have no reason to return. **Patient retention is the prerequisite, not care circle.** Care circle amplifies a working retention loop; it doesn't create one.

### On the broader product hypothesis
We may be too focused on growth mechanics while ignoring a more fundamental question: are we attracting the right people, and is the core product valuable enough to retain them? Even with virality, if we're acquiring the wrong users, we're compounding the wrong thing.

The Uber analogy is relevant here: I rarely take a cab, but when I do, I immediately open Uber. The app earns its place on the phone through reliability at the moment of need, not through daily engagement. **Is Ditto's value proposition strong enough that users will reach for it at their healthcare moments, even if those moments are rare?** We don't know yet whether low retention is a frequency problem (no appointments) or a value problem (the product didn't deliver enough).

### On TAM and narrow targeting
110,000 new cancer patients per year in the Netherlands is not a small number. If we target narrow (oncology, pregnancy, chronic illness), the addressable group is significant. The real question is: does narrow targeting give us high-quality users who activate and retain at much better rates? A cancer-branded acquisition campaign might cost more per install but deliver substantially higher quality. We need to test this hypothesis, not assume it.

---

## Ideas

### Influencer / Role Model Strategy (Substack-like)
What ignited Substack was getting writers people genuinely looked up to onto the platform. A parallel for Ditto: partner with people who are publicly open about their health journey (e.g., health influencers on Instagram/TikTok dealing with chronic illness, cancer). Create a version of their care journey in a shareable format — an ongoing, visual care narrative that people can follow. This goes more toward the social/peer support direction and requires a significant UX shift, but it could create a content-driven pull that the current product lacks.

**Prerequisite:** this only works if we're willing to go all-in on social and visual content. It's a strategic bet, not a feature.

### Personalized Invite Card
The current invite link is plain text. It should be a personalized visual card: "Follow my care journey" or "I want to follow [Name]'s health story." Something shareable that conveys warmth and context, not just a URL. This is relatively low-hanging fruit and could lift invite→install conversion meaningfully.

### Invite Tracking via Contact-Based Invites
Currently, we can't track who received an invite if we use phone number verification. If patients invite from their contacts, we can track invite→accept and see who specifically didn't convert. This data is currently invisible to us and would unlock a lot. Worth scoping as a small feature.

---

## Open Research Questions

### Virality in low-frequency, small-network products
Ditto is fundamentally different from Facebook or Slack:
- Network ceiling is ~5-10 people per user (care circle), not hundreds
- Engagement frequency is low (tied to appointments)
- Value doesn't grow exponentially with more connections

**Research ask:** How does virality actually work in low-frequency, finite-network products? What is the "atomic unit" that makes a small network valuable? Are there products where this has worked, and how did they approach it? Look at Lenny's newsletter, Reforge, academic work on network effects in constrained graphs. Report back with a short synthesis and implications for Ditto.

### Comparable product cases
Are there successful consumer health or low-frequency apps that solved retention without daily engagement hooks? How did they maintain top-of-mind awareness? What made users return at the moment of need rather than abandoning the app?

**Research ask:** Find 3-5 comparable cases. For each: what was the use frequency, what was the core retention mechanic, what did they do that Ditto could learn from? Focus on products that are "always there when you need them" rather than daily drivers.

### Quality-adjusted acquisition analysis
We need to understand whether targeted acquisition (e.g., oncology-specific campaigns) outperforms broad acquisition on LTV-adjusted metrics, not just install cost. A higher CPR on a cancer-branded Facebook campaign might be worth it if D14 activation is 2-3x higher.

**Research ask:** Can we pull cohort data by acquisition channel and compare D14 activation rates? If we don't have clean channel attribution, what would it cost to run a small test?

---

## Analytical Model Request

Build a growth model that is more granular than the current one. It should include:

1. **Inflow segmentation** — split new users into "high-quality" (appointment-ready, right intent) and "low-quality" (curious, wrong context, no appointments near-term)
2. **Differentiated activation** — high-quality and low-quality users activate at different rates
3. **Differentiated retention** — same split applied to M1, M2+ retention
4. **Care circle multiplier** — applied only to activated, retained patients (not to all installs)
5. **Levers to model:**
   - What happens if we increase total inflow volume?
   - What happens if we improve inflow *quality* (shift mix toward high-quality)?
   - What happens if we improve activation rate within each group?
   - What happens if we improve retention?
   - Interaction effects between all of the above

This will help us answer the question: is it better to acquire more users at current quality, or fewer users at higher quality?

---

## Engineering & Team

- **Proposal on table:** Hire 1 junior + 1 senior engineer (Iman-equivalent). Juri steps back to a few hours/week. Iman confirmed this gives us good coverage for the next year unless we hit hyperscaling or certification requirements (MDR).
- **Immediate action:** Align with Iman today on bringing in an additional mobile dev for 3 months. Push to start ASAP. Explore 1-2 mobile devs in-office if needed.
- **Patrick:** As engineering team grows, likely stop working with Patrick from a broker/manager perspective. Larger team will eventually need a subteam structure.
- **Merlijn's bandwidth:** Needs to substantially free up time to focus on product. This is blocked by engineering capacity; solving the engineering bottleneck unlocks product focus.
- **Hiring pool:** Canada is a viable talent pool worth exploring.

---

## Budget Reality Check

The €1.53M scenario in the document is not realistic given current funding. It also doesn't account for international expansion or what we need heading into next year. We need to agree on a realistic cost curve as a meeting output, not model a scenario we can't afford.

---

## Follow-Up Actions

| Action | Owner | Deadline |
|---|---|---|
| Research: virality in low-frequency / finite-network products | Mewtwo | This week |
| Research: comparable product cases (retention without daily engagement) | Mewtwo | This week |
| Build quality-adjusted growth model with high/low user segments | Mewtwo | Next week |
| Investigate: pull D14 activation rates by acquisition channel | Niek / Mewtwo | This week |
| Scoping: personalized invite card (visual, shareable) | Ilayda | Next sprint |
| Scoping: contact-based invite tracking | Engineering | Backlog |
| Agree on partnership prove-it deadline (what, by when, consequence) | Bart + founders | Today |
| Align Iman on mobile dev hire | Merlijn | Today |
| Qualitative research: 10-15 churn interviews | [TBD] | ASAP |

---

*Last updated: May 21, 2026*
