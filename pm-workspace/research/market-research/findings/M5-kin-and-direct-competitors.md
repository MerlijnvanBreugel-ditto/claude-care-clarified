# M5 — Deep Dive: Kin and ditto's Closest Direct Competitors

**Prepared for:** ditto.care (EU / Netherlands) — AI patient-facing summaries of healthcare appointments, building toward a daily "Living Health Companion."
**Analyst:** Competitive intelligence
**Access date:** 2026-06-10
**Scope:** Anchor deep-dive on **Kin Health**; head-to-head Kin vs ditto feature matrix; 3–6 closest direct competitors.

**Sourcing conventions.** Inline citations are `[Source, year](url)`. **Tier 1** = official/filings/company site; **Tier 2** = reputable press; **Tier 3** = app-store/blog/self-report — flagged inline as `[T3]`. Confidence tags: **(High)**, **(Med)**, **(Low)**. Note: several primary sources (TechCrunch, HIT Consultant, BusinessWire/Morningstar, app-store listings) returned HTTP 403 to direct fetch in this environment; their content is captured here via search-engine extracts and is flagged **(via search extract)** where it could not be confirmed against the live page. Treat those as Tier 2 with reduced confidence.

---

## Key takeaways

- **Kin Health is ditto's single closest competitor and a near-mirror of ditto's wedge.** It records doctor visits (in-person or telehealth), produces plain-English summaries with action items, and lets patients share with a "care circle" of family/caregivers — exactly ditto's "understand my care + share with loved ones" position. It raised a **$9M seed led by Maveron in May 2026** [TechCrunch, 2026](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/). **(High)**
- **Kin is US-anchored, free-forever, and monetizes via referrals** (to specialists/labs), not subscriptions — a fundamentally different revenue model than a likely EU SaaS/B2B2C play [search extract of TechCrunch/HIT Consultant, 2026](https://hitconsultant.net/2026/05/21/kin-health-raises-9m-seed-patient-ambient-ai/). This referral model is hard to replicate in the EU and raises GDPR/data-use questions ditto can position against. **(Med)**
- **Kin's explicit roadmap is ditto's stated roadmap**: a "health graph" aggregating data from multiple sources (incl. physician EHR notes "this year"), evolving from a notetaker into a longitudinal companion [search extract, 2026](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/). The two companies are converging on the same destination from the same starting point.
- **ditto's clearest differentiators are geography and trust**: EU/Netherlands data residency, GDPR-native design, EU AI Act/MDR posture, and multi-language by necessity. Kin is **not HIPAA-certified** (patient-facing, so outside HIPAA scope) and has documented privacy questions around third-party API processing of audio/transcripts [search extract, 2026](https://www.newsbytesapp.com/news/business/kin-health-raises-9-million-to-transcribe-and-summarize-doctor-visits/tldr). **(Med)**
- **A cluster of near-identical patient-side notetakers exists**: **Patiently** ("Medical Memory," family sharing, free-in-beta) and **Hedy AI** (real-time jargon translation + 30+ languages, $9.99/mo) are the next-closest. The category is crowding fast. **(High)**
- **Clinician-side incumbents leak into ditto's space**: **Abridge** already generates real-time **patient** visit summaries at 8th-grade reading level inside health systems — a distribution advantage ditto/Kin cannot match, but it is provider-owned, not patient-owned. **(High)**
- **Big-Tech adjacency is the macro threat**: ChatGPT Health, Perplexity Health, Claude for Healthcare, Copilot Health and Amazon Health all launched Jan–Mar 2026, connecting EHRs + wearables for personalized health Q&A [IAPP, 2026](https://iapp.org/news/a/the-health-ai-agent-rush-five-products-in-three-months-and-the-privacy-questions-that-got-left-behind). These don't yet own the appointment-capture moment, but they own the "ask questions about my health" layer ditto is building toward.

---

## 1. Kin (anchor) — disambiguation and deep dive

### 1.1 Which "Kin" — disambiguation (critical)

There are at least three distinct products named "Kin." The one analyzed here is the **patient health companion**:

- **✅ ANALYZED — Kin Health** (a.k.a. "Kin — Record Doctor Visits"). Web: **[meetkin.com](https://www.meetkin.com/)** and **[kinhealth.app](https://kinhealth.app/)**; iOS: [apps.apple.com/us/app/kin-health/id6756894542](https://apps.apple.com/us/app/kin-health/id6756894542); Android package `com.meetkin.android`. This is the patient-facing visit recorder / care-circle app. **This is ditto's direct competitor.**
- **❌ NOT this — "Kin: Personal AI Advisors"** (mykin.ai, Android package `ai.mykin.app`, iOS id6473448146) — a general-purpose personal AI companion for life/relationships/journaling, *not* a health record [Google Play, 2025 [T3]](https://play.google.com/store/apps/details?id=ai.mykin.app&hl=en). Despite "appointment/meeting prep" language, it is **not** healthcare-specific. Do not conflate.
- **❌ NOT this — "Kin Wellness & Support"** (iOS id6747573503) — a separate wellness app, unrelated [Apple App Store [T3]](https://apps.apple.com/us/app/kin-wellness-support/id6747573503).
- Note also a separate **"KinHealth – Your Family Health History, Organized"** ([kinhealthapp.com](https://www.kinhealthapp.com/)), which appears to be a family-health-history organizer and is a *different* company from meetkin.com. Low confidence on its current status; not the funded startup. **(Low)**

Everything in §1.2–§1.8 refers to **Kin Health / meetkin.com** unless stated.

### 1.2 What it does & target user

Kin is a patient's "personal health assistant" that **records any healthcare visit — in person or telehealth — and turns the conversation into a clear summary, plain-English explanations of what the doctor said, and a concrete list of next steps** [meetkin.com, 2026 [T3], via search extract](https://www.meetkin.com/). The framing in coverage: it helps "bewildered patients, and in many cases their overwhelmed relatives or caregivers, fully remember and understand their conversations with doctors and specialists" [search extract of LA Business Journal, 2026](https://labusinessjournal.com/healthcare/kin-health-raises-9-million-in-seed-funding/).

**Target user:** patients (especially those with complex/chronic care or many specialists) and their family caregivers — the same dual user (patient + loved one) ditto targets. **(High)**

### 1.3 Features & AI capabilities

- **One-tap recording** — starts in seconds, in-person or telehealth [meetkin.com [T3]](https://www.meetkin.com/). **(Med)**
- **Plain-English explanations** of medical jargon for patient + family. **(High)**
- **Action-item lists** — prescriptions to fill, specialists to see, labs to book, follow-ups to schedule. **(High)**
- **Appointment prep** — helps users organize questions and an agenda before a visit [search extract, 2026](https://www.meetkin.com/). **(Med)**
- **Longitudinal record** — assembles a record "grounded in actual physician conversations" over time, organized for re-use. **(Med)**
- **AI pipeline (notable):** Kin transcribes the visit → an algorithm converts the transcript into a **clinical narrative** → that is "crunched" into a user-facing summary with action items. The company says it uses **specialized medical models** for transcription and **evaluates/observes outputs at multiple stages** for accuracy [search extract of TechCrunch, 2026](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/). **(Med)**

### 1.4 Caregiver / family features

Kin's "care circle" is a first-class feature: **invite family members or caregivers to access visit summaries**, with role-based access — **Manager** access (can help manage care) vs **Viewer** access (stays informed only) [search extract, 2026](https://hitconsultant.net/2026/05/21/kin-health-raises-9m-seed-patient-ambient-ai/). This role split is more developed than most competitors and is a direct analogue to ditto's "share with loved ones." **(Med)**

### 1.5 Business model / pricing

- **Free forever for consumers.** Kin states it will keep the app permanently free [search extract, 2026](https://hitconsultant.net/2026/05/21/kin-health-raises-9m-seed-patient-ambient-ai/). **(Med)**
- **Monetization via referrals** to services such as specialists and labs [search extract of TechCrunch, 2026](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/). **(Med)** — *Strategic note:* a referral-fee model on patient health data would face stiff EU GDPR / anti-kickback / advertising-of-health-services scrutiny and is unlikely to transplant cleanly to the Netherlands. This is a structural vulnerability ditto can exploit on trust.

### 1.6 Geography

US-anchored (Los Angeles / Seattle investor base; US App Store and Play Store launch; coverage in US outlets). **No evidence of EU launch, EU data residency, or non-English support** as of access date — a gap ditto owns by construction. **(Med)**

### 1.7 Funding / team / traction

- **$9M seed, May 2026, led by Maveron (Seattle).** Participants: Town Hall Ventures, Flex Capital, Eniac Ventures, the Family Fund, Pear VC, Watershed Ventures, Foundry Square Capital, plus angels [search extract of LA Business Journal, 2026](https://labusinessjournal.com/healthcare/kin-health-raises-9-million-in-seed-funding/); [BusinessWire/Morningstar, 2026](https://www.morningstar.com/news/business-wire/20260518890468/kin-health-raises-9m-to-give-patients-a-record-of-their-own-care). **(High on amount/lead; Med on full investor list)**
- **Founders:** Arpan Parikh (physician, CEO), Kyle Alwyn (co-founded telemedicine startup **HeyDoctor**, sold to GoodRx in 2019), and Amit Parikh [search extract of LA Business Journal, 2026](https://labusinessjournal.com/healthcare/kin-health-raises-9-million-in-seed-funding/). Strong consumer-health/exit pedigree. **(Med)**
- **Traction:** Specific install counts, MAU, and app-store ratings were **not confirmable** — app-store and press pages returned 403 in this environment and search extracts did not surface numbers. The app launched on both stores in 2026; treat traction as **early/unconfirmed**. **(Low)**

### 1.8 Positioning & privacy posture

Kin positions as "**a record of your own care**" — patient ownership vs. provider-owned notes [BusinessWire, 2026](https://www.businesswire.com/news/home/20260518890468/en/Kin-Health-Raises-$9M-To-Give-Patients-a-Record-of-Their-Own-Care). It says it encrypts patient data (enterprise-grade) and keeps summaries private by default; it is **not HIPAA-certified** (patient-facing tools fall outside HIPAA's scope), though it claims equivalent practices [search extract, 2026](https://www.newsbytesapp.com/news/business/kin-health-raises-9-million-to-transcribe-and-summarize-doctor-visits/tldr). **Documented privacy concerns:** audio/transcripts of private appointments may be processed by third-party API providers, with open questions on data deletion after transcription, retention windows, and rights claimed over deidentified/aggregated data [search extract, 2026](https://www.newsbytesapp.com/news/business/kin-health-raises-9-million-to-transcribe-and-summarize-doctor-visits/tldr). **(Med)** — These are precisely the weaknesses an EU/GDPR-native player can turn into a differentiator.

---

## 2. Head-to-head feature matrix — Kin vs ditto

Legend: ✅ yes / present · ⚠️ partial or planned/roadmap · ❌ no / not evident · ❓ unconfirmed. ditto entries reflect its stated current product (AI patient-facing appointment summaries) and roadmap (Living Health Companion); some are aspirational and marked accordingly.

| Capability | Kin Health | ditto.care | Where ditto differentiates / is behind |
|---|---|---|---|
| **Appointment capture (record visit, in-person + telehealth)** | ✅ one-tap recording | ✅ record/ingest consultation (core product) | Parity. Both built on visit capture. |
| **Plain-language summary** | ✅ plain-English summary + action items | ✅ plain-language summary patient understands | Parity — ditto's explicit core promise. |
| **Action items / next steps** | ✅ prescriptions, labs, specialists, follow-ups | ⚠️ summary-centric; action-item structuring ❓ | Likely behind/at-parity — confirm ditto extracts structured to-dos. |
| **Longitudinal record / health timeline** | ⚠️ assembling, roadmap "health graph" | ⚠️ roadmap "Living Health Companion" | Both roadmap; neither shipped a mature longitudinal record. Tied. |
| **Document / record ingestion (labs, EHR docs)** | ⚠️ planned (EHR notes "this year") | ❓ unconfirmed | Both early; opportunity for ditto to ship first in EU. |
| **Ask-questions / Q&A assistant** | ❓ not clearly advertised | ⚠️ roadmap (daily companion) | Neither confirmed shipped; ditto's roadmap names it. |
| **Grounded / cited answers** | ⚠️ summaries grounded in the recorded conversation; multi-stage eval | ❓ unconfirmed | Open — ditto could lead on EU-grade groundedness/citations. |
| **Caregiver / family sharing** | ✅ "care circle," Manager vs Viewer roles | ✅ share with loved ones (core promise) | Kin has explicit role tiers; ditto should match/exceed role granularity. |
| **Symptom / medication tracking** | ⚠️ meds surfaced in summaries; tracking ❓ | ❓ unconfirmed | Both thin; greenfield. |
| **Reminders** | ⚠️ action items implied; native reminders ❓ | ❓ unconfirmed | Both unconfirmed. |
| **Multi-language** | ❌ English-only evident | ✅ EU-driven necessity (NL + others) ❓ scope | **ditto advantage** — EU market forces multilingual; Kin US-English. |
| **EU data residency / GDPR-native** | ❌ US-hosted; third-party API processing flagged | ✅ EU/NL anchored, GDPR-native | **ditto's strongest moat.** |
| **Regulatory posture (AI Act / MDR)** | ❌ US framing; not HIPAA-certified | ⚠️ EU AI Act + MDR awareness expected | **ditto advantage** if it operationalizes EU compliance. |
| **Integrations / EHR** | ⚠️ planned EHR ingestion 2026 | ❓ unconfirmed | Both early; EU EHR landscape differs (no single equivalent of US EHR vendors). |
| **Business model / pricing** | Free forever; **referral monetization** | ❓ likely SaaS / B2B2C (payers, clinics, insurers) | **Different models.** Kin's referral model is GDPR-fragile in EU; ditto can sell trust + B2B2C. |
| **Geography** | US | EU / Netherlands | Non-overlapping today — but both will expand. |
| **Funding (disclosed)** | $9M seed (Maveron, May 2026) | ❓ not in scope here | Kin is well-capitalized for a US push. |

**Read:** Kin and ditto are **feature-twins on the wedge** (capture → plain-language summary → caregiver share) and **roadmap-twins on the destination** (longitudinal health graph / companion). ditto is **behind** only on funding/maturity of the care-circle role model and action-item structuring; ditto is **ahead** structurally on **EU data residency, multilingual, regulatory posture, and a non-referral (trust-aligned) business model**. The defensible wedge for ditto is *"the EU-anchored, GDPR-native, trust-first version of Kin"* — not a feature race.

---

## 3. Other closest direct competitors

### 3.1 Patiently (Medical AI Notes) — *closest after Kin*
**Web:** [patiently.me](https://www.patiently.me/) · iOS id6748413070. **Profile:** Patient-side app that "records your visits, explains the jargon, and builds your **Medical Memory**." Press-record or import existing recordings; transcribes and extracts diagnoses/medications/follow-ups in "under a minute," organized into **Health Topics**. **Family/caregiver sharing** for kids, aging parents, self. **Free during beta** with later subscription ("Founder pricing" for early users). Privacy: Face ID/Touch ID, end-to-end encryption, no data sale/ads, delete anytime [Patiently, 2025 [T3]](https://www.patiently.me/); [Apple App Store [T3]](https://apps.apple.com/us/app/patiently-medical-ai-notes/id6748413070). **Maps to ditto:** near-identical to Kin and ditto's wedge (capture → plain-language → Medical Memory → share). Differentiator vs ditto: same as Kin — **US-centric, no EU residency/multilingual evidence**. **(Med)** Geography/funding **unconfirmed**.

### 3.2 Hedy AI — *real-time visit assistant*
**Web:** [hedy.ai](https://www.hedy.ai/) · [patient tool page](https://www.hedy.ai/patient-ai-tool). **Profile:** Broader "AI meeting coach" (30,000+ users across professionals/students) with a **dedicated medical-visit mode**: **translates medical jargon in real time as the doctor speaks**, suggests follow-up questions, and summarizes the visit afterward with key points, medication changes, and follow-up instructions. Strong on **multi-language (8 free / 30+ paid)** and **searchable transcripts** you can "share with siblings." Compliance: SOC 2 Type I, HIPAA assessment, **GDPR documentation + DPAs** [hedy.ai, 2025 [T3]](https://www.hedy.ai/); [Hedy patient tool, 2025/26 [T3]](https://www.hedy.ai/patient-ai-tool). **Pricing:** Free (15-min sessions, 8 languages); Pro $9.99/mo (unlimited length/sessions, web chat, multilingual); a $12.99/mo tier also referenced [Hedy pricing, 2025 [T3]](https://www.hedy.ai/pricing/). **Maps to ditto:** strongest on **real-time in-visit help + multilingual + GDPR docs** — i.e. it already has some EU-credible compliance and is the most multilingual rival. **This is the competitor closest to ditto on the multilingual/EU-trust axis.** Weaker on caregiver role tiers and longitudinal record. **(High)**

### 3.3 Abridge — *clinician-side incumbent that produces patient summaries*
**Web:** [abridge.com](https://www.abridge.com/). **Profile:** Market-leading **clinician** ambient-AI scribe deployed across major US health systems; for each recording it generates an **AI Patient Visit Summary (PVS)** with plan and instructions written at an **8th-grade reading level, in real time** [Abridge blog, 2025](https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time). Adoption scale: at UCHealth it grew from a 250-provider pilot to ~one-third of ~6,000 clinicians [UCHealth Today, 2025/26](https://www.uchealth.org/today/ai-note-taking-tool-helps-doctors-focus-fully-on-patients/). **Maps to ditto:** Abridge produces the *same artifact* (plain-language patient summary) but **provider-owned and provider-distributed**, not patient-controlled. Its threat is **distribution** — patients get the summary from their hospital, reducing the felt need for a standalone patient app. ditto/Kin's counter: **patient ownership across all providers** (not just one health system), portability, and family sharing. EU note: Abridge is US-centric; EU footprint **unconfirmed**. **(High)**

### 3.4 PatientNotes / PatientNotes.ai — *clinician scribe (adjacent, not patient-owned)*
**Web:** [patientnotes.app](https://www.patientnotes.app/) and [patientnotes.ai](https://patientnotes.ai/). **Profile:** AI medical scribe for **healthcare professionals** — records consultations, drafts SOAP/clinical notes, and can also produce **patient-facing summaries and letters**. HIPAA-compliant; from ~$50/user/mo [PatientNotes.ai, 2025/26 [T3]](https://patientnotes.ai/). **Maps to ditto:** clinician-side, B2B — competes for the *summary* artifact but sells to providers, not patients/families. Relevant as a reminder that the "patient summary" can be generated upstream by the clinician's tool. Lower direct overlap with ditto's patient-owned companion. **(Med)**

### 3.5 Big-Tech consumer health AI — *adjacent macro-threat to the "companion" vision*
Between **Jan–Mar 2026**, five major consumer health-AI products launched: **ChatGPT Health** (OpenAI, 7 Jan), **Claude for Healthcare** (Anthropic, 11 Jan), **Amazon Health AI** (22 Jan), **Microsoft Copilot Health** (12 Mar), and **Perplexity Health** (19 Mar). Each connects to **EHRs via intermediaries (b.well, HealthEx, state HIEs)** + **wearables (Apple Health, Fitbit, Oura)** to answer personalized health questions [IAPP, 2026](https://iapp.org/news/a/the-health-ai-agent-rush-five-products-in-three-months-and-the-privacy-questions-that-got-left-behind); [Modern Healthcare, 2026](https://www.modernhealthcare.com/health-tech/mh-perplexity-health-ai-ehr-wearable-data/); [Fierce Healthcare, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records). **Maps to ditto:** these own the **"ask questions about my health" + records aggregation** layer ditto's Living Health Companion targets — but they **do not yet own the appointment-capture moment** or the **caregiver/loved-ones sharing** experience, and they are US-EHR-centric. The IAPP framing ("the privacy questions that got left behind") is itself a wedge for an EU/GDPR-native, consent-first product. **(High on launches; Med on EU exposure)** — *Family-record organizers* like MyDigiRecords (up to 5 family profiles, medication reminders, "ask when was X's last shot") are a lighter-weight adjacent category [Jotform blog, 2026 [T3]](https://www.jotform.com/blog/medical-records-app/).

---

## 4. So-what for ditto (concise)

1. **Kin validates the wedge and the destination** — same product, same roadmap, real VC money. ditto is not first, but Kin proves the market and gives ditto a concrete playbook to differentiate against.
2. **Compete on geography + trust, not features.** EU data residency, GDPR-native consent, AI Act/MDR posture, and multilingual are structural moats Kin/Patiently/Abridge cannot quickly replicate.
3. **Attack the referral business model on trust.** Kin's "free + referral monetization" is GDPR-fragile in the EU; ditto's likely B2B2C/SaaS model can be framed as "we don't monetize your medical conversations."
4. **Match Kin's care-circle role tiers (Manager/Viewer) and ship structured action items** — these are concrete near-term gaps.
5. **Watch Hedy (multilingual + GDPR docs) and Big-Tech health AI** most closely — Hedy is the EU-credible patient-side rival; Big Tech owns the Q&A/aggregation layer ditto's companion will need.

---

## Sources

**Tier 1 — official / company / filings**
- Kin Health — official site, [meetkin.com](https://www.meetkin.com/) (2026) and [kinhealth.app](https://kinhealth.app/) (2026)
- Kin Health — "$9M to Give Patients a Record of Their Own Care," [BusinessWire](https://www.businesswire.com/news/home/20260518890468/en/Kin-Health-Raises-$9M-To-Give-Patients-a-Record-of-Their-Own-Care) (2026)
- Abridge — "Patient Visit Summaries—Now Generated in Real-Time," [abridge.com/blog](https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time) (2025); [abridge.com](https://www.abridge.com/)
- Hedy AI — [hedy.ai](https://www.hedy.ai/), [patient tool](https://www.hedy.ai/patient-ai-tool), [pricing](https://www.hedy.ai/pricing/) (2025/26)
- Patiently — [patiently.me](https://www.patiently.me/) (2025)
- PatientNotes — [patientnotes.app](https://www.patientnotes.app/), [patientnotes.ai](https://patientnotes.ai/) (2025/26)

**Tier 2 — reputable press**
- TechCrunch — "Kin Health raises $9M to build an AI notetaker for patients," [techcrunch.com](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/) (2026) *(403 on direct fetch; via search extract)*
- HIT Consultant — "Kin Health Raises $9M to Launch Free Conversational App for Patients," [hitconsultant.net](https://hitconsultant.net/2026/05/21/kin-health-raises-9m-seed-patient-ambient-ai/) (2026) *(403; via search extract)*
- LA Business Journal — "Kin Health Raises $9 Million in Seed Funding," [labusinessjournal.com](https://labusinessjournal.com/healthcare/kin-health-raises-9-million-in-seed-funding/) (2026) *(via search extract — founders/investors)*
- Morningstar / BusinessWire — [morningstar.com](https://www.morningstar.com/news/business-wire/20260518890468/kin-health-raises-9m-to-give-patients-a-record-of-their-own-care) (2026)
- Quartz — [qz.com](https://qz.com/kin-health-raises-9-million-ai-notetaker-patients-051926) (2026)
- NewsBytes — "Kin Health raises $9 million to transcribe and summarize doctor visits," [newsbytesapp.com](https://www.newsbytesapp.com/news/business/kin-health-raises-9-million-to-transcribe-and-summarize-doctor-visits/tldr) (2026) *(privacy concerns; via search extract)*
- UCHealth Today — "How an AI note-taking tool helps doctors focus fully on their patients," [uchealth.org](https://www.uchealth.org/today/ai-note-taking-tool-helps-doctors-focus-fully-on-patients/) (2025/26)
- IAPP — "The health AI agent rush: Five products in three months…," [iapp.org](https://iapp.org/news/a/the-health-ai-agent-rush-five-products-in-three-months-and-the-privacy-questions-that-got-left-behind) (2026)
- Modern Healthcare — "Perplexity launches consumer-focused AI health tool," [modernhealthcare.com](https://www.modernhealthcare.com/health-tech/mh-perplexity-health-ai-ehr-wearable-data/) (2026)
- Fierce Healthcare — "OpenAI launches ChatGPT Health…," [fiercehealthcare.com](https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records) (2026)

**Tier 3 — app-store / blog / self-report (FLAGGED)**
- Kin Health — [Apple App Store id6756894542](https://apps.apple.com/us/app/kin-health/id6756894542); [Google Play `com.meetkin.android`](https://play.google.com/store/apps/details?id=com.meetkin.android&hl=en) *(403 on direct fetch; ratings/installs unconfirmed)*
- Patiently — [Apple App Store id6748413070](https://apps.apple.com/us/app/patiently-medical-ai-notes/id6748413070)
- Disambiguation references (NOT the analyzed Kin): [Kin: Personal AI Advisors — mykin.ai / Play `ai.mykin.app`](https://play.google.com/store/apps/details?id=ai.mykin.app&hl=en); [Kin Wellness & Support id6747573503](https://apps.apple.com/us/app/kin-wellness-support/id6747573503); [KinHealthApp.com family history organizer](https://www.kinhealthapp.com/)
- MyDigiRecords / family-record organizers — [Jotform blog "11 best apps for managing medical records"](https://www.jotform.com/blog/medical-records-app/) (2026)

**Confidence & gaps:** Kin funding amount/lead investor **(High)**; full investor list and founder roster **(Med)**. Kin traction/app-store ratings **unconfirmed (Low)** — not surfaced and pages 403'd. ditto's own current feature set is taken from the task brief, not independently verified; matrix cells marked ❓ are genuine unknowns to confirm internally. Several Tier-2 sources are cited via search-engine extracts because the live pages blocked direct fetch in this environment.
