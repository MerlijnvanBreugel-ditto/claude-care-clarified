# Brief D: US Demand-Side Macro Trends
**Workstream:** D — Consumer/Patient Demand Forces
**Published:** 2026-05-30
**Scope:** US as leading signal for European patient demand; relevant to patient-understanding and care-coordination apps
**Confidence level:** Medium-High (most claims sourced to 2024-2026 surveys; recall/literacy stats draw on older but widely-replicated research)

---

## Executive Summary

- **The information gap is the core problem.** Patients forget 40-80% of medical information immediately after a visit [1], and 29-72% of what they remember is incorrect [2]. This is not a niche edge case — it is the default human condition after a medical encounter.
- **Health literacy is in crisis at scale.** Only 12% of US adults are health-literate; ~90% struggle with basic healthcare information; low literacy costs the system an estimated $236B annually [3][4]. The population hardest hit (65+, low income, Medicaid) overlaps directly with heavy healthcare users.
- **63 million Americans are caregivers — a 45% surge in a decade.** Family caregivers now represent 1 in 4 US adults, contribute $1T in unpaid labor, and are increasingly managing complex medical tasks without training [5][6]. Care coordination is a primary pain point.
- **Chronic disease is the dominant demand engine.** 76% of US adults (194M people) have at least one chronic condition; 51% have two or more [7]. This cohort generates the bulk of medical encounters and the highest information burden.
- **Consumer AI adoption for health has doubled in one year.** 32% of US adults used AI chatbots for health information in 2025 (up from 16% in 2024, Rock Health [8]). Pew (April 2026) finds 22% use AI at least sometimes for health, driven by convenience and speed over accuracy [9].
- **Patient portal access has doubled since 2014 but coordination remains broken.** 65% of US adults accessed their medical records online in 2024 [10]; caregiver proxy access doubled to 51%. Yet 59% hold records across multiple portals; only 7% use an aggregator. Fragmentation is the bottleneck.
- **After-visit summary demand is validated but not yet well-served.** When given plain-language summaries, 90%+ of patients found them easy to understand; 38% of patients who received an AVS shared it with someone else [11]. The moment of "what did the doctor just say?" is a clear, high-frequency pain point with proven willingness to engage.

---

## Demand Vectors

### 1. Patient Empowerment / "E-Patient" Movement

**The trend.** The e-patient movement, catalyzed by the iPhone (2007) and accelerated by COVID, has matured from a fringe position into mainstream healthcare policy. Over 70% of patients now use digital health tools [12]. The 21st Century Cures Act (2016, implemented 2021) legally mandated patient access to nearly all EHR data including clinical notes — cementing data ownership as a right, not a privilege [10].

**Signal moments:**
- The #WeAreNotWaiting hashtag emerged from the OpenAPS community, where patients built insulin management systems that outperformed commercial alternatives — demonstrating patients as active system designers [13].
- FDA launched a Patient Engagement Advisory Committee in 2017; by 2020 the EU followed with the European Patient Engagement Resource Center [13].
- Patient-and-Public Involvement (PPI) is now standard in research across the US, UK, Australia, Denmark, and Germany [13].

**Patient portal data (2024, ONC/ASTP):**
- 65% of US individuals accessed online medical records in 2024 (up from 25% in 2014) [10]
- 77% were offered access; 89% of those encouraged by their provider actually used it [10]
- 51% accessed portals as proxy/caregiver for someone else — doubled from 24% in 2020 [10]
- 95% of US hospitals now enable patients to view clinical notes electronically [10]

**Contrarian note.** Engagement drops sharply without provider encouragement (57% vs. 87% access rate). The empowered e-patient is real but dependent on clinical nudging — passive users remain the majority.

**EU read-across.** EU EHR access reached 83% of member states in 2024 (up from 72% in 2022), with Belgium, Estonia, and Denmark at or near 100% [14]. The European Health Data Space (EHDS), proposed in 2022, will standardize patient data access EU-wide — NL is mid-adoption. The empowerment wave is arriving in Europe, roughly 2-4 years behind the US.

---

### 2. The Health Literacy Crisis

**Scale.** Only 12% of US adults are proficient in health literacy. Approximately 36% have basic or below-basic skills; some estimates put the share struggling with basic health information at ~90% when functional health literacy is included [3][4].

**Economic cost.** Low health literacy costs the US healthcare system an estimated $236-238B annually, accounting for 7-17% of all personal healthcare expenditure [3][4]. A 2003 IOM report ("Hidden in Plain Sight") first quantified this; subsequent analyses have consistently confirmed the magnitude.

*Note: The $236B figure draws on studies from the 2000s-2010s, methodology varies; treat as order-of-magnitude, not precise.* [INFERENCE]

**Who is affected.** The burden is not evenly distributed:
- Adults 65+: only 2% have proficient health literacy [3]
- Medicaid recipients: significantly more likely to have below-basic literacy than privately insured
- Low-education cohort recalls ~38% of doctor recommendations vs. ~65% for college graduates [2]

**The recall problem.** Patients forget 40-80% of medical information immediately after leaving a consultation [1][15]. Of what they retain, roughly half is recalled incorrectly [2]. This is not primarily a literacy issue — it is a cognitive load issue under stress. Even high-literacy patients forget. Plain-language summaries reduce the gap: personalized instructions improved comprehension to 96% "easy to understand" in one RCT [16].

**Contrarian note.** Plain-language AVS does not automatically drive behavior change. Medication adherence improvements from structured summaries (18-28%) are meaningful but modest [11]; the information gap is real, the causal pathway to outcomes is not automatic.

**EU read-across.** EU data is thinner. OECD (Health at a Glance Europe 2024) finds digital health literacy among primary care users 45+ is substantially below younger cohorts; low-education EU patients score 18 vs. 26 for high-education on digital health literacy [14]. The structural problem is comparable; the quantification lags the US.

---

### 3. The Caregiver Economy

**Scale (2025, AARP/NAC).**
- **63 million Americans** are family caregivers, a 45% increase over the past decade [5]
- 1 in 4 US adults; 59 million care for another adult [5]
- 29% are "sandwich generation" caregivers supporting both children and an adult [5]

**Economic value and burden.**
- Unpaid family caregiving is valued at **$1 trillion annually** (2024, AARP) [6]; prior estimates were $873.5B
- Average caregiver: 51 years old, 60% female, spending $7,200/year out of pocket [5]
- 44% provide high-intensity care; 55% perform complex medical or nursing tasks — yet only 22% receive any training [5]
- 23% are in debt due to caregiving; 20% report poor health [5]

**Coordination pain.** 70% of working-age caregivers are also employed [5]. Managing medical information across providers, tracking what the doctor said at the last appointment, and communicating with other family members are documented coordination failures — not luxuries. The after-visit summary is a natural coordination artifact.

**Caregiver proxy access to patient portals has doubled to 51% (2020-2024)** [10] — a direct demand signal for digital care coordination tools.

**Contrarian note.** Many caregivers are time-poor and tech-ambivalent. Products that require setup overhead or separate accounts face abandonment. Simplicity is a requirement, not a feature.

**EU read-across.** The Netherlands has 1.9 million informal caregivers (13% of adults 16+); they dedicate an average of 13 hours/week, up from 11 hours in 2015 [17]. The societal cost is €17.5-30.1B/year (2.15-3.71% of Dutch GDP) [18]. A 2025 Lancet Europe microsimulation projects the EU informal caregiving burden rising substantially through 2050 as populations age [19]. The care circle concept is directly applicable; NL is not behind the US on this demand.

---

### 4. Aging Population + Chronic-Disease Burden

**Demographics.**
- By 2040, 80.8M Americans will be 65+; by 2060, 94.7M (25% of total population) [20]
- The 85+ cohort is projected to triple by 2060 [20]

**Chronic disease burden (2023 CDC data):**
- **76.4% of US adults** (approximately 194 million people) report at least one chronic condition [7]
- **51.4%** have two or more conditions [7]
- Breakdown by life stage: 6 in 10 young adults, 8 in 10 midlife adults, 9 in 10 older adults have 1+ conditions [7]
- By 2050, the number of adults 50+ with at least one chronic disease is projected to nearly double from 71.5M to 142.7M [20]

**Healthcare demand implications.** Demand for adult primary care services was projected to grow 14% by 2025 (pre-pandemic baseline); chronic conditions like Alzheimer's, cardiovascular disease, and multi-morbidity are driving rising mortality and increasing complexity of each encounter [20].

**Relevance to Ditto.** Chronic disease patients are high-frequency healthcare users with complex information management needs across multiple providers. They are already Ditto's core oncology users, extrapolated to the broader chronic-condition population.

**Contrarian note.** High chronic disease prevalence does not automatically translate to digital health adoption. The 65+ cohort uses AI for health at one-third the rate of 18-29 year-olds (10% vs. 32%) [9]. The demand is there; the channel requires intentional design for older users.

**EU read-across.** Europe faces the same demographic curve. The EU's 65+ population is projected to grow from 21% (2023) to 29% by 2050 (Eurostat). Netherlands: 20.6% of the population is already 65+. Chronic disease burden statistics track the US with a slight lag in multi-morbidity prevalence.

---

### 5. Consumer AI Adoption for Health ("Dr. Google" → "Dr. ChatGPT")

**Adoption trajectory.**
- **32%** of US adults used AI chatbots for health information in 2025 — double the 16% in 2024 (Rock Health Consumer Adoption Survey, Dec 2025, n=8,000) [8]
- **22%** use AI for health at least sometimes; 7% do so often/extremely often (Pew, Oct 2025, n=5,111) [9]
- **32%** of US adults have turned to AI for physical or mental health information (KFF, Feb-Mar 2026, n=1,343) [21]

**Trust landscape.** Trust is conditional and divided:
- Among AI users: 69% trust AI "a great deal or fair amount" for health info (KFF) [21]; 92% were satisfied with responses
- Among non-users: only 18% trust AI for health (KFF) [21]
- Pew (2026): only 18% of AI users rate chatbot health info as "extremely or very accurate"; but 48% rate it as "extremely or very convenient" [9]
- Privacy concern is near-universal: 77% of all adults worried about medical data privacy with AI [21]

**Behavior after AI use (Rock Health 2025):**
- 81% of AI users took at least one relevant follow-up action [8]
- 40% consulted a provider after using AI; 42% searched for more information; 32% tried a new health behavior; 18% adjusted medications [8]

**Demographics.**
- 18-29: 36% use AI for physical health; 21% did not follow up with a doctor (KFF) [21]
- Uninsured: 11% use AI "often/extremely often" vs. 7% insured — AI as healthcare access substitute [9]
- ChatGPT is used by 23% of all US adults for health; Gemini by 15% (Rock Health) [8]

**Contrarian note.** Accuracy is the weak link. Pew's "convenient, not accurate" framing is the key finding to internalize. Consumers are using health AI despite low confidence in accuracy because the alternative (waiting for a provider) is too slow and expensive. This creates both the opportunity (a verified, provider-sourced summary) and the risk (competition from fast-but-unreliable general LLMs).

**EU read-across.** WHO Europe (April 2026): 50-63% of EU member states now deploy AI chatbots for patient support [22]. Cross-national research shows generative AI health use follows a shared early-adopter pattern across Europe. EU patient AI adoption lags US by 12-24 months but is accelerating. The convenience driver is identical; trust dynamics likely similar.

---

### 6. Demand for After-Visit Summaries / "What Did the Doctor Say?"

**The core gap.** Patients forget 40-80% of medical information immediately after leaving a consultation [1][15]; of what they remember, roughly half is wrong [2]. This is the direct problem Ditto solves.

**AVS usage data (US).**
- 82.8% of patients recall receiving an AVS; 67.4% consulted it; 45.9% consulted it more than once; **31.6% shared it with someone else** [16]
- Higher education and older age are positively associated with AVS consultation — but the unmet need is highest in the low-literacy/low-income population [16]
- When AI-generated summaries were tested in oncology (pilot study, 2025): 90.6% found information "very easy to understand"; 92.4% reported the summary captured the appointment "very well" [23]

**OpenNotes adoption.** As of 2024, 95% of US hospitals allow patients to view clinical notes electronically [10]. Among patients who read at least one note, 37.7% shared it with someone else [24]. Patients rated notes as "very important" for: taking care of their health (72.6%), feeling in control (69.9%), remembering the care plan (65.8%) [24].

**Sharing behavior.** Sharing the summary with family is already a documented behavior — not a hypothetical. 31-38% of patients who engage with AVS/notes share them. The "care circle" is a natural extension of an existing behavior.

**Oncology specificity.** 75% of patients recently diagnosed with cancer accessed their patient portal in 2024, above the 65% national average [10]. Cancer patients have above-average information hunger and higher stakes. This is Ditto's current beachhead — and the data supports it as a rational starting point.

**Contrarian note.** Current AVS quality is the bottleneck, not patient willingness. Standard EHR-generated summaries are often full of jargon, auto-populated boilerplate, and clinical shorthand. 29% of current AVS recipients cite excessive medical jargon as a barrier to comprehension [11]. The product opportunity is quality, not access.

**EU read-across.** No EU-wide equivalent of the ONC AVS mandate exists yet. The EHDS and 21st Century Cures-style data access requirements are at an earlier stage. The Netherlands uses GP summaries and referral letters but patient-facing AI summaries are nascent. This is a genuine first-mover window in Europe.

---

## Implications for Ditto

| Implication | Priority | Confidence |
|---|---|---|
| The core use case (after-visit comprehension) is validated at scale — not a hypothesis | Foundation | High |
| Caregiver/family sharing is a documented behavior (31-38% AVS sharing rate) — "care circle" is real, not aspirational | Core product bet | High |
| Oncology is the right beachhead: higher portal engagement, higher information hunger, higher stakes | Validate and expand | High |
| Health literacy gap creates product obligation: plain language must be non-negotiable, not a nice-to-have | Product requirement | High |
| AI health chatbots are eating the general "what did the doctor say?" query from below — Ditto's advantage is provider-sourced, verified, context-aware | Competitive moat | Medium-High |
| The 65+ user (highest literacy gap, lowest AI adoption) needs a dedicated UX strategy — the product must work for them or misses the highest-burden segment | Design debt | Medium |
| EU is 12-24 months behind US on consumer health AI; NL informal caregiver burden and aging demographics are EU-equivalent to US signals | Geographic timing | Medium |
| Privacy anxiety (77% of US adults) is a conversion barrier; GDPR compliance is both a legal floor and a marketing asset | Risk/opportunity | Medium |

---

## Risks & Caveats

1. **The convenience-vs-accuracy tradeoff cuts both ways.** Pew's finding that 48% find AI health info "convenient" but only 18% find it "accurate" is both a Ditto opportunity (accuracy) and a user acquisition risk (why switch from fast-and-free?).

2. **High-need populations are hard to reach digitally.** The 36% of Americans with basic/below-basic health literacy are also less likely to use patient portals, apps, or AI. Ditto's current app-first model skews toward the already-engaged patient.

3. **Provider friction is the real bottleneck.** 89% of patients encouraged by providers used portals vs. 57% without encouragement. Ditto's growth depends on clinical workflow integration, not consumer marketing alone.

4. **Caregiver burnout and digital fatigue.** 20% of caregivers report poor health; time-starved caregivers may not engage with another app. The product must deliver value in under 2 minutes or it won't survive.

5. **EU regulatory divergence.** GDPR is stricter than HIPAA on data sharing; AI-generated medical summaries may require regulatory clearance in some EU markets. This is an execution risk, not a demand risk.

6. **Recall statistics are from a fragmented body of research.** The "40-80%" figure is widely cited but spans heterogeneous settings (ambulatory, hospital, emergency) and decades. It is directionally correct; the specific percentage varies by context.

---

## Confidence & Gaps

| Claim | Source recency | Confidence |
|---|---|---|
| 32% US adults using AI for health (2025) | Dec 2025 (Rock Health) | High |
| 63M US caregivers, 45% increase | 2025 (AARP/NAC) | High |
| $1T caregiver labor value | 2024 (AARP) | High |
| 65% patient portal access (2024) | 2024 (ONC/ASTP) | High |
| 76.4% US adults have 1+ chronic condition | 2023 (CDC BRFSS) | High |
| 31.6% of AVS recipients share with someone | 2020-era RCT (JABFM) | Medium — needs replication in smartphone era |
| 40-80% of medical info forgotten immediately | 2003+ (replicated) | Medium-High — replicated but heterogeneous methods |
| $236B annual cost of low health literacy | 2007-2011 origin, widely cited | Medium — methodology varies; order-of-magnitude only |
| EU AI health chatbot adoption at 50-63% of member states | WHO Europe, April 2026 | High — but refers to hospital/health system deployment, not consumer use |
| Dutch caregiver statistics | 2023 (CBS Netherlands) | High |

**Gaps to address in Phase 2:**
- Direct NL/EU consumer survey data on AI chatbot use for health (patient-side, not system-side)
- Oncology-specific AVS sharing and comprehension rates post-LLM (only one pilot study found, preprint)
- Willingness-to-pay data for patient-facing health AI summaries
- Competitive landscape: how many apps are directly competing in the "after-visit summary" space in EU

---

## Sources

1. [Patients' memory for medical information — PMC/NIH (Kessels 2003)](https://pmc.ncbi.nlm.nih.gov/articles/PMC539473/)
2. [What Did the Doctor Say? Health Literacy and Recall of Medical Instructions — PMC (2012)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3305916/)
3. [Health Literacy Statistics 2025 — HealthcareGPS.ai (Mar 2025)](https://healthcaregps.ai/blog/2025/03/breaking-down-health-literacy-90-percent-americans-struggle)
4. [Health Literacy: Data Reports 2026 — WifiTalents](https://wifitalents.com/health-literacy-statistics/)
5. [Caregiving in the US 2025 — AARP/NAC](https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025/)
6. [Family Caregivers Account for $1 Trillion in Essential Care — AARP 2026](https://www.aarp.org/caregiving/financial-legal/valuing-the-invaluable-report-2026/)
7. [Trends in Multiple Chronic Conditions Among US Adults — CDC PCD 2025](https://www.cdc.gov/pcd/issues/2025/24_0539.htm)
8. [Rock Health 2025 Consumer Adoption Survey: Health AI Insights (Mar 2026)](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)
9. [Pew Research Center: Users of Social Media and AI Chatbots for Health Information (Apr 2026)](https://www.pewresearch.org/science/2026/04/07/users-of-social-media-and-ai-chatbots-for-health-information-are-more-likely-to-say-they-are-convenient-than-accurate/)
10. [ONC/ASTP: Individuals' Access and Use of Patient Portals and Smartphone Health Apps, 2024](https://healthit.gov/data/data-briefs/individuals-access-and-use-patient-portals-and-smartphone-health-apps-2024/)
11. [Patient-Reported Use of the After Visit Summary — PMC (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7705830/)
12. [A New Health Care Paradigm: The Power of Digital Health and E-Patients — PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11975701/)
13. [The Evolution of Patient Empowerment and Its Impact on Health Care's Future — JMIR/PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12082052/)
14. [Digital Decade 2025: eHealth Indicator Study — European Commission](https://digital-strategy.ec.europa.eu/en/library/digital-decade-2025-ehealth-indicator-study)
15. [Patients Forget 40-80% of What You Tell Them — Dya Clinical (cites Journal of Royal Society of Medicine)](https://www.dyaclinical.com/blog/patient-recall-consultation-summary)
16. [Association of Patient Recall, Satisfaction, and Adherence to AVS Content — JABFM (2014)](https://www.jabfm.org/content/27/2/209)
17. [How many people provide informal care? — CBS Netherlands in Numbers 2024](https://longreads.cbs.nl/the-netherlands-in-numbers-2024/how-many-people-provide-informal-care/)
18. [The Economic Costs of Informal Care in The Netherlands — PubMed (2024)](https://pubmed.ncbi.nlm.nih.gov/38294595/)
19. [The Burden of Informal Family Caregiving in Europe, 2000-2050 — The Lancet (2025)](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(25)00087-0/fulltext)
20. [Navigating the Future of Elderly Healthcare — PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11986089/)
21. [KFF Tracking Poll: Use of AI For Health Information and Advice (Mar 2026)](https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/)
22. [WHO/Europe: First-ever snapshot of AI in health care across EU Member States (Apr 2026)](https://www.who.int/europe/news/item/20-04-2026-new-who-europe-report-provides-first-ever-snapshot-of-ai-in-health-care-across-european-union-member-states)
23. [Patient-friendly summaries of oncology consultations generated by LLMs — medRxiv preprint (Oct 2025)](https://www.medrxiv.org/content/10.1101/2025.10.13.25337951.full.pdf)
24. [Insights and Trends in Open Note Access: Retrospective Observational Study — JMIR (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11688596/)
