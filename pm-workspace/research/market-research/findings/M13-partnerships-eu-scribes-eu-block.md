# M13 — Marquee Partnerships, EU AI Scribes & the ChatGPT-Health EU Block

**Module:** M13 (Deep-dive overlays for the market-research deck)
**Prepared for:** ditto.care strategy / founder deep-dive requests
**Access date:** 2026-06-10
**Scope:** (1) Named, dated digital-health partnerships 2024–2026; (2) EU-native AI scribes as serious rivals, incl. patient-facing after-visit summaries + the EHDS threat; (3) the detailed legal reasoning for why ChatGPT Health is EU-blocked.

**Tiering:** T1 = filings / official company or regulator releases / legal texts; T2 = trade press; T3 = blogs / vendor self-report (FLAGGED inline). **US→EU** flag marks moves born in a US-regulatory context whose EU/NL relevance needs separate validation. Confidence tags inline.

---

## Key takeaways

1. **The marquee partnerships of 2024–2026 cluster on four axes** — pharma×digital-health (Viz.ai×Sanofi/Regeneron COPD, May 2025), big-tech×health-system (OpenAI for Healthcare across ~8 US systems, Jan 2026), payer×AI (Abridge×Availity prior-auth, Jan 2026; Highmark×Abridge), and big-tech×EHR (Microsoft×Epic ambient AI). The named deals confirm the "2,675→4,051" count is being driven by enterprise AI embedding, not consumer apps. (T1/T2, high confidence; most are **US→EU** flagged.)
2. **Patient-facing after-visit summaries are no longer ditto-exclusive territory — the scribes already ship them.** Nabla auto-generates patient-friendly "Patient Instructions" as a post-visit recap, in the family's preferred language, written back into the EHR ([Nabla help, 2025](https://help.nabla.com/en/articles/769346); T1 vendor doc). Suki launched patient summaries + Q&A on Google Cloud (Dec 2024). This is the single most important competitive fact for ditto. (T1/T2, high confidence.)
3. **EU-native scribes are well-funded, fast-growing and the *right* user-base, not also-rans.** Corti (Copenhagen, ~$95M raised, 250k patient interactions/day, NHS + DACH) ([Tracxn, 2026](https://tracxn.com/d/companies/corti/__0s9fLHIXnFrC5tD32K5PLq7c3jKthk5baNst_XJEMfI); T2); Nabla (Paris, $120M total, 85k clinicians, 20M+ encounters/yr) ([STAT, 2025](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/); T2); Tortus (London, NHS trial across 9 sites / 17,000 encounters, £834M/yr national potential) ([Digital Health, 2025](https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/); T2). (High confidence.)
4. **The EHDS turns the scribe's patient summary into a structural threat.** From **March 2029**, Patient Summaries and ePrescriptions become a mandatory priority data category exchanged across all Member States ([EC Health, 2025](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en); T1). If scribe-generated summaries flow natively into EHDS-linked records, a standalone patient-summary app loses its "we aggregate the record" wedge — ditto's durable edge must be **comprehension, longitudinal continuity, and patient trust/UX**, not document capture. (High confidence, forward-looking.)
5. **ChatGPT Health is EU/EEA/UK/CH-blocked for a stack of reasons, not just "GDPR."** Three independent legal mechanisms each suffice to block it: GDPR Art. 9 special-category health data + US transfer scrutiny; EU AI Act high-risk classification for medical-use AI; and MDR medical-device classification risk ([Euronews, 2026](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations); [Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-healthcare-ai-regulations-mdr-gdpr-ai-act); T2). (High confidence.)
6. **The barrier is durable but not permanent.** Entry requires EU data residency/localization + DPIAs + a valid Art. 9 legal basis, a defensible non-medical-device positioning *or* CE marking under MDR, and an AI Act conformity path (high-risk obligations phasing in Aug 2026 / Aug 2027). Realistic localized EU launch by US giants: **2027–2028**, behind native-EU incumbents who are already compliant-by-construction. (Medium confidence on timing; **US→EU**.)
7. **Founder's framing is correct: high adoption velocity = the right market.** NHS, Kaiser (24,600 physicians), Mayo (2,000+), 130+ orgs on Nabla — healthcare AI adoption has never been faster. Well-funded, fast-growing rivals validate the category; the contest is over *which layer* (capture vs. comprehension) owns the patient. (T2, high confidence.)

---

## Section 1 — Biggest DISCLOSED digital-health partnerships (named, dated, 2024–2026)

The count (2,675→4,051) is being driven by AI embedding into clinical and payer workflows. The marquee, *disclosed* examples below span all four axes the founder asked for.

### Partnerships table

| Partners | Axis | What | When | Why it matters | Tier / flag |
|---|---|---|---|---|---|
| **Viz.ai × Sanofi × Regeneron** | Pharma × digital-health | Multi-year collaboration; AI/NLP workflow on EHR data to screen & triage high-risk **COPD** patients (Viz COPD module) | **May 20, 2025** | Pharma funding an AI care-coordination layer to find drug-eligible patients; Viz spans 1,700+ hospitals, 60k+ providers | T1 ([Businesswire](https://www.businesswire.com/news/home/20250520566222/en/Viz.ai-Announces-Collaboration-With-Sanofi-and-Regeneron-to-Improve-Management-and-Care-of-Chronic-Obstructive-Pulmonary-Disease-COPD)) **US→EU** |
| **Viz.ai × Novartis** | Pharma × digital-health | AI-powered care coordination for oncology patients | 2024–25 | Second marquee pharma deal confirms the "AI triage as patient-finder for pharma" model | T2 ([MobiHealthNews](https://www.mobihealthnews.com/news/vizai-novartis-partner-ai-powered-care-patients-cancer)) **US→EU** |
| **OpenAI for Healthcare × AdventHealth, Baylor Scott & White, Boston Children's, Cedars-Sinai, HCA, Memorial Sloan Kettering, Stanford Children's, UCSF** | Big-tech × health-system | HIPAA-compliant "ChatGPT for Healthcare" enterprise workspace + OpenAI API for Healthcare; data residency, audit logs, customer-managed keys, no training on patient data | **Jan 7–8, 2026** | OpenAI lands ~8 marquee US systems simultaneously — the clearest signal a frontier-model vendor is now a direct health-system platform | T1 ([OpenAI](https://openai.com/index/openai-for-healthcare/)); T2 ([Becker's](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openai-launches-suite-of-ai-tools-for-hospitals-health-systems/)) **US→EU** |
| **Abridge × Epic** | Big-tech/AI × EHR | "Abridge Inside" co-built via Epic's Workshop (ED first, then inpatient); generative AI inside Epic workflows | 2025 | The scribe is fused into the EHR of record — distribution moat | T1 ([Abridge](https://www.abridge.com/press-release/abridge-inside-for-emergency-medicine-announcement)) **US→EU** |
| **Abridge × Availity** | Payer × AI | Contextual Reasoning Engine into Availity's network for **real-time prior authorization** at the point of conversation; Abridge 200+ systems, Availity 95% of payers / 3M providers | **Jan 12, 2026 (JPM26)** | Scribe data now reaches the payer adjudication layer — capture→note→code→prior-auth | T1 ([Abridge](https://www.abridge.com/press-release/abridge-availity-collaboration-announcement)); T2 ([Fierce](https://www.fiercehealthcare.com/ai-and-machine-learning/jpm26-abridge-teams-availity-scale-real-time-prior-authorization)) **US→EU** |
| **Highmark Health / AHN × Abridge** | Payer × AI | Payer-provider prior-authorization collaboration | 2025–26 | A named payer (Highmark) directly partnering an AI scribe — payer×AI is real, not theoretical | T1 ([Abridge](https://www.abridge.com/press-release/highmark-health-ahn-abridge-prior-authorization)) **US→EU** |
| **Suki × Google Cloud** | Big-tech × AI scribe | Suki Assistant on Vertex AI adds **patient summarization + clinical Q&A**; "industry's first end-to-end clinical assistant" | **Dec 18, 2024** | A scribe shipping *patient-facing* summarization on hyperscaler infra — direct adjacency to ditto | T1 ([Businesswire](https://www.businesswire.com/news/home/20241218566553/en/Suki-Launches-Patient-Summarization-and-Clinical-QA-for-Doctors-With-Google-Cloud)) **US→EU** |
| **Microsoft × Epic** | Big-tech × EHR | Expanded generative-AI collaboration; Epic charting on Azure OpenAI; Dragon ambient AI for transcription; reaffirmed at Ignite 2025 | 2023 → 2025 | The two largest incumbents jointly own the EHR+AI substrate; Dragon Copilot lands NL early 2026 | T2 ([Healthcare Dive](https://www.healthcaredive.com/news/microsoft-epic-generative-ai-partnership/691505/); [Optimum HIT](https://optimumhit.com/insights/blog/cloud-services/epic-embraces-ai-key-highlights-from-microsoft-ignite-2025/)) **US→EU** |
| **Universal Health Services × Hippocratic AI** | Provider × patient-facing AI | GenAI agents make **post-discharge follow-up phone calls** to patients (Summerlin, Texoma) | 2025 | Patient-facing conversational AI deployed at scale by a provider — the patient-engagement lane | T1 ([UHS](https://uhs.com/news/universal-health-services-launches-hippocratic-ais-generative-ai-healthcare-agents-to-assist-with-post-discharge-patient-engagement/)) **US→EU** |
| **University Hospitals × Hippocratic AI** | Provider × patient-facing AI | Strategic collaboration to deploy conversational agents across the UH system | **Sep 2025** | Second marquee system; Hippocratic claims 50+ systems/payers/pharma in 6 countries, 115M+ patient interactions | T1 ([UH](https://news.uhhospitals.org/news-releases/articles/2025/09/university-hospitals-and-hippocratic-ai-collaborate-to-advance-patient-outcomes)) **US→EU** |
| **AstraZeneca — 40 digital-health partnerships + AstraZeneca Direct** | Pharma × digital-health / D2C | 40 partnerships over three years; D2C patient services launched Oct 2025 | 2022–2025 | Pharma is building direct-to-patient channels that compete for the patient relationship ditto wants | T2 ([Galen Growth](https://www.galengrowth.com/pharma-digital-health-innovation-index-2025/)) **US→EU** |

**Read:** the disclosed marquee deals confirm the count growth is enterprise-AI-driven, and three of them (Suki×Google, Hippocratic deployments, Abridge after-visit work) are explicitly *patient-facing* — the encroachment is already here.

---

## Section 2 — EU AI scribes as serious rivals (deep dive)

The founder's thesis is right: these are well-funded, fast-growing, EU-native, and increasingly patient-facing. They are the *right* kind of competitor (validating the category and adoption velocity), and they hold the clinician relationship — the channel ditto must reach the patient through.

### EU-scribe table

| Scribe | HQ | Funding | Traction / adoption | What they do | Patient-facing after-visit summary? | Tier |
|---|---|---|---|---|---|---|
| **Corti** | Copenhagen, DK | ~$94.5M total ($60M Series B 2023, Prosus/Atomico); CEO says IPO "at some point," not 2026 | **250,000 patient interactions/day** across EU + US hospitals; NHS (UK); DACH via Maris Healthcare (Apr 2025) | Developer AI platform: speech-to-text, medical coding, ambient docs; **FactsR** real-time clinical-reasoning layer (Jun 2025, cuts note-bloat 65%) | Indirect — powers documentation/summarization for partners; reasoning layer could feed patient summaries | T2 ([Tracxn](https://tracxn.com/d/companies/corti/__0s9fLHIXnFrC5tD32K5PLq7c3jKthk5baNst_XJEMfI); [PR Newswire](https://www.prnewswire.com/news-releases/introducing-factsr-by-corti--the-first-clinical-reasoning-layer-for-ambient-ai-in-healthcare-302478475.html)) |
| **Nabla** | Paris, FR | **$120M total** ($70M Series C, HV Capital, Jun 17 2025) | **85,000 clinicians**, 130+ orgs, **20M+ encounters/yr**, 5× revenue in 6 months; athenahealth Marketplace | Ambient scribe → "Adaptive Agentic Platform": coding agent, order agent, nurse/inpatient agent; Nabla Connect embeds in any EHR | **YES — explicit.** Auto-generates patient-friendly "Patient Instructions" as a post-visit recap, in the family's preferred language, written into the EHR | T1/T2 ([STAT](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/); [Nabla help](https://help.nabla.com/en/articles/769346)) |
| **Tortus** | London, UK | Growth-stage (NHS-backed pilots; X-on Health partnership) | NHS England study, **9 London sites, 17,000+ encounters** (Jun 2024–Feb 2025): +23.5% patient-interaction time, −8.2% appt length, A&E +13.4% patients/shift; **£834M/yr** national potential; X-on rollout to 3,500+ GP practices | Ambient voice → summarized clinical notes for clinician review (Surgery Intellect / OSLER) | Summarizes the encounter into notes; patient-recap extension is the natural next step | T2 ([Digital Health](https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/); [GOSH](https://www.gosh.nhs.uk/news/researchgosh-led-trial-of-ai-scribe-technology-shows-transformative-benefits-for-patients-and-clinicians-across-london/)) |
| **Heidi / Accurx Scribe (Tandem)** | UK | Private | Named alongside Tortus in NHS buyer's guides; widely piloted in UK primary care | Ambient scribe for NHS GP/primary care | Note-centric today; primary-care context makes patient instructions a likely add | T2 ([iatroX](https://www.iatrox.com/blog/nhs-ai-scribes-2025-buyers-guide-heidi-tortus-accurx-tandem)) — FLAG (analyst blog) |

### The EHDS-summary threat — be critical and concrete

The threat is not "scribes do summaries." It is **where those summaries land.**

- **Nabla already ships the exact artifact ditto sells.** Its "Patient Instructions" is a patient-friendly, multilingual, post-visit recap — generated automatically and written back to the EHR ([Nabla help, 2025](https://help.nabla.com/en/articles/769346); T1 vendor doc). For a clinician already paying for Nabla, the patient summary is a *free included feature*, not a separate app. That is a bundling threat to a standalone like ditto.
- **EHDS makes the bundle structural, not optional.** From **March 2029**, Patient Summaries (and ePrescriptions/eDispensations) are the first priority data category exchanged across all EU Member States; patients get free, fast access and control over their own electronic health record, including cross-border ([EC Health, 2025](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en); [Regulation (EU) 2025/327, EY, 2025](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds); T1). If a scribe writes a standardized patient summary directly into the EHDS-linked record, the patient receives it *natively in the national patient portal* — no separate app required.
- **So the question for ditto is: what edge survives when the summary is a commodity inside the record?** Concrete, defensible edges:
  - **Comprehension and longitudinal continuity, not single-visit capture.** Scribes produce a per-encounter artifact tied to one clinician. ditto's value is stitching *the whole record over time* into plain-language understanding — the layer EHDS exposes but does not interpret.
  - **Patient-side trust, UX and engagement.** EHDS gives access; it does not give a delightful, trustworthy consumer experience. Scribe summaries are a by-product of a clinician tool, not designed for patient comprehension, reminders, or follow-through.
  - **EHDS as a feed, not a competitor.** ditto can consume the standardized EHDS patient summary as an *input* and add the comprehension/engagement layer on top — turning the threat into a data source. This requires ditto to be EHDS-ready early.
  - **Cross-source aggregation beyond one EHR.** Scribe summaries cover the encounters their host clinician runs; ditto can aggregate across providers, wellness apps, and patient-entered data.
- **Net assessment (critical):** the scribes' patient summaries are a **real and near-term encroachment** on the *artifact*, and EHDS will commoditize the *artifact* further. ditto's durable moat is therefore the **interpretation + continuity + patient-trust layer**, plus being an early EHDS data-consumer rather than an aggregator that EHDS makes redundant. If ditto positions as "we generate summaries," it loses; if it positions as "we make your whole, cross-provider record understandable and actionable over time," it wins. (High confidence on the threat direction; medium on 2029 timing executing on schedule.)

**Adoption-momentum note (founder's point):** Kaiser (24,600 physicians), Mayo (2,000+ physicians), Nabla (85k clinicians / 20M+ encounters), Corti (250k interactions/day), NHS national rollouts — healthcare-AI adoption velocity is at an all-time high. Well-funded + fast-growing rivals are the signal that the *category* is being adopted; that is the right user base to be adjacent to, not a red flag.

---

## Section 3 — Why ChatGPT Health is blocked in the EU (the detailed reasoning)

At launch (Jan 7–8, 2026), ChatGPT Health shipped to supported countries **excluding the EEA, Switzerland and the UK** ([Euronews, 2026](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations); T2). Three independent legal mechanisms each suffice to block it; together they make EU entry slow and expensive.

### Mechanism 1 — GDPR Article 9 special-category health data (+ transfer scrutiny)
- Health data is **special-category personal data** under **GDPR Art. 9**, prohibited from processing unless a narrow exception applies (explicit consent, etc.). ChatGPT Health connects medical records + wellness-app data — squarely Art. 9 ([heise, 2026](https://www.heise.de/en/news/ChatGPT-Health-OpenAI-launches-AI-health-assistant-11134998.html); T2).
- A consumer product relying on **explicit consent** for sensitive health data faces fragile, revocable consent and DPIA obligations under Art. 35.
- **US data transfers** are examined "particularly strictly" for health data; even under the EU–US Data Privacy Framework, supervisory authorities scrutinize sensitive-category transfers. This is why **data residency/localization** is a precondition, not a nicety ([heise, 2026](https://www.heise.de/en/news/ChatGPT-Health-OpenAI-launches-AI-health-assistant-11134998.html); T2).

### Mechanism 2 — EU AI Act high-risk classification
- Under **Art. 6(1)**, an AI system that is itself a medical device (or a safety component of one) regulated under **MDR 2017/745** is **automatically high-risk**; medical-use AI also falls under the Annex III high-risk regime ([Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-healthcare-ai-regulations-mdr-gdpr-ai-act); [Decomplix](https://decomplix.com/ai-medical-device-software-eu-mdr-ivdr/); T2).
- High-risk obligations: transparency, explainability, reproducible/replicable outputs, risk management, human oversight, logging, conformity assessment — hard to meet for a probabilistic general-purpose chatbot whose outputs are non-deterministic ([thewellnesslondon, 2026]; T3 FLAG, corroborated by Tandem).
- Timeline: high-risk SaMD obligations phase in **Aug 2026**, or **Aug 2027** for CE-marked devices under Notified-Body review ([mdxcro, 2026](https://mdxcro.com/eu-ai-act-medical-devices-samd/); T2).

### Mechanism 3 — MDR medical-device classification risk + liability
- If the tool gives clinical/diagnostic guidance, it likely meets the **medical-device** definition, requiring **CE marking** under MDR, a Notified Body, and clinical evaluation. The UK MHRA has said such a platform would "likely be considered a medical device" ([doctors.net.uk, 2026](https://www.doctors.net.uk/news/chatgpt-health-likely-to-be-regulated-as-medical-device-in-the-uk); T2). The same logic applies under EU MDR.
- The expected pattern is a **single CE mark with two declarations of conformity** (MDR + AI Act) — a heavy dual-conformity burden ([Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-healthcare-ai-regulations-mdr-gdpr-ai-act); T2).
- **Liability:** medical-device status + the revised EU product-liability/AI-liability regime expose OpenAI to clinical-harm claims it does not face for general chat — a strong incentive to geofence rather than risk it.

### OpenAI's own stated reasons
- OpenAI's public framing is restrained: Health is available "in supported countries (excluding the EEA, Switzerland and the UK)," with EU exclusion attributed to **more restrictive local health and data regulations** ([Euronews, 2026](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations); T2). OpenAI also stresses health content **won't be used for training** — a GDPR-purpose-limitation signal, but not enough to clear Art. 9 + AI Act + MDR together.

### Durability and entry path (timeline view) — **US→EU**
- **How durable:** robust in the near term. The barrier is three stacked regimes; clearing one (e.g., DPF transfer mechanics) still leaves AI Act + MDR. EHDS adds further governance for any product touching the patient record.
- **What entry requires:** (1) EU **data residency/localization** + DPIAs + a durable Art. 9 legal basis; (2) either a defensible **non-medical-device** scoping (pure general-info, no individualized clinical advice) *or* full **MDR CE marking** with a Notified Body; (3) an **AI Act conformity** path for high-risk use; (4) DPA engagement / approvals member-state by member-state.
- **Realistic timeline:** a localized, compliant EU launch by a US giant is plausible **2027–2028** at the earliest, lagging native-EU players (Nabla, Corti, Doctolib, Ada) who are compliant-by-construction. A *non-medical, info-only* EU variant could appear sooner but would be deliberately less capable. (Medium confidence on timing.)

**Strategic implication for ditto:** the EU regulatory moat is *temporarily* keeping the largest US consumer-AI entrant out of ditto's exact lane. That is a window — but a closing one. ditto's advantage is being EU/NL-native, EHDS-ready and patient-trust-first *before* the US giants localize.

---

## Sources

### Tier 1 — filings / official company & regulator releases / legal texts
- Viz.ai × Sanofi × Regeneron COPD collaboration — [Businesswire, 2025](https://www.businesswire.com/news/home/20250520566222/en/Viz.ai-Announces-Collaboration-With-Sanofi-and-Regeneron-to-Improve-Management-and-Care-of-Chronic-Obstructive-Pulmonary-Disease-COPD)
- OpenAI for Healthcare launch — [OpenAI, 2026](https://openai.com/index/openai-for-healthcare/)
- Abridge Inside for Emergency Medicine / Epic Workshop — [Abridge, 2025](https://www.abridge.com/press-release/abridge-inside-for-emergency-medicine-announcement)
- Abridge × Availity prior authorization — [Abridge, 2026](https://www.abridge.com/press-release/abridge-availity-collaboration-announcement)
- Highmark Health / AHN × Abridge — [Abridge, 2025-26](https://www.abridge.com/press-release/highmark-health-ahn-abridge-prior-authorization)
- Suki × Google Cloud patient summarization & Q&A — [Businesswire, 2024](https://www.businesswire.com/news/home/20241218566553/en/Suki-Launches-Patient-Summarization-and-Clinical-QA-for-Doctors-With-Google-Cloud)
- UHS × Hippocratic AI post-discharge agents — [UHS, 2025](https://uhs.com/news/universal-health-services-launches-hippocratic-ais-generative-ai-healthcare-agents-to-assist-with-post-discharge-patient-engagement/)
- University Hospitals × Hippocratic AI — [UH, 2025](https://news.uhhospitals.org/news-releases/articles/2025/09/university-hospitals-and-hippocratic-ai-collaborate-to-advance-patient-outcomes)
- Hippocratic AI $126M Series C ($3.5B) — [Businesswire, 2025](https://www.businesswire.com/news/home/20251103432446/en/Hippocratic-AI-Raises-$126-Million-in-Series-C-at-$3.5-Billion-Valuation-Led-by-Avenir-Growth-to-Expand-Clinically-Safe-Generative-AI-Agents-Across-Healthcare)
- Nabla "Patient Instructions" post-visit recap (vendor doc) — [Nabla help, 2025](https://help.nabla.com/en/articles/769346)
- Corti FactsR clinical-reasoning layer — [PR Newswire, 2025](https://www.prnewswire.com/news-releases/introducing-factsr-by-corti--the-first-clinical-reasoning-layer-for-ambient-ai-in-healthcare-302478475.html)
- EHDS Regulation (EU) 2025/327 — [EC Health, 2025](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en); [EY summary, 2025](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds)

### Tier 2 — trade press / analyst
- OpenAI for Healthcare hospital partners — [Becker's, 2026](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openai-launches-suite-of-ai-tools-for-hospitals-health-systems/)
- ChatGPT Health EU exclusion + reasons — [Euronews, 2026](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations); [heise, 2026](https://www.heise.de/en/news/ChatGPT-Health-OpenAI-launches-AI-health-assistant-11134998.html)
- Abridge × Availity (JPM26) — [Fierce Healthcare, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/jpm26-abridge-teams-availity-scale-real-time-prior-authorization)
- Microsoft × Epic generative-AI partnership — [Healthcare Dive, 2023](https://www.healthcaredive.com/news/microsoft-epic-generative-ai-partnership/691505/); [Optimum HIT (Ignite 2025), 2025](https://optimumhit.com/insights/blog/cloud-services/epic-embraces-ai-key-highlights-from-microsoft-ignite-2025/)
- Viz.ai × Novartis oncology — [MobiHealthNews, 2024](https://www.mobihealthnews.com/news/vizai-novartis-partner-ai-powered-care-patients-cancer)
- AstraZeneca 40 partnerships + Direct — [Galen Growth, 2025](https://www.galengrowth.com/pharma-digital-health-innovation-index-2025/)
- Nabla $70M Series C / traction — [STAT, 2025](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/); [Fierce, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/nabla-banks-70m-series-c)
- Corti profile / funding / traction — [Tracxn, 2026](https://tracxn.com/d/companies/corti/__0s9fLHIXnFrC5tD32K5PLq7c3jKthk5baNst_XJEMfI); [CNBC, 2025](https://www.cnbc.com/2025/12/30/corti-will-go-public-but-not-in-2026-says-ai-healthcare-startups-ceo.html); Corti × Maris Healthcare DACH — [Corti, 2025](https://www.corti.ai/news/corti-and-maris-healthcare)
- Tortus NHS study / X-on rollout — [Digital Health, 2025](https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/); [GOSH, 2025](https://www.gosh.nhs.uk/news/researchgosh-led-trial-of-ai-scribe-technology-shows-transformative-benefits-for-patients-and-clinicians-across-london/)
- EU AI Act / MDR / CE-marking mechanics — [Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-healthcare-ai-regulations-mdr-gdpr-ai-act); [mdxcro, 2026](https://mdxcro.com/eu-ai-act-medical-devices-samd/); [Decomplix](https://decomplix.com/ai-medical-device-software-eu-mdr-ivdr/)
- ChatGPT Health "likely medical device" (MHRA) — [doctors.net.uk, 2026](https://www.doctors.net.uk/news/chatgpt-health-likely-to-be-regulated-as-medical-device-in-the-uk)
- EHDS legal commentary — [Skadden, 2025](https://www.skadden.com/insights/publications/2025/06/the-european-health-data-space)

### Tier 3 — blogs / vendor self-report (FLAGGED)
- AI Act explainability/replicability argument for ChatGPT Health — [thewellnesslondon, 2026] (analyst blog; corroborated by Tandem Health T2) — FLAG
- NHS scribe buyer's guide (Heidi/Tortus/Accurx) — [iatroX, 2025](https://www.iatrox.com/blog/nhs-ai-scribes-2025-buyers-guide-heidi-tortus-accurx-tandem) — FLAG

---

## Deep-dive blocks (ready-to-embed)

### (a) Marquee partnerships
The 2024–2026 partnership surge is enterprise-AI-driven across four axes: pharma×digital-health (Viz.ai×Sanofi/Regeneron for COPD, May 2025; Viz.ai×Novartis oncology), big-tech×health-system (OpenAI for Healthcare onboarding ~8 marquee US systems incl. Cedars-Sinai, UCSF, Boston Children's and HCA, Jan 2026), payer×AI (Abridge×Availity real-time prior authorization at JPM26, Jan 2026; Highmark×Abridge), and big-tech×EHR (Microsoft×Epic ambient AI; Abridge Inside built in Epic's Workshop). Three of these are explicitly patient-facing — Suki×Google Cloud patient summaries (Dec 2024) and Hippocratic AI's post-discharge patient calls at UHS and University Hospitals — confirming that the marquee deals are encroaching directly on ditto's patient lane, not just clinician documentation.
- [Viz.ai × Sanofi/Regeneron COPD — Businesswire, 2025](https://www.businesswire.com/news/home/20250520566222/en/Viz.ai-Announces-Collaboration-With-Sanofi-and-Regeneron-to-Improve-Management-and-Care-of-Chronic-Obstructive-Pulmonary-Disease-COPD)
- [OpenAI for Healthcare — OpenAI, 2026](https://openai.com/index/openai-for-healthcare/) · [hospital partners — Becker's, 2026](https://www.beckershospitalreview.com/healthcare-information-technology/ai/openai-launches-suite-of-ai-tools-for-hospitals-health-systems/)
- [Abridge × Availity prior auth — Abridge, 2026](https://www.abridge.com/press-release/abridge-availity-collaboration-announcement)
- [Suki × Google patient summaries — Businesswire, 2024](https://www.businesswire.com/news/home/20241218566553/en/Suki-Launches-Patient-Summarization-and-Clinical-QA-for-Doctors-With-Google-Cloud)
- [UHS × Hippocratic AI post-discharge agents — UHS, 2025](https://uhs.com/news/universal-health-services-launches-hippocratic-ais-generative-ai-healthcare-agents-to-assist-with-post-discharge-patient-engagement/)
- [Microsoft × Epic — Healthcare Dive, 2023](https://www.healthcaredive.com/news/microsoft-epic-generative-ai-partnership/691505/)

### (b) EU scribes + the EHDS-summary threat
EU-native scribes are well-funded and fast-growing: Nabla (Paris, $120M, 85k clinicians, 20M+ encounters/yr), Corti (Copenhagen, ~$95M, 250k interactions/day, NHS+DACH), Tortus (London, NHS study across 9 sites and 17,000 encounters, £834M/yr national upside). Critically, Nabla *already* auto-generates patient-friendly, multilingual after-visit "Patient Instructions" written back to the EHR — the exact artifact a standalone patient-summary app sells, bundled free inside the clinician's tool. The EHDS makes this structural: from March 2029, standardized Patient Summaries become a mandatory cross-border data category surfaced in national patient portals. ditto's durable edge is therefore NOT generating the summary but owning the comprehension + longitudinal-continuity + patient-trust layer, and consuming the EHDS summary as an input rather than competing as a now-commoditized aggregator. Position as "we make your whole, cross-provider record understandable over time," not "we generate summaries."
- [Nabla "Patient Instructions" — Nabla help, 2025](https://help.nabla.com/en/articles/769346)
- [Nabla $70M Series C / traction — STAT, 2025](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/)
- [Corti profile/traction — Tracxn, 2026](https://tracxn.com/d/companies/corti/__0s9fLHIXnFrC5tD32K5PLq7c3jKthk5baNst_XJEMfI)
- [Tortus NHS study — Digital Health, 2025](https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/)
- [EHDS Regulation — EC Health, 2025](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)

### (c) Why ChatGPT Health is EU-blocked (legal mechanisms)
ChatGPT Health launched Jan 2026 excluding the EEA, Switzerland and the UK because three independent legal regimes each suffice to block it. GDPR Art. 9 treats health data as special-category, demanding explicit consent, DPIAs, and strict scrutiny of US transfers — forcing EU data residency. The EU AI Act auto-classifies medical-use AI as high-risk (Art. 6(1) via MDR/Annex III), imposing transparency, explainability, reproducibility and conformity-assessment duties hard for a probabilistic chatbot to meet (high-risk obligations phasing in Aug 2026/Aug 2027). And MDR likely classifies an individualized health-advice tool as a medical device requiring CE marking, a Notified Body, and dual MDR+AI Act declarations of conformity — plus elevated liability. OpenAI's own framing cites "more restrictive local health and data regulations." The barrier is durable: clearing one regime leaves the others. Realistic localized EU entry by US giants is 2027–2028, behind compliant-by-construction EU incumbents — a closing window ditto should exploit now.
- [ChatGPT Health EU exclusion — Euronews, 2026](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations)
- [GDPR Art. 9 / US-transfer scrutiny — heise, 2026](https://www.heise.de/en/news/ChatGPT-Health-OpenAI-launches-AI-health-assistant-11134998.html)
- [AI Act / MDR / CE-marking mechanics — Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-healthcare-ai-regulations-mdr-gdpr-ai-act)
- [SaMD AI Act deadlines — mdxcro, 2026](https://mdxcro.com/eu-ai-act-medical-devices-samd/)
- [Likely "medical device" (MHRA) — doctors.net.uk, 2026](https://www.doctors.net.uk/news/chatgpt-health-likely-to-be-regulated-as-medical-device-in-the-uk)
