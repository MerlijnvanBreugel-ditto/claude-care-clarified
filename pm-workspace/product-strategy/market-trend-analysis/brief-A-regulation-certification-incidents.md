# Brief A — EU Regulation, Certification & AI-Error Incidents

**Workstream A of the outside-in market/trend scan.** Focus: EU primary, US/global as leading signal.
**Author:** Senior healthcare-regulation analyst (Mewtwo research)
**Date:** 2026-05-30 · **Depth:** Phase 1 (broad map, well-sourced) · **Currency:** data current as of late May 2026

Legend for claim types used throughout: **[FACT]** = sourced statement of record · **[INFERENCE]** = my reasoning from facts · **[REC]** = recommendation · **[EST]** = estimate, treat as directional.

---

## 1. Executive summary

- **[FACT]** The EU AI Act's hardest medical-AI deadlines just slipped. The "Digital Omnibus" reached provisional political agreement on **6 May 2026** (confirmed by Member States 13 May): high-risk **embedded-in-product** obligations (Annex I, which covers CE-marked medical devices under MDR) move from **2 Aug 2027 → 2 Aug 2028**; standalone high-risk (Annex III) moves to **2 Dec 2027**. Not yet in the Official Journal, so **not yet binding**. [1][2][3]

- **[FACT]** The obligation that bites a *patient-facing* AI app first is **not** the high-risk regime but the **Article 50 transparency rule**, still on schedule for **2 Aug 2026**: any AI that interacts directly with a person must make clear the user is talking to an AI, perceivably at the point of interaction (a buried T&C line does not count). [4][5]

- **[FACT/INFERENCE]** Whether Ditto's summary feature is a *regulated medical device* turns on **MDR Rule 11 / MDCG 2019-11**. Software that merely presents/reformats information *to a patient* without supporting a clinical decision can stay outside the device regime or at Class I; the moment intended purpose drifts toward "information used to take diagnostic or therapeutic decisions," it defaults to **Class IIa** (notified body required) and almost never stays Class I. This boundary is the single highest-leverage regulatory decision Ditto controls. [6][7][8]

- **[FACT]** **Only** medical-device AI that requires a notified body (broadly MDR Class IIa+) is automatically "high-risk" under the AI Act per **MDCG 2025-6**. A Class I or non-device app is therefore *outside* the AI Act high-risk regime — a strong argument for keeping the summary feature non-diagnostic by design. [9][10]

- **[FACT]** **EHDS (Reg. (EU) 2025/327)** entered into force **26 Mar 2025**. Primary-use patient-data exchange (patient summaries, ePrescriptions) and most secondary-use rules apply from **March 2029**; images/labs/discharge from **March 2031**. EHR-vendor interoperability certification and national digital-health authorities phase in 2025–2027. This is a multi-year tailwind for data portability, not a near-term obligation. [11][12][13]

- **[FACT]** GDPR health-data enforcement is intensifying: 265 healthcare-sector fines totalling ~€32.3M across 27 countries, with 2025 new fines up **~26%** YoY; recurring themes are weak technical/organisational measures and **bundled / invalid consent** (e.g., Italian Garante €1.5M against a health app for bundling health-data consent with marketing). [14]

- **[FACT — incident scan]** AI clinical tools are having a visibly bad 12 months. Headline EU/global cases: **Ontario AG (12 May 2026)** found *all 20* approved AI-scribe vendors produced hallucinations/fabrications, used by ~5,000 doctors; **Pennsylvania v. Character.AI (5 May 2026)** alleges chatbots posed as licensed medical professionals; a **BMJ Open** study (~Apr 2026) found **49.6%** of chatbot health answers problematic; a **Mount Sinai** study found ChatGPT-style triage under-triaged **52%** of genuine emergencies; **Whisper** medical transcription showed hallucinations in up to **8/10** clips with ~40% potentially harmful. [15][16][17][18][19][20]

- **[REC]** Two near-term must-dos regardless of device strategy: (a) ship clear Article-50-grade AI disclosure before Aug 2026; (b) write the intended-purpose statement deliberately to stay out of Class IIa unless Ditto chooses to invest in CE marking. A deeper Phase-2 dive on the device-classification line and on a defensible "non-diagnostic summarizer" positioning would pay off most.

---

## 2. Key findings (by the five questions)

### Q1 — EU AI Act: status, classification of medical/health AI, obligations, timelines, what it means for a patient-facing summary app

**Status & timeline (as of late May 2026).** The AI Act entered into force **1 Aug 2024**. Prohibited-practices and AI-literacy provisions applied from **Feb 2025**; **GPAI** model-provider obligations applied from **2 Aug 2025**, with Commission enforcement powers (including fines) from **2 Aug 2026**. [21][2] The **Digital Omnibus** simplification package reached provisional political agreement on **6 May 2026** (Member-State confirmation 13 May), pushing the high-risk deadlines: standalone Annex III systems **2 Aug 2026 → 2 Dec 2027**; product-embedded Annex I systems (incl. MDR/IVDR devices) **2 Aug 2027 → 2 Aug 2028**; regulatory sandboxes to Aug 2027. **Important caveat: this is not yet adopted/published, so legally non-binding until it hits the Official Journal.** [1][2][3]

**How medical/health AI becomes "high-risk."** Two routes under Article 6. Route 6(1): the AI is a product, or safety component of a product, that already requires **third-party conformity assessment** under Annex I harmonised law — which includes MDR/IVDR. Per **MDCG 2025-6**, AI that *is* a medical device **and** needs notified-body involvement (broadly MDR **Class IIa and up**, IVDR Class B+) is automatically high-risk. MDR **Class I** software is generally **not** high-risk AI unless separately caught by Annex III. Route 6(2)/Annex III lists standalone high-risk use-cases. [9][10][22]

**Core obligations once high-risk (Chapter III).** Risk-management system (extended to fundamental rights, not just safety); data governance and bias detection/mitigation; technical documentation; automatic event logging; transparency and instructions for use including accuracy/cybersecurity/fundamental-rights risks; effective human oversight with the ability to halt; accuracy/robustness; and post-market monitoring. For device AI these are run *through* the MDR/IVDR conformity assessment (integrated notified-body review), not as a parallel certificate. [10][9]

**GPAI / LLM dependency angle (directly relevant — Ditto builds on foundation models).** GPAI provider obligations (technical documentation, downstream-info, training-data summary, copyright policy) have applied since **2 Aug 2025**; the voluntary **GPAI Code of Practice** (published 10 Jul 2025; 26 signatories incl. OpenAI, Anthropic, Google, Microsoft) gives a presumption of conformity. **Key point for Ditto: you cannot outsource compliance to your model vendor.** If Ditto builds a high-risk system on top of a GPAI model, Ditto inherits the full high-risk obligations for the integrated system. [23][24]

**What it concretely means for a patient-facing AI summary app.**
- **[INFERENCE]** If the summary is positioned as a *non-diagnostic patient communication aid* (reformatting/explaining what was said, not recommending diagnosis or treatment), the strongest reading keeps it out of the AI-Act high-risk regime (because it's not a notified-body device).
- **[FACT]** Regardless of device status, **Article 50 transparency** still applies from **2 Aug 2026**: users must be told they're interacting with AI, perceivably, at the point of interaction — relevant to any chat/Q&A surface and arguably to AI-generated summaries. Watermarking of AI-generated content gets a grace period to **2 Dec 2026**. [4][5][2]
- **[INFERENCE]** The Omnibus delay buys time on the heavy high-risk machinery but does **not** delay Article 50, GPAI duties, or GDPR.

### Q2 — Medical device certification: MDR, CE marking, MDSW classification, Class I vs IIa, UK MHRA + AI Airlock

**MDR / MDSW qualification (MDCG 2019-11).** Software is a medical device ("MDSW") when it has a medical *intended purpose* beyond simple storage/communication/search of data. Pure data display, lifestyle/wellness, and administrative software typically fall outside. [6][8]

**Rule 11 — the Class I vs IIa line (the decision that matters most).** [6][7][8]

| Output of the software | MDR class |
|---|---|
| Does **not** provide information used for diagnostic/therapeutic decisions (e.g., wellness, generic info, non-clinical monitoring) | **Class I** (rare) — or out of scope entirely |
| Provides information **used to take decisions** with diagnosis/therapy purposes | **Class IIa** (notified body) — the default for clinical software |
| Could cause serious deterioration / surgical intervention | Class IIb |
| Could cause death / irreversible deterioration | Class III |

- **[FACT]** In practice "nearly all medical device software is at least Class IIa"; genuine Class I cases are narrow (e.g., a validated conception/fertility calculator). The Rule-11 severity bias is widely criticised for over-classifying low-risk software. [6][7]
- **[FACT]** MDCG 2019-11 (rev.1) explicitly extends Rule 11(a) to **prognosis/prevention** framed as diagnostic information → Class IIa. So "predict/flag" framing pulls toward IIa. [6]
- **[INFERENCE — Ditto-specific]** A tool that **summarizes a consultation for the patient in plain language** is closer to "presenting information to the patient" than "providing information used to take a clinical decision," which supports a **non-device or Class I** reading. But the line is genuinely ambiguous, and intended-purpose wording (and any feature that nudges toward advice/recommendation/triage) can flip it to IIa. This deserves a written legal/regulatory opinion before scaling.

**Note:** **EUDAMED** — mandatory use of the first modules begins **May 2026**, raising baseline transparency/registration expectations for device players. [25]

**UK MHRA equivalent + reforms (relevant to UK expansion).** [26][27][28][29][30]
- **AI Airlock** — world-first regulatory sandbox for AI as a medical device; pilot finished **Mar 2025**, **Phase 2 runs to ~Apr 2026** (focus: risk classification, change management, bias/fairness); **£3.6M over 3 years (2026–2029)** / DHSC ~£1.2M/yr committed.
- **Dedicated AI-as-a-medical-device framework** expected to be **published in 2026**; a **National Commission into the Regulation of AI in Healthcare** ran a Call for Evidence (Dec 2025), reporting in 2026.
- **PMS reform live since Jun 2025** (UK MDR Part 4A): **serious-incident reporting cut from 30 → 15 days**.
- **International reliance route** (recognising US FDA, Health Canada, TGA approvals for a streamlined GB application) expected to open **H1 2026**, including for SaMD/AI — potentially **6–12 months faster** to UK market.
- **[FACT]** Post-reform, UK intends most SaMD to be **Class IIa**, converging with EU. [29]

### Q3 — EHDS: status, what it enables for app developers, key dates

**Status.** **Regulation (EU) 2025/327** published in the OJ **5 Mar 2025**, in force **26 Mar 2025**. Phased application over ~4–6 years. [11][12][13]

**Key dates.** [11][12]
- **By Jun 2025** — Member States appoint National Digital Health Authorities.
- **2025–2027** — Commission implementing/delegating acts; EHR-system interoperability certification phases in (key acts due ~Mar 2027).
- **Mar 2029** — primary application: cross-border exchange of first priority categories (**patient summaries, ePrescriptions/eDispensations**) via **MyHealth@EU**; most **secondary-use** rules begin.
- **Mar 2031** — second priority categories (**medical images, lab results, discharge reports**).

**What it enables for app developers.** [13][12]
- **Primary use:** patients get free, fast access to their own EHR data; can add info, restrict access, see access logs, request corrections, and exercise **cross-border portability** in a standard EU format. Patient apps can plug into portability via mechanisms like the **xShare "Yellow Button."**
- **Secondary use:** governed access to large-scale, high-quality health datasets via **HealthData@EU** — explicitly framed by the Commission as enabling a health-tech company to access medical images to **train/validate an AI model** before market approval.
- **[INFERENCE — Ditto]** EHDS is a structural tailwind: portability rights and standardised formats make a "care intelligence layer" that aggregates a patient's records more feasible, and secondary-use access could feed model improvement. But the impactful dates are **2029+**; near-term it shapes architecture and partnership strategy, not this year's roadmap.

### Q4 — GDPR special-category (health) data: recent developments (2024–2026)

- **[FACT]** Health data is Article 9 special-category data; processing needs both an Art. 6 basis and an Art. 9 condition (typically **explicit consent** for a consumer health app). Valid consent must be freely given, specific, informed, unambiguous, documented and withdrawable. [14][31]
- **[FACT — enforcement]** Healthcare sector: **265 fines, ~€32.3M, 27 countries**; 2025 new fines **+26% YoY**; the most common cause is inadequate **technical/organisational measures (100 fines, €22.8M)**. [14]
- **[FACT — health-app specifics]** Italian **Garante €1.5M** against a health app for **bundling** health-data consent with marketing consent; a Norwegian DPA ~€6M fine on a mobile app for unlawful third-party ad-data sharing without valid consent. Consent design is the dominant failure mode for apps. [14]
- **[FACT — guidance]** EDPB published a **2025 study on secondary use of health data for research**, flagging fragmented national interpretations; EDPB **Guidelines 3/2025** on the DSA–GDPR interplay; new German guidelines (2025) on international transfers of health data in research. [32][33]
- **[INFERENCE — Ditto]** The recurring enforcement pattern (bundled consent, weak TOMs, third-party data sharing) maps directly onto risks for a consult-recording app with a family "care circle" sharing loop. **Sharing summaries with family members is a consent/lawful-basis design problem, not just a feature.**

### Q5 — Incident scan (last ~12 months, emphasis on last ~2 months; EU + notable global)

| Date | Tool / company | What happened | Consequence |
|---|---|---|---|
| **12 May 2026** | **Ontario approved AI medical scribes** (20 vendors) | Auditor General found **all 20** approved vendors produced inaccuracies — hallucinations/fabrications, wrong drug names, fabricated treatments, missing mental-health detail, privacy lapses; ~**5,000** doctors using them; "inadequate evaluation and oversight." | Province issued guidance requiring **manual review** of AI notes before clinical use; widely covered (CBC, PBS, Futurism); logged as an OECD.AI incident. [15][16] |
| **~Apr 2026** | **5 major chatbots** (ChatGPT, Gemini, DeepSeek, Meta AI, Grok) — BMJ Open study | Of 250 responses on cancer/vaccines/nutrition etc., **49.6% problematic** (19.6% "highly problematic" = outright misinfo / plausibly harmful). | Authors warn deployment without oversight "risks amplifying misinformation." [17][34] |
| **5 May 2026** | **Character.AI** (Pennsylvania AG suit) | State alleges chatbots **posed as licensed medical professionals**, violating medical-licensing law. | Active state-AG litigation; reputational + regulatory. [35][36] |
| **Jan 2026** | **Character.AI** | **Settled** multiple wrongful-death/mental-health suits from families (minors). | Settlement; ongoing scrutiny. Part of ≥10 known suits vs OpenAI/Character by end-2025 (7 deaths). [37][38] |
| **2025–2026** | **OpenAI / ChatGPT** | Wrongful-death suits: alleged dangerous substance-combination guidance (Sam Nelson); alleged facilitation of self-harm (Adam Raine, 16). | Product-liability/negligence litigation; major press. [38][37] |
| **Feb 2026** | Oxford study on chatbot medical advice | New study warns of **risks of chatbots giving medical advice**. | Adds to evidence base for regulation. [39] |
| **~Feb 2026** | **Mount Sinai** study | ChatGPT-style health triage **under-triaged 52%** of genuine emergencies, steering people away from urgent care; chatbots also "run with" injected misinformation. | Patient-safety warning; calls for stronger safeguards. [18][40] |
| **Jul 2025** | **Woebot Health** | Pioneering therapy chatbot **shut down**; founder cited AI "moving faster than regulators." | Market exit; signal that the safe regulatory path for clinical chatbots is unclear. [41] |
| **Nov 2025** | **FDA digital advisers** | Advisory committee convened on **risks of therapy chatbots**, weighing regulation; classification of health chatbots as devices debated (Petrie-Flom, May 2026: "health AI chatbots are legally medical devices"). | Signals tightening US posture; leading indicator for EU. [42][43] |
| **Oct 2024–2025** | **OpenAI Whisper** (incl. **Nabla** medical build, ~30k clinicians / 7M visits) | Research ("Careless Whisper") found fabricated text in up to **8/10** clips; ~**40%** of hallucinations potentially harmful; invented phrases in silences, worse for aphasia patients. OpenAI warns against high-risk use. | Sustained press (Fortune, AP/Science, PBS); reputational risk for transcription-based clinical tools. [19][20][44] |
| **Mar 2025** | **EMA** AIM-NASH | **Positive** counter-signal: EMA qualification opinion on an AI tool supporting liver-biopsy analysis — regulators *can* greenlight well-validated medical AI. | Shows the upside path. [45] |

**Direct relevance to Ditto:** the scribe/transcription cluster (Ontario AG, Whisper/Nabla) is the closest analog to Ditto's pipeline (record consultation → AI-generated text). The failure modes are exactly those that hit a summarizer: **hallucination, omission, speaker mix-up, fabricated treatments/drug names.** The chatbot-liability cluster is the cautionary tale of what happens when an AI surface drifts into giving medical advice.

---

## 3. Implications for Ditto

1. **[REC] Treat the intended-purpose statement as a strategic regulatory asset.** Position the summary as a *patient-facing communication/comprehension aid* — explaining what was said, not advising what to do. Done well, this is the difference between **out-of-scope / Class I** and **Class IIa (notified body, AI-Act high-risk)**. This is the single highest-leverage lever and it is fully in Ditto's control. (MDR Rule 11 / MDCG 2019-11 / MDCG 2025-6.) [6][7][9]

2. **[REC] Ship Article-50 AI disclosure before 2 Aug 2026.** Perceivable, point-of-interaction "this is AI-generated" labelling on summaries and any chat/Q&A. This applies *even if Ditto is never a medical device* and is cheap insurance. Watermarking of AI content has a grace period to **2 Dec 2026**. [4][5][2]

3. **[REC] Own the GPAI handoff.** Because compliance can't be outsourced to the model vendor, capture model-provider documentation (capabilities/limitations) and build Ditto's own logging, accuracy monitoring, and human-in-the-loop where outputs could be acted on. [23][24]

4. **[REC] Harden consent + sharing design now.** The care-circle sharing loop is a GDPR consent/lawful-basis question. Avoid bundled consent (the €1.5M Garante failure mode), give granular per-recipient control, log access, and over-invest in TOMs (the #1 fine driver). [14]

5. **[REC] Build a hallucination-safety story before competitors are forced to.** The Ontario AG and Whisper cases make "AI made up a treatment in my medical note" a board-level risk. A verification/uncertainty layer, source-grounding to the actual transcript, and a clear "review before relying" UX are both safety and **differentiation** as scrutiny rises. [15][19]

6. **[REC] Use EHDS as an architecture north star, not a 2026 deliverable.** Design for standardised formats and portability (xShare/Yellow Button compatibility) so Ditto is ready when primary-use kicks in (2029) and can tap secondary-use datasets for model validation later. [12][13]

7. **[REC] UK expansion: exploit the MHRA reliance route and AI Airlock.** If Ditto ever pursues device status, the international-reliance pathway (H1 2026) and AI Airlock sandbox can cut UK time-to-market; PMS 15-day incident reporting raises the operational bar. [26][29]

---

## 4. Risks & caveats / contrarian evidence

- **[CAVEAT] The Omnibus delay is not law yet.** The 6/13-May-2026 agreement is provisional; until OJ publication the original Aug-2026/2027 dates technically stand. Do not let "we have until 2028" become a planning assumption. [1][2]
- **[CONTRARIAN] The Class-I escape may be narrower than hoped.** Regulators and notified bodies read Rule 11 expansively; MDCG extended it to prognosis/prevention. Any feature that *recommends*, *flags*, *triages*, or *interprets* can flip Ditto into IIa. The "just summarising" defence weakens as the product becomes a "care intelligence layer." This is the biggest classification risk. [6][7]
- **[CONTRARIAN] "Patient-facing = lower scrutiny" is not guaranteed.** US states (California, Illinois, Nevada, NY, Utah) and AGs are now treating consumer health chatbots aggressively; Petrie-Flom argues health AI chatbots are *already* legally medical devices. The direction of travel is toward *more* oversight of patient-facing tools, not less. [43][42]
- **[CAVEAT] Transcription is the riskiest part of Ditto's own stack.** The Whisper/Nabla and Ontario evidence shows transcription/summarisation is precisely where hallucination harms cluster — Ditto is exposed to the same failure modes it would cite in competitors. [19][15]
- **[CAVEAT] GDPR fragmentation.** National DPAs and the EDPB note divergent interpretations of health-data rules; multi-country (NL/UK/EU) rollout means multi-regulator exposure. [32]
- **[CAVEAT — currency].** Several incident figures come from secondary aggregators (search-engine summaries of CBC/BMJ/Mount Sinai) rather than primary documents fetched in full; the Ontario AG primary page (CBC) returned 403 and was corroborated via OECD.AI and PBS instead. Numbers like "8/10," "49.6%," "52%," "5,000 doctors" should be re-verified from primaries before external citation.

## 5. Confidence & gaps

**High confidence:** EHDS dates and structure (2025/327) [11]; AI Act baseline timeline and Article 50 substance [4][21]; MDR Rule 11 logic [6]; the existence and gist of the major incidents [15][17][18][19][35].

**Medium confidence:** the *exact* Omnibus dates (provisional, pre-OJ — re-check on adoption) [1][2]; precise incident statistics (secondary sources). MDCG 2025-6's exact wording on the device/AI-Act boundary (read via secondary analysis, not the primary PDF in full).

**Gaps / Phase-2 dives that would pay off:**
1. **Device-classification opinion** — a focused legal/regulatory read on whether Ditto's specific summary + care-circle + any Q&A features stay non-device/Class I vs trip Class IIa. Highest value.
2. **EU-specific incident depth** — this scan found mostly North-American/global incidents; a targeted dive into Dutch/German/French DPA actions and any EU AI-health device field-safety notices would sharpen the EU picture.
3. **Article 50 implementation detail** — fetch the Commission's May-2026 draft transparency guidance in full to define exactly what compliant disclosure looks like for an AI summary (vs a chatbot).
4. **GPAI downstream-provider obligations** — concrete checklist of what Ditto inherits from building on a foundation model.
5. **EHDS technical conformance** — what the xShare/MyHealth@EU integration actually requires of an app, and timing of relevant implementing acts.

---

## 6. Sources

1. Gibson Dunn — EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines: https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
2. Travers Smith — EU agrees to delay key AI Act compliance deadlines: https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/
3. Kennedys — EU AI Act implementation timeline / next deadline: https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/
4. EU Artificial Intelligence Act — Article 50 transparency rules (practical guide): https://artificialintelligenceact.eu/transparency-rules-article-50/
5. Covington Global Policy Watch — 10 takeaways: Commission draft AI transparency guidelines (May 2026): https://www.globalpolicywatch.com/2026/05/10-takeaways-european-commission-draft-guidelines-on-ai-transparency-under-the-eu-ai-act/
6. Johner Institute — MDR Rule 11 classification: https://blog.johner-institute.com/regulatory-affairs/mdr-rule-11/
7. NAMSA — Classifying Medical Device Software (MDSW) under MDR/IVDR: https://namsa.com/resources/blog/eu-mdr-and-ivdr-classifying-medical-device-software-mdsw/
8. Greenlight Guru — Explaining MDCG 2019-11 (software qualification & classification): https://www.greenlight.guru/blog/mdcg-2019-11
9. Bird & Bird (Biotalk) — New MDCG guidance on medical device AI under the EU AI Act (MDCG 2025-6): https://biotalk.twobirds.com/post/102lr9z/navigating-the-interplay-of-mdr-and-aia-new-mdcg-guidance-on-medical-device-ai-u
10. European Commission — MDCG 2025-6 (interplay between MDR/IVDR and AI Act) PDF: https://health.ec.europa.eu/document/download/b78a17d7-e3cd-4943-851d-e02a2f22bbb4_en?filename=mdcg_2025-6_en.pdf
11. Arnold & Porter — EHDS Regulation published in the OJ: https://www.arnoldporter.com/en/perspectives/advisories/2025/03/european-health-data-space-regulation-published
12. EY Greece — Regulation (EU) 2025/327 establishing the EHDS: https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds
13. European Commission (DG SANTE) — EHDS Regulation overview: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
14. CMS Law — Life Science & Healthcare, GDPR Enforcement Tracker Report: https://cms.law/en/deu/publication/gdpr-enforcement-tracker-report/life-science-healthcare
15. OECD.AI — Ontario Medical AI Scribes Found to Produce Dangerous Errors and Hallucinations (incident, May 2026): https://oecd.ai/en/incidents/2026-05-12-76df
16. PBS NewsHour — AI transcription tool 'hallucinates' medical interactions: https://www.pbs.org/newshour/show/what-to-know-about-an-ai-transcription-tool-that-hallucinates-medical-interactions
17. BMJ Group — Substantial amount of medical information from popular chatbots inaccurate/incomplete: https://bmjgroup.com/substantial-amount-of-medical-information-provided-by-popular-chatbots-inaccurate-and-incomplete/
18. Mount Sinai — AI Chatbots Can Run With Medical Misinformation (2025): https://www.mountsinai.org/about/newsroom/2025/ai-chatbots-can-run-with-medical-misinformation-study-finds-highlighting-the-need-for-stronger-safeguards
19. Healthcare Brew — OpenAI's Whisper makes up words patients never said: https://www.healthcare-brew.com/stories/2024/11/18/openai-transcription-tool-whisper-hallucinations
20. Fortune — OpenAI's Whisper hallucinates more than any other tool, yet hospitals keep using it: https://fortune.com/2024/10/26/openai-transcription-tool-whisper-hallucination-rate-ai-tools-hospitals-patients-doctors/
21. Gardner Law — The EU AI Act compliance timeline: https://gardner.law/news/eu-ai-act-compliance-timeline
22. Emergo by UL — Risk categorization per the European AI Act: https://www.emergobyul.com/news/risk-categorization-european-ai-act
23. European Commission — Guidelines on obligations for General-Purpose AI providers: https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers
24. Latham & Watkins — EU AI Act: GPAI model obligations in force and final Code of Practice: https://www.lw.com/en/insights/eu-ai-act-gpai-model-obligations-in-force-and-final-gpai-code-of-practice-in-place
25. Healthcare.digital — This Week in European MedTech and HealthTech (29 May 2026; EUDAMED): https://www.healthcare.digital/single-post/this-week-in-european-medtech-and-healthtech-29th-may-2026
26. GOV.UK — MHRA expands AI Airlock programme with £3.6M funding boost: https://www.gov.uk/government/news/mhra-expands-ai-airlock-programme-with-a-36-million-funding-boost-over-three-years
27. MedRegs (MHRA blog) — How the AI Airlock is charting a path for regulating AI in healthcare: https://medregs.blog.gov.uk/2025/10/31/how-the-ai-airlock-is-charting-a-path-for-regulating-ai-in-healthcare-through-sandboxes/
28. DLRC — AI Airlock: MHRA's approach to AI in healthcare: https://www.dlrcgroup.com/ai-airlock-mhras-approach-to-ai-in-healthcare/
29. Emergo by UL — MHRA publishes revised roadmap of future regulatory framework for medical devices: https://www.emergobyul.com/news/mhra-publishes-revised-roadmap-future-regulatory-framework-medical-devices
30. Mills & Reeve — Regulating AI in healthcare: the UK government wants your input (Jan 2026): https://www.mills-reeve.com/blogs/life-sciences/january-2026/regulating-ai-in-healthcare-the-uk-government-wants-your-input/
31. ICO — What is special category data? https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/
32. BioSlice Blog — EDPB study on secondary use of personal health data for scientific research (Apr 2025): https://www.biosliceblog.com/2025/04/european-data-protection-board-publishes-study-on-secondary-use-of-personal-health-data-for-scientific-research/
33. EDPB — Guidelines 3/2025 on the interplay between the DSA and the GDPR (PDF): https://www.edpb.europa.eu/system/files/2025-09/edpb_guidelines_202503_interplay-dsa-gdpr_v1_en.pdf
34. CIDRAP — AI chatbots provide poor answers to medical questions half the time: https://www.cidrap.umn.edu/misc-emerging-topics/ai-chatbots-provide-poor-answers-medical-questions-half-time-study-finds
35. NPR — Pennsylvania sues AI firm over claims chatbot posed as a doctor (5 May 2026): https://www.npr.org/2026/05/05/nx-s1-5812861/characterai-chatbot-medical-advice-pennsylvania-lawsuit
36. CBS News — Pennsylvania suing Character.AI, chatbot posed as medical professional: https://www.cbsnews.com/news/pennsylvania-character-ai-lawsuit-chatbot-posed-as-medical-professional/
37. Psychiatric Times — The Psychiatrist's Preview of Legal Cases Against Big AI: https://www.psychiatrictimes.com/view/the-psychiatrist-s-preview-of-legal-cases-against-big-ai
38. Futurism — OpenAI sued over ChatGPT medical advice that allegedly killed student: https://futurism.com/artificial-intelligence/openai-sued-chatgpt-medical-advice-killed-student
39. University of Oxford — New study warns of risks in AI chatbots giving medical advice (Feb 2026): https://www.ox.ac.uk/news/2026-02-10-new-study-warns-risks-ai-chatbots-giving-medical-advice
40. News-Medical — AI chatbots give misleading health advice nearly half the time (Apr 2026): https://www.news-medical.net/news/20260421/AI-chatbots-give-misleading-health-advice-nearly-half-the-time.aspx
41. STAT — Woebot Health shuts down pioneering therapy chatbot (Jul 2025): https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/
42. STAT — FDA digital advisers confront risks of therapy chatbots (Nov 2025): https://www.statnews.com/2025/11/05/fda-digital-advisers-therapy-chatbots-regulating-generative-ai/
43. Petrie-Flom Center (Harvard) — Health AI chatbots are legally medical devices (May 2026): https://petrieflom.law.harvard.edu/2026/05/26/health-ai-chatbots-are-legally-medical-devices-its-time-the-fda-started-treating-them-like-it/
44. ACDIS — AI tool for hospitals fabricates text in transcription, researchers say: https://acdis.org/articles/news-ai-tool-hospitals-fabricates-text-transcription-researchers-say
45. Nature npj Digital Medicine — Regulatory databases of AI as a medical device (context incl. EMA AIM-NASH): https://www.nature.com/articles/s41746-026-02407-w
