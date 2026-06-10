# M8 — Strategic Moves & Migrations Map

**Module:** M8 (Strategic Moves & Migrations)
**Prepared for:** ditto.care strategy team
**Access date:** 2026-06-10
**Scope:** Documented competitive entries + adjacency expansions across digital health, AI clinical documentation, femtech, consumer health, and PHR infrastructure. The goal is *directional*: where players are heading, not just where they sit today.

**Tiering:** Tier 1 = filings / official company releases / analyst trackers; Tier 2 = trade press; Tier 3 = blogs / self-report (FLAGGED inline). **US→EU** flag marks moves originating in a US-regulatory context whose EU/NL relevance needs separate validation.

---

## Key takeaways

1. **The dominant vector is "capture → workflow → revenue."** Every leading ambient AI scribe (Abridge, Nabla, Ambience, Suki, Dragon/Microsoft) has migrated from *transcribing the visit* to *coding, orders, prior-auth, and revenue-cycle (RCM)* within ~18 months. Documentation is now treated as the wedge, not the product. (Tier 1/2, high confidence.)
2. **"Agentic" is the new packaging of that same vector** — Nabla, Suki and Ambience now describe multi-agent platforms (coding agent, order agent, nurse/inpatient agent) rather than a single scribe. (Tier 1/2, high confidence.)
3. **Single-condition consumer apps are becoming life-stage / multi-condition platforms.** Flo (period → perimenopause/menopause), Belong.Life (cancer → MS → weight). The pattern: monetize one cohort, then expand the *same engagement engine* to adjacent indications. (Tier 1/2, high confidence.)
4. **Consumer ↔ clinical/regulated crossing runs both ways in the EU.** DiGA (Germany) pulls wellness apps toward prescription/reimbursement (Oviva, Sidekick via aidhere/zanadio); meanwhile big consumer AI (OpenAI ChatGPT Health, Jan 2026) pushes down from general-purpose chat into grounded personal-health Q&A. (Tier 1/2, high confidence; **US→EU** flag on ChatGPT Health.)
5. **Data plumbing is climbing the stack into a comprehension/AI layer.** b.well moved from PHR aggregation to a "Health AI SDK" and was selected to power OpenAI's ChatGPT Health data connectivity — the clearest signal that aggregation alone is commoditizing and the value is moving to the comprehension layer ditto occupies. (Tier 1/2, high confidence; **US→EU** flag.)
6. **The EHR incumbent (Epic) is entering ditto's exact lane.** Epic's patient-facing assistant "Emmie" delivers plain-language lab/visit explanations inside MyChart (announced 2025, rolling out into 2026) — a structural fast-follow risk for patient-facing summaries. (Tier 1/2, high confidence; **US→EU** flag — Epic's NL footprint is limited but its product direction sets buyer expectations.)
7. **D2C is converging on B2B2C, and B2B is acquiring its way to a full "operating system."** Ro/Hims push from cash-pay D2C toward payer/employer-credible chronic care; Commure+Athelas consolidated scribing, RCM, RPM and patient comms into one "CommureOS" via the Augmedix and Memora acquisitions. (Tier 1/2, high confidence; **US→EU** flag.)

---

## Summary table: player → from → to → signal

| Player | From (wedge) | To (adjacency) | Signal for ditto |
|---|---|---|---|
| **Abridge** | Ambient scribe | Coding/"billable notes", outpatient orders, nursing docs, real-time prior-auth (Availity) | Scribes own the clinician relationship and are extending toward the *whole encounter*, incl. patient after-visit summaries |
| **Nabla** | Ambient scribe | "Adaptive Agentic Platform": coding agent, order agent, nurse/inpatient agent; embeddable via Nabla Connect | EU-origin (France) player going agentic + platform; closest cultural analog to ditto's geography |
| **Ambience** | Ambient scribe | End-to-end coding (claims >physician ICD-10 accuracy), inpatient CDI, full continuum platform | Coding accuracy is becoming the moat; documentation alone is table stakes |
| **Suki** | Voice assistant / scribe | Ambient order staging (Rx), CPT/E&M coding, patient summarization + Q&A, RCM | Even "assistant" framing collapses into the capture→workflow→revenue vector |
| **Microsoft/Nuance (Dragon Copilot)** | Dictation + DAX scribe | Merged Dragon Copilot brand; referral letters, after-visit & encounter summaries, order suggestions, ICD-10; EU rollout incl. NL early 2026 | Incumbent with scale entering after-visit summaries + landing in NL |
| **Epic (Emmie / Art)** | EHR of record | Patient-facing plain-language lab/imaging/visit explanations in MyChart; clinician pre-visit summaries | **Direct overlap with ditto's patient-facing summary wedge** |
| **Flo Health** | Period/ovulation tracker | Pregnancy → perimenopause (Jul 2025) → menopause; full female life-stage platform; €1B+ unicorn | Single-utility → life-stage platform playbook; femtech's reference case |
| **Belong.Life** | Cancer social network + AI mentor (Dave) | MS (Sophie), weight/health (Fred), trial matching (Tara) — multi-indication AI companion | The "condition companion → companion platform" path ditto could face |
| **Ada Health** | Consumer symptom checker | Enterprise SaaS for pharma/payers/providers/governments (Bayer, Novartis, Pfizer, Takeda, Sanofi) | Classic D2C → B2B2C pivot; care-navigation framing |
| **Oviva / Sidekick** | Coaching / wellness | DiGA-listed prescription therapeutics (Oviva Direkt obesity; Sidekick via aidhere/zanadio) | EU wellness → regulated/reimbursed crossing |
| **b.well** | PHR / data aggregation | "Health AI SDK"; powers OpenAI ChatGPT Health data connectivity | Plumbing → comprehension layer; the layer ditto wants to own |
| **OpenAI (ChatGPT Health)** | General-purpose chat | Grounded personal-health Q&A over linked portals/Apple Health/wellness apps (Jan 2026) | Consumer-AI giant entering patient comprehension top-down |
| **Ro / Hims & Hers** | D2C Rx (ED, hair, GLP-1) | Chronic care w/ outcomes data → payer/employer (B2B2C) credibility | D2C → B2B2C distribution convergence |
| **Commure + Athelas** | Scribe + RCM/RPM | "CommureOS" superplatform via Augmedix (scribe) + Memora (patient comms) acquisitions | Roll-up toward a single healthcare "operating system" |

---

## Vector 1 — Ambient scribe → coding → orders/RCM → "agentic" workflow

This is the most documented and fastest-moving migration in the market. The scribe captures the conversation; the company then monetizes everything *downstream* of that capture.

- **Abridge.** Raised $250M (Feb 2025) then a $300M Series E led by a16z, doubling valuation to ~$5.3B by June 2025 ([TechCrunch, 2025](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/); Tier 2). It explicitly expanded documentation into AI-generated medical **codes** ("billable notes"), making it directly competitive with CodaMetrix and Epic's own coding feature ([TechTarget, 2025](https://www.techtarget.com/revcyclemanagement/news/366626555/Gen-AI-company-Abridge-raises-300M-targets-revenue-cycle); Tier 2). It has since added **outpatient orders** and **inpatient** ("Abridge Inside"), **nursing documentation** (co-developed with Mayo), and **real-time prior authorization** via an Availity partnership announced Jan 2026 ([Businesswire, 2025](https://www.businesswire.com/news/home/20250618519815/en/Abridge-Announces-Inside-for-Inpatient-and-Initial-Rollout-of-Outpatient-Orders); [Abridge press, 2026](https://www.abridge.com/press-release/abridge-availity-collaboration-announcement); Tier 1/2). **Signal:** the scribe is becoming the revenue-cycle and prior-auth layer — and auto-generated **plain-language after-visit summaries** are part of that envelope, directly adjacent to ditto.
- **Nabla (France).** $70M Series C (HV Capital, June 2025; total $120M) explicitly to "deliver agentic AI to the heart of clinical workflows" ([PR Newswire, 2025](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html); Tier 1). Its **"Adaptive Agentic Platform"** comprises a proactive **coding agent** (ICD-10/HCC/MCC, E&M), a **context-aware agent** that can initiate **orders**, and a **custom care-setting agent** for nurses/inpatient. Nabla Connect (Oct 2025) lets any EHR vendor embed it ([Nabla blog, 2025](https://www.nabla.com/blog/70m-series-c); Tier 3 — self-report, FLAGGED). **Signal:** the EU-origin peer is taking the same capture→workflow path and adding distribution leverage.
- **Ambience Healthcare.** $243M Series C (Oak HC/FT + a16z, July 2025) to scale an end-to-end **documentation + coding + clinical-workflow** platform across ambulatory, ED and inpatient ([HIT Consultant, 2025](https://hitconsultant.net/2025/07/29/ambience-healthcare-raises-243m-to-expand-clinical-ambient-ai-platform/); Tier 2). It claims an ICD-10 coding model that beats board-certified physicians by ~27% (using OpenAI RFT) and launched the first point-of-care **inpatient CDI** assistant ([Ambience, 2025](https://www.ambiencehealthcare.com/blog/ambience-healthcare-s-ai-platform-surpasses-clinician-performance-by-27-in-medical-coding-powered-by-new-openai-breakthrough); Tier 1 self-report on benchmark — treat accuracy claim as vendor-reported). **Signal:** *coding accuracy* is emerging as the defensible moat above commoditizing transcription.
- **Suki.** Industry-first **ambient order staging** (structures/codes/stages Rx orders from the visit, April 2025), plus CPT/E&M coding, **patient summarization & Q&A** (on Google Vertex AI), and RCM ([Suki press, 2025](https://www.suki.ai/press-releases/suki-unveils-industry-first-ambient-orders-staging-for-its-ai-assistant/); Tier 1). **Signal:** even the "assistant" framing converges on the same downstream stack — including patient-facing summarization.
- **Microsoft / Nuance — Dragon Copilot.** DAX Copilot and Dragon Medical One merged into **Dragon Copilot** (March 2025). Beyond notes it now generates **referral letters, after-visit & encounter summaries, ICD-10 coding suggestions, and order suggestions**, embedded in Epic ([Microsoft blog, 2024](https://blogs.microsoft.com/blog/2024/09/26/a-year-of-dax-copilot-healthcare-innovation-that-refocuses-on-the-clinician-patient-connection/); Tier 1). Crucially for ditto: EU rollout to Austria/France/Germany/Ireland (Oct 2025) and **Belgium/Netherlands (early 2026)** ([Healthcare Dive, 2024](https://www.healthcaredive.com/news/dax-copilot-nuance-automated-doctor-tool-artificial-intelligence-healthcare/694818/); Tier 2). **US→EU flag is partly resolved — Dragon Copilot is actively landing in NL with after-visit summaries in scope.**

**Vector reads as:** *capture the encounter → automate the note → automate the code → automate orders/prior-auth → wrap the patient-facing summary.* Patient summaries are increasingly a *feature inside the scribe envelope* rather than a standalone category — a competitive-encroachment risk ditto should track closely.

---

## Vector 2 — Single-condition / single-utility app → life-stage or multi-condition platform

- **Flo Health.** Raised $200M+ from General Atlantic at a $1B+ valuation (July 2024), Europe's first femtech unicorn ([TechCrunch, 2024](https://techcrunch.com/2024/07/30/fertility-tracking-app-flo-health-raises-200m-at-a-1b-valuation/); Tier 2). The capital was earmarked for "new user segments including **perimenopause and menopause**," and **Flo for Perimenopause** launched to all users on 21 July 2025 ([Flo newsroom, 2025](https://flo.health/newsroom/flo-for-perimenopause-is-launching-to-empower-the-1-billion-women-who-experience-perimenopause-without-the-support-they-deserve); Tier 1). 70M+ MAU, 380M+ downloads. **Signal:** the period tracker became a *life-stage platform* (menstruation → conception → pregnancy → perimenopause → menopause) by reusing one engagement/data engine across cohorts — the canonical "single-utility → platform" path.
- **Belong.Life.** Started as the largest cancer social network + AI oncology mentor "Dave" (trained on 7 years of patient/provider interactions) ([Fierce Healthcare, 2023](https://www.fiercehealthcare.com/digital-health/belonglife-maker-social-network-cancer-patients-launches-ai-mentor); Tier 2). It then extended the *same AI-mentor pattern* to **MS (Sophie)**, **weight/health (Fred)**, and **trial matching (Tara)** ([Belong.Life, 2023](https://belong.life/press/belong-life-launches-dave-2/); Tier 3 — self-report, FLAGGED). **Signal for ditto:** a condition companion can generalize into a multi-condition companion platform — relevant because ditto's "Living Health Companion" ambition is the same generalization move, and incumbents in single conditions may race ditto to it.

---

## Vector 3 — Consumer wellness ↔ clinical / regulated (DiGA, prescription)

The EU has a structural on-ramp the US lacks: **DiGA** (Germany's prescribable, reimbursed digital health apps) and equivalent reimbursement pathways. This pulls wellness apps *up* into the regulated tier — and is highly relevant to a NL company contemplating regulated positioning.

- **Oviva.** Crossed from digital coaching into a **DiGA-listed prescription** product, *Oviva Direkt für Adipositas* (obesity), backed by an RCT and endorsed in German obesity guidelines ([DiGA Directory](https://www.diga-verzeichnis.de/en/diga/oviva-direkt-fuer-adipositas); Tier 1; [Nature Int. J. Obesity, 2025](https://www.nature.com/articles/s41366-025-01967-3); Tier 1).
- **Sidekick Health.** Acquired German PDT firm **aidhere** (and thus **zanadio**, 50,000+ DiGA prescriptions filled), explicitly to add "regulated Prescription Digital Therapeutics" to a portfolio that began as consumer engagement ([PR Newswire, 2023](https://www.prnewswire.com/news-releases/sidekick-health-announces-landmark-acquisition-expanding-its-portfolio-to-offer-regulated-prescription-digital-therapeutics-301952420.html); Tier 1). **Signal:** wellness players buy/build into reimbursement to escape D2C unit economics.

**Counter-flow (clinical/general → consumer):** **OpenAI's ChatGPT Health** (launched 7 Jan 2026) is a general-purpose AI pushing *down* into grounded personal-health Q&A: users link patient portals, Apple Health and wellness apps (MyFitnessPal, WW, Peloton, Function) and ask questions over their own labs/visit summaries; OpenAI cites 230M weekly health questions ([OpenAI, 2026](https://openai.com/index/introducing-chatgpt-health/); Tier 1; [Fortune, 2026](https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/); Tier 2). Explicitly **not** described as HIPAA-compliant. **US→EU flag** — EU availability and GDPR/EHDS posture unconfirmed, but the directional threat to consumer comprehension is real and immediate.

---

## Vector 4 — Data plumbing → comprehension / AI layer (PHR aggregators moving up the stack)

- **b.well.** Moved from a PHR aggregation platform to a **"Health AI SDK"** that converts connected health data into "clean, aggregated, AI-optimized inputs for LLM applications" — incl. notes, discharge summaries, labs, care plans ([b.well, 2025](https://www.icanbwell.com/health-sdks-to-power-every-digital-channel/); Tier 3 — self-report, FLAGGED). It was then **selected by OpenAI to power data connectivity for ChatGPT Health** ([PR Newswire, 2026](https://www.prnewswire.com/news-releases/openai-selects-bwell-to-power-secure-health-data-connectivity-for-ai-driven-health-experiences-in-chatgpt-302655598.html); Tier 1; [Fierce Healthcare, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records); Tier 2). **Signal:** raw aggregation is commoditizing into infrastructure; the *comprehension* layer (turning records into understanding) is where value accrues — exactly ditto's territory. Aggregators are racing up; AI giants are racing down; ditto sits in the contested middle. **US→EU flag.**

---

## Vector 5 — D2C → B2B2C distribution, and B2B roll-up toward an "operating system"

- **Ro / Hims & Hers.** Cash-pay D2C leaders (ED, hair, GLP-1; Ro ~$598M annualized revenue 2024, +66% YoY) are publishing clinical outcomes (e.g. 16.6% weight loss over 68 weeks) precisely to become **payer/employer-credible** in chronic care — eroding the historical D2C/B2B2C boundary with platforms like Teladoc/Amwell ([Sacra](https://sacra.com/c/ro/); Tier 1 analyst; [eMarketer, 2025](https://www.emarketer.com/content/direct-to-consumer-telehealth-initiatives-grew-2025--fueled-by-pharma--new-services--federal-push); Tier 2). **US→EU flag.**
- **Ada Health (Berlin).** The cleanest D2C→B2B2C pivot in EU digital health: a consumer symptom checker repositioned as **enterprise care-navigation SaaS** for pharma, payers, providers and governments (Bayer, Novartis, Pfizer, Takeda, Sanofi, Alnylam), reaching profitability with ~260% YoY revenue growth ([Fierce Biotech](https://www.fiercebiotech.com/medtech/symptom-checking-platform-ada-health-inks-partnerships-takeda-sanofi-alnylam); Tier 2). **Signal:** pharma/payer partnerships are the survivable distribution channel for consumer-origin health AI in the EU — a likely ditto channel too.
- **Commure + Athelas.** Merged (~$6B, General Catalyst) into a single "CommureOS" spanning RCM, workflow automation, scribing, patient engagement, RPM and mobile EHR; then acquired **Augmedix** (ambient scribe, ~$139M) and **Memora Health** (patient communication/care coordination, Dec 2024) ([Commure, 2024](https://www.commure.com/blog/commure-and-athelas-sign-deal-to-acquire-augmedix); Tier 1; [Fierce Healthcare, 2024](https://www.fiercehealthcare.com/ai-and-machine-learning/augmedix-acquired-commure-valuation-139-mil); Tier 2). **Signal:** consolidation toward a single "operating system of healthcare" — small point-solutions get bought or boxed in. **US→EU flag.**

---

## Synthesis — the dominant vectors of the market

1. **Capture → workflow → revenue.** Whoever captures the encounter expands into coding, orders, prior-auth and RCM. This is the gravitational center of clinical AI. *Implication for ditto:* patient summaries are being absorbed as a *feature* of scribe platforms (Suki, Dragon Copilot, Abridge) — ditto must define a defensible patient-side wedge the clinician-side scribes will under-serve (longitudinal, daily, cross-encounter comprehension vs. a single after-visit note).
2. **Single-player utility → multi-player / multi-condition network.** Flo and Belong show how one engagement engine generalizes across life-stages/conditions. *Implication:* ditto's "Living Health Companion" is the right shape, but the path runs *through* a beachhead cohort, not across all conditions at once.
3. **Data plumbing → comprehension.** Aggregation commoditizes; understanding is the value layer (b.well climbing up, OpenAI coming down). *Implication:* owning comprehension + trust is more defensible than owning connectivity — but ditto needs a data-access strategy (EHDS, MedMij in NL) so it isn't disintermediated by SDK providers.
4. **D2C → B2B2C.** Pure consumer economics push everyone toward pharma/payer/provider distribution (Ada, Ro, Sidekick). *Implication:* a B2B2C channel (via providers, payers, or pharma) is likely ditto's most durable distribution, consistent with EU reimbursement structures.
5. **Consumer-AI giants entering top-down.** ChatGPT Health is the wildcard: it normalizes "ask AI about my records" at consumer scale. *Implication:* ditto's differentiation must be EU-trust, regulatory posture (GDPR/EHDS/DiGA-style), clinical grounding, and daily-companion continuity — not raw Q&A, where a frontier model wins on capability.

**Net directional read for ditto:** the market is collapsing toward (a) clinician-side scribe superplatforms reaching *into* patient summaries from the visit, and (b) consumer-side AI giants reaching *into* personal-health comprehension from general chat. Ditto sits between them. The defensible space is the **EU-native, trust-and-regulation-anchored, longitudinal patient-comprehension layer** — the part neither the US scribes nor the US consumer-AI giants are positioned to own well in the Netherlands. Track Dragon Copilot's NL launch (early 2026) and Epic Emmie as the most concrete near-term encroachment signals.

---

## Sources

### Tier 1 — filings / official company releases / analyst trackers
- Nabla — Series C release: https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html
- Abridge — Inside for Inpatient / Outpatient Orders: https://www.businesswire.com/news/home/20250618519815/en/Abridge-Announces-Inside-for-Inpatient-and-Initial-Rollout-of-Outpatient-Orders
- Abridge — Availity prior-auth collaboration: https://www.abridge.com/press-release/abridge-availity-collaboration-announcement
- Suki — Ambient Orders Staging release: https://www.suki.ai/press-releases/suki-unveils-industry-first-ambient-orders-staging-for-its-ai-assistant/
- Ambience — coding-accuracy / OpenAI RFT release (vendor benchmark): https://www.ambiencehealthcare.com/blog/ambience-healthcare-s-ai-platform-surpasses-clinician-performance-by-27-in-medical-coding-powered-by-new-openai-breakthrough
- Microsoft — "A year of DAX Copilot" (capabilities): https://blogs.microsoft.com/blog/2024/09/26/a-year-of-dax-copilot-healthcare-innovation-that-refocuses-on-the-clinician-patient-connection/
- Flo — Perimenopause launch: https://flo.health/newsroom/flo-for-perimenopause-is-launching-to-empower-the-1-billion-women-who-experience-perimenopause-without-the-support-they-deserve
- Belong.Life — "Dave" launch: https://belong.life/press/belong-life-launches-dave-2/
- DiGA Directory — Oviva Direkt für Adipositas: https://www.diga-verzeichnis.de/en/diga/oviva-direkt-fuer-adipositas
- Nature, Int. J. Obesity (2025) — Oviva RCT: https://www.nature.com/articles/s41366-025-01967-3
- Sidekick Health — aidhere/zanadio PDT acquisition: https://www.prnewswire.com/news-releases/sidekick-health-announces-landmark-acquisition-expanding-its-portfolio-to-offer-regulated-prescription-digital-therapeutics-301952420.html
- OpenAI — Introducing ChatGPT Health: https://openai.com/index/introducing-chatgpt-health/
- b.well x OpenAI — data connectivity selection: https://www.prnewswire.com/news-releases/openai-selects-bwell-to-power-secure-health-data-connectivity-for-ai-driven-health-experiences-in-chatgpt-302655598.html
- Commure — Augmedix acquisition / CommureOS: https://www.commure.com/blog/commure-and-athelas-sign-deal-to-acquire-augmedix
- Sacra — Ro company profile (analyst): https://sacra.com/c/ro/
- Sacra — Abridge company profile (analyst): https://sacra.com/c/abridge/

### Tier 2 — trade press
- TechCrunch (2025) — Abridge valuation doubles to $5.3B: https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/
- TechTarget (2025) — Abridge $300M, targets revenue cycle: https://www.techtarget.com/revcyclemanagement/news/366626555/Gen-AI-company-Abridge-raises-300M-targets-revenue-cycle
- Fierce Healthcare — Abridge $250M Series D: https://www.fiercehealthcare.com/ai-and-machine-learning/abridge-scores-250m-series-d-ambient-ai-tech-now-use-100-health-systems
- STAT (2025) — Nabla $70M: https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/
- HIT Consultant (2025) — Ambience $243M: https://hitconsultant.net/2025/07/29/ambience-healthcare-raises-243m-to-expand-clinical-ambient-ai-platform/
- Healthcare Dive — DAX Copilot rollout: https://www.healthcaredive.com/news/dax-copilot-nuance-automated-doctor-tool-artificial-intelligence-healthcare/694818/
- TechCrunch (2024) — Flo $200M / unicorn: https://techcrunch.com/2024/07/30/fertility-tracking-app-flo-health-raises-200m-at-a-1b-valuation/
- Fierce Healthcare — Flo $200M: https://www.fiercehealthcare.com/digital-health/fertility-and-period-tracking-app-flo-health-bank-200m-reach-unicorn-status
- Fierce Healthcare (2023) — Belong.Life AI mentor: https://www.fiercehealthcare.com/digital-health/belonglife-maker-social-network-cancer-patients-launches-ai-mentor
- Fierce Biotech — Ada Health pharma partnerships (Takeda/Sanofi/Alnylam): https://www.fiercebiotech.com/medtech/symptom-checking-platform-ada-health-inks-partnerships-takeda-sanofi-alnylam
- Fortune (2026) — OpenAI ChatGPT Health: https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/
- TechCrunch (2026) — ChatGPT Health / 230M weekly: https://techcrunch.com/2026/01/07/openai-unveils-chatgpt-health-says-230-million-users-ask-about-health-each-week/
- Fierce Healthcare (2026) — OpenAI/b.well ChatGPT Health: https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records
- Fierce Healthcare (2025) — Epic AI moves & scribe market: https://www.fiercehealthcare.com/ai-and-machine-learning/how-epics-ai-moves-could-shake-health-tech-market
- Fierce Healthcare (2024) — Commure acquires Augmedix: https://www.fiercehealthcare.com/ai-and-machine-learning/augmedix-acquired-commure-valuation-139-mil
- eMarketer (2025) — D2C telehealth growth: https://www.emarketer.com/content/direct-to-consumer-telehealth-initiatives-grew-2025--fueled-by-pharma--new-services--federal-push
- Hospitalogy (2025) — Inside Commure: https://hospitalogy.com/articles/2025-10-22/inside-commure-the-ai-platform-powering-healthcare-transformation-today/
- Advisory.com (2025) — Epic debuts new AI tools (Emmie/Art): https://www.advisory.com/daily-briefing/2025/08/28/epic-meeting
- Digital Health (2025) — Epic native AI charting: https://www.digitalhealth.net/2025/08/epic-announces-the-launch-of-native-ai-charting-tool/

### Tier 3 — blog / self-report (FLAGGED — treat as directional, vendor-stated)
- Nabla blog — "$70M Series C: Just Getting Started" (agentic platform detail): https://www.nabla.com/blog/70m-series-c
- b.well — "Four Health SDKs" / Health AI SDK (self-described capabilities): https://www.icanbwell.com/health-sdks-to-power-every-digital-channel/
- Belong.Life — product/portfolio pages (Sophie/Fred/Tara): https://belong.life/
- Epic — AI for Patients (Emmie) product page: https://www.epic.com/software/ai-patients/

### Confidence & flags
- **High confidence** on all funding events, named product launches, and acquisitions (multiple Tier 1/2 corroboration).
- **Vendor-reported, verify independently:** Ambience's "+27% vs physicians" coding-accuracy benchmark; Nabla/Suki/b.well clinician-count and revenue-multiple claims (Tier 1 release or Tier 3 self-report).
- **US→EU flags:** ChatGPT Health, b.well, Epic Emmie, Commure/Athelas, Ro/Hims are US-context; EU/NL availability and GDPR/EHDS/DiGA posture need separate validation. **Exception — already EU-relevant:** Nabla (France), Flo (UK/EU), Ada (Berlin), Oviva & Sidekick (DiGA/Germany), and Dragon Copilot (confirmed NL rollout early 2026).
- **Unconfirmed:** No standalone EU-native patient-facing-summary fast-follower to ditto was identified in this pass beyond Dragon Copilot's NL after-visit summaries and Epic Emmie; flagged as a gap for a dedicated competitor scan.
