# Brief C — Competitive Landscape

> Workstream C of the outside-in market/trend scan. Phase-1 depth: broad and well-sourced, map rather than exhaust. Created 2026-05-30. All dates and numbers labelled; estimates flagged. `[F]` = fact (sourced), `[I]` = inference, `[R]` = recommendation.

## 1. Executive summary

- **Ambient scribes are crossing onto the patient side — this is the single most important finding.** Abridge, Suki, Microsoft/Nuance DAX, and Nabla now generate patient-facing after-visit summaries as a feature inside their clinician tools. They remain B2B (sold to health systems), but the *output Ditto sells* (a plain-language visit summary for the patient) is becoming a free byproduct of clinician documentation. `[F]` [1][7][14][16][20]
- **The patient summary is being delivered to the patient *through the clinician's EHR portal*, not via a separate consumer app.** That is a structurally different distribution path than Ditto's consumer-app + care-circle loop, which is both a threat (incumbents own the visit) and an opening (their summary is institution-gated, not family-shareable). `[I]`
- **A direct B2C analog to Ditto just got funded: Kin Health, $9M seed (May 2026, led by Maveron), physician-built, free consumer app that records visits, produces plain-English summaries with next steps, and shares with family/caregivers — GoodRx-style referral monetization.** This is the closest thing to a Ditto clone, US-based. `[F]` [22]
- **Sword Health is a $4B, AI-first care platform, but it is an adjacent threat, not a direct one.** It does AI clinical *care* (MSK, pelvic, mental health) with clinicians + wearables, not patient summaries. The relevance is strategic: it shows the "AI-first care layer" thesis is being aggressively capitalized, and via the **Kaia Health acquisition ($285M, Jan 2026)** Sword now sits inside Germany's DiGA reimbursement and is consolidating European digital care. `[F]` [1][3][26][27]
- **EU scribes are real and well-funded: Nabla (France, $120M total), Corti (Denmark), Tandem (Sweden, $50M Series A), Tortus (UK, NHS), Heidi (AU but UK/EU heavy).** Most are B2B clinician tools; patient summaries are an emerging feature, not the core. None is yet a consumer-facing care companion. `[F]` [9][10][13][17][24][30]
- **Direct EU/global patient-summary competitors today: Kin (US), Medcorder (US), Hedy (US/global, 19-30 languages), plus the patient-facing edges of Abridge/DAX.** This category is nascent, fragmented, and mostly US-origin. No dominant EU consumer player yet — Ditto's 35k-user NL base + oncology focus + care-circle loop is a genuine, if narrow, lead. `[F][I]` [16][19][20][22]
- **Contrarian signal: the patient-recording category carries live legal/consent risk.** Two California health systems were sued in 2025 over recording visits without consent, with **Abridge** named as the scribe. Patient surveys show ~39% worry about documentation accuracy. This is a barrier *and* a trust-led differentiation opening for an EU/GDPR-native, consent-first product. `[F]` [32]
- **Net competitive read:** Ditto is not yet directly contested in EU consumer patient-summaries, but the moat is thin and closing from two directions — upstream (scribes capture the visit and hand patients a summary) and direct (funded US consumer clones like Kin). The defensible space is the **care-circle / family network + EU trust/regulatory posture + condition depth (oncology)**, not the summary artifact itself. `[I][R]`

## 2. Sword Health profile + threat read

| Attribute | Detail | Source |
|---|---|---|
| What it is | AI-first virtual care platform; "shifting healthcare from human-first to AI-first." Clinicians + AI + proprietary wearables. | [1][2] |
| Conditions covered | Physical/MSK pain (origin), pelvic health, movement health, and **mental health (Mind, launched Jun 2025)**, with M-band wearable. | [1][2][4] |
| Scale | 500,000+ members across 3 continents, 6.5M AI sessions, 1,000+ enterprise clients; claims ~$1B in avoided healthcare costs. (Company figures, mid-2025.) `[F, vendor-reported]` | [1] |
| Funding / valuation | $40M raised Jun 2025 at **$4B valuation** (led by General Catalyst); **~$380M total** to date. Plans to raise ~$500M in Q1 2026 for M&A. | [1][3][5] |
| Geography | HQ split US (NYC) + Portugal (European roots). US is the revenue core (self-insured employers, payers); aggressively buying into EU. | [26][27] |
| Recent strategic moves (~12 mo) | **Kaia Health acquisition, $285M, Jan 2026** — gains Germany DiGA reimbursement (covers 70M+ people) and consolidates European digital MSK. **Surgery Hero (UK) acquired Jan 2025** as UK beachhead. Mind mental-health launch Jun 2025. Stated intent to be "very active in acquisitions." | [3][26][27][28][29] |

**Threat read for Ditto:** 🟡 **Adjacent, not direct — but strategically instructive.** `[I]`
- Sword does **AI-delivered clinical care** (treatment, therapy, coaching). Ditto does **comprehension** (turning a real-world doctor visit into a patient-friendly summary). Different jobs, different buyers (Sword sells to employers/payers; Ditto is consumer/patient-led). No product overlap today. `[I]`
- Why it still matters: (1) it is the loudest proof that the **"AI care layer / care intelligence" thesis is being funded at scale and consolidating Europe via reimbursement** — exactly the pathway Ditto would need; (2) at $4B with $500M to deploy, Sword could enter or acqui-hire into the patient-companion space if it decided patient-side comprehension/coordination was strategic; (3) it validates **wearable + AI + reimbursement** as the playbook, raising the bar for what "care layer" credibly means. `[I]`
- **Obvious peer — Hinge Health:** the other digital-MSK giant. IPO'd May 2025 at $32/share, **~$2.6B valuation** (down ~60% from a $6.2B 2021 peak — a notable down-round signal for digital health). 532,000 members; Q2 2025 revenue $139M (+55% YoY). Same adjacent category as Sword; same "not a direct Ditto competitor" verdict. The Sword/Kaia deal is partly a defensive move against Hinge's global expansion. `[F]` [25][26]
- **Phase-2 flag:** If Merlijn weights "care intelligence layer" heavily, a deeper dive on *how* Sword/Hinge monetize via employer/payer + DiGA, and whether a patient-summary product could ride a similar reimbursement rail, would pay off (links to Brief B).

## 3. Scribes-to-consumer

These are ambient AI scribes — built to relieve clinician documentation burden. The question is whether they are encroaching on the **patient side** (patient-facing summaries) and whether they show **B2C ambition**.

| Player | Patient-facing summary? | B2C / consumer signals | Geography | Source |
|---|---|---|---|---|
| **Abridge** (US) | **Yes** — real-time AI Patient Visit Summary at 8th-grade reading level, plain-language plan + instructions. | Pure B2B (enterprise health-system contracts, no self-serve). Patient summary delivered *via the health system*, not a consumer app. Named in 2025 consent lawsuits. | US (250 large health systems; ~80M+ conversations/yr claimed 2025). | [7][14][32] |
| **Microsoft / Nuance DAX (Dragon Copilot)** | **Yes** — generates after-visit summaries, encounter summaries, referral letters. | Pure B2B, embedded in EHR (Microsoft healthcare stack). No consumer product. | US, Canada, UK GA; rollout to AT/FR/DE/IE (Oct 2025), **BE/NL early 2026**. | [16][17] |
| **Suki** (US) | **Yes** — patient summaries + clinical Q&A launched 2025 (Google Cloud / Vertex AI), at no extra cost. | Pure B2B (350-400+ health systems). Zoom Ventures investor. No consumer app. | US-centric. | [20][21] |
| **Nabla** (France) | **Partial / emerging** — context-aware agent "strengthens existing support for patient summaries"; core is clinician notes + billing/orders. | Pure B2B. $70M Series C Jun 2025 ($120M total). 85k+ clinicians, 150+ orgs, 20M+ encounters/yr. No B2C move. | France HQ; US-heavy customer base; EU. | [9][10] |
| **Corti** (Denmark) | Indirect — real-time documentation, structured notes, FactsR clinical-reasoning layer; summaries are clinician-side. | Pure B2B infrastructure/API for healthcare orgs. Mobile + Apple Watch app (clinician-facing). No B2C. | Denmark HQ; EU (DACH partnership via Maris); clinical-grade Danish ASR. | [11][12][13] |
| **Tortus** (UK) | Indirect — summarises consultation into clinic notes (clinician reviews before EHR save). | Pure B2B. NHS-trusted, DTAC-compliant, MHRA Class I (pursuing IIa). X-on partnership targets 3,500+ GP practices. | UK / NHS. | [30][31] |
| **Heidi Health** (AU) | **Yes (on request)** — generates patient summaries, referral letters; 2025 roadmap adds pre-chart + patient outreach; launched **Heidi Comms** (patient communications) Feb 2026. | B2B SaaS but **product-led / bottom-up freemium** (individual clinicians sign up free) — the closest scribe to a self-serve motion. Acquired UK's AutoMedica. Still clinician-buyer, not patient-buyer. | Melbourne HQ; UK/EU heavy; 2.5M consults/week, 190 countries. $96.6M raised. | [8][24] |
| **Suki / Tandem / others EU** — **Tandem Health** (Sweden) | Indirect — ambient note generation; patient benefit is "more time with patient," not a patient artifact. | Pure B2B. **$50M Series A Jul 2025** (Kinnevik). CE-marked Class IIa. Accurx partnership → ~98% of UK GPs. | Stockholm HQ; UK, DE, FR, ES, NL, NO, DK, FI. **Most EU-distributed scribe.** | [18][19] |

**Verdict on scribes encroaching on the patient side:** 🟡 **Partially yes — confirm and revise Merlijn's hypothesis.** `[I]`
- Merlijn's hypothesis ("purely B2B, but some offer patient summaries") is **correct and slightly understated**. The patient summary has gone from rare to a *standard feature* among the leaders (Abridge, DAX, Suki, Heidi) in the last ~12 months. `[F]`
- **But the encroachment is on the artifact, not the relationship.** None of these has a consumer app, a patient as the buyer, or a family/care-circle loop. The summary lands in the health system's portal (EHR/MyChart), gated by the institution, tied to one provider, English-only or limited-language, and not designed to be forwarded to a daughter in another city. `[I]`
- **The real strategic pressure:** if "good enough" patient summaries become a free byproduct of clinician scribing inside every EHR, the *standalone* value of "a summary" erodes. Ditto's defensibility cannot be the summary; it must be the **patient-owned, cross-provider, family-shareable, multilingual, trust-first** layer the scribes structurally cannot build (they serve the clinician/institution, not the patient). `[I][R]`
- **Heidi's product-led freemium + Heidi Comms (patient communications)** is the scribe most likely to drift toward patient-side; worth a Phase-2 watch. `[R]`

## 4. Direct patient-summary competitors

Who turns a recorded/transcribed medical visit into a **patient-friendly, shareable summary for the patient** — i.e. roughly Ditto's job?

| Player | One-line | Geography | Overlap with Ditto |
|---|---|---|---|
| **Kin Health** [22] | Free B2C app: records doctor visits → plain-English summary + next steps, share with family/caregivers, choose who manages vs. who's informed; GoodRx-style referral monetization. Physician-founded, $9M seed May 2026 (Maveron). | US | **Very high — near-clone.** Same job, same care-circle/sharing loop, same free-consumer model. Different geography (US). The most direct competitor identified. `[F]` |
| **Medcorder** [19] | Free app: record + transcribe doctor visits, securely share with family/caregivers, in-app group chat + appointment planning. Established (iOS/Android, updated Aug 2025). | US | **High.** Record + share-with-family is the same loop. Weaker on AI plain-language *summarization* (transcription-led); no oncology focus. `[F][I]` |
| **Hedy AI** [18][23] | AI visit assistant for patients/caregivers: real-time jargon translation, suggested questions, post-visit plain-language summary + searchable transcript, share with family; 19-30 languages. Freemium ($12.99/mo). | US-origin, multi-language/global | **High.** Patient-side comprehension + summary + family share + multilingual — overlaps Ditto's core and its EU/multilingual angle. Consumer self-serve. `[F]` |
| **Abridge / DAX / Suki (patient-summary edges)** [7][16][20] | Clinician scribes that emit a patient after-visit summary into the EHR/portal. | US (DAX → EU 2026) | **Medium / flanking.** Same artifact, opposite distribution (institution-gated, not patient-owned). Encroach on value, not on the relationship. `[I]` |
| **The Medical Memory** [—] | Provider-oriented platform to record/share medical videos with patients; older, provider-led. | US | **Low-medium.** Adjacent (recorded visit access) but provider-distributed, video-centric, not an AI summary/care-circle product. `[I]` |

**Read:** The direct category is **real but nascent, fragmented, and US-dominated.** No incumbent EU consumer patient-summary player surfaced in Phase 1. Ditto's NL/oncology base (35k+ users), care-circle growth loop, and EU-native trust posture are a defensible early lead — but **Kin and Hedy prove the model is being built and funded elsewhere**, and geography is the main thing currently protecting Ditto. `[I]`
**Phase-2 flag:** dedicated EU-language search (DE/FR/NL/ES/Nordic) for local patient-summary apps — a Phase-1 English-search bias may under-count regional players. `[R]`

## 5. Tiered competitive map

| Tier | Definition | Players | Threat |
|---|---|---|---|
| **Direct** | Does roughly Ditto's job (visit → patient-friendly, shareable summary for the patient). | **Kin Health** (US, near-clone), **Hedy AI** (multilingual, consumer), **Medcorder** (US, record+share). | 🟡 Real but geographically separated; model is being funded. |
| **Adjacent — encroaching** | Owns the visit and now emits a patient summary as a feature; could drift patient-side. | **Abridge, Microsoft/Nuance DAX, Suki, Nabla, Heidi (+ Comms)** — scribes with patient-facing summaries. **DAX entering NL/BE 2026.** | 🟡→🔴 if "free EHR summary" commoditizes the artifact. Watch Heidi (PLG) + DAX (NL/BE). |
| **Upstream capture** | Builds the broader "AI care layer," could absorb comprehension/coordination if it chose. | **Sword Health** ($4B, +Kaia/DiGA), **Hinge Health** (public, ~$2.6B). | 🟡 Adjacent today; deep-pocketed, EU-consolidating, capable of entering. |

## 6. Implications for Ditto

`[R]` — recommendations for Merlijn's synthesis, not conclusions to act on blindly.

1. **The summary is not the moat.** Within 12 months, a competent patient after-visit summary is a free EHR byproduct (Abridge/DAX/Suki). Ditto must articulate defensibility as the **patient-owned, cross-provider, family-shareable, multilingual, consent-first care layer** — the things institution-bound scribes structurally cannot do.
2. **The care circle is the strongest differentiator — and Kin just validated it as a wedge.** Kin and Medcorder both build family/caregiver sharing. Ditto should treat the care-circle growth loop as the core competitive asset and out-build it (roles, permissions, multi-provider aggregation), not the summary engine.
3. **EU + GDPR + consent-first is a real, timely advantage.** US consent lawsuits (Abridge) and ~39% patient accuracy concern make trust a differentiator. An EU-native, consent-by-design, GDPR-clean product can position trust as a feature the US-origin field has not earned. (Links to Brief A.)
4. **Watch DAX's NL/BE entry (early 2026) closely.** Microsoft putting clinician scribes with after-visit summaries into Dutch/Belgian health systems is the most direct near-term pressure on Ditto's home turf — institution-side, but it changes patient expectations.
5. **Reimbursement is the upstream battle.** Sword's Kaia/DiGA play shows the EU "care layer" prize is unlocked via reimbursement, not app-store revenue. If Ditto wants to be a "care intelligence layer," the reimbursement pathway (Brief B) is the decisive lever, and the big players are already moving on it.

## 7. Confidence & gaps

| Item | Confidence | Note |
|---|---|---|
| Scribes now emit patient summaries | **High** | Multiple primary/vendor sources confirm Abridge, DAX, Suki, Heidi. |
| Scribes have no consumer/B2C product today | **Medium-High** | True as of Phase 1; Heidi's PLG + Comms is the drift risk. |
| Kin Health = near-direct Ditto analog | **High** | Primary TechCrunch source, May 2026. |
| Sword scale figures (500k members, $1B saved) | **Medium** | Vendor-reported, not independently audited. |
| No dominant EU consumer patient-summary player | **Medium** | English-search bias; needs EU-language Phase-2 sweep before asserting. |
| Hinge/Sword "could enter patient-summary" | **Low (inference)** | No stated intent; capability + capital only. |

**Gaps to close in Phase 2:** (a) native-language EU competitor sweep (DE/FR/NL/ES/Nordic); (b) Heidi/DAX patient-side roadmap depth; (c) how patient summaries actually reach EU patients (portal vs. app) market-by-market; (d) Sword/Hinge reimbursement mechanics as a template for a Ditto care-layer (joins Brief B).

## 8. Sources

1. https://swordhealth.com/newsroom/sword-health-raises-40m-launches-mind
2. https://www.armilar.com/articles/sword-health-raises-40-million-and-unveils-always-on-ai-mental-health-solution-to-address-the-global-mental-health-crisis
3. https://hlth.com/insights/news/sword-health-secures-40m-funding-at-4b-valuation-launches-mental-health-platform-2025-06-18
4. https://www.fiercehealthcare.com/digital-health/sword-health-banks-40m-launches-ai-based-mental-health-solution
5. https://tech.eu/2025/06/17/sword-health-raises-40m-at-4b-valuation-to-expand-ai-first-care-into-mental-health/
7. https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time
8. https://www.heidihealth.com/en-us
9. https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/
10. https://www.fiercehealthcare.com/ai-and-machine-learning/nabla-banks-70m-series-c
11. https://www.corti.ai/news/corti-launches-mobile-app-for-ambient-clinical-documentation-on-the-go
12. https://www.corti.ai/news/introducing-factsr-by-corti
13. https://www.corti.ai/news/corti-and-maris-healthcare
14. https://www.beckershospitalreview.com/healthcare-information-technology/ai/uchealth-selects-systemwide-ai-scribe/
16. https://www.microsoft.com/en-us/industry/blog/healthcare/2024/08/08/dax-copilot-new-customization-options-and-ai-capabilities-for-even-greater-productivity/
17. https://www.nuance.com/healthcare/dragon-ai-clinical-solutions/dax-copilot.html
18. https://tandemhealth.ai/
19. https://medcorder.com/
20. https://www.suki.ai/press-releases/suki-launches-patient-summarization-and-clinical-qa-for-doctors-with-google-cloud/
21. https://www.healthcaredive.com/news/suki-70-million-Series-D-funding/729573/
22. https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/
23. https://www.hedy.ai/patient-ai-tool
24. https://www.mobihealthnews.com/news/anz/melbourne-based-heidi-health-expand-ai-scribe-capability-new-17m-fund
25. https://www.cnbc.com/2025/05/21/hinge-health-prices-ipo-at-32-the-top-end-of-expected-range.html
26. https://www.galengrowth.com/in-the-battle-for-digital-health-supremacy-sword-healths-european-roots-fuel-a-global-power-play/
27. https://www.fiercehealthcare.com/ai-and-machine-learning/sword-health-buys-kaia-health-285m-deal-expand-its-footprint-us-germany
28. https://kaiahealth.com/newsroom/press-releases/kaia-health-joins-sword-health/
29. https://hlth.com/insights/news/sword-acquires-kaia-health-extending-its-lead-in-ai-health-and-expanding-reach-to-100-million-people-worldwide-2026-01-29
30. https://tortus.ai/
31. https://www.digitalhealth.net/2025/09/major-nhs-ai-scribe-trial-shows-transformative-patient-benefits/
32. https://www.emarketer.com/content/health-systems-hit-with-lawsuits-over-ai-recorded-visits-without-consent
