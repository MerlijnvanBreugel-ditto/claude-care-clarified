# M4 — Competitor & Solution Landscape (Refreshed, June 2026)

**Prepared for:** ditto.care competitive intelligence (M4 market-research corpus)
**Scope:** Players adjacent to a patient-level AI companion that turns appointments and the surrounding record into plain-language understanding — clinician scribes, patient-facing summaries/explainers, disease companions, caregiver apps, PHR/aggregation, second-opinion, EHR portals, and the **2026 wave of Big Tech consumer health AI assistants**. Mapping who serves whom, EU presence, and what nobody yet solves.
**Method:** WebSearch + WebFetch. Access date for all URLs: **2026-06-10**. Refreshes the prior in-repo file `07-competitive-landscape.md` (access date 2025-05-31).
**Source tiers:** Tier 1 = company filings / funding databases / official product docs; Tier 2 = reputable tech/health press, peer-reviewed; Tier 3 = blogs / self-report (flagged). US→EU applicability flagged throughout.
**Out of scope (covered in sibling files):** the Kin deep-dive + head-to-head feature matrix; Flo/Calm-style consumer-health retention. Not duplicated here.

---

## Key takeaways

1. **The single biggest change since mid-2025 is Big Tech going direct-to-consumer on health AI — but only in the US.** In Jan–Mar 2026, OpenAI (ChatGPT Health), Anthropic (Claude for Healthcare), Amazon (One Medical Health AI), Google (Gemini Health Coach) and Microsoft (Copilot Health) all launched consumer-facing health assistants that ingest medical records and explain labs/diagnoses. **All are US-first; ChatGPT Health is explicitly unavailable in the EU/UK/Switzerland on GDPR + MDR grounds** [Euronews/heise, 2026]. This both validates ditto.care's thesis (the comprehension companion is now the contested frontier) and hands the EU a regulatory moat. **Confidence: High.**

2. **Clinician-facing scribes kept compounding and pulled even further ahead on capital.** Abridge raised a $300M Series E to a $5.3B valuation (Jun 2025) and reportedly added a ~$316M Series E extension in 2026 (total >$1.1B raised) [PitchBook/TechCrunch, 2025–26 — extension Tier 2/unconfirmed]. Nabla's founder co-founded a $1.03B "world models" lab (AMI Labs, with Yann LeCun), giving Nabla first access to frontier models [HIT Consultant, 2026]. The patient is still the data source, not the customer. **Confidence: High** (Abridge core round); **Medium** (2026 extension exact figure).

3. **Corti is the clearest "EU-sovereign" counter-positioning** and is explicitly framing 2026 around Europe: no Series C (still ~$94.5M raised), staying private, and launching a no-equity accelerator while publicly noting "OpenAI pushes into the space and others retreat from Europe" [PR Newswire/CNBC, 2026 — Tier 1/2]. Useful signal that EU healthcare-AI defensibility is now an explicit narrative. **Confidence: High.**

4. **Patient companions are still oncology-locked and largely unchanged.** Outcomes4Me (~280k patients) + acquired Mika/Fosanis (~100k, MDR IIa, German DiGA) closed the $21M round and EU expansion in mid-2025; no major 2026 reset found. Nothing cross-condition emerged. **Confidence: High.**

5. **The EU data substrate is maturing in ditto.care's favour, and the comprehension gap is now an explicit policy goal.** NL MedMij's updated roadmap targets PGOs that are "better-filled, more **understandable**, and more valuable" with new data types (pathology, screening) from 2026 [MedMij, 2026]. Germany's ePA is opt-out for all statutory insured, yet ~48% of Germans say digital health tools are "too complex" and active use lags awareness [medicalblogs/JLI, 2025–26]. Records are arriving; understanding is not. **Confidence: High.**

6. **The incumbent portal pain is now in active litigation, still unsolved.** The Epic MyChart fragmentation/antitrust suit (filed Mar 9, 2026, W.D. Texas) is at an early stage with no ruling; Epic denies it [Becker's/DistilINFO, 2026]. Epic's own patient chatbot "Ask Emmie" is EHR-bound and provider-gated [TechTarget, 2026]. The strongest documented patient pain is being argued in court, not fixed by a product. **Confidence: High.**

7. **Stress-tested whitespace holds, but it narrowed.** "A patient+caregiver, cross-condition, plain-language comprehension companion across the fragmented EU multi-provider reality" is still unowned — but the US consumer-AI wave proves the category is real and will arrive in the EU eventually. ditto.care's durable edges are **EU regulatory-native build, the caregiver as a first-class co-user, and longitudinal cross-provider synthesis** — not "AI that explains a lab," which is now commoditizing. **Confidence: Medium-High.**

---

## 1. AI medical scribes / visit documentation (clinician-facing)

Still the best-capitalized category by an order of magnitude. **Sold to clinicians/health systems**; patient is the data source. Where they emit a "patient summary" it is a clinic-bound, single-visit by-product.

| Player | Facing | EU presence | Funding / traction (2026) | What they do NOT solve |
|---|---|---|---|---|
| **Abridge** (US) | Clinician / health system | US-centric; deep Epic | $300M Series E, **$5.3B valuation** (Jun 2025); ~$100M ARR (May 2025), $117M contracted ARR; **reported ~$316M Series E extension in 2026, total >$1.1B raised** [TechCrunch 2025; PitchBook 2026 — extension Tier 2/unconfirmed]; 250+ health systems (Mayo, Duke, JHU, Kaiser) | No patient-owned longitudinal record; tied to one system's Epic; not a caregiver product |
| **Nabla** (FR/US) | Clinician | Paris-founded; Highland Europe backer; 35+ languages | $70M Series C, **$120M total** (Jun 2025); 85k clinicians, 130+ orgs. **Founder co-founded AMI Labs — $1.03B seed, $3.5B pre-money (Yann LeCun); Nabla has exclusive first-access to AMI "world models"** [HIT Consultant/Nabla, 2026 — Tier 1/2] | Documentation → agentic CDI/EHR actions; patient never the user; no caregiver layer |
| **Microsoft Dragon Copilot (Nuance DAX)** | Clinician | Live UK/IE; rolling AT/FR/DE, BE/NL | Microsoft-owned (Nuance ~$19.7B, 2022) | AVS is a clinician one-click output; provider/EHR-bound; English-first |
| **Corti** (DK) | Clinician / health-AI infra | **Copenhagen; EU "sovereign" cloud; explicitly EU-defensive narrative** | **~$94.5M total; no Series C** (deliberately private); launched **no-equity startup accelerator (May 2026)**; "others retreat from Europe" framing [PR Newswire/CNBC, 2026 — Tier 1/2] | Clinician co-pilot + coding/QA + now a platform/infra play; patient comprehension out of scope |
| **Tortus** (UK) | Clinician (NHS) | UK/NHS-native, DTAC | NHS Innovation Accelerator; rollout to 3,500+ GP practices via X-on | Note-drafting for clinicians; no patient/caregiver deliverable |
| **Heidi, Suki, Ambience, Accurx Scribe** | Clinician | Heidi/Accurx UK-active; others US | Various (Tier 2/3) | Same pattern — clinician productivity, not patient understanding |

**Category gap (High):** Scribes capture the richest raw material (the actual conversation) but discard the patient as a user; output lives in the EHR + billing pipeline. The 2026 twist: scribe leaders are moving *upmarket* (Abridge into revenue cycle/coding, Nabla into agentic CDI and frontier "world models"), not downstream to patients. The portable, cross-provider, patient-owned plain-language layer remains structurally vacant.

---

## 2. NEW IN 2026 — Big Tech consumer health AI assistants (patient-facing)

The defining shift of the last six months. Five US giants launched consumer-facing health AIs that **ingest medical records, explain labs/diagnoses, and answer health questions** — the closest thing yet to a "comprehension companion." Crucially, **all are US-first and the leading one is GDPR/MDR-blocked from the EU.**

| Player | Launch | What it does | EU availability | Gap / read-through for ditto.care |
|---|---|---|---|---|
| **OpenAI — ChatGPT Health** | Jan 7, 2026 | Hub to upload medical records; aggregates records + wearables; positions as personal "health concierge" [OpenAI; National Law Review, 2026] | **NOT available in EU/UK/Switzerland** — GDPR special-category data + possible MDR classification cited [Euronews/heise, 2026] | General-purpose; not condition-aware, not caregiver-modelled, not EU-legal; no appointment-capture loop |
| **Anthropic — Claude for Healthcare** | Jan 11, 2026 | Health-record access + medical databases/coding; HIPAA-ready; **enterprise/clinical workbench tilt** (prior auth, life sciences) more than consumer concierge [Fierce/TechCrunch, 2026] | US-first; EU consumer posture unclear | Skews B2B/health-system; not a daily patient+caregiver companion |
| **Amazon — One Medical Health AI** | Jan 2026 (app); Mar 2026 (web, 200M Prime) | Agentic: explains labs/diagnoses/records, books appts, manages meds, 24/7 guidance via Bedrock LLMs [Amazon/CNBC/Fierce, 2026] | US-only (One Medical footprint) | Tied to Amazon's own care delivery; US insurance/care model; no caregiver layer |
| **Google — Gemini Health Coach** | May 19, 2026 ($9.99/mo, Google Health Premium) | Summarizes shared US medical records + Fitbit/Pixel + nutrition/sleep; chatbot over fitness + medical data [TechCrunch/eMarketer, 2026] | US medical-records integration; wellness-led | Wellness/coaching-led, not serious-illness comprehension; US records only |
| **Microsoft — Copilot Health** | Mar 2026 | Reviews records, preps for appointments, personalized insights over records + wearables [Fierce, 2026] | US-first; note separate Copilot EU data-routing controversy (Apr 2026) raising GDPR flags | Generalist; appointment-prep feature, not capture/longitudinal synthesis |

**Category gap & strategic read (High):** This wave is the loudest validation yet that "turn my records into understanding" is a real, contested consumer category — and the loudest reminder of ditto.care's moat. A peer-reviewed JMIR 2026 analysis of consumer-facing health AI assistants flags misdiagnosis, overreliance and "hypochondria spiral" risks and notes LLMs often fail to redirect problematic questions [JMIR, 2026 — Tier 1/2; fetch blocked, summary via search]. None of these are EU-legal at consumer scale today, none model the **caregiver**, none are **condition-aware for serious illness**, and none own the **appointment-capture → translate → longitudinal-synthesis** loop. They are generalist concierges riding US health-information-exchange plumbing that does not exist for consumers in the EU.

---

## 3. Patient-facing visit summaries / "explain my results"

Three sub-types, all still partial — now being commoditized from above by the Big Tech wave (Section 2).

**(a) EHR after-visit summaries (AVS).** Templated (weight, BP, meds, instructions), auto-generated for compliance; shallow, single-visit, provider-locked. **(b) OpenNotes.** Raw clinician note access (184+ US systems; 98% call it a good idea) — accurate but written *for clinicians*. **(c) AI explainers.** Lab/results translators (BloodGPT, TestResult.ai, AIDiagme, Kantesti), plus **Epic's "Ask Emmie"** — a HIPAA-compliant, EHR-backed patient chatbot, but provider-gated and bound to the Epic record [TechTarget, 2026]. PatientNotes (clinician-sold patient AVS) and Hedy AI (patient/caregiver appointment recording) persist.

| Player | Facing | Scope | EU | Gap |
|---|---|---|---|---|
| EHR AVS (Epic/MEDITECH/Cerner) | Patient (compliance) | Single visit | EU portals patchy | No synthesis, no translation, provider-locked |
| OpenNotes | Patient | Raw clinician note | Mostly US; some Nordic | Written for clinicians; not translated/synthesized |
| **Epic Ask Emmie** (US) | Patient | EHR-backed Q&A | US (Epic systems) | Provider-gated, single-EHR; not cross-provider, not caregiver |
| BloodGPT / TestResult.ai / AIDiagme / Kantesti | Patient (self-serve) | Lab results only | Mixed/multilingual | Results-only; no visit context; MDR/CE status unclear (Tier 3) |
| PatientNotes / Hedy AI | Clinician-sold AVS / patient capture | Per-visit | UK-ish / app stores | Per-visit, clinic-bound / generic capture, not condition-aware |

**Category gap (High):** Everything here is single-visit, single-modality (labs), or untranslated. The Big Tech assistants (Section 2) now subsume the "explain my lab" job in the US — meaning standalone lab-explainers are the most exposed to commoditization. No product owns the full loop end-to-end in the EU.

---

## 4. Patient navigation / care companions (serious illness)

Real funding, **almost entirely oncology**, US payer/employer channel — unchanged in 2026.

| Player | Facing | Condition | EU | Funding / traction | Gap |
|---|---|---|---|---|---|
| **Outcomes4Me** (US) | Patient (+caregiver) | Cancer | Expanding via Mika acquisition (Jun 2025) | $21M round (May 2025); ~280k patients [Outcomes4Me/PRNewswire, 2025] | Cancer-only; guideline/trial-matching, not appointment comprehension |
| **Mika / Fosanis** (DE) | Patient | Cancer | German **DiGA**-prescribable; MDR IIa; ~100k patients | Acquired by Outcomes4Me (Jun 2025) | Cancer-only ePRO + psycho-oncology; not cross-condition |
| **Jasper Health** (US) | Patient + caregiver | Cancer | US | ~$31M total; $25M Series A (2022); no confirmed 2025–26 raise | Cancer-only; US payer/Medicare |
| **Belong.Life** (IL/US) | Patient | Cancer (+expanding) | Limited EU | Private | Community + navigation; not appointment-level |
| **Vinehealth** (UK) | Patient | Cancer | UK/EU CE Class I; acquired by Sciensus (2024) | Innovate UK grant | Self-management absorbed into pharma services |

**Category gap (High):** Closest analog to ditto.care's companion posture, but **condition-locked (oncology)** and focused on tracking/trials/coaching, not on making each appointment understood. A heart-failure, neuro, rare-disease or multimorbid/frail patient still has no equivalent. The German DiGA + French PECAN + Nordic reimbursement paths remain the obvious EU monetization rails (64 DiGA apps, >€125M reimbursable revenue in 2025 [Mordor/QuickBird, 2025–26]).

---

## 5. Caregiver coordination apps

| Player | Facing | EU | What it is | Gap |
|---|---|---|---|---|
| **CaringBridge** (US) | Caregiver/family | Global web | Updates feed, support community | No clinical comprehension; a journal/feed |
| **Lotsa Helping Hands** (US) | Caregiver/family | Global web | Help calendar, task coordination | Pure logistics; zero medical content |
| **Birdie** (UK/EU) | **Care agency (B2B)** | UK + Spain, expanding FR/DE/Nordics | Homecare agency SaaS; ~$52M raised | **Not family-facing** — agency software |
| Carely, Caringly, etc. | Family | Mostly US | Family update/coordination | No appointment comprehension |

**Category gap (High):** Caregiver tools are a social/logistics layer with no clinical brain — they tell the family *that* there was an appointment, not *what it meant*. Notably, **not one** of the 2026 Big Tech consumer health assistants (Section 2) models the caregiver as a first-class user either. The caregiver-as-co-user remains ditto.care's least-contested wedge. **Confidence: High.**

---

## 6. Personal health records / aggregation (EU emphasis) — the substrate

Still being solved at the infrastructure/government layer: data plumbing, not comprehension. A tailwind, not a competitor.

| Player | Facing | EU | Status (2026) | Gap |
|---|---|---|---|---|
| **NL MedMij / PGO** (Ivido, Quli, etc.) | Patient | Netherlands | Updated roadmap explicitly targets **"better-filled, more understandable, more valuable"** PGOs; new MedMij Register, granular-data test phase, new data types (pathology, screening, LTC) from 2026 [MedMij, 2026]; VWS pushing more data / fewer suppliers [DutchHealthHub, 2026] | Aggregates + (aspirationally) clarifies, but does not synthesize or translate per-patient; adoption still building |
| **DE ePA "für alle"** (gematik) | Patient | Germany | Opt-out for all statutory insured; mandatory for providers since Oct 2025; **but ~48% of Germans find digital health tools "too complex," active use lags awareness** [medicalblogs/JLI, 2025–26] | Document vault, not a companion; the complexity gap is the comprehension opportunity |
| **Apple Health Records** | Patient | UK + Canada providers; EU limited | FHIR/SMART aggregation; provider-sharing largely US | Aggregation, not comprehension; thin EU coverage |
| **Google / consumer PHRs** | Patient | Global | Now feeding Gemini Health Coach (US records) | No durable EU comprehension layer |

**Category gap (High):** The EU is rapidly giving patients *access to their data* and the NL roadmap now explicitly names "understandable" as a goal — confirming, from the inside, that today's PGOs are *not* understandable. This creates the "I have my records but don't understand them" gap a comprehension companion rides. **The substrate (ePA, PGO) is arriving for free; the understanding layer is not built into it.** **Confidence: High.**

---

## 7. Second-opinion, decision-support & EHR portals (status quo)

| Player | Facing | EU | Role | Gap |
|---|---|---|---|---|
| **Teladoc / 2nd.MD, Included Health** | Patient (employer/payer) | Mostly US | Expert second opinions | Episodic, decision-point only; not a daily companion |
| **Medexo** (DE) | Patient | Germany | Records-based written second opinion | One-off; no ongoing understanding |
| **Epic MyChart** | Patient | US-dominant; some EU hospitals | Default portal: messaging, AVS, results, OpenNotes, now **Ask Emmie** chatbot | **Fragmentation across orgs** — central allegation of the Mar 2026 antitrust/disability suit (W.D. Texas, no ruling yet; Epic denies) [Becker's/DistilINFO, 2026]; accessibility barriers for elderly/low-literacy/non-native speakers |
| **EU hospital portals** (Chipsoft/HiX NL, DE) | Patient | EU | Per-hospital portals | More fragmented than US; per-hospital silos, no cross-provider synthesis, no caregiver model |

**Category gap (High):** Portals are provider-centric and silo'd by institution — exactly broken for the multi-provider patients who need them most. The strongest documented patient pain (cross-provider record fragmentation) is being *litigated against Epic*, not solved by a product, and Epic's own AI answer (Ask Emmie) is still single-EHR and provider-gated.

---

## Landscape map — who-serves-whom × what-they-deliver

Two axes: **who is served** (clinician / patient / caregiver) × **what is delivered** (raw data & logistics → comprehension & companion).

| | **Raw data / logistics** | **Comprehension / companion** |
|---|---|---|
| **Clinician** | EHR documentation, RCM/coding | **AI scribes: Abridge, Nabla, Corti, Tortus, Dragon, Heidi/Suki/Ambience** — richest signal, wrong user; emit clinic-bound by-products |
| **Patient** | EHR AVS; **PHR/aggregation: NL PGO, DE ePA, Apple Health**; lab-explainers (BloodGPT etc.) | **Big Tech consumer AI: ChatGPT Health, Claude, Amazon One Medical, Gemini Coach, Copilot Health** (US-only, GDPR/MDR-blocked from EU); **Epic Ask Emmie** (single-EHR); **oncology companions: Outcomes4Me/Mika, Jasper, Belong, Vinehealth** (condition-locked) |
| **Caregiver** | **CaringBridge, Lotsa** (logistics); **Birdie** (B2B agency SaaS) | **— essentially empty —** no product delivers appointment-level medical comprehension to the family as a first-class user |
| **Patient + caregiver, cross-condition, EU-legal, longitudinal** | — | **ditto.care's target cell — unowned** |

**Reading the map:** Capability concentrates top-right (scribes) and a new patient-comprehension cluster appeared mid-right in 2026 (Big Tech) — but **the entire bottom-right cell (caregiver comprehension) is empty**, and **no occupant of the patient-comprehension cluster is simultaneously EU-legal, caregiver-modelled, condition-agnostic for serious illness, and built on the appointment-capture loop.**

---

## Whitespace — re-stated and stress-tested against 2026 reality

**The position (unchanged target):**
> "The patient's *and family's* understanding of their own care, over time, across every provider" — a companion that (1) captures/ingests each appointment and the record (riding ePA/PGO/portal data), (2) translates to the patient's language + literacy level, (3) synthesizes **longitudinally across visits and providers**, (4) treats the **caregiver as a co-user**, (5) works for **any serious illness**, (6) in the **EU's regulatory + multilingual** environment.

**What changed in 2026 — and what it means for the whitespace:**

- **Validation, not invalidation, of the category.** Five US giants launching record-ingesting comprehension assistants in one quarter is the strongest possible proof the job-to-be-done is real and valuable. The risk is no longer "is there a market" but "incumbents arriving." **Confidence: High.**
- **The EU moat got more concrete.** ChatGPT Health is *explicitly* unavailable in EU/UK/Switzerland on GDPR special-category-data + MDR grounds [Euronews/heise, 2026]; Corti is openly building an "EU-sovereign / others retreat from Europe" narrative [PR Newswire, 2026]. An **EU-native, GDPR/MDR-built** patient companion is defensible *because* the US generalists cannot trivially cross the border. **Confidence: High.**
- **The substrate now names "understanding" as a gap.** NL MedMij's own 2026 roadmap commits to making PGOs "more understandable" — an admission they aren't — and German ePA's complexity problem (~48% find tools too complex) is the comprehension wedge. **Confidence: High.**
- **The differentiators that survive commoditization.** "AI explains a lab/diagnosis" is now commoditizing (Big Tech + lab-explainers). What does **not** commoditize quickly: caregiver-as-co-user (empty cell), cross-provider longitudinal synthesis in the EU's multi-portal reality, condition-agnostic serious-illness coverage, and EU regulatory-native trust. ditto.care should anchor on these, not on the explainer feature. **Confidence: Medium-High.**

**Where the whitespace narrowed (honest caveats):**

- **Time-bound EU moat.** The GDPR/MDR barrier is real today but not permanent — OpenAI/Google/Microsoft will localize eventually (Microsoft already routes some Copilot EU data, contentiously). The window to build EU trust + data integrations is open *now*, perhaps 18–36 months. **Confidence: Medium.**
- **Big Tech bundling risk.** If Apple/Google bundle a serious-illness-grade companion into the OS/health app with caregiver sharing, the standalone thesis weakens. No evidence of caregiver-first serious-illness intent yet, but monitor. **Confidence: Medium.**
- **"Nobody owns it" is a negative finding.** Broad search, not exhaustive proof; stealth EU DiGA/NHS-track ventures may be building toward this invisibly. **Confidence: Medium.**
- **Closest fast-followers to watch:** Epic Ask Emmie (if it goes cross-provider + caregiver), Amazon One Medical (if it enters EU via acquisition), and any oncology companion (Outcomes4Me/Mika) expanding cross-condition off its MDR/DiGA base. **Confidence: Medium.**

**Net:** The specific cell ditto.care targets — **patient + caregiver, cross-condition, longitudinal, appointment-anchored, EU-legal comprehension** — remains unowned in June 2026. The 2026 Big Tech wave validates demand and raises the urgency, while GDPR/MDR and the empty caregiver cell preserve a defensible, time-bound opening.

---

## Sources

All accessed **2026-06-10**.

**Tier 1 — official / filings / funding DBs / product docs:**
- [OpenAI — Introducing ChatGPT Health](https://openai.com/index/introducing-chatgpt-health/)
- [Amazon — One Medical agentic Health AI](https://www.aboutamazon.com/news/retail/one-medical-ai-health-assistant)
- [Amazon — expanding Health AI to more US customers](https://www.aboutamazon.com/news/retail/amazon-health-ai-agent-one-medical)
- [UnitedHealth Group — AI companion "Avery"](https://www.unitedhealthgroup.com/newsroom/2026/2026-03-26-uhc-introduces-ai-companion-empowering-people-with-simpler-navigation-personal-experience.html)
- [Corti — $60M Series B / EU sovereign infra](https://www.corti.ai/stories/corti-raises-60m-in-series-b-funding-to-accelerate-healthcare-ai-innovation-and-expand-work-in-public-safety)
- [PR Newswire — Corti accelerator / "others retreat from Europe" (2026)](https://www.prnewswire.com/news-releases/corti-steps-up-its-support-for-the-next-wave-of-healthcare-startups-as-openai-pushes-into-the-space-and-others-retreat-from-europe-302771088.html)
- [PR Newswire — Nabla $70M Series C, $120M total](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html)
- [Outcomes4Me — $21M round](https://outcomes4me.com/press-release/outcomes4me-secures-21m-in-funding-to-accelerate-ai-driven-innovation-and-drive-global-expansion-to-transform-cancer-care/)
- [Outcomes4Me — acquires Mika (Germany)](https://outcomes4me.com/press-release/outcomes4me-acquires-germanys-mika-health-app-to-accelerate-ai-driven-patient-empowerment-globally/)
- [MedMij — updated roadmap toward better-filled/understandable PGOs (2026)](https://www.icthealth.nl/nieuws/geactualiseerde-medmij-roadmap-voor-beter-gevulde-pgos)
- [MedMij — informatiestandaarden / Wegiz](https://medmij.nl/informatiestandaarden/)
- [PitchBook — Abridge 2026 profile](https://pitchbook.com/profiles/company/268134-40)

**Tier 2 — reputable press / analyst / peer-reviewed:**
- [TechCrunch, 2025 — Abridge $5.3B](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/)
- [HIT Consultant, 2026 — Nabla / AMI Labs $1.03B world models](https://hitconsultant.net/2026/03/10/nabla-ami-labs-world-models-agentic-ai-healthcare/)
- [CNBC, 2025 — Corti will IPO but not in 2026](https://www.cnbc.com/2025/12/30/corti-will-go-public-but-not-in-2026-says-ai-healthcare-startups-ceo.html)
- [Tech.eu, 2026 — Corti no-equity accelerator](https://tech.eu/2026/05/13/corti-launches-no-equity-accelerator-for-healthcare-ai-startups/)
- [Euronews, 2026 — ChatGPT Health launch + records](https://www.euronews.com/next/2026/01/08/open-ai-launches-dedicated-chatgpt-health-feature-with-medical-record-integrations)
- [heise online, 2026 — ChatGPT Health not available in EU/CH/UK (GDPR/MDR)](https://www.heise.de/en/news/ChatGPT-Health-OpenAI-launches-AI-health-assistant-11134998.html)
- [TechCrunch, 2026 — Anthropic Claude for Healthcare](https://techcrunch.com/2026/01/12/anthropic-announces-claude-for-healthcare-following-openais-chatgpt-health-reveal/)
- [Fierce Healthcare, 2026 — JPM26 Claude for Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/jpm26-anthropic-launches-claude-healthcare-targeting-health-systems-payers)
- [National Law Review, 2026 — ChatGPT Health & Claude go direct to consumers](https://natlawreview.com/article/health-care-without-hospital-chatgpt-health-and-claude-go-direct-consumers)
- [Fierce Healthcare, 2026 — Microsoft Copilot Health for consumers](https://www.fiercehealthcare.com/ai-and-machine-learning/microsoft-unveils-copilot-health-ai-health-companion-consumers)
- [TechCrunch, 2026 — Amazon health AI on web/app](https://techcrunch.com/2026/03/10/amazon-launches-its-healthcare-ai-assistant-on-its-website-and-app/)
- [CNBC, 2026 — Amazon AI for One Medical members](https://www.cnbc.com/2026/01/21/amazon-ai-health-care-one-medical-members.html)
- [TechCrunch, 2026 — Google $9.99 AI Health Coach (May 19)](https://techcrunch.com/2026/05/07/googles-9-99-per-month-ai-health-coach-launches-may-19/)
- [eMarketer, 2026 — Gemini AI coach in revamped health app](https://www.emarketer.com/content/google-injects-gemini-ai-coach-revamped-health-app)
- [JMIR, 2026 — Big Tech & consumer-facing health AI assistants (peer-reviewed)](https://www.jmir.org/2026/1/e99230)
- [TechTarget, 2026 — Epic's Ask Emmie EHR-backed patient chatbot](https://www.techtarget.com/patientengagement/feature/Epics-Ask-Emmie-offers-EHR-backed-AI-chatbot-option-for-patients)
- [Becker's, 2026 — Epic sued over MyChart fragmentation](https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/epic-sued-over-claims-mychart-fragments-patient-medical-records/)
- [DistilINFO, 2026 — Epic MyChart records lawsuit (filing detail)](https://distilinfo.com/2026/03/11/epic-mychart-patient-records-lawsuit/)
- [EU-Startups, 2026 — Oska Health €11M chronic-care app](https://www.eu-startups.com/2026/02/with-half-of-chronically-ill-patients-failing-to-take-medication-correctly-oska-health-secures-e11-million-for-personal-health-app/)
- [Mordor Intelligence — Europe digital health market (DiGA share / revenue)](https://www.mordorintelligence.com/industry-reports/europe-digital-health-market)
- [DutchHealthHub, 2026 — VWS pushes more PGO data, fewer suppliers](https://www.dutchhealthhub.nl/artikelen/vws-pakt-door-op-pgo-meer-data-minder-leveranciers)
- [Joep Lange Institute — Germany ePA quiet launch to mass adoption](https://www.joeplangeinstitute.org/data_and_health/electronic-patient-record-germany/)

**Tier 3 — blogs / self-report (FLAGGED — directional only):**
- [medicalblogs.de — ePA für alle 2026 changes / complexity sentiment](https://www.medicalblogs.de/elektronische-patientenakte-deutschland-7)
- [QuickBird Medical — DiGA development & approval 2026](https://quickbirdmedical.com/en/diga-development-approval/)
- [Hedy AI — best AI patient tools 2026 (lab-explainer landscape)](https://www.hedy.ai/post/best-ai-patient-tools/)
- [Sacra — Abridge revenue/funding profile](https://sacra.com/c/abridge/)
- [The Wellness London — ChatGPT Health not available in UK](https://www.thewellnesslondon.com/ai-doctor/blog/chatgpt-health-isn-t-available-in-the-uk-here-s-what-works-instead)
- [camocopy — Microsoft Copilot EU data routing controversy](https://www.camocopy.com/blog/microsoft-copilot-data-eu/)
