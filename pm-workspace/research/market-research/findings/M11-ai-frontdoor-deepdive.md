# M11 — The Consumer AI Health "Front Door": the real picture

**Prepared for:** ditto.care market-research deck (deep-dive overlays)
**Author:** Market research analyst
**Access date:** 2026-06-10 · **Data preference:** 2025–2026
**Geographic note:** Most named players below are **US-first**. EU/NL availability is flagged throughout — this is material for ditto.care, because the biggest US "front door" products are partly or wholly **unavailable in the EU/EEA** today.

Source tiers: **T1** = peer-reviewed / official company or regulator / named analyst · **T2** = reputable trade & general press · **T3** = blogs / SEO vendors / opinion (FLAGGED). Confidence: High / Medium / Low. Unconfirmed items are marked **[UNCONFIRMED]**.

---

## Key takeaways

- **Google still wins on raw scale, by an order of magnitude — but the gap is narrowing fast.** Google handles on the order of **~1 billion health-related questions per day** (≈5–7% of all searches) [T1/T2, Medium], versus **~40 million people/day** asking ChatGPT health questions and **>5% of all ChatGPT messages** being health-related [T1 OpenAI, High]. So Dr Google is still ~20–25× larger by volume, **but** the "search" itself is changing: Google now answers health queries with **AI Overviews**, which trigger on **88% of healthcare queries** as of Dec 2025 [T3, Medium]. The founder's instinct (Google dominates) is correct on volume; it is wrong if it implies the experience is still "ten blue links."
- **The front door is being re-papered with AI on both sides.** Google **removed AI Overviews from certain medical queries in Jan 2026** after misinformation scrutiny [T2, Medium], while OpenAI launched **ChatGPT Health** (Jan 7 2026) connecting patient portals — **explicitly excluded from the EEA/Switzerland/UK** [T1 OpenAI, High]. **This EU exclusion is the single most important strategic fact in this report for ditto.care.**
- **Payer bots are real and large but narrow.** UnitedHealthcare's **"Avery"** targets ~20M members by end-2026 (~6.5M live now) [T2, Medium]; **Cigna**, **Oscar (GPT-5 "Superagent")**, and **Elevance/Anthem "Sydney Health"** all ship member assistants. These are **navigation/benefits/claims** bots, not clinical advice engines [T2, Medium].
- **Provider bots are consolidating around Epic.** Epic's **"Emmie"** (patient) + **"Art"** (clinician) ship inside MyChart; Epic claims **85% of its health-system customers are live with its generative-AI copilots** [T2, Medium]. **Hippocratic AI** runs voice agents across 50+ health systems for non-diagnostic tasks [T2, Medium].
- **The diagnostic-accuracy story is genuinely mixed — "trust gap opening" is defensible but must be stated carefully.** GPT-4 *alone* scored **~92%** on diagnostic reasoning vs **~74–76%** for physicians, yet **giving physicians the tool did not improve them** (Goh et al., *JAMA Network Open* 2024) [T1, High]. Counter-evidence: a 2026 *npj Digital Medicine* study found **5–13% of LLM answers to patient questions were outright "unsafe"** [T1, High].
- **Patient-facing grounded-and-cited is still a white space.** The best *cited* engines today are clinician-only (**OpenEvidence**, ~40% of US physicians, NEJM/JAMA-licensed) [T1/T2, High] or general-purpose (**Perplexity Health**, **Google AI Overviews**). No one yet owns **patient-grade, grounded, cited, EU-available** health answers — the gap ditto.care is pointed at.
- **EU regulatory overhang is real:** triage/recommendation chatbots can fall under **high-risk** classification in the **EU AI Act**, and transparency duties apply from **Aug 2, 2025** [T1, Medium].

---

## 1. Dr. Google vs Dr. ChatGPT — the actual share

**Bottom line: Google still dwarfs ChatGPT on volume, but "Google" is no longer just search results — it is increasingly an AI answer engine, and ChatGPT is growing into a genuine second front door.**

### Google scale (Confidence: Medium — figures are vendor/exec estimates, not audited)
- Google processes **~14–16 billion searches/day** in 2025 [T3 SEO vendor, Low]; an estimated **~5–7% are health-related** — the "7%" figure traces to former Google Health VP David Feinberg [T2/T3, Medium].
- That yields **~1 billion health questions/day** — Google has repeatedly cited "1 billion health questions a day" [T2 Becker's, Medium]. ≈70,000 health searches/minute.
- **AI Overviews now intercept these.** Per SEO analytics vendors, healthcare queries triggered AI Overviews **~72% of the time in 2024, rising to ~88% by Dec 2025**; treatment/procedure queries hit **~100%**, pain **~98%**, symptoms/conditions **~93%** [T3 BrightEdge/ALM, Medium — FLAG: SEO-vendor methodology, not peer-reviewed]. **US→EU FLAG:** AI Overviews / AI Mode rollout in the EU lags the US and is subject to DSA/DMA scrutiny.
- **Citation quality is weak for health.** In AI Overview health citations, **YouTube was the single most-cited domain (~4.4%)** while **peer-reviewed journals were ~0.48%** and government health ~0.39%; only **~34% of citations came from sources with editorial/clinical oversight** [T3 ALM/BrightEdge, Low — FLAG vendor data]. This is the wedge for a *clinically grounded* engine.
- **Jan 2026 retrenchment:** Google **removed AI Overviews from certain medical queries** following misinformation scrutiny (incl. a Guardian investigation) [T2 TechCrunch, Medium]. Signal: even Google is uncertain about answering health queries generatively.

### ChatGPT health scale (Confidence: High — OpenAI first-party, Jan 2026)
- **>40 million people/day** ask ChatGPT health questions [T1 OpenAI via Axios/Healthcare Dive, High].
- **>5% of all ChatGPT messages globally are about healthcare** — "billions of messages each week" [T1 OpenAI, High].
- **~1.5–2 million health-insurance questions/week** (plan comparison, claims, billing) [T1 OpenAI, High].
- **~7 in 10 health conversations happen outside clinical hours** — the "3am question" use case [T1 OpenAI, High].
- OpenAI's Dec 2025 survey: **3 in 5 US adults** used AI for a health question in the prior 3 months; 55% to check symptoms, 48% to understand terms/instructions, >40% to learn treatment options [T1 OpenAI, High — note self-reported survey].

### Honest comparison
| Dimension | Dr. Google | Dr. ChatGPT |
|---|---|---|
| Daily health-query volume | **~1 billion/day** [T2, Med] | **~40 million users/day** [T1, High] |
| Relative scale | ~20–25× larger (volume) | Smaller but compounding fast |
| Format | Search → increasingly **AI Overviews** (88% of health queries) [T3, Med] | Conversational, multi-turn |
| Citations | Yes in AI Overviews, but weak source quality [T3, Low] | Inline links variable; ChatGPT Health adds grounding |
| Personalization | Minimal | **ChatGPT Health** connects portals/records (US only) [T1, High] |
| EU availability | Search yes; AI Overviews lagging | **ChatGPT Health excluded from EEA/CH/UK** [T1, High] |

**Verdict for the founder:** "Google is still the vast majority" is **true on volume** and likely to remain so for years. But the *nature* of the front door has flipped from "links" to "answers," and ChatGPT is a credible #2 that is purpose-building a health vertical. The strategic risk is not that ChatGPT overtakes Google tomorrow — it is that **both giants now answer health questions directly, and in the EU both do so in a degraded/absent form**, leaving room for a local, grounded entrant.

---

## 2. Payer bots & provider bots — the named players

The founder doesn't know examples; here they are. **Key framing:** almost all of these are **navigation/administrative** ("where do I go, what's covered, what does this bill mean") rather than **diagnostic**. None of the major payer bots give clinical diagnosis.

### Payer / insurer member bots (all US, Confidence: Medium)
| Player | Product | What it does | Rough adoption / status |
|---|---|---|---|
| **UnitedHealthcare** | **"Avery"** (genAI assistant) | Care navigation, benefits/coverage Q&A | ~6.5M employer members + 160k Medicare Advantage **live now**; targeting **~20M by end-2026** [T2 Investing.com/Becker's, Med]. Part of UHG's **$1.5B AI spend** [T2, Med] |
| **Cigna** | AI-powered Virtual Assistant (myCigna) | Conversational answers on benefits, claims, care options; handoff to human advocate | Phased rollout; early data: **2 of 3** members used it proactively, **4 of 5** found it helpful [T1 Cigna newsroom / T2 Healthcare Dive, Med] |
| **Oscar Health** | **"Superagent"** (GPT-4 → GPT-5) | Explains insurance, prior auth, benefit costs, ID cards, Rx renewal; began member-facing as Clinical Intake Bot | Built ~8 months; internal CSAT **~82.6%**; experimenting with GPT-5 [T2 Fierce / T3 Oscar Tech blog, Med] |
| **Elevance Health / Anthem** | **"Sydney Health"** app (incl. AI nutrition tracker) | Member app with chat for cost-share/benefit explanation; AI food-photo logging | Nutrition tool reached **~15M** people; chat criticized as **menu-driven, not true AI** [T2 Fierce / T3 user reviews, Med — FLAG: maturity disputed] |
| **Babylon (legacy)** | Babylon "Ask"/symptom checker | Diagnostic-style symptom chatbot for payers/NHS | **Defunct** — Babylon went bankrupt 2023; UK ops sold to **eMed**; safety concerns were raised with UK regulators [T2 TechCrunch/Fierce, High]. **Cautionary tale.** |

### Provider / health-system patient bots (Confidence: Medium)
| Player | Product | What it does | Rough adoption / status |
|---|---|---|---|
| **Epic** (EHR) | **"Emmie"** (patient, in MyChart) + **"Art"** (clinician) + **"Penny"** (rev-cycle) | Emmie: explains labs, proposes appointment times, screening suggestions, billing/payments, via MyChart + SMS | Unveiled Aug 2025 UGM; **Sutter Health** first adopter; Epic claims **~85% of customers live** with its genAI copilots [T2 TechTarget/Fierce/Healthcare IT News, Med] |
| **Hippocratic AI** | Patient-facing voice agents + AI Agent App Store | Non-diagnostic: post-discharge check-ins, med reconciliation, screening/education calls | **50+ health systems/payers/pharma**, ~1,000 use cases; UHS & University Hospitals deployments; patient rating **~9.0/10**; raised **$126M Series C** [T2 Fierce/BusinessWire, Med] |
| **Mayo Clinic** | Microsoft-partnered AI assistant (in development) | Patient-facing assistant via portal; Mayo owns the model | Announced ~Jun 2026; Suleyman says **"many years"** to reach trust for high-stakes Q&A [T2 CNN, Med] — **not yet shipping to patients** |
| **K Health** | AI symptom assessment + physician access | Consumer app: AI intake → clinician; condition management | Subscription (~$49/mo); provider/payer partnerships [T3 comparison sites, Low] |
| **Ada Health** (DE 🇪🇺) | Ada symptom checker | Conversational symptom assessment; enterprise payer/provider deals | **Most clinically validated** consumer symptom checker; millions of downloads; **European** origin [T3 iatroX / validation lit, Med] |
| **Buoy Health** | AI symptom checker | Conversational symptom triage on medical database | Consumer + enterprise; US [T3, Low] |
| **Cleveland Clinic** | — | No standalone patient genAI chatbot confirmed for 2025 | **[UNCONFIRMED]** — not found in this pass |

**EU note:** **Ada (Germany)** is the standout European patient-facing player. NHS-flavored options include **NHS 111 online** (AI triage trials) and emerging tools (Ubie, Isabel). The **US payer/provider bots above largely do not operate in the EU.**

---

## 3. Diagnostic-accuracy research — "is the trust gap opening?"

**Balanced answer: LLMs *alone* now match or beat physicians on structured diagnostic-reasoning benchmarks, but (a) they don't reliably make doctors better, and (b) they still produce a meaningful rate of unsafe answers to real patient questions. Both halves are true; the deck should present both.**

### The "LLMs are good" evidence (Confidence: High)
- **Goh, Rodman, Chen et al., *JAMA Network Open*, 2024 ("Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial").** 50 physicians (26 attendings, 24 residents). **GPT-4 alone scored ~92%** on diagnostic reasoning. Physicians with GPT-4 scored **~76%**; physicians with conventional resources (UpToDate, Google) **~74%** — i.e. **adding the AI barely moved physicians (~2 pts, n.s.)** even though the AI alone crushed them [T1 JAMA Network Open, High]. **This is the headline study for "the model is better than the human, but humans don't know how to use it."**
- **Frontier-LLM triage/diagnosis vs physicians, *JMIR* 2024 (updated):** correct diagnosis in **top-3 for ~98.6%** of cases for frontier LLMs [T1 JMIR, Medium].
- **Nature Medicine 2025 (Goh et al. follow-up):** GPT-4 assistance for physician patient-care tasks — RCT, mixed/modest physician uplift [T1 Nature Medicine, Medium].
- A 2025 **meta-analysis (medRxiv)** of 15 studies / 498 physicians / 7,274 case evaluations found a **significant positive effect of LLM assistance** on diagnostic accuracy [T1 preprint, Medium — FLAG: preprint, not yet peer-reviewed].

### The counter-evidence: hallucination & patient-grade safety (Confidence: High)
- ***npj Digital Medicine*, 2026 — "Large language models provide unsafe answers to patient-posed medical questions."** Across leading models, **problematic responses ranged ~21.6% (Claude) to ~43.2% (Llama)**; **outright unsafe responses ranged ~5% (Claude) to ~13% (GPT-4o / Llama)**, with qualitative cases judged capable of **serious patient harm** [T1 npj Digital Medicine, High]. **This is the headline safety counter-study.**
- **Clinical-guideline omission/hallucination (PMC 2025):** when checking whether outputs correctly reflected guidelines, accuracy was **~46% (GPT-4.1)** down to **~3% (DeepSeek-V3)**, with high omission rates [T1 PMC, Medium].
- **Adversarial robustness (*Communications Medicine*, Nature, 2025):** LLMs are **"highly vulnerable to adversarial hallucination attacks"** in clinical decision support [T1, Medium].
- A documented real-world case: **delayed TIA (mini-stroke) diagnosis** attributed to ChatGPT reliance [T1 review article, Low — single case].

### How to phrase "the trust gap is opening" honestly
The defensible claim: *On clean, structured cases, top models now match or exceed physician diagnostic reasoning — yet on messy, patient-phrased questions a non-trivial minority of answers are unsafe, and unsupervised consumer use lacks the guardrails clinicians have.* The gap that is "opening" is between **what models can do in benchmarks** and **what is safe to ship to an unsupervised patient** — which is precisely the grounding/safety problem ditto.care must solve.

---

## 4. Consumer grounded / cited answer engines

**Who does grounded-and-cited best today, and what's missing for patients.**

### The landscape (Confidence: High where first-party)
- **OpenEvidence — clinician-only, best-in-class grounding.** Licensed **NEJM + JAMA + NCCN** content; cites primary literature. **~18M clinical consultations in Dec 2025 alone**; used by **>40% of US physicians**, across **10,000+ hospitals**; **$250M Series D at $12B valuation (Jan 2026)**, total funding ~$700M [T1 BusinessWire/CNBC / T2 Becker's, High]. **Crucially: NPI-verified, US-physician-only — NOT for patients, NOT consumer-facing.** [T1 OpenEvidence, High]. **US→EU FLAG:** US-centric (US guidelines), limited fit for EU clinicians.
- **Perplexity Health — closest to patient-facing grounded-and-cited.** Launched as a suite connecting **EHRs, wearables, labs** (via **b.well** national health-data network) to personalize answers "grounded in clinical guidelines and peer-reviewed research," with **citations + guidance on when to seek care**; added **Premium Health Sources** (e.g. Springer) [T1 Perplexity / T2 TechRepublic/PRNewswire, High]. Still general-consumer, not a regulated medical device.
- **Google AI Overviews / AI Mode — cited but quality-mixed.** Surfaces source links on most health queries, but (§1) citation quality skews to YouTube over journals, and Google **pulled AI Overviews from some medical queries in Jan 2026** [T2/T3, Medium].
- **ChatGPT Health — personalized, grounding-aware, but EU-excluded.** Connects patient portals (via **b.well**, ~2.2M US providers), Apple Health, and wellness apps; plain-language lab summaries, visit prep, insurance comparison; isolated/encrypted, not used for training [T1 OpenAI, High]. **Early access excludes EEA, Switzerland, UK** [T1 OpenAI, High]. **This is the most important EU gap in the entire report.**

### Who's doing patient-facing grounded-and-cited *best* — and what's missing
| Engine | Cited sources? | Patient-facing? | EU-available? | Grounded in *your* records? |
|---|---|---|---|---|
| OpenEvidence | **Yes (NEJM/JAMA)** | **No (clinicians only)** | Limited | No |
| Perplexity Health | Yes | **Yes** | Partial/unclear | Yes (b.well) |
| Google AI Overviews | Partial (weak quality) | Yes | Lagging | No |
| ChatGPT Health | Yes (grounding) | **Yes** | **No (excluded)** | Yes (b.well, US) |

**What's still missing (the white space):** a **patient-facing** engine that is **(1) grounded in vetted clinical sources with visible citations, (2) safe by patient-grade design (not just benchmark-good), (3) available and compliant in the EU/NL, and (4) ideally personalized to the patient's own records.** Today the *cited+grounded* leaders are clinician-only (OpenEvidence) or EU-absent (ChatGPT Health); the *patient+EU* options are weaker on grounding. **No single player occupies all four corners — that is the opening for ditto.care.**

---

## Sources

### T1 — peer-reviewed / official / named analyst
- OpenAI — *Introducing ChatGPT Health* (Jan 7 2026): https://openai.com/index/introducing-chatgpt-health/
- OpenAI Help Center — *What is ChatGPT Health*: https://help.openai.com/en/articles/20001036-what-is-chatgpt-health
- Goh, Rodman, Chen et al., *JAMA Network Open* 2024 — *Large Language Model Influence on Diagnostic Reasoning: An RCT*: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395
- *Nature Medicine* 2024/25 — *GPT-4 assistance for improvement of physician performance: an RCT*: https://www.nature.com/articles/s41591-024-03456-y
- *npj Digital Medicine* 2026 — *Large language models provide unsafe answers to patient-posed medical questions*: https://www.nature.com/articles/s41746-026-02428-5
- *Communications Medicine* (Nature) 2025 — *LLMs highly vulnerable to adversarial hallucination attacks in clinical decision support*: https://www.nature.com/articles/s43856-025-01021-3
- *JMIR* 2024 — *Triage and Diagnostic Accuracy of Frontier LLMs vs Physicians*: https://www.jmir.org/2024/1/e67409
- PMC 2025 — *Omission and hallucination prevalence of clinical guidelines in diagnostic LLM outputs*: https://pmc.ncbi.nlm.nih.gov/articles/PMC13110572/
- OpenEvidence — *$250M Series D at $12B* (BusinessWire, Jan 21 2026): https://www.businesswire.com/news/home/20260121029132/en/
- Perplexity — *Introducing Perplexity Health*: https://www.perplexity.ai/hub/blog/introducing-perplexity-health
- Perplexity / b.well — *Trusted Health Data to AI Search* (PRNewswire): https://www.prnewswire.com/news-releases/perplexity-and-bwell-bring-trusted-health-data-to-ai-search-enabling-personalized-health-answers-302718967.html
- Cigna newsroom — *AI-Powered Digital Tools*: https://newsroom.cigna.com/cigna-healthcare-unveils-industry-leading-ai-powered-digital-tools
- EU AI Act — Article 6 (high-risk classification): https://artificialintelligenceact.eu/article/6/

### T2 — reputable trade & general press
- Axios — *40M people turn to ChatGPT for health care* (Jan 5 2026): https://www.axios.com/2026/01/05/chatgpt-openai-health-insurance-aca
- Healthcare Dive — *40M users turn to ChatGPT daily for health questions*: https://www.healthcaredive.com/news/40-million-use-chatgpt-health-questions-openai/808861/
- Becker's — *Google receives more than 1 billion health questions every day*: https://www.beckershospitalreview.com/healthcare-information-technology/google-receives-more-than-1-billion-health-questions-every-day/
- TechCrunch — *Google removes AI Overviews for certain medical queries* (Jan 11 2026): https://techcrunch.com/2026/01/11/google-removes-ai-overviews-for-certain-medical-queries/
- CNBC — *OpenAI launches ChatGPT Health*: https://www.cnbc.com/2026/01/07/openai-chatgpt-health-medical-records.html
- Fortune — *OpenAI launches ChatGPT Health*: https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/
- Investing.com — *UnitedHealthcare launches AI assistant Avery*: https://www.investing.com/news/company-news/unitedhealthcare-launches-ai-assistant-avery-for-members-93CH-4582311
- Becker's Payer — *UnitedHealth $1.5B AI spend*: https://www.beckerspayer.com/virtual-care/unitedhealth-is-spending-1-5b-on-ai-this-year-heres-where-the-money-is-going/
- Healthcare Dive — *Cigna launches generative AI member assistant*: https://www.healthcaredive.com/news/cigna-launches-generative-ai-member-assistant/750480/
- FierceHealthcare — *Oscar Health builds AI 'superagent,' GPT-5*: https://www.fiercehealthcare.com/payers/oscar-health-builds-ai-superagent-experimenting-gpt-5
- TechTarget — *Epic's Ask Emmie offers EHR-backed AI chatbot for patients*: https://www.techtarget.com/patientengagement/feature/Epics-Ask-Emmie-offers-EHR-backed-AI-chatbot-option-for-patients
- Healthcare IT News — *Epic unveils AI agents (Emmie/Art/Penny)*: https://www.healthcareitnews.com/news/epic-unveils-ai-agents-showcases-new-foundational-models
- FierceHealthcare — *Hippocratic AI $126M Series C*: https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-lands-126m-series-c-expand-patient-facing-ai-agents-fuel-ma
- CNN — *Microsoft teams with Mayo Clinic on AI for health questions* (Jun 2 2026): https://www.cnn.com/2026/06/02/tech/ai-for-healthcare-microsoft-mayo-clinic
- TechCrunch — *The fall of Babylon Health* (2023): https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/
- Becker's — *OpenEvidence used by half of physicians*: https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/
- ScienceDaily — *Promise and limits of physicians working with GPT-4* (Goh study coverage): https://www.sciencedaily.com/releases/2024/10/241028164534.htm
- TechRepublic — *Perplexity Health connects medical records and wearables*: https://www.techrepublic.com/article/news-perplexity-health-ai/

### T3 — blogs / SEO vendors / opinion (FLAGGED, use with caution)
- BrightEdge — *Healthcare and AI Overviews 2023–2025* (FLAG: SEO-vendor methodology): https://www.brightedge.com/resources/weekly-ai-search-insights/healthcare-ai-evolution-google-2023-2025
- ALM Corp — *AI Overview citations drop / health misinformation* (FLAG: SEO blog): https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/
- SeoProfy — *Google AI Overviews stats 2026* (FLAG): https://seoprofy.com/blog/google-ai-overviews/
- iatroX — *Patient-facing AI in 2025 (Ada, K Health, Buoy, NHS)* (FLAG: vendor blog): https://www.iatrox.com/blog/patient-facing-ai-health-tools-2025-ada-khealth-buoy-aide-mirror-nhs
- Oscar Tech (Medium) — *How we built Oscar's member-facing AI* (FLAG: company blog): https://medium.com/oscar-tech/how-we-built-oscars-first-member-facing-ai-the-clinical-intake-bot-a39907b35a2a

---

## Deep-dive blocks (ready to embed in overlays)

### (a) Dr Google vs ChatGPT — scale
Google still owns the raw volume of health-information seeking — roughly **1 billion health questions a day** (≈5–7% of all searches), some 20–25× ChatGPT's **~40 million daily health users**. But the experience has flipped from "ten blue links" to AI answers: **AI Overviews now trigger on ~88% of health queries** (Dec 2025), while ChatGPT reports **>5% of all its messages are health-related** and **7 in 10 health chats happen outside clinic hours**. Both giants now *answer* health questions directly — and in the EU, both do so in a degraded (AI Overviews lagging) or absent (ChatGPT Health excluded) form.
- ChatGPT 40M/day (OpenAI via Axios): https://www.axios.com/2026/01/05/chatgpt-openai-health-insurance-aca
- Google ~1B health questions/day (Becker's): https://www.beckershospitalreview.com/healthcare-information-technology/google-receives-more-than-1-billion-health-questions-every-day/
- AI Overviews on health queries (BrightEdge, FLAG T3): https://www.brightedge.com/resources/weekly-ai-search-insights/healthcare-ai-evolution-google-2023-2025
- Google pulls AI Overviews on some medical queries (TechCrunch): https://techcrunch.com/2026/01/11/google-removes-ai-overviews-for-certain-medical-queries/
- ChatGPT Health launch — EU excluded (OpenAI): https://openai.com/index/introducing-chatgpt-health/

### (b) Payer & provider bots
The "front door" is being re-papered with AI on both the insurer and provider sides — but almost entirely for **navigation, benefits and admin**, not diagnosis. On the payer side, **UnitedHealthcare's "Avery"** (targeting ~20M members), **Cigna's** virtual assistant, **Oscar's GPT-5 "Superagent,"** and **Anthem/Elevance "Sydney Health"** answer coverage, claims and care-routing questions. On the provider side, **Epic's "Emmie"** lives inside MyChart (Epic claims 85% of customers live with its genAI copilots) and **Hippocratic AI** runs voice agents across 50+ health systems for post-discharge and education calls. Babylon Health — the cautionary tale — went bankrupt in 2023 after safety concerns about its diagnostic chatbot.
- UnitedHealthcare "Avery" (Investing.com): https://www.investing.com/news/company-news/unitedhealthcare-launches-ai-assistant-avery-for-members-93CH-4582311
- Cigna AI assistant (Healthcare Dive): https://www.healthcaredive.com/news/cigna-launches-generative-ai-member-assistant/750480/
- Oscar Superagent / GPT-5 (Fierce): https://www.fiercehealthcare.com/payers/oscar-health-builds-ai-superagent-experimenting-gpt-5
- Epic Emmie/Art/Penny (Healthcare IT News): https://www.healthcareitnews.com/news/epic-unveils-ai-agents-showcases-new-foundational-models
- Hippocratic AI Series C / deployments (Fierce): https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-lands-126m-series-c-expand-patient-facing-ai-agents-fuel-ma
- Babylon bankruptcy (TechCrunch): https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/

### (c) Diagnostic-accuracy research
The evidence is genuinely two-sided. In a 2024 *JAMA Network Open* RCT (Goh/Rodman/Chen), **GPT-4 alone scored ~92% on diagnostic reasoning vs ~74–76% for physicians** — yet **giving doctors the tool barely improved them**, exposing a usage gap, not a capability gap. The counterweight: a 2026 *npj Digital Medicine* study found **5–13% of LLM answers to patient-posed questions were outright unsafe**, and other 2025 work shows high guideline-omission and adversarial-hallucination rates. The honest takeaway for a deck: models can be benchmark-excellent and still unsafe to hand an unsupervised patient — the gap that's "opening" is between capability and patient-grade safety.
- Goh et al., JAMA Network Open 2024 RCT: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395
- npj Digital Medicine 2026 — unsafe answers to patient questions: https://www.nature.com/articles/s41746-026-02428-5
- Nature Medicine — GPT-4 physician-assistance RCT: https://www.nature.com/articles/s41591-024-03456-y
- Communications Medicine — adversarial hallucination vulnerability: https://www.nature.com/articles/s43856-025-01021-3

### (d) Consumer grounded / cited engines
Grounded-and-cited health answers exist — but no one yet serves them to **patients, in the EU, safely, and personalized**. **OpenEvidence** is the gold standard for citations (NEJM/JAMA-licensed, ~40% of US physicians, $12B valuation) but is **clinician-only**. **Perplexity Health** is the closest patient-facing grounded engine (EHR/wearable connectors via b.well, citations, "when to seek care" guidance). **Google AI Overviews** cite sources but skew to weak ones and were partly withdrawn from medical queries. **ChatGPT Health** personalizes against your records — but is **excluded from the EEA/Switzerland/UK**. The white space is the intersection of all four: grounded + cited + patient-facing + EU-available.
- OpenEvidence $250M/$12B (BusinessWire): https://www.businesswire.com/news/home/20260121029132/en/
- OpenEvidence used by ~40%+ of US physicians (Becker's): https://www.beckershospitalreview.com/healthcare-information-technology/ai/openevidence-6-things-to-know-about-the-ai-tool-used-by-half-of-physicians/
- Perplexity Health (Perplexity): https://www.perplexity.ai/hub/blog/introducing-perplexity-health
- ChatGPT Health — EU excluded (OpenAI): https://openai.com/index/introducing-chatgpt-health/
- AI Overview health citation quality (ALM, FLAG T3): https://almcorp.com/blog/google-ai-overviews-health-misinformation-investigation-2026/
