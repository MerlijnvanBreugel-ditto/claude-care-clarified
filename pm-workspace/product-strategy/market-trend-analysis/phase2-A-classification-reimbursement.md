# Phase-2A — Device Classification & EU Reimbursement: Resolving the Fork

**Decision-grade deep dive.** Builds on Phase-1 Brief A (regulation) and Brief B (reimbursement); does not repeat them.
**Author:** Senior digital-health regulatory + market-access strategist (Mewtwo research)
**Date:** 2026-05-30 · **Currency:** sources current to late May 2026 · **Geography:** EU, NL-first
**Claim legend:** **[FACT]** sourced · **[INFERENCE]** my reasoning · **[REC]** recommendation · **[EST]** estimate, directional. Source numbers `[n]` map to Section 8.

---

## 1. Executive summary

**The Phase-1 fork was framed on a false premise, and resolving it changes the recommendation.** Phase-1 said crossing into reimbursement means "Class IIa (notified body) AND AI-Act high-risk." That is wrong for the route that matters. **[FACT]** Per the Dutch Ministry of Health's own December-2025 comparative report, **54 of 57 German DiGA (95%) and all 4 French PECAN apps are Class I medical devices — not assessed by a notified body** [1]. Germany's DiGA does **not** require Class IIa. It requires a **CE-marked Class I *or* IIa** device plus a study showing a positive care effect [2][12]. So Ditto can, in principle, become a reimbursed German DiGA **while staying Class I and outside the AI-Act high-risk regime.** The genuine cost wall is the **clinical study and ongoing evidence burden**, not a notified-body certificate.

**The Mika precedent is more cautionary than Phase-1 implied — it is the strategic headline of this brief.** **[FACT]** Mika (Fosanis) was Germany's 12th DiGA, listed **24 Mar 2021** as a *provisional* listing, for three gynaecological cancers, on the **structural-and-procedural-improvement** track [3][6]. It **never converted to permanent**. It withdrew once in **Mar 2022** and again in **Feb 2024**, each time to gather stronger RCT evidence rather than risk a rejection that would force a one-year re-application bar [4][7][8]. Its published waitlist RCT (n=218, 12 weeks) hit distress, anxiety, depression and fatigue but **missed quality-of-life** [5]. In **Jun 2025 Fosanis sold the Mika assets to US firm Outcomes4Me** [9]. The "near-exact precedent" is therefore a company that spent ~4 years chasing permanent DiGA status, never got it, and exited. **[FACT]** The second oncology precedent, **CANKADO PRO-React Onco** (Class I, structural/procedural track, listed May 2021), was **struck from the directory on 21 Apr 2023** [10][11]. **As of May 2026 there is no live, permanently-listed oncology companion DiGA.** [INFERENCE] The oncology-companion DiGA thesis is real but **unproven at the permanent-listing finish line** — every attempt so far has stalled or exited.

**Three feature decisions control Ditto's regulatory class, and they are entirely in Ditto's hands.** The line is set by *intended purpose* under MDR Rule 11 / MDCG 2019-11, not by the underlying tech. Plain-language summarising and family sharing stay **Class I / out-of-scope**; the moment a feature outputs **scores, flags, prioritised actions, triage, or treatment/question recommendations the patient acts on**, it defaults to **Class IIa** and pulls in AI-Act high-risk [13][14][16]. The "care intelligence layer" is exactly where this tips.

**The recommendation: light-now, clinical-later — but pick the *Dutch* clinical-later, not the German one.** [REC] Stay Class I and monetise via the **Dutch B2B route** (hospital/insurer-funded inside care tariffs and IZA transformation money) for the next 12–18 months. In parallel, position for the **emerging Dutch "diga.nl" provisional-reimbursement-plus-research scheme** that VWS formally recommended building in Dec 2025 [1] — a home-market, Class-I-friendly path that did not exist when the Mika thesis was written. Treat German DiGA as an option to **buy later with a single tight oncology indication**, not the near-term plan.

---

## 2. Feature-by-feature classification map

The controlling question for every feature (MDCG 2019-11 / MDR Rule 11): *does the software output information that a patient or clinician uses to take a diagnostic or therapeutic decision?* If no → Class I or out-of-scope. If yes → Class IIa by default (IIb/III if the decision could cause serious/irreversible harm) [13][14][16]. "Information" explicitly includes **scores, gradings, classifications, recommended actions, priority flags, alerts** [14].

| Ditto feature | What it outputs | Likely class | Why (the controlling logic) | The decision that controls the line |
|---|---|---|---|---|
| **Visit summary** (transcribe consult → plain-language recap) | Reformatted record of what was said | **Class I / arguably out-of-scope** | Reformatting/presenting information *already given by the clinician* is "all other software" under Rule 11 — not new information used to take a decision [14][16] | Keep it a faithful recap. The instant it *adds* clinical interpretation ("this likely means X") it becomes decision-support → IIa |
| **Suggested questions for next appointment** | Generic prompts to ask the doctor | **Class I** (borderline) | Helps the patient communicate; does not tell them what to *do* clinically | Keep questions generic/communication-oriented. Condition-specific "you should ask about switching to drug Y" drifts toward therapeutic recommendation → IIa |
| **Appointment prep** (logistics, what to bring, prior summaries) | Organisational/admin support | **Class I / out-of-scope** | Administrative + information retrieval; MDCG explicitly excludes pure admin/comms software [16] | Stays safe as long as it's logistics, not symptom-triage |
| **Family / care-circle sharing** | Distributes the summary to chosen recipients | **Class I / out-of-scope** (device-wise) | Communication/storage function — not a medical purpose. *Real* risk is GDPR consent, not MDR [Brief A §Q4] | Not a classification lever; it's a consent-design problem |
| **Symptom logging shown back to patient** | Patient's own entries, displayed | **Class I** | Display of patient-entered data without interpretation = monitoring without decision-support | If Ditto *interprets* the log ("your symptoms suggest you should contact your team") → triage → **IIa** (the CANKADO line) |
| **"Care intelligence layer" — passive aggregation** (one timeline of records, history, summaries) | Organised view of the patient's own data | **Class I** (likely) | Aggregation/portability of the patient's record, no new clinical conclusion. EHDS makes this a first-class data object | Stays Class I if it *shows* and *organises* only |
| **"Care intelligence layer" — active intelligence** (flags, "ask about this", risk surfacing, drug-interaction or guideline alerts, prioritisation) | Scores, flags, recommended actions | **Class IIa** (→ AI-Act high-risk) | This is *exactly* the Rule-11 trigger list. MDCG Rev.1 extends it to prognosis/prevention framing too [13][14] | **The single highest-stakes product decision Ditto owns.** Active intelligence = device + high-risk AI |
| **Any chatbot / Q&A surface that answers medical questions** | Free-form medical responses | **IIa or worse** + Article-50 exposure | The Character.AI / chatbot-liability cluster (Brief A §Q5) is the cautionary tale; answering "what should I do" is therapeutic decision-support | Avoid medical Q&A, or hard-scope it to "explain what your doctor said," with sourcing to the transcript |

**[INFERENCE] The bright line:** *explain and organise* = Class I. *Interpret, score, flag, triage, recommend* = Class IIa + AI-Act high-risk. Ditto's current product sits comfortably on the Class-I side. The "care intelligence layer" is the feature family that will be under constant pressure to cross it, and **crossing should be a deliberate, costed decision — not a roadmap drift.**

**[REC] Write the intended-purpose statement now**, before the care-layer ships, and gate every care-layer feature against it. A feature that "surfaces what to pay attention to" is already on the IIa side in a regulator's reading.

---

## 3. Mika teardown (+ comparable precedents)

### 3.1 Mika (Fosanis GmbH) — the near-exact precedent

| Dimension | Detail | Source |
|---|---|---|
| **What it is** | Cancer companion: distress/symptom monitoring, CBT-based coping, mindfulness, patient education, AI-tailored content. Explicitly a *companion*, not a treatment. | [5][9] |
| **Medical-device class** | **Class I** (in line with 95% of DiGA being Class I; no notified body) | [1][3] |
| **DiGA track** | **Patient-relevant structural & procedural improvement** (not "medical benefit") — counts patient sovereignty, health literacy, adherence, care coordination | Brief B [22][24]; [1] |
| **Listing** | Listed **24 Mar 2021** as Germany's 12th DiGA, **provisional**, initially for **ovarian, cervical, endometrial cancer**; later widened toward all cancers | [3][6] |
| **What happened** | Withdrew **28 Mar 2022** (couldn't fold in-progress study data into the fast-track), planning to re-apply for permanent. Withdrew **again Feb 2024** to strengthen evidence rather than risk rejection. **Never achieved permanent listing.** | [4][7][8] |
| **Pivotal RCT** | Nationwide unblinded 2-arm **waitlist RCT**, fully decentralised (recruited via Facebook/Instagram + support groups). **n=218 ITT** (99 intervention / 119 control), **12 weeks**. | [5] |
| **Endpoints** | **Primary:** distress (NCCN Distress Thermometer, 0–10) → **p=.03**. **Secondary:** depression (HADS) **p<.001**; anxiety (HADS) **p=.03**; fatigue (FACIT-F) **p=.04**; **quality of life (CGI-I) p=.38 — NOT significant.** Effect sizes small (ηp² ~0.02). No adverse events. | [5] |
| **Confirmatory trial** | Larger RCT at Leipzig University (Mehnert-Theuerkauf), **planned n=524**, to support permanent listing | [4][7] |
| **Listed price** | **[EST]** Not separately public. DiGA permanent band ≈ **€189–€243 / 90 days**; market mean negotiated price **€227 / 90 days** at end-2025 | [2][15]; Brief B |
| **Build-to-listing timeline** | Founded ~2019; first DiGA listing 2021 (~18–24 months to provisional). **4+ years and never permanent.** | [3][9] |
| **Exit** | **12 Jun 2025: Fosanis sold Mika assets to US firm Outcomes4Me** (Outcomes4Me Germany GmbH). Mika had served 100,000+ patients globally. | [9] |

**[INFERENCE — the lesson for Ditto].** Mika is the closest map to Ditto (oncology, companion, structural/procedural track, Class I, AI-tailored). Three takeaways: (1) the **structural/procedural track genuinely fits a non-treatment companion** — this part of the Phase-1 thesis holds; (2) **provisional ≠ durable** — Mika earned-while-proving for years and the finish line kept moving; (3) the **QoL miss** shows endpoint selection is do-or-die: pick patient-reported outcomes you can actually move (distress, literacy, adherence, decisional conflict), not QoL. The exit to a US buyer suggests the German-DiGA-only economics did not justify staying independent.

### 3.2 Comparable oncology / companion precedents

| App | Country / scheme | Class & track | Study | Status (May 2026) | Source |
|---|---|---|---|---|---|
| **CANKADO PRO-React Onco** | DE / DiGA | **Class I**, structural-procedural | **PreCycle** RCT (NCT03220178), HR+/HER2- metastatic breast cancer on palbociclib; primary outcome = **time to QoL deterioration, significantly delayed**; multicentre phase-IV ePRO | Listed **3 May 2021**; **struck 21 Apr 2023**. First breast-cancer DiGA; no longer reimbursed. | [10][11] |
| **Mika** | DE / DiGA | Class I, structural-procedural | n=218 waitlist RCT (above) | Withdrawn twice; never permanent; sold to Outcomes4Me 2025 | [3][9] |
| **OWise** | NL/UK (not DE-reimbursed) | n/a — not a DiGA | BMC Trials 2020: improved patient motivation/activity, early breast cancer | Used in NL/UK; **never entered German DiGA** (English-only, no DiGA listing) | [search: Thieme review; OWise] |
| **Resilience PRO** | FR / PECAN→LPPR | Telemonitoring DTx | Symptom monitoring on systemic therapy | Live; FR cap **€780/patient/yr** | Brief B [17] |

**[INFERENCE]** Of the two German oncology-companion DiGAs that existed, **both are now gone from the directory.** The functioning reimbursed oncology digital products that *survived* (Moovcare in France, Resilience PRO) are **telemonitoring with a hard clinical endpoint** (Moovcare showed a survival benefit), not plain companions. This is a strong signal: **a pure companion has historically struggled to hold a permanent reimbursed listing; the durable ones carry a measurable clinical-pathway outcome.**

---

## 4. Path 1 — Stay light (Class I, patient-owned, no app-on-prescription)

**Premise:** Ditto stays a CE-marked Class I (or out-of-scope) patient communication aid. No notified body, no AI-Act high-risk, low regulatory burden (the Phase-1 "stay light" leg). The question is **where revenue comes from without a reimbursement code.**

### 4.1 The Dutch B2B route, concretely

**[FACT] The Netherlands has no app-on-prescription scheme.** Digital care is funded *inside* existing care, and there are no special provisions to reimburse an app as a standalone line item — "the app is part of the fulfilment of the activity and not an independent ground for compensation" [17][18]. So Ditto cannot be "prescribed and reimbursed." It must be **bought by an institution out of money that institution already controls.** Four channels:

| Channel | Who pays | How it works | Benchmark / amount | Source |
|---|---|---|---|---|
| **Inside the DBC / care tariff** | Hospital, from its NZa-set treatment tariff (DBC) | If Ditto is used within a reimbursed consult/pathway, the hospital funds it from the tariff it already receives. No new code. | No separate tariff; absorbed into existing DBC | [17][18] |
| **Facultatieve prestatie** (optional/elective performance, since 2021) | Hospital ↔ insurer, negotiated regionally | Lets a hospital and insurer agree local funding for digital care that doesn't fit a standard DBC — covers patient-instruction time, monitoring software (app/algorithms), and patient-provider contact. **Six telemonitoring prestaties** exist (arrhythmia, hypertension, heart failure, chest pain, COPD, asthma) — **oncology is not yet one of them.** | Negotiated per contract; not public | NZa Wegwijzer 2026 [search]; ICT&health |
| **IZA transformatiemiddelen** (transformation funds) | VWS → insurers → providers | **€2.8B** national pot (2024–2028) for care-transformation incl. "digital self-care tools"; assessed by the two market-leading regional insurers. **Caveat: the fast-track pot was fully committed by mid-Sept 2025 and the fast-assessment mailbox closed 1 Jul 2025** — remaining money is being steered to a few priority themes (care coordination is one — adjacent to Ditto). | Project-based grants | DUS-I; NVZ; zorgakkoorden.nl [search] |
| **Supplementary insurance (aanvullende verzekering)** | Insurer's optional top-up package, member-funded | Insurers can put a product in their voluntary package; not basic-insurance. Benchmarks for adjacent digital/wellness items run **~€100–€350 one-off** (e.g. mindfulness training) rather than monthly subscriptions. | ~€100–€350 one-off, varies by insurer | [search: CZ/Menzis supplementary] |

**On the "€6–12/mo Menzis/Hello24-7" benchmark in the brief:** [INFERENCE/CAVEAT] I could not verify a specific Menzis "Hello24-7" €6–12/month line; the verified Dutch comparators are (a) telehealth/teleconsult services bundled into insurer platforms (e.g. Menzis SamenGezond) and (b) one-off supplementary-package reimbursements (~€100–€350). Treat "€6–12 PMPM" as an **unverified planning anchor** — the realistic Dutch B2B model is a **per-patient-per-pathway or annual-licence fee negotiated with a hospital/insurer**, not a consumer PMPM. **[REC] Validate with 1–2 actual insurer/hospital procurement conversations before pricing.**

### 4.2 The emerging "diga.nl" opportunity (new since the Phase-1 thesis)

**[FACT]** There is a live Dutch initiative, **diga.nl**, that currently funds **3 apps via a lump-sum licence** [search]. In its **Dec 2025 report, VWS formally recommended (Recommendation 2) to "realise in the short term a provisional reimbursement and research initiative working towards structural reimbursement as a next step for the diga.nl initiative"** [1]. VWS explicitly argues the Dutch scope should be **wider than medical devices** (covering self-care/wellness apps), citing that the German device-only focus leaves self-care apps "of unknown quality" [1]. **[INFERENCE]** This is the most important new fact for Ditto's home market: a **Class-I-friendly, possibly non-device-friendly, NL provisional-reimbursement scheme is being actively designed right now**, oriented to *exactly* the "support the delivery of healthcare / self-care" framing Ditto fits. Getting into the diga.nl pilot cohort early could be far cheaper and faster than German DiGA. Decision-maker: **VWS, advised by Zorginstituut Nederland** [search].

### 4.3 Path-1 economics & verdict

- **Regulatory cost:** low — Class I self-certification, EUDAMED registration, GDPR/TOM hardening, Article-50 AI disclosure (due 2 Aug 2026, Brief A). **[EST] sub-€100k** of regulatory/compliance effort, mostly internal.
- **Revenue:** B2B contracts with hospitals/insurers; no per-prescription reimbursement. Slower, relationship-led, but **no clinical-study gate.**
- **Strategic fit:** matches Ditto's actual product today; keeps the company out of AI-Act high-risk; preserves optionality.
- **Risk:** revenue is bespoke and procurement-cycle-slow; no national tailwind until diga.nl matures; "free patient app" expectation depresses willingness to pay.

---

## 5. Path 2 — Go clinical (CE-mark + DiGA), costed

**Corrected premise:** Going clinical does **not** require Class IIa. The DiGA route works at **Class I** (95% of DiGA are Class I [1]). Ditto would only become Class IIa — and thus AI-Act high-risk — if it adds the interpret/flag/triage features from §2. **[REC] If pursuing DiGA, do it as Class I to avoid the notified-body + high-risk burden.** The real cost is **evidence**, not certification.

### 5.1 What it costs and takes

| Component | Class I DiGA (recommended clinical path) | Class IIa DiGA (only if active care-layer) | Source |
|---|---|---|---|
| **Total programme, zero-base** | **€1.2M–€3M, 18–30 months** (no prior CE, no EU ops) | Add notified-body conformity assessment + AI-Act high-risk obligations on top | DUX [search] |
| **If migrating an existing CE-marked product** | **€400k–€1.2M, 8–14 months** | Higher | DUX [search] |
| **BSI TR-03161 security cert** | **€50k–€150k, 4–6 months** (critical path) | Same | DUX [search] |
| **Pivotal study** | Prospective comparative study / RCT. Permanently-listed DiGA RCTs: **n 56–608 (mean 244), 9–48 weeks (mean 24)** | Same study burden | [search: DiGAs Fast Track]; Mika n=218, Leipzig n=524 |
| **Notified body (IIa only)** | **Not required** | Required (Annex IX QMS + tech-doc review) — adds cost & time | [13][16] |
| **AI-Act high-risk (IIa only)** | **Not triggered** | Triggered — risk-mgmt, data governance, logging, human oversight, PMS (Brief A §Q1) | Brief A |
| **Ongoing (DiGA 2.0, from 2026)** | 6-monthly outcome reporting to BfArM from 2027; **≥20% of price performance-linked**; delisting risk | Same | Brief B [10] |

**[EST] All-in for a Class-I oncology-companion DiGA: €1.5M–€3.5M and 2–3 years** to a *provisional* listing, with **no guarantee of permanent** (Mika and CANKADO both failed to convert). Revenue at the finish line: **mean €227 / 90 days, post-negotiation** (a ~59% haircut off the ~€544 manufacturer mean) [2][15].

### 5.2 Which EU market first

**[REC] If Ditto goes the German-DiGA route at all, target Germany — it is the only mature scheme — but with a single tight indication** (e.g. "newly-diagnosed solid-tumour patients, post-consultation, distress + health-literacy + adherence outcomes"), on the **structural/procedural track** (Mika's track), at **Class I**. France PECAN is faster/cheaper to enter but DTx/telemonitoring-oriented and capped at €780/yr (Brief B). **[INFERENCE] But the corrected read is that Ditto's *home* clinical path (diga.nl, §4.2) may dominate the German one** on cost, speed, and strategic control — and should be evaluated head-to-head before committing to Germany.

### 5.3 Path-2 verdict

The clinical path is **viable at Class I** (the Phase-1 IIa fear was overstated for DiGA), but it is **expensive, slow, evidence-gated, and has a demonstrated finish-line failure rate in exactly Ditto's category.** It is a 2–3 year, multi-million-euro bet that converts Ditto from a software company into a clinical-evidence company.

---

## 6. Decision framework + sequencing + the decisions Ditto owes itself

### 6.1 When each path wins

| Condition | Path 1 (stay light) wins | Path 2 (go clinical) wins |
|---|---|---|
| **Capital** | <€1M to spare for regulatory/clinical | €1.5M–€3.5M committable over 2–3 yrs |
| **Time horizon** | Need revenue in <12 months | Can wait 2–3 yrs for a reimbursed code |
| **Product identity** | Want to stay a fast-moving software co. | Willing to become a clinical-evidence co. |
| **Feature roadmap** | Care layer stays *explain/organise* (Class I) | Care layer goes *interpret/flag/triage* anyway (already IIa) |
| **Geography** | NL-first, B2B + diga.nl pilot | Germany-first, national reimbursement at scale |
| **Risk appetite** | Avoid delisting/clawback exposure | Accept Mika/CANKADO-style finish-line risk |

### 6.2 Sequencing — yes, light-now / clinical-later works, and is the recommended order

**[REC]**
1. **Now (0–6 mo):** Stay Class I. Lock the intended-purpose statement (§2). Ship Article-50 AI disclosure before 2 Aug 2026. Pursue 2–3 Dutch B2B contracts (facultatieve-prestatie or DBC-embedded) and **apply to join the diga.nl pilot cohort.**
2. **Parallel (0–18 mo):** Design the pivotal study *as if* you'll run it — pick the indication and the movable patient-reported endpoints (distress, health-literacy, decisional-conflict, adherence — **not QoL**, per Mika's miss). This makes a later clinical decision cheap to trigger.
3. **Later (12–24 mo, gated):** Only commit the €1.5M–€3.5M clinical programme **if** (a) the care-layer roadmap is going to cross into IIa anyway, **or** (b) a reimbursement scheme (diga.nl structural track, or German DiGA) is demonstrably reachable and the unit economics clear the ~59% price haircut + DiGA-2.0 performance clawback.

Light-now does **not** burn the clinical bridge — but **two one-way doors must be respected:** (i) claiming a medical purpose to qualify for reimbursement *can* pull you into the device regime, and (ii) shipping active "intelligence" features tips you to IIa + AI-Act high-risk. Sequence so those doors are opened deliberately, not by drift.

### 6.3 The 2–3 decisions Ditto owes itself, and when

| # | Decision | Owner | By when | Why it can't wait |
|---|---|---|---|---|
| **D1** | **Write & ratify the intended-purpose statement**, and decide whether the "care intelligence layer" is *passive* (explain/organise → Class I) or *active* (interpret/flag/triage → IIa + high-risk). | CEO + product, w/ regulatory counsel | **Before the care layer ships** | This is the master switch for the entire regulatory burden. Drifting into it accidentally is the worst outcome. |
| **D2** | **Validate the Dutch B2B model with real money:** 1–2 insurer/hospital procurement conversations to confirm who pays, how, and at what price (replace the unverified €6–12 PMPM anchor with a real number). And **apply to diga.nl.** | Commercial + founder | **Next 1–2 quarters** | Path 1 revenue and the new diga.nl tailwind both depend on this; cheap to test now. |
| **D3** | **Set the clinical go/no-go gate:** define the exact trigger conditions (capital, reachable scheme, indication, endpoints) under which Ditto commits the €1.5M–€3.5M study — and pre-design the study so it's ready when/if triggered. | CEO + board | **Within 12 months** | Avoids both premature spend and being caught flat-footed if D1 forces IIa or a scheme opens. |

---

## 7. Confidence & gaps

**High confidence:** Mika's listing/withdrawal/exit history and RCT design & endpoints [3][4][5][7][8][9]; CANKADO listed-then-struck [10][11]; the corrected fact that ~95% of DiGA are Class I [1]; DiGA price benchmarks (~€227 negotiated / €544 manufacturer mean) [2][15]; DiGA programme cost/time bands [DUX]; the Dutch funding mechanics (no app-on-prescription; facultatieve prestatie; €2.8B IZA pot now committed) [17][18][search]; the VWS Dec-2025 diga.nl recommendation [1].

**Medium confidence:** exact Mika/CANKADO negotiated prices (not public — used DiGA bands); diga.nl's precise current scope, eligibility, and whether non-devices qualify (initiative is mid-design); whether oncology will get a facultatieve prestatie.

**Low confidence / unverified:** the "€6–12/mo Menzis/Hello24-7" Dutch benchmark — **could not confirm; flagged as a planning anchor only**, replace with a real procurement quote (D2). Clinical-study cost as a standalone line (folded into the €1.2M–€3M programme band, not separately itemised by sources). MDCG 2025-6 exact wording on the IIa→high-risk auto-trigger (read via Phase-1 secondary analysis).

**Highest-value next dives:** (1) a one-page **regulatory counsel opinion** ratifying the §2 classification map against Ditto's *actual* current feature build; (2) **direct diga.nl / Zorginstituut contact** to learn pilot eligibility, timing, and whether a Class-I-or-lighter summary tool qualifies; (3) **2 insurer + 2 hospital procurement conversations** to price the Dutch B2B model.

---

## 8. Sources

1. VWS / Ministry of Health (Netherlands) — *Financing and making available of digital health applications in Europe* (Dec 2025): https://www.zorgakkoorden.nl/documenten/publicaties/2025/251210-vws-financing-and-making-available-of-digital-health-applications-in-europe.pdf
2. QuickBird Medical — DiGA pricing & negotiation / revenue & costs: https://quickbirdmedical.com/en/diga-pricing-negotiation/ ; https://quickbirdmedical.com/en/diga-revenue-cost/
3. Healthcare Startups Deutschland — "Die zwölfte DiGA heisst Mika": https://healthcare-startups.de/die-zwoelfte-diga-heisst-mika/
4. Krankenhaus-IT Journal — Erste onkologische DiGA strebt mit zusätzlicher Evidenz permanente Erstattungsfähigkeit an: https://www.krankenhaus-it.de/item.1401/erste_onkologische_diga_strebt_mit_zus%C3%A4tzlicher_evidenz_permanente_erstattungsf%C3%A4higkeit_an.html
5. JMIR (2024) — Digital Therapeutic (Mika) Targeting Distress in Patients With Cancer: Nationwide Waitlist RCT: https://www.jmir.org/2024/1/e51949 ; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11082740/
6. Presseportal / Fosanis — Mika als neue DiGA aufgenommen: https://www.presseportal.de/pm/148260/4873826
7. Ärzteblatt — Psychoonkologie-App steigt vorübergehend aus DiGA-Verzeichnis aus (Mar 2022): https://www.aerzteblatt.de/nachrichten/132937/Psychoonkologie-App-steigt-voruebergehend-aus-DiGA-Verzeichnis-aus
8. Mika (Fosanis) press — "Weitere Finanzierung auf dem Weg zur App auf Rezept" (Apr 2024): https://de.mika.health/wp-content/uploads/2024/04/Weitere-Finanzierung-auf-dem-Weg-zur-_App-auf-Rezept_.pdf
9. Outcomes4Me — Acquires Germany's Mika Health App (12 Jun 2025): https://outcomes4me.com/press-release/outcomes4me-acquires-germanys-mika-health-app-to-accelerate-ai-driven-patient-empowerment-globally/ ; PR Newswire: https://www.prnewswire.com/news-releases/outcomes4me-acquires-germanys-mika-health-app-to-accelerate-ai-driven-patient-empowerment-globally-302479404.html
10. QuickBird Medical — CANKADO PRO-React Onco (listed 3 May 2021, struck 21 Apr 2023; Class I; structural/procedural): https://quickbirdmedical.com/diga-verzeichnis/cankado-pro-react-onco/
11. CANKADO Partners — Germany's first DiGA for breast cancer patients: https://partners.cankado.com/germanys-first-diga-for-breast-cancer-patients/ ; PreCycle trial (Annals of Oncology): https://www.annalsofoncology.org/article/S0923-7534(23)00684-1/fulltext
12. Prova Health — DiGA reimbursement in Germany explained (Class I or IIa eligibility; 90-day BfArM decision): https://www.provahealth.com/insights/diga-reimbursement-germany-guide
13. Johner Institute — MDR Rule 11 classification: https://blog.johner-institute.com/regulatory-affairs/mdr-rule-11/
14. Evidence.systems — How to use MDR Rule 11 ("information" = scores, gradings, flags, recommended actions): https://evidence.systems/blog/how-to-use-mdr-rule-11-chapter-1/
15. DUX Healthcare — Market Access Germany / International DTx Guide to DiGA (cost €1.2M–€3M, BSI €50–150k, timelines, price bands): https://dux-healthcare.com/en/knowledge/international-markets/market-access-germany/
16. European Commission — MDCG 2019-11 Guidance on Qualification and Classification of Software (PDF): https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf
17. CMS Law — Digital health apps and telemedicine in the Netherlands (no special app reimbursement; app funded inside the activity): https://cms.law/en/int/expert-guides/cms-expert-guide-to-digital-health-apps-and-telemedicine/netherlands
18. Med Tech Reimbursement Consulting — Reimbursement of telemedicine and digital care in the Netherlands (facultatieve prestatie mechanics): https://mtrconsult.com/news/reimbursement-telemedicine-and-digital-care-netherlands

*Additional verification searches (not separately numbered): NZa Wegwijzer bekostiging digitale zorg 2026 (six telemonitoring facultatieve prestaties); DUS-I / NVZ / zorgakkoorden.nl (IZA transformatiemiddelen €2.8B, pot committed by Sept 2025); ISPOR/JMIR "DiGAs on a Fast Track" (RCT n & duration ranges); MDCG 2019-11 Rev.1 secondary analyses (Emergo, Greenlight Guru, NAMSA).*
