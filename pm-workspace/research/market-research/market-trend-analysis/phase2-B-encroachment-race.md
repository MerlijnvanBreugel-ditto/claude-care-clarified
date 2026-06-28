# Phase-2 Dive B — The Encroachment Race (Native-Language EU Sweep)

> Phase-2 deep dive. Scope: the **summary/recording artifact only** — who is taking Ditto's job (record/transcribe/summarize a medical visit into a patient-friendly output) on Ditto's EU home turf, and how fast. The relationship/care-circle layer is a separate dive and is deliberately out of scope here. Searched in **Dutch, German, French, plus English**, because the Phase-1 English-only sweep under-counted regional players (flagged in Brief C §4 and §7). Scan date: 2026-05-30. `[F]` = fact (sourced), `[I]` = inference, `[R]` = recommendation. Estimates labelled.

---

## 1. Executive summary

- **The native-language sweep confirms Phase-1's fear: the patient-summary artifact is being attacked from at least four directions on Ditto's home turf, and several are already live in NL/BE — but almost none combines what Ditto does (patient-initiated + cross-provider + multilingual + recording-based).** `[I]`
- **The most under-counted layer was German B2C document-summarizers.** Simply Onno (Berlin) has generated **60,000+ free plain-language summaries since end-2024, "thousands of users daily," won DIE WELT's Best AI Startup 2025, and is no-account/privacy-first.** Plus mein-arztbefund.de (15 languages, ~€7.99/report) and Befino. These are *document* translators, not recording-based, and not care-circle products — but they are real consumer traction on the comprehension job, in a major EU market, that English search entirely missed. `[F]` [12][13][14][15][16]
- **The "Doctolib-type" player Merlijn flagged is real and dual-pronged.** Doctolib's **clinician consultation assistant** (live since Oct 2024, 6M+ consultations) already **sends the patient a digital after-visit summary** (diagnosis, treatment, prescriptions); and **Doctolib Parents**, an AI patient assistant, launches **early 2026** for parents of under-4s, freemium, with French-pediatric-society backing. Doctolib is the scheduling/portal incumbent most aggressively walking onto the patient side. `[F]` [6][7][8][9]
- **The EHR itself is now shipping the artifact to NL/BE patients.** ChipSoft (HiX — the dominant NL/BE hospital EHR) runs a **"Patiëntvriendelijke brief" GenAI project** (with UZ Brussel + AZ Maria Middelares) that converts letters to a plain-language summary, returns it to HiX, and delivers it via eHealth platforms like COZO. Antwerp's **ZAS hospital went LIVE on 2026-04-16** with patient-facing B1-level letter summaries (~40,000 letters/year, rheumatology + nephrology, delivered via the Belgian gov portal + patient portal). This is the artifact becoming a free portal byproduct, in production, on home turf. `[F]` [10][17][18]
- **Epic in NL is more clinician-mediated than Brief E implied — an important correction.** The live NL deployments (ETZ Tilburg, UMCG Groningen) are GPT-4 **draft answers a clinician reviews before the patient sees them**, plus clinician-side patient-friendly summaries of op-reports. Patient-direct AI summaries were a *planned* pilot. **Ask Emmie** (the patient-facing chatbot) was only unveiled at **HIMSS, ~March 2026, with no confirmed EU/NL deployment.** So Epic's patient-direct encroachment in NL is real and inevitable but **not yet shipped to patients** — the window is wider than Brief E suggested. `[F][I]` [4][19][20]
- **DAX/Dragon Copilot is now confirmed GA in NL + BE as of 2026-02-12** (Phase-1 said "early 2026" — now dated). But the NL/BE release is **clinician documentation only**; the patient-facing after-visit summary is not part of the Benelux launch. `[F]` [21][22]
- **Nordics: clinician scribes only, no patient-facing consumer summary app surfaced.** Leapscribe (Sweden), Tandem Health (Sweden, which **acquired Dutch scribe Juvoly** — 200k consults/mo, 1,500 GP practices), and Region Dalarna/Syddanmark pilots are all B2B clinician note-generation. The patient-facing layer in the Nordics is academic/research-stage, not a shipped competitor. `[F]` [2][23][24][25]
- **Net read:** The artifact is commoditizing fast on home turf — portal/EHR delivery (ChipSoft, Epic, eventually Doctolib + DAX) plus free B2C document-summarizers (Simply Onno et al.). But **every one of them is single-provider, document- or portal-bound, and none is a patient-owned, recording-based, cross-provider, multilingual, family-shareable product.** The closest true analog found, **Clareco CoPilot (NL+BE)**, validates the model but is tiny (3 orgs testing, €0–10k revenue). The gap Ditto occupies is still open — but it is narrowing from the portal side, not the consumer-app side. `[I][R]`

---

## 2. Native-language EU player sweep

New players surfaced by NL/DE/FR/BE-language search (excludes those already in Brief C/E: Nabla, Corti, Tandem, Tortus, Heidi, Abridge, DAX, Suki, Kin, Hedy, Medcorder, Epic, MedMij, NHS App). "Patient summary?" = does the *patient* get a plain-language output.

| Name | Country | B2B / B2C | Patient summary? | Traction | Source |
|---|---|---|---|---|---|
| **Simply Onno** | DE (Berlin) | **B2C** | **Yes** — upload doc → plain-language summary; free + premium | **60,000+ summaries since end-2024; "thousands daily"; DIE WELT Best AI Startup 2025; self-funded; no-account/privacy-first** | [12][13] |
| **mein-arztbefund.de** | DE | **B2C** | **Yes** — upload letter/lab/PDF → plain German summary | Live since Aug 2025; **15 languages**; med-tracker + lab overview; ~€7.99/report; iOS app | [14][15] |
| **Befino** | DE | **B2C** | **Yes** — "Arztbefund übersetzen" | iOS app store listing (id6760299903); early-stage, traction not disclosed | [16] |
| **Doctolib (Consultation Assistant)** | FR (EU-wide) | **B2B → patient output** | **Yes** — post-consult digital summary (diagnosis, treatment, prescriptions) sent to patient | **6M+ consultations since Oct 2024 launch** | [6][8] |
| **Doctolib Parents** | FR | **B2C (freemium)** | Partial — AI chat for parenting/child-health Q&A, shareable with clinicians; **not** a visit-summary | Launching **early 2026**, under-4s first; backed by French pediatric societies | [7][9] |
| **Loquii (MediStory)** | FR | **B2B** | Indirect — structured consult summary into clinician software | Embedded in MediStory EHR; clinician-side; sovereign/secure positioning | [11] |
| **Juvoly** | NL | **B2B** | Indirect — live transcript → medical report; 90+ languages incl. Frisian/dialects | **200k+ consults/month, 1,500+ GP practices; acquired by Tandem Health (SE)**; data stays on NL servers | [2][3] |
| **Autoscriber** | NL | **B2B** | Indirect — structured summary into HiX; clinician-side | Integrated in ChipSoft HiX; ~€89/mo entry pricing | [1][10] |
| **OurMind** | NL | **B2B** | Indirect — clinician documentation | ~€219/yr entry pricing | [1] |
| **SmartIntake AI** | NL | **B2B** | Indirect — AI conversation summaries in practice software | Integrated in MijnDiAd practice software | [1] |
| **ChipSoft "Patiëntvriendelijke brief"** | NL/BE | **B2B (EHR feature)** | **Yes** — letter → line-by-line + plain summary, returned to HiX, delivered via COZO | Innovation project w/ **UZ Brussel + AZ Maria Middelares**; FHIR interface; pilot/rollout, no public live date | [10][17] |
| **ZAS (Ziekenhuis aan de Stroom)** | BE (Antwerp) | **B2B (hospital)** | **Yes** — original + line-by-line + B1-level summary + med glossary | **LIVE 2026-04-16; ~40,000 letters/yr; rheumatology + nephrology; via mijngezondheid.belgie.be + mijnZAS.be** | [18] |
| **Clareco CoPilot** | NL + BE | **B2B2C** (free patient, doctor subscription) | **Yes** — patient + doctor record together → transcript → patient gets downloadable doc, 22 languages | **Early-stage: 3 orgs testing; €0–10k revenue; live in app stores** | [26] |
| **Bingli** | BE (Flanders) | **B2B** | Indirect — pre-consult intake + saves ~5 min/consult | Flemish AI tool, multiple practices | [27] |
| **Squire** | BE (Ghent) | **B2B** | Indirect — records consult → auto GP report | Pilot w/ 9 GPs; free trial for all Flemish doctors (Jan 2025) | [28] |
| **CareConnect AI (Corilus)** | BE | **B2B** | Indirect — records/documents into patient file; NL + FR | Corilus (large BE/NL practice-software vendor) | [29] |
| **Spexter / ExplainMed** | BE (Ghent) | **B2C** | **Yes** — scan report → short simple summary + term definitions | €125k Flemish gov funding (Jan 2024); ~150 cardiology terms; narrow/early | [30] |
| **Leapscribe** | SE | **B2B** | No — clinician journal draft only | Used in Swedish regions; real-time record-to-note | [24] |
| **Region Dalarna / Syddanmark pilots** | SE / DK | **B2B (public)** | No — record → into medical record | Regional public-health pilots; clinician-side | [25][31] |

**Read on the sweep:** `[I]`
- **The biggest English-search blind spot was the German B2C document-summarizer category** (Simply Onno + mein-arztbefund + Befino). These do the *comprehension* half of Ditto's job, for consumers, with real traction (Simply Onno 60k+ summaries) — but they are **document-upload, not recording-based**, single-shot, and have no care-circle or cross-provider memory. They are the clearest proof the *comprehension artifact* is being consumerized in a major EU market.
- **The recording-based, patient-output, cross-provider, multilingual combination — Ditto's actual product — was matched by exactly one player: Clareco CoPilot (NL+BE)**, and it is pre-traction. No funded, scaled, native-EU direct clone exists *today*. Geography + the recording+care-circle combination still protect Ditto.
- **Everything else is either clinician-side (Juvoly/Autoscriber/Loquii/Bingli/Squire/Leapscribe — the patient benefit is "more doctor time," not an artifact they own) or portal-bound (ChipSoft/ZAS/Epic — the patient gets a summary but it is one hospital's letter, in one portal, not patient-initiated or cross-provider).**

---

## 3. Scheduling / portal encroachers

The question: are the booking/portal incumbents that already own the patient relationship adding patient-facing visit summaries / AI?

| Player | Type | Patient-facing summary / AI move | Status & timing | Source |
|---|---|---|---|---|
| **Doctolib** (FR, EU-wide) | Scheduling + portal giant | (a) Clinician **Consultation Assistant** sends patient a **digital after-visit summary** (diagnosis/treatment/prescriptions); (b) **Doctolib Parents** AI patient assistant | (a) **Live since Oct 2024, 6M+ consults**; (b) **Doctolib Parents early 2026**, under-4s first, freemium | [6][7][8][9] |
| **ChipSoft / HiX** (NL/BE — dominant hospital EHR) | EHR + patient portal | **"Patiëntvriendelijke brief"** GenAI: letters → plain-language summary in portal/COZO; plus SNOMED-based "infobutton" explaining diagnoses in Franciscus Gasthuis portal | Innovation/pilot (UZ Brussel, AZ Maria Middelares); infobutton live at Franciscus; no public GA date | [10][17] |
| **Pharmeon / Uw Zorg Online** (NL — GP portal/app) | GP patient portal | No recording-to-summary. Has **Klinik** AI triage (reimbursed from 2026-01-01), **Kijksluiter** plain-language med videos (~6,500), SmartConsult intake. Patient-friendly, but not a visit summary. | Triage reimbursed Jan 2026; no visit-summary product | [32][33] |
| **Zorgdomein** (NL — referral/transfer infra) | B2B referral plumbing | No patient-facing visit-summary product surfaced | — | — (absence noted) |
| **MedMij / PGO** (NL — mandated PHR) | Data-aggregation layer | Raw data only; "patient-friendly terms" on roadmap, no AI summary (per Brief E) | Roadmap H2 2026 | (Brief E [12][13]) |

**Read:** 🟡→🔴 on the portal/scheduling axis. `[I]`
- **Doctolib is the encroacher to watch.** It owns booking + the patient app + (now) the clinician's documentation, and it is already pushing a patient summary out the back of the consultation, plus a standalone patient AI assistant. Today the summary is single-provider and the patient AI is narrow (under-4 parenting). But Doctolib has the distribution Ditto has to fight for. It is **broad and shallow** where Ditto is **narrow and deep (oncology, recording, care-circle)**.
- **ChipSoft is the structural threat in NL/BE hospitals.** Because HiX is the dominant hospital EHR, a "patient-friendly letter" shipped as a HiX feature reaches patients at near-zero marginal cost, gated by the hospital. ZAS proves it can go live (Apr 2026). This is exactly the "summary becomes a free EHR byproduct" thesis from Brief C — now confirmed in production on home turf.
- **Dutch GP-side portals (Pharmeon/Uw Zorg Online) are not yet in the visit-summary game** — their AI is triage + med-info, not recording-to-summary. That sub-segment (GP visits, not hospital) is comparatively open.

---

## 4. Encroachment-speed timeline on NL home turf

When does an in-portal/EHR patient AI summary become standard-of-care in NL? Best-evidence timeline (facts dated; the "standard-of-care" call is inference):

| Date | Event | Patient-direct? | Source |
|---|---|---|---|
| Aug 2023 | ETZ Tilburg pilots GPT-4 draft answers to patient portal questions (first outside US); ~1,000+ patient messages/week | **No** — clinician reviews before patient sees it | [19] |
| Nov 2023 | UMCG = first European hospital to deploy the Epic AI chatbot in written patient contact (with ETZ, Amsterdam UMC via Epic NL association) | Clinician-mediated | [20] |
| ~2024–2025 | Epic NL adds clinician-side patient-friendly summaries of op-reports / discharge letters | Indirect (helps clinician produce patient/GP letter) | [4][19] |
| Oct 2024 | Doctolib Consultation Assistant live; patient gets digital visit summary | **Yes** (single-provider, FR-led EU) | [6][8] |
| Jan 2024 → ongoing | ChipSoft "Patiëntvriendelijke brief" project (UZ Brussel, AZ Maria Middelares); Franciscus infobutton | **Yes** (portal-gated, pilot) | [10][17] |
| 2026-02-12 | DAX / Dragon Copilot GA in **NL + BE** | **No** (clinician documentation only in Benelux release) | [21][22] |
| Early 2026 | Doctolib Parents AI patient assistant (under-4s) | **Yes** (narrow domain, not visit-summary) | [7][9] |
| **2026-04-16** | **ZAS Antwerp LIVE: patient-facing B1 letter summaries, ~40k/yr, rheum + nephro** | **Yes (live, in production)** | [18] |
| ~Mar 2026 | Epic **Ask Emmie** unveiled at HIMSS — patient chatbot (explains labs, scheduling) | Yes, **but no confirmed EU/NL deployment** | [20] |
| **2026–2027 [I, estimate]** | NL academic hospitals (Epic sites) begin shipping patient-direct AI summaries as Emmie/AI Patient Summaries reach EU; ChipSoft "Patiëntvriendelijke brief" generalizes across HiX sites | Becoming patient-direct | inference |
| **~2027–2028 [I, estimate]** | In-portal patient AI summary plausibly **standard-of-care for hospital encounters** in NL/BE, gated by the hospital's EHR (Epic or HiX) | — | inference |

**Speed read:** `[I]`
- **Confirmed and dated:** DAX NL/BE GA = **12 Feb 2026** (clinician-only). DAX does **not** ship a patient summary in the Benelux release (corrects any assumption that DAX brings the patient artifact to NL/BE now).
- **Correction to Brief E:** Epic's NL footprint is **clinician-mediated drafts + clinician-side summaries**, *not* a live patient-direct chatbot. **Ask Emmie has no confirmed EU deployment** as of May 2026. So the patient-direct Epic threat in NL is **2026–2027, not "already live."** The window is modestly *wider* than Brief E framed it.
- **The fastest-moving patient-direct artifact on home turf is portal letter-summarization, not Epic's chatbot:** ChipSoft's project + ZAS going live (Apr 2026) show hospital-side plain-language letter summaries are *shipping now* in BE and piloting in NL.
- **Inference (label as estimate):** in-portal patient AI summaries for hospital visits likely become broadly normal in NL/BE within **~2 years (2027–2028)**. The artifact's standalone value erodes on that horizon — consistent with Brief C's core warning.

---

## 5. The open gap

Across every player above — portal/EHR, scheduling, scribe, and B2C document-summarizer — here is what **none** of them does, which is the space a patient-initiated, cross-provider, multilingual player keeps: `[I]`

1. **Patient-initiated, not institution-gated.** ChipSoft, ZAS, Epic, Doctolib summaries exist only if *the provider/hospital* turns them on and only for *that* encounter. A patient at a hospital that hasn't deployed it, or seeing a provider outside the system, gets nothing. Ditto works regardless of whether the clinic adopted anything.
2. **Cross-provider, longitudinal.** Every encroacher is single-provider/single-portal: a HiX letter, a Doctolib visit, one hospital's portal. None aggregates the GP + oncologist + radiologist + second-opinion clinic into one patient-owned record. The B2C German tools (Simply Onno) are single-shot, no memory across visits.
3. **Recording-based, not document-/portal-only.** The B2C consumer tools (Simply Onno, mein-arztbefund, Spexter) summarize a *document the patient already has*. They cannot capture the spoken consultation — the 60–75% of information that never makes it onto paper. Only the clinician scribes record, and they keep the output for the clinician. Ditto records the actual conversation for the patient.
4. **Multilingual at the patient's choosing.** Several have translation (Clareco 22 langs, mein-arztbefund 15, Juvoly 90+), but it's a feature bolted onto a single-provider tool, not the spine of a patient-owned, share-with-family-abroad product.
5. **Condition depth (oncology).** All the live patient-summary encroachers are general (ZAS started with rheum/nephro; Doctolib Parents is pediatrics). None is built around the serious-condition / oncology journey Ditto targets, where comprehension stakes and care-circle involvement are highest.
6. **The family/care-circle loop** — explicitly out of scope for this dive, but it is the one dimension *zero* of these competitors touch and the strongest moat candidate (see Brief C §6 and the separate relationship-layer dive).

**The gap in one line:** the artifact is commoditizing, but *patient-owned + recording-based + cross-provider + multilingual + condition-deep* is still unoccupied in the EU. The threat is that "good enough, free, in your hospital portal" makes patients stop reaching for a separate app — not that anyone has built Ditto's exact product better.

---

## 6. Implications for Ditto

`[R]` — for Merlijn's synthesis, not to action blindly.

1. **Re-time the Epic threat.** Brief E's "Epic is already live in NL with patient AI summaries" overstates it. Reality: clinician-mediated drafts + clinician-side summaries are live; **patient-direct Emmie has no confirmed EU deployment.** The patient-direct EHR threat in NL is a **2026–2027** problem, not a today problem. Don't burn strategy cycles defending against a chatbot that hasn't shipped to EU patients — but do assume it ships within 18–24 months.
2. **Treat the portal letter-summary (ChipSoft/ZAS), not Epic's chatbot, as the nearest live encroacher.** It's shipping now in BE, piloting in NL, and it directly commoditizes "explain my hospital letter." Ditto's defense is the three things the portal can't do: **record the conversation, aggregate across providers, and live in the patient's hands not the hospital's portal.** Make those the explicit positioning.
3. **Watch Doctolib hardest of the encroachers.** It is the only one combining distribution (the patient app + booking) with a patient summary and a standalone patient AI. If Doctolib Parents succeeds and generalizes beyond under-4s, it becomes the EU consumer-distribution threat Epic is structurally too B2B to be. Track its assistant's expansion roadmap.
4. **The German B2C document-summarizer market is a validated, under-served wedge — and a competitive flag.** Simply Onno's 60k+ summaries and DIE WELT award prove German consumers will use a free AI tool to understand medical documents, with no provider in the loop. That's both (a) a market-entry signal for Ditto in DE and (b) a warning that a German player could add recording + care-circle and become a regional Kin. Worth a dedicated DE go/no-go look.
5. **Lead with the recording + cross-provider + multilingual combination, because that is literally the only combination unoccupied.** Clareco CoPilot is the sole NL/BE player attempting it and is pre-traction — Ditto's 35k users + oncology depth is a real head start, but the moat is the *combination plus the care-circle*, not any single feature, all of which are individually being matched.
6. **GDPR/consent-first stays a differentiator, and the home-turf data point strengthens it.** ChipSoft explicitly frames its letter-translator as a way to stop patients using "external, unsafe, non-optimized AI apps." That's the incumbent conceding the trust frame matters — and an opening for an EU-native, consent-first product to own it credibly. (Links to Brief A.)

---

## 7. Confidence & gaps

| Item | Confidence | Note |
|---|---|---|
| German B2C document-summarizers (Simply Onno et al.) real & with traction | **High** | Multiple sources; Simply Onno 60k+ summaries, award, press. |
| Doctolib clinician assistant sends patient a summary; Doctolib Parents early 2026 | **High** | Doctolib's own pages + multiple FR press. |
| DAX/Dragon Copilot GA in NL/BE = 2026-02-12, clinician-only | **High** | Partner (ORdigiNAL) + Microsoft confirm GA; patient-summary absence is inference from release scope. |
| ZAS live with patient letter summaries 2026-04-16 | **High** | ZAS newsroom, dated, with volumes. |
| ChipSoft "Patiëntvriendelijke brief" = pilot/innovation, no public GA date | **Medium-High** | Confirmed project + hospitals + COZO delivery; live-date not disclosed. |
| Epic NL is clinician-mediated, Emmie not yet in EU | **Medium-High** | ETZ/UMCG sources clear on clinician-review; Emmie's EU-deployment absence is "not found," not "confirmed absent." |
| No scaled native-EU direct (recording→patient summary) clone today | **Medium** | Clareco is the only match found and is pre-traction; a stealth player could exist below search visibility. |
| Nordic patient-facing summary apps absent | **Medium** | Found only clinician scribes + research; native Danish/Norwegian/Finnish consumer search was lighter than NL/DE/FR. |
| "Standard-of-care by 2027–2028" timeline | **Low (inference)** | Reasoned estimate from rollout pace, not a sourced forecast. |

**Gaps to close next:** (a) deeper Nordic + Spanish/Italian consumer-language sweep (this dive weighted NL/DE/FR/BE); (b) Clareco CoPilot primary check (funding, real install base) — it's the one true EU analog; (c) Doctolib Parents roadmap beyond under-4s; (d) whether ChipSoft's "Patiëntvriendelijke brief" has a public GA date / which NL hospitals; (e) the care-circle/relationship competitive layer (separate dive).

---

## 8. Sources

1. https://service.mijndiad.nl/article/395-ai-gesprekssamenvattingen-via-smartintake-ai
2. https://www.medischcontact.nl/actueel/laatste-nieuws/nieuwsartikel/nederlandse-ai-start-up-voor-medische-verslaglegging-wordt-overgenomen-door-zweeds-bedrijf
3. https://juvoly.nl/
4. https://www.epic.com/epic/post/healthcare-innovators-showcase-real-world-outcomes-at-egm-2025/
5. https://www.zilverenkruis.nl/zorgaanbieders/visie-en-transformatie/goede-voorbeelden/ai-spraakherkenning
6. https://info.doctolib.fr/solution/assistant-consultation/
7. https://www.banquepopulaire.fr/professionnels/conseils/doctolib-assistant-ia-patients/
8. https://about.doctolib.fr/news/intelligence-artificielle-doctolib-lance-lassistant-de-consultation/
9. https://doctolibpatient.zendesk.com/hc/fr/articles/23206190450460-D%C3%A9couvrir-Doctolib-Parents-un-nouveau-service-con%C3%A7u-pour-les-parents-de-jeunes-enfants
10. https://www.chipsoft.com/nl-nl/nieuws-en-blogs/tijdwinst-in-het-consult-door-ai-in-het-epd/
11. https://loquii.ai/
12. https://www.simply-onno.com/en/press-releases/german-startup-uses-ai-to-explain-medical-findings
13. https://www.trustpilot.com/review/simply-onno.com
14. https://mein-arztbefund.de/
15. https://apps.apple.com/de/app/mein-arztbefund/id6754453147
16. https://apps.apple.com/de/app/befino-arztbefund-%C3%BCbersetzen/id6760299903
17. https://www.chipsoft.com/nl-be/nieuws-blogs/gestandaardiseerde-uitwisseling-van-zorggegevens-via-fhir-voor-betere-patientzorg/
18. https://nieuws.zas.be/primeur-zas-maakt-medische-verslagen-begrijpelijk-met-ai
19. https://www.medischcontact.nl/actueel/laatste-nieuws/nieuwsartikel/ai-in-epic-helpt-bij-beantwoording-patientvragen
20. https://www.techtarget.com/patientengagement/feature/Epics-Ask-Emmie-offers-EHR-backed-AI-chatbot-option-for-patients
21. https://ordiginal.com/company-news/microsoft-dragon-copilot-nu-beschikbaar-in-nederland-en-belgie/
22. https://www.microsoft.com/nl-nl/health-solutions/clinical-workflow/dragon-copilot
23. https://tandemhealth.ai/en/
24. https://leapscribe.se/en/
25. https://www.svt.se/nyheter/lokalt/dalarna/region-dalarnas-ai-plan-spela-in-moten-mellan-lakare-och-patient
26. https://zorginnovatie.nl/innovaties/clareco-copilot
27. https://www.digitaletoekomst.be/nl/artificiele-intelligentie/verhalen/artsen-winnen-5-minuten-per-consultatie-met-de-vlaamse-ai-tool
28. https://www.vrt.be/vrtnws/nl/2025/01/16/gentse-start-up-helpt-huisartsen-consultatieverslagen-maken-met/
29. https://ai.corilus.be/
30. https://comon.gent/spexter
31. https://www.dr.dk/nyheder/indland/med-nyt-ai-vaerktoej-slipper-laeger-papirarbejdet-vi-faar-tid-til-flere-patienter
32. https://uwzorgonline.nl/zorgverleners/triage-overzicht-voor-zorgverleners/
33. https://pharmeon.nl/kijksluiter-digitale-bijsluiter-patienten/
