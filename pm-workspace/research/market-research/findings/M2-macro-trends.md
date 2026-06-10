# M2 — Macro Market Trends: Healthcare / Health Tech / Consumer Health

**Prepared for:** ditto.care (NL-based digital health; AI patient-facing appointment summaries → "Living Health Companion")
**Access date:** 2026-06-10
**Source window:** prioritised 2024–2026
**Confidence legend:** High / Med / Low. **Source tiers:** T1 = official/peer-reviewed/analyst; T2 = reputable press; T3 = blog/self-report (FLAGGED).
**Geo flag:** Most quantified data is US/global. EU (NL/DACH) applicability flagged inline where it diverges.

---

## Key takeaways

- **The headline "40M/week" claim is materially understated — the verified figure is ~40 million people using ChatGPT for health *every day*, per a January 2026 OpenAI report tied to its "ChatGPT Health" launch.** OpenAI also says >5% of all ChatGPT messages globally are healthcare-related, and ~1 in 4 of its 800M+ weekly users sends a health prompt each week ([OpenAI / Healthcare Dive, 2026](https://www.healthcaredive.com/news/40-million-use-chatgpt-health-questions-openai/808861/); [Axios, 2026](https://www.axios.com/2026/01/05/chatgpt-openai-health-insurance-aca)). **Confidence: High** that the real claim is "per day," not "per week."
- **Consumerization is the dominant demand-side trend:** patients now behave like consumers — expecting digital access, price/clinical transparency, and plain-language understanding — and this is the exact wedge ditto's product addresses ([Deloitte, 2024](https://www.deloitte.com/global/en/Industries/life-sciences-health-care/research/global-consumer-trends-in-health-care.html); [PwC Health Consumer Survey, 2025](https://www.pwc.com/us/en/industries/health-industries/library/healthcare-consumer-insights-survey.html)).
- **"Dr. Google → Dr. ChatGPT" is real and accelerating,** but trust is throttled by accuracy/hallucination concerns; LLM diagnostic accuracy is now strong (~76–78% on study benchmarks) yet still positioned as a clinician aid, not a patient-grade replacement ([NPR, 2023](https://www.npr.org/sections/health-shots/2023/09/16/1199924303/chatgpt-ai-medical-advice); [EurekAlert/study, 2026](https://www.eurekalert.org/news-releases/1129964); [MIT Tech Review, 2026](https://www.technologyreview.com/2026/01/22/1131692/dr-google-had-its-issues-can-chatgpt-health-do-better/)).
- **The market is shifting from "plausible" to "grounded/cited" medical answers.** OpenEvidence — RAG over NEJM/JAMA with every output source-linked — went from a $1B valuation (Feb 2025) to $12B (Jan 2026), used by >40% of US physicians. This validates the demand for evidence-grounded, citable AI in health ([CNBC, 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html); [Becker's, 2025](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/)).
- **Go-to-market is rotating from pure D2C to B2B2C/partnerships.** Consumer health app funding fell ~40% H1 2025; disclosed digital-health collaborations grew from 2,675 (2021) to 4,051 (2024), ~14–15% CAGR. Winners build distribution through providers, payers, pharma and employers ([Galen Growth, 2025](https://www.galengrowth.com/digital-health-exits-navigating-2025s-shifting-tides-towards-maturity/); [DrugPatentWatch, 2025](https://www.drugpatentwatch.com/blog/the-great-convergence-pharmaceuticals-digital-health-and-the-direct-to-patient-paradigm/)) — T3, FLAGGED.
- **Value-based care is structurally entrenched in the US (CMS targets ~all Medicare beneficiaries in VBC by 2030) and outcomes-led in EU systems via centralised registries (e.g. NL Heart Registry).** Outcomes data is becoming the unit of account ([Optum, 2025](https://business.optum.com/en/insights/state-value-based-care-2025-growth-challenges.html); [VBHC scoping review, PMC, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12084849/)).
- **Longitudinal personal-health data is still a moat — but a softening one.** Accumulated, cross-visit data creates lock-in and cross-sell value, yet each LLM release narrows the proprietary-data advantage. For ditto, the durable moat is *patient-owned longitudinal context* (the daily companion), not model IP ([Insignia, 2025](https://review.insignia.vc/2025/03/10/ai-moat/); [Healthcare.Digital, 2025](https://www.healthcare.digital/single-post/the-different-types-of-moat-creating-sustainable-competitive-advantage-in-healthtech)) — T3, FLAGGED.

---

## 1. Patient power / consumerization of health

The structural demand-side shift underpinning ditto is the **consumerization of healthcare**: patients increasingly behave like consumers in other industries, expecting digital-first access, transparency on price and clinical content, personalization, and information they can actually understand. Patients are described as "no longer passive recipients of care — informed, empowered, and demanding more: convenience, transparency, personalization, and digital access" ([Kyruus, 2025](https://kyruushealth.com/healthcare-consumerism-trends/) — T3, FLAGGED; corroborated by analyst sources below). **Confidence: High** that this is a genuine, widely-evidenced macro trend.

Three concrete expectation shifts matter for a patient-summary/companion product:

1. **Access & convenience.** Online scheduling, virtual consults, portal access, and digital communication have moved from "nice to have" to baseline expectation ([eMarketer, 2025](https://www.emarketer.com/content/the-2025-healthcare-consumer); [PwC, 2025](https://www.pwc.com/us/en/industries/health-industries/library/healthcare-consumer-insights-survey.html), T2/T1).
2. **Transparency.** Patients want to know costs and clinical reasoning up front; in the US, price-transparency mandates exist but execution is poor (one figure: ~81% of provider-directory entries still contain inconsistencies) ([Kyruus, 2025](https://kyruushealth.com/healthcare-consumerism-trends/) — T3, FLAGGED).
3. **Plain-language understanding.** There is an explicit policy and patient-advocacy movement toward plain-language health information. In Europe, plain-language summaries are being formally evaluated within Health Technology Assessment (HTA) processes to empower patient participation ([PP94 / PMC, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12768806/), T1). This is **directly EU-applicable** and aligns precisely with ditto's "translate the appointment into language the patient understands" thesis.

**EU/NL applicability — High.** Deloitte's multi-country consumer-health work has repeatedly included the Netherlands, Germany, Denmark and the UK, confirming the consumerization trend is not US-only ([Deloitte global consumer trends, 2024](https://www.deloitte.com/global/en/Industries/life-sciences-health-care/research/global-consumer-trends-in-health-care.html), T1). The attention/spend shift "toward the patient" is most quantified in the US (where patients bear more direct cost), so the *spend* dimension is weaker in single-payer-leaning EU systems; the *attention/empowerment* dimension is strongly present in EU too. **Flag:** treat US "patient-as-payer" framing with caution for NL.

---

## 2. LLM / generative-AI consumer-health usage — and verifying the "40M" claim

### 2.1 The verified figure (the key task)

**Claim under test:** "ChatGPT is used ~40 million times per week for health-related questions."

**Verified reality:** The real, sourced figure is **~40 million people using ChatGPT for health questions *per day*, not per week** — a *larger* and more striking number than the claim. This comes from an **OpenAI report released ~5 January 2026**, alongside/ahead of its **"ChatGPT Health"** launch. Multiple independent outlets reported it consistently:

- "**More than 40 million people ask ChatGPT healthcare questions every day**" ([Healthcare Dive, 2026](https://www.healthcaredive.com/news/40-million-use-chatgpt-health-questions-openai/808861/), T2).
- "**Exclusive: 40 million people turn to ChatGPT for health care**" ([Axios, 2026](https://www.axios.com/2026/01/05/chatgpt-openai-health-insurance-aca), T2).
- "**OpenAI says 40 million people use ChatGPT for health advice every day**" ([TechRadar, 2026](https://www.techradar.com/ai-platforms-assistants/openai/openai-says-40-million-people-use-chatgpt-for-healthcare-every-day), T2).
- "**40 million people now use ChatGPT daily for health questions**" ([Medical Economics, 2026](https://www.medicaleconomics.com/view/40-million-people-now-use-chatgpt-daily-for-health-questions-openai-report-finds), T2).

Supporting OpenAI-reported metrics from the same report:

- **>5% of all ChatGPT messages globally are about healthcare** — "averaging billions of messages each week."
- Of **800M+ weekly users, ~1 in 4 submits a health prompt every week.**
- **~1.5–2 million health-insurance questions per week** (plan comparison, claims, billing, pricing).
- **~70% (7 in 10) of health conversations occur outside typical clinical hours** — a strong signal that people turn to AI when they cannot reach a provider (directly relevant to a 24/7 companion).
- Self-reported use types: **55% checked/explored symptoms, 48% understood medical terms/instructions, >40% explored treatment options** ([Healthcare Dive, 2026](https://www.healthcaredive.com/news/40-million-use-chatgpt-health-questions-openai/808861/); [Fierce Healthcare, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says), T2).

**Verdict: the "40M/week" claim is directionally right but mis-stated — the source says ~40M/day.** When citing externally, use: *"~40 million people use ChatGPT for health questions every day, and >5% of all ChatGPT messages are healthcare-related (OpenAI, Jan 2026)."* **Confidence: High** (multiple concordant T2 reports of an OpenAI primary report; OpenAI's own pages were 403-blocked at access time, so the underlying *primary* PDF was not directly read — flagged as a minor verification gap). **Geo flag:** OpenAI figures are global; no NL-specific split published.

### 2.2 Independent corroboration: the NBER / OpenAI "How People Use ChatGPT" paper

A separate, peer-grade source triangulates the scale. The **NBER working paper w34255, "How People Use ChatGPT"** (Chatterji, Cunningham, Deming, Hitzig, Ong, Shan, Wadman; **Sept 2025**) analysed ~1.5M conversations and reports:

- By **July 2025, ~700 million users sent ~18 billion messages per week** (~10% of the global adult population).
- **Non-work usage grew from 53% to >70%** of all messages — i.e. ChatGPT is increasingly a *personal-life* assistant, the category health questions sit in.
- **"Practical Guidance," "Seeking Information," and "Writing" ≈ 80% of all conversations.** "Seeking Information" is "a very close substitute for web search."
- **49% of messages are "Asking" (advice/explanation) vs ~40% "Doing"** — people most value ChatGPT as an *advisor*, which is exactly the posture of a health-explanation tool ([NBER w34255, 2025](https://www.nber.org/papers/w34255); [SSRN, 2025](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5487080); [HBS AI Institute, 2025](https://aiinstitute.hbs.edu/heres-what-people-actually-do-with-chatgpt/), T1). **Confidence: High.** Note: the NBER paper itself does not isolate a single "health %"; the ~5%/40M-per-day health figures come from OpenAI's later (Jan 2026) health-specific analysis, not from w34255 — do not conflate the two.

### 2.3 Dr. Google → Dr. ChatGPT: trust and accuracy

The behavioural shift from web search ("Dr. Google") to conversational AI ("Dr. ChatGPT") has been tracked since 2023 ([NPR, 2023](https://www.npr.org/sections/health-shots/2023/09/16/1199924303/chatgpt-ai-medical-advice), T2) and is now mainstream. The open question is **trust vs. accuracy**:

- A 2026 study found AI responses to healthcare queries are **~76% accurate**; OpenAI's o1 model hit ~78% on complex diagnostic cases and outperformed ER physicians on diagnosis in some setups ([EurekAlert, 2026](https://www.eurekalert.org/news-releases/1129964); [The Conversation, 2025](https://theconversation.com/dr-chatgpt-is-getting-remarkably-good-at-diagnosing-health-problems-but-actual-doctors-are-still-better-at-weighing-treatment-options-281813), T2/T1).
- **But hallucination and the patient-vs-clinician gap remain the core risk.** Models do well *in the hands of trained clinicians*; patient-grade safety (especially in specialties like neurology/dermatology) is unresolved, and MIT Tech Review explicitly frames "ChatGPT Health" as inheriting Dr. Google's reliability problem unless grounded ([MIT Tech Review, 2026](https://www.technologyreview.com/2026/01/22/1131692/dr-google-had-its-issues-can-chatgpt-health-do-better/), T2).

**Implication for ditto:** the volume proves demand; the accuracy/trust gap is the wedge. A product that grounds answers in *the patient's own clinical record + cited evidence* is differentiated precisely where generic LLMs are weakest. **Confidence: High** on the strategic read.

---

## 3. The shift toward grounded / cited / truthful medical answers

A clear market signal is that **"plausible-sounding" is no longer enough — buyers and users want evidence-grounded, citable answers** (retrieval-augmented generation over trusted medical literature, with sources linked). The clearest proof point is **OpenEvidence** (framed here; a separate file does the deep traction scan):

- Positioned as "ChatGPT for doctors," it uses **RAG plus medical ontologies (SNOMED CT, MeSH), trained on NEJM and JAMA content, with every output linked to its source** ([Becker's, 2025](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/), T2).
- **Valuation trajectory:** ~$1B (Feb 2025) → $3.5B (Jul 2025) → $6B (Oct 2025) → **$12B (Jan 2026)** ([TechCrunch, 2025](https://techcrunch.com/2025/10/20/openevidence-the-chatgpt-for-doctors-raises-200m-at-6b-valuation/); [CNBC, 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html), T2).
- **Adoption:** reportedly used by **>40% of US physicians**, ~757k verified clinicians, ~15M consultations/month, ~$100M revenue by Jan 2026 ([Becker's, 2025](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/); [CNBC, 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html), T2).

The trend: **the next competitive frontier in health AI is provenance and grounding, not raw fluency.** Even OpenAI is moving here — "ChatGPT Health" links to patient portals to ground answers in the user's own data ([Medical Economics, 2026](https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot), T2). **Confidence: High.** **EU flag:** OpenEvidence figures are US-clinician; EU clinician adoption is less documented. For ditto, the read-through is that a *patient-facing* grounded/cited equivalent (grounded in the patient's record + plain-language evidence) is an open, defensible position.

---

## 4. B2B / B2B2C partnership shift

Digital-health go-to-market is rotating away from pure direct-to-consumer toward **B2B2C and partnership-led distribution** (via providers, payers, employers, pharma, insurers). Drivers: D2C CAC is brutal, retention of standalone wellness apps is poor, and capital has tightened.

- **D2C funding contracted:** consumer health-app venture funding fell **~40% in H1 2025**; standalone telehealth without data/workflow integration faces consolidation, with many "pivoting toward embedded telehealth within existing provider workflows" ([DrugPatentWatch, 2025](https://www.drugpatentwatch.com/blog/the-great-convergence-pharmaceuticals-digital-health-and-the-direct-to-patient-paradigm/) — T3, FLAGGED).
- **Partnerships are scaling fast:** publicly disclosed digital-health collaborations grew from **2,675 (2021) to 4,051 (2024), ~14–15% CAGR**; providers ≈20% of partnerships, tech ≈16%, pharma/medtech/insurers collectively ≈20% ([Galen Growth, 2025](https://www.galengrowth.com/digital-health-exits-navigating-2025s-shifting-tides-towards-maturity/), T1-ish analyst — treat as Med confidence).
- **Capital itself is rotating to strategics:** corporate VC arms of pharma/payer/medtech reportedly made up **~40% of active digital-health investors** in mid-2025 — a structural signal that strategic distribution partners are also the funders ([Galen Growth, 2025](https://www.galengrowth.com/50-core-digital-health-investors-2025/), analyst, Med).
- **Examples:** Viz.ai × Sanofi/Regeneron AI COPD workflow (May 2025); Eli Lilly's direct-to-patient channel as a "data and margin play" to see therapy drop-off and bypass PBMs ([DrugPatentWatch, 2025](https://www.drugpatentwatch.com/blog/the-great-convergence-pharmaceuticals-digital-health-and-the-direct-to-patient-paradigm/) — T3, FLAGGED; [eMarketer, 2025](https://www.emarketer.com/content/direct-to-consumer-telehealth-initiatives-grew-2025--fueled-by-pharma--new-services--federal-push), T2).

**Nuance:** D2C is not dead — pharma-fuelled D2C telehealth actually *grew* in 2025 ([eMarketer, 2025](https://www.emarketer.com/content/direct-to-consumer-telehealth-initiatives-grew-2025--fueled-by-pharma--new-services--federal-push), T2). The accurate framing is **"D2C alone is hard to fund and retain; the durable model couples a consumer-facing experience with a B2B2C distribution and reimbursement partner."** **Confidence: Med** (strong directional consensus; several supporting figures are T3 and should be re-verified against Rock Health / CB Insights primaries before external use). **EU flag:** much of this is US (PBMs, employer-sponsored insurance don't map to NL). In NL/DACH, the analogous partners are **health insurers (zorgverzekeraars), hospital groups, GP cooperatives, and pharma** — the B2B2C logic holds, the counterparties differ.

---

## 5. Value-based care & outcomes

Healthcare globally is shifting from fee-for-service toward **paying for outcomes**, making outcomes/PROM data the unit of account.

**US:** CMS has committed to moving **~all Medicare beneficiaries into value-based/accountable arrangements by 2030**, with ~28.5% of payments already tied to shared-risk arrangements — a $500B+ addressable shift. Provider sentiment has crossed over: **~84% of providers** see VBC enablers as standard infrastructure and **~60%** expect higher VBC revenue in 2025 ([Optum, 2025](https://business.optum.com/en/insights/state-value-based-care-2025-growth-challenges.html), T2/analyst; [NIC, 2025](https://www.nic.org/blog/progress-toward-value-based-care-in-2025/), T2). Headwinds remain in Medicare Advantage regulatory uncertainty. **Confidence: Med-High.**

**EU/NL:** EU systems pursue outcomes/VBHC less through risk contracts and more through **centralised registries and integrated care**. The **Netherlands Heart Registry** is the canonical example — a nationwide initiative collecting outcomes and costs to benchmark best practice and drive quality improvement; the centralised financing of most EU systems makes this scope feasible in ways the fragmented US multi-payer system struggles with ([VBHC scoping review, PMC, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12084849/), T1). **Confidence: High** for NL applicability.

**Implication for ditto:** outcomes-based systems reward anything that improves adherence, comprehension and self-management between visits — a patient who *understands* their care plan is a measurable outcomes lever, and PROM/engagement data has reimbursement value to payers and registries. **Confidence: Med** (logical, not yet quantified for patient-summary products specifically).

---

## 6. Data as moat / longitudinal data

Accumulating **longitudinal personal-health data** is widely cited as a competitive moat, via three mechanisms:

1. **Lock-in:** health data proprietary to a platform makes it the preferred ongoing service for the patient ([Healthcare.Digital, 2025](https://www.healthcare.digital/single-post/the-different-types-of-moat-creating-sustainable-competitive-advantage-in-healthtech) — T3, FLAGGED).
2. **Cross-sell / LTV:** a patient who arrives for one condition is later served for others, raising lifetime value without proportional CAC ([DrugPatentWatch, 2025](https://www.drugpatentwatch.com/blog/the-industrialization-of-telehealth-a-strategic-analysis-of-the-ro-and-hims-hers-duopoly/) — T3, FLAGGED).
3. **Scale datasets:** e.g. Symphony Health's Integrated Dataverse links longitudinal data across physicians, pharmacies, patients and hospitals over 17 years for 317M+ patients ([search-surfaced, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC10155113/), T1 PMC context).

**Crucial caveat — the moat is softening.** Analysts increasingly argue proprietary-data moats are *harder to maintain*: "each new LLM release narrows the performance gap that proprietary data might have provided," and competitors reach "good enough" with public models plus light fine-tuning ([Insignia, 2025](https://review.insignia.vc/2025/03/10/ai-moat/), T2/analyst). **Confidence: Med.**

**Implication for ditto:** the defensible asset is **not model IP and not a generic clinical dataset** (both commoditising). It is the **patient-owned, longitudinal, cross-visit context** built by a daily companion — data that is consented, individual-level, and continuously refreshed, which generic LLMs and one-off competitors cannot replicate. **EU flag — important:** under **GDPR + the EU AI Act + EHDS (European Health Data Space)**, health data is special-category and increasingly portable; a moat built on *patient consent and trust* (not data hoarding) is both more durable and more compliant in the EU than a US-style data-aggregation play. **Confidence: Med-High** on the strategic framing.

---

## Open verification gaps / caveats

- OpenAI's own primary pages (`openai.com/index/introducing-chatgpt-health`, the NBER PDF, several trade outlets) returned **HTTP 403** at access time; the 40M/day and ≥5% figures rest on **multiple concordant T2 reports of OpenAI's primary report** rather than a directly-read primary. Re-confirm against the OpenAI primary when accessible.
- Several B2B2C and data-moat figures are **T3 blog sources** — re-verify deal-count/funding figures against Rock Health, CB Insights, or Galen Growth primaries before external citation.
- Most quantification is US/global; **NL/DACH-specific** figures are sparse and should be sourced separately for any go-to-market claim.

---

## Sources

### Tier 1 — Official / peer-reviewed / analyst
- NBER w34255, "How People Use ChatGPT," Chatterji et al., Sept 2025 — https://www.nber.org/papers/w34255 ; PDF https://www.nber.org/system/files/working_papers/w34255/w34255.pdf
- SSRN mirror of w34255, 2025 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5487080
- HBS AI Institute, "Here's What People Actually Do With ChatGPT," 2025 — https://aiinstitute.hbs.edu/heres-what-people-actually-do-with-chatgpt/
- Deloitte, Global consumer trends in health care, 2024 — https://www.deloitte.com/global/en/Industries/life-sciences-health-care/research/global-consumer-trends-in-health-care.html
- PwC 2025 Health Consumer Survey — https://www.pwc.com/us/en/industries/health-industries/library/healthcare-consumer-insights-survey.html
- PP94 Plain Language in HTA (EU), PMC, 2025 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12768806/
- Global Adoption of Value-Based Health Care (scoping review), PMC, 2024 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12084849/
- Impact of commercial health datasets (longitudinal data), PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC10155113/
- EurekAlert, "AI responses to healthcare queries ~76% accurate," 2026 — https://www.eurekalert.org/news-releases/1129964
- CMS, Value-Based Care key concepts — https://www.cms.gov/priorities/innovation/key-concepts/value-based-care

### Tier 2 — Reputable press
- Healthcare Dive, "40M use ChatGPT for health questions: OpenAI," 2026 — https://www.healthcaredive.com/news/40-million-use-chatgpt-health-questions-openai/808861/
- Axios, "40 million people turn to ChatGPT for health care," 2026 — https://www.axios.com/2026/01/05/chatgpt-openai-health-insurance-aca
- TechRadar, "OpenAI says 40M use ChatGPT for health every day," 2026 — https://www.techradar.com/ai-platforms-assistants/openai/openai-says-40-million-people-use-chatgpt-for-healthcare-every-day
- Medical Economics, "40M use ChatGPT daily for health," 2026 — https://www.medicaleconomics.com/view/40-million-people-now-use-chatgpt-daily-for-health-questions-openai-report-finds
- Fierce Healthcare, "40M use ChatGPT for healthcare questions," 2026 — https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says
- Medical Economics, "OpenAI launches ChatGPT Health, links patient portals," 2026 — https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot
- MIT Technology Review, "'Dr. Google' had issues. Can ChatGPT Health do better?," 2026 — https://www.technologyreview.com/2026/01/22/1131692/dr-google-had-its-issues-can-chatgpt-health-do-better/
- NPR, "'Dr. Google' meets its match in Dr. ChatGPT," 2023 — https://www.npr.org/sections/health-shots/2023/09/16/1199924303/chatgpt-ai-medical-advice
- The Conversation, "Dr. ChatGPT is getting remarkably good at diagnosing," 2025 — https://theconversation.com/dr-chatgpt-is-getting-remarkably-good-at-diagnosing-health-problems-but-actual-doctors-are-still-better-at-weighing-treatment-options-281813
- CNBC, "OpenEvidence doubles valuation to $12B," 2026 — https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html
- TechCrunch, "OpenEvidence raises $200M at $6B," 2025 — https://techcrunch.com/2025/10/20/openevidence-the-chatgpt-for-doctors-raises-200m-at-6b-valuation/
- Becker's Hospital Review, "OpenEvidence: 6 things to know," 2025 — https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/
- eMarketer, "The 2025 Healthcare Consumer," 2025 — https://www.emarketer.com/content/the-2025-healthcare-consumer
- eMarketer, "D2C telehealth initiatives grew 2025," 2025 — https://www.emarketer.com/content/direct-to-consumer-telehealth-initiatives-grew-2025--fueled-by-pharma--new-services--federal-push
- Optum, "State of value-based care 2025," 2025 — https://business.optum.com/en/insights/state-value-based-care-2025-growth-challenges.html
- National Investment Center, "Progress Toward VBC in 2025," 2025 — https://www.nic.org/blog/progress-toward-value-based-care-in-2025/
- Insignia Business Review, "Is Proprietary Data Still a Moat in the AI Race?," 2025 — https://review.insignia.vc/2025/03/10/ai-moat/
- Galen Growth, "Digital Health Exits 2025" — https://www.galengrowth.com/digital-health-exits-navigating-2025s-shifting-tides-towards-maturity/
- Galen Growth, "50 Core Digital Health Investors 2025" — https://www.galengrowth.com/50-core-digital-health-investors-2025/

### Tier 3 — Blog / self-report (FLAGGED — re-verify before external use)
- Kyruus Health, "Healthcare Consumerism Trends in 2025" — https://kyruushealth.com/healthcare-consumerism-trends/
- DrugPatentWatch, "The Great Convergence: Pharma, Digital Health, DTP" — https://www.drugpatentwatch.com/blog/the-great-convergence-pharmaceuticals-digital-health-and-the-direct-to-patient-paradigm/
- DrugPatentWatch, "Industrialization of Telehealth: Ro & Hims" — https://www.drugpatentwatch.com/blog/the-industrialization-of-telehealth-a-strategic-analysis-of-the-ro-and-hims-hers-duopoly/
- Healthcare.Digital, "Types of moat in HealthTech" — https://www.healthcare.digital/single-post/the-different-types-of-moat-creating-sustainable-competitive-advantage-in-healthtech
