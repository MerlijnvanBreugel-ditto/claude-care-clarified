# Long-Term Product Vision — Ditto Care

> **Built**: 2026-06-03 by Mewtwo, with Merlijn.
> **Status**: Exploratory synthesis. Five product × strategy × monetization routes + a recommendation. This is a thinking artifact, not a committed strategy. The committed strategy today is [`care-brain-one-pager`](../../specs/care-brain/care-brain-one-pager.md); this doc reframes the question and should either supersede it or be folded into it once a route is chosen.
> **How to read**: This file is the synthesis and the bet. The [`sources/`](./sources/) folder distills each evidence base it rests on. None of the source files are copies; each is a decision-relevant condensation with pointers back to the originals.

---

## The through-line

The patient-friendly summary, Ditto's core product, is commoditizing from every direction and will be a free byproduct of NL/BE portals around 2027-28. The defensible ground is no longer the artifact or the AI. It is some combination of the **patient + family relationship (care graph)**, **EU-native trust and consent**, **oncology depth**, and the **patient-owned, cross-provider longitudinal record**. Demand for the job is validated and large. Two constraints bind any durable version of Ditto: it is **too low-frequency** (episodic, appointment-gated) and its **monetization leans on reimbursement** that is slow, uncertain, and evidence-gated. The long-term prize is a product that taps a daily, high-intensity need, locks people in through accumulated context and relationships, monetizes directly (not only via insurers), and scales fast. This doc lays out five distinct ways to get there and recommends one.

---

## The strategic situation (condensed; full evidence in `sources/`)

| Force | What it means for the vision | Source |
|---|---|---|
| **Summary commoditizing** | Portals (ChipSoft, ZAS live), Epic Emmie (2026-27), scribes (Abridge already ships a patient app), German B2C translators (Simply Onno), and all three foundation-model labs (Jan 2026) now do "explain my visit." Standard-of-care in portals ~2027-28. | [01-market](./sources/01-market-and-competitive-landscape.md) |
| **Demand validated & large** | Recall/literacy crisis, caregiver economy (NL 1.9M carers), ~32% of NL adults already used AI for a health question. The job is real and mainstream. | [01-market](./sources/01-market-and-competitive-landscape.md), [05-tam](./sources/05-market-sizing-and-tam.md) |
| **Frequency is the core wound** | Episodic appointment-gated use sits in the "Forgettable Zone." Escape routes: own the unavoidable event, latch onto a daily behavior, or add between-visit utility. | [02-growth](./sources/02-growth-and-retention-diagnosis.md) |
| **Retention > virality (the data)** | Funnel model: retention has ~1.5x the MAU leverage of any other lever; care-circle K ≈ 0.012 is tiny; the viral graph is unproven (0.14% daily share, ~1.4 circle members). | [02-growth](./sources/02-growth-and-retention-diagnosis.md) |
| **Moat must shift** | Relationship/care graph, EU-native trust (OpenEvidence exited EU/UK over the AI Act, vacating regulated high ground), oncology depth, patient-owned cross-provider data. | [01-market](./sources/01-market-and-competitive-landscape.md), [03-carebrain](./sources/03-care-brain-vision-corpus.md) |
| **Investors are skeptical of the summary** | DD calls: pick a tight wedge, build a habit/"so-what" layer, summaries are not a business, insurers buy outcomes not summaries, pharma pays only for adherence + advertising. | [06-dd](./sources/06-investor-and-dd-signals.md) |

---

## The design lens

The two binding constraints (frequency, reimbursement-independent monetization) are the design axes. Each route below is built as:

**a distinct frequency engine** (why someone opens Ditto with no appointment today) **×** **a monetization engine where reimbursement is upside, never the spine.**

A precondition sits under all five: the retention curve has to be fixed first. A frequency engine on a leaky bucket burns money faster. See [`02-growth`](./sources/02-growth-and-retention-diagnosis.md).

---

## The five routes

### Route A — The Caregiver Command Center
- **Thesis**: Build for the caregiver (the daughter managing her mother's cancer), not the patient. The caregiver is the daily-active user, the willing buyer, the coordinator. The patient is the data source.
- **Product**: Shared command center for a care journey: recorded-visit comprehension + medication + appointments + symptom log + family circle + task coordination, with AI doing adapted updates and the "what changed / what's next" briefing.
- **Frequency engine**: Caregiving is the highest-frequency relationship in healthcare. Years, not visits.
- **Monetization (non-reimbursement-first)**: Caregiver/family subscription (€9-13/mo). Reimbursement is a free distribution topper (Hello 24/7 proves NL insurers reimburse a €5.83/mo caregiver app 100%). Employer caregiving benefit (B2B2B) is the third leg.
- **Lock-in & scale**: Accumulated journey + the whole family on one graph. Rides the caregiver-economy boom.
- **Must be true**: Caregivers will pay, and the AI comprehension layer is a real wedge over Carenzorgt / Hello 24/7 (who own coordination but not the AI).

### Route B — The Proactive Care Agent
- **Thesis**: Ditto stops waiting to be opened and starts doing things. Voice in, agentic follow-through out. The 2031 vision pulled forward.
- **Product**: Proactive companion: voice capture between visits, then the agent drafts questions, sets reminders, preps the next visit, catches cross-doctor interactions, generates family updates. Moat = longitudinal memory + follow-through + permission to act.
- **Frequency engine**: Proactivity. The product initiates contact, so frequency is not gated by appointments.
- **Monetization**: B2C premium for the agentic tier (Google Health Coach validates $9.99/mo for proactive coaching) + B2B2C insurer on outcomes (fewer repeat visits / no-shows, better adherence).
- **Lock-in & scale**: The agent that knows your full context and acts on it.
- **Must be true**: You can stay on the safe side of the Class IIa / AI-Act-high-risk line while being genuinely agentic, and survive operating in ChatGPT's busiest room. One hallucinated action is existential. This route lives or dies on trust engineering.

### Route C — The Treatment Companion + Real-World-Data Engine
- **Thesis**: Pick the window where frequency is already high (active treatment), nail self-monitoring, and turn the resulting structured oncology dataset into a second business that never touches reimbursement.
- **Product**: Daily symptom/side-effect + medication tracking during active treatment, anchored by the recorded visit and wrapped in comprehension + care circle. Self-monitoring is the strongest retention lever in the literature (~80% vs ~60% retained at 40 weeks).
- **Frequency engine**: Daily symptom logging during treatment. Oncology-on-treatment is weekly-to-daily, not episodic.
- **Monetization (two engines, neither reimbursement)**: (1) patient/caregiver premium; (2) consent-first oncology RWD to pharma/research + trial-matching fees. Validated by Vinehealth→Sciensus, Belong←IQVIA, Ada←Bayer; Novartis named adherence + trial-matching as what pharma reliably funds.
- **Lock-in & scale**: Longitudinal structured data + the tracking habit. The data asset compounds and is uncopiable.
- **Must be true**: The comprehension + circle bundle keeps you a company, not a feature (tracking-only got Vinehealth acqui-hired). Patient revenue stands alone before RWD, which is slow and churny.

### Route D — The Verified Care Record (trust + consent + grounding layer)
- **Thesis**: Be the patient-owned, verified, EU-native record that grounds AI, in a regulated market the best-funded clarity player just abandoned.
- **Product**: Cross-provider, patient-owned care record + consent broker. "Bring your verified care record to any AI or service." Interoperate with MedMij/PGO rather than wall off. As EHDS lands, you are the consumer-facing consent + grounding layer.
- **Frequency engine**: Lower direct frequency; you are queried often (every time any AI or service needs trusted patient context). Frequency-by-being-infrastructure.
- **Monetization**: Consumer premium + B2B connectivity/API fees for verified, consented EU patient context (the b.well "bailey" model that OpenAI and Samsung already pay for) + hospital/insurer licensing.
- **Lock-in & scale**: Data gravity + being the consent broker in the EHDS era. Structural and durable.
- **Must be true**: You reach it before PGOs (Quli/Ivido) bolt an AI layer onto the record they already own with government distribution, and a small team can run a platform play. Slowest to revenue (EHDS is 2029).

### Route E — The Family Health Network ("Polarsteps for health")
- **Thesis**: Make the relationship layer the product, not a share button. The viral loop is the business. The brand's stated ambition, made explicit.
- **Product**: A living, multi-patient family health space. Members follow journeys, contribute (daughter adds the lab result, partner logs the pharmacy run), react, coordinate. The Family Dashboard turns recipients into daily-actives. Cross-journey: the member following dad's cancer later starts her own pregnancy journey.
- **Frequency engine**: The network. Circle members check on a loved one daily even when the patient is episodic.
- **Monetization**: Freemium B2C at scale (Spotify-shaped) + B2B2C insurer once dense. Density drives near-zero CAC and fast scale.
- **Lock-in & scale**: The whole family on one platform; highest scale ceiling of the five.
- **Must be true**: The graph actually compounds. This is the exact thesis your own data contradicts today (0.14% daily share, ~1.4 members vs the 3-5 a real network needs). Highest ceiling, least evidence. Validate cheaply before betting the company.

---

## Comparison

| Route | Frequency | Monetization strength | Reimb-independent | Lock-in | Time to revenue | Fit w/ assets | Evidence it works |
|---|---|---|---|---|---|---|---|
| **A. Caregiver OS** | High (daily care) | Strong (caregivers pay) | Yes | High | Fast | High | Hello 24/7 |
| **B. Proactive Agent** | Med-high | Medium | Yes | Medium | Medium | Medium | Health Coach $ point |
| **C. Treatment Companion + RWD** | High (on-treatment) | Strong (2 engines) | Yes | High (data) | Medium | High (oncology) | Vinehealth / Belong / Ada |
| **D. Verified Care Record** | Low-direct | Medium (API) | Yes | Very high | Slow | Medium | b.well bailey |
| **E. Family Network** | If dashboard works | Freemium-at-scale | Yes | Very high | Slow (needs density) | High (care circle) | Contradicted by own data |

---

## Recommendation

Against the stated criteria (high frequency, strong non-reimbursement monetization, big need, fast scale), **A and C score highest, and they compose.** The sharpest single move is a hybrid:

> **Serve a high-frequency primary user (the caregiver, Route A) in a high-frequency window (active treatment, Route C). They pay directly. Structured oncology RWD is the second engine. Insurer reimbursement is the distribution topper. Nothing depends on reimbursement to survive.**

The hybrid satisfies all five criteria without betting the company on the one thesis the data contradicts (E) or on a 2029 regulatory timeline (D).

The other three, positioned honestly:
- **E** is the current implicit strategy and the highest ceiling, but faith-based today. Treat it as a thesis to prove cheaply (does a Family Dashboard make circle members daily-active?) before resourcing it as the spine.
- **B** is the purest AI-trend ride and the most fragile (lab exposure, regulation, trust). Better as a capability layer inside A or C than a standalone route.
- **D** is the most defensible in 2029 and the weakest in 2026. An "earn the right to build it later" option, not a now-bet.

---

## What must be true regardless of route

1. **Fix retention first.** Publish the 90-day oncology cohort curve, set a target, gate frequency work on it. A frequency engine on a leaky bucket fails faster. ([02-growth](./sources/02-growth-and-retention-diagnosis.md))
2. **Answer the caregiver-vs-patient fork.** Three of the five routes (A, C, E) quietly assume the caregiver is the customer. That decision is still open in the committed one-pager. Decide it deliberately.
3. **Stay model-agnostic and trust-first.** Rent the model, own the refinery (extraction, grounding, eval, audience adaptation, consent). One bad medical output is existential; EU-native trust is the asset the labs are retreating from.
4. **Pick one monetization motion to lead.** B2C-premium, caregiver-pay, and B2B2C-insurer are different companies operationally. A small team cannot run all at full intensity. Lead with one, treat the others as upside.

---

## Open decisions

| # | Decision | Why it gates the vision |
|---|---|---|
| 1 | Which route (or A+C hybrid) becomes the spine | Determines product, customer, and monetization for 18 months |
| 2 | Caregiver vs patient as primary customer | Reshapes design, growth, and pricing |
| 3 | Lead monetization motion (caregiver-pay vs B2B2C vs RWD) | A small team cannot run all three |
| 4 | Narrow (oncology deep) vs Wide (reduce appointment-dependency) | The open Code Red Part 2 fork; the Q3 strategy exercise (mid-June) should resolve it |

---

## Source map

This synthesis rests on the distilled evidence in [`sources/`](./sources/), each pointing back to the live originals:

| Synthesis | Distills | Originals |
|---|---|---|
| [01 Market & competitive landscape](./sources/01-market-and-competitive-landscape.md) | Commoditization, encroachers, AI trends, moat verdict, reimbursement | `product-strategy/market-trend-analysis/`, `specs/care-brain/competitive-analysis.md` |
| [02 Growth & retention diagnosis](./sources/02-growth-and-retention-diagnosis.md) | Code Red, the leaky bucket, frequency problem, funnel leverage, virality math | `product-strategy/code-red-mau-improvement/`, `product-strategy/funnel-leverage-model/` |
| [03 Care Brain vision corpus](./sources/03-care-brain-vision-corpus.md) | The care-intelligence platform vision + the Lenny critique | `specs/care-brain/` |
| [04 Activation & unicorn theses](./sources/04-activation-and-unicorn-theses.md) | Life moments, 3 pillars, 4 layers of need, the consumer-layer thesis | `specs/ideas/activation-and-audience/` |
| [05 Market sizing & TAM](./sources/05-market-sizing-and-tam.md) | Addressable populations NL + EU | `specs/patient-population-sizing.md`, `code-red-mau-improvement/research-life-moments-tam.md` |
| [06 Investor & DD signals](./sources/06-investor-and-dd-signals.md) | SpringTide / Maljers / Bupa / Novartis takeaways | `context/260223-expert-call-summaries-dd-investment.md` |
| [07 Product context & brand](./sources/07-product-context-and-brand.md) | Current state, North Star, positioning, voice, care circle | `context/product-context.md`, `brand-positioning-v2.md`, `care-circle.md` |
| [08 Lenny's guest panel](./sources/08-lenny-guest-perspectives.md) | Ten verified outside perspectives on the open decision forks, staged debate, opposing-view synthesis | Lenny's Podcast/Newsletter episodes, cited inline (deep-research verified 2026-06-04) |
| [09 Aspirational playbooks & human needs](./sources/09-aspirational-playbooks-and-human-needs.md) | Category-definer wedge-to-vision patterns + human-needs hypotheses for the seriously ill | Company histories (directional), board input 2026-06-03 |
| [10 Rethinking the core action](./sources/10-rethinking-the-core-action.md) | Candidate weekly-or-better core actions mapped to evidence, one-loop convergence, validation plan incl. the 20-interview hard requirement | `research/healthcare-life-changing-moments/`, ZeroClaw/care-brain JTBD corpus, board input |
