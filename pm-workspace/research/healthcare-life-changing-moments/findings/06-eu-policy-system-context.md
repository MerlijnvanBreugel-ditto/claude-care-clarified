# EU Policy, Data-Infrastructure & Regulatory Context for a Patient-Facing AI Health Companion

**Prepared for:** ditto.care (European patient-facing health-tech)
**Author:** Health-policy & regulatory research
**Access date for all sources:** 2026-05-31
**Scope:** EHDS, EU AI Act, MDR/MDSW, GDPR & proxy access, national patient-data ecosystems (NL/DE/AT/CH), reimbursement & payer landscape.

> **Source tiers:** Tier 1 = official EU/EUR-Lex, national authorities (BfArM, gematik, BSI, Nictiz/MedMij, oesterreich.gv.at), regulatory guidance (MDCG). Tier 2 = reputable legal/consultancy analysis. Tier 3 = news (flagged).

---

## Key takeaways

1. **The infrastructure tailwind is real and dated.** EHDS is in force (26 March 2025); patient access to own data and cross-border exchange of Patient Summaries + ePrescriptions must be operational in all Member States by **March 2029**, with labs/images/discharge reports by **March 2031**. Germany's ePA and the Dutch MedMij/PGO framework already give ditto standardized, consented rails to pull patient data into an app — exactly what a companion needs. **Tailwind.**

2. **Proxy/loved-one access is already a first-class, legally-supported feature in DE and NL** — Germany's ePA lets a patient name up to 5 representatives; the Netherlands runs national proxy authorization via DigiD Machtigen (from age 16) plus legal-representative access for minors. ditto's caregiver use-case rides existing national plumbing rather than inventing it. **Strong tailwind.**

3. **MDR is the sharpest fork in the road.** If ditto only *informs/explains/summarizes/organizes* (and the output stays with the patient), it can stay a non-device "information/wellness" tool. The moment it provides output **intended to drive or inform clinical management of a specific patient** (decision support, triage, diagnosis, treatment recommendation), it becomes Medical Device Software (MDSW), almost certainly **class IIa+ under Rule 11**, triggering CE marking. This is the dominant product-design constraint. **Constraint (manageable via intended-purpose discipline).**

4. **AI Act risk depends entirely on whether ditto is a medical device.** Non-device patient-information AI is mostly subject only to **Article 50 transparency** (tell users they're talking to AI; label AI-generated content) — light. If it becomes MDSW, it is **high-risk** and inherits the full Annex III/Chapter III regime on top of MDR. Deadlines are being pushed: political agreement (7 May 2026) signals **Dec 2027** (standalone high-risk) / **Aug 2028** (product-embedded/medical-device AI); Article 50 transparency still lands **2 August 2026**. **Constraint that scales with ambition; transparency duty applies regardless.**

5. **Reimbursement is fragmented and only Germany offers a clean, scalable payer path (DiGA).** DiGA is a statutory-insurance fast-track: BfArM-listed apps are prescribed by physicians and paid by SHI funds for all 73M insured. The Netherlands has **no DiGA equivalent** — digital tools get funded inside existing care pathways/consultations at insurer discretion. Switzerland (EPD) and Austria (ELGA) have no app-reimbursement scheme. **Mixed: DiGA = tailwind in DE; elsewhere a go-to-market constraint (B2B2C / self-pay).**

---

## 1. European Health Data Space (EHDS)

**What it is.** Regulation **(EU) 2025/327** establishing a European Health Data Space — an EU-wide framework giving individuals control over their electronic health data and creating cross-border digital infrastructure for both **primary use** (care delivery) and **secondary use** (research/policy). Published in the Official Journal **5 March 2025**; entered into force **26 March 2025** ([EUR-Lex, Reg (EU) 2025/327, 2025](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng); [Arnold & Porter, 2025](https://www.arnoldporter.com/en/perspectives/advisories/2025/03/european-health-data-space-regulation-published)).

**Timeline (staged application).**
- **March 2027** — Commission to adopt key implementing acts (detailed operational rules) ([EY, 2025](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds); [Baker McKenzie, 2025](https://healthcarelifesciences.bakermckenzie.com/2025/03/05/european-health-data-space-regulation-published-whats-next/)).
- **March 2029** — Primary-use provisions apply: cross-border exchange of the first priority data categories (**Patient Summaries, ePrescriptions/eDispensations**) operational in all Member States ([EUR-Lex, 2025](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng); [EPR, 2025](https://www.epr.eu/eu-health-data-space-regulation-to-be-implemented-throughout-the-next-4-years/)).
- **March 2031** — Second priority categories (medical images, lab results, hospital discharge reports) and clinical-trial/genetic data ([EPR, 2025](https://www.epr.eu/eu-health-data-space-regulation-to-be-implemented-throughout-the-next-4-years/)).

**What "primary use" enables for a patient app.** Individuals can **access, control and share** their electronic health data, including across borders, for care delivery. Concrete patient rights: submit online requests to rectify records; **data portability** to move data between providers and across borders; **restrict** health-professional access to all/parts of their data; **know who accessed** their data (records kept ≥3 years, free of charge); and (where a Member State legislates it) **opt out** of access — reversible, with vital-interests override ([EUR-Lex, 2025, Arts 4/8–12](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng); [Noerr, 2025](https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview)). For a companion app this is the legal mandate that patient data must be made available to the patient (and their chosen apps) in a structured, portable form.

**MyHealth@EU.** The operational cross-border infrastructure (formerly eHDSI) connecting national contact points so citizens can use Patient Summaries and ePrescription/eDispensation abroad. As of 2025 ~**15 Member States** support at least one service live (incl. Czechia, Estonia, Greece, Finland, France, Croatia, Ireland, Lithuania, Luxembourg, Latvia, Malta, Poland, Portugal), with most others expected to join; EHDS makes participation and the priority data flows **mandatory** by 2029/2031 ([EC, Electronic cross-border health services](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en); [HaDEA, 2025](https://hadea.ec.europa.eu/news/2024-eu4health-work-programme-new-projects-advancing-digital-healthcare-across-eu-2025-12-03_en)).

**Tailwind/Constraint: TAILWIND (structural, multi-year).** EHDS legally compels exactly the data availability and portability ditto depends on — turning today's fragmented access into a guaranteed, standardized rail. The constraint is timing: full cross-border flows are 2029/2031, so near-term ditto must integrate national systems (Section 5) rather than rely on EHDS being "done." *Confidence: High.*

---

## 2. EU AI Act

**Risk classification of health/medical AI.** The AI Act is risk-tiered: prohibited / high-risk / limited-risk (transparency) / minimal. **AI that is itself a medical device, or a safety component of one, requiring third-party (Notified Body) conformity assessment under MDR/IVDR, is high-risk** under Article 6(1). High-risk uses explicitly include **diagnosis, clinical decision support, treatment recommendation, patient triage and patient monitoring** ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/eu-ai-act-pharma-medical-device-compliance); [Tandem Health, 2025](https://tandemhealth.ai/en/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know)). High-risk obligations: risk management, data governance, technical documentation, logging, transparency, **human oversight**, accuracy/robustness, and post-market monitoring — layered on top of MDR ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/eu-ai-act-pharma-medical-device-compliance)).

**Implications for an AI tool that summarizes/explains medical info to patients.** If ditto's AI is **not** a medical device (it explains/summarizes general or the patient's own information without driving clinical management — see Section 3), it is **not high-risk**. Its principal duty is **Article 50 transparency**: users interacting with an AI system (chatbot) must be informed they are talking to AI, at/ before the start of the conversation; AI-generated content (text/audio/image/video) must be **marked as artificially generated** in machine-readable form ([artificialintelligenceact.eu, Art. 50](https://artificialintelligenceact.eu/article/50/); [AI Act Service Desk (EC), Art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)). If the AI becomes MDSW, the full high-risk regime attaches.

**Timeline of obligations.**
- **2 Aug 2026** — most provisions apply, **including Article 50 transparency** and the original high-risk date ([artificialintelligenceact.eu, Art. 50](https://artificialintelligenceact.eu/transparency-rules-article-50/); [Trilateral Research, 2025](https://trilateralresearch.com/responsible-ai/eu-ai-act-implementation-timeline-mapping-your-models-to-the-new-risk-tiers)).
- **2 Aug 2027** — original date for Article 6(1) AI embedded in third-party-assessed products (CE-marked medical devices/IVDs) ([MedDeviceGuide, 2026](https://meddeviceguide.com/blog/eu-ai-act-medical-devices-compliance-guide)).
- **Delay in progress (Digital Omnibus):** As of **April 2026** Council and Parliament support pushing high-risk deadlines to **2 Dec 2027** (standalone high-risk) and **2 Aug 2028** (AI embedded in regulated products incl. medical devices); **political agreement reached 7 May 2026** [Tier 3 — confirm final text] ([Travers Smith, 2026](https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/); search summary, 2026).

**Tailwind/Constraint: CONSTRAINT that scales with ambition.** As a patient-information/explanation tool, the burden is light (Article 50 disclosure + AI-content labelling, live Aug 2026) — easily met by design. The high-risk regime only bites if ditto crosses into medical-device territory, where it stacks on MDR. *Confidence: High on classification logic and Aug-2026 transparency date; Medium on the high-risk delay (still being finalized as of May 2026).*

---

## 3. Medical Device Regulation (MDR) — the MDSW line

**When software becomes a medical device.** Under MDR (Reg (EU) 2017/745) and **MDCG 2019-11**, software is MDSW when it has a **medical intended purpose** as defined in the medical-device definition — e.g. diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease — regardless of whether it drives hardware ([MDCG 2019-11, EC](https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf); [Decomplix, 2024](https://decomplix.com/medical-software-mdr/)).

**The line that keeps a product OUT of MDR.**
- **Software for general purposes (even in healthcare), administration, lifestyle/well-being, or that merely stores, communicates, or displays data is NOT a medical device** ([MDCG 2019-11](https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf); [NAMSA](https://namsa.com/resources/blog/eu-mdr-and-ivdr-classifying-medical-device-software-mdsw/)).
- Software providing **information** to patients vs **information that informs treatment/diagnosis of a disease** is the qualifier: health/wellness info = out; clinical-purpose info = in ([greenlight.guru on MDCG 2019-11](https://www.greenlight.guru/blog/mdcg-2019-11)).
- A notable carve-out: software letting **patients estimate their own risk from self-entered data** (e.g. a diabetes risk calculator) **may be treated as not driving/informing clinical management if the output stays with the patient and is not transferred to a healthcare professional** ([MDCG 2019-11 Rev.1 reinterpretation, per Emergo by UL](https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful)).

**What pulls it IN.** Output **intended to drive or inform clinical management of an individual patient** — clinical decision support, triage, diagnosis, treatment recommendations, monitoring with alerts. Under **MDR Rule 11**, almost all such MDSW is **class IIa or higher** (IIb/III where decisions could cause serious deterioration/death), requiring **Notified Body conformity assessment and CE marking** ([NAMSA](https://namsa.com/resources/blog/eu-mdr-and-ivdr-classifying-medical-device-software-mdsw/); [Decomplix, 2024](https://decomplix.com/medical-software-mdr/)). Rule 11 is the reason there is effectively no "low-risk software MD" safe harbor for clinical-decision features.

**Design implication for ditto.** A companion that **summarizes the patient's own records, explains medical terms/letters in plain language, answers general health questions, and helps organize care/appointments** can be positioned as a non-device information tool — *provided* its intended purpose and claims avoid individualized clinical recommendations and its outputs are framed as information for the patient, not clinical decision support for a professional. Adding "what should I do about this symptom/result" individualized advice, triage, or alerting risks tipping into MDSW.

**Tailwind/Constraint: CONSTRAINT (the central product-design boundary).** Manageable: the intended-purpose/claims discipline is well-documented and gives ditto a clear non-device lane. But it materially limits how prescriptive the AI can be without a CE/MDR program (which also unlocks DiGA — see Section 5). *Confidence: High.*

---

## 4. GDPR & proxy / loved-one access

**Lawful basis for health data.** Health data is an Article 9 special category: processing is prohibited unless an Art. 9(2) condition applies — for a consumer health app the realistic bases are **explicit consent** (Art. 9(2)(a)) or, in care contexts, **health/medical-care purposes under professional-secrecy** (Art. 9(2)(h)). This is **cumulative** with an Art. 6 lawful basis — both layers required for every processing activity ([gdpr-info.eu, Art. 9](https://gdpr-info.eu/art-9-gdpr/); [Secure Privacy healthcare guidance](https://support.secureprivacy.ai/article/industry-specific-dpo-guidance-healthcare/)). Consent must be freely given, specific, informed, unambiguous. For a patient-facing app not delivering professional care, **explicit consent is the practical basis**.

**Proxy / loved-one access — the legal mechanics.** GDPR permits a third party to act for the data subject, but the *authority* (who may access, how proxy is established, minors/incapacity) is set by **national law** — Art. 9(4) lets Member States add conditions on health data, and access/representation rules vary by state ([gdpr-info.eu, Art. 9](https://gdpr-info.eu/art-9-gdpr/); [Adequacy DPO Insights](https://www.adequacy.app/en/blog/health-data-gdpr-compliance)). For minors/incapacitated persons the legal representative may exercise access rights independently ([revolve.healthcare](https://revolve.healthcare/blog/patient-consent-and-digital-health-data-in-gdpr-and-hipaa-context)).

**National implementations ditto can build on (see also Section 5):**
- **Netherlands:** national proxy via **DigiD Machtigen** — from age 16 a patient can authorize a family member/caregiver to access their portal (revocable any time at machtigen.digid.nl); parents/legal reps access records of children <12 ([LHV](https://www.lhv.nl/thema/patientengegevens-en-ict/online-inzage-in-het-patientendossier/); [Volgjezorg/MedMij](https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij)).
- **Germany:** the **ePA lets the insured nominate up to 5 representatives** (relatives, friends, caregivers, legal reps), each using their own ePA app; reps can manage but not delete the record or appoint other reps; the patient sees and controls all access ([BSI](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/E-Health/Elektronische-Patientenakte/elektronische-patientenakte.html); [gesund.bund.de](https://gesund.bund.de/en/die-elektronische-patientenakte)).

**Tailwind/Constraint: TAILWIND for the caregiver use-case, with a per-country compliance overhead.** ditto's loved-one/caregiver feature aligns with — and can plug into — existing national proxy mechanisms; explicit-consent design plus national-variation handling is the cost. *Confidence: High for NL/DE mechanics; Medium on the breadth of national variation across all target markets.*

---

## 5. National patient-data ecosystems

### Netherlands — MedMij / PGO / Nictiz
**MedMij** is the Dutch trust framework/standard for secure exchange of health data between citizens and providers; a **PGO (persoonlijke gezondheidsomgeving)** is the patient-facing app/portal where a person views, manages and shares their data. A **MedMij label** certifies a PGO meets strict security/interoperability requirements so providers can trust data retrieval. **Nictiz** develops/maintains the underlying information standards ([Nictiz, MedMij](https://nictiz.nl/wat-we-doen/programmas/medmij/); [Volgjezorg](https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij)). For ditto, becoming/integrating with a MedMij-certified PGO is the credible route to pull Dutch patient data with consent. *Confidence: High.*

### Germany — ePA, gematik, DiGA
- **ePA ("ePA für alle"):** v3.0 piloted Jan 2025; SHI funds auto-created an ePA for every insured unless they opted out (from **15 Jan 2025**); nationwide availability from **April 2025** (rollout 29 Apr 2025); **mandatory use by providers from Oct 2025** — ~73M insured covered ([BSI](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/E-Health/Elektronische-Patientenakte/elektronische-patientenakte.html); [iamexpat, 2025, Tier 3](https://www.iamexpat.de/expat-info/germany-news/electronic-patient-files-epa-roll-out-across-germany-april-29)). **gematik** operates the telematics infrastructure.
- **DiGA (BfArM fast-track, §139e SGB V):** statutory reimbursement pathway for CE-marked medical-device apps (classes I/IIa; **IIb added 2024 and from 2026 certain low-risk IIb**). **Provisional listing** (12 months, extendable to 24) lets a DiGA be prescribed and reimbursed while collecting evidence. As of **23 Feb 2026, 61 apps** are listed; mental health is the largest category ([BfArM DiGA Guide](https://www.bfarm.de/SharedDocs/Downloads/EN/MedicalDevices/DiGA_Guide.html); [BfArM DiGA](https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/_node.html); [MTRC, 2026](https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany)). **2026 changes:** mandatory success measurement (AbEM) with continuous reporting to BfArM; a DiGA Remuneration Reform effective **1 April 2026** adding billable GOP codes for DiGA-related consultation/documentation ([Inside EU Life Sciences, 2026](https://www.insideeulifesciences.com/2026/02/03/germany-changes-rules-for-digital-health-applications/)). *Confidence: High.*

### Austria — ELGA
**ELGA** (Elektronische Gesundheitsakte), live since 2015, is a **federated** record (it stores pointers to where data lives, not a central copy) covering e-medication, e-findings/lab/discharge. Switched toward broader **opt-out** in **April 2025**; patients can access their own data, and care facilities (not just doctors/pharmacies as in Germany) can access ([oesterreich.gv.at, ELGA](https://www.oesterreich.gv.at/en/themen/gesundheit/elektronisches-gesundheitssystem/elga_elektronische_gesundheitsakte); [EC digital-building-blocks, ELGA](https://ec.europa.eu/digital-building-blocks/sites/pages/viewpage.action?pageId=533365925)). No app-reimbursement scheme. *Confidence: Medium-High.*

### Switzerland — EPD
The **elektronisches Patientendossier (EPD)**, established 2017, remains **patchily adopted**: not mandatory for the public or for office-based doctors, pharmacies, physiotherapists; uptake is low and full hospital/care-home implementation incomplete. Note Switzerland is **non-EU/EEA**, so EHDS does not apply and it has its own data-protection (revFADP) regime ([JMIR, 2025](https://www.jmir.org/2025/1/e78193/XML)). *Confidence: Medium.*

**Tailwind/Constraint:** Data infrastructure is a **TAILWIND** in NL (MedMij/PGO) and DE (ePA at scale), **emerging** in AT (ELGA opt-out), and a **CONSTRAINT** in CH (low EPD adoption, outside EHDS).

---

## 6. Reimbursement & payer landscape

| Market | Who pays for a patient-facing digital tool | Dedicated app pathway? |
|---|---|---|
| **Germany** | **SHI funds** pay BfArM-listed DiGA; physician/psychotherapist prescribes, patient downloads, insurer reimburses for all 73M SHI insured | **Yes — DiGA** (fast-track, §139e) ([BfArM Guide](https://www.bfarm.de/SharedDocs/Downloads/EN/MedicalDevices/DiGA_Guide.html); [Prova Health, 2025](https://www.provahealth.com/insights/diga-reimbursement-germany-guide)) |
| **Netherlands** | Digital care reimbursable only if it meets Zvw package criteria (safe + proven effective); typically **funded inside an existing reimbursable act/consultation** at insurer discretion, not as a standalone product | **No DiGA equivalent** (steps toward DTx, not concrete) ([Zorginstituut Nederland](https://english.zorginstituutnederland.nl/about-us/working-methods-and-procedures/advising-on-and-clarifying-the-contents-of-the-standard-health-care-benefit-package); [MTRC, NL](https://mtrconsult.com/news/reimbursement-telemedicine-and-digital-care-netherlands)) |
| **Austria** | No app reimbursement scheme; tools funded by providers or self-pay | No |
| **Switzerland** | No app reimbursement scheme; basic insurance (KVG) covers defined services only; largely self-pay | No |

**Implications.** Germany's DiGA is the only clean, scalable third-party-payer route — but it **requires CE/MDR medical-device status** (Section 3), so it's available only if ditto deliberately builds a regulated clinical feature. As a non-device companion, ditto's near-term routes are **self-pay (B2C subscription), employer/insurer partnerships, or provider/B2B2C bundling** — and in NL, riding an existing reimbursable care pathway. ([HBS/PMC digital-health reimbursement reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC10576236/); [VWS, Financing digital health apps in Europe, 2025](https://www.zorgakkoorden.nl/documenten/publicaties/2025/251210-vws-financing-and-making-available-of-digital-health-applications-in-europe.pdf)).

**Tailwind/Constraint: MIXED.** DiGA = a real reimbursement **tailwind in DE** but gated behind MDR. Elsewhere reimbursement is a **constraint** — expect self-pay / B2B2C as the default monetization for a non-device companion. *Confidence: High for DE/NL structure; Medium on AT/CH specifics.*

---

## Implications for ditto

1. **Stay deliberately on the non-device side of the MDSW line** to keep MDR + AI-Act-high-risk burdens off the core product: position the AI as explaining/summarizing the patient's own data and general health information, with outputs framed as information *for the patient* — not individualized clinical recommendations, triage, or decision support for professionals. This is the single highest-leverage strategic constraint (Sections 2–3).

2. **Build the caregiver/loved-one feature on existing national proxy rails** (DE ePA's up-to-5-representatives; NL DigiD Machtigen) rather than a bespoke consent scheme. It's legally supported, lowers trust friction, and differentiates. Plan for **per-country national variation** in proxy/representation law (Section 4).

3. **Treat EHDS + ePA + MedMij as the medium-term data moat.** Near term, integrate national systems (MedMij-certified PGO in NL, ePA/gematik in DE); EHDS guarantees portability/cross-border by 2029/2031, so early integration compounds (Sections 1, 5).

4. **Ship Article 50 transparency by Aug 2026 regardless** — clear "you're talking to an AI" disclosure and AI-generated-content labelling. Cheap, mandatory, and a trust feature (Section 2).

5. **Sequence markets by payer reality:** Germany has scale infrastructure (ePA) and the only clean reimbursement (DiGA, but MDR-gated); Netherlands has excellent data rails (MedMij) but no app reimbursement → self-pay/B2B2C; Austria emerging; Switzerland weakest infra + outside EHDS. If ditto ever wants SHI reimbursement, the DiGA-via-MDR path in DE is the route — a deliberate, separate, regulated product track (Sections 5–6).

---

## Top 5 policy facts that most change product strategy

1. **MDR Rule 11 / MDCG 2019-11 intended-purpose line** decides everything: information/summarization tools whose output stays with the patient can avoid MDR; clinical decision support cannot, and is class IIa+ requiring CE marking. — [MDCG 2019-11](https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf); [NAMSA](https://namsa.com/resources/blog/eu-mdr-and-ivdr-classifying-medical-device-software-mdsw/)
2. **AI Act high-risk only applies if ditto is a medical device;** otherwise just Article 50 transparency (live 2 Aug 2026). — [artificialintelligenceact.eu Art. 50](https://artificialintelligenceact.eu/article/50/); [Tandem Health](https://tandemhealth.ai/en/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know)
3. **EHDS (in force 26 Mar 2025) mandates patient data access + portability + cross-border flows by 2029/2031** — a structural tailwind for any patient-data companion. — [EUR-Lex Reg (EU) 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng)
4. **Proxy access already exists nationally:** DE ePA = up to 5 named representatives; NL = DigiD Machtigen (from age 16). ditto's caregiver feature can plug in. — [BSI ePA](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/E-Health/Elektronische-Patientenakte/elektronische-patientenakte.html); [LHV](https://www.lhv.nl/thema/patientengegevens-en-ict/online-inzage-in-het-patientendossier/)
5. **DiGA is the only clean SHI reimbursement path (DE, 61 apps as of 23 Feb 2026) — but requires MDR device status;** NL has no equivalent. Monetization elsewhere = self-pay / B2B2C. — [BfArM DiGA Guide](https://www.bfarm.de/SharedDocs/Downloads/EN/MedicalDevices/DiGA_Guide.html); [MTRC 2026](https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany)

## Uncertain / changing-status items

- **AI Act high-risk deadlines are in flux (Digital Omnibus).** Political agreement reported **7 May 2026** to push standalone high-risk to **~2 Dec 2027** and product-embedded/medical-device AI to **~2 Aug 2028**; **final legislative text not yet confirmed** as of 2026-05-31 (Tier 2/3). Article 50 transparency (Aug 2026) appears unaffected. *Confidence: Medium.*
- **EHDS implementing acts (due ~March 2027)** will define the practical technical/interoperability requirements for patient apps — details not yet published. *Confidence: Medium.*
- **DiGA 2026 reforms** (mandatory AbEM success measurement; remuneration reform effective 1 Apr 2026; IIb scope expansion) are newly in force — real-world impact on listing rates/economics still emerging. *Confidence: Medium.*
- **Netherlands DTx/DiGA-style pathway** is discussed but not concrete; reimbursement remains care-pathway/insurer-discretionary. *Confidence: Medium.*
- **National proxy-access law varies** beyond the well-documented DE/NL mechanics; AT/CH and other markets need per-country legal review. *Confidence: Low-Medium.*

---

## Sources (accessed 2026-05-31)

**Tier 1 — Official EU / national authorities / regulatory guidance**
- EUR-Lex — Regulation (EU) 2025/327 (EHDS): https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng
- European Commission — Electronic cross-border health services (MyHealth@EU): https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en
- European Commission — EHDS Regulation page: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
- HaDEA — EU4Health digital health projects (2025): https://hadea.ec.europa.eu/news/2024-eu4health-work-programme-new-projects-advancing-digital-healthcare-across-eu-2025-12-03_en
- MDCG 2019-11 — Qualification & Classification of Software (MDR/IVDR): https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf
- AI Act Service Desk (European Commission) — Article 50: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50
- GDPR Article 9 (gdpr-info.eu): https://gdpr-info.eu/art-9-gdpr/
- BfArM — DiGA overview: https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/_node.html
- BfArM — DiGA Fast-Track Guide: https://www.bfarm.de/SharedDocs/Downloads/EN/MedicalDevices/DiGA_Guide.html
- BSI (Germany) — Electronic Patient Records (ePA), incl. representative access: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/E-Health/Elektronische-Patientenakte/elektronische-patientenakte.html
- gesund.bund.de — The electronic patient record (ePA): https://gesund.bund.de/en/die-elektronische-patientenakte
- Nictiz — MedMij programme: https://nictiz.nl/wat-we-doen/programmas/medmij/
- Volgjezorg / MedMij — about the PGO: https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij
- LHV — online inzage patiëntendossier (NL proxy/DigiD Machtigen): https://www.lhv.nl/thema/patientengegevens-en-ict/online-inzage-in-het-patientendossier/
- oesterreich.gv.at — ELGA electronic health record: https://www.oesterreich.gv.at/en/themen/gesundheit/elektronisches-gesundheitssystem/elga_elektronische_gesundheitsakte
- EC Digital Building Blocks — Austrian ELGA: https://ec.europa.eu/digital-building-blocks/sites/pages/viewpage.action?pageId=533365925
- Zorginstituut Nederland — standard health care benefit package: https://english.zorginstituutnederland.nl/about-us/working-methods-and-procedures/advising-on-and-clarifying-the-contents-of-the-standard-health-care-benefit-package
- VWS (NL) — Financing and making available of digital health applications in Europe (2025): https://www.zorgakkoorden.nl/documenten/publicaties/2025/251210-vws-financing-and-making-available-of-digital-health-applications-in-europe.pdf

**Tier 2 — Legal / consultancy / academic analysis**
- Arnold & Porter — EHDS published in OJ (2025): https://www.arnoldporter.com/en/perspectives/advisories/2025/03/european-health-data-space-regulation-published
- EY — Regulation 2025/327 establishing EHDS: https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds
- Baker McKenzie — EHDS published, what's next (2025): https://healthcarelifesciences.bakermckenzie.com/2025/03/05/european-health-data-space-regulation-published-whats-next/
- EPR — EHDS implemented over next 4 years: https://www.epr.eu/eu-health-data-space-regulation-to-be-implemented-throughout-the-next-4-years/
- Noerr — The EHDS is on its way: https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview
- IntuitionLabs — EU AI Act high-risk pharma/medical device compliance: https://intuitionlabs.ai/articles/eu-ai-act-pharma-medical-device-compliance
- Tandem Health — EU AI Act for healthcare organisations: https://tandemhealth.ai/en/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know
- MedDeviceGuide — EU AI Act for Medical Devices (2026): https://meddeviceguide.com/blog/eu-ai-act-medical-devices-compliance-guide
- Trilateral Research — AI Act compliance timeline by risk tier: https://trilateralresearch.com/responsible-ai/eu-ai-act-implementation-timeline-mapping-your-models-to-the-new-risk-tiers
- artificialintelligenceact.eu — Article 50 / transparency rules: https://artificialintelligenceact.eu/article/50/ ; https://artificialintelligenceact.eu/transparency-rules-article-50/
- Decomplix — Medical device software under MDR/IVDR: https://decomplix.com/medical-software-mdr/
- NAMSA — Classifying MDSW under MDR/IVDR: https://namsa.com/resources/blog/eu-mdr-and-ivdr-classifying-medical-device-software-mdsw/
- greenlight.guru — Explaining MDCG 2019-11: https://www.greenlight.guru/blog/mdcg-2019-11
- Emergo by UL — MDCG 2019-11 Revision 1: https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful
- Prova Health — DiGA reimbursement in Germany explained: https://www.provahealth.com/insights/diga-reimbursement-germany-guide
- MTRC — GKV report on DiGA utilization (2026); NL telemedicine reimbursement: https://mtrconsult.com/news/gkv-report-utilization-and-development-digital-health-application-diga-care-germany ; https://mtrconsult.com/news/reimbursement-telemedicine-and-digital-care-netherlands
- Secure Privacy — healthcare GDPR / Article 9 guidance: https://support.secureprivacy.ai/article/industry-specific-dpo-guidance-healthcare/
- Adequacy — Health data and the GDPR: https://www.adequacy.app/en/blog/health-data-gdpr-compliance
- PMC — Digital Health Reimbursement Strategies of 8 European Countries (scoping review): https://pmc.ncbi.nlm.nih.gov/articles/PMC10576236/
- JMIR (2025) — Austria/Switzerland EHR interdisciplinary requirements study: https://www.jmir.org/2025/1/e78193/XML

**Tier 3 — News (flagged)**
- Inside EU Life Sciences — Germany changes DiGA rules (Feb 2026): https://www.insideeulifesciences.com/2026/02/03/germany-changes-rules-for-digital-health-applications/
- Travers Smith — EU agrees to delay key AI Act deadlines (2026): https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/
- iamexpat — ePA rollout across Germany (April 2025): https://www.iamexpat.de/expat-info/germany-news/electronic-patient-files-epa-roll-out-across-germany-april-29
