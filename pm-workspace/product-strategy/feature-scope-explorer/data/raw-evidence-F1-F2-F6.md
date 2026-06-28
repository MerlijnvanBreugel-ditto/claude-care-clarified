# Raw evidence — F1 (symptom tracking), F2 (journaling), F6 (proactive assistants)
_Extracted 2026-06-25. Raw material for features.json._

## Understanding (consult summary / trusted info / treatment explained / visit prep) — F6, F2
- **Players**: Ada Health (symptom assessment/navigation; ~€37M FY24, ~$201M raised; EU-MDR Class IIa Dec 2022; CORE); Outcomes4Me (AI navigation+guidelines+trial-matching; 280k+ users, $21M May 2025/$38M total; 7 of top-10 cancer pharma are customers); OWise/Px HealthCare (shared-decision tools, question prompts; CE-marked, NHS-accredited, NL origin); Ditto positioned at Rung 0.
- **Popularity**: Mature as a job but structurally episodic ("no return loop").
- **Retention**: Weak by nature — "you use it when sick." Ada's challenge is monetization not retention (frequency is episodic).
- **Reimbursement**: Rung 0 understanding is CE-exempt (only AI-Act Art.50 chatbot disclosure). Not reimbursed at this rung. Ada hit Class IIa once advising on individual symptoms.
- **Who pays**: Not patients. Ada = consumer sub + enterprise. Outcomes4Me = pharma RWD/recruitment. Every pure-consumer AI assistant (K Health, Ada, Healthily) pivoted from D2C to B2B.
- **Takeaway**: Understanding is Ditto's free CE-exempt base — real trust, episodic, unmonetizable alone; must feed something higher up the ladder.

## Medical diary / journaling — F2
- **Players**: CaringBridge (300k-400k daily, new page ~12 min, ~1,600 msgs/hr, 25 yrs; nonprofit FY24 rev $10.7M/exp $11.6M/net -$0.9M; CORE); Day One (Automattic; ~$34.99/yr; ~200k subs + 15M lifetime downloads; Shared Journals up to 30; CORE); Finch (self-care wrapped in virtual-pet game; bootstrapped ~$30M ARR, ~9M DAU «unverified»; best-in-class D30; journaling is FUEL); Rosebud (AI journal/mentor $12.99/mo, $6M seed 2025, long-term memory); Mindsera/Reflectly/Stoic; Kanker.nl (NL cancer peer blogs, ~41k participants, ~1,850 bloggers, KWF/NFK/IKNL funded); PatientsLikeMe ($100M raised, sold data to pharma, fire-sale to UnitedHealth 2019).
- **Popularity**: Demand enormous; as a *paid* business barely survives the filter.
- **Retention**: Notoriously fragile standalone (median D15 ~3.9%, >80% gone by day 10). Two engineered exceptions: CaringBridge audience/guestbook loop (socially enforced) and Finch game loop. AI memory (Rosebud) removes the blank page + creates "it knows me."
- **Reimbursement**: None anywhere. Serious-illness narrative "never been a paid product."
- **Who pays**: Patient essentially never. Nonprofit/donations (CaringBridge), charity (Kanker.nl), platform absorption (Day One→Automattic), data-to-pharma (PatientsLikeMe — detonated on trust/GDPR), or game wrapper (Finch).
- **Takeaway**: Don't build "a journal." Build what journaling is fuel for — the care journey shared with loved ones (guestbook mechanic), paid B2B, with AI memory as the one defensible asset.

## AI question-answering — F6
- **Players**: K Health (AI intake + clinician closes loop; licensed to Cedars-Sinai, Mayo, MGB, Northwell; ~$900M val 2024, ~$380M raised, last public rev $52M 2022); Healthily (ex-Your.MD, pivoted to B2B navigation; ~$139M raised); Counsel Health (physician-supervised AI front door; $25M Series A a16z/GV + $11M seed, >100k members); Ada (MDR Class IIa).
- **Retention**: Weak for pure-AI; strong only with human/health-system attached. Episodic standalone.
- **Who pays**: B2B health systems/insurers. "Pure-consumer AI primary care didn't monetize; wrapping it in a trusted provider's brand did."
- **Takeaway**: AI Q&A retains and pays only with a human-in-the-loop wrapper.

## Proactive care advice — F6
- **Players**: Omada ($170M FY24 +38%; 752k members; IPO 2025 ~$1.1B; CVS Caremark, Cigna); Lark (AI-first coach; Elevance/Anthem + BCBS; ~$185M+ raised; RCT AI-vs-human parity); Vida (~$110.9M ARR 2025); Thrive AI Health (OpenAI Fund + Huffington; non-functional demo).
- **Popularity**: "The only rung of the intelligence ladder with proven retention AND proven monetization."
- **Retention**: Strongest in the field — but bought via human(-supervised) coach in loop (2-3× 90-day retention). Pure-AI nudges/streaks retain 30-60d then decay unless RCT parity (Lark).
- **Reimbursement**: US employer/PMPM (doesn't transplant to NL). EU = DiGA/statutory insurer (€234M cumulative to end-2024, ~€221/3-mo) but requires MDR device. Pharma-sponsored (Sidekick/Pfizer) in EU.
- **Who pays**: Employers/payers/PBMs (US); pharma + statutory insurers (EU). Never consumer as primary engine.
- **Takeaway**: Advice is where money lives, but only via coach-in-loop + B2B; the same step that unlocks money crosses the MDR line.

## Symptom triage — F6
- **Players**: Ada (MDR Class IIa, ~€37M FY24); K Health; Healthily; Counsel Health.
- **Retention**: Does not retain — structurally episodic.
- **Reimbursement**: Individualised triage interpreting the person's data → MDR Class IIa (Rule 11) + AI-Act high-risk. Ada is the reference.
- **Takeaway**: Credential-builder (CE moat) but episodic; valuable as B2B navigation with a human owning the individualised step.

## Lab & result interpretation — F6
- Not a standalone product. Closest mechanic: Hello Heart (interprets your BP), Ada (interprets symptoms). A continuous "what changed since last scan" narrative is described as a Ditto *opportunity*, not an existing player.
- **Reimbursement**: Interpreting an individual's results to recommend action = MDR Class IIa / AI-Act high-risk (MDCG 2019-11, Rule 11). "The cliff."
- **Takeaway**: Crosses the individualised-advising line into Class IIa — keep AI to explaining, let a human own "what to do."

## Medication intelligence — F6/F1
- **Players**: MyTherapy/smartpatient (med reminders+adherence; 12M+ users, 100M+ monthly engagements, 1B+ confirmed intakes; free to patients, business is B2B pharma PSP/RWD/DTx — Merck/Novartis/Pfizer/Bayer/Sanofi; CORE); mySugr (bolus calc+reminders; 3.5M+ users; Pro $2.99/mo, real money in Roche's reimbursed ~€999/yr bundle); Sweetch (behavioural-AI for Abbott/Dexcom/NovoCare); Sidekick (pharma adherence).
- **Retention**: Daily by design (pill times). Among the stickier mechanics.
- **Reimbursement**: Not the app directly; mySugr rides reimbursed device bundle (Germany).
- **Who pays**: Pharma (adherence ROI + RWD), not patients.
- **Takeaway**: Adherence is genuinely daily and pharma-funded (most reachable EU patron) — but the patient is the product; fits a pharma-sponsored oncology program.

## Light accountability — F6/F2
- **Players**: Finch (Accountability Buddies; ~$30M ARR, ~9M DAU, best-in-class D30); Omada/Lark/Hello Heart (human coach = retention engine); Visible (daily pace score governs behavior).
- **Retention**: Strongest, most durable driver — human/accountability support = 2-3× 90-day retention. Streaks/gamification alone decay after 30-60d.
- **Who pays**: Rides B2B coaching/payer (Omada) or game-sub (Finch); not paid standalone.
- **Takeaway**: The single best retention unlock — but works through a human (or care-circle) in the loop, not AI streaks.

## Second-opinion & trial pathways — F6/F1
- **Players**: Outcomes4Me (trial-matching via ClinicalTrials.gov on cancer type/location/biomarkers = the *differentiated hook*; 280k+ users; 7 of top-10 cancer pharma); PatientsLikeMe (trial recruitment, data sold to pharma).
- **Retention**: Episodic, decision-driven (around treatment decisions/scans).
- **Who pays**: Pharma (trial recruitment). The patient is the product.
- **Takeaway**: Strong differentiated hook but money is pharma recruitment — brand/GDPR risk; EU trial landscape makes the US engine less transplantable.

## Self-updating health profile — F6/F1/F2
- No dedicated player. Built from mechanics: Rosebud long-term memory (the defensible analog); MyTherapy/CANKADO longitudinal logs. Framed as a Ditto multiplier, not an existing product.
- **Retention**: Indirect — AI memory is "the one genuinely defensible journaling asset"; compounds + creates switching cost.
- **Takeaway**: A continuous AI-held health profile is the compounding switch-cost asset Ditto is uniquely positioned to own — frame as memory/multiplier, not a feature to sell.

## Symptom overview + correlations — F1
- **Players**: Bearable (correlation/insight reports; 900k members; freemium $34.99/yr or $6.99/mo, no ads no pharma; bootstrapped, beloved; CORE); CANKADO PRO-React Onco (daily dynamic questionnaires + auto recommendations; DiGA-reimbursed €499.80); Kaiku/Noona (algorithmic grading of symptom panels).
- **Retention**: Bearable closest to a real daily habit in F1 — insight loop is intrinsic (no clinician needed). But engaged users are a minority of 900k. Oncology ePRO is treatment-gated, decays after therapy.
- **Reimbursement**: Bearable none; CANKADO DiGA €499.80 (Germany).
- **Who pays**: Bearable = patient subscription (ONLY F1 player that passes on patient-pay) — but ARPU/conversion small, caps at small-business scale. CANKADO = statutory payer (DiGA).
- **Takeaway**: Self-knowledge-via-correlations is the one tracking mechanic that retains without a clinician — but patient-pay caps small unless bundled.

## Wearable integration — F1/F6
- **Players**: Visible (morning HRV via phone camera/armband → daily pace/stability score → overexertion alerts; 250k+ users; Plus sub bundled with armband; long-COVID/ME-CFS/POTS; CORE — best frequency engine in the brief); Hello Heart (FDA-cleared BP cuff+app; $70M raised; Amwell distribution Oct 2024; claims 21 mmHg drop); mySugr (CGM/meter); Sweetch (engagement for Dexcom/Abbott CGM).
- **Retention**: The device/measurement IS the habit — "a connected device is a cheaper retention engine than a human coach." Visible daily + durable (score drives a daily decision in a chronic condition).
- **Reimbursement**: Hello Heart BP feedback = individualised advising → MDR Class IIa in EU. mySugr bundle reimbursed (Germany ~€999/yr).
- **Who pays**: Subscription + hardware bundle (Visible, mySugr) or B2B employer/plan (Hello Heart).
- **Takeaway**: A wearable manufactures durable daily frequency cheaply — but needs a bundle, and BP/result feedback crosses into Class IIa.

## Candidate missing features (from F1/F2/F6)
- **Alert-to-responder loop** (graded report → someone acts): Kaiku (grade ≥3 → care unit calls; Elekta, 40+ EU clinics), Noona (Varian/Siemens), CANKADO, Basch RCTs (PRO-TECT HR 0.84 time-to-ER). F1's #1 implication: "Build the alert-to-action loop, not a tracker." Without a responder, tracking is "a graveyard feature."
- **Care-circle guestbook / shared updates with reactions**: CaringBridge (300k+ daily), Day One Shared Journals, Finch, Kanker.nl. F2's "highest-leverage idea." The summary IS the post; the care circle IS the guestbook.
- **Human navigator / nurse touchpoint**: Jasper Health (oncology social workers; CMS nav G-codes; ~$31M raised), Omada/Lark/Hello Heart (coach), K Health/Counsel (clinician-in-loop). Strongest, most durable retention driver (2-3× 90-day). Also how survivors deliver Rung-2 value without the Class IIa bill.
- **Virtual-pet / care-relationship game loop**: Finch (~$30M ARR, ~9M DAU). Guilt-removal unlock.
- **Trial-matching engine**: Outcomes4Me (the differentiated hook), PatientsLikeMe. Oncology-relevant; pharma-funded.
