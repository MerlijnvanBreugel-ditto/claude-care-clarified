# F6 — Proactive / Preventive Health Assistants & Coaches

> Market Deep Dive brief. Field F6, informs the Intelligence layer (top of the ladder). Created 2026-06-09 by Mewtwo.
> Web access available. Every non-obvious claim is cited and source-graded: **[P]** primary, **[S]** reputable secondary, **[V]** vendor self-report. Regulatory claims flagged for caution; «unverified» tags on soft figures.

## The one-line answer

Proactive coaching is the **only rung of the intelligence ladder with proven retention AND proven monetization** — but both are bought, not earned: retention comes from a **human (or human-supervised) coach in the loop**, and money comes from **employers and payers**, not consumers. The catch is that the same step up the ladder that unlocks the money (from "understanding" to "advising/agency") is the step that crosses the **MDR medical-device line** and, above it, the **AI-Act high-risk line**. The ladder is real; the top is expensive.

---

## (a) Field map — one screen

### The two tribes in this field

| Tribe | Who | What they actually sell | Who pays | Retention proof | Regulatory posture |
|---|---|---|---|---|---|
| **Disease-management coaches** (proven set) | Omada, Lark, Hello Heart, Dario, Vida, Sidekick, Sweetch | Behaviour change for a *named chronic condition* (diabetes, hypertension, weight) with measured biomarker outcomes | **Employers / health plans / PBMs** (US); **pharma + statutory insurers** (EU via DiGA) | Strong — they live or die on engagement, and the survivors publish RCTs | Mostly **wellness or low-class device**; the reimbursed-EU ones are **CE-marked MDR Class IIa** |
| **AI health assistants** | Ada, K Health, Healthily, Wysa, Woebot (RIP), Thrive AI, Counsel | General triage / advice / "front door" — *not* condition-locked | Mixed and **weaker**: provider/health-system licences (K Health), enterprise/insurer (Healthily, Ada), consumer freemium, VC subsidy (Thrive, Counsel) | **Weak and unproven** for the pure-AI consumer apps; strong only where a human or health system is attached | The advice ones are **CE-marked MDR Class IIa** (Ada); the therapy ones hit the **regulatory wall** (Woebot) |

### Intelligence ladder → regulatory class (the most important table in this brief)

This maps Ditto's own ladder (understanding → advising → agency) onto what regulation actually does at each rung. Treat the classes as **directional, confirm with a notified body / regulatory counsel** — the line is fact-specific and MDCG guidance was revised June 2025. [P][S]

| Rung | What the product does | Example in this field | Likely MDR status | Likely AI-Act tier | What it costs to operate here |
|---|---|---|---|---|---|
| **0. Understanding** | Explains *what the doctor meant*; summarises; reformats info the user already has | Ditto today; a plain-language explainer | **Not a medical device** — general info / "supporting" software, *if* it doesn't interpret the individual's data to recommend | Minimal / limited-risk (Art. 50 chatbot disclosure only) | Cheap. CE-exempt. The free rung. |
| **1. Advising (generic)** | Generic education, lifestyle/wellness nudges not tied to a specific diagnosis | Lark wellness track, Thrive coaching | Often **wellness exemption** if no diagnostic/treatment claim | Limited-risk | Cheap-ish, but the claim wording is the whole game |
| **2. Advising (individualised)** | Interprets *this person's* data to give a recommendation for diagnosis / monitoring / treatment | Ada symptom assessment; Hello Heart BP guidance | **Medical device, ~Class IIa** (MDR Rule 11) — notified-body conformity assessment | **High-risk** once it's a device requiring NB review | Expensive: QMS (ISO 13485), clinical evaluation, NB audit |
| **3. Agency** | *Acts* — titrates, triggers clinical decisions, autonomous treatment recommendation | Insulin-dosing DTx; autonomous therapy bot | **Class IIa–III**, higher rules | **High-risk**, full conformity assessment + post-market surveillance | Very expensive: clinical trial-grade evidence, the Woebot trap |

**The line bites between Rung 1 and Rung 2.** The moment software interprets *an individual's* data to recommend something about *their* diagnosis, monitoring or treatment, MDR Rule 11 pulls it into Class IIa (device, notified body). [S] MDCG 2019-11 is explicit: software that gives "recommendations for diagnosis, prognosis, monitoring and treatment of individual patients" is a medical device. [P] Once it's a device requiring third-party conformity assessment, the AI-Act treats it as **high-risk** by the MDR/IVDR route. [P][S]

---

## (b) Player teardowns — the 7 lenses

### Disease-management coaches (the proven-retention, proven-monetization set)

#### Omada Health — the canonical "who pays" answer

| Lens | Finding |
|---|---|
| **1. Job & moment** | Prevent/manage a chronic condition (diabetes prevention, T2D, hypertension, MSK, now GLP-1 adherence). Trigger: employer/plan enrols an at-risk member. [S] |
| **2. Sticky mechanic** | **Human coach + connected device + structured curriculum.** Coach accountability is the retention engine; the cellular scale / BP cuff makes data passive. Not gamification, not AI alone. [S] |
| **3. Frequency engine** | Weekly-cadence curriculum + coach check-ins + device readings. Episodic→habitual over a defined program length. |
| **4. Monetization** | **B2B: employers, health plans, PBMs (CVS Caremark, Cigna).** Revenue $170M FY24 (+38% YoY) [S]; Q2'25 $61.4M (+49% YoY), 752k members (+52%), net loss narrowed to $5.3M; FY25 guide $235–241M. [S] IPO'd 2025 at ~$1.1B target [S]. Pricing PMPM-style, **not disclosed** «unverified». Note: Medicare's MDPP pays *digital* suppliers only ~$18/online session [P] — so Omada's money is **commercial contracts, not Medicare DPP**. That is the tell. |
| **5. Moat** | Distribution (2,000 employer/plan contracts) + outcomes data + CDC DPP recognition. Moat is the **enterprise sales motion and the evidence base**, not the app. [S] |
| **6. Outcome & graveyard lesson** | Survivor and now public. Lesson: it took ~13 years and an IPO to make B2B chronic-care coaching a real business; still barely EBITDA-positive. This is a **grind, not a flywheel**. |
| **7. EU class** | US-shaped (employer health benefits don't exist the same way in NL). EU equivalent monetization is **DiGA / statutory insurer**, a different and slower motion. As a device-grade coach in EU → likely **MDR Class IIa**, AI-Act high-risk. |

#### Lark Health — "can AI replace the human coach?"

| Lens | Finding |
|---|---|
| **1. Job & moment** | Same DPP/diabetes/hypertension jobs as Omada, but **AI-first** conversational coach (no human in the loop by default). |
| **2. Sticky mechanic** | 24/7 conversational AI nudges trained on ~a decade of coaching messages; lower cost-to-serve than human coaches. [V][S] |
| **3. Frequency engine** | Daily/passive nudges + device data. Engagement "20–40% above traditional" per Lark [V] «unverified vendor claim». |
| **4. Monetization** | B2B payers: **Elevance/Anthem, multiple BCBS plans**; positioned top-3 US digital DPP by volume. ~$185M+ raised through Series D. [S][V] |
| **5. Moat** | Conversational-coaching dataset + payer distribution + CDC Full Recognition (enables Medicare/commercial reimbursement). [S] |
| **6. Outcome & graveyard lesson** | Survivor through the 2023–24 shakeout **because it published RCTs showing AI-coach parity with human coaching** on weight/A1c. [S] Lesson: pure-AI coaching can retain *if* you prove parity with evidence; the evidence is the moat, not the AI. |
| **7. EU class** | Reimbursed-grade chronic-disease AI coach in EU → **MDR Class IIa, AI-Act high-risk**. The AI-first model raises the conformity bar (transparency, robustness). |

#### Hello Heart — the device-anchored loop

| Lens | Finding |
|---|---|
| **1. Job & moment** | Hypertension self-management. Trigger: member with high BP/cholesterol enrolled by employer/plan. |
| **2. Sticky mechanic** | **FDA-cleared BP cuff + app** — taking your own BP is the daily ritual; AI gives feedback on the reading. The hardware manufactures the habit. [S] |
| **3. Frequency engine** | Daily BP measurement; the cuff is the frequency engine. |
| **4. Monetization** | B2B employers/plans; distributed via **Amwell clinical programs** (Oct 2024). $70M raised to scale employer reach. Claims 21 mmHg BP drop over 3y, >$2k/member yr-1 savings [V] «unverified vendor outcomes». [S][V] |
| **5. Moat** | Device clearance + payer distribution + longitudinal outcome data. |
| **6. Outcome & graveyard lesson** | Survivor. Lesson: **a connected device is a cheaper retention engine than a human coach** for the right condition — the measurement itself is the habit. |
| **7. EU class** | The BP feedback = individualised advising → **MDR Class IIa device** in EU; AI-Act high-risk. The cuff adds hardware regulatory load. |

#### Dario & Vida — the two paths and the warning

| Lens | Dario Health | Vida Health |
|---|---|---|
| **1. Job** | Cardiometabolic suite (diabetes, BP, weight, behavioural), B2B2C | Multi-condition cardiometabolic + behavioural, virtual-care provider network |
| **4. Monetization** | B2B employers/plans; FY24 rev $27M (+33%); **FY25 fell to $22.4M on one legacy client non-renewal**; client renewal >90%, 3-yr deals. [P][V] | B2B employers/plans; ~$110.9M ARR 2025 [S] «unverified, aggregator»; claims 10–20% medical-cost reduction, 1.5–2pt A1c [V] |
| **6. Graveyard lesson** | **Concentration risk is lethal** — a single client churn knocked ~17% off revenue. B2B coaching revenue is lumpy and contract-dependent. [P] | Scaled larger by adding a **human provider network** (telehealth), i.e. moved *up* the value/cost curve, not down. |
| **7. EU** | US-shaped; reimbursed EU version → Class IIa device. | Same. Provider network doesn't transplant to NL cheaply. |

#### Sidekick Health — the EU/pharma model

| Lens | Finding |
|---|---|
| **1–3. Job / mechanic / frequency** | Gamified digital therapeutics for chronic/lifestyle conditions (diabetes → UC → smoking cessation). **Gamification + behavioural economics** is the loop. Live in SE, FI, BE, **NL**, IE, CH, AT. [S][V] |
| **4. Monetization** | **Pharma-paid (Pfizer landmark EU deal)** + payer pilots, not consumer. ~$20M Series A (2020); no verified 2024–25 raise found «unverified». The EU model is **pharma sponsors the program to support its drug**. [S] |
| **5–6. Moat / lesson** | Moat = pharma relationships + EU regulatory footprint. Lesson: in EU, **pharma is the patron** where employers aren't. Gamification alone hasn't produced a breakout. |
| **7. EU class** | Already EU-native. Therapeutic claims → **MDR device (IIa)**; wellness-framed tracks stay lower. AI-Act high-risk if device. |

#### Sweetch — the acqui-hire signal

| Lens | Finding |
|---|---|
| **1–2. Job / mechanic** | Behavioural-AI + "emotional intelligence" engagement layer for CGM/T2D; now a **B2B2C engagement engine for Abbott, Dexcom, NovoCare**. [V] |
| **6. Graveyard lesson** | Pivoted from standalone DTx to being the **engagement layer inside someone else's device/drug funnel**. Lesson: the behavioural-AI coaching layer is **more valuable as a component than as a standalone app** — a recurring pattern in this field. [V][S] |

---

### AI health assistants

#### Ada Health — how far up a pure-AI advisor can climb in EU

| Lens | Finding |
|---|---|
| **1. Job & moment** | Symptom assessment / care navigation. Trigger: "what's wrong with me / where do I go." Episodic, not habitual. |
| **2. Sticky mechanic** | Accuracy + branching medical reasoning. But symptom-checking is **inherently episodic** — no return loop. |
| **3. Frequency engine** | **Weak.** You use it when sick. This is the structural problem with symptom checkers. |
| **4. Monetization** | Dual: consumer subscription + **enterprise (health systems, insurers, partners)**. Rev ~€37M FY24 [S] «aggregator-sourced, ranges $37–56M reported, unverified». ~$201M raised; €30M debt for runway. [S] |
| **5. Moat** | Medical knowledge base + **EU-MDR Class IIa certification** (Dec 2022) — a real regulatory moat few symptom checkers cleared. [P][V] |
| **6. Graveyard lesson** | Survivor, but **monetization is the chronic struggle**, not retention — because frequency is episodic. Lesson: being *right* (and CE-marked) doesn't fix *being rarely needed*. |
| **7. EU class** | **The reference case for Ditto.** Ada chose to be a **Class IIa medical device under MDR** because its product interprets individual symptoms to advise. This is exactly the line: individualised advising = device. AI-Act high-risk by the device route. [P] |

#### K Health — the "AI + health system" wrapper

| Lens | Finding |
|---|---|
| **1. Job & moment** | AI-driven virtual primary care. |
| **2. Sticky mechanic** | **AI does intake, a real clinician closes the loop** inside a health-system brand (Cedars-Sinai Connect, Mayo, Mass General Brigham, Northwell). The clinician + the health-system trust is the stickiness. [S] |
| **4. Monetization** | Pivoted from D2C to **licensing AI to health systems** (B2B). Valued ~$900M (2024), ~$380M raised; last public revenue $52M (2022). [S] «no verified 2024–25 revenue» |
| **6. Graveyard lesson** | The interesting move: **abandoned consumer-direct, became infrastructure for incumbents.** Lesson: pure-consumer AI primary care didn't monetize; **wrapping it in a trusted provider's brand did.** [S] |
| **7. EU class** | The AI-does-advice part → device territory; the clinician-in-loop model is how they manage liability. EU equivalent = telehealth + device hybrid. |

#### Wysa vs Woebot — the cleanest graveyard lesson in the field

| Lens | Wysa (alive, growing) | Woebot (dead, June 2025) |
|---|---|---|
| **1. Job** | Mental-health support between sessions | Standalone CBT therapy chatbot |
| **2. Mechanic** | **Wysa Copilot: AI supports a *human therapist's* patients between sessions** — human in the loop | Fully autonomous therapeutic agent — *replaced* the clinician |
| **4. Monetization** | B2B (employers, payers, providers) + NIH grant; expanding via acquisitions (April Health, Kins) [S] | Burned **$124M** chasing FDA marketing authorization that never came [S] |
| **6. Graveyard lesson** | **Position as the layer between human sessions, not the replacement.** 30+ peer-reviewed studies; FDA Breakthrough designation. [S] | Founder: shut down because the **cost/challenge of FDA requirements for an autonomous therapy device** was unbearable; *zero* FDA-authorized AI devices exist for mental-health conditions as of late 2025. [S] |
| **7. EU class** | "Support between sessions" framing keeps it nearer the wellness/limited line; therapeutic claims push to device | A standalone autonomous therapy bot is **the high-risk device case** — the rung-3 trap |

**This pair is the brief's sharpest lesson: the same AI capability is a thriving B2B business when it sits *beside* a clinician (Wysa), and a $124M graveyard when it tries to *be* the clinician (Woebot).** [S] The regulator drew the line at agency, and Woebot walked over it.

#### Counsel Health, Thrive AI, Healthily — the frontier, mostly unproven

| Player | Read |
|---|---|
| **Counsel Health** | The 2025 answer to Woebot's lesson: **"physician-supervised AI front door."** Free consumer chatbot + licensed physicians for diagnosis/Rx/referral. $25M Series A (a16z, GV) + $11M seed; >100k members. [S] Human-in-the-loop by design from day one. **Too early to judge retention/monetization** «unverified — no outcome data». |
| **Thrive AI Health** | OpenAI Fund + Huffington; hyper-personalised lifestyle coach (sleep/food/stress/connection). As of late 2024, **bare-bones non-functional demo.** [S] Big name, no product, no monetization yet. Treat as a *signal of where capital thinks the puck is going*, not a proof point. |
| **Healthily (ex-Your.MD)** | Pivoted from consumer symptom checker to **B2B "navigation & demand-management" for insurers/providers/pharmacies.** ~$139M raised, last round 2022. [S] Same lesson as K Health/Ada: **the consumer assistant monetizes as a B2B navigation tool, not a D2C app.** |

---

### Oncology-specific (Ditto's beachhead)

#### Jasper Health — the closest analog to where Ditto could go

| Lens | Finding |
|---|---|
| **1. Job & moment** | Organise the cancer journey: calendar, daily mood/symptom trackers, med adherence, **live sessions with oncology social workers**. Trigger: diagnosis. [S] |
| **2. Sticky mechanic** | **Human care navigator + symptom/mood tracking + supportive content.** The human navigator is the retention core; "AskJasper" AI is additive, not the spine. [S] |
| **3. Frequency engine** | Daily tracking during active treatment (high-intensity window) + navigator touchpoints. Naturally high-frequency *during treatment* — then it drops. |
| **4. Monetization** | **B2B: health plans + Medicare**, explicitly aligned to **CMS reimbursement codes** for navigation / health-related social needs (the 2024 G-codes for principal illness navigation). ~$31M raised (Series A led by General Catalyst). [S] |
| **5. Moat** | Navigator workforce + payer contracts + alignment to new oncology-navigation reimbursement. |
| **6. Outcome & graveyard lesson** | Still small. Lesson: **oncology navigation only became monetizable when CMS created navigation codes** — the money followed reimbursement, not user love. Outcomes are satisfaction-stat soft [V] «unverified». |
| **7. EU class** | Navigation/supportive-care framing largely **stays below the device line** (it organises and supports, doesn't diagnose/treat). EU reimbursement for navigation is **immature** — no clean DiGA analog for "navigation." This is a gap. |

#### OncoPower — thinner

| Lens | Finding |
|---|---|
| **1–2. Job / mechanic** | Oncology patient community + SDoH support + oncologist-burden tools; **provider-first, community as the loop.** [V] |
| **4. Monetization / 6. lesson** | Provider/practice-paid; little public traction data «unverified». Lesson: the oncology patient-app space is real but **fragmented and pre-scale**; nobody has won it. That cuts both ways for Ditto. |

> Sword / Hinge (MSK) deliberately not re-torn-down here — covered elsewhere. The one transferable point: both monetize **per-engaged-member B2B with a human coach/PT in the loop**, same playbook as Omada.

---

## (c) White space for Ditto

### Q1 — What actually makes proactive coaching retain?

| Retention driver | Verdict | Evidence |
|---|---|---|
| **Human (or human-supervised) coach in the loop** | **The strongest, most durable driver.** Users with accountability support show 2–3× 90-day retention; humans win on *sustained* (3–12mo) behaviour change. | [S] systematic review 2025; [S] |
| **Connected device / passive measurement** | **Strong and cheap** where a device fits (Hello Heart BP, CGM). The measurement *is* the habit. | [S] |
| **Pure-AI nudges / streaks / gamification** | **Retains 30–60 days, then decays.** Works only with proven parity evidence (Lark) or as a layer inside something else (Sweetch). Standalone gamification has produced no breakout. | [S] |
| **Episodic symptom-checking** | **Does not retain** — structurally episodic (Ada). | [S] |

**Implication for Ditto:** Ditto's frequency problem is the same one that kills symptom checkers — "understanding what the doctor said" is *episodic* (per appointment). The retention unlock is to attach a **light human-supervised layer** (oncology nurse / navigator touchpoint) and/or **passive symptom tracking during the active-treatment window**, where cadence is naturally high (oncology appointments can be weekly during treatment). Don't bet retention on AI nudges or streaks alone — the field has tested that and it decays.

### Q2 — What monetization survives the filter?

| Model | Survives? | Why |
|---|---|---|
| **Employer-paid (US PMPM)** | **Yes in US, no in NL.** | Omada/Hello Heart/Lark all live here; it doesn't transplant — NL has no employer-benefits health market of that shape. |
| **Payer / statutory insurer (DiGA in DE, basisverzekering-adjacent in NL)** | **Yes, but slow and gated by device status.** | DiGA paid €234M cumulative to end-2024, median ~€221/3-mo prescription post-negotiation [S]; but **requires CE-marked MDR device + evidence**. This is the EU money — and it's *above* the regulatory line. |
| **Pharma-sponsored programs** | **Yes in EU.** | Sidekick/Pfizer model — pharma funds the coach to support its drug. Viable for oncology (high-value drugs, adherence matters). |
| **Reimbursement-code-aligned navigation (CMS oncology nav)** | **Yes in US; immature in EU.** | Jasper's whole model. No clean EU navigation reimbursement yet — a gap, not an opening, today. |
| **Direct consumer subscription** | **No, as the primary engine.** | Every pure-consumer AI assistant (K Health, Ada, Healthily) **pivoted away from D2C to B2B**. Consumer pays for *acute access*, not *ongoing coaching*. |

**Verdict:** The monetization that survives is **B2B — pharma-sponsored or payer/insurer-reimbursed — and in EU oncology specifically, pharma is the most reachable patron near-term.** Consumer subscription does not survive as the retention/revenue engine. This matches the deep-dive's hard filter: a beloved free thing is excluded.

### Q3 — How far up the ladder can Ditto climb before regulation bites? (the key output)

| Rung | Ditto move | Regulatory cost | Recommendation |
|---|---|---|---|
| **0 — Understanding** | Explain the doctor's words; summarise; reformat | **CE-exempt** (general info), only AI-Act Art. 50 chatbot disclosure | **Free zone. Stay here as the base. Ditto is here today.** |
| **1 — Advising (generic)** | Generic education, "questions to ask your doctor," non-individualised lifestyle nudges | **Wellness exemption** if no diagnostic/treatment claim — *claim wording is everything* | **Safe to climb, with disciplined copy.** This is the cheap expansion. |
| **2 — Advising (individualised)** | Interpret *this patient's* results/symptoms to recommend what to do | **MDR Class IIa device** (Rule 11) — notified body, ISO 13485, clinical evaluation; **AI-Act high-risk** | **The cliff.** Only cross with eyes open: it's a clinical-evidence + QMS + NB commitment, not a feature. |
| **3 — Agency** | Act / titrate / autonomous recommendation | **Class IIa–III, full high-risk conformity + post-market** | **The Woebot trap. Do not approach without trial-grade evidence and a regulatory team.** |

**The precise line:** Ditto can climb freely to **Rung 1** (generic advising) with careful claim language and an AI-disclosure notice. The instant the product **interprets an individual user's data to recommend something about their diagnosis, monitoring, or treatment, it becomes a Class IIa medical device** (MDCG 2019-11; MDR Rule 11) and AI-Act high-risk. [P][S] That is the most expensive sentence in this brief.

**The strategic resolution of the regulatory ceiling:** the field's survivors don't beat the line — they **route around it with a human**. Wysa, K Health, Jasper, Counsel all put a **licensed human in the loop** so the *human* makes the individualised clinical recommendation and the AI *supports* it. This keeps the software nearer the support/wellness line while still delivering Rung-2 value to the user. For Ditto in oncology, the equivalent is: **AI does understanding + generic advising; a human navigator/nurse owns the individualised clinical step.** This is how Ditto climbs the ladder commercially without buying a Class IIa conformity assessment on day one — and it's the same structure that makes pharma- and payer-money reachable.

### The Ditto-shaped wedge (synthesis)

1. **Base (Rung 0–1, owned today):** plain-language understanding + generic advising. CE-light. The trust and frequency foundation.
2. **Retention layer:** passive symptom tracking in the active-treatment window (naturally high cadence) + a **human navigator touchpoint** — the proven retention mechanic, not AI streaks.
3. **Monetization:** **pharma-sponsored oncology programs** near-term (Sidekick/Pfizer shape, fits high-value oncology drugs + adherence), payer/DiGA-style reimbursement only if/when Ditto commits to a Class IIa device.
4. **Ceiling discipline:** the AI never crosses into individualised diagnosis/treatment recommendation; the human does. That's how the survivors monetize Rung-2 value without paying the Rung-2 regulatory bill — until a deliberate, well-funded decision to become a device.

---

## (d) Graded citations

| # | Claim it supports | Source | Grade |
|---|---|---|---|
| 1 | Omada FY24 rev $170M (+38%); IPO ~$1.1B; 679k members S-1 | fiercehealthcare.com; mobihealthnews.com | [S] |
| 2 | Omada Q2'25 $61.4M (+49%), 752k members, net loss $5.3M, FY25 guide $235–241M; payers incl. CVS Caremark, Cigna; GLP-1 minority | healthcaredive.com (Omada Q2 2025) | [S] |
| 3 | Medicare MDPP G-codes (G9886/G9887/online), ~$18 online session, bridge code removed 2025 | cms.gov MDPP billing refguide; CMS CY2026 PFS | [P] |
| 4 | Hello Heart $70M raise; Amwell partnership Oct 2024; FDA-cleared cuff; 21 mmHg / $2k savings claims | fiercehealthcare.com; business.amwell.com | [S] / [V] (outcomes) |
| 5 | Lark Elevance/Anthem + BCBS distribution; RCT parity-with-human; CDC Full Recognition; ~$185M+ raised | lark.com; intuitionlabs.ai; mobihealthnews.com | [S] / [V] |
| 6 | Dario FY24 $27M (+33%), FY25 $22.4M on one client non-renewal, >90% renewal, 3-yr deals | dariohealth.investorroom.com / prnewswire (DRIO results) | [P] / [V] |
| 7 | Vida ~$110.9M ARR 2025; 10–20% cost / 1.5–2pt A1c claims | getlatka.com; vida.com/our-outcomes | [S] aggregator / [V] |
| 8 | Sidekick gamified DTx; live in NL+6; Pfizer EU deal; ~$20M Series A | pharmaphorum.com; sidekickhealth.com | [S] / [V] |
| 9 | Sweetch behavioural-AI engagement layer for Abbott/Dexcom/NovoCare | sweetch.com | [V] |
| 10 | Ada EU-MDR Class IIa cert (Dec 2022); dual consumer+enterprise model; ~€37M FY24; ~$201M raised; €30M debt | about.ada.com/press; cbinsights; pitchbook | [P] (cert) / [S] |
| 11 | K Health pivot to health-system AI licensing; Cedars-Sinai/Mayo/MGB/Northwell; ~$900M val, ~$380M raised | statnews.com; fiercehealthcare.com; businesswire.com | [S] |
| 12 | Woebot shutdown June 2025; $124M burned; FDA-authorization cited as cause; zero FDA AI mental-health authorizations | statnews.com; telehealth.org; mobihealthnews.com | [S] |
| 13 | Wysa Copilot human-in-loop; FDA Breakthrough; 30+ studies; April Health/Kins acquisitions; NIH grant | buildmvpfast.com; telehealth.org | [S] |
| 14 | Counsel Health physician-supervised AI; $25M Series A (a16z, GV) + $11M seed; >100k members | hitconsultant.net; fiercehealthcare.com; businesswire.com | [S] |
| 15 | Thrive AI Health launch; bare-bones non-functional demo late 2024 | techcrunch.com; prnewswire.com | [S] |
| 16 | Healthily pivot to B2B navigation/demand-management; ~$139M raised | pitchbook.com; pharmaphorum.com | [S] |
| 17 | Jasper navigator + trackers + AskJasper; CMS navigation/HRSN code alignment; ~$31M raised | prnewswire.com (Jasper); fiercehealthcare.com; medcitynews.com | [S] / [V] (outcomes) |
| 18 | OncoPower provider-first community + SDoH; pre-scale | medium.com/@OncoPower | [V] |
| 19 | Retention: human/accountability 2–3× 90-day; AI decays 30–60d; hybrid best | frontiersin.org systematic review 2025; productgrowth.in | [S] |
| 20 | DiGA: €234M cumulative to end-2024, median ~€221/3-mo post-negotiation, MDR CE-mark Class I/IIa/IIb required | nature.com (npj Digital Medicine); provahealth.com; mtrconsult.com | [S] / [P] (npj) |
| 21 | EU AI Act: device-route MDAI = high-risk; integrated MDR+AI-Act conformity; Aug 2026/2027 timeline | reedsmith.com; taylorwessing.com; intuitionlabs.ai | [S] |
| 22 | AI-Act Art. 50 chatbot disclosure; applies 2 Aug 2026 | artificialintelligenceact.eu/article/50; ec.europa.eu | [P] / [S] |
| 23 | MDCG 2019-11: software giving individual diagnosis/treatment recommendations = medical device; revised June 2025 | health.ec.europa.eu (MDCG 2019-11 PDF); greenlight.guru | [P] / [S] |

### Verification notes / caveats
- **Regulatory classes are directional.** MDR Rule 11 / MDCG 2019-11 classification is fact-specific; the June-2025 MDCG revision and AI-Act guidelines are still settling. Confirm any rung-2/3 move with a notified body and regulatory counsel before relying on it.
- **Revenue figures from aggregators (Vida, Ada secondary numbers) are «unverified»** — ranges reported across sources; treat as order-of-magnitude.
- **Vendor outcome stats (Hello Heart, Vida, Jasper, Lark) are [V]** and self-reported; not independently audited here.
- **No clean EU reimbursement path exists for "care navigation"** the way CMS created one in the US — flagged as a gap for the synthesis, needs Merlijn/regulatory input.
