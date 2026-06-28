# Market Deep Dive — "Who Already Won, and How"

> Scope & research plan. Created 2026-06-09 by Mewtwo, with Merlijn.
> **Status**: Phases 1–3 complete 2026-06-09 (8 briefs, 6 direction chapters, 4 synthesis docs). Decisions resolved (bottom). Payload: `synthesis/17-layer-stack-scorecard.md`.
> Complements `../market-trend-analysis/`. Built to serve `../long-term-product-vision/own-perspective-v2.md` and its questions 0–4 (why we exist, what we solve, for whom, the moat, the monetization).
> Mode: **both** field teardowns **and** per-direction chapters · **even depth** across all fields and layers (the weighting is a conclusion the synthesis draws, not a filter on the research) · **global best-in-class, EU-filtered**.

## Why this exists

The existing `market-trend-analysis/` answers one question: *who is coming for our summary wedge?* It is a **threat map**, organized by threat vector (commoditization, encroachment, regulation, reimbursement, trust incidents). Deep on competitors, regulation, reimbursement.

It does **not** answer the question v2 turns on: *in each layer Ditto could build, who already won that game, what feature made them sticky, how do they monetize, and is the direction therefore real?* That is an **opportunity-and-mechanics map**, and it barely exists today.

This deep dive builds that mirror image, structured to v2's architecture so the output drops straight into the strategy session.

### What v2 changed in the plan
1. **Two reasoning axes, run in parallel.** Vision-backwards (the layers) **and** JTBD-forwards (the concrete jobs people already do badly): booking appointments, finding their own data, looking things up, making sense of literature, updating loved ones.
2. **Two layers, not five equal bets.** **Intelligence layer** (the contrarian core: understanding → advising → agency, with the personal health record as a *multiplier*, not a destination). **Operational layer** (the "front door": scheduling, prescriptions, messaging, data access; competitor shape ~DrLeap/Doctolib). Coordination + social are *lean-in* layers, not the spine.
3. **Monetization is a hard filter, not a column.** Every direction and job must survive "who pays and why." A beloved thing nobody pays for is excluded regardless of how good the vision or job.
4. **"Connect / loved ones" is claimed as Ditto's own** in the draft mission. The connection layer gets tested as a differentiator, not assumed.

## How this complements the existing analysis (per field)

| Field | What `market-trend-analysis` already has | What this adds |
|---|---|---|
| Symptom / outcome tracking (ePRO) | Shallow. Bearable, Visible, Vinehealth, MyTherapy as features; retention stat. | The standout oncology ePRO players it **misses** (Kaiku Health, Noona, Navify), the survival evidence (Basch/PRO-CTCAE), and *why* tracking retains or gets acqui-hired. |
| Health journaling / diary | Medium. CaringBridge + Kanker.nl as care-circle journals. | Broad consumer journaling (Day One, Reflectly, the AI-journaling wave) and what makes a diary habitual and monetizable. |
| Patient-owned records / data integration | Medium-shallow. Quli/Ivido/MedMij, HealthEx, Apple/Google Health. | The aggregation infra layer (b.well, Particle, Health Gorilla, Fasten), Germany's ePA rollout, and the **PHR graveyard** (Google Health, HealthVault, Vivy): why most died, what is different now. |
| EHDS positioning | **Barely.** Timeline only. No player mapped. | Who is positioning to capture EHDS value (secondary-use data players, consent brokers, national nodes), what a "launching partner" requires, Finland's Findata/Kanta as the working precedent. |
| Care coordination | Deep (Caren, Lotsa, Jointly, CaringBridge, Hello 24/7). | Extend: the **employer-paid** caregiving model (Wellthy, Cariloop, ianacare) and value-based oncology navigation (Thyme Care, Jasper). |
| Proactive / preventive assistants & coaches | Deep on wearables + AI labs as threats (briefs F, G). | Flip threat to playbook: disease-management coaches that retain and get reimbursed (Omada, Lark, Hello Heart, Sidekick); the agentic frontier (Thrive AI, Counsel). |
| Social / family networks | Deep (Belong, Inspire, PatientsLikeMe, Kanker.nl). | Extend: consumer social-habit precedents Ditto's own data has not hit (Strava, Flo) — does a social layer manufacture frequency. |
| **Operational front door** | **Threat-footnote only** (Doctolib as encroacher). | **New.** The operational stack as a *layer Ditto could own or must integrate*: scheduling, prescriptions, professional messaging, second opinion, data access. DrLeap/Doctolib shape, and whether the front door feeds the intelligence layer. |

## The teardown lens — "five levels deeper"

Every standout player gets the **same 7-lens teardown**. This is what makes it deeper than the existing scan, and it maps onto v2's questions and the monetization filter.

1. **Job & moment** — what problem, for whom, what trigger.
2. **The sticky mechanic** — the *specific* feature that creates the return visit (not the marketing).
3. **Frequency engine** — actual cadence (daily / weekly / episodic) and *why* it holds.
4. **Monetization (the hard filter)** — who pays, model, price point, evidence it works; and where it fails the filter.
5. **Defensibility / moat** — data, network, integration, regulatory, or brand. Which, and how durable.
6. **Outcome & graveyard lesson** — scale reached; if it failed, stalled, or got acqui-hired, *why*.
7. **EU-applicability filter** — what survives the move to EU/NL (regulation, reimbursement, culture).

Source-graded throughout (primary > reputable secondary > vendor self-report), with a citation index, carrying forward the existing analysis's honesty about unverified figures.

## Part I — Capability-field teardowns (8 briefs, even depth)

Each brief: a one-screen field map, then 5–10 standout players run through the 7-lens teardown, then a "white space for Ditto" close. Seed player lists (open to add/cut):

| # | Field | Seed standouts to tear down (global) | Layer it informs |
|---|---|---|---|
| F1 | **Symptom / outcome tracking (ePRO)** | Kaiku Health (Elekta), Noona (Varian/Siemens), Navify (Roche), CANKADO, Outcomes4Me, OWise, Vinehealth→Sciensus, Bearable, Visible, mySugr, MyTherapy · + Basch/PRO-CTCAE survival evidence | Intelligence |
| F2 | **Journaling / diary / narrative** | Day One, Reflectly, Finch, Rosebud (AI), Stoic · CaringBridge (the journal), PatientsLikeMe narratives, Kanker.nl bloggers | Intelligence / Social |
| F3 | **Patient-owned records / data integration** | Apple Health Records, Google Health Connect, Withings · b.well, Particle, Health Gorilla, Fasten, Zus · Quli, Ivido, MedMij, Germany ePA · graveyard: Google Health 1.0, HealthVault, Vivy | PHR multiplier |
| F4 | **EHDS & the patient-data economy** | Secondary-use: TriNetX, IQVIA, Datavant, Aridhia, Owkin · consent/infra: Gravitate Health, MedMij, Quli/Ivido · precedent: Finland Findata / Kanta · HealthData@EU nodes | PHR multiplier |
| F5 | **Care coordination platforms** | Family: CaringBridge, Lotsa, Jointly, ianacare, Caily · employer-paid: Wellthy, Cariloop · NL/pro: Caren (Nedap), OZOverbindzorg, Familienet · oncology nav: Thyme Care, Jasper, Memora | Coordination (lean) |
| F6 | **Proactive / preventive assistants & coaches** | Omada, Lark, Hello Heart, Sidekick, Vida, Dario · Ada, K Health, Wysa, Thrive AI Health, Counsel · oncology: Jasper, OncoPower | Intelligence (top of ladder) |
| F7 | **Social / family health networks & peer** | Belong, Inspire, HealthUnlocked, Smart Patients, Kanker.nl · habit-precedents: Strava, Flo, Peanut | Social (lean) |
| F8 | **Operational front door** (anchor: Doctolib) | Doctolib (anchor), ZorgDomein, Zocdoc, Jameda/Doctena, Kry/Livi, Qare · messaging: Siilo, Klara, Spruce · second opinion: Included Health, Medbelle, Medexo · national: NHS App, MijnGezondheid.net | Operational |

## Part II — Direction work, structured to v2's architecture (even depth)

Six syntheses, each drawing from the Part I briefs plus targeted gap-fill, each answering for Ditto: who is already there, the proven frequency engine, the monetization that works, the moat, the graveyard, and **the white space Ditto could own**.

| Ch | v2 element | Draws on | Special angle |
|---|---|---|---|
| C1 | **Intelligence layer — the ladder** (understanding → advising → agency) | F1, F2, F6 + consumer medical-search (Ada, Healthily, ChatGPT Health, OpenEvidence analog) | Where each rung adds frequency/value, and where MDR / AI-Act high-risk bites at the top (reuse the existing classification-cliff work). |
| C2 | **PHR as multiplier** (not destination) | F3, F4 | What integration actually unlocks for the intelligence layer; why PHRs die alone; EHDS as the enabler timeline. |
| C3 | **Operational front door** (new) | F8 | DrLeap/Doctolib shape; own vs integrate; does the front door's scheduling + data access genuinely feed the intelligence layer. |
| C4 | **Coordination (lean-in)** | F5 | The real market if done extremely well; the employer-paid and oncology-navigation monetization unlocks. |
| C5 | **Social (lean-in layer)** | F7 | Is "connect / loved ones" genuinely ownable and frequency-generating, or a feature anyone bolts on. Tests the draft mission's core claim. |
| C6 | **JTBD-forward map** | all | For each of v2's five named jobs, who solves it best today, how, the monetization, and whether there is a wedge for Ditto. The "forwards" reasoning axis made explicit. |

## Part III — Synthesis & strategic implications

- **Cross-cutting pattern extraction**: what actually manufactures frequency, what monetizes without leaning on reimbursement, what is genuinely defensible vs a copyable feature.
- **The monetization filter applied**: per layer/lean/job, who pays and why, and what gets **excluded** by the filter (v2's hard constraint).
- **Layer-stack scorecard**: the two layers + two leans + the front door scored against the four criteria (frequency · defensibility · monetization · real value), evidence-backed. This is where the **weighting conclusion** v2 hypothesizes gets confirmed or revised against the data, rather than assumed.
- **Reconciliation with the threat map**: what this changes in the existing `market-trend-analysis` conclusions, and what it confirms.
- **Inputs to questions 0–4** for the strategy session, framed as direction (per v2's "bigger bets, shorter cycles; point the right way and correct"), not a fixed 10-year destination.

## Method & sourcing

- Same engines as the existing analysis: `deep-research` (fan-out + adversarial verify) and `market-research` (sourcing discipline), plus the 7-lens template for consistency.
- Every claim cited and source-graded; a `citation-index.md`; unverified figures flagged, not laundered.
- Global search to find best-in-class (the strongest teardowns are often US/UK/Nordic), then the EU-applicability lens on every implication.

## Execution & sequencing

1. **Resolve the open decisions below**, then start.
2. **Phase 1 — Part I**: one research agent per field (F1–F8) in parallel, each producing a source-graded 7-lens teardown brief. Checkpoint.
3. **Phase 2 — Part II**: synthesize the six chapters from the briefs, with small per-direction gap-fill agents where a chapter is thin.
4. **Phase 3 — Part III**: synthesis, monetization filter, scorecard, reconciliation.
5. Update the registry and `long-term-product-vision` sources.

## Deliverables & file structure

```
market-deep-dive/
  00-scope-and-research-plan.md          ← this spine
  README.md                              ← how to read, status
  briefs/F1-symptom-tracking.md … F8-operational-front-door.md
  directions/C1-intelligence-ladder.md … C5-social-lean.md
  directions/C6-jtbd-forward-map.md
  synthesis/15-cross-cutting-patterns.md
  synthesis/16-monetization-filter.md
  synthesis/17-layer-stack-scorecard.md
  synthesis/18-reconciliation-with-threat-map.md
  citation-index.md
```

## Decisions (resolved 2026-06-09)

1. **Operational front-door anchor** = **Doctolib** (DrLeap was a mishearing). Studied here as the front-door *playbook* (how it won the operational layer), not as a threat. Research stays outside-in; Ditto's own context enters only in the "white space for Ditto" closes and the synthesis.
2. **Folder** = `market-deep-dive/` (sibling to `market-trend-analysis/`).
3. **Execution** = parallel `Agent` dispatch per field (not a single orchestrated workflow).
4. **Cadence** = verify as we go; come back to Merlijn only when a real fork or a quality/validation gap needs his input, rather than a fixed per-brief checkpoint.
