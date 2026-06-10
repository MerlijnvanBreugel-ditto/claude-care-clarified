# Appendices — Long-term Product Vision (evidence base)

_The claims in the main narrative lean on two research programs. The appendices are the receipts. Graded citations live in `../market-trend-analysis/citation-index.md` and `../market-deep-dive/citation-index.md`._

- **`market-trend-analysis/`** = the threat map: who is coming for the summary wedge.
- **`market-deep-dive/`** = the opportunity map: in each layer we could build, who already won that game, what made them sticky, who pays, and whether the direction is real.

A note on labels used throughout: **Core** = the intelligence we build the company on (understanding → advising). **Additional** = everything that strengthens or extends the Core but is not the foundation (a record we integrate, a coordination or social layer we lean into selectively, an operational front door).

---

## Appendix A — Market forces: a heating market is a tailwind

For years, patient-facing health tech was a backwater. In the last ~18 months it became one of the hottest markets in technology. Capital is pouring in and the largest companies in the world are all building here. The category we bet on is being validated in real time. That is a tailwind, not only a threat.

**Where the capital and the giants are going:**

| Player | Move | Signal |
|---|---|---|
| **Whoop** | $575M at a $10.1B valuation (Abbott and Mayo Clinic on the cap table, IPO signalled); ~2.5M members, ~$1.1B run-rate | Consumers pay for health at scale; medicalising fast (FDA-cleared ECG) |
| **Oura** | $900M+ at ~$11B (Fidelity); 5.5M+ rings, >$1B revenue in 2025; Dexcom invested $75M | Consumer health hardware is a real business |
| **Apple** | Watch FDA-cleared hypertension + sleep apnea, but scaled back its "AI doctor" (Project Mulberry, Feb 2026) | Even Apple could not ship the "explain my health" layer. It is genuinely hard. |
| **Google** | Gemini "Personal Health Coach" → Google Health Premium ($9.99/mo) after 500k+ testers | A big-tech consumer health subscription, live and paid |
| **OpenAI / Anthropic / Google** | ChatGPT Health (7 Jan), Claude for Healthcare + HealthEx (11 Jan), Gemini Health Coach — all within one week, Jan 2026 | The three biggest AI labs entered consumer health at once, aimed at "explain my records" |
| **Epic** | "Ask Emmie" patient assistant; 85% of customers live with genAI; already live in NL hospitals | The incumbent EHR is moving patient-direct |

**The demand behind it is exploding, not hypothetical.** ~40M people ask ChatGPT a health question every day (230M+/week). Consumer AI-for-health use doubled in a year (16%→32% in the US; the EU runs 12–24 months behind). Patient comfort with AI listening in the room jumped from 21% (2024) to 60% (2026). Voice is becoming the default interface. Every one of those curves points at the exact moment Ditto already owns: a spoken medical conversation people want to understand.

**Why a hot market is good for us, not only scary:**
- **It validates the category.** We are no longer evangelising a niche. The biggest companies in the world are telling the market this matters.
- **The tailwinds are on-thesis.** Voice-first, ambient capture, agentic assistants, and rising consumer comfort all favour a product whose raw input is the recorded visit.
- **The giants are aimed elsewhere.** Wearables own _what your body did_ (biometrics, sleep, longevity). The labs answer _generic_ questions and ground in _your_ records _for you_. None owns _what the doctor actually said_, none is built for _the family around a serious diagnosis_, and none is EU-record-native.
- **The best-resourced player couldn't do the hard part.** Apple shelved its AI health coach because "explain and advise on my health" is hard. That is a signal, not a gap, for a focused player.
- **Heat brings capital and exits.** A hot, well-funded category is a better place to raise, partner, and be bought into than a cold one.

The flip side of the same heat: the _generic_ summary commoditises fast. That is Appendix B.

---

## Appendix B — The six end states, in depth and scored

Each end state below carries the same four lines: how it relates to the vision, what the product actually does, its strengths, and its risks. The scoring table at the end quantifies all six on six dimensions, the same way as the interactive decision map.

### 1. Care Companion — _Core_
- **Relation to the vision:** the base. Understanding your own care, the job Ditto already does. Everything else stacks on this.
- **What the product does:** clarifications, overview and visualisation of your care, disease-specific context, context-aware AI Q&A, light symptom-tracking. Heavy AI.
- **Strengths:** better than general-purpose AI on _your_ actual care; trusted; EU-native; oncology depth; brings AI to people who don't reach for it elsewhere.
- **Risks:** the summary artifact itself commoditises (Appendix C); episodic frequency. It needs the climb above to stay something people grow attached to.

### 2. Trusted Health Assistant — _Core_
- **Relation to the vision:** the top of the intelligence ladder, what the companion becomes as you keep adding intelligence. A dedicated end state in its own right.
- **What the product does:** proactive, personalised advice and nudges on the medical behaviour you can control; smart reminders; wearable inputs; a full AI assistant. Very heavy AI.
- **Strengths:** the highest technology IP; once trusted, strong lock-in; the rung where the most user value and the most money sit.
- **Risks:** the device rung. Individualised advice triggers MDR Class IIa and AI-Act high-risk, and you compete with consumer big tech. The way through is to keep a human or the care circle making the clinical call.

### 3. Patient-Owned Record — _Additional (integrate, don't own)_
- **Relation to the vision:** not a destination on its own. It is the input that lets the Companion and the Assistant see the whole picture.
- **What the product does:** ingest all available medical data, make it understandable and shareable; data integrations; a possible EHDS launching partner.
- **Strengths:** if it were the superior EU solution it would carry immense lock-in.
- **Risks:** data alone is low value without insight; you fight governments and EHRs; heavy dependency on integrations that can be cut; owning the record pays zero (Appendix D). So we integrate it, we don't own it.

### 4. Care Coordination — _Additional (selective lean)_
- **Relation to the vision:** improves how families manage the disease together. It rides the Companion; it is not a foundation.
- **What the product does:** factual medical updates, a shared overview, agenda and task management, flexible managed accounts. Low AI.
- **Strengths:** increasingly needed as care gets complex; too messy for a WhatsApp group; high practical value.
- **Risks:** a feature unless bolted to an institutional cost; no clear NL buyer; depends on the whole group (including professionals) adopting it (cf. Caren).

### 5. Social Care Platform — _Additional (selective lean)_
- **Relation to the vision:** improves the experience of not being alone. Connection that rides understanding, never replaces it.
- **What the product does:** support gestures, shared daily updates, narrative/blogging, finding peers, communities.
- **Strengths:** network effects; could be the go-to place to share anything health-related; genuinely exciting.
- **Risks:** competes with WhatsApp and existing social; improves perception, maybe not outcome; standalone communities get acqui-hired, not paid (Appendix D). Connection alone is a worse WhatsApp.

### 6. The Front Door of European healthcare — _Additional (integrate; owning it is a board-level fork)_
- **Relation to the vision:** the operational "do-it-all" entry point. Not intelligence, but it holds the scheduling and data that feed everything above.
- **What the product does:** scheduling, planning appointments, second opinions, finding your data, messaging professionals, prescriptions. The rails.
- **Strengths:** a closed provider moat is genuinely defensible; clear B2B monetization (the Doctolib model); high frequency for whoever owns it.
- **Risks:** owning it means becoming a provider-SaaS company, a different company than the one we are. Doctolib is weak in NL, but taking the booking seat is a supply war and a board call, not a product call. The lighter move is to plug into the rails and own the intelligence on top.

### The scores

1–5 per dimension. Five are higher-is-better; **Regulatory (⚠) is a burden, so higher means heavier MDR / AI-Act exposure.** Scores are research-informed judgement from the two market programs, for recalibration at founder alignment, not measured fact.

| End state | Frequency | Defensibility | Monetization | User value | Company excitement | Regulatory ⚠ | Role |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| _Today — the bare summary_ | 2 | 2 | 2 | 3 | 2 | 2 | _starting point_ |
| 1. Care Companion | 3 | 4 | 3 | 4 | 4 | 2 | **Core** |
| 2. Trusted Health Assistant | 5 | 4 | 4 | 5 | 5 | 5 | **Core** |
| 3. Patient-Owned Record | 2 | 2 | 2 | 3 | 3 | 3 | Additional |
| 4. Care Coordination | 3 | 2 | 2 | 4 | 2 | 1 | Additional |
| 5. Social Care Platform | 3 | 2 | 2 | 3 | 5 | 1 | Additional |
| 6. Front Door | 5 | 4 | 4 | 4 | 4 | 3 | Additional |

**What the scores say:**
- The two **Core** states (Companion → Assistant) carry the most value, monetization and excitement, and the Assistant carries the heaviest regulatory burden. The climb is where the prize _and_ the device-line risk both live.
- The **Record** scores low as a destination but is the input that lifts the Core. Chase it as an enabler, not a goal.
- **Coordination** and **Social** show real user value but thin defensibility and monetization. Selective additions where there is genuine pull, not foundations.
- The **Front Door** scores high on frequency, monetization and defensibility, but as an operational business it is a different company. Integrate the rails, or treat owning them as a board fork.
- Against _Today — the bare summary_ (defensibility 2, commoditisation maxed), almost every direction is stronger. Standing still on the summary is the weakest position on the board.

---

## Appendix C — Conversation summaries: the commoditization clock

The patient-friendly summary is commoditizing from every direction. The institution will likely ship it for free in NL/BE around **2027–28**. This is the clock the whole strategy runs against.

| Vector | Signal | Status & timing |
|---|---|---|
| Portal / EHR | ChipSoft HiX "patiëntvriendelijke brief"; ZAS Antwerp live 2026-04-16 (~40k/yr) | Patient-friendly letters already shipping in NL/BE; standard-of-care ~**2027–28** |
| Incumbent EHR | Epic "Ask Emmie" | Patient-direct 2026–27; no confirmed EU deployment yet |
| Scribe | Nuance DAX / Dragon Copilot | GA NL/BE 2026-02-12, clinician-only so far |
| Scheduling incumbent | Doctolib Consultation Assistant (6M+ after-visit summaries since Oct 2024); Doctolib Parents (patient AI) early 2026 | A scaled incumbent already bundles summary + assistant |
| B2C consumer | Simply Onno (DE, 60k+ summaries) | Real traction on the comprehension job; comprehension alone is not defensible |
| Direct analog (US) | Kin Health ($9M, May 2026), Hedy, Medcorder | Same wedge + care-circle loop; geography protects the EU for now |

**The gap that still holds:** patient-initiated + cross-provider + recording-based + multilingual + oncology-deep is still unoccupied. Nobody is building Ditto's exact product better. The threat is commoditization, not a head-on clone yet.

**Demand is not the question.** Patients forget 40–80% of a visit (~$236B/yr in the US), there are 63M US caregivers (NL 1.9M at parity), 76% carry ≥1 chronic condition, and 31–38% of summary-engagers already share with someone. The user, the moment, and the problem are validated. The race is the moat, not the demand.

**Implication:** move from a weak relationship moat to a strong one before the artifact goes free. The summary is the way in, not the thing we defend.

---

## Appendix D — Monetization: routes and realism

Monetization is a real constraint on strategy, but it is not a wall. With enough scale and trust, almost anything monetises. The honest question is not "can this make money" but "which route fits us, and what does the evidence say works and fails." Health is harder than its neighbours: fitness, wellness and longevity monetise on consumer payment relatively easily, because the use is habitual and aspirational. Episodic, severe healthcare is harder, because consumers pay reluctantly for something they hope to use rarely, and institutions want proof before they reimburse. So we plan realistically: lead with the route most reachable for a ~16-person EU company, and keep the others open as scale grows.

**The routes:**

| Route | What it is | Realism for Ditto |
|---|---|---|
| **Home-market B2B licensing** | Hospital/insurer pays per-pathway or annual for the value a better-informed patient creates: comprehension, fewer crisis contacts, channel replacement, no-show reduction. Rides the Dutch B2B channels + the diga.nl scheme + €2.8B IZA funds. | **Most reachable. Lead here.** |
| **Pharma-sponsored / RWD** | Pharma funds patient-support, adherence, and consented real-world data. Validated patrons (Novartis, Sciensus). | Real money, near-term, but carries a trust cost. A deliberate fork, consent-first only. |
| **Reimbursement (DiGA / diga.nl)** | Clinical evidence, then a reimbursed tariff. Achievable at Class I; the wall is an RCT, not device class. | A dated go/no-go bet (~€1.5–3.5M over 2–3 yr). Not the near-term Core. |
| **Consumer subscription** | Patient / caregiver premium tier. | A topper today in episodic illness, but Whoop, Oura and Google Health Premium prove consumers _do_ pay at scale when value and habit are high. Grows as we climb the intelligence ladder. |
| **B2B2C** | Serve the patient free or near-free; bill the institution that benefits. | The shape that fits a patient-first product. The likely synthesis of the routes above. |

**What works (success cases):**
- **Consumer-pay does work in health-adjacent categories.** Whoop (~$1.1B run-rate, 2.5M members), Oura (>$1B revenue, 5.5M rings) and Google Health Premium ($9.99/mo) show consumers will pay for health when the value is high and the use is habitual.
- **Provider-SaaS scales.** Doctolib monetises providers at scale and stacks patient features on top.
- **Institutions and pharma pay for outcomes and data.** Hospital ePRO, pharma-funded oncology programs, and infra players (b.well) all carry real revenue.
- **Reimbursement is reachable at Class I.** 95% of German DiGA and all French PECAN are Class I; the barrier is clinical evidence, not certification.

**What fails or disappoints (caution cases):**
- **Consumer subscription on low-frequency, episodic illness.** Every D2C health-coach player pivoted to B2B; the one-shot summary does not sustain a subscription on its own.
- **Owning the record pays zero.** Google Health, HealthVault and Vivy all shut; value accrues to reasoning over the record, not to holding it.
- **Stranger communities get bought, not paid.** PatientsLikeMe → UnitedHealth; the community monetised as data, not subscription.

**The realistic read:** lead with home-market B2B licensing, hold pharma-RWD as a consent-gated fork, treat reimbursement as a dated bet, and treat consumer-pay as upside that grows with scale and with how far we climb. No single route is the only door. If we earn enough scale and trust, more of them open.

---

_Caveat for external use: several vendor figures are flagged «unverified» in the source briefs (e.g., the €6–12/mo reimbursement benchmark; some valuations and usage stats are company-reported; a few incident stats from secondary aggregators). Re-verify against each program's `citation-index.md` before any outside-facing use._
