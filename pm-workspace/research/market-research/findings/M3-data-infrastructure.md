# M3 — Health Data Infrastructure & Data Rights

**Prepared for:** ditto.care (EU/Netherlands patient-facing health-tech; AI appointment summaries → "Living Health Companion")
**Theme:** The "data side" — what infrastructure, standards and rights determine what a patient companion can legally pull, show, and act on.
**Access date for all sources:** 2026-06-10
**Relationship to prior work:** Extends and refreshes `healthcare-life-changing-moments/findings/06-eu-policy-system-context.md` (which already covers EHDS dates, AI Act, MDR, DiGA, proxy basics). This file goes deeper on the **data infrastructure & data-rights** layer (BGZ, MedMij/PGO, Wegiz, ePA adoption, FHIR/EEHRxF, MyHealth@EU, consent/proxy) with 2026-current status. Where the prior file already nailed a fact (e.g. EHDS in force 26 Mar 2025), this file does not re-derive it — it builds on it.

> **Source tiers:** Tier 1 = EU/national gov bodies, EUR-Lex, gematik, Nictiz/MedMij, VWS/datavoorgezondheid, HL7 Europe. Tier 2 = reputable legal/consultancy/analyst/academic. Tier 3 = news/blog (FLAGGED). Confidence tags note where status is fast-moving.

---

## Key takeaways

1. **The legal mandate to give patients their own data exists and is hardening — but the usable rails are national, not EU-wide, until 2029+.** EHDS is in force (26 Mar 2025); patient access + cross-border Patient Summaries/ePrescriptions only become mandatory **March 2029**, images/labs/discharge reports **March 2031**, with implementing acts (incl. the FHIR-based exchange format) due **~early 2027** ([EC EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en); [HL7 Europe, 2026](https://hl7news.hl7.org/2026/01/02/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/)). **For ditto's 2026–2028 roadmap, integrate national systems (NL MedMij/PGO, DE ePA) — do not wait for EHDS.** *Confidence: High.*

2. **The Netherlands is structurally ideal but adoption is the weak link.** The legal right to a PGO has existed since 1 July 2020; the **BGZ (Basisgegevensset Zorg)** — a ~26-zib FHIR "patient summary" — is now fully exchangeable to PGOs, and the **Wegiz** law is making BGZ exchange between institutions mandatory (phasing through 2025–2026). But **PGO end-user adoption remains very low** despite the rails being built ([Nictiz BgZ](https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/); [datavoorgezondheid Wegiz/BgZ](https://www.datavoorgezondheid.nl/onderwerpen/w/wegiz/focus-op-vijf-gegevensuitwisselingen/basisgegevensset-zorg-bgz); [Berenschot, 2025, T2](https://www.berenschot.nl/artikelen/pgo-s-in-beweging-bouwen-aan-vertrouwen-en-gebruik)). **The infrastructure is a tailwind; the adoption gap is ditto's opportunity AND its risk.** *Confidence: High on infra; Medium on exact adoption %.*

3. **Germany has near-universal coverage but near-zero active use — the same gap, larger scale.** ePA "für alle" (opt-out) auto-created records for ~70M insured; mandatory provider use began Oct 2025. Yet only **~3.6% of insured actively use** their ePA as of early 2026 ([Joep Lange Institute, 2026, T2](https://www.joeplangeinstitute.org/data_and_health/electronic-patient-record-germany/)). A companion that makes the record *worth opening* addresses the single biggest unsolved problem in both flagship national systems. *Confidence: Medium-High (numbers fast-moving).*

4. **FHIR is the lingua franca across all three layers** — Dutch zibs/BgZ profiles, German MIOs, and the EU's EEHRxF are all HL7 FHIR-based ([HL7 Europe, 2026](https://hl7news.hl7.org/2026/01/02/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/); [gematik MIO](https://www.ina.gematik.de/themenbereiche/medizinische-informationsobjekte); [Nictiz BgZ](https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/)). Building ditto's data model on FHIR (BgZ/IPS profiles) is the safe, future-proof bet — it maps onto national systems today and EHDS later. *Confidence: High.*

5. **Proxy / caregiver access is a first-class, legally-supported feature in NL, DE and now EHDS itself.** EHDS Art. 4(2) explicitly recognizes "digital representatives"; NL runs national proxy via DigiD Machtigen (own PGO from 16; parents view-only for 16–17; full proxy via authorization); DE ePA allows named representatives ([EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng); [PGO.nl FAQ](https://www.pgo.nl/veelgestelde-vragen-pgo/); [MedMij](https://medmij.nl/zorggebruikers/vragen-van-zorggebruikers/)). ditto's loved-one use-case rides existing plumbing. *Confidence: High for NL/DE; High for EHDS recognition.*

6. **Consent is layered and patient-controlled by design — a constraint that doubles as a trust feature.** EHDS gives patients rights to restrict/partition access (Art. 8), opt out of primary use where a Member State legislates it (Art. 10), and opt out of secondary use anytime (Art. 71). GDPR Art. 9 explicit consent remains ditto's practical lawful basis. Granular consent UX is mandatory plumbing — and a differentiator. *Confidence: High.*

7. **Net read: strong, dated tailwinds on rights/standards; the binding near-term constraints are (a) low end-user adoption of the very rails ditto depends on, and (b) per-country integration cost.** EHDS removes the "will the data be available?" question on a multi-year horizon; it does not solve "will patients open the app?" — which is ditto's actual job. *Confidence: High.*

---

## 1. EHDS — the data-rights backbone (2026 status)

EHDS is **Regulation (EU) 2025/327**, in force since 26 March 2025 (covered in file 06). The 2026-relevant detail for a data companion is the **staging and what "primary use" concretely grants the patient**:

**Timeline (refreshed June 2026):**
- **April 2026** — first implementing act adopted, establishing the **EHDS Board**; "the implementation marathon has begun" ([Kennedys, 2026, T2](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-healthcare-medtech-and-life-sciences/)).
- **By Jan 2026** — providers/EHR vendors expected to begin certifying systems for interoperability/security under emerging standards (transition activity, not yet a hard mandate) ([Healthy Europe, 2026, T2/T3](https://healthyeurope.eu/european-health-data-space/)).
- **~March 2027** — key **implementing acts due**, including detailed operational rules and the European EHR Exchange Format (EEHRxF) specs ([EC EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en); [HL7 Europe, 2026](https://hl7news.hl7.org/2026/01/02/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/)).
- **March 2029** — primary use: cross-border exchange of **Patient Summaries + ePrescriptions/eDispensations** mandatory in all Member States; most secondary-use rules also start ([EC EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)).
- **March 2031** — second priority categories: **medical images, lab results, hospital discharge reports**, plus remaining secondary-use categories (e.g. genomic) ([EC EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)).

**What primary use grants a patient (and their chosen app).** Member States must establish **electronic health data access service(s)** so individuals can access their own data and exercise Articles 3, 5–10 ([Noerr, 2025, T2](https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview); [EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng)). Concrete rights relevant to ditto:
- **Access own data** and **data portability** across providers/borders (Arts. 3, 5–7).
- **Restrict access** fully or partially to specific data (Art. 8).
- **Opt out of primary use** where a Member State legislates it, with a vital-interests override for professionals (Art. 10) ([Aridhia, 2025, T2](https://www.aridhia.com/blog/ehds-patient-consent-and-the-expectations-on-secure-processing-environment-providers/)).
- **Appoint digital representatives** who can also obtain access (Art. 4(2)) — the legal hook for caregiver/proxy features (see §6).
- **Opt out of secondary use** anytime, no reason needed (Art. 71).

**Tailwind/Constraint: TAILWIND (structural, dated). Near-term constraint = timing.** EHDS guarantees the data must be made available to the patient and their apps — but the binding cross-border dates are 2029/2031, so ditto's 2026–2028 product must ride national rails. *Confidence: High.*

---

## 2. Netherlands — PGO/MedMij, BGZ, and Wegiz

### 2.1 PGO & MedMij (the patient-facing rail)
A **PGO (Persoonlijke GezondheidsOmgeving)** is the patient-facing app/portal to view, manage and share one's own health data. **MedMij** is the Dutch trust framework + information standard governing secure citizen↔provider exchange; a **MedMij label** certifies a PGO meets strict security/interoperability requirements so providers will release data to it ([MedMij, "Wat is een PGO"](https://medmij.nl/wat-is-een-pgo/); [Volgjezorg/MedMij EN](https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij)). **Nictiz** develops/maintains the underlying information standards (zibs and BgZ).

- **Legal right since 1 July 2020:** every Dutch resident has the right to electronic access to their own records via a PGO ([Rijksoverheid](https://www.rijksoverheid.nl/onderwerpen/digitale-gegevens-in-de-zorg/vraag-en-antwoord/waar-kan-ik-een-persoonlijke-gezondheidsomgeving-pgo-voor-gebruiken)).
- **March 2025:** VWS selected three PGO providers — **Curavista, Health Cloud Initiative (HCI), Topicus** — to consolidate/support the market ([datavoorgezondheid, 2025](https://www.datavoorgezondheid.nl/onderwerpen/p/persoonlijke-gezondheidsomgeving)).
- **Adoption is the problem, not the plumbing.** Most GPs are connected; many hospitals/long-term-care/mental-health orgs participate — but **end-user uptake remains low** and is moving slowly ([Berenschot, 2025, T2](https://www.berenschot.nl/artikelen/pgo-s-in-beweging-bouwen-aan-vertrouwen-en-gebruik); [PGO.nl](https://www.pgo.nl/)). *Exact active-user counts not reliably published; treat any single number with caution.* **This is precisely the comprehension/engagement gap ditto targets.**

### 2.2 BGZ — Basisgegevensset Zorg (get this right)
**What it is.** The **BgZ (Basisgegevensset Zorg / "Basic Healthcare Dataset")** is the **minimal set of patient data relevant across specialisms, disease types and professional groups, important for continuity of care** — effectively a Dutch **patient summary** ([Nictiz BgZ](https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/); [Registratie aan de bron](https://www.registratieaandebron.nl/basisgegevensset-zorg)). It is **not** an app or a network — it is a **clinical dataset standard / information standard**.

**How it's built.** The BgZ is assembled from **zibs (zorginformatiebouwstenen / healthcare information building blocks)** — standardized, reusable clinical data units. The set comprises on the order of **~26 zibs**, all of which have been **technically developed as HL7 FHIR profiles** ([Nictiz, "Informatiestandaard BgZ-uitwisseling med-spec zorg klaar"](https://nictiz.nl/nieuws/informatiestandaard-bgz-uitwisseling-medisch-specialistische-zorg-klaar/)). *Note: the exact zib count varies slightly by release (sources reference 26–28); treat "~26" as indicative, not exact. Confidence: Medium on precise count.*

**Representative content** (illustrative, not exhaustive): Patient demographics, Problems/diagnoses, Allergies/intolerances, Medication, Procedures (verrichtingen), Treatment instructions, Lab results, Medical devices/implants, Functional status, Vaccinations, Contact details of providers ([Nictiz BgZ](https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/); [datavoorgezondheid BgZ](https://www.datavoorgezondheid.nl/onderwerpen/w/wegiz/focus-op-vijf-gegevensuitwisselingen/basisgegevensset-zorg-bgz)). For several core zibs (Patient, Problem, Allergy, Procedure, Treatment instructions, Lab result) a guideline specifies the minimum that must be documented ([Nictiz news](https://nictiz.nl/nieuws/informatiestandaard-bgz-uitwisseling-medisch-specialistische-zorg-klaar/)).

**Relationship to IPS (international).** The BgZ is the Dutch national analogue of the **International Patient Summary (IPS)**; mapping work between BgZ and IPS exists, which matters for EHDS cross-border Patient Summaries ([de Graauw, 2023, T3 blog — FLAGGED](https://www.marcdegraauw.com/2023/10/16/van-basisgegevensset-zorg-naar-international-patient-summary/)).

**BgZ → PGO.** Nictiz/MedMij have made the **full BgZ exchangeable with PGOs** — meaning a patient's complete BgZ can be retrieved into their personal health environment, not just fragments ([Nictiz, "Volledige BgZ geschikt voor uitwisseling met PGO's"](https://nictiz.nl/nieuws/volledige-basisgegevensset-zorg-geschikt-gemaakt-voor-uitwisseling-met-persoonlijke-gezondheidsomgevingen/)). *Exact go-live date of "full BgZ to PGO" not confirmed from a primary page (Nictiz blocked direct fetch); the capability is current as of 2025–2026. Confidence: Medium on precise date, High on the capability existing.*

### 2.3 Wegiz — the law forcing exchange
**Wegiz (Wet elektronische gegevensuitwisseling in de zorg)** has been in force since **July 2023**; it requires that designated electronic data exchanges become standardized and (eventually) mandatory, implemented via NEN standards ([wetten.overheid.nl, Wegiz](https://wetten.overheid.nl/BWBR0048095/2025-07-05/0/informatie); [Eldermans|Geerts, 2025, T2](https://www.eldermans-geerts.nl/de-wegiz-wat-is-de-stand-van-zaken/)). Wegiz prioritizes **five data exchanges**: BgZ, image availability + reports, nursing handover (eOverdracht), medication transfer, and acute-care data exchange ([datavoorgezondheid, Wettelijk kader](https://www.datavoorgezondheid.nl/themas/wat-er-in-de-wet-staat)).

**Status 2025–2026 (fast-moving):**
- **Electronic prescribing** mandatory since **1 Jan 2024** (NEN 7503) ([datavoorgezondheid](https://www.datavoorgezondheid.nl/themas/wat-er-in-de-wet-staat)).
- **BgZ exchange between medical-specialist institutions:** targeted to become mandatory (NEN 7540/related), with implementation support from early 2025 and the digital-exchange obligation phasing in **~2025–2026**; institutions can implement earlier if their EPD/EHR vendor supports it ([ictrecht, T2](https://www.ictrecht.nl/blog/databeschikbaarheid-een-update-over-gegevensuitwisseling-en-acute-zorg); [ICT&health, NFU, T2/T3](https://icthealth.nl/nieuws/nfu-vanaf-2025-ondersteuning-voor-uitwisseling-bgz)). *Exact mandatory date is moving; treat "BgZ mandatory ~2025/2026" as directional. Confidence: Medium.*
- **Medication transfer** following in 2026; **nursing handover (eOverdracht)** decree targeted for H2 2026, in force ~1 Jan 2027 ([ictrecht](https://www.ictrecht.nl/blog/databeschikbaarheid-een-update-over-gegevensuitwisseling-en-acute-zorg)).
- **Wegiz + EHDS reinforce each other** — Wegiz builds the national exchange capability that EHDS will require ([ICT&health, 2024, T2](https://www.icthealth.nl/magazine/editie-6-2024/wegiz-en-ehds-versterken-elkaar)).

**Tailwind/Constraint: STRONG TAILWIND on infrastructure (NL is among Europe's most advanced on patient-data standards), with a LOW-ADOPTION CONSTRAINT.** ditto can pull a standardized, FHIR-native BgZ into a MedMij-certified PGO with consent — but few patients currently use PGOs, so distribution/engagement is the real battle. *Confidence: High on infra, Medium on adoption specifics.*

---

## 3. Germany — ePA "für alle", gematik, MIOs

**ePA "für alle" (opt-out) status (refreshed June 2026):**
- Opt-out model launched **Jan 2025**; records auto-created for **~70M** statutory-insured unless they opted out; nationwide rollout from late April 2025; **mandatory provider use from 1 Oct 2025** (doctors/HCPs obliged to fill the record) ([gesund.bund.de ePA](https://gesund.bund.de/en/die-elektronische-patientenakte); [Versicherungsbüro Weiss, T2/T3](https://www.versicherungsbuero-weiss.com/blog/electronic-patient-records-epa-in-germany)).
- **Active usage is the headline problem:** as of **early 2026, ~3.6% of insured actively use** their ePA (logging in, uploading, sharing), up only ~1 point since mid-2025 — far below the ~61% pre-launch intent and officials' hopes ([Joep Lange Institute, 2026, T2](https://www.joeplangeinstitute.org/data_and_health/electronic-patient-record-germany/)). A 2025 survey found ~48% feel digital health tools are too complex ([Joep Lange Institute, 2026, T2](https://www.joeplangeinstitute.org/data_and_health/electronic-patient-record-germany/)). *Numbers are fast-moving; confidence Medium-High.*

**gematik & the standards.** **gematik** operates the telematics infrastructure (TI) and authors Germany's national FHIR specs. The ePA is populated by **MIOs (Medizinische Informationsobjekte)** — FHIR-based, terminology-bound clinical objects mandated under §355 SGB V ([gematik MIO/INA](https://www.ina.gematik.de/themenbereiche/medizinische-informationsobjekte)). The ePA "für alle" exposes documents via an **IHE ITI MHD-compatible interface** over XDS, with metadata + full-text search ([gematik ePA MHD IG](https://www.gematik.de/fhir/epa-mhd/1.1.0); [gematik ePA Basisfunktionalitäten](https://gemspec.gematik.de/ig/fhir/epa/1.1.5/index.html)). For ditto, this means a **documented FHIR/IHE integration surface** for any German ePA-connected feature.

**Tailwind/Constraint: TAILWIND (universal coverage + documented FHIR/IHE rails) crippled by a USAGE CONSTRAINT.** The German market hands ditto ~70M records that almost nobody opens — the clearest possible statement of the "data exists, comprehension/engagement doesn't" problem ditto exists to solve. *Confidence: Medium-High.*

---

## 4. FHIR / interoperability standards (the through-line)

**FHIR (HL7 Fast Healthcare Interoperability Resources) is the common substrate across all three layers ditto cares about:**
- **NL:** zibs and the full BgZ are implemented as **HL7 FHIR profiles**; MedMij exchange = FHIR ([Nictiz BgZ](https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/)).
- **DE:** MIOs and the ePA interfaces are **FHIR + IHE** ([gematik MIO](https://www.ina.gematik.de/themenbereiche/medizinische-informationsobjekte)).
- **EU:** the **European EHR Exchange Format (EEHRxF)** is **FHIR-based**; HL7 Europe published **three new FHIR Implementation Guides in Nov 2025** (after summer-2025 balloting) to support EHDS, feeding the Commission's EEHRxF implementing acts expected **~early 2027** ([HL7 Europe, 2026](https://hl7news.hl7.org/2026/01/02/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/); [Frontiers, 2025, T2](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1648170/full)).
- **Governance:** the **European Standards for Health Interoperability Alliance (ESHIA)** is forming (2025) to steward EHDS standards and inherit the EHRxF Hub when the xShare project's funding ends Nov 2026 ([Frontiers, 2025, T2](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1648170/full)).

**Implication:** Build ditto's internal data model on **FHIR (BgZ/IPS profiles + national extensions)**. It maps onto NL and DE today and onto EEHRxF later — minimizing rework as EHDS lands. Investment in FHIR/IPS mapping is durable. *Confidence: High.*

**MyHealth@EU** (cross-border operational layer) — refreshed: 13 Member States live with ≥1 service (Czechia, Estonia, Greece, Finland, France, Croatia, Ireland, Lithuania, Luxembourg, Latvia, Malta, Poland, Portugal); a 2025 wave adds Austria, Cyprus, Denmark, Hungary, Iceland, Italy, Norway, Romania, Sweden, Slovenia; **Slovakia joins 2026**; Romania/Denmark beginning imaging/lab/discharge and NCP work from 2026 ([EC cross-border health services](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en)). EHDS makes participation + priority flows mandatory by 2029/2031. *Confidence: High on roster, Medium on exact 2026 dates.*

---

## 5. Consent management

EHDS makes patient control of access a design requirement, not an afterthought:
- **Granular restriction (Art. 8):** patients can restrict access to all or part of their data — implying data partitioning/sensitivity handling in any connected app ([Noerr, 2025, T2](https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview)).
- **Primary-use opt-out (Art. 10):** where a Member State legislates it, reversible, with vital-interests override ([Aridhia, 2025, T2](https://www.aridhia.com/blog/ehds-patient-consent-and-the-expectations-on-secure-processing-environment-providers/)).
- **Secondary-use opt-out (Art. 71):** anytime, no reason needed.
- **GDPR layer (unchanged):** health data is Art. 9 special-category; ditto's practical lawful basis as a patient-facing app is **explicit consent (Art. 9(2)(a))**, cumulative with an Art. 6 basis (see file 06 §4).
- **National framework (NL):** MedMij/Volgjezorg already operate a consent-registration layer ("toestemming") so providers know whether they may release data ([Volgjezorg/MedMij](https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij)).

**Implication:** ditto must build **granular, revocable, auditable consent UX** as core plumbing. This is a constraint that doubles as a **trust differentiator** in a market where privacy anxiety is a top adoption barrier (DE: ~48% find tools too complex / privacy-anxious — §3). *Confidence: High.*

---

## 6. Proxy / caregiver access rights

Caregiver/loved-one access — central to ditto's "Living Health Companion" — is **legally supported at every level**:

- **EHDS (EU):** Art. 4(2) explicitly recognizes **digital representatives** who can obtain data access; access services must be **free of charge for individuals and their representatives** ([EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng); [EY, 2025, T2](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds)).
- **Netherlands (DigiD Machtigen):**
  - From **age 16** a person can create their own PGO and retrieve their own data ([PGO.nl FAQ](https://www.pgo.nl/veelgestelde-vragen-pgo/); [MedMij](https://medmij.nl/zorggebruikers/vragen-van-zorggebruikers/)).
  - For **16–17 year-olds**, an authorized parent can **view (not retrieve)** the data in the PGO.
  - Adults authorize a representative via **DigiD Machtigen** (announced in advance at machtigen.digid.nl), letting a family member/caregiver manage data on their behalf ([PGO.nl FAQ](https://www.pgo.nl/veelgestelde-vragen-pgo/)).
  - *Note: full caregiver/guardian (mantelzorger) proxy flows are still being expanded ("can be arranged in the future") — some scenarios are not yet fully operational. Confidence: Medium on the breadth of currently-live caregiver scenarios.*
- **Germany (ePA):** the insured can nominate **representatives** who use their own ePA app to manage (not delete) the record; the patient retains visibility/control (see file 06 §4 for the up-to-5-representatives detail) ([gesund.bund.de](https://gesund.bund.de/en/die-elektronische-patientenakte)).

**Tailwind/Constraint: TAILWIND.** ditto's caregiver feature plugs into existing national proxy rails and is now reinforced by EHDS recognition of digital representatives — rather than inventing a bespoke (and legally fragile) consent scheme. Per-country variation (and not-yet-live NL caregiver flows) is the integration cost. *Confidence: High on legal support; Medium on which flows are live today.*

---

## 7. What this means for a patient-facing comprehension companion

**Tailwinds**
- **Right-to-access is law and hardening** (PGO since 2020; EHDS access services; Wegiz forcing BgZ exchange) — the data *must* be made available to the patient and their chosen app. ditto isn't fighting for access; it's building on a mandated right.
- **A ready-made, FHIR-native "patient summary" exists in NL (BgZ) and DE (MIOs/ePA)** — ditto can ingest a structured clinical summary rather than scraping PDFs.
- **The flagship national systems have a comprehension/engagement vacuum** (DE ~3.6% active use; NL PGO uptake low). A tool that makes the record understandable and worth opening attacks the exact gap governments have failed to close.
- **Proxy/caregiver access is legally blessed at EU + national level** — directly enabling the "Living Health Companion for me and my loved ones" vision.
- **FHIR everywhere** means one durable data model maps onto NL, DE, and future EHDS.

**Constraints**
- **EHDS cross-border data is 2029/2031** — near-term ditto must integrate national systems (MedMij/PGO in NL, ePA/gematik in DE), each with its own certification, FHIR profiles, and consent rails. Integration cost is real and per-country.
- **MedMij certification is a gate** to pulling Dutch data into a PGO-class app — a deliberate compliance/engineering investment.
- **Low end-user adoption of PGO/ePA** means ditto can't assume patients already have data flowing; onboarding may need to drive ePA/PGO activation itself.
- **Granular consent + sensitivity partitioning + audit logging** are mandatory plumbing (EHDS Art. 8; GDPR Art. 9), not optional.
- **Standards are still being finalized** (EEHRxF implementing acts ~2027; NL Wegiz BgZ mandatory dates moving; HL7 Europe IGs fresh as of Nov 2025) — build to FHIR but expect profile churn.
- **Adoption-gap risk cuts both ways:** the same low uptake that is ditto's opportunity is also a market-education burden ditto inherits.

**Strategic read.** The data infrastructure is a **multi-year structural tailwind** that progressively removes the "is the data available?" question. The binding near-term work is (1) **national FHIR integrations** (NL BgZ/MedMij first, DE ePA second), (2) **first-class consent + proxy UX**, and (3) **owning the comprehension/engagement layer** that both NL and DE systems conspicuously lack. ditto's thesis — that the bottleneck is *understanding and using* health data, not *accessing* it — is strongly corroborated by the DE ~3.6% active-use figure and low NL PGO uptake. *Confidence: High on direction; Medium on specific adoption numbers (fast-moving).*

---

## Uncertain / fast-moving items

- **Exact PGO active-user counts (NL)** — not reliably published; adoption qualitatively low. *Confidence: Medium.*
- **ePA active-use % (DE)** — ~3.6% early 2026 per a single T2 source; verify against gematik/BMG official figures before quoting externally. *Confidence: Medium.*
- **BgZ zib count** — sources say ~26 (some 26–28); confirm current MedMij release before publishing a precise number. *Confidence: Medium.*
- **Wegiz BgZ mandatory date** — phasing through 2025–2026; exact mandatory date moving. *Confidence: Medium.*
- **"Full BgZ to PGO" go-live date** — capability confirmed, exact date not (Nictiz pages blocked direct fetch). *Confidence: Medium.*
- **EEHRxF implementing acts** — expected ~early/March 2027; specs not final. *Confidence: Medium.*
- **NL caregiver (mantelzorger) proxy flows** — some scenarios "to be arranged in future," not all live. *Confidence: Medium.*

---

## Sources (accessed 2026-06-10)

**Tier 1 — EU/national gov bodies, gematik, Nictiz/MedMij, VWS, HL7 Europe, EUR-Lex**
- EUR-Lex — Regulation (EU) 2025/327 (EHDS): https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng
- European Commission — EHDS Regulation page (timeline, implementing acts): https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
- European Commission — Electronic cross-border health services (MyHealth@EU roster): https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en
- Nictiz — Informatiestandaard Basisgegevensset Zorg (BgZ): https://www.nictiz.nl/informatiestandaarden/basisgegevensset-zorg/
- Nictiz — Informatiestandaard BgZ-uitwisseling medisch-specialistische zorg klaar (zibs/FHIR detail): https://nictiz.nl/nieuws/informatiestandaard-bgz-uitwisseling-medisch-specialistische-zorg-klaar/
- Nictiz — Volledige BgZ geschikt voor uitwisseling met PGO's: https://nictiz.nl/nieuws/volledige-basisgegevensset-zorg-geschikt-gemaakt-voor-uitwisseling-met-persoonlijke-gezondheidsomgevingen/
- datavoorgezondheid (VWS) — Wegiz / focus op vijf gegevensuitwisselingen / BgZ: https://www.datavoorgezondheid.nl/onderwerpen/w/wegiz/focus-op-vijf-gegevensuitwisselingen/basisgegevensset-zorg-bgz
- datavoorgezondheid (VWS) — Wetten en regels: https://www.datavoorgezondheid.nl/themas/wat-er-in-de-wet-staat
- datavoorgezondheid (VWS) — Persoonlijke gezondheidsomgeving (PGO): https://www.datavoorgezondheid.nl/onderwerpen/p/persoonlijke-gezondheidsomgeving
- wetten.overheid.nl — Wet elektronische gegevensuitwisseling in de zorg (Wegiz), BWBR0048095: https://wetten.overheid.nl/BWBR0048095/2025-07-05/0/informatie
- Rijksoverheid — PGO (right to electronic access): https://www.rijksoverheid.nl/onderwerpen/digitale-gegevens-in-de-zorg/vraag-en-antwoord/waar-kan-ik-een-persoonlijke-gezondheidsomgeving-pgo-voor-gebruiken
- MedMij — Wat is een PGO: https://medmij.nl/wat-is-een-pgo/
- MedMij — Vragen van zorggebruikers (proxy/16+): https://medmij.nl/zorggebruikers/vragen-van-zorggebruikers/
- PGO.nl — Veelgestelde vragen (DigiD Machtigen, 16+, parent view-only): https://www.pgo.nl/veelgestelde-vragen-pgo/
- Volgjezorg / MedMij (EN) — about PGO/portals, consent: https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij
- Registratie aan de bron — Basisgegevensset Zorg (BgZ): https://www.registratieaandebron.nl/basisgegevensset-zorg
- gesund.bund.de — The electronic patient record (ePA): https://gesund.bund.de/en/die-elektronische-patientenakte
- gematik — Medizinische Informationsobjekte (MIO), INA: https://www.ina.gematik.de/themenbereiche/medizinische-informationsobjekte
- gematik — ePA MHD Service Implementation Guide v1.1.0 (IHE/FHIR): https://www.gematik.de/fhir/epa-mhd/1.1.0
- gematik — ePA Basisfunktionalitäten v1.1.5: https://gemspec.gematik.de/ig/fhir/epa/1.1.5/index.html
- HL7 Europe — New FHIR Implementation Guides to support EHDS (Nov 2025): https://www.hl7europe.org/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/

**Tier 2 — Legal / consultancy / analyst / academic**
- Kennedys — The EHDS is in force: implications (2026): https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-healthcare-medtech-and-life-sciences/
- Noerr — The EHDS is on its way: an overview (patient rights, Arts. 4/8/10): https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview
- EY (Greece) — Regulation 2025/327 establishing EHDS (digital representatives): https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds
- Aridhia — EHDS, patient consent, secure processing environments: https://www.aridhia.com/blog/ehds-patient-consent-and-the-expectations-on-secure-processing-environment-providers/
- Arnold & Porter — EHDS published in OJ (2025): https://www.arnoldporter.com/en/perspectives/advisories/2025/03/european-health-data-space-regulation-published
- Eldermans | Geerts — De Wegiz: wat is de stand van zaken? (2025): https://www.eldermans-geerts.nl/de-wegiz-wat-is-de-stand-van-zaken/
- ICTRecht — Databeschikbaarheid: update gegevensuitwisseling en acute zorg (Wegiz timeline): https://www.ictrecht.nl/blog/databeschikbaarheid-een-update-over-gegevensuitwisseling-en-acute-zorg
- ICT&health — Wegiz en EHDS versterken elkaar (2024): https://www.icthealth.nl/magazine/editie-6-2024/wegiz-en-ehds-versterken-elkaar
- ICT&health — NFU: vanaf 2025 ondersteuning voor uitwisseling BgZ: https://icthealth.nl/nieuws/nfu-vanaf-2025-ondersteuning-voor-uitwisseling-bgz
- Berenschot — PGO's in beweging: bouwen aan vertrouwen en gebruik (2025; adoption): https://www.berenschot.nl/artikelen/pgo-s-in-beweging-bouwen-aan-vertrouwen-en-gebruik
- Joep Lange Institute — Germany's Electronic Patient Record: From Quiet Launch to Mass Adoption (ePA ~3.6% active, 2026): https://www.joeplangeinstitute.org/data_and_health/electronic-patient-record-germany/
- Frontiers in Medicine (2025) — Accelerating EEHRxF implementation across Europe (FHIR, ESHIA): https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1648170/full
- Versicherungsbüro Weiss — Electronic Patient Records (ePA) in Germany overview: https://www.versicherungsbuero-weiss.com/blog/electronic-patient-records-epa-in-germany

**Tier 3 — News / blog (FLAGGED)**
- Healthy Europe — EHDS update (2026 certification framing) [FLAGGED]: https://healthyeurope.eu/european-health-data-space/
- HL7 News — New HL7 Europe FHIR IGs to support EHDS (Jan 2026) [press/blog, FLAGGED but authoritative]: https://hl7news.hl7.org/2026/01/02/new-hl7-europe-fhir-implementation-guides-to-support-the-european-health-data-space/
- Marc de Graauw — Van BasisGegevensset Zorg naar International Patient Summary (2023) [personal blog, FLAGGED]: https://www.marcdegraauw.com/2023/10/16/van-basisgegevensset-zorg-naar-international-patient-summary/
