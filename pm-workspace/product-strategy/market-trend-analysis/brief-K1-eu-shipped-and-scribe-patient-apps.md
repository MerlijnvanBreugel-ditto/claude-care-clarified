# Brief K1 — EU/NL Shipped Patient-Summary Products + Scribes Moving Patient-Side

**Date compiled:** 2026-05-31 · **Analyst:** Mewtwo (competitive intelligence) · **Geography focus:** EU/NL primary, with US scribe context
**Discipline:** Every claim cites a full URL inline. `[F]` = fact from a source; `[I]` = inference; recency flagged per row. "Shipped" = live to real patients today; "Piloting" = limited live deployment; "Announced" = stated/roadmap, not confirmed live; "Rumored" = unverified.
**Builds on prior briefs** (Brief C competitive landscape, Phase2-B encroachment-race). This brief adds **new names not in those** and corrects two earlier claims (see Corrections box).

---

## 1) Executive Summary

**Job 1 — EU/NL shipped "understand your own record" products.** Beyond the prior set (ZAS Antwerp, ChipSoft HiX "Patiëntvriendelijke brief", Simply Onno, Doctolib), the comprehension artifact is being consumerized and institutionalized across the EU through three channels:

1. **Dutch PGOs (MedMij personal health environments)** — Quli and Ivido are live, MedMij-labelled PGOs with 35k+ user-class scale, but they ship **raw aggregated records, not AI plain-language summaries**. The AI-summary layer is arriving *on top of* PGOs via partners (HealthTalk.ai) and via the national accessibility push (Pharos "Begrijpelijke PGO's"). `[F]`
2. **German consumer document-translators** — beyond Simply Onno, the category is crowded and partly free/public: **mein-arztbefund.de** (paid, AI), **Befunddolmetscher.de** (free, public/Bertelsmann-origin, now under gesund.bund.de), and **Was hab' ich?** (free, volunteer medical students, the original 2011 model). All do the *comprehension half* of Ditto's job for consumers, document-upload only, no care-circle. `[F]`
3. **Research-grade oncology tools on home turf** — a **Tilburg University** AI tool to make medical info understandable/personalized, partnered with **Antoni van Leeuwenhoek** (the Dutch national cancer hospital) and Elisabeth-TweeSteden. Pre-product (focus groups Mar 2025), but it is the closest academic analog to Ditto's exact oncology-comprehension job, in NL. `[F]`
4. **UK NHS** — discharge-summary LLM pilot (Chelsea & Westminster, Aug 2025) is **clinician-drafted, not patient-direct**; no shipped patient-facing plain-language letter feature in the NHS App yet. `[F]`

**Net for Job 1:** The comprehension artifact is commoditizing fast, but it remains fragmented along the same axis as in prior briefs: **document-bound or portal-bound or single-provider, none patient-owned + recording-based + cross-provider + family-shareable.** PGOs are the structural threat to watch in NL because they own the aggregated record and the patient relationship; they just lack the AI summary layer today.

**Job 2 — Scribes moving patient-side.** The single clearest finding: **Abridge already ships a standalone consumer app, "Abridge for Patients"** (free, App Store + Google Play), that records visits, produces an 8th-grade-reading-level summary, tracks meds, and lets the patient **share with family** — i.e. it is functionally the closest thing to Ditto built by the best-funded scribe ($5.3B+ valuation). It is US-only and not the company's strategic focus (enterprise is), but it exists and is maintained (v2.26 in 2026). `[F]` Other scribes are adding patient *outputs* but staying B2B: **Ambience "Patient Recap", Commure** (patient-friendly pre/post-visit summaries), **Nabla** (auto plain-language visit summaries), **Heidi Comms** (patient communications, not a summary app). **Sword Health** is the inverse case: a genuinely consumer (B2B2C) patient app, but for physiotherapy/mental-health coaching, now pivoting *toward* provider tools.

**Correction to prior briefs:** **Suki's "patient summary" is clinician-facing** (a pre-visit chart digest for the doctor), **not** a patient-facing after-visit summary. Prior Brief C listed it as patient-facing — that is wrong. `[F]`

---

## 2) EU/NL Shipped Patient-Summary Examples (new since prior briefs)

| Name | Country | What ships to the patient | Status | Date / recency | URL |
|---|---|---|---|---|---|
| **Quli (PGO)** | NL | Aggregated medical record from multiple providers in one app (MedMij). **No AI plain-language summary** — raw data + self-tracking. | **Shipped** (live PGO) | Ongoing; IZA 2025 mandate context | https://www.quli.nl/pgo-persoonlijke-gezondheidsomgeving/ |
| **Ivido (PGO)** | NL | Same: MedMij-network record aggregation, lab results, meds, wearables, e-consult. **No AI summary** layer found. | **Shipped**; MedMij-labelled (label awarded by Minister Bruins) | Label + financing news 2024–25 | https://ivido.nl/nieuws/minister-bruins-reikt-medmij-label-uit/ |
| **HealthTalk.ai** | NL | AI speech-recognition + summary of the consult; generates a **simple, understandable summary** and can sit on top of a PGO; endorsed by insurer **Zilveren Kruis** as a good-practice. Primary summary target is the *provider*, patient benefit emerging. | **Shipped / piloting** (GGZ + hospitals) | Insurer good-practice page; active 2025 | https://healthtalk.ai/nl/solutions/ · https://www.zilverenkruis.nl/zorgaanbieders/visie-en-transformatie/goede-voorbeelden/ai-spraakherkenning |
| **Pharos "Begrijpelijke PGO's" / eHealth4ALL** | NL | National accessibility program making PGOs/patient-portals understandable for low-literacy users (co-design, B1 language). Not a product — a standard-setting + testing initiative shaping what PGOs must ship. | **Active program** (not a single product) | 2023 PGO tests; ongoing 2025 | https://www.pharos.nl/kennisbank/begrijpelijke-persoonlijke-gezondheidsomgevingen-pgos/ |
| **Tilburg University AI tool** (w/ Antoni van Leeuwenhoek + Elisabeth-TweeSteden) | NL | Personalized, plain-language + storytelling explanation of medical info to **reduce patient anxiety**; EHR-linkable. Oncology-relevant (AvL = national cancer hospital). | **Pre-product / research** (focus groups Mar 2025) | 2025 | https://www.tilburguniversity.edu/magazine/overview/new-ai-tool-makes-medical-information-understandable-and-personalized |
| **mein-arztbefund.de** | DE | Upload doctor's letter/report → instant AI plain-language translation (15 languages, ~€7.99/report per prior brief). Consumer, document-upload. | **Shipped** (commercial) | Active, content updated Nov 2025 | https://mein-arztbefund.de/ |
| **Befunddolmetscher.de** | DE | Free public tool translating ~10,000 medical terms into plain language; Bertelsmann-Stiftung origin, now under gesund.bund.de (federal health portal). Term-lookup, not whole-letter AI. | **Shipped** (free, public) | Long-running; live under gesund.bund.de | https://befunddolmetscher.de/ |
| **Was hab' ich? (washabich.de)** | DE | Free service: medical students/doctors translate uploaded findings into plain language. The original (2011) human model behind the category. | **Shipped** (free, volunteer) | Long-running, still live | https://www.aok.de/pk/magazin/wohlbefinden/selbstbewusstsein/den-arztbrief-uebersetzen-welche-online-angebote-wirklich-helfen/ |
| **NHS discharge-summary LLM pilot** (Chelsea & Westminster, on Federated Data Platform) | UK | LLM drafts discharge summaries from the record; **clinician reviews + signs off**. Aim = faster discharge, not a patient-direct plain-language letter. **Not patient-facing.** | **Piloting** (clinician-mediated) | Announced 17 Aug 2025 | https://www.digitalhealth.net/2025/08/ai-assisted-tool-on-fdp-will-help-write-hospital-discharge-letters/ |

**Notable absence (verified):** No live AI "explain-your-medical-letter" patient feature surfaced inside Dutch insurers (CZ/VGZ/Zilveren Kruis) as their own product — Zilveren Kruis instead *endorses* HealthTalk.ai as a provider good-practice. `[F]` Denmark's **Min Sundhedsplatform / sundhed.dk** patient portals ship records + appointments but **no AI plain-language summary** surfaced. `[F]` https://www.sundhed.dk/

---

## 3) Scribes Moving Patient-Side

| Scribe | Patient-facing app / feature? | Shipped / Announced | Geography & consumer ambition | URL |
|---|---|---|---|---|
| **Abridge** | **YES — standalone consumer app "Abridge for Patients."** Records visit → real-time 8th-grade-level summary + interactive transcript; med list; **secure share with family.** This is the closest scribe-built analog to Ditto. | **Shipped** (free; App Store + Google Play; v2.26 maintained into 2026). Originated as a free telehealth-capture app (UPMC, 2020). | US-only. Strategic focus is enterprise B2B ($5.3B val, $300M Series E Jun 2025; +$316M extension Apr 2026); patient app is a maintained side product, not the growth thesis. | https://play.google.com/store/apps/details?id=ai.abridge.nativeclient.release · https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time |
| **Ambience Healthcare** | **Patient-facing output: "Patient Recap"** — plain-language after-visit summaries (next steps, meds, takeaways) for patients/families/caregivers; also a pre-visit chart digest. Delivered **via the health system**, no consumer app. | **Shipped** via health systems (launched at St. Luke's 24 Jun 2025; deployed Cleveland Clinic, UCSF). | US/North America. Pure B2B, no consumer ambition stated. | https://www.ambiencehealthcare.com/blog/ambience-healthcare-s-patient-recap-offers-clinicians-the-first-chart-summarization-technology-from-an-ambient-ai-platform |
| **Commure** | **Patient-facing outputs:** patient-engagement platform with **patient-friendly insurance details + pre/post-visit summaries + follow-up recommendations**, plus AI-generated patient emails/letters from encounter context. Delivered via provider. | **Shipped / rolling out** (post-$200M raise, AI agents incl. patient outreach). | US. Pure B2B; "patient engagement" is a provider-sold module, not a consumer app. | https://www.fiercehealthcare.com/ai-and-machine-learning/fresh-200m-raise-commure-rolls-out-ai-agents-automate-physician-workflow |
| **Nabla** | **Patient-facing feature:** auto-generated **plain-language visit summaries** as part of clinician documentation. No consumer app. | **Shipped** (feature). | France HQ, US-heavy. Pure B2B; no B2C move. (Named in a US no-consent incident, Jan 2026.) | https://www.nabla.com/ · https://hospitalogy.com/articles/2025-06-18/breaking-down-nabla-sword-and-commons-clinics-recent-raises/ |
| **Heidi Health** | **Heidi Comms** = AI **patient communications** (calls, bookings, reminders, follow-ups, post-visit engagement across SMS/email/app) — communications layer, **not** a patient summary app. Heidi also generates patient summaries on request (clinician-mediated). | **Shipped** (Heidi Comms launched Feb 2026). | AU HQ, UK/EU heavy, PLG/freemium for clinicians. Closest to a self-serve motion, but buyer is still the clinician, not the patient. | https://www.heidihealth.com/en-us/comms |
| **Suki** | **NO patient-facing summary.** Its "patient summary" is a **clinician-facing pre-visit chart digest** (overview of the patient's history *for the doctor*). **Prior-brief correction.** | Shipped to clinicians, not patients. | US. Pure B2B, no consumer product. | https://www.fiercehealthcare.com/ai-and-machine-learning/suki-launches-patient-summary-and-qa-features-its-ai-assistant-google-cloud |
| **Tortus** | No patient-facing app/feature surfaced — clinician notes, referral letters, coding. | n/a (clinician-only) | UK/NHS (Kent & Medway eval; X-on Health primary-care rollout 2025). No consumer move. | https://tortus.ai/product |
| **Corti** | No patient-facing app/feature surfaced — clinician co-pilot, transcription/summary for clinicians. | n/a (clinician-only) | Denmark/EU. No consumer move. | https://www.eesel.ai/blog/corti-ai |
| **Tandem Health** | No patient-facing artifact — ambient note generation; patient benefit = "more doctor time." (Acquired Dutch scribe Juvoly per prior brief.) | n/a (clinician-only) | Sweden HQ; most EU-distributed scribe (UK/DE/FR/ES/NL/Nordics). No consumer move. | (prior Brief C [18][19]) |
| **Sword Health** | **Inverse case: a genuine consumer (B2B2C) patient app** — but for MSK/pain + **"Mind"** mental-health AI care, *not* visit summaries. Now extending its patient-facing agents into **provider-facing** tools ("Sword Intelligence"). | **Shipped** (consumer app, 800k+ users). | US/EU (Portugal origin). Strongest consumer DNA of the group, but adjacent job (coaching, not comprehension). | https://swordhealth.com/ · https://apps.apple.com/us/app/sword-health-ai-care/id1468523447 |

**Pattern `[I]`:** Two distinct motions. (a) **Patient *output* as a B2B feature** (Ambience, Commure, Nabla, Suki's clinician digest) — the summary reaches the patient *through the institution*, the scribe never owns the patient relationship. (b) **Patient-*owned* app** — only **Abridge for Patients** does this among scribes, and it is a maintained-but-deprioritized side product. **No scribe is making a strategic B2C push.** The one with consumer DNA (Sword) is moving the *other* direction (toward providers).

---

## Corrections to Prior Briefs

- **Suki — NOT patient-facing.** Brief C listed Suki's patient summary as patient-facing. It is a **clinician pre-visit chart digest**. Corrected. `[F]`
- **Abridge — has a *standalone consumer app*, not just an EHR-embedded summary.** Brief C framed Abridge's patient summary as "delivered via the health system, not a consumer app." That is true for the *enterprise* product, but Abridge **also ships "Abridge for Patients"** (free, patient-owned, family-shareable). This materially strengthens the "scribe encroaching patient-side" thesis — the best-funded scribe has already built Ditto's shape, just not as its priority. `[F]`

---

## 4) Implications for Ditto

1. **The PGO is the structural NL threat, not the scribes.** Quli/Ivido already own the aggregated, cross-provider, patient-owned record — the one thing Ditto's care-layer claims as a moat — and the IZA 2025 mandate + Pharos accessibility push will force an AI plain-language layer on top of them. If a PGO bolts on HealthTalk-style summarization, it has Ditto's data position *plus* government distribution. **Recommendation:** treat MedMij/PGO interoperability as both threat and channel — Ditto should be a MedMij data source/consumer, not a walled garden the PGO routes around. `[I]`

2. **"Abridge for Patients" is the proof and the warning.** The category leader has already built a patient-owned, family-shareable, recording-based summary app. It is US-only and deprioritized today, but it removes "no one has built this" as a defensibility claim. Ditto's edge is **EU/GDPR-native + oncology depth + care-circle as the core (not a share button) + cross-provider memory**, not the existence of a patient app. Position accordingly. `[I]`

3. **The comprehension artifact is now table stakes in DE consumer + NL/BE portals.** Befunddolmetscher (free, federal), Was hab' ich? (free), Simply Onno, mein-arztbefund, ZAS, HiX. A one-shot "translate my letter" is no longer differentiated. **Defensibility must live in the longitudinal, recording-based, family-coordinated care relationship** — the repeated visit, the shared circle, the cross-provider thread — not the single summary. `[I]`

4. **Antoni van Leeuwenhoek is doing oncology-comprehension research with Tilburg.** This is Ditto's exact job, exact domain, on home turf, with a top oncology institution. **Recommendation:** scope a partnership/awareness conversation before it crystallizes into a hospital-owned tool that competes for the same clinicians and patients. `[I][R]`

5. **Trust/consent is a real EU wedge.** Two US no-consent incidents now name scribes (Abridge 2025 lawsuits; Nabla Jan 2026 LCMC incident). An EU-native, consent-first, GDPR-clean product can market trust as a feature US-origin scribes have not earned. `[F]` (Links to Brief A.)

---

## 5) Sources

**Job 1 — EU/NL shipped patient-summary**
- Quli PGO — https://www.quli.nl/pgo-persoonlijke-gezondheidsomgeving/ (live PGO; accessed May 2026)
- Ivido MedMij label — https://ivido.nl/nieuws/minister-bruins-reikt-medmij-label-uit/ (2024–25)
- Ivido PGO features — https://ivido.nl/pgo-informatie/
- HealthTalk.ai solutions — https://healthtalk.ai/nl/solutions/
- Zilveren Kruis good-practice (AI speech recognition / HealthTalk) — https://www.zilverenkruis.nl/zorgaanbieders/visie-en-transformatie/goede-voorbeelden/ai-spraakherkenning
- Pharos "Begrijpelijke PGO's" — https://www.pharos.nl/kennisbank/begrijpelijke-persoonlijke-gezondheidsomgevingen-pgos/
- Pharos eHealth4ALL program — https://www.pharos.nl/over-pharos/programmas-pharos/ehealth4all/
- Tilburg University AI tool (w/ Antoni van Leeuwenhoek, Elisabeth-TweeSteden) — https://www.tilburguniversity.edu/magazine/overview/new-ai-tool-makes-medical-information-understandable-and-personalized
- mein-arztbefund.de — https://mein-arztbefund.de/
- Befunddolmetscher (under gesund.bund.de) — https://befunddolmetscher.de/
- Was hab' ich? / overview of DE translation services (AOK) — https://www.aok.de/pk/magazin/wohlbefinden/selbstbewusstsein/den-arztbrief-uebersetzen-welche-online-angebote-wirklich-helfen/
- NHS discharge-summary LLM pilot (Chelsea & Westminster) — https://www.digitalhealth.net/2025/08/ai-assisted-tool-on-fdp-will-help-write-hospital-discharge-letters/
- sundhed.dk (DK patient portal, no AI summary found) — https://www.sundhed.dk/

**Job 2 — Scribes patient-side**
- Abridge for Patients (Google Play) — https://play.google.com/store/apps/details?id=ai.abridge.nativeclient.release
- Abridge patient visit summaries — https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time
- Abridge funding/scale (Contrary) — https://research.contrary.com/company/abridge
- Ambience "Patient Recap" — https://www.ambiencehealthcare.com/blog/ambience-healthcare-s-patient-recap-offers-clinicians-the-first-chart-summarization-technology-from-an-ambient-ai-platform
- Commure AI agents / patient engagement — https://www.fiercehealthcare.com/ai-and-machine-learning/fresh-200m-raise-commure-rolls-out-ai-agents-automate-physician-workflow
- Nabla — https://www.nabla.com/ ; raise context — https://hospitalogy.com/articles/2025-06-18/breaking-down-nabla-sword-and-commons-clinics-recent-raises/
- Heidi Comms — https://www.heidihealth.com/en-us/comms
- Suki patient summary (clinician-facing) — https://www.fiercehealthcare.com/ai-and-machine-learning/suki-launches-patient-summary-and-qa-features-its-ai-assistant-google-cloud
- Tortus product — https://tortus.ai/product
- Corti overview — https://www.eesel.ai/blog/corti-ai
- Sword Health — https://swordhealth.com/ ; consumer app — https://apps.apple.com/us/app/sword-health-ai-care/id1468523447

**Confidence notes**
- HIGH: Abridge for Patients exists & is patient-owned/family-shareable; Ambience/Commure/Nabla ship patient outputs as B2B features; Quli/Ivido are live raw-data PGOs without AI summary; DE consumer translators are live.
- MEDIUM: HealthTalk.ai's exact patient-vs-provider summary delivery (sources emphasize provider-facing summary; patient benefit is implied). Tilburg tool is pre-product. NHS pilot is clinician-mediated (high confidence it is NOT patient-direct).
- Recency: most sources 2025–2026; PGO/DE-translator pages are living pages accessed May 2026.
