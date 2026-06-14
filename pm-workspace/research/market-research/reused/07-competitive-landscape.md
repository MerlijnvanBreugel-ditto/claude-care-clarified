# 07 — Competitive & Solution Landscape

**Prepared for:** ditto.care competitive intelligence
**Scope:** Players adjacent to a patient-level AI summary of healthcare appointments; mapping who serves whom, EU presence, and — most importantly — what they do NOT solve.
**Method:** Web research (WebSearch + WebFetch). Access date for all URLs: **2026-05-31**.
**Source tiers:** Tier 1 = company filings / funding databases / official product docs; Tier 2 = reputable tech/health press, analyst reports; Tier 3 = blogs (flagged). Company self-claims flagged as such.

---

## Key takeaways

1. **The money and momentum are almost entirely clinician-facing.** The best-funded category by an order of magnitude is AI medical scribes (Abridge $5.3B valuation, Nabla $120M raised, Corti $94.5M, Microsoft/Nuance Dragon Copilot). These optimize clinician documentation and revenue cycle — the *patient* and *caregiver* are bystanders, and the visit summary is a by-product, not the product. **Confidence: High.**

2. **"Patient-facing summary" today means one of two weak things:** (a) a templated **after-visit summary (AVS)** auto-generated inside the EHR for compliance (vitals, meds, instructions) — shallow and clinic-bound; or (b) **OpenNotes**-style raw access to the clinician's note — accurate but written *for clinicians*, not translated for patients. Neither is a longitudinal, plain-language companion. **Confidence: High.**

3. **Disease-specific patient companions exist and are consolidating in the EU**, but they are siloed by condition — overwhelmingly **oncology** (Outcomes4Me + Germany's Mika/Fosanis, Jasper Health, Belong.Life, Vinehealth). Nothing spans the *cross-condition* serious-illness journey (cancer + cardiac + neuro + rare disease + frailty). **Confidence: High.**

4. **Caregiver tools and patient tools are separate products.** Caregiver coordination (CaringBridge, Lotsa Helping Hands) is a social/logistics layer with no clinical comprehension; clinical patient apps barely model the caregiver as a first-class user. **Confidence: High.**

5. **EU health-record aggregation is being solved at the infrastructure/government layer** (NL MedMij/PGO, DE ePA opt-out for ~70M people, Apple Health Records) — but these are *data plumbing*, not *comprehension*. They hand the patient raw records, not understanding. **Confidence: High.**

6. **The conspicuous whitespace:** a **patient + caregiver companion that turns each appointment (and the record around it) into plain-language understanding, continuously, across any serious-illness journey, in the EU's fragmented multi-portal reality.** No incumbent owns "the patient's understanding of their own care over time." **Confidence: Medium-High** (negative finding — see Whitespace map for evidence basis and caveats).

---

## 1. AI medical scribes / visit documentation (clinician-facing)

These are the loudest, best-capitalized players. **All are sold to clinicians/health systems**; the patient is the data source, not the customer. Where they emit a "patient summary" (e.g. Abridge real-time patient visit summaries, Dragon Copilot after-visit summaries), it is a clinic-bound feature, single-visit, and not a longitudinal patient/caregiver product.

| Player | Facing | EU presence | Funding / stage | What they do NOT solve |
|---|---|---|---|---|
| **Abridge** (US) | Clinician / health system | US-centric; deep Epic integration | $300M Series E, **$5.3B valuation** (Jun 2025); ~$117M contracted ARR; 150+ health systems [TechCrunch, 2025] | No patient-owned longitudinal record; tied to one health system's Epic instance; not a caregiver product |
| **Microsoft Dragon Copilot (Nuance DAX)** | Clinician | Live UK/Ireland; rolling out AT/FR/DE (Oct 2025), BE/NL (early 2026) [Microsoft, 2025] | Microsoft-owned (Nuance acq. ~$19.7B, 2022) | AVS is a clinician one-click output, not a patient companion; bound to provider/EHR; English-first |
| **Nabla** (FR/US) | Clinician | **Paris-founded**, Highland Europe investor; 35+ languages [STAT, 2025] | $70M Series C, **$120M total** (Jun 2025); 85k clinicians, 20M annual encounters | Documentation/agentic clinical workflow — patient never the user; no caregiver layer |
| **Corti** (DK) | Clinician / health system | **Copenhagen; EU "sovereign" cloud**; strongest EU-native infra story [Corti, 2025] | **$94.5M total**, $60M Series B (Prosus/Atomico) | Real-time clinician co-pilot + coding/QA; patient-facing comprehension out of scope |
| **Tortus** (UK) | Clinician (NHS) | **UK/NHS-native**, DTAC-compliant; rollout to 3,500+ GP practices via X-on [Digital Health, 2025] | NHS Innovation Accelerator-backed; largest NHS AI-scribe trial (+23.5% patient interaction time) | Note-drafting for clinicians; no patient/caregiver deliverable |
| **Heidi Health, Suki, Ambience, Accurx Scribe** | Clinician | Heidi/Accurx active in UK; others US | Various (Tier 2/3) | Same pattern — clinician productivity, not patient understanding |

**Category gap (High):** Scribes capture the *richest raw material* (the actual conversation) but discard the patient as a user. The output lives in the clinician's EHR and the billing pipeline. There is no portable, cross-provider, patient-owned, plain-language understanding that follows the patient across appointments and providers. This is the structural opening ditto.care sits in.

---

## 2. Patient-facing visit summaries / "explain my results"

Three sub-types, all partial:

**(a) EHR after-visit summaries (AVS) — the status quo.** Templated: weight, BP, meds, allergies, instructions. Auto-generated for CMS Promoting Interoperability compliance [Alliance/OpenNotes blog, Tier 3]. Shallow, single-visit, locked to one provider's portal.

**(b) OpenNotes movement.** Patients can read the clinician's *actual* note. 184+ confirmed US health systems; 98% of patients call access a good idea; 73% say it helps them feel in control [OpenNotes.org / Ann Intern Med 7-yr study, 2019]. **But the note is written for clinicians** — jargon, abbreviations, no translation, no synthesis across visits, no caregiver framing.

**(c) AI explainers (lab/results translation).** A crowded but thin layer of point tools: **BloodGPT, Smart Blood Analytics, AIDiagme, Kantesti, TestResult.ai**, plus Stanford Medicine's clinician-mediated results-explainer [Stanford Medicine, 2025]. **PatientNotes** generates patient-facing AVS in the patient's language/reading level (sold to clinicians) [patientnotes.ai, Tier 3]. **Hedy AI** records appointments for patients/caregivers [hedy.ai, Tier 3].

| Player | Facing | Scope | EU | Gap |
|---|---|---|---|---|
| EHR AVS (Epic/MEDITECH/Cerner) | Patient (compliance) | Single visit | EU hospital portals patchy | No synthesis, no translation, provider-locked |
| OpenNotes | Patient | Raw clinician note | Mostly US; some EU/Nordic | Written for clinicians, not translated/synthesized |
| BloodGPT / TestResult.ai / AIDiagme / Kantesti | Patient (self-serve) | **Lab results only** | Mixed, some EU/multilingual | Results-only; no visit context; no longitudinal journey; safety/regulatory unclear (Tier 3) |
| Stanford results-explainer | Clinician-mediated → patient | Results | US | Not a standalone patient product |
| PatientNotes | Clinician-sold patient AVS | Per-visit summary | UK-ish | Still per-visit, clinic-bound |
| Hedy AI | Patient/caregiver | Appointment recording/notes | Global app store | General meeting-style capture; not condition-aware companion |

**Category gap (High):** Everything here is either *single-visit*, *single-modality (labs)*, or *untranslated*. No product owns the full loop: capture the appointment → translate to plain language → place it in the patient's ongoing story → make it caregiver-shareable → carry it across providers.

---

## 3. Patient navigation / care companions (serious illness)

Real products with real funding — but **almost entirely oncology**, and mostly US payer/employer-channel.

| Player | Facing | Condition | EU | Funding | Gap |
|---|---|---|---|---|---|
| **Outcomes4Me** (US) | Patient (+caregiver) | **Cancer** | **Expanding to EU via Mika acquisition (Jun 2025)** | $21M round 2025; ~280k patients [PRNewswire, 2025] | Cancer-only; guideline/trial-matching focus, not appointment comprehension |
| **Mika / Fosanis** (DE) | Patient | **Cancer** | **Germany DiGA — prescribable, statutory-insurance-reimbursed**; MDR IIa [Debiopharm/Medica, Tier 1/2] | Series A (Debiopharm-led); now part of Outcomes4Me | Cancer-only; ePRO + psycho-oncology coaching, not a cross-condition appointment companion |
| **Jasper Health** (US) | Patient + caregiver | **Cancer** | US | ~$31M total; $25M Series A (2022) [Fierce, 2022] | Cancer-only; US payer/Medicare channel |
| **Belong.Life** (IL/US) | Patient | Cancer (+expanding) | Limited EU | Private | Cancer community + navigation; not appointment-level comprehension |
| **Vinehealth** (UK) | Patient | **Cancer** | **UK/EU CE-marked Class I**; acquired by Sciensus (2024) | Innovate UK £1M grant | Cancer self-management; absorbed into pharma services |

**Category gap (High):** This is the closest analog to ditto.care's *companion* posture — but it is **condition-locked (oncology)** and **journey-fragmented**. A patient with heart failure, a neurological diagnosis, a rare disease, or multimorbidity/frailty has no equivalent. And even the cancer companions focus on tracking/trials/coaching, not on *making each appointment understood*.

---

## 4. Caregiver coordination apps

| Player | Facing | EU | What it is | Gap |
|---|---|---|---|---|
| **CaringBridge** (US) | Caregiver/family | Global web | Updates feed, support community; ~900k patients/families served [caring.com, Tier 3] | No clinical comprehension; a journal/feed, not understanding |
| **Lotsa Helping Hands** (US) | Caregiver/family | Global web | Help calendar, task/volunteer coordination | Pure logistics; zero medical content |
| **Birdie** (UK/EU) | **Care agency (B2B)** | UK + Spain, expanding FR/DE/Nordics | Homecare agency SaaS (rostering, care plans); $52M raised, $30M Series B (Sofina) [Sifted, 2022] | **Not family-facing** — it's professional agency software |
| Carely, Caringly, etc. | Family | Mostly US | Family update/coordination | No appointment comprehension |

**Category gap (High):** Caregiver tools are a **social/logistics layer with no clinical brain**. They tell the family *that* there was an appointment, not *what it meant*. Birdie shows the EU caregiver-software market is real but is sold to agencies, not families. Nobody combines caregiver coordination with appointment-level medical understanding.

---

## 5. Personal health records / aggregation (EU emphasis)

This is being solved **at the infrastructure/government layer** — which is data plumbing, not comprehension.

| Player | Facing | EU | Status | Gap |
|---|---|---|---|---|
| **NL MedMij / PGO** (Ivido, Quli, Drimpy, Selfcare) | Patient | **Netherlands** | National framework; goal of well-filled PGO for every citizen by end-2025; GP/hospital/vaccination data flowing [MedMij/HL7, 2025] | Aggregates data into one view — does **not explain or synthesize**; adoption still building |
| **DE ePA "für alle"** (gematik; insurer apps) | Patient | **Germany** | **Opt-out** since Jan 2025; ~70M auto-enrolled, ~5% opt-out; mandatory for providers since Oct 2025; eMedication list called up ~22M times in 3 weeks [gematik/BMG, 2025] | Government record store; the app is a document vault, not a companion |
| **Apple Health Records** | Patient | UK + Canada providers (US for sharing); EU limited | Aggregates EHR data via FHIR/SMART; provider-sharing **US-only** [Apple/MobiHealthNews, 2025] | Aggregation, not comprehension; EU coverage thin |
| **Google Health / consumer PHRs** | Patient | Global | Fragmented, repeatedly sunset/relaunched | No durable EU comprehension layer |

**Category gap (High):** The EU is rapidly giving patients *access to their data* (MedMij, ePA). This is a **tailwind, not a competitor** — it creates a populated substrate and an "I have my records but don't understand them" problem that a comprehension companion can ride. None of these turn records into understanding.

---

## 6. Second-opinion & decision-support platforms

| Player | Facing | EU | What it is | Gap |
|---|---|---|---|---|
| **Teladoc / 2nd.MD, Grand Rounds (Included Health)** | Patient (employer/payer channel) | Mostly US | Expert second opinions for complex/cancer/surgical cases | Episodic, decision-point only; not a daily companion |
| **Medexo** (DE) | Patient | **Germany** | Records-based written second opinion; cooperates with insurers [BMC Health Serv Res, 2021] | One-off opinion; no ongoing understanding |
| German statutory second-opinion directive (2018) | Patient | DE | Legal right to second opinion for certain elective surgeries | Process/right, not a product |
| Hospital programs (Erasmus MC NL, Charité, Dana-Farber, MSK) | Patient | NL/DE + US | Institutional second-opinion services | Bound to institution; episodic |

**Category gap (Medium):** Second opinions are **episodic decision-support at branch points**, not continuous comprehension. Complementary to, not competitive with, an always-on companion.

---

## 7. EHR patient portals / incumbents (the status quo)

| Player | Facing | EU | Role | Where it fails serious-illness patients |
|---|---|---|---|---|
| **Epic MyChart** | Patient | US-dominant; some EU hospital deployments | The default portal; messaging, AVS, results, OpenNotes | **Fragmentation:** a patient seen by multiple orgs juggles **separate MyChart accounts per organization** and must manually assemble their history — subject of a 2025 class-action alleging MyChart fragments records, with plaintiffs unable to assemble records during disability/serious-illness episodes [Becker's/Nurse.org, 2025]. Accessibility barriers for elderly, low-literacy, non-English, cognitively impaired patients [JMIR, 2025] |
| **EU hospital portals** (e.g. Chipsoft/HiX NL, various DE) | Patient | EU | Per-hospital portals | Even more fragmented than US; per-hospital silos, no cross-provider synthesis, no caregiver model |

**Category gap (High):** Portals are **provider-centric and silo'd by institution**. For exactly the patients who see the most providers (serious/chronic illness), the portal model breaks down: many logins, no synthesis, jargon notes, no caregiver access, no plain-language layer. This is the strongest documented evidence of the unmet need.

---

## Whitespace map

**The conspicuous, unowned space:** a **patient-and-caregiver comprehension companion that continuously turns appointments (and the surrounding record) into plain-language understanding, across the whole serious-illness journey, condition-agnostic, in the fragmented multi-provider reality of the EU.**

Map of the field on two axes — *who is served* (clinician → patient → caregiver) and *what is delivered* (raw data/logistics → comprehension/synthesis):

- **High capability, wrong user:** AI scribes (Abridge, Nabla, Corti, Tortus, Dragon) have the richest signal (the conversation) but serve clinicians and emit clinic-bound by-products. **Nobody re-points that capability at the patient+caregiver as the primary product.**
- **Right user, shallow output:** EHR AVS and patient portals (MyChart) reach the patient but deliver templated/jargon, single-visit, provider-locked content — and actively *fragment* across providers (2025 MyChart litigation).
- **Right intent, condition-locked:** Patient companions (Outcomes4Me/Mika, Jasper, Belong, Vinehealth) are real and EU-active **but oncology-only** and focused on tracking/trials/coaching rather than appointment comprehension. No cross-condition companion exists.
- **Right relationship, no clinical brain:** Caregiver apps (CaringBridge, Lotsa) coordinate people but understand nothing medical. Birdie proves EU caregiver-software demand but sells to agencies, not families.
- **Substrate is arriving for free:** EU data access (NL MedMij/PGO by end-2025; DE ePA opt-out, ~70M enrolled) populates the record but **explicitly does not explain it** — creating the "I have my data, I still don't understand it" gap.

**What nobody owns (the specific unclaimed position):**
> **"The patient's (and family's) understanding of their own care, over time, across every provider."** A companion that: (1) captures/ingests each appointment and the patient's records (riding ePA/PGO/portal data), (2) translates into the patient's language and literacy level, (3) synthesizes longitudinally across visits and providers — not single-visit, (4) is built for the **caregiver as a co-user**, and (5) works for **any serious illness**, not just cancer, **in the EU's regulatory and multilingual environment**.

**Why this is credibly empty (evidence, not assertion):**
- Scribe leaders publicly frame themselves as clinician/health-system tools and are moving *upstream into coding/revenue*, not downstream to patients [Fierce/STAT, 2025]. **Confidence: High.**
- The only patient companions with EU traction are oncology and consolidating among themselves (Outcomes4Me acquiring Mika), leaving non-oncology serious illness uncovered. **Confidence: High.**
- The strongest documented patient pain — record fragmentation across providers during serious illness — is currently being *litigated against the incumbent (Epic MyChart)*, not solved by a product [Becker's/Nurse.org, 2025]. **Confidence: High.**

**Caveats / uncertain claims:**
- "Nobody owns it" is a **negative finding** from broad search, not exhaustive proof. Stealth/early-stage EU startups (especially DiGA-track German or NHS-track UK ventures) may be building toward this and not yet visible. **Confidence: Medium.**
- Several AI-explainer tools (BloodGPT, TestResult.ai, AIDiagme, Kantesti) are thinly documented (Tier 3) and their regulatory status (MDR/CE) is unclear — they could expand toward visit comprehension. **Confidence: Low** on their trajectory.
- Hedy AI / PatientNotes / Abridge's real-time patient summaries are the closest *features* to ditto.care's core and warrant ongoing monitoring as potential fast-followers. **Confidence: Medium.**
- Exact Jasper Health funding/status is dated (2022 figures); no confirmed 2025 raise found. **Confidence: Medium.**

---

## Sources

All accessed **2026-05-31**.

**AI scribes (Tier 1/2):**
- [TechCrunch, 2025 — Abridge $5.3B valuation](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/)
- [STAT, 2025 — Abridge $300M](https://www.statnews.com/2025/06/24/ai-clinical-documentation-ambient-scribe-abridge-raises-300-million/)
- [Sacra — Abridge revenue/funding](https://sacra.com/c/abridge/)
- [Microsoft Source, 2025 — Dragon Copilot launch](https://news.microsoft.com/source/2025/03/03/microsoft-dragon-copilot-provides-the-healthcare-industrys-first-unified-voice-ai-assistant-that-enables-clinicians-to-streamline-clinical-documentation-surface-information-and-automate-task/)
- [Microsoft for Healthcare — Dragon Copilot product](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot)
- [STAT, 2025 — Nabla $70M](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/)
- [PRNewswire, 2025 — Nabla $70M Series C, $120M total](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html)
- [EIFO / Corti $60M Series B](https://eifo.dk/en/knowledge/news/with-60m-series-b-corti-will-scale-ai-co-pilot-to-support-overburdened-healthcare-staff-globally/)
- [Corti — sovereign EU AI infrastructure](https://www.corti.ai/news/corti-pioneers-europes-first-sovereign-healthcare-ai-infrastructure)
- [Tortus.ai — product](https://tortus.ai/)
- [Digital Health, 2025 — NHS AI-scribe trial results](https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/)
- [GOSH — AI-scribe trial](https://www.gosh.nhs.uk/news/researchgosh-led-trial-of-ai-scribe-technology-shows-transformative-benefits-for-patients-and-clinicians-across-london/)
- [iatrox — UK scribe guide (Tortus/Accurx/Heidi), Tier 3](https://www.iatrox.com/blog/ai-medical-scribes-uk-gp-guide-tortus-accurx-heidi)

**Patient summaries / OpenNotes / AI explainers:**
- [OpenNotes.org — 7-year patient experience study](https://www.opennotes.org/research/opennotes-after-7-years-patient-experiences-with-ongoing-access-to-their-clinicians-outpatient-visit-notes/)
- [The Alliance — OpenNotes vs AVS explainer (Tier 3)](https://the-alliance.org/blog/opennotes-encourages-patients-access-doctors-notes-medical-record/)
- [Stanford Medicine, 2025 — AI results-explainer](https://med.stanford.edu/news/all-news/2025/01/ai-test-results.html)
- [BloodGPT (Tier 3)](https://bloodgpt.com/)
- [TestResult.ai — AI lab tools comparison (Tier 3)](https://testresult.ai/blog-best-ai-medical-tools.html)
- [PatientNotes — patient-facing AVS (Tier 3)](https://patientnotes.ai/resources/after-visit-summary-template)
- [Hedy AI — patient/caregiver AI tools (Tier 3)](https://www.hedy.ai/post/best-ai-patient-tools/)
- [Abridge — real-time patient visit summaries](https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time)

**Patient navigation / companions:**
- [PRNewswire, 2025 — Outcomes4Me $21M](https://www.prnewswire.com/news-releases/outcomes4me-secures-21m-in-funding-to-accelerate-ai-driven-innovation-and-drive-global-expansion-to-transform-cancer-care-302468806.html)
- [PRNewswire, 2025 — Outcomes4Me acquires Mika (Germany)](https://www.prnewswire.com/news-releases/outcomes4me-acquires-germanys-mika-health-app-to-accelerate-ai-driven-patient-empowerment-globally-302479404.html)
- [Mika Health — product](https://us.mika.health/)
- [Debiopharm — Mika investment / DiGA](https://www.debiopharm.com/innovation-fund/press-releases/debiopharm-leads-investment-round-for-evidence-based-digital-cancer-therapeutic-app-mika-to-empower-cancer-patients/)
- [Medica — DiGA explainer](https://www.medica-tradefair.com/en/media-news/spheres-of-medica-magazine/digital-health/diga-app-on-prescription)
- [Fierce Healthcare, 2022 — Jasper Health $25M](https://www.fiercehealthcare.com/digital-health/former-cvs-health-exec-gets-25m-cancer-care-navigation-platform-jasper-health)
- [Jasper Health — product](https://hellojasper.com/)
- [pharmaphorum — Vinehealth CE marks](https://pharmaphorum.com/news/vinehealth-earns-ce-marks-for-cancer-management-apps)
- [HTN, 2024 — Sciensus acquires Vinehealth](https://htn.co.uk/2024/01/23/sciensus-acquires-patient-app-and-physician-support-platform-vinehealth/)

**Caregiver coordination:**
- [Caring.com — best caregiving apps (CaringBridge, Lotsa) (Tier 3)](https://www.caring.com/resources/best-caregiving-apps)
- [Sifted, 2022 — Birdie $30M Series B](https://sifted.eu/articles/elderly-care-birdie-raise)
- [Birdie — product](https://www.birdie.care/)

**PHR / aggregation (EU):**
- [MedMij — HL7 Netherlands](https://confluence.hl7.org/display/HNETH/MedMij)
- [Ivido — NL PGO](https://ivido.nl/)
- [gematik — ePA für alle](https://fachportal.gematik.de/anwendungen/epa-fuer-alle)
- [Bundesgesundheitsministerium — ePA für alle](https://www.bundesgesundheitsministerium.de/epa-vorteile/)
- [MobiHealthNews — Apple Health Records international](https://www.mobihealthnews.com/news/apple-health-records-goes-international-rollouts-five-uk-canadian-providers)
- [Apple Support — Health Records sharing FAQ](https://support.apple.com/guide/healthregister/health-app-data-share-with-provider-faq-apd531bc6215/web)

**Second opinion:**
- [BMC Health Services Research, 2021 — German second-opinion programs / Medexo](https://bmchealthservres.biomedcentral.com/articles/10.1186/s12913-021-06207-8)
- [Erasmus MC — second opinion (NL)](https://www.erasmusmc.nl/en/patient-care/second-opinion)

**EHR portals / status quo:**
- [Becker's, 2025 — Epic MyChart fragmentation lawsuit](https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/epic-sued-over-claims-mychart-fragments-patient-medical-records/)
- [Nurse.org, 2025 — MyChart access lawsuit detail](https://nurse.org/news/epic-lawsuit-mychart-patient-record-access/)
- [JMIR, 2025 — patient portal implementation experiences](https://www.jmir.org/2025/1/e65967)
