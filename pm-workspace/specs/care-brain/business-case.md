# Care Brain: Business Case

**Date**: 2026-04-05
**Status**: Internal draft
**Author**: Mewtwo (PM Co-Pilot)

---

## Executive Summary

Ditto Care's current product (medical conversation summarization) is commoditizing. Epic, Ambience, and every major EHR vendor now offer ambient summarization. Big Tech (OpenAI, Microsoft) has entered consumer health AI. Staying "the summarization app" leads to slow irrelevance.

The Care Brain transforms Ditto from a single-feature tool into a care intelligence platform. The AI becomes the brain of the product, powering every interaction: understanding conversations, building health profiles, answering questions, and distributing contextual understanding across care circles.

The defensible moat is not the AI (that commoditizes). It's the Care Graph: the map of who cares about whom, what they need to know, and how they coordinate. No one else is building this.

---

## The Problem We're Solving

### For patients

When healthcare gets serious, people are lost, overwhelmed, and alone.

| Pain | Frequency | Intensity | Current workaround |
|---|---|---|---|
| Can't remember what doctor said | Every appointment | High | Notes on phone, ask family member who was there |
| Don't understand medical terms in MY context | Every appointment | High | Google (generic, often alarming) |
| Questions arise after leaving the office | Days after appointment | Very high | Wait for next visit, call GP (slow), ask ChatGPT (no context) |
| Need to tell 5 people what happened | After every appointment | Moderate | Phone calls, WhatsApp group, retelling the same thing |
| Each family member needs different level of detail | Ongoing | Moderate | Manually adapt each message |
| Forget what to ask at next appointment | Before appointments | High | Scribbled notes, usually forgotten |
| Don't know what changed between appointments | Over time | Medium | No longitudinal view exists |

### For care circles

The people around the patient carry an invisible burden: they need to understand what's happening, coordinate care, and provide support, but they have no tool designed for this. They piece together information from phone calls, forwarded messages, and Google searches.

### For the healthcare system

Informed patients have better outcomes, fewer unnecessary follow-up calls, higher treatment adherence, and lower readmission rates. Insurers and hospitals benefit when patients and their circles understand what's happening.

---

## Market Sizing

### EU Total Addressable Market

| Segment | Patients | Circle (3-5x) | EU total |
|---|---|---|---|
| Cancer (active treatment) | ~5M | ~20M | ~25M |
| Chronic condition escalation | ~50M | ~150M | ~200M |
| Cognitive decline + family | ~10M | ~50M | ~60M |
| Serious acute events/year | ~15M | ~50M | ~65M |
| New parents (first 18 months) | ~10M | ~30M | ~40M |

**Conservative overlap-adjusted total: 80-100M patients + 250-400M circle members at any given time across the EU.**

### Netherlands (launch market)

| Segment | Patients | Circle | Total |
|---|---|---|---|
| Cancer (new diagnoses/year) | ~120K | ~480K | ~600K |
| Chronic conditions (escalation) | ~500K | ~1.5M | ~2M |
| Menzis members (partnership) | ~2M members | -- | ~2M addressable |

### Revenue model scenarios

**Scenario A: B2C Subscription (freemium)**

| Tier | Price | Features | Conversion target |
|---|---|---|---|
| Free | 0 | Record + summarize (limited/month) | 100% of users |
| Premium | EUR 7.99/month | Unlimited summaries, Q&A, health profile, full circle sharing, appointment prep | 5-10% of active users |
| Family | EUR 12.99/month | Premium + multi-patient (follow multiple journeys) | 2-5% of circle members |

Revenue at scale:

| Users (active) | Premium conversion | Revenue/month | ARR |
|---|---|---|---|
| 50K | 7% | EUR 28K | EUR 336K |
| 200K | 8% | EUR 128K | EUR 1.5M |
| 1M | 10% | EUR 800K | EUR 9.6M |
| 5M | 10% | EUR 4M | EUR 48M |

**Scenario B: B2B2C (insurer partnerships)**

Insurers pay per-member-per-month for access.

| Insurer deal | Members | PMPM | Revenue/month | ARR |
|---|---|---|---|---|
| Menzis (NL) | 2M | EUR 0.50 | EUR 1M | EUR 12M |
| 3 EU insurers | 15M | EUR 0.75 | EUR 11.25M | EUR 135M |
| 10 EU insurers | 50M | EUR 1.00 | EUR 50M | EUR 600M |

**Scenario C: Blended (most likely)**

B2C for organic users + B2B2C for insurer channels.

| Phase | Timeline | Users | Revenue mix | ARR |
|---|---|---|---|---|
| **Phase 1**: NL focus | Now - 12 months | 50-100K | 80% B2B2C (Menzis), 20% B2C | EUR 1-3M |
| **Phase 2**: 3 EU markets | 12-36 months | 500K-1M | 60% B2B2C, 40% B2C | EUR 10-25M |
| **Phase 3**: EU-wide | 36-60 months | 5-10M | 50% B2B2C, 50% B2C | EUR 50-100M |

### Path to unicorn valuation

At 10-20x ARR (standard for high-growth health-tech SaaS):
- EUR 50M ARR = EUR 500M-1B valuation
- EUR 100M ARR = EUR 1-2B valuation
- Achievable in Phase 3 (year 4-5) with successful EU expansion

---

## Cost Structure

### AI costs (Care Brain operations)

Based on current Claude/GPT API pricing (April 2026, costs declining 40-80% annually):

| Operation | Input tokens | Output tokens | Cost/call | Frequency |
|---|---|---|---|---|
| Summarize conversation | ~15K | ~2K | ~$0.02 | 1x per recording |
| Extract health data | ~15K | ~1K | ~$0.015 | 1x per recording |
| Generate suggestions | ~3K | ~300 | ~$0.004 | 1x per summary |
| Answer question | ~8K | ~500 | ~$0.01 | ~2x per summary view |
| Adapt for circle member | ~3K | ~500 | ~$0.005 | ~3x per summary shared |
| Appointment prep | ~10K | ~1K | ~$0.015 | 1x per upcoming appointment |

**Full "brain processing" per recording**: ~$0.07

**Monthly AI cost by scale:**

| Active users | Recordings/month | Q&A interactions | Circle adaptations | Monthly AI cost |
|---|---|---|---|---|
| 5K | 3K | 6K | 5K | ~$500 |
| 50K | 25K | 50K | 40K | ~$4,500 |
| 500K | 200K | 400K | 300K | ~$40,000 |

AI costs are negligible relative to revenue at every scale. Even at 500K users, AI costs are ~$40K/month against projected ARR of $10M+. **AI cost is not a constraint.**

### Cost decline trajectory

AI API costs have dropped 40-80% annually. By 2027, current costs will be roughly halved. By 2028, they'll be a quarter. The economics only improve.

### Infrastructure costs

| Component | Monthly cost (est.) |
|---|---|
| Cloud hosting (app + API) | EUR 2-5K (current), EUR 10-20K (500K users) |
| AI API calls | EUR 500 (current), EUR 40K (500K users) |
| Database | EUR 500 (current), EUR 3-5K (500K users) |
| Monitoring/observability | EUR 200-500 |
| STT (voice input) | EUR 100 (current), EUR 5K (500K users) |

**Total infrastructure at 500K users: ~EUR 60-70K/month.** Well within margins for a SaaS product with premium pricing.

---

## The Moat (Why We Win)

Listed by strength:

| Moat layer | What it is | Switching cost | Time to replicate |
|---|---|---|---|
| **Care Graph** | Map of who cares about whom, what they need, how they coordinate | Very high (can't export family care coordination) | 2-3 years |
| **Journey History** | Longitudinal record across providers, months, years | Very high (accumulated context can't be recreated) | Equal to patient's care duration |
| **Trust** | Earned during most vulnerable health moments | Extreme (won't switch mid-cancer-treatment) | Years |
| **Regulatory Navigation** | GDPR + AI Act + MDR compliance across EU markets | High (compliance cost IS the barrier) | 1-2 years per market |
| **Network Density** | Each patient brings 3-7 circle members | Increasing with density | Requires care graph |
| **EHDS Readiness** | First consumer app to ingest portable health data | Medium-high | Regulatory timeline |

### Why Big Tech can't replicate this easily

1. **They build for individuals.** The care graph is fundamentally multi-user with asymmetric information needs. Apple Health+ is "me and my health." Ditto is "us and our health journey."

2. **They optimize for engagement.** Ditto optimizes for reducing burden. The best outcome is the circle member who DOESN'T need to open the app because they already know what's happening.

3. **They can't build trust at the bedside.** Trust in healthcare is earned through specificity, not capability. A general-purpose AI that also helps you plan dinner doesn't earn the same trust as the app that helped you understand your cancer diagnosis.

4. **Healthcare is deeply local.** Dutch medical terminology, German insurance structures, French patient rights. Big Tech builds globally; Ditto builds specifically. Specificity builds trust.

---

## Competitive Position (April 2026)

### Direct threats

| Competitor | What they do | Threat to Ditto | Our advantage |
|---|---|---|---|
| **ChatGPT Health** | Personal health Q&A with medical record integration | High (could add summarization) | No care circle, no care graph, no audience adaptation. Individual-only. |
| **Microsoft Copilot Health** | Health record aggregation + AI insights | Medium (US-focused, enterprise) | Not consumer-first, not European, no care coordination |
| **Apple Health AI** | Wearable data + wellness coaching (scaled back) | Low (retreated from full launch) | Ditto is care-journey-focused, not wellness |
| **Ambience Healthcare** | Ambient clinical documentation for providers | Low (provider-facing, not patient) | Different audience entirely |

### Structural advantages

| Factor | Ditto | Big Tech | Other startups |
|---|---|---|---|
| Care circle / social layer | Core product | None have it | CaringBridge (blog, not AI) |
| Audience-adapted sharing | Yes (in plan) | No | No one |
| European / EHDS-ready | Yes (EU-first) | US-first | Few EU startups |
| Patient trust | Earned at bedside | General-purpose trust | Varies |
| Insurer distribution | Menzis (2M) | None | Varies |
| Regulatory compliance | GDPR + AI Act native | Adapting from US | Varies |

### Validated unique position

**No one is building audience-adapted health sharing for care circles.** This is Ditto's claimed differentiation. Market research confirms:
- Big Tech builds individual health AI
- CaringBridge does broadcast (one post to everyone), not adapted sharing
- Lotsa Helping Hands does logistics, not understanding
- Patient portals are provider-centric, not patient-family-centric

The gap is real. The question is execution speed.

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **Summarization becomes free/commodity** | Near-certain | High | Already happening. Pivot to care intelligence is the mitigation. This business case IS the response. |
| **Big Tech adds care circle features** | Low-medium (2-3 year window) | Very high | Speed. Build the care graph before they realize it matters. Regulatory moat slows them in EU. |
| **Care graph doesn't create real switching costs** | Medium | High | Journey history is the sticky layer. 18 months of cancer context can't be recreated. Validate with CC V2 retention data. |
| **Insurer sales cycles too slow** | Medium-high | Medium | Menzis proof case. B2C growth creates pull ("your members already use this"). |
| **AI quality issues damage trust** | Medium | Very high | Fix current 95% regression. Invest in eval infrastructure before scaling. One bad medical answer = permanent trust loss. |
| **GDPR enforcement on health AI** | Low-medium | Medium | Already EU-first with proper DPAs. Compliance posture is an advantage, not a risk. |
| **10-person team can't build this fast enough** | Medium-high | High | Focus. Phase 1 (Smart Suggestions) needs 2-3 engineers for 5 weeks. Don't try to build everything. |
| **Users don't engage with Q&A/suggestions** | Medium | Medium | Validate with offline quality test (50 summaries) before building. A/B test before full rollout. |

---

## Investment Thesis (For Fundraising)

### The one-liner

Ditto is building the consumer layer for healthcare in Europe: the care graph that connects patients and families through serious health journeys, powered by AI that transforms raw health moments into shared understanding.

### Why now

1. **AI costs collapsed.** What was impossible 18 months ago is now $0.07 per interaction.
2. **EHDS creates the regulatory tailwind.** Patient-portable health data across the EU by 2029. First elements in Fall 2026.
3. **Big Tech entered but chose the wrong surface area.** They're building for individuals. Nobody is building the social layer of care.
4. **Apple retreated.** Health+ AI Coach scaled back in Feb 2026. The field is more open than expected.
5. **Summarization proved the wedge.** 35K users, 50 circle invitations/day, Menzis partnership. The product has pull.

### Key milestones for next 12 months

| Milestone | Target | Why it matters |
|---|---|---|
| Care Brain Phase 1 shipped (Smart Suggestions) | Q2 2026 | Proves "brain" concept. Drives frequency. |
| 20%+ suggestion engagement rate | Q3 2026 | Validates demand for contextual Q&A |
| Living Health Profile shipped | Q3 2026 | Creates switching costs. Foundation for everything. |
| CNIS at 40%+ (circle engagement) | Q4 2026 | Proves care graph network effects |
| 100K active users (patients + circle) | Q4 2026 | Scale milestone for Series A narrative |
| Voice input shipped | Q4 2026 | Bridges activation gap. Positions for voice-first market. |
| First non-NL market pilot | Q1 2027 | Proves cross-market viability |

### Ask

Series A: EUR 5-10M to fund:
- Engineering team expansion (10 → 20) for Care Brain build-out
- First EU market expansion (Germany or Belgium)
- EHDS integration infrastructure
- Insurer partnership development (2-3 additional insurers)

### Return profile

- Year 3: EUR 10-25M ARR across 3 EU markets
- Year 5: EUR 50-100M ARR across 10+ EU markets
- Unicorn valuation: 10-20x ARR at Phase 3

---

## Persona Critiques (Self-Review)

### The Skeptical VC

"Your numbers look nice but they're projections, not evidence. Show me: (1) What's the actual CC V2 invitation-to-activation conversion rate? 50 invitations/day means nothing if they don't onboard. (2) What's retention after 90 days? If patients stop using after their treatment ends, your LTV model breaks. (3) Why EUR 0.50-1.00 PMPM for insurers? What's the evidence they'll pay that? Menzis is a proof-of-concept, not a price point."

**Response**: Fair. The business case is built on leading indicators, not trailing revenue. The 50 invitations/day is new (CC V2 soft launch). We need 2-3 months of data on circle activation rates and retention. The insurer pricing is based on comparable health app PMPM in NL/EU (range EUR 0.30-2.00). Menzis deal terms are the anchor.

### The CTO

"Your cost model assumes current API pricing. But you're planning to use Opus for Q&A and long-context reasoning. At scale, that's not $0.01 per answer, it's $0.05-0.10 with full journey context. Also, your 'model-agnostic' claim is aspirational. In practice, each model has different tool use formats, streaming behaviors, and quality characteristics. Swapping models is a week of work per task, not a config change."

**Response**: Correct on both counts. Cost model should use Opus pricing for Q&A ($15/M input, $75/M output) which roughly 5x the estimate. Still manageable at scale (EUR 200K/year at 500K users), but worth tracking. Model abstraction layer needs to be a real engineering investment, not a hand-wave. Prompt caching helps significantly (up to 90% reduction for repeated system prompts + profile context).

### The Chief Medical Officer

"You say 'never provide medical advice' but a patient who asks 'Should I be worried about this test result?' and gets a detailed contextual answer WILL treat it as medical advice, regardless of your disclaimer. The disclaimer is a legal fig leaf, not a safety mechanism. What's your actual plan for when a patient makes a medical decision based on a Care Brain answer that turns out to be wrong?"

**Response**: This is the hardest risk in the entire plan. The mitigation layers are: (1) grounding in conversation data only (answer what the doctor said, not what medicine says), (2) source attribution on every answer, (3) disclaimers, (4) UX design that frames answers as "understanding what was discussed" not "medical guidance", (5) never answer questions that require new medical knowledge not present in the conversation. But the CMO is right that users will overshoot. The insurance against catastrophic failure is: never fill gaps with general medical knowledge. If the conversation doesn't contain the answer, say "This wasn't discussed in your appointment. Ask your doctor at your next visit."

### The 60-Year-Old Cancer Patient

"I don't understand what 'Care Brain' means. I just want to know what the doctor said and be able to show my daughter. Don't make this complicated. And please don't change the summary screen. I finally figured out how it works."

**Response**: The patient should never hear "Care Brain." They should see: suggestions below their summary that answer their unspoken questions. A health overview that updates automatically. Updates for their daughter that they can send with one tap. Everything feels like "Ditto got smarter," not "Ditto added AI features." The summary screen doesn't change. It gets better.
