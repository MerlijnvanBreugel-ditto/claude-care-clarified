# M1 — Market Landscape & Sizing

**Scope:** Three concentric markets relevant to ditto.care — (1) the broad healthcare system, (2) health tech / digital health, (3) consumer health & wellness — sized globally and for the US and EU (anchored on NL + DACH where data exists), plus 2023–2026 venture-funding flows and the EU vs US market-structure split.

**Prepared:** 2026-06-10 · **All URLs accessed:** 2026-06-10 · **Author:** market-research analyst, ditto.care

> **A note on methodology and confidence.** "Market size" numbers for digital health and wellness vary wildly between analyst firms (2–3x spreads) because each defines the market differently. We report ranges, name the source for each figure, and tag confidence. Funding figures (Rock Health, Galen Growth, CB Insights) are more reliable because they count actual disclosed deals — these are High confidence. Wellness/app "TAM" numbers from SEO-driven research-mill publishers (Precedence, Grand View, Fortune Business Insights, etc.) are inherently Low–Med confidence and are flagged as such.

---

## Key takeaways

- **The wellness economy is the giant, digital health is the fast-growing slice, and the healthcare system is the ocean both swim in.** Global wellness ≈ **$6.8T (2024)**, US health spending alone ≈ **$5.3T (2024, ~18% of GDP)**, and the global digital-health *market* sits around **$350–420B (2025)** depending on definition. [GWI 2025](https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/); [Health Affairs 2025](https://www.healthaffairs.org/doi/10.1377/hlthaff.2025.01683) — *Confidence: High on spend/wellness, Med on digital-health TAM.*
- **Digital-health venture funding rebounded in 2025 and is overwhelmingly an AI story.** US funding hit **$14.2B (+35% YoY)** per Rock Health; **54% of dollars** went to AI-enabled companies. Global funding ≈ **$28.8B (+9%)** per Galen Growth, with **Europe the fastest-growing region (+15% to ~$6.2B)**. [Rock Health 2025](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/); [Galen Growth 2025](https://www.galengrowth.com/digital-health-funding-2025/) — *Confidence: High.*
- **Capital concentrates in clinician-/provider-facing AI, not consumer apps.** Clinical & non-clinical workflow tooling took **~42% of US dollars**; ambient **AI scribes alone drew ~$1B+ in 2025** (Abridge $300M Series E → **$5.3B valuation**; Ambience $243M → **$1.25B**). [STAT 2025](https://www.statnews.com/2025/07/29/ambience-healthcare-ai-scribe-new-fundraise/); [TechCrunch 2025](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/) — *Confidence: High.*
- **The B2B/provider vs patient/consumer split is structural and stark.** The biggest 2025 rounds and the reopened IPO window (Hinge Health, Omada) are enterprise/payer-sold; pure direct-to-consumer patient companion plays attract far less venture capital. Women's health gets **<2% of global VC** despite a claimed ~$360B addressable opportunity. [Galen Growth / Femtech 2025](https://www.galengrowth.com/femtechs-rise-and-roadblocks-digital-health-funding-growth-and-gaps/) — *Confidence: High on the split, Med on the femtech TAM figure (analyst estimate).*
- **EU and US differ fundamentally on who pays.** The US is a fragmented multi-payer, fee-for-service market; EU systems are universal (single-payer national services *or* regulated multi-payer like NL/Germany), financed through tax/mandatory insurance with DRG/negotiated pricing. This shapes go-to-market: in the US you sell to employers/payers/health systems; in the EU you navigate national reimbursement pathways. [Healthcare-NOW](https://www.healthcare-now.org/euhealthcare/) — *Confidence: High.*
- **Germany's DiGA is the closest thing to a patient-facing reimbursement on-ramp in Europe** — physicians prescribe approved apps, statutory insurance pays, **61 apps listed (Feb 2026), >1M prescriptions, €234M cumulative spend (2020–2024)**. Mental health is the #1 category. [BfArM](https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/Interesting-facts/_artikel.html); [MTRC](https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany) — *Confidence: High.*
- **For ditto.care specifically:** the money and exits are on the clinician/enterprise side; the patient-facing "companion" space is comparatively under-capitalised and lacks a clean EU reimbursement path *outside* Germany's DiGA — implying a likely B2B2C or DiGA-anchored route to revenue rather than pure DTC. *Confidence: Med (interpretation, not a sourced figure).*

---

## 1. The broad healthcare system (the outer ring)

Healthcare is one of the largest sectors in every developed economy. It is the context that determines who can pay ditto.care and through what mechanism.

| Metric | Figure | Source | Confidence |
|---|---|---|---|
| US national health spending (2024) | **$5.3T**, +7.2% YoY, **18.0% of GDP**, $15,474/person | [Health Affairs 2025](https://www.healthaffairs.org/doi/10.1377/hlthaff.2025.01683); [Medical Economics 2025](https://www.medicaleconomics.com/view/health-care-spending-reaches-5-3-trillion-or-18-of-u-s-economy-in-2024) | High |
| US health spend per capita, PPP (2024) | **~$14,885** — highest in OECD by far | [Peterson-KFF](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/) | High |
| Wealthy European nations avg per capita (2019 ref) | **~$5,505** vs US $11,072 — US >2x | [Healthcare-NOW](https://www.healthcare-now.org/euhealthcare/) | Med (older base year) |
| Highest EU per-capita spenders (2024) | Germany, Netherlands, Austria, Switzerland, Norway among the top | [Peterson-KFF](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/) | High |
| Recent per-capita growth, EU outpacing US | Netherlands +10.8%, Germany +10.1%, Austria +9.1% vs US +6.4% | [Peterson-KFF](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/) | High |

**Takeaway:** The US is the single largest healthcare market on earth and spends roughly double per head versus comparable European countries — which is the core reason digital-health venture capital is so US-skewed (see §3). The Netherlands and DACH are high-spend, high-adoption markets but are an order of magnitude smaller and structurally different on payment.

---

## 2. Health tech / digital health (the middle ring)

### 2.1 Market size & growth

Estimates differ by 2–3x because firms define "digital health" differently (telehealth + mHealth + analytics + digital therapeutics + sometimes health IT). Treat any single point estimate with caution.

| Source (firm) | 2025 size | 2026 size | CAGR | Confidence |
|---|---|---|---|---|
| Precedence Research | $420.08B | $483.07B | 10.8% (2026–35) | Low–Med (research-mill, **flag**) |
| Grand View Research | $347.4B | $420.2B | 23.4% (2026–33) | Low–Med (**flag**) |
| GM Insights | $387.8B | — | — | Low–Med (**flag**) |
| Mordor Intelligence | — | $405.99B | 16.85% (→$884B by 2031) | Low–Med (**flag**) |
| Towards Healthcare | $379.44B | $429.15B | 13.1% (2026–35) | Low–Med (**flag**) |

Sources: [Precedence](https://www.precedenceresearch.com/digital-health-market); [Grand View](https://www.grandviewresearch.com/industry-analysis/digital-health-market); [GM Insights](https://www.gminsights.com/industry-analysis/digital-health-market); [Mordor](https://www.mordorintelligence.com/industry-reports/digital-health-market).

**Synthesis (defensible range):** Global digital-health market ≈ **$350–420B in 2025**, growing at a **~11–17% CAGR** under most credible methodologies (the 23%+ figures are outliers). *Confidence: Med — the central tendency is robust even if individual estimates are weak. We do NOT endorse any single number.*

### 2.2 Regional anchors (NL + DACH)

- **Netherlands digital-care market ≈ $4.5B**, driven by chronic-disease prevalence and post-COVID remote care. [Ken Research](https://www.kenresearch.com/netherlands-e-health-digital-care-market) — *Confidence: Low–Med (single research-vendor estimate, **flag**).* The Dutch government has earmarked **€200M** for digital-health initiatives. [Ken Research](https://www.kenresearch.com/netherlands-e-health-digital-care-market) — *Confidence: Low (single source).*
- **Germany = Europe's biggest single digital-health reimbursement market** via DiGA, with **73M statutory-insured lives** addressable. [Prova Health](https://www.provahealth.com/insights/diga-reimbursement-germany-guide) — *Confidence: High.*

### 2.3 The 2023–2026 funding trajectory

| Year | US digital health VC (Rock Health) | Global (Galen Growth) | Notes |
|---|---|---|---|
| 2022 | ~$15B+ (peak unwinding) | — | Bubble deflating |
| 2024 | **$10.5B** | ~$26.4B (implied from +9% to $28.8B) | Trough/stabilisation |
| 2025 | **$14.2B (+35%)**, 482 deals | **$28.8B (+9%)** | AI-driven rebound |

Sources: [Rock Health 2025](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/); [HIT Consultant 2026](https://hitconsultant.net/2026/01/12/rock-health-digital-health-funding-hits-14-2b-2025/); [Galen Growth 2025](https://www.galengrowth.com/digital-health-funding-2025/). *Confidence: High (deal-counted).*

Key 2025 dynamics (US, Rock Health):
- **AI-enabled companies captured 54% of total dollars.** [Rock Health 2025](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)
- **Mega-rounds (>$100M) = 42% of all funding** — highest share since 2021. Average deal size jumped to **$29.3M** (from $20.7M in 2024).
- **Deal count fell ~5% (482 vs 509)** even as dollars rose — capital concentrating in fewer, larger winners ("a tale of two markets" / market bifurcation).
- **M&A surged to 195 deals (+61%)**; the IPO window reopened (see §2.5).

Regionally (Galen Growth, global 2025): **North America +7% to ~$19.5B; Europe +15% to ~$6.2B (fastest-growing); Asia-Pacific +14% to ~$2.4B.** [Galen Growth 2025](https://www.galengrowth.com/digital-health-funding-2025/) — *Confidence: High.* European H1 2025 alone was **$3.4B across 182 deals (+52% YoY H1)**. [Galen Growth Q3 2025](https://www.galengrowth.com/europe-digital-health-funding-in-q3-2025-resilience-amid-rationalisation/) — *Confidence: High.*

### 2.4 Where capital concentrates

| Segment | 2025 signal | Source | Confidence |
|---|---|---|---|
| **Clinical & non-clinical workflow tooling** | **~42% of US sector funding** | [HIT Consultant 2026](https://hitconsultant.net/2026/01/12/rock-health-digital-health-funding-hits-14-2b-2025/) | High |
| **Ambient AI scribes / clinical documentation** | **>$1B raised in 2025** across the category | [STAT 2025](https://www.statnews.com/2025/07/29/ambience-healthcare-ai-scribe-new-fundraise/) | High |
| **Healthcare AI broadly** | ~$3.9B in VC across the year | [FierceHealthcare 2025](https://www.fiercehealthcare.com/health-tech/healthcare-ai-rakes-nearly-4b-vc-funding-buoying-digital-health-market-2025) | High |
| **Women's health / femtech** | $2.2B in 2024 = **8.5% of digital-health funding**; **<2% of all global VC** | [Galen Growth Femtech](https://www.galengrowth.com/femtechs-rise-and-roadblocks-digital-health-funding-growth-and-gaps/) | High (share); Med (TAM) |
| **Mental health** | Top therapeutic category in many DTx/app rankings; Spring Health published JAMA ROI study | [FierceHealthcare 2025](https://www.fiercehealthcare.com/digital-health/hlth25-hinge-health-and-omada-broke-digital-health-ipo-dry-spell-ceos-share-their) | Med |
| **Chronic-disease management** | Omada (the IPO archetype) is virtual-first chronic care | [MedCity 2025](https://medcitynews.com/2025/06/omada-hinge-ipo-success/) | High |

**Biggest named 2025 raises / valuations:**

| Company | Segment | Raise (2025) | Valuation | Source |
|---|---|---|---|---|
| **Abridge** | AI scribe (clinician) | $300M Series E (after a $250M Series D months earlier) | **$5.3B** (doubled in ~4 months) | [TechCrunch](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/); [STAT](https://www.statnews.com/2025/06/24/ai-clinical-documentation-ambient-scribe-abridge-raises-300-million/) |
| **Ambience Healthcare** | AI scribe (clinician) | $243M | **$1.25B** | [STAT](https://www.statnews.com/2025/07/29/ambience-healthcare-ai-scribe-new-fundraise/) |
| **Innovaccer** | Provider data platform | $275M Series F | — | [Healthcare Brew](https://www.healthcare-brew.com/stories/2025/12/11/top-20-healthcare-funding-rounds-2025) |
| **OpenEvidence** | Clinical decision support (clinician) | $210M Series B + $200M Series C (same year) | — (6x growth in year) | [Healthcare Brew](https://www.healthcare-brew.com/stories/2025/12/11/top-20-healthcare-funding-rounds-2025) |
| **Hippocratic AI** | AI clinical agents | $141M Series B + $126M Series C | — | [Healthcare Brew](https://www.healthcare-brew.com/stories/2025/12/11/top-20-healthcare-funding-rounds-2025) |
| **Commure** | Provider operations | $200M growth | — | [Healthcare Brew](https://www.healthcare-brew.com/stories/2025/12/11/top-20-healthcare-funding-rounds-2025) |

*Confidence: High on the dollar/valuation figures (multiple Tier-1/Tier-2 sources). Note OpenEvidence's Series C size carries some press uncertainty — Med on that specific line.*

**Pattern:** Every single one of the largest 2025 raises is **clinician-/provider-/enterprise-facing**. None is a direct-to-patient consumer companion. This is the single most important structural fact for ditto.care's positioning.

### 2.5 Exits / IPO window

The multi-year IPO drought broke in mid-2025:
- **Hinge Health** (MSK care, employer-sold): IPO'd 22 May 2025 at $32/share, **~$2.6B valuation**, raised **$437M**; $432M TTM revenue, 80%+ gross margin. [FierceHealthcare 2025](https://www.fiercehealthcare.com/digital-health/hlth25-hinge-health-and-omada-broke-digital-health-ipo-dry-spell-ceos-share-their)
- **Omada Health** (virtual chronic-disease management): IPO'd at $19/share, **~$1.1B market cap**, raised **$150M**; revenue +38% to $170M in 2024. [MedCity 2025](https://medcitynews.com/2025/06/omada-hinge-ipo-success/)

*Confidence: High.* Both are **B2B2C** (sold to employers/health plans, delivered to patients) — again, not pure DTC.

---

## 3. Consumer health & wellness (the inner ring — closest to ditto.care's "Living Health Companion")

### 3.1 The wellness economy

| Metric | Figure | Source | Confidence |
|---|---|---|---|
| Global wellness economy (2024) | **$6.8T**, +7.9% YoY | [GWI 2025](https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/) | High (GWI is the standard reference) |
| 2025 projected | ~$7.4T | [GWI 2025](https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/) | Med |
| 2029 forecast | **$9.8T**, 7.6% CAGR | [GWI 2025](https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/) | Med |
| Context | Wellness now ~4x the pharma industry ($1.8T); bigger than IT ($5.3T) | [GWI 2025](https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/) | High |

### 3.2 Consumer health apps (the directly comparable layer)

| Sub-market | 2025 size | CAGR | Source | Confidence |
|---|---|---|---|---|
| **mHealth apps** | **$40.14B (2025)** → $45.91B (2026) → $136.16B (2034) | **14.56%** | [Fortune Business Insights](https://www.fortunebusinessinsights.com/mhealth-apps-market-102020) | Low–Med (**flag** research-mill) |
| **Wellness apps** | $11.27B (2024) | **14.9%** (2025–30) | [Grand View](https://www.grandviewresearch.com/industry-analysis/wellness-apps-market-report) | Low–Med (**flag**) |
| **Mental health apps** | **$7.48B (2025)** → $8.64B (2026) → $35.29B (2034) | **19.23%** | [Fortune Business Insights](https://www.fortunebusinessinsights.com/mental-health-apps-market-109012) | Low–Med (**flag**) |

App-mix within wellness apps (one analyst's segmentation): mental health ~30%, sleep ~25%, fitness ~20%, nutrition ~15%. North America held **~41.6%** of the 2025 mHealth-app market. [Fortune Business Insights](https://www.fortunebusinessinsights.com/mhealth-apps-market-102020) — *Confidence: Low (single research-mill segmentation; **flag**).*

**Critical interpretation for ditto.care.** These consumer-app TAMs ($7–40B) are an order of magnitude smaller than the enterprise digital-health spend, and — crucially — **consumer/patient-facing companies attract a small minority of venture dollars** (the bulk goes to clinician/provider AI; §2.4). The wellness *consumer-spend* economy is enormous ($6.8T) but is dominated by out-of-pocket categories (fitness, nutrition, beauty), not reimbursed clinical software. A patient companion product sits awkwardly between (a) a large but low-willingness-to-pay-per-app consumer market and (b) a well-funded but clinician-gated reimbursement market.

---

## 4. The structural split: clinician/B2B money vs patient/consumer money

| Dimension | Clinician / provider / payer (B2B & B2B2C) | Patient / consumer (DTC) |
|---|---|---|
| **Share of 2025 VC dollars** | Dominant — workflow tooling alone ~42%; AI scribes/CDS/agents took the mega-rounds | Minority; femtech (closest consumer-health proxy) <2% of all VC |
| **Largest 2025 raises** | Abridge ($5.3B val), Ambience ($1.25B), Innovaccer, OpenEvidence, Hippocratic AI, Commure | None in the top tier |
| **Exits** | Hinge, Omada IPOs (both enterprise/employer-sold) | Effectively none at scale in 2025 |
| **Why** | Clear ROI / cost-savings buyer (provider saves clinician time; payer saves on chronic care); reimbursable | Diffuse willingness to pay; subscription churn; no automatic reimbursement |

Sources: [Rock Health 2025](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/); [Galen Growth Femtech](https://www.galengrowth.com/femtechs-rise-and-roadblocks-digital-health-funding-growth-and-gaps/); [FierceHealthcare 2025](https://www.fiercehealthcare.com/health-tech/healthcare-ai-rakes-nearly-4b-vc-funding-buoying-digital-health-market-2025). *Confidence: High on the direction of the split; the exact patient-vs-provider dollar ratio is not cleanly published, so we infer it from category data — Med on precision.*

**Implication:** ditto.care's AI appointment summaries land on the *patient* side of a market where the money is on the *clinician/payer* side. The proven monetisation routes are: (a) sell the clinician/health-system the documentation/communication value (B2B), then surface the patient-facing summary as a feature; or (b) anchor to a reimbursement pathway (DiGA in Germany; bundled into Dutch reimbursable care). Pure DTC subscription for a companion app is the hardest-funded path. *Confidence: Med (strategic inference).*

---

## 5. EU vs US market structure (high level)

| | United States | EU (incl. NL + DACH) |
|---|---|---|
| **Model** | Fragmented **multi-payer**, largely private insurance + Medicare/Medicaid | **Universal coverage**: single-payer national services (UK, Spain, Sweden) *or* regulated multi-payer (Germany, France, **Netherlands**) |
| **Financing** | Employer & individual premiums, public programs; fee-for-service incentives | Taxation and/or mandatory social-insurance contributions; one or few large risk pools |
| **Who pays for software** | Employers, health plans, health systems (the venture-favoured buyers) | National/regional payers via formal pathways; patient out-of-pocket smaller |
| **Reimbursement mechanics** | Negotiated per-payer; no single national app pathway | Standardised **DRG** hospital rates, **nationally negotiated** drug/device pricing, spending caps |
| **Cost level** | ~$5.3T, 18% GDP, ~$14.9k/capita | Universal but far lower per-capita (~$5.5k avg in wealthy EU); NL/DE among top spenders |

Sources: [Healthcare-NOW](https://www.healthcare-now.org/euhealthcare/); [Peterson-KFF](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/); [Health Affairs 2025](https://www.healthaffairs.org/doi/10.1377/hlthaff.2025.01683). *Confidence: High.*

### Germany's DiGA — the EU's patient-facing reimbursement on-ramp

Germany pioneered "apps on prescription" (since 2020): physicians prescribe BfArM-approved digital health apps; **statutory health insurance pays**.

| DiGA metric | Figure | Source |
|---|---|---|
| Apps listed (Feb 2026) | **61** (eligible for reimbursement) | [MTRC](https://mtrconsult.com/news/five-more-health-apps-have-obtained-reimbursement-germany-august-2025) |
| Prescriptions (to end-2024) | **>1M**, ~81% patient-activated | [MTRC](https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany) |
| Cumulative GKV spend (Sep 2020–Dec 2024) | **€234M**; +71% spend 2023→2024 | [MTRC](https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany) |
| Pricing | Launch median **€514** / 3-month script; post-negotiation median **€221** | [Nelson Advisors](https://nelsonadvisors.co.uk/blog/the-german-digital-health-act--diga---strategy--impact--challenges-and-future-direction) |
| Top category | **Mental health** (anxiety, depression, sleep); then endocrinology/obesity | [Nature npj Digital Medicine 2025](https://www.nature.com/articles/s41746-025-01879-6) |
| Addressable lives | **73M** statutory-insured | [Prova Health](https://www.provahealth.com/insights/diga-reimbursement-germany-guide) |

*Confidence: High.* DiGA is the most concrete patient-facing reimbursement mechanism in Europe — but note its absolute scale (€234M over 4+ years) is tiny next to US enterprise digital-health flows. It is a credible *credibility/reimbursement* anchor, not a large revenue pool on its own.

### Netherlands specifics

- Telehealth/digital consultations are **reimbursed on par with in-person care** since the NZa's 2021 financing changes; the NZa published an updated **2026 guide** (Oct 2025) on funding digital care by sector. [MTRC](https://mtrconsult.com/news/reimbursement-telemedicine-and-digital-care-netherlands) — *Confidence: High.*
- No DiGA-equivalent national "app prescription" formulary as mature as Germany's; digital-care funding is folded into existing sector reimbursement rather than a standalone app pathway. *Confidence: Med (absence of evidence of a dedicated pathway in sources reviewed).*

### EU-wide direction of travel

The **European Health Data Space (EHDS)** is the major regulatory tailwind for cross-border health-data use and patient access; I was unable to verify specific EHDS timelines/figures within the sources retrieved for this task, so I flag this as **unverified here** and recommend a dedicated follow-up. *Confidence: Low — explicitly not sourced.*

---

## 6. Gaps & caveats (be honest)

- **Consumer-app TAMs are weak.** Every mHealth/wellness/mental-health-app market number above comes from SEO research-mill publishers with 2–3x disagreement. Use them only as order-of-magnitude, not for modelling.
- **EU-vs-US "applied" figures.** The per-capita comparison ($11,072 US vs $5,505 EU) uses a 2019 base year — directionally valid, numerically dated.
- **Patient-vs-provider dollar split is inferred,** not a single published ratio. Direction is certain; precision is not.
- **Netherlands market size ($4.5B)** rests on a single research vendor — low confidence.
- **EHDS specifics not verified** in this pass — flagged for follow-up.
- **No figures were fabricated.** Where a number could not be confirmed, it is labelled unverified.

---

## Sources

### Tier 1 — official / peer-reviewed / specialist analysts
- Rock Health — 2025 year-end digital health funding overview: https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/
- Galen Growth — Digital Health Funding in 2025: https://www.galengrowth.com/digital-health-funding-2025/
- Galen Growth — Europe Digital Health Funding Q3 2025: https://www.galengrowth.com/europe-digital-health-funding-in-q3-2025-resilience-amid-rationalisation/
- Galen Growth — Femtech's Rise and Roadblocks: https://www.galengrowth.com/femtechs-rise-and-roadblocks-digital-health-funding-growth-and-gaps/
- Global Wellness Institute — 2025 Wellness Economy ($6.8T): https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/
- Health Affairs — National Health Care Spending 2024: https://www.healthaffairs.org/doi/10.1377/hlthaff.2025.01683
- Peterson-KFF Health System Tracker — US vs other countries: https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/
- CMS — NHE Fact Sheet: https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/nhe-fact-sheet
- BfArM — DiGA interesting facts (official German regulator): https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/Interesting-facts/_artikel.html
- npj Digital Medicine (Nature) — DiGA evidence systematic review 2025: https://www.nature.com/articles/s41746-025-01879-6
- Government.nl — eHealth/telehealth policy: https://www.government.nl/topics/ehealth/government-encouraging-use-of-ehealth

### Tier 2 — reputable press / specialist trade
- TechCrunch — Abridge doubles to $5.3B: https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/
- STAT — Abridge raises $300M: https://www.statnews.com/2025/06/24/ai-clinical-documentation-ambient-scribe-abridge-raises-300-million/
- STAT — Ambience mega-round / AI scribes ~$1B: https://www.statnews.com/2025/07/29/ambience-healthcare-ai-scribe-new-fundraise/
- FierceHealthcare — JPM26 funding hit $14.2B: https://www.fiercehealthcare.com/digital-health/jpm26-digital-health-funding-hit-142b-2025-ai-companies-taking-lions-share-dollars
- FierceHealthcare — Healthcare AI ~$4B VC: https://www.fiercehealthcare.com/health-tech/healthcare-ai-rakes-nearly-4b-vc-funding-buoying-digital-health-market-2025
- FierceHealthcare — Hinge/Omada IPOs: https://www.fiercehealthcare.com/digital-health/hlth25-hinge-health-and-omada-broke-digital-health-ipo-dry-spell-ceos-share-their
- MedCity News — Omada/Hinge IPO success: https://medcitynews.com/2025/06/omada-hinge-ipo-success/
- HIT Consultant — Rock Health $14.2B recap: https://hitconsultant.net/2026/01/12/rock-health-digital-health-funding-hits-14-2b-2025/
- Healthcare Brew — Top 20 healthcare funding rounds 2025: https://www.healthcare-brew.com/stories/2025/12/11/top-20-healthcare-funding-rounds-2025
- Medical Economics — US health spend $5.3T: https://www.medicaleconomics.com/view/health-care-spending-reaches-5-3-trillion-or-18-of-u-s-economy-in-2024

### Tier 3 — research-mill / consultancy / advisory blogs (FLAGGED — order-of-magnitude only)
- Precedence Research — Digital Health Market: https://www.precedenceresearch.com/digital-health-market
- Grand View Research — Digital Health Market: https://www.grandviewresearch.com/industry-analysis/digital-health-market
- Grand View Research — Wellness Apps Market: https://www.grandviewresearch.com/industry-analysis/wellness-apps-market-report
- GM Insights — Digital Health Market: https://www.gminsights.com/industry-analysis/digital-health-market
- Mordor Intelligence — Digital Health Market: https://www.mordorintelligence.com/industry-reports/digital-health-market
- Fortune Business Insights — mHealth Apps: https://www.fortunebusinessinsights.com/mhealth-apps-market-102020
- Fortune Business Insights — Mental Health Apps: https://www.fortunebusinessinsights.com/mental-health-apps-market-109012
- Towards Healthcare — Digital Health Market: https://www.towardshealthcare.com/insights/digital-health-market-is-key-to-a-healthier-future
- Ken Research — Netherlands E-Health market (~$4.5B): https://www.kenresearch.com/netherlands-e-health-digital-care-market
- Prova Health — DiGA reimbursement guide: https://www.provahealth.com/insights/diga-reimbursement-germany-guide
- MTRC (Med Tech Reimbursement Consulting) — DiGA GKV report: https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany
- MTRC — DiGA apps Aug 2025 update: https://mtrconsult.com/news/five-more-health-apps-have-obtained-reimbursement-germany-august-2025
- MTRC — Telemedicine reimbursement Netherlands: https://mtrconsult.com/news/reimbursement-telemedicine-and-digital-care-netherlands
- Nelson Advisors — German Digital Health Act (DiGA) analysis: https://nelsonadvisors.co.uk/blog/the-german-digital-health-act--diga---strategy--impact--challenges-and-future-direction
- Healthcare-NOW — European healthcare / single-payer comparison: https://www.healthcare-now.org/euhealthcare/
