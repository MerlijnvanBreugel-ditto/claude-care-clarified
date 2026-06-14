# S1 — The Market Framework & Where the Puck Is Going

**Prepared:** 2026-06-10 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Inputs:** findings `M1–M8` + reused `01/06/07/08b`. Every claim traces to a findings file (cited there with primary URLs); this synthesis names the source file in brackets, e.g. `[M4]`.

> This is the connective-tissue document: it states the lens, then reads the eight findings through it to answer "what is happening, and where is it going." `S2` turns this into implications for ditto.

---

## The lens: three concentric markets × four forces

```
  Healthcare system  ── the ocean: ~$5.3T US spend (18% GDP); EU universal, ~half the per-capita [M1]
   └ Health tech     ── the fast slice: ~$28.8B global VC 2025 (+9%), Europe fastest +15% [M1]
      └ Consumer health ── the inner ring closest to ditto: $6.8T wellness economy, but tiny app TAMs [M1]

  FOUR FORCES bending all three:
   1. Patient power / consumerization        — patients act like consumers; demand understanding [M2]
   2. AI & data                              — LLMs as default; grounding as the new trust bar [M2,M6]
   3. Regulation & data rights               — EHDS, PGO/BGZ, ePA, AI Act, MDR, GDPR [M3]
   4. Capital & business-model shifts        — money on the clinician side; D2C → B2B2C [M1,M2,M8]
```

---

## 1. The market as it stands (June 2026)

**The money is on the clinician side; the patient sits on the under-capitalised side of a giant market.** Of 2025's $14.2B US digital-health VC, AI-enabled companies took 54% and clinical/non-clinical workflow tooling ~42%; ambient AI scribes alone drew >$1B (Abridge $5.3B valuation; Ambience $1.25B). *Every* top-tier 2025 raise and both reopened IPOs (Hinge $2.6B, Omada) are B2B/B2B2C. Women's health — the closest consumer-health proxy — gets <2% of all VC `[M1]`. ditto's appointment-summary lands on the *patient* side of a market whose capital is on the *clinician/payer* side.

**Consumer demand, by contrast, is enormous — and is being captured by general LLMs, not health apps.** ~40 million people use ChatGPT for health questions *every day* (OpenAI, Jan 2026 — the widely-repeated "40M/week" figure is understated; it is per *day*), >5% of all ChatGPT messages are health-related, ~1 in 4 of 800M+ weekly users asks a health question weekly, and ~70% of those conversations happen outside clinical hours `[M2]`. 32% of US consumers used an AI chatbot for health in 2025 (up from 16% in 2024); 74% of them reached for general tools (ChatGPT, Gemini) over provider (5%) or payer (4%) bots `[M6]`. The demand for "help me understand my health" is overwhelming and unmet by the system.

**The category ditto sits in just got validated — and contested — by Big Tech, but only in the US.** In Jan–Mar 2026, OpenAI (ChatGPT Health), Anthropic (Claude for Healthcare), Amazon (One Medical Health AI), Google (Gemini Health Coach) and Microsoft (Copilot Health) all launched record-ingesting consumer health assistants. Crucially, **ChatGPT Health is explicitly unavailable in the EU/UK/Switzerland on GDPR + MDR grounds** `[M4]`. The "turn my records into understanding" job is now a proven, contested consumer category — and the leading product is legally blocked from Europe.

## 2. The four forces, read forward

**Force 1 — Patient power / consumerization (tailwind, structural).** Patients expect access, transparency and plain-language understanding; the EU is formalising plain-language summaries inside HTA `[M2]`. The *attention* shift toward the patient is real in the EU even where the *spend* shift (US patient-as-payer) is not. This is the demand-side engine under ditto's entire thesis.

**Force 2 — AI & data: grounding is the new frontier (tailwind + threat).** Raw fluency is commoditised; **provenance and grounding** are the emerging trust standard. OpenEvidence — RAG over licensed NEJM/JAMA with every answer cited and refusal-when-unsure — went $1B (Feb 2025) → $12B (Jan 2026), >40% of US physicians, ~20M consultations/month, but it is *clinician-facing* `[M2,M6]`. A *patient-language* grounded-and-cited answer layer is largely unoccupied. The threat: general LLMs are "good enough" and free, and the proprietary-data moat is softening as each model release narrows it `[M2]`.

**Force 3 — Regulation & data rights: the data is becoming available, but nobody can use it (tailwind + the core opportunity).** EHDS is in force; patient access + cross-border summaries become mandatory only 2029 (images/labs 2031), so 2026–2028 runs on national rails `[M3]`. The Netherlands has world-class plumbing — BGZ (a ~26-zib FHIR patient summary) now exchangeable to PGOs, Wegiz forcing exchange — but **PGO end-user adoption is low**. Germany auto-enrolled ~70M people into ePA, yet **only ~3.6% actively use it** `[M3]`. NL MedMij's own 2026 roadmap commits to making PGOs "more understandable" — an admission they are not `[M4]`. **The single clearest market fact: records are arriving for free; understanding is not built into them.** That gap is ditto's reason to exist, corroborated from inside the flagship national systems.

**Force 4 — Capital & business-model shifts: D2C is hard; B2B2C is the survivable path (constraint + direction).** Consumer health-app funding fell ~40% in H1 2025; disclosed digital-health partnerships grew 2,675 (2021) → 4,051 (2024); strategic CVCs are ~40% of active investors `[M2]`. Germany's DiGA is the EU's only mature patient-facing reimbursement on-ramp (61 apps, >1M prescriptions, €234M cumulative) — credible but small `[M1]`. The pattern across the market: pure D2C struggles to fund and retain; the durable model couples a consumer experience to a B2B2C distribution + reimbursement partner (in NL: zorgverzekeraars, hospital groups, GP cooperatives, pharma) `[M2,M8]`.

## 3. Where the puck is going — the five vectors `[M8]`

1. **Capture → workflow → revenue.** Every scribe (Abridge, Nabla, Ambience, Suki, Dragon) migrated from transcription into coding, orders, prior-auth and RCM within ~18 months — and **patient after-visit summaries are increasingly a feature *inside* the scribe envelope.** Dragon Copilot (with after-visit summaries) is landing in the **Netherlands in early 2026**, and **Epic's "Emmie"** gives plain-language explanations inside MyChart. These are the two most concrete encroachment signals on ditto's wedge.
2. **Single-utility → life-stage / multi-condition platform.** Flo (period → perimenopause → menopause, €1B+ unicorn) and Belong.Life (cancer → MS → weight) reuse one engagement engine across cohorts — the same generalisation ditto's "Living Health Companion" attempts. The path runs *through a beachhead cohort*, not all conditions at once.
3. **Data plumbing → comprehension.** Aggregation is commoditising into infrastructure (b.well went from PHR aggregator to a "Health AI SDK" now powering ChatGPT Health); value accrues to the comprehension layer. Aggregators climb up, AI giants reach down, ditto sits in the contested middle.
4. **D2C → B2B2C.** Ada (Berlin), Ro/Hims, Oviva and Sidekick all moved toward payer/pharma/provider distribution and (in the EU) reimbursement.
5. **Consumer-AI giants entering top-down.** ChatGPT Health normalises "ask AI about my records" at consumer scale — the wildcard that raises urgency.

## 4. What the consumer-health winners teach `[M7]`

Retention is a **category property, not an execution property**. The strongest consumer-health category in existence is **cycle/pregnancy tracking** (Flo retains ~60% of MAU past one year — ~2× the Health & Fitness norm; Clue passed 1M paid subscribers), because it pairs a **daily-relevant, anticipatory question whose answer changes** ("where am I in my cycle / is this normal") with **compounding personal data** and **life-stage urgency**. Meditation (Calm ~$596M revenue; Headspace DAU/MAU ~17%) retains via ritual + immediate reward but **decays**, because its reward is replaceable and its data doesn't compound. The losers — symptom trackers, generic logging, many disease-management apps — churn structurally: **~71% of health-app users disengage within 90 days**; chronic-disease app dropout pools ~43% `[M6,M7]`. They demand effort today for a deferred, abstract payoff, with weak external triggers and no compounding loop.

And the feature directions ditto is weighing inherit these patterns `[M6]`: **symptom tracking** is the weakest stand-alone bet (low accuracy — correct-first ~34% — *and* low retention); **grounded/cited answers** are the breakout trust model but only clinician-side so far; **AI coaches** show modest effect but chronic engagement decay (hybrid human+AI retains best); and the cautionary graveyard (Babylon's $4.2B→bankruptcy; Woebot's 2025 shutdown) teaches that **positioning as a medical device invites a regulatory burden that can kill the product** — especially under the EU AI Act + MDR high-risk regime (compliance Aug 2026/2027).

## 5. The one-paragraph reading of the market

The healthcare system is enormous and the demand for understanding is overwhelming (40M ChatGPT health questions a day), but the capital, the products and the exits cluster on the *clinician* side, and general LLMs are mopping up consumer demand for free. The data patients need is finally being made available by regulation (EHDS, BGZ/PGO, ePA) — yet almost nobody opens it, because access was solved and *comprehension* was not. Big Tech has validated the patient-comprehension category and is blocked from the EU on GDPR/MDR grounds, while clinician-side scribes and the EHR incumbent (Dragon Copilot in NL, Epic Emmie) reach into patient summaries from the visit. The market is collapsing toward two poles — clinician-side scribe superplatforms and consumer-side AI giants — and the defensible space between them is a **trust-anchored, EU-native, longitudinal, caregiver-inclusive patient-comprehension layer**, monetised through B2B2C/reimbursement rather than pure D2C, retained by manufacturing a daily-relevant, compounding question rather than an episodic summary.
