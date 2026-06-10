# F1 — Symptom & Outcome Tracking (ePRO), Oncology Emphasis

> Market Deep Dive · Part I capability-field teardown · 7-lens template.
> Written 2026-06-09 by Mewtwo. Sources graded inline: **[P]** primary (peer-reviewed, regulator, company filing) · **[S]** reputable secondary (quality press, analyst) · **[V]** vendor self-report/marketing. Figures I could not verify are flagged «unverified».
> Web access available; all non-obvious claims cited. Preference for 2024–2026 sources.

---

## (a) Field map — one screen

**What this field is.** Electronic patient-reported outcomes (ePRO) = the patient self-reports symptoms and side effects on a structured schedule (often the NCI's **PRO-CTCAE** item library), an algorithm grades severity, and **severe or worsening symptoms trigger an alert to a clinician** who intervenes. In oncology this is the dominant shape. Outside oncology it shades into consumer symptom/mood trackers (Bearable), illness-specific pacing tools (Visible), and adherence apps (MyTherapy).

**The single most important fact in this brief — the Basch evidence, and its honest arc:**

| Trial | Design | Survival result | QoL / function / ER | What it proves |
|---|---|---|---|---|
| **Basch 2017, JAMA** (MSKCC) | Single-center RCT, 766 metastatic patients, web self-report of 12 symptoms, **email alert to nurse on severe/worsening symptom** | **Median OS 31.2 vs 26.0 mo, +5.0 mo, HR 0.83, p=.04** [P] | QoL ↑, ER use ↓, chemo tolerated longer (8.2 vs 6.3 mo, p=.002) [P] | Symptom self-report **plus an alert-to-clinician loop** improved survival at one elite center |
| **PRO-TECT (Basch), JAMA 2022 + final Nature Medicine 2025** | Cluster-RCT, **52 US community practices, 1,191 patients**, weekly surveys, alerts on severe/worsening | **No survival difference: HR 0.99 (0.83–1.17), p=.86** [P] | Physical function +2.47, symptom control +2.56, HRQL +2.43 (all p≤.02 at 3 mo); **time-to-first-ER-visit prolonged, HR 0.84, p=.03** [P] | At scale in the real world, **the survival signal did NOT replicate**; the QoL, function, and ER-visit benefits did |

**The mechanic, stated precisely.** The benefit is **not the tracking**. It is the **closed loop**: structured self-report → severity grading → *alert to a clinician who acts*. In 2017, nurses responded to alerts 77% of the time with a discrete clinical intervention [P, PMC5817466]. Tracking that goes into a dashboard nobody watches does nothing. This is the load-bearing insight for Ditto: **value lives in the response, not the capture.** And the honest 2025 reading is that even a perfect loop reliably buys **quality of life and fewer ER visits**, but **not extra months of life** once you leave a single resourced academic center.

**Market shape.** Two non-overlapping camps:
- **Clinical ePRO (the winners by revenue):** sold B2B to hospitals/oncology networks, embedded in the EHR/oncology information system, monetized via license + (US) reimbursement codes. Kaiku Health (Elekta), Noona (Siemens Healthineers/Varian), CANKADO (DiGA-reimbursed in Germany). These are **clinician-alert engines**, not consumer apps.
- **Consumer/patient trackers:** free or freemium, downloaded by patients directly. Outcomes4Me, OWise, Vinehealth (→Sciensus), Bearable, Visible, mySugr, MyTherapy. **None has become a standalone company on subscription revenue.** They monetize via pharma real-world data (RWD), patient-support-program (PSP) services, or device bundling, or they get acqui-hired.

**Key dynamics.**
1. **The frequency is treatment-gated.** Oncology ePRO is intense during active chemo/IO, then collapses. It is a high-frequency engine for a *window*, not a life.
2. **Standalone trackers do not survive as companies.** Survival evidence accrues to the *loop inside the health system*, so value pools at the institution or the pharma sponsor, not the app. Hence the acqui-hire pattern (Vinehealth → Sciensus).
3. **Reimbursement is the cleanest patient-facing money, and it is jurisdiction-locked** (Germany DiGA; US oncology RPM/principal-care codes). Without it, the only buyer is pharma, who pays for *data and adherence*, not for the patient's experience.

---

## (b) Player teardowns

### Clinical ePRO — the revenue winners

#### Kaiku Health (Elekta) — the category reference
| Lens | Finding |
|---|---|
| **1. Job & moment** | Cancer patient on active systemic therapy reports side effects between visits; care team catches deterioration early. Trigger = symptom flare at home. |
| **2. Sticky mechanic** | **Algorithmic grading → alert to the care unit.** When the algorithm infers a grade ≥3 symptom, an alert fires and the unit calls the patient. 16 symptom questionnaires built from NCI-CTCAE v4.03 in patient-friendly language; predictive modules for 25+ cancer types. [V/P, kaikuhealth.com; Elekta] |
| **3. Frequency engine** | Treatment-cycle cadence (per chemo cycle / weekly during active therapy). Holds because the clinician acts on the data, so reporting has a felt payoff. Decays after treatment ends. |
| **4. Monetization** | **B2B SaaS to hospitals**, embedded in Elekta's Mosaiq/Elekta ONE oncology information system. In the US, clinics can use it to meet Medicare program-reporting (RPM-adjacent) requirements. **PASSES** the filter: institutions pay, recurring, tied to reimbursable workflow. Patient pays nothing. [V, Elekta ONE brochure] |
| **5. Moat** | **Integration + regulatory + clinical evidence.** EHR/OIS embedding is the real moat (sticky, switching-cost-heavy). Owned by Elekta (radiotherapy install base = distribution). Published evidence (e.g., earlier detection of peripheral neuropathy, fewer phone calls). [V/P, Elekta] |
| **6. Outcome & lesson** | Acquired by Elekta 2020; «exact price unverified». Deployed in 40+ European clinics; "thousands" of patients across 25+ cancer types «unverified scale». **Lesson: the standout oncology ePRO did not stay independent — it became a feature of an oncology-hardware company's software stack.** [S, MobiHealthNews; V, Elekta] |
| **7. EU-applicability** | **High.** Finnish-built, European-deployed, CTCAE-based. The model (sell to the hospital, embed in the OIS) is exactly how it already runs in the EU. This is the template, not the exception. |

#### Noona (Siemens Healthineers / Varian) — the same model, bigger parent
| Lens | Finding |
|---|---|
| **1–3. Job / mechanic / frequency** | Oncology ePRO + secure patient-clinician messaging; remote symptom monitoring with oncology-specific questionnaires and alerts. Same treatment-window cadence as Kaiku. [V, Siemens Healthineers] |
| **4. Monetization** | B2B to cancer centers, sold inside the Varian/Siemens oncology portfolio. **PASSES** filter (institutional). Patient does not pay. |
| **5. Moat** | Distribution via Varian's linac install base + Siemens Healthineers' hospital relationships. Integration moat, same as Kaiku. |
| **6. Outcome & lesson** | **Same lesson as Kaiku, twice over:** a strong standalone oncology ePRO (Finnish-origin again) absorbed by a radiotherapy/imaging giant. The two best oncology ePROs in the world both ended up owned by linac companies. **Tracking is a feature that big oncology-equipment vendors buy to make their hardware stickier.** [S/V] |
| **7. EU-applicability** | High; actively marketed in EU. |

#### CANKADO PRO-React Onco — the one with a patient-facing reimbursement path
| Lens | Finding |
|---|---|
| **1. Job & moment** | Breast-cancer patient on systemic therapy; daily health documentation + dynamic symptom questionnaires + automated self-care recommendations + clinician communication. |
| **2. Sticky mechanic** | **Daily dynamic questionnaires with automated recommendations**, plus a clinician channel. Reporting cadence is *daily*, the most frequent of the clinical group. |
| **3. Frequency engine** | Daily during therapy. Holds via automated guidance + the prescription framing (it is "prescribed"). |
| **4. Monetization** | **The most interesting case for Ditto. Germany DiGA reimbursement at €499.80**, prescribable, payer-reimbursed. **PASSES the filter without pharma** — a statutory payer pays per patient. Also runs pharma-/publicly-funded study deployments. [S, MTRC reimbursement; V, CANKADO] |
| **5. Moat** | **Regulatory (DiGA listing + clinical evidence) + RCT proof.** The **PreCycle RCT (ASCO 2023)** showed CANKADO support **delayed time-to-deterioration of QoL** in HR+/HER2- metastatic breast cancer on palbociclib. [P, ASCO/JCO] Evidence is the moat that earns the reimbursement code. |
| **6. Outcome & lesson** | Still independent, niche. **Lesson: a patient-facing tracker CAN be a business — but only by becoming a reimbursed medical device in one country at a time.** Scale is gated by per-indication, per-country DiGA approval, which is slow and narrow. «Revenue/active-patient scale unverified». |
| **7. EU-applicability** | **Directly EU.** It IS the EU reimbursement model. But DiGA is Germany-specific; NL has no equivalent fast-track with the same patient-app reimbursement maturity (NL routes via Zvw/`add-on`/insurer pilots, slower). |

#### Roche Navify — included to rule it out
Navify is Roche's **clinician/lab-facing** digital portfolio (tumor board, clinical hub, algorithm suite, data aggregation across institutional IT), 30+ solutions, recently rebranded (navify Clinical Hub). It is **not a patient symptom-tracker**; it aggregates data for oncologists. [V, navify.roche.com] **Relevance to Ditto = low** as a tracking competitor; **relevant as a warning** that pharma/diagnostics giants are building the *clinician-side* data layer that consumer trackers feed into.

---

### Consumer / patient-facing trackers — beloved, but the monetization filter bites

#### Outcomes4Me — the broadest patient-facing oncology platform
| Lens | Finding |
|---|---|
| **1. Job & moment** | Newly/actively diagnosed cancer patient wants to understand options, match to trials, track symptoms, and self-advocate. Trigger = diagnosis shock + "am I getting the right treatment?" |
| **2. Sticky mechanic** | **AI navigation across guidelines + genomics + trial-matching + symptom tracking** in one free app. Trial-matching (ClinicalTrials.gov integration on cancer type, location, biomarkers) is the differentiated hook, not tracking. |
| **3. Frequency engine** | Episodic, decision-driven (around treatment decisions and scans), with tracking layered on. **Not a daily habit by design.** |
| **4. Monetization** | **Free to patients; pays via pharma/life-sciences.** $21M raised May 2025 ($38M total); 7 of top-10 cancer pharma are customers; revenue from trial recruitment + reaching "the right patient at the right time." [S, PR Newswire; Crunchbase] **PASSES filter only via pharma RWD/recruitment, NOT via patients.** 280k+ users. [V/S] |
| **5. Moat** | Data network + pharma relationships + guideline/genomics content depth. Brand among US patients. |
| **6. Outcome & lesson** | Scaling, still independent, venture-funded. **Lesson: the patient love is real, but the money is pharma's; the patient is the product, not the customer.** |
| **7. EU-applicability** | **Weak on the money side.** EU pharma RWD/recruitment spend exists but GDPR + EU trial landscape make the US trial-matching engine less transplantable; guidelines differ (ESMO vs NCCN). |

#### OWise (Px HealthCare) — NL-origin, the closest cultural analog
| Lens | Finding |
|---|---|
| **1. Job & moment** | Breast/prostate cancer patient logs symptoms, side effects, questions; shares real-time data with clinicians; shared decision-making and self-management. |
| **2. Sticky mechanic** | Symptom/side-effect log **shared with the clinician** + structured shared-decision tools (question prompts before consults). CE-marked, NHS-accredited. |
| **3. Frequency engine** | Treatment-window; consult-driven peaks (logging before/after appointments). Same decay pattern. |
| **4. Monetization** | Free to patients; revenue via **RWE studies with pharma (e.g., AstraZeneca UK)** + NHS/health-system relationships. **PASSES only via pharma/health-system, not patients.** [V, pxhealthcare.com] «Revenue scale unverified». |
| **5. Moat** | NHS accreditation + CE mark + RWE datasets + Dutch origin. Brand/trust in NL/UK. Moat is modest and copyable. |
| **6. Outcome & lesson** | Long-lived (NHS Innovation Accelerator 2016) but **small and indication-narrow** after ~a decade. **Lesson: even a trusted, CE-marked, NL-born oncology tracker has not become a large standalone company on tracking alone.** |
| **7. EU-applicability** | **Highest cultural fit** (Dutch origin, NHS route). Directly relevant as the realistic ceiling of "good oncology tracker, no bundle." |

#### Vinehealth → Sciensus — the canonical acqui-hire, the answer to question 3
| Lens | Finding |
|---|---|
| **1–3. Job / mechanic / frequency** | Cancer patient tracks/manages/understands symptoms; generates clinician-facing insight. Treatment-window cadence. UK-built, award-winning UX. |
| **4. Monetization** | Never cracked patient-pay. Value was **the longitudinal RWD + patient-support delivery**. |
| **5. Moat** | Data + UX; **not durable as a standalone** — the data is only valuable to someone who can monetize it (pharma services). |
| **6. Outcome & lesson** | **Acquired by Sciensus (Jan 2024)** — a pharma-services/medicines-delivery firm — explicitly for "rich longitudinal real-world data" and to strengthen patient-support-program capability. [S, Medical Device Network; V, Sciensus] **This is the thesis: a standalone tracker's exit value is its data + PSP fit to a pharma-services buyer, not a consumer business.** «Price unverified». |
| **7. EU-applicability** | The acqui-hire dynamic is jurisdiction-agnostic and **applies fully to EU**. |

#### Bearable — proof a tracker CAN earn subscription, and why it is small
| Lens | Finding |
|---|---|
| **1. Job & moment** | Person with chronic/undiagnosed condition tracks symptoms + meds + triggers to **find correlations** and feel in control. Trigger = "what makes me worse?" |
| **2. Sticky mechanic** | **Correlation/insight reports** across symptoms, treatments, triggers. The payoff is *self-knowledge*, not a clinician response. |
| **3. Frequency engine** | **Genuinely daily** for engaged users — closest to a real habit in this brief — because the insight loop is intrinsic (no clinician needed). But the engaged cohort is the minority of the 900k installs. [V, bearable.app] |
| **4. Monetization** | **Freemium subscription, $34.99/yr or $6.99/mo, no ads, no pharma.** **PASSES the filter on patient-pay — the only player here that does — but the ARPU and conversion are small** (free tier is generous by design/ethos; "Bearable Heroes" gives free premium). A real but small business. |
| **5. Moat** | **Weak.** Brand + community goodwill; the feature is copyable. No data/network/regulatory moat. |
| **6. Outcome & lesson** | Bootstrapped, small, beloved. **Lesson: patient-pay tracking is possible but caps at small-business scale unless bundled with something higher-value.** |
| **7. EU-applicability** | High (consumer app, no reimbursement dependency), but the small-scale ceiling travels with it. |

#### Visible — the wearable-bundle frequency engine
| Lens | Finding |
|---|---|
| **1. Job & moment** | Long-COVID/ME-CFS/POTS patient **paces activity to avoid crashes** (post-exertional malaise). Trigger = daily risk of a crash. |
| **2. Sticky mechanic** | **Morning HRV reading (phone camera or wearable) → daily "stability"/pace score → real-time overexertion alerts.** The number tells you how much you can safely do *today*. This is a genuinely sticky, daily, *forward-looking* mechanic. [S, TechCrunch; ME Association] |
| **3. Frequency engine** | **Daily and durable** because the disease is chronic (not a treatment window) and the score governs daily behavior. Best frequency engine in the brief. |
| **4. Monetization** | **Visible Plus subscription bundled with a wearable armband** for continuous HR/actimetry. **PASSES the filter via subscription + hardware bundle** (the mySugr pattern, consumer-side). 250k+ users. «Subscriber count/price unverified». |
| **5. Moat** | Disease-community trust + the longitudinal HRV/symptom dataset + wearable integration. Moderate. |
| **6. Outcome & lesson** | Growing; venture-backed. **Lesson: durable daily frequency comes from a CHRONIC condition where the metric drives a daily decision — and the money still needs a bundle (hardware/subscription).** |
| **7. EU-applicability** | High (consumer, no reimbursement needed). Condition-specific, not oncology. |

#### mySugr (Roche) — the bundling lesson, made explicit
| Lens | Finding |
|---|---|
| **1–3. Job / mechanic / frequency** | Diabetes logbook + bolus calculator + reminders; daily because glucose management is daily. Most-loved diabetes app, 3.5M+ users. [S, DiaTribe] |
| **4. Monetization** | **Standalone Pro = only $2.99/mo (weak).** The real money: Roche's **German "package" at ~€999/yr** = unlimited test strips + Accu-Chek meter + Coach + Pro, **fully reimbursed**; and giving meters away free to drive app downloads. **PASSES — but ONLY because it is bundled with a reimbursed consumable/device.** [S, DiaTribe; Porsche Consulting] |
| **5. Moat** | Brand + the strip/meter razor-and-blade tie. |
| **6. Outcome & lesson** | Acquired by Roche 2017. **Lesson, stated plainly: even the world's best-loved tracker monetizes through a reimbursed device bundle, not through the app. A tracker is a customer-acquisition and stickiness layer for a consumable.** |
| **7. EU-applicability** | High (the €999 bundle IS a German construct). |

#### MyTherapy (smartpatient) — the pharma-platform endgame
| Lens | Finding |
|---|---|
| **1–3. Job / mechanic / frequency** | Medication reminders + adherence + symptom/measurement logging; **daily by design** (pill times). 12M+ users, 100M+ monthly engagements, 1B+ confirmed intakes. [V, smartpatient.eu] |
| **4. Monetization** | **Free to patients; the entire business is a B2B platform for pharma** — custom patient-support programs, adherence/persistence ROI, DTx, and RWD (MS, psoriasis, wet AMD; Merck/Novartis/Pfizer/Bayer/Sanofi). **PASSES via pharma, not patients.** [V] |
| **5. Moat** | **Scale + adherence-data network + pharma integrations.** The largest patient-facing engagement dataset in this brief. |
| **6. Outcome & lesson** | 10+ years, large, sustainable — **by becoming pharma's patient-engagement OS.** **Lesson: the biggest patient-facing tracker in the world is, commercially, a pharma-services company.** |
| **7. EU-applicability** | High (German-built, EU pharma customers). |

---

## (c) White space for Ditto — sharpest implications

The three mandated questions, answered, then the implications.

**Q1 — Does symptom tracking create durable weekly/daily frequency, or only in treatment windows?**
**Mostly treatment windows, with two exceptions Ditto should learn from.** Every oncology player's frequency is treatment-gated and decays when therapy ends (Kaiku, Noona, CANKADO, OWise, Vinehealth). Durable *daily* frequency appears only where (a) the condition is chronic-by-nature (Visible, mySugr, MyTherapy — diabetes/ME-CFS/medication), or (b) the metric **drives a daily decision the patient cares about** (Visible's pace score; Bearable's correlations; mySugr's bolus dose). **For Ditto's oncology beachhead, tracking is a high-intensity engine for the active-treatment window, not a forever-habit.** That window is still valuable (weekly contact during chemo is real frequency), but it is a *season*, not a life.

**Q2 — Can it monetize WITHOUT reimbursement, or is reimbursement/RWD-to-pharma the only model?** Four monetization paths exist, and the patient is the paying customer in only one:

| Path | Who pays | Players | Verdict for Ditto |
|---|---|---|---|
| **Institutional B2B (embed in OIS/EHR)** | Hospital / oncology network | Kaiku, Noona | Strong, but requires hospital integration + a clinician to staff the alert loop. Ditto is not in the OIS. |
| **Reimbursed patient app (DiGA / RPM codes)** | Statutory payer / Medicare | CANKADO, mySugr-bundle | Cleanest patient-facing money; **but jurisdiction-locked and slow; NL lacks Germany's DiGA fast-track.** |
| **Pharma RWD / PSP / trial-matching** | Pharma | Outcomes4Me, OWise, Vinehealth, MyTherapy | The default for "free consumer" trackers. **Makes the patient the product** — uncomfortable fit with Ditto's trust brand and GDPR posture. |
| **Consumer subscription / hardware bundle** | Patient | Bearable, Visible, mySugr | Possible but **caps at small-business scale unless bundled** with a device/consumable Ditto does not have. |

**So: pure patient-subscription on tracking alone tops out small (Bearable). The scaled money is institutional, reimbursed, or pharma, and the pharma route conflicts with Ditto's brand.**

**Q3 — Why do standalone trackers get acqui-hired instead of becoming companies? What must Ditto bundle?**
Because **the value the evidence created (the survival/QoL benefit) pools at the institution and the data pools to pharma, not in the app.** A tracker's standalone asset is a longitudinal RWD set + a patient-support delivery channel, which is worth most to a pharma-services buyer (Vinehealth → Sciensus, explicitly for "longitudinal real-world data" and PSP capability) or an oncology-equipment vendor making its hardware stickier (Kaiku → Elekta, Noona → Varian/Siemens). **A tracker is a feature, so it gets bought by someone who owns the surrounding system.**

**The four implications for Ditto:**

1. **Build the alert-to-action loop, not a tracker.** The entire evidence base (Basch 2017, PRO-TECT, Kaiku) says value = *structured report → severity grade → someone acts*. A symptom log in Ditto with no responder is a graveyard feature. But Ditto is not a clinic and cannot staff a nurse alert line. **The white space: Ditto's "responder" can be the Intelligence layer (advice/triage/"call your team about X") + the care circle (route the alert to the loved one or the patient's own clinician contact), not a Ditto-employed nurse.** This is the one configuration of the loop a consumer app can own. Validate it: does an AI-graded "this looks like it needs a call" + a nudge to the existing care team reproduce *any* of the QoL/ER-visit benefit? That is a testable, fundable hypothesis.

2. **Treat tracking as a frequency engine FOR the treatment window, bundled into the front door — not as the product.** Tracking alone is treatment-gated and monetizes small. But during active oncology treatment it manufactures the weekly/daily contact Ditto lacks today (Ditto is episodic/appointment-gated). **Use the treatment window's tracking to feed the operational front door (symptom report → "book a call," "message your team," "flag at next appointment") and the PHR multiplier (the longitudinal symptom record makes summaries and advice better).** Tracking earns its place as the between-appointment engine that *routes into* layers that monetize, not as a standalone.

3. **Be honest about survival. Sell QoL, fewer ER visits, and control, not "live longer."** The 2017 +5-month headline does NOT replicate at scale (PRO-TECT HR 0.99). **What reliably survives the move out of an elite center is better quality of life, better symptom control, and fewer ER visits.** That is still a strong, payer-relevant, patient-relevant claim, and it is the honest one. **Flag for Merlijn:** any Ditto narrative leaning on "ePRO improves survival" is overclaiming on 2026 evidence; lead with QoL + avoided crises + reduced ER use.

4. **Pick a money path deliberately, and it probably is not patient-subscription-on-tracking.** Given Ditto's trust brand, the **pharma-RWD route is a brand risk** (patient-as-product). The institutional and reimbursed routes need a clinician loop and jurisdiction work Ditto does not yet have. **The most Ditto-native path: tracking is free, drives frequency and PHR depth during treatment, and monetizes indirectly through the front door / coordination / B2B-to-provider relationships — i.e., tracking is the hook, not the till.** This must be stress-tested in the synthesis against the hard filter: if no adjacent layer monetizes the frequency tracking creates, tracking is excluded as a standalone bet.

**Bottom line for the synthesis:** ePRO is a **proven mechanic (the alert loop) attached to a weak standalone business**. It belongs in Ditto's Intelligence layer as a *between-appointment frequency engine for the active-treatment window*, valuable mainly because it feeds the front door and the PHR — and only if Ditto can manufacture a credible "responder" (AI + care circle) without becoming a clinic. It should never be the thing Ditto charges for.

---

## (d) Citations

| # | Source | Grade | Used for |
|---|---|---|---|
| 1 | Basch E. et al., *Overall Survival Results of a Trial Assessing PROs for Symptom Monitoring During Routine Cancer Treatment*, JAMA 2017 — PMC5817466 (pmc.ncbi.nlm.nih.gov/articles/PMC5817466/) | **[P]** | 2017 single-center RCT: OS 31.2 vs 26.0 mo, HR 0.83 p=.04; nurse alert loop; 77% response rate; chemo duration 8.2 vs 6.3 mo |
| 2 | Basch E. et al., PRO-TECT, JAMA 2022;327(24):2413-2422, doi:10.1001/jama.2022.9265 — PubMed 35661856; Johns Hopkins Pure record | **[P]** | Cluster-RCT, 1,191 patients / 52 practices; physical function +2.47, symptom control +2.56, HRQL +2.43 (p≤.02) |
| 3 | Basch E. et al., *Final results of the PRO-TECT cluster-randomized trial*, Nature Medicine 2025, s41591-025-03507-y; PubMed 39920394 | **[P]** | Final OS HR 0.99 (0.83–1.17), p=.86 (no survival benefit); time-to-first-ER-visit HR 0.84, p=.03 |
| 4 | NCI PRO-CTCAE development & methods — PMC4200059; Dueck et al., *Cancer* 2025 (Wiley); healthcaredelivery.cancer.gov/pro-ctcae | **[P]** | PRO-CTCAE item library (124 items / 78 toxicities); clinicians miss up to half of symptomatic AEs; FDA support |
| 5 | MobiHealthNews, *Cancer-focused Elekta snaps up Kaiku Health* | **[S]** | Elekta acquisition of Kaiku (2020); Mosaiq integration |
| 6 | Kaiku Health / Elekta product pages + Elekta ONE Patient Companion brochure | **[V]** | Grade ≥3 alert→care unit loop; 16 CTCAE-based questionnaires; 25+ cancer types; 40+ EU clinics; US Medicare program reporting |
| 7 | kaikuhealth.com — peripheral-neuropathy detection / phone-call-burden study | **[V/P]** | Clinical evidence claim (vendor-reported study) |
| 8 | Siemens Healthineers / Varian — Noona product pages | **[V]** | Noona oncology ePRO + messaging + alerts; portfolio ownership |
| 9 | CANKADO PRO-React product site + pro-react.de | **[V]** | Daily dynamic questionnaires, automated recommendations, breast cancer indication |
| 10 | Med Tech Reimbursement Consulting — *health apps reimbursed in Germany* | **[S]** | CANKADO DiGA reimbursement, €499.80 tariff |
| 11 | PreCycle trial, ASCO/JCO 2023 (ascopubs.org/doi/10.1200/JCO.2023.41.16_suppl.1008) | **[P]** | CANKADO delays time-to-deterioration of QoL in HR+/HER2- mBC on palbociclib |
| 12 | navify.roche.com — navify Oncology Hub / Clinical Hub; PR Newswire navify launch | **[V/S]** | Navify is clinician/lab-facing, 30+ solutions; not a patient tracker |
| 13 | Outcomes4Me press release + PR Newswire ($21M, May 2025); Crunchbase; Precision Medicine Online | **[S/V]** | $21M raise / $38M total; 280k+ users; 7 of top-10 cancer pharma; trial-matching via ClinicalTrials.gov |
| 14 | Px HealthCare / OWise (pxhealthcare.com; owise.uk) | **[V]** | NL origin, CE-marked, NHS-accredited; AstraZeneca UK RWE; breast + prostate |
| 15 | Medical Device Network; Sciensus knowledge base; HTN — *Sciensus acquires Vinehealth* (Jan 2024) | **[S/V]** | Acqui-hire rationale: longitudinal RWD + patient-support-program capability |
| 16 | Bearable (bearable.app pricing & principles; chronic-illness tracker pages) | **[V]** | 900k members; $34.99/yr or $6.99/mo; no ads/pharma; correlation reports; Heroes free tier |
| 17 | TechCrunch (2022 launch); ME Association (2024); makevisible.com; Wikipedia | **[S/V]** | Visible: HRV/pace score, PEM pacing, 250k+ users, Visible Plus wearable bundle |
| 18 | DiaTribe *Roche Buys mySugr*; Porsche Consulting case (2021); MedCity Q&A | **[S]** | mySugr 3.5M+ users; Pro $2.99/mo; German €999/yr reimbursed strip+meter+Coach bundle |
| 19 | smartpatient.eu (platform, 10-year blog); mytherapyapp.com pharma page | **[V]** | MyTherapy 12M+ users, 100M+ monthly engagements, 1B+ intakes; pharma-PSP/RWD/DTx model; Merck/Novartis/Pfizer/Bayer/Sanofi |

**Verification gaps flagged in-text:** Elekta/Varian acquisition prices; Kaiku & OWise active-patient/revenue scale; Outcomes4Me revenue; Visible subscriber count & price; Sciensus/Vinehealth deal terms. All marked «unverified» at point of use.
