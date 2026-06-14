# ditto — Market Research (Healthcare · Health Tech · Consumer Health)

**For:** ditto.care · **Compiled:** 2026-06-10 · **Branch:** `claude/market-research-synthesis-ltz3lu`

A holistic, cited, reusable view of *what is happening in the market* — across healthcare, health tech and consumer health — for a patient comprehension companion. Mostly EU-anchored (NL + DACH), with explicit US & global benchmarks. Built to be discussed with the team and returned to without re-doing the research.

## How to navigate

**The deck:** [`market-research-deck.html`](market-research-deck.html) — open in any browser (self-contained, offline, **51 slides** in a consultant pyramid: 9 section dividers → supporting slides → a **ⓘ Deep dive** overlay on every detail slide with the reasoning, named players, and clickable sources). Use ← / → or Space; click any **ⓘ Deep dive** (or press **i**); Esc closes.
**The argument:** [`synthesis/S1-market-framework-and-direction.md`](synthesis/S1-market-framework-and-direction.md) (what's happening + where it's going) → [`synthesis/S2-implications-for-ditto.md`](synthesis/S2-implications-for-ditto.md) (where to play / watch / avoid).
**The evidence:** the `findings/` files below — every claim cited, tiered, confidence-tagged, with US→EU flags.

## Contents

| File | What it is |
|---|---|
| [`00-research-plan.md`](00-research-plan.md) | Methodology, framework (3 markets × 4 forces), scope, source bar |
| **Findings (fresh research, June 2026)** | |
| [`findings/M1-market-landscape-sizing.md`](findings/M1-market-landscape-sizing.md) | Market sizing & funding flows; the clinician-vs-patient capital split; EU vs US structure; DiGA |
| [`findings/M2-macro-trends.md`](findings/M2-macro-trends.md) | Consumerization · LLM health usage (40M/day) · grounded answers · B2B2C shift · value-based care · data-as-moat |
| [`findings/M3-data-infrastructure.md`](findings/M3-data-infrastructure.md) | EHDS · NL PGO/MedMij/BGZ/Wegiz · DE ePA · FHIR · consent · proxy/caregiver rights |
| [`findings/M4-competitor-landscape.md`](findings/M4-competitor-landscape.md) | Refreshed full landscape + the 2026 Big Tech consumer-health-AI wave + the whitespace map |
| [`findings/M5-kin-and-direct-competitors.md`](findings/M5-kin-and-direct-competitors.md) | **Kin deep-dive + Kin-vs-ditto feature matrix** + Hedy/Patiently/Abridge |
| [`findings/M6-feature-direction-traction.md`](findings/M6-feature-direction-traction.md) | Traction: AI assistants · grounded/cited (OpenEvidence) · coaches · symptom tracking · journaling/logging |
| [`findings/M7-consumer-health-retention.md`](findings/M7-consumer-health-retention.md) | Why cycle/meditation win & symptom trackers churn; the 7-gate retention checklist |
| [`findings/M8-strategic-moves-map.md`](findings/M8-strategic-moves-map.md) | How players migrate (scribe→billing→workflow; single→platform; D2C→B2B2C) |
| **Findings (round 2 — depth & recency, for the deep-dive overlays)** | |
| [`findings/M9-funding-recency-leaderboards.md`](findings/M9-funding-recency-leaderboards.md) | Q1 2026 funding · consumer-app leaderboards 2024/25/26 · Europe top-10 · NL white-space |
| [`findings/M10-consumer-app-deepdives.md`](findings/M10-consumer-app-deepdives.md) | Profiles: cycle/pregnancy · meditation · journaling (Finch/Daylio/Bearable) · fitness super-apps & wearables |
| [`findings/M11-ai-frontdoor-deepdive.md`](findings/M11-ai-frontdoor-deepdive.md) | Dr Google vs Dr ChatGPT scale · named payer/provider bots · diagnostic-accuracy research · consumer grounded engines |
| [`findings/M12-consumerization-comprehension.md`](findings/M12-consumerization-comprehension.md) | Scheduling shift (Doctolib/NHS App) · plain-language reality check · comprehension↔adherence · data moat |
| [`findings/M13-partnerships-eu-scribes-eu-block.md`](findings/M13-partnerships-eu-scribes-eu-block.md) | Marquee partnerships · EU scribes + the EHDS-summary threat · why ChatGPT Health is EU-blocked |
| [`findings/M14-ai-mental-health-therapy.md`](findings/M14-ai-mental-health-therapy.md) | AI therapy chapter: LLM-as-therapist trend & risks · Ash/Slingshot, Wysa, Limbic, Therabot, Woebot · EU regs |
| [`findings/M15-winners-losers-why.md`](findings/M15-winners-losers-why.md) | Winners vs losers & **why**: symptom checkers (Ada/Babylon) · coaches (Hinge/Omada vs Noom) · trackers |
| **Findings (round 3 — the proven-mechanics playbook)** | |
| [`findings/M16-solution-catalogue.md`](findings/M16-solution-catalogue.md) | **152-product catalogue** in 16 categories (incl. non-health exemplars) — each tagged with mechanism, why-it-works, traction, adopt/innovate flag |
| [`findings/M17-table-stakes-mechanisms.md`](findings/M17-table-stakes-mechanisms.md) | The **10 table-stakes mechanisms** (definition · cited evidence · exemplars · failure mode · adopt-as-is vs innovate verdict) |
| **Synthesis** | |
| [`synthesis/S1-market-framework-and-direction.md`](synthesis/S1-market-framework-and-direction.md) | The lens + "where the puck is going" |
| [`synthesis/S2-implications-for-ditto.md`](synthesis/S2-implications-for-ditto.md) | Opportunities, watch-list, what-to-avoid, the strategic question |
| [`synthesis/S3-proven-mechanics-playbook.md`](synthesis/S3-proven-mechanics-playbook.md) | **The Pincus "proven → better" playbook**: adopt-as-is vs innovate-with-ditto for each mechanism, mapped to the market research + ditto's roadmap loop |
| [`sources.md`](sources.md) | Consolidated bibliography (all URLs, by tier) |
| [`reused/`](reused/) | Mirrored reference material from the prior healthcare-strategy round (see `reused/README.md`) |

## The one-paragraph takeaway

Demand for understanding is overwhelming — ~40 million people ask ChatGPT health questions **every day** — but capital, products and exits cluster on the **clinician** side, and general LLMs absorb consumer demand for free. Regulation is finally making patient data *available* (EHDS, NL BGZ/PGO, DE ePA), yet almost nobody opens it: access was solved, **comprehension was not** (Germany auto-enrolled ~70M into ePA; ~3.6% use it). Big Tech validated the patient-comprehension category in early 2026 and is **blocked from the EU** on GDPR/MDR grounds, while clinician scribes and Epic reach into patient summaries from the visit (Dragon Copilot lands in NL early 2026; Epic "Emmie"). ditto's near-mirror competitor **Kin** ($9M seed, May 2026) shares its wedge and roadmap — so the edge is not features but **EU-native trust, the caregiver as co-user, cross-provider continuity, grounded-and-cited answers, and B2B2C reimbursement**, retained by turning the episodic summary into a daily, compounding, anticipatory question.

## Method & limitations

External/public sources only (no internal ditto data; no Drive/Confluence this round — Confluence was referenced but not reachable from this session). Built across two research rounds (M1–M8 landscape; M9–M15 depth & recency for the deck's deep-dive overlays). Tiered sourcing (Tier 1 official/peer-reviewed/analyst · Tier 2 reputable press · Tier 3 blog/self-report, flagged) with confidence levels and US→EU flags. The "40M ChatGPT health questions" figure was re-verified as **per day** (not per week). Several primary pages (OpenAI, some app stores, journals) blocked automated fetch; those figures are triangulated across multiple independent reports and flagged in the findings. Competitor self-claims (funding, MAU, retention) are treated as Tier 3 unless independently corroborated. See [`sources.md`](sources.md) and each findings file's caveats.
