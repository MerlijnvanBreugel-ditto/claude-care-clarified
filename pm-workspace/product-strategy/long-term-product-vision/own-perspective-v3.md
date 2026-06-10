# Ditto — Long-term Product Vision

_Working narrative, June 2026. Up for debate. The point is to get us aligned enough to make better daily decisions, not to lock a ten-year plan. The appendices at the end are the evidence base._

## Why we exist

I want to start with the why, because the strategy will change, but the reason we are doing this should be steadier. Mission so far: **clarify and connect care journeys, for you and your loved ones.**

This sits on the belief we started from: the patient is massively underserved, and the patient is the unlock for a healthcare system that is otherwise stuck. Scribes took off because the technology finally caught up, but the real gap was never the doctor's note. It was the person walking out of the room with a failing memory, a notepad, and a letter full of Latin that tells them they have cancer. EHRs have not fixed that. They gave us clunky software, fragmentation, and portals that store data without ever explaining it. AI assistants are individualistic yet generic, and omnipotent yet unreliable.

## Summaries cannot be the goal

Summary tools are a commodity now and they keep getting more reliable. On the business side they are becoming standard for every conversation.

- Better summaries are only defensible if you have something no one else has: proprietary models, unique validation data, a sharp niche. We do not truly have that yet. We get the most we can out of the underlying models.
- EHRs and scribes are catching up. Within about a year, patient summaries are native. When ChatGPT or Gemini ship dedicated conversation summaries, that attacks us directly. Saying "doctors will never allow it" is stretching reality.
- A summary is relevant around the appointment and maybe the day after. Even when you are severely ill, that is a reason to open Ditto weekly at most. Unless we deliver something incredible in that moment, we are a convenient function, not something people grow attached to.
- Low frequency is hard to monetize. Consumers do not pay easily for health apps, and insurers want activity before they reimburse.
- Pushing frequency or growth features for their own sake is a dead end. Unless we solve real problems, we can only nudge so far in the direction _we_ want.

The good part:

- Our summaries are genuinely better, and people trust them. That trust is key, and we have to keep measuring it instead of assuming it.
- We are roughly 10x better than the alternative, which is forgetting.
- Summaries and recordings hold far more potential than we unlock today.
- The summary is the way in. We have to squeeze the most value out of that episodic moment.
- From there the list is long: auto-update your health profile, nudge and help with follow-up actions, inform the family dynamically, link you to peers, explain your treatment in podcast or visual form, point you to a second opinion, find a fitting trial. The summary is the door, not the room.

## The long-term: six product end states

I do not know exactly what Ditto will be in five years, and I do not think that vagueness is a reason to stay vague now. We keep circling the same handful of futures. I want them all on the table, with real body this time, then synthesized. I have also scored them on six dimensions; the scores live in Appendix B.

Two labels run through all of this. **Core** is the intelligence we build the company on, from understanding to advising. **Additional** is everything that strengthens or extends the Core but is not the foundation: a record we integrate, a coordination or social layer we lean into selectively, an operational front door.

### 1. Care Companion — _Core_
- **Relation to the vision:** the base. Understanding your own care, the job Ditto already does. Everything else stacks on this.
- **What the product does:** clarifications, overview and visualisation of your care, disease-specific context, context-aware AI Q&A, light symptom-tracking. Heavy AI.
- **Strengths:** better than general-purpose AI on _your_ actual care; trusted; EU-native; oncology depth; brings AI to people who do not reach for it elsewhere.
- **Risks:** the summary artifact itself commoditises (Appendix C); episodic frequency. It needs the climb above to become something people grow attached to.

### 2. Trusted Health Assistant — _Core_
- **Relation to the vision:** the top of the intelligence ladder, what the companion becomes as you keep adding intelligence. A dedicated end state in its own right, and the natural peak if you combine end states.
- **What the product does:** proactive, personalised advice and nudges on the medical behaviour you can control; smart reminders; wearable inputs; a full AI assistant. Very heavy AI.
- **Strengths:** the highest technology IP; once trusted, strong lock-in; the rung where the most user value and the most money sit.
- **Risks:** the device rung. Individualised advice triggers MDR Class IIa and AI-Act high-risk, and you compete with consumer big tech. The way through is to keep a human or the care circle making the clinical call.

### 3. Patient-Owned Record — _Additional (integrate, don't own)_
- **Relation to the vision:** not a destination on its own. It is the input that lets the Companion and the Assistant see the whole picture.
- **What the product does:** ingest all available medical data, make it understandable and shareable; data integrations; a possible EHDS launching partner.
- **Strengths:** if it were the superior EU solution it would carry immense lock-in.
- **Risks:** data alone is low value without insight; you fight governments and EHRs; heavy dependency on integrations that can be cut; owning the record pays zero (Appendix D). So we integrate it, we do not own it.

### 4. Care Coordination — _Additional (selective lean)_
- **Relation to the vision:** improves how families manage the disease together. It rides the Companion; it is not a foundation.
- **What the product does:** factual medical updates, a shared overview, agenda and task management, flexible managed accounts. Low AI.
- **Strengths:** increasingly needed as care gets complex; too messy for a WhatsApp group; high practical value.
- **Risks:** a feature unless bolted to an institutional cost; no clear NL buyer; depends on the whole group (including professionals) adopting it (cf. Caren).

### 5. Social Care Platform — _Additional (selective lean)_
- **Relation to the vision:** improves the experience of not being alone. Connection that rides understanding, never replaces it.
- **What the product does:** support gestures, shared daily updates, narrative or blogging, finding peers, communities.
- **Strengths:** network effects; could be the go-to place to share anything health-related; genuinely exciting.
- **Risks:** competes with WhatsApp and existing social; improves perception, maybe not outcome; standalone communities get acqui-hired, not paid (Appendix D). Connection alone is a worse WhatsApp.

### 6. The Front Door of European healthcare — _Additional (integrate; owning it is a board-level fork)_
- **Relation to the vision:** the operational "do-it-all" entry point. Not intelligence, but it holds the scheduling and data that feed everything above.
- **What the product does:** scheduling, planning appointments, second opinions, finding your data, messaging professionals, prescriptions. The rails.
- **Strengths:** a closed provider moat is genuinely defensible; clear B2B monetization (the Doctolib model); high frequency for whoever owns it.
- **Risks:** owning it means becoming a provider-SaaS company, a different company than the one we are. Doctolib is weak in NL, but taking the booking seat is a supply war and a board call, not a product call. The lighter move is to plug into the rails and own the intelligence on top.

## The synthesis: Core and Additional

These are not six equal bets. They stack.

**The intelligence is the Core, and it is our contrarian heart.** It runs from understanding (Care Companion) to advising (Trusted Health Assistant), and it grows in two directions: up the intelligence ladder, and outward into the day-to-day and weekly needs between appointments where frequency and attachment actually live. The **Patient-Owned Record is not a goal, it is a multiplier**: if we can integrate it, the assistant finally sees the full picture and every rung gets better. So we chase the record as an enabler, not a destination.

**The Front Door is Additional and operational.** Scheduling, prescriptions, messaging, data access. This is not intelligence, it is operations, and it is where Doctolib and the portals live. It can sit under or beside the Core: it brings reach and data, and being the front door is itself defensible. Being honest that some of this is operations and some is intelligence is what was missing before. It makes the whole thing buildable instead of one vague tower.

**Coordination and social are Additional too, and selective.** We take the parts that make the companion a more complete experience, we experiment where there is a real market, but neither becomes the foundation.

One tension to name honestly. The rung where the money is, individualised advising, is also the rung where regulation bites hardest. Advising is the MDR and AI-Act device rung. The companies that survive there route around it by keeping a human or the care circle in the loop, rather than having the AI act alone. That is the line we have to respect as we climb.

## Two ways of reasoning

We keep confusing ourselves because we mix two ways of reasoning. Both are valid, and I want to run them at the same time.

**Backwards from a vision.** Imagine the Ditto that should exist in a few years and reason back to what we build now. This keeps us coherent and stops us becoming a pile of features. We do not know the precise route, but we have directionality.

**Forwards from jobs to be done.** Watch how people actually struggle in healthcare today and solve one job, then the next, so Ditto solves more and more real problems over time. The care-management jobs people already do badly are concrete: booking and landing appointments, finding their own data, looking things up online, making sense of literature, updating their loved ones. This keeps us useful and grounded in how people already behave.

Over both sits one hard filter: **monetization.** What actually becomes a business is a real constraint, not an afterthought, and it excludes options no matter how nice the vision or how real the job. The uncomfortable truth is that almost nothing in this space monetizes on patient-pay directly. Fitness: easy. Wellness: doable. Longevity: easy. Healthcare: hard. The honest answer to "can a reimbursed app be a unicorn?" is: not on reimbursement alone. The reimbursed market is small and has bankrupted its pioneers; the companies that got big did it on B2B at scale. So reimbursement is a credible starting point, and the engine has to be B2B. Appendix D works this through.

## The how for product

I believe the following will be key to moving fast(er):
1. Creating more clarity on where we want to be in a few years helps prioritize product in the short term. If we want to be an intelligent assistant, we should favour interactive AI chat over task management for care circles.
2. We should make bigger bets in shorter cycles and learn fast. Anthropic spends ~70% of its time on big bets; the rest is polish, maintenance, and low-hanging fruit.
3. If the strategic priorities are clear, we can seriously consider buy options too, to directly buy distribution, scale, and so on.
4. We should be careful with the perspective of "what would be good for Ditto." On the product side, we should address actual (or unaware) problems and needs.
5. Not committing to a direction keeps options open, but it can just as easily lead to a frankenstein product and to windows closing. If we invest heavily in data integrations and anticipating EHDS, we slow down on adding real intelligence to the data users already put into Ditto. That is a genuine trade-off, not a free choice.

## Market dynamics and forces

Three forces frame every decision, detailed in the appendices:
- **The market is heating, and that is a tailwind, not only a threat** (Appendix A). Capital and the biggest companies in the world have entered patient health tech. The category we bet on is being validated in real time, and the giants are aimed at biometrics and generic Q&A, not at what the doctor actually said.
- **Our current wedge, the summary, commoditises fast** (Appendix C). The institution will likely ship a free patient summary in NL/BE around 2027–28. The race is to build the moat before the artifact is free.
- **The money in this space is B2B** (Appendix D). Patient-pay is hard, reimbursement is bounded, and the durable engine is institutional. We stay patient-first in the product and let the institution that benefits pay (B2B2C).

## What we need to decide

This narrative is the input. The strategy session is where we choose. The questions:

0. **Why do we exist?** The mission above, up for debate.
1. **What does Ditto solve or improve?**
2. **Who are we building for, primarily?**
3. **What is, or will be, our moat?**
4. **How do we monetize it?**

Underneath Q4 sits the tension that shapes all the others: we are patient-first, but every payer in this space is an institution. My current lean is B2B2C, serve the patient and bill the institution, but I want us to land it together.

---

# Appendices — the evidence base

_Sourced from two research programs. Graded citations live in `../market-trend-analysis/citation-index.md` and `../market-deep-dive/citation-index.md`._

- **`market-trend-analysis/`** = the threat map: who is coming for the summary wedge.
- **`market-deep-dive/`** = the opportunity map: in each layer we could build, who already won that game, what made them sticky, who pays, and whether the direction is real.

## Appendix A — Market forces: a heating market is a tailwind

For years, patient-facing health tech was a backwater. In the last ~18 months it became one of the hottest markets in technology. Capital is pouring in, the largest companies in the world are all building here, and even direct analogs of Ditto are now funded. The category we bet on is being validated in real time. That is a tailwind, not only a threat.

**Where the capital and the giants are going:**

| Player | Move | Signal |
|---|---|---|
| **Whoop** | $575M at a $10.1B valuation; ~2.5M members, ~$1.1B run-rate. Strategic investors **Abbott and Mayo Clinic**; SHA Wellness clinical tie-in | Consumers pay for health at scale, and the consumer winner is already going B2B / clinical |
| **Oura** | $900M+ at ~$11B; 5.5M+ rings, >$1B 2025 revenue. **Essence Healthcare (Medicare Advantage)** gives members free rings; **US DoD** partnership; **Dexcom** invested $75M | Same pattern: a consumer hardware hit moving into payer and institutional channels |
| **Apple** | Watch FDA-cleared hypertension + sleep apnea, but **scaled back its "AI doctor" (Project Mulberry, Feb 2026)** | Even Apple could not ship the "explain my health" layer. It is genuinely hard. |
| **Google** | Gemini "Personal Health Coach" → **Google Health Premium ($9.99/mo)** after 500k+ testers | A big-tech consumer health subscription, live and paid |
| **OpenAI / Anthropic / Google** | ChatGPT Health (7 Jan), Claude for Healthcare + HealthEx (11 Jan), Gemini Health Coach — **all within one week, Jan 2026** | The three biggest AI labs entered consumer health at once, aimed at "explain my records" |
| **Epic** | "Ask Emmie" patient assistant; 85% of customers live with genAI; already live in NL hospitals | The incumbent EHR is moving patient-direct |
| **Kin Health** | **$9M (May 2026)**, US-only; the closest direct analog — same recorded-visit wedge + care-circle loop | Even our exact shape is now venture-funded. The window is real but watched. |

**The consumer winners are themselves going B2B.** Whoop sits next to Abbott and Mayo Clinic; Oura is in Medicare Advantage and the DoD. This both shows the market maturing and foreshadows Appendix D: even the consumer hits make their durable money through institutions.

**The demand behind it is exploding, not hypothetical.** ~40M people ask ChatGPT a health question every day (230M+/week). Consumer AI-for-health use doubled in a year (16%→32% in the US; the EU runs 12–24 months behind). Patient comfort with AI listening in the room jumped from 21% (2024) to 60% (2026). Voice is becoming the default interface. Every one of those curves points at the exact moment Ditto already owns: a spoken medical conversation people want to understand.

**Why a hot market is good for us, not only scary:**
- **It validates the category.** We are no longer evangelising a niche. The biggest companies in the world are telling the market this matters.
- **The tailwinds are on-thesis.** Voice-first, ambient capture, agentic assistants, and rising consumer comfort all favour a product whose raw input is the recorded visit.
- **The giants are aimed elsewhere.** Wearables own _what your body did_. The labs answer _generic_ questions and ground in _your_ records _for you_. None owns _what the doctor actually said_, none is built for _the family around a serious diagnosis_, and none is EU-record-native.
- **The best-resourced player couldn't do the hard part.** Apple shelved its AI health coach because "explain and advise on my health" is hard. That is a signal, not a gap, for a focused player.
- **Heat brings capital and exits.** A hot, well-funded category is a better place to raise, partner, and be bought into than a cold one.

The flip side of the same heat: the _generic_ summary commoditises fast. That is Appendix C.

## Appendix B — The six end states, scored

The bodies for each end state are in the main document above. This is the quantification, the same way as the interactive decision map: 1–5 per dimension. Five are higher-is-better; **Regulatory (⚠) is a burden, so higher means heavier MDR / AI-Act exposure.** Scores are research-informed judgement from the two market programs, for recalibration at founder alignment, not measured fact.

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

## Appendix D — Monetization: routes and realism

Monetization is a real constraint, but it is not a wall. With enough scale and trust, most things monetise. The honest questions are which route fits us, what the evidence says works and fails, and how big each route can actually get. Health is harder than its neighbours: fitness, wellness and longevity monetise on consumer payment relatively easily, because the use is habitual and aspirational. Episodic, severe healthcare is harder. So we plan realistically, lead with the most reachable route, and stop treating reimbursement as the prize.

**The routes:**

| Route | What it is | Realism for Ditto |
|---|---|---|
| **Home-market B2B licensing** | Hospital/insurer pays per-pathway or annual for the value a better-informed patient creates: comprehension, fewer crisis contacts, channel replacement, no-show reduction. Rides the Dutch B2B channels + the diga.nl scheme + €2.8B IZA funds. | **The engine. Lead here.** |
| **Pharma-sponsored / RWD** | Pharma funds patient-support, adherence, and consented real-world data. Validated patrons (Novartis, Sciensus). | Real money, near-term, but carries a trust cost. A deliberate fork, consent-first only. |
| **Reimbursement (DiGA / diga.nl)** | Clinical evidence, then a reimbursed tariff. Achievable at Class I; the wall is an RCT, not device class. | A credible starting point, but bounded. Not the engine (see below). |
| **Consumer subscription** | Patient / caregiver premium tier. | Works only with frequent, recurring value (see below). A topper, not a base, in episodic illness. |
| **B2B2C** | Serve the patient free or near-free; bill the institution that benefits. | The shape that fits a patient-first product. The synthesis of the routes above. |

**Consumer subscription works only when the value recurs.** SkinVision (Dutch skin-cancer checks) sustains a consumer subscription largely on its own, with only light insurer top-ups (CZ, Zilveren Kruis), because the worry and the check recur. The catch: even done well, its revenue is ~$3.8M (2025). Whoop and Oura sustain consumer-pay through a daily habit. The lesson for us: in episodic severe illness, consumer-pay only holds if we engineer recurring value (the climb up the ladder, treatment-window tracking). Without frequency, a subscription does not stick.

**Reimbursement is bounded, a starting point and not the engine.** Worth having for credibility and a first revenue line, but you do not build a large company on it:
- The entire German DiGA market, the biggest reimbursed digital-health market in the world, was ~**€171M in 2025 across ~58 apps** (~€3M each on average), after tariffs are roughly halved in negotiation (median ~**€221** per 3-month prescription).
- Reimbursement alone has killed its pioneers. **Pear Therapeutics**, the FDA-cleared pioneer of prescription digital therapeutics, went **bankrupt in 2023 and sold its assets for ~$6M**, with its CEO blaming insurance denials. A reimbursable product is not the same as a business.
- No digital-health company has become a unicorn on reimbursement revenue alone.

**The companies that got big did it on B2B at scale.** **Hinge Health** IPO'd in 2025 at ~$3B on ~$588M revenue (and turned profitable); **Sword Health** is valued ~$4B. Both were built on selling to self-insured **employers**, not per-prescription reimbursement. **Doctolib** scaled on provider SaaS. The pattern is consistent: the engine is B2B contracts on the value you create, at scale. One caveat for us: the US employer-benefit model does not transplant to the Dutch market, so our B2B engine is **hospital and insurer licensing, plus pharma**, not employer benefits.

**What fails or disappoints (caution cases):** consumer subscription on low-frequency illness (every D2C health-coach player pivoted to B2B); owning the record (Google Health, HealthVault, Vivy all shut, value accrues to reasoning over the record); standalone communities (PatientsLikeMe → UnitedHealth, monetised as data, not subscription).

**The realistic read:** use reimbursement (diga.nl, B2B tariffs) as a credible starting point, but build the real engine on home-market B2B licensing (hospital and insurer) and pharma, with consumer-pay as upside that only grows once we deliver recurring value. Lead B2B, serve the patient (B2B2C). No single route is the only door, but reimbursement is not the one that leads to a large company.

---

_Caveat for external use: several vendor and market figures are company-reported or from secondary aggregators (e.g., DiGA market totals, valuations, usage stats, the €6–12/mo reimbursement benchmark, some incident stats). Re-verify against the source briefs and each program's `citation-index.md` before any outside-facing use._
