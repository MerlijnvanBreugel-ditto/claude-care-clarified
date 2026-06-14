# M12 — Consumerization & Comprehension: Critical Substantiation

**For:** ditto.care market-research deck "deep dive" overlays
**Prepared:** 2026-06-10 (access date for all URLs: 2026-06-10)
**Scope:** EU/NL patient-facing health-tech. Prefer 2024–2026 data.
**Source tiers:** **T1** = peer-reviewed / official statistics / regulator / primary filings; **T2** = established trade press, company-published research, named-vendor reports; **T3** = blogs, secondary aggregators, opinion — **FLAGGED inline**.
**Confidence:** stated per claim (High / Medium / Low).
**US→EU flag:** ⚑ marks where a finding is US-origin and EU applicability is partial; ✅EU marks EU/NL-native evidence (Doctolib, NHS App, EHDS, EU HTA).

---

## Key takeaways

- **Access/convenience is real and measurable, including in the EU.** Doctolib reports ~80M patient accounts and ~400–500K healthcare professionals across France/Germany/Italy/NL (✅EU); the NHS App passed 40M registered users with 62.3M logins in a single month (Nov 2025) (✅EU); Zocdoc reports 35% of appointments booked within 48 hours and 51% within 4 days in 2025 (⚑US). The shift to self-service, same-day, mobile booking is substantiated, not asserted. **Confidence: High.**
- **Transparency is regulation-driven but uneven.** US "open notes" (21st Century Cures Act, effective Apr 2021) made near-real-time note access the default, and ~91% of hospitals post machine-readable price files — but *substantive* price-file quality and patient usability lag. **Confidence: High (mandate exists); Medium (real-world utility).**
- **Plain language is still largely aspirational, not achieved.** A 2025 systematic review of systematic reviews (29,424 materials, 438 studies) found most patient materials exceed the recommended 6th–8th-grade level, and **readability did not improve from 2001 to 2022.** ~47.6% of EU adults have limited health literacy (NL is best-in-class at ~28.7%). The mandates that "bite" (EU HTA plain-language summaries) are recommended/best-practice, not hard, enforceable text requirements yet. **Confidence: High.**
- **The two slides are reconcilable.** "Comprehension is not built into health *data*" and "plain language is becoming more common" are both true: AI *explainers* are bolted on top of records (Epic's Emmie, ChatGPT Health + Apple Health, Jan 2026 ⚑US), but comprehension is not a native, cross-provider, longitudinal, caregiver-aware, EU-legal property of the record itself. **Confidence: High.**
- **What's genuinely missing (the wedge):** cross-provider aggregation, caregiver/proxy context, EU-legal data handling (GDPR/EHDS), and longitudinal continuity. US tools (Apple Health, ChatGPT Health) lean on a US records ecosystem that does not exist the same way in the EU; EHDS patient-summary exchange only applies from **March 2029.** **Confidence: Medium-High.**
- **Comprehension precedes adherence — but the effect is modest.** Meta-analyses show health literacy is positively but *weakly* associated with adherence (r≈0.14); health-literacy *interventions* raise both literacy (r≈0.22) and adherence (r≈0.16). It's a real precursor, not a silver bullet — frame it as a contributing lever in value-based care. **Confidence: High.**
- **The wearable-style longitudinal data moat is real but softening.** Oura (~$11B valuation, Oct 2025; ~80% subscription renewal) and Whoop (~$10B) show passive longitudinal data + subscription stickiness creates switching costs — but commoditizing hardware, AI aggregators (ChatGPT Health ingesting any source), and patent litigation suggest the moat is now in the *longitudinal data + engagement layer*, not the device. **Confidence: Medium.**

---

## 1. Consumerization — substantiated

### 1(a) Access & convenience: who defines modern scheduling, and what changed

**The shift is measurable across three reference platforms — two of them EU-native.**

**Doctolib (✅EU — France/Germany/Italy/Netherlands).** Doctolib reports ~80M patient accounts and ~400,000 healthcare-professional subscribers across its markets; more recent figures cite 500,000+ professionals across Europe ([MobiHealthNews, 2025](https://www.mobihealthnews.com/news/emea/doctolib-now-used-300000-doctors-and-health-workers-across-europe), T2). It hit €348M ARR in 2024 (+22.5% YoY), with France ~80% of ARR and Germany ~17% (25M patients, 100K professionals) ([Sifted, 2024](https://sifted.eu/articles/doctolib-results-2024), T2). **NL flag:** Doctolib is actively targeting the Dutch market but penetration is still nascent there ([Zorgvisie, 2024](https://www.zorgvisie.nl/doctolib-richt-pijlen-op-nederlandse-markt-2704700w/), T2) — for NL specifically, online booking is fragmented across local players (e.g. Doctena, MijnGezondheid.net/Uw Zorg online portals). **Confidence: High on EU-wide scale; Medium on NL-specific penetration.**

**NHS App (✅EU/UK).** Over 40M registered users; in November 2025 alone the app saw **62.3M logins (+43% vs the prior 12-month monthly average)**, 20.8M GP-record views, 6.6M secondary-care appointments managed, and 6.3M repeat prescriptions ([NHS England, Dec 2025](https://www.england.nhs.uk/2025/12/record-numbers-using-nhs-app-to-manage-health/), T1). 25.0M distinct users logged in over the year to Oct 2025 ([NHS Digital, Oct 2025](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-app-statistics/october-2025), T1). This is the clearest EU-relevant evidence that patients now self-serve scheduling, records and prescriptions in one app.

**Zocdoc (⚑US — directional, not EU).** In its 2025 *What Patients Want* report: **35% of appointments occurred within 48 hours of booking and 51% within 4 days**; 80% of urgent-care visits within 24 hours; 68% of bookings on mobile; 93% of non-mental-health visits in-person ([Zocdoc, 2025](https://www.zocdoc.com/about/news/zocdoc-reveals-evolving-patient-preferences-and-trends-in-third-annual-what-patients-want-report/), T2; [PRNewswire, 2025](https://www.prnewswire.com/news-releases/zocdoc-reveals-evolving-patient-preferences-and-trends-in-third-annual-what-patients-want-report-302637388.html), T2). **What changed in ~2 years:** the centre of gravity moved to *timeliness* (same-day/48-hour expectation), *mobile-first* self-scheduling, and *hybrid* (a swing back to in-person for non-mental-health), away from the pandemic-era video peak.

**Critical note:** Zocdoc is US-only and EU applicability is indirect — cite it as a *consumer-expectation* signal, not an EU market metric. The EU-native anchors are Doctolib and the NHS App.

### 1(b) Transparency / clinical reasoning up front

**Open notes (⚑US, near-universal there).** The 21st Century Cures Act information-blocking rule (effective **5 April 2021**) requires that 8 categories of clinical notes plus test results, medication and referral lists be made available to patients immediately, free, electronically; "blocking" is now unlawful and penalised (OIG final rule, June 2023) ([OpenNotes, ONC Federal Rule](https://www.opennotes.org/onc-federal-rule/), T1/T2; [HIMSS](https://www.himss.org/resources/21st-century-cures-act-part-two-information-blocking-and-interoperability/), T2). Effect: near-real-time note access is the US default. **EU flag:** no single equivalent yet — the closest is EHDS (§2/§3) and national portals; transparency-of-reasoning is patchier in the EU.

**Price transparency (⚑US).** ~91% of US hospitals post a machine-readable price file; ~90.7% posted a file and ~83.1% posted substantial negotiated rates by end-2023 ([AHA, Jan 2024](https://www.aha.org/news/headline/2024-01-05-analysis-91-hospitals-posting-machine-readable-price-transparency-data), T2; [Turquoise Health, 2024](https://turquoise.health/resources/blog/moving-into-2024-state-of-price-transparency), T2). CMS tightened schema/fields for 2024 ([HFMA](https://www.hfma.org/price-transparency/new-guidance-makes-hospital-price-transparency-obligations-more-exacting/), T2). **Critical:** *posting a file* ≠ *patient-usable transparency* — compliance on substantive, comparable rates is weaker and contested, and this is a US-only regime with little direct EU read-through.

### 1(c) Plain language — the reality check (be critical)

**The founder is right: most patient-facing material is still above readable level, and it has not improved.**

- A 2025 **systematic review of systematic reviews** — 24 reviews, **29,424 materials, 438 studies, 1990–2022** — found *all* reviews reported most materials exceed the recommended 6th–8th-grade level, and **readability did not improve between 2001 and 2022** ([Sci Direct / Patient Educ Couns, 2025](https://www.sciencedirect.com/science/article/pii/S0738399125000230), T1). This is the single strongest "still jargon" citation.
- A 2024 systematic review of head-and-neck-cancer patient materials found **none** met the AMA-recommended ≤6th-grade level ([PubMed, 2024](https://pubmed.ncbi.nlm.nih.gov/38900443/), T1).
- **Health-literacy gap (✅EU):** ~47.6% of EU adults have limited (inadequate/problematic) health literacy; range 28.7% (Netherlands, best) to 62.1% (Bulgaria) ([JGIM systematic review/meta-analysis, 2021](https://link.springer.com/article/10.1007/s11606-020-06407-8), T1). Digital health literacy remains low among primary-care users 45+ ([OECD Health at a Glance: Europe 2024](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/health-at-a-glance-europe-2024_bb301b77/b3704e14-en.pdf), T1).

**Where do plain-language mandates actually bite? Less than the hype suggests.**
- **EU HTA Regulation (Reg. (EU) 2021/2282), in force for new oncology medicines & ATMPs from 12 Jan 2025** mandates systematic *patient/clinician consultation* in Joint Clinical Assessments ([European Commission, JCA](https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en), T1; [DIA Global Forum, 2025](https://globalforum.diaglobal.org/issue/august-2025/inside-the-eu-htar-joint-clinical-assessments-lessons-along-the-way/), T2). **Critical caveat:** plain-language summaries are described as *best-practice / recommended* for patient engagement — not (yet) a hard, enforceable text-output requirement in the JCA reports ([MDPI, 2024](https://www.mdpi.com/2001-6689/13/3/38), T1). So this mandate "bites" at the *process* (consult patients) more than the *artifact* (guaranteed lay summary).

**Verdict (critical):** "Plain language" is a *direction of travel and a regulatory aspiration*, not an achieved, widespread reality. The evidence base (decades of unimproved readability + ~half of EU adults with limited literacy) is the strongest part of ditto's thesis. Frame plain language as an **unmet need with regulatory tailwinds**, not as a solved or fast-arriving shift.

---

## 2. Reconciling "comprehension is NOT built into health data" vs "plain language is becoming more common"

**Both slides are correct once you separate the *record* from the *explainer layer*.** Comprehension is being *bolted on* via AI; it is not a native property of the underlying health data. Be critical: concede what already exists, then name the gap.

### What is ALREADY happening (concede this)

- **ChatGPT Health + Apple Health (⚑US, launched Jan 2026).** OpenAI launched a dedicated, isolated "Health" space where users connect medical records, lab results and apps (Apple Health, Function, MyFitnessPal, etc.); patients can upload PDF lab reports and get **plain-language summaries** or visit-prep questions. Data is user-initiated, scoped, and excluded from model training ([OpenAI, Jan 2026](https://openai.com/index/introducing-chatgpt-health/), T1/company; [CNBC, Jan 2026](https://www.cnbc.com/2026/01/07/openai-chatgpt-health-medical-records.html), T2; [MacRumors, Jan 2026](https://www.macrumors.com/2026/01/07/openai-chatgpt-health-apple-health-integration/), T2). Stanford's open-source HealthGPT already let users query Apple Health in natural language ([GitHub, Stanford BDHG](https://github.com/StanfordBDHG/HealthGPT), T2).
- **Patient-portal AI explainers (⚑US).** Epic unveiled **Emmie**, a 24/7 MyChart assistant that **explains lab results in plain language**, suggests screenings and helps schedule; Epic is building ~200 AI features and tools that rewrite clinician communications into plain language ([CNBC, Aug 2024](https://www.cnbc.com/2024/08/21/epic-systems-ugm-2024-ai-tools-in-mychart-cosmos-.html), T2; [CNBC, Aug 2025](https://www.cnbc.com/2025/08/20/epic-ugm-2025-epic-touts-new-ai-tools.html), T2; [Healthcare IT News, 2025](https://www.healthcareitnews.com/news/epic-unveils-ai-agents-showcases-new-foundational-models), T2).
- **LLMs measurably improve readability.** A 2025 cross-sectional study (JMIR) found LLMs significantly improve readability of online patient-education materials ([JMIR, 2025](https://www.jmir.org/2025/1/e69955), T1).

### EU equivalents (✅EU — thinner, later, more legal friction)

- **EHDS (Reg. (EU) 2025/327), in force 26 Mar 2025.** Gives patients fast, free access to and control over their electronic health data EU-wide, cross-border via MyHealth@EU — but **primary-use exchange of patient summaries/ePrescriptions only applies from March 2029**, and images/labs/discharge reports from **2031**; Member States may opt out ([European Commission, EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en), T1; [Council of the EU, Jan 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/01/21/european-health-data-space-council-adopts-new-regulation-improving-cross-border-access-to-eu-health-data/), T1).
- EU citizens already have national portals (NHS App, MijnGezondheid.net / patient portals in NL), but **AI explainer layers comparable to Emmie/ChatGPT Health are not yet broadly deployed**, and GDPR/medical-device rules raise the bar for any AI that interprets records.

### What is STILL genuinely missing (the wedge — be critical)

1. **Cross-provider, longitudinal aggregation.** US tools lean on a relatively connected records ecosystem (Apple Health, Epic) that the EU lacks; EHDS interoperability is years out (2029/2031). A patient's record is still fragmented across GP, hospital, pharmacy, specialists.
2. **Caregiver / proxy comprehension.** Current explainers are single-user and consumer-initiated; they do not natively model a caregiver or family proxy understanding a longitudinal record.
3. **EU-legal handling.** ChatGPT Health/Apple Health are US-centric; GDPR, EHDS, and (for anything advisory) MDR/AI-Act obligations mean a compliant EU comprehension layer is genuinely different, not a copy-paste.
4. **Comprehension as a native record property.** Today, comprehension is an *afterthought layer* (ask an AI to explain a PDF). It is not built into how data is captured, stored, or handed off — which is exactly the gap both ditto slides describe.

**Reconciliation sentence for the deck:** *"Plain-language explainers are proliferating on top of records (Epic Emmie, ChatGPT Health), but comprehension is still not a built-in, cross-provider, caregiver-aware, EU-legal, longitudinal property of health data — it's bolted on, US-centric, and single-user."*

---

## 3. Comprehension → adherence → outcomes, and the data moat

### 3(a) Is comprehension a precursor of adherence? (evidence, with critical framing)

- **Direct association is positive but modest.** A meta-analysis found health literacy positively associated with medication adherence at **r≈0.14**, stronger for non-medication regimens and cardiovascular samples ([Health literacy & adherence meta-analysis, PMC4912447](https://pmc.ncbi.nlm.nih.gov/articles/PMC4912447/), T1; [Patient Educ Couns, 2016](https://www.sciencedirect.com/science/article/abs/pii/S0738399116300416), T1).
- **Earlier systematic review/meta-analysis** in *Value in Health* found low health literacy associated with worse adherence ([Value in Health, 2014](https://www.valueinhealthjournal.com/article/S1098-3015(13)00277-5/fulltext), T1; [PubMed 24619949](https://pubmed.ncbi.nlm.nih.gov/24619949/), T1).
- **Interventions move both.** Health-literacy interventions increased literacy (r≈0.22) *and* adherence (r≈0.16) — i.e. improving comprehension is a *modifiable lever*, not just a correlate (same meta-analysis, PMC4912447, T1).
- **Recent corroboration:** a 2025 study links higher health literacy to better antihypertensive adherence via understanding-the-rationale and self-efficacy ([Scientific Reports, 2025](https://www.nature.com/articles/s41598-025-30399-2), T1).

**Critical framing for value-based care:** comprehension is a *genuine precursor* in the causal chain (understand → adhere → outcome), and it's *modifiable* — but effect sizes are small-to-moderate and vary by disease. Position comprehension as a **necessary-but-not-sufficient upstream lever** that compounds with reminders, cost, and access, rather than as a standalone outcomes driver. This is the honest, defensible claim.

### 3(b) Who builds a wearable-style data moat — and is it real or softening?

**The Oura/Whoop analogy holds at the *longitudinal-data + engagement* layer, not the hardware.**

- **Oura:** ~$11B valuation (Oct 2025 $900M round led by Fidelity, >2x its Dec-2024 $5.2B); ~$1B 2025 revenue (+100% YoY); on pace for >5M paid members in Q2 2026; ~5.5M rings sold; revenue ~80% hardware / 20% subscription ([CNBC, Oct 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html), T2; [Sacra](https://sacra.com/c/oura/), T2; **the5krunner, 2025 — T3, FLAGGED**: [link](https://the5krunner.com/2025/10/06/oura-hits-a-11-billion-valuation-with-explosive-growth/)).
- **Whoop:** ~$10B valuation; published a large longitudinal study combining 300,000+ monthly mental-health surveys from 170,000+ members with ~7.9M days of wearable data (Jul 2025) — a concrete example of *longitudinal passive data* compounding into research/IP value ([healthcare.digital, 2025 — T3, FLAGGED](https://www.healthcare.digital/single-post/oura-whoop-strava-consumer-health-ipo-wave-outlook)).
- **The moat mechanics:** passive longitudinal data → switching costs; subscription drives recurring engagement (Oura's ~80%+ renewal argues against churn); IP enforced via patents (ITC orders vs Ultrahuman; RingConn licensing) ([healthcare.digital — T3, FLAGGED](https://www.healthcare.digital/single-post/oura-whoop-strava-consumer-health-ipo-wave-outlook); CNBC/Sacra above, T2).

**Critical: is the moat real or softening?**
- **Real:** the *longitudinal record itself* (years of passive data + the personalized baseline it enables) is hard to replicate and creates genuine switching costs.
- **Softening:** (1) hardware is commoditizing (Apple Watch, cheap rings); (2) **aggregators erode device lock-in** — ChatGPT Health now ingests *any* connected source, so the value migrates from "who owns the sensor" to "who owns the interpreted, longitudinal, multi-source story"; (3) patent litigation is a sign of defending a *narrowing* hardware edge.

**Read-through for ditto:** the durable moat is **longitudinal, multi-source, comprehension-enriched patient context** — not a device and not a one-off explainer. A health-comprehension layer that accrues a longitudinal, caregiver-aware, EU-compliant understanding of a patient is the analog of Oura's data moat, and it's defensible precisely where the US aggregators are weakest (EU-legal, cross-provider, caregiver).

---

## Deep-dive blocks (ready to embed)

### (a) Scheduling / access shift
Modern patient access is now self-service, mobile-first, and same-day. EU-native Doctolib reports ~80M patient accounts and ~400–500K professionals across FR/DE/IT/NL; the NHS App passed 40M registered users with 62.3M logins in a single month (Nov 2025). In the US, Zocdoc reports 35% of appointments booked within 48 hours and 51% within 4 days (2025), 68% on mobile. The last ~2 years shifted expectations toward *timeliness* and *hybrid* care. (Zocdoc = US directional signal; Doctolib + NHS App = the EU anchors.)
- [Doctolib scale — MobiHealthNews, 2025](https://www.mobihealthnews.com/news/emea/doctolib-now-used-300000-doctors-and-health-workers-across-europe)
- [Doctolib €348M ARR — Sifted, 2024](https://sifted.eu/articles/doctolib-results-2024)
- [NHS App record usage — NHS England, Dec 2025](https://www.england.nhs.uk/2025/12/record-numbers-using-nhs-app-to-manage-health/)
- [NHS App stats — NHS Digital, Oct 2025](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-app-statistics/october-2025)
- [Zocdoc What Patients Want 2025 — Zocdoc](https://www.zocdoc.com/about/news/zocdoc-reveals-evolving-patient-preferences-and-trends-in-third-annual-what-patients-want-report/)

### (b) Plain-language reality check
Plain language is aspirational, not achieved. A 2025 systematic review of systematic reviews (29,424 materials, 438 studies) found most patient materials exceed the recommended 6th–8th-grade level, with no improvement from 2001–2022. ~47.6% of EU adults have limited health literacy (NL best at 28.7%). The EU HTA Regulation (in force for oncology/ATMPs since Jan 2025) mandates patient *consultation* but treats plain-language summaries as best-practice, not a hard output requirement — so mandates bite the process more than the artifact.
- [Readability unchanged 1990–2022 — Patient Educ Couns, 2025](https://www.sciencedirect.com/science/article/pii/S0738399125000230)
- [Head & neck cancer materials, none ≤6th grade — PubMed, 2024](https://pubmed.ncbi.nlm.nih.gov/38900443/)
- [EU low health literacy ~47.6% — JGIM meta-analysis, 2021](https://link.springer.com/article/10.1007/s11606-020-06407-8)
- [Digital health literacy low 45+ — OECD Health at a Glance Europe 2024](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/health-at-a-glance-europe-2024_bb301b77/b3704e14-en.pdf)
- [EU HTA Joint Clinical Assessments — European Commission](https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en)

### (c) Comprehension already happening (critical)
Concede that AI explainers are real: ChatGPT Health (Jan 2026) connects Apple Health and medical records and turns uploaded lab PDFs into plain-language summaries; Epic's Emmie explains lab results in MyChart 24/7. But this is a *bolted-on, US-centric, single-user* layer — comprehension is not native to the record. EU equivalents are thinner and later: EHDS (in force Mar 2025) only exchanges patient summaries from 2029. The unmet need is cross-provider, caregiver-aware, EU-legal, longitudinal comprehension.
- [ChatGPT Health launch — OpenAI, Jan 2026](https://openai.com/index/introducing-chatgpt-health/)
- [ChatGPT Health + medical records — CNBC, Jan 2026](https://www.cnbc.com/2026/01/07/openai-chatgpt-health-medical-records.html)
- [Epic Emmie explains labs in plain language — CNBC, Aug 2024](https://www.cnbc.com/2024/08/21/epic-systems-ugm-2024-ai-tools-in-mychart-cosmos-.html)
- [EHDS patient rights & timeline — European Commission](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)
- [EHDS adopted — Council of the EU, Jan 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/01/21/european-health-data-space-council-adopts-new-regulation-improving-cross-border-access-to-eu-health-data/)

### (d) Comprehension → adherence + data moat (Oura/Whoop)
Comprehension is a real but modest precursor of adherence: health literacy correlates with adherence at r≈0.14, and literacy interventions raise adherence (r≈0.16) — a modifiable upstream lever for value-based care, not a silver bullet. The durable moat looks like wearables': Oura (~$11B, ~80% subscription renewal) and Whoop (~$10B, 7.9M days of longitudinal data) show passive longitudinal data + engagement creates switching costs. But the moat is migrating from hardware (commoditizing; ChatGPT Health ingests any source) to the *interpreted, longitudinal, multi-source* layer — exactly where an EU-legal, caregiver-aware comprehension product can defend.
- [HL ↔ adherence meta-analysis (r≈0.14; interventions r≈0.16) — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4912447/)
- [Low HL → worse adherence — Value in Health, 2014](https://www.valueinhealthjournal.com/article/S1098-3015(13)00277-5/fulltext)
- [HL → antihypertensive adherence — Scientific Reports, 2025](https://www.nature.com/articles/s41598-025-30399-2)
- [Oura $11B valuation/$900M round — CNBC, Oct 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [Oura revenue/members — Sacra](https://sacra.com/c/oura/)
- *(T3, FLAGGED)* [Oura/Whoop moat & Whoop longitudinal study — healthcare.digital, 2025](https://www.healthcare.digital/single-post/oura-whoop-strava-consumer-health-ipo-wave-outlook)

---

## Sources

### T1 — peer-reviewed / official statistics / regulator / primary
- [NHS England — Record numbers using NHS App, Dec 2025](https://www.england.nhs.uk/2025/12/record-numbers-using-nhs-app-to-manage-health/)
- [NHS Digital — NHS App Management Information, Oct 2025](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-app-statistics/october-2025)
- [OpenNotes — ONC Federal Rule (Cures Act open notes)](https://www.opennotes.org/onc-federal-rule/)
- [Patient Educ Couns — Readability of written patient info across 30 years (review of reviews), 2025](https://www.sciencedirect.com/science/article/pii/S0738399125000230)
- [PubMed — Readability of head & neck cancer materials, 2024](https://pubmed.ncbi.nlm.nih.gov/38900443/)
- [JGIM — Prevalence of low health literacy in EU member states (meta-analysis), 2021](https://link.springer.com/article/10.1007/s11606-020-06407-8)
- [OECD — Health at a Glance: Europe 2024](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/health-at-a-glance-europe-2024_bb301b77/b3704e14-en.pdf)
- [European Commission — EU HTA Joint Clinical Assessments](https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en)
- [MDPI — Patient involvement in HTA / lessons for EU JCAs, 2024](https://www.mdpi.com/2001-6689/13/3/38)
- [European Commission — European Health Data Space (EHDS)](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)
- [Council of the EU — EHDS adopted, Jan 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/01/21/european-health-data-space-council-adopts-new-regulation-improving-cross-border-access-to-eu-health-data/)
- [OpenAI — Introducing ChatGPT Health, Jan 2026](https://openai.com/index/introducing-chatgpt-health/)
- [JMIR — LLMs improve readability of patient-education materials, 2025](https://www.jmir.org/2025/1/e69955)
- [PMC — Health literacy & adherence in chronic/acute illness (meta-analysis)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4912447/)
- [Value in Health — Health literacy & medication adherence (review/meta-analysis), 2014](https://www.valueinhealthjournal.com/article/S1098-3015(13)00277-5/fulltext)
- [PubMed — Impact of health literacy on medication adherence, 2014](https://pubmed.ncbi.nlm.nih.gov/24619949/)
- [Patient Educ Couns — Health literacy & treatment adherence, 2016](https://www.sciencedirect.com/science/article/abs/pii/S0738399116300416)
- [Scientific Reports — Health literacy & antihypertensive adherence, 2025](https://www.nature.com/articles/s41598-025-30399-2)

### T2 — established trade press / company-published / named-vendor
- [MobiHealthNews — Doctolib used by 300,000+ professionals across Europe](https://www.mobihealthnews.com/news/emea/doctolib-now-used-300000-doctors-and-health-workers-across-europe)
- [Sifted — Doctolib €348M ARR, 2024](https://sifted.eu/articles/doctolib-results-2024)
- [Zorgvisie — Doctolib targets Dutch market (NL)](https://www.zorgvisie.nl/doctolib-richt-pijlen-op-nederlandse-markt-2704700w/)
- [Zocdoc — What Patients Want (3rd annual), 2025](https://www.zocdoc.com/about/news/zocdoc-reveals-evolving-patient-preferences-and-trends-in-third-annual-what-patients-want-report/)
- [PRNewswire — Zocdoc What Patients Want, 2025](https://www.prnewswire.com/news-releases/zocdoc-reveals-evolving-patient-preferences-and-trends-in-third-annual-what-patients-want-report-302637388.html)
- [HIMSS — 21st Century Cures Act: information blocking & interoperability](https://www.himss.org/resources/21st-century-cures-act-part-two-information-blocking-and-interoperability/)
- [AHA — 91% of hospitals posting machine-readable price files, Jan 2024](https://www.aha.org/news/headline/2024-01-05-analysis-91-hospitals-posting-machine-readable-price-transparency-data)
- [Turquoise Health — State of price transparency, 2024](https://turquoise.health/resources/blog/moving-into-2024-state-of-price-transparency)
- [HFMA — More exacting hospital price-transparency obligations](https://www.hfma.org/price-transparency/new-guidance-makes-hospital-price-transparency-obligations-more-exacting/)
- [CNBC — Epic UGM 2024 AI tools (Emmie) in MyChart](https://www.cnbc.com/2024/08/21/epic-systems-ugm-2024-ai-tools-in-mychart-cosmos-.html)
- [CNBC — Epic UGM 2025 AI tools](https://www.cnbc.com/2025/08/20/epic-ugm-2025-epic-touts-new-ai-tools.html)
- [Healthcare IT News — Epic AI agents & foundational models](https://www.healthcareitnews.com/news/epic-unveils-ai-agents-showcases-new-foundational-models)
- [CNBC — OpenAI ChatGPT Health connects medical records, Jan 2026](https://www.cnbc.com/2026/01/07/openai-chatgpt-health-medical-records.html)
- [MacRumors — ChatGPT Health + Apple Health integration, Jan 2026](https://www.macrumors.com/2026/01/07/openai-chatgpt-health-apple-health-integration/)
- [GitHub StanfordBDHG — HealthGPT (query Apple Health in natural language)](https://github.com/StanfordBDHG/HealthGPT)
- [CNBC — Oura $11B valuation / $900M round, Oct 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [Sacra — Oura revenue/valuation/funding](https://sacra.com/c/oura/)
- [DIA Global Forum — Inside EU HTAR Joint Clinical Assessments, 2025](https://globalforum.diaglobal.org/issue/august-2025/inside-the-eu-htar-joint-clinical-assessments-lessons-along-the-way/)

### T3 — blogs / aggregators / opinion (FLAGGED — corroborate before quoting)
- [healthcare.digital — Oura/Whoop/Strava consumer-health IPO outlook & moat (incl. Whoop longitudinal study), 2025](https://www.healthcare.digital/single-post/oura-whoop-strava-consumer-health-ipo-wave-outlook)
- [the5krunner — Oura $11B valuation growth, 2025](https://the5krunner.com/2025/10/06/oura-hits-a-11-billion-valuation-with-explosive-growth/)

---

*Methodology note: All figures retrieved via web search on 2026-06-10. Where only T3 sources carried a datapoint (Whoop longitudinal-study scale; some moat framing), it is flagged and should be corroborated against Whoop's primary publication before use in investor-facing material. NL-specific online-booking penetration is the weakest evidenced area and is marked Medium confidence — a dedicated NL portal/CBS data pull is recommended before the deck claims hard NL numbers.*
