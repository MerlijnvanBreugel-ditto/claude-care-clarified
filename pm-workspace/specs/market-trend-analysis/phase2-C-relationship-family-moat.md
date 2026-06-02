# Phase-2 Deep Dive C — The Relationship / Family Moat

> Phase-2 deep dive on the most important question: if the summary artifact is not defensible (Brief C established it is becoming a free EHR byproduct), the moat is the **patient + family relationship**. How do you win it, and who is competing for it?
> Scope: the RELATIONSHIP / FAMILY layer — acquisition, retention, the family loop, and who else is trying to own that layer. The summary/scribe artifact and its direct clones (Kin, Hedy, Medcorder, Abridge/DAX/Suki) are covered by Brief C; referenced here only where they touch the relationship loop.
> Created 2026-05-30. `[F]` = fact (sourced) · `[I]` = inference · `[R]` = recommendation · `[E]` = estimate. Vendor-reported figures are flagged. Recency noted where it matters.

---

## 1. Executive summary

- **The moat is real but it is a network moat, not a feature moat — and network moats are won by the invite loop, not the product.** Every durable patient-relationship business studied (CaringBridge, Lotsa Helping Hands, Belong.Life) wins because *the patient or first caregiver pulls in others*, and value compounds per added member. Ditto's care circle is the right asset; the question is whether the loop is engineered to compound. `[I]`
- **Direct-to-patient acquisition that works is condition-specific entry + trusted-referrer hand-off + content/SEO, not paid consumer ads.** The repeated failure mode is treating a health app like a D2C consumer app and buying installs. What works: enter through one acute, high-anxiety condition (oncology fits), ride a trusted referrer (clinician, pharmacy, charity) who transfers trust, and rank for the long-tail questions patients Google at 2am. `[F][I]` [stackmatix][bcg][owise]
- **Retention in health apps is driven by self-monitoring habit + human/peer support, NOT by the summary.** Evidence: regular self-monitoring users have ~80% probability of still using an app at 40 weeks vs ~60% for non-users. A one-shot summary after a visit has no habit hook. The relationship layer (recurring updates, a circle that checks in, a place that holds the whole journey) is what creates return visits. `[F]` [pmc-selfmonitor][i-jmr]
- **The family/care-circle loop is the strongest moat AND the strongest growth engine — they are the same thing.** The mechanics that compound: (1) free-for-invitees (only the patient/anchor "pays" in effort), (2) differentiated roles (Manager vs Viewer / informed vs involved), (3) value-per-member that rises with each join (calendar coverage, fewer "how is mum?" calls), (4) the emotionally urgent moment (diagnosis) as the trigger. Kin already ships Manager/Viewer roles and text-invite; CaringBridge and Lotsa proved the loop at million-page scale. `[F]` [kin-tc][kin-hit][lotsa][caringbridge-stribune]
- **The relationship/family layer is contested but fragmented — and no EU-native, oncology-focused, patient-owned, cross-provider, family-shareable player is dominant.** US cancer-companion players (Outcomes4Me 280k patients + acquired Germany's Mika 100k; Belong.Life ~200k) own patient communities. Caregiver-coordination apps (CaringBridge, Lotsa, Jointly/Carers UK, Caily, CircleCare) own the family-logistics job. EU agetech (Patronus, Birdie, Cera) own elderly/professional care. **None combines Ditto's wedge: the recorded-visit comprehension artifact as the reason-to-open, with the family circle as the loop.** `[I]`
- **"Tandem" disambiguation: there is no prominent caregiver/relationship app called Tandem doing extremely well.** The two "Tandem"s actually doing extremely well are both NOT relationship apps: **Tandem Health** (Stockholm AI ambient scribe — €40-42.6M Series A Jul 2025, Kinnevik-led, 1,000+ hospitals/clinics, Accurx → 200k+ NHS pros) and **Tandem Technology** (US AI-for-prescriptions, ~$1B valuation Jan 2026, $137M+ raised). Most likely Merlijn means **Tandem Health** (it is the EU healthcare-AI breakout). It is a competitor for the *clinician*, not the patient/family relationship — covered by Brief C as a scribe. Profiled in §6 with the ambiguity flagged. `[F][I]` [tandem-eustartups][tandem-kinnevik][tandem-bbg][tandem-tfn]
- **Net read:** Ditto should stop thinking of itself as a summary tool and start operating as a **patient + family relationship company that uses the recorded visit as the wedge**. The summary is the hook; the care circle is the moat; condition-depth (oncology) + EU trust posture are the defensible flanks. The growth model and the moat are one loop, and it is buildable now. `[R]`

---

## 2. Playbook: winning the patient relationship (direct-to-patient, not via the hospital)

### 2a. What actually works for direct-to-patient acquisition

| Channel | What works / fails | Evidence | Read for Ditto |
|---|---|---|---|
| **Condition-specific entry** | Win works when you enter through ONE acute, high-anxiety condition and own its long-tail intent, then expand. Nurx grew via condition-specific + alt-treatment search, 56 custom landing pages mapped to search intent. Cancer-companion winners (Outcomes4Me, OWise, Vinehealth, Belong) all started single-condition. | [stackmatix][adm-nurx][outcomes4me] | 🟢 Oncology is the right wedge — acute, high-anxiety, high-search-intent, family-mobilizing. Don't dilute to "all health" early. |
| **Trusted-referrer hand-off (clinician / pharmacy / nurse)** | The highest-value channel: a trusted referrer transfers trust directly. Works when you reduce friction for the referrer (waiting-room one-pagers, prescription-pad-style cards, co-branded patient materials, in-workflow). OWise reached UK patients via NHS Innovation Accelerator + clinician recommendation; 90% of patients/clinicians recommend it. | [bcg][stackmatix][owise] | 🟢 Oncology nurses / clinics are the warm channel. Give them a 10-second "here's an app that helps you understand today's visit" card. The clinician doesn't sell software; they hand off a comprehension tool. |
| **Advocacy / charity partnerships** | Patient-advocacy orgs and disease charities are concentrated, trusted distribution. Cancer Support Community (175 locations), national cancer charities, condition foundations recruit patients for trials, programs, resources. The hand-off is mission-aligned not commercial. | [nccn][csc][cancer-advocacy] | 🟢 EU oncology charities (KWF Kankerbestrijding NL, Macmillan/CRUK UK, DKG/Deutsche Krebshilfe DE) are a credibility-laundering channel. Slow to land, high trust, hard for US clones to replicate locally. |
| **Content / SEO (long-tail patient questions)** | Patients Google their diagnosis, drug names, side-effects, "what did the doctor mean by X." Ranking for that intent is durable, compounding, cheap relative to ads. The whole consumer-health-AI wave ("Dr. ChatGPT") runs on this intent. | [stackmatix][evokad] | 🟢 Build plain-language, multilingual condition/term explainers that ALSO funnel to the recorded-visit product. SEO moat is local-language — a structural EU advantage. |
| **Community** | Communities (Belong, PatientsLikeMe) acquire and retain by giving patients people-like-me. High engagement, but heavy to moderate and slow to monetize. PatientsLikeMe sold to UnitedHealth (2019); communities tend to need an acquirer. | [belong-prnews][plm-wiki] | 🟡 A full social network is a different company. A *light* peer layer scoped to the care circle (not strangers) is on-strategy; a public forum is not. |
| **Paid consumer ads (D2C install buying)** | The repeated failure mode. High CAC, low trust transfer, weak retention in health. BCG: "acquisition in consumer health has its own formula" — it is not standard D2C performance marketing. | [bcg] | 🔴 Do not build the growth model on paid installs. Use the loop + referrers + SEO. |

### 2b. What makes a patient STAY (the habit / relationship hooks)

Evidence-graded, from the engagement/retention literature and the products that retained:

1. **Self-monitoring / recurring data is the single strongest retention lever.** Regular self-monitoring users ~80% retained at 40 weeks vs ~60% for non-users. A one-time visit summary has zero recurrence. **Implication: Ditto needs a recurring reason to open between visits** — symptom/side-effect logging, "questions for next visit," medication, the unfolding journey timeline. `[F]` [pmc-selfmonitor]
2. **Human / peer support beats features.** The eHealth retention literature is consistent: in-app support (peers, coach, or — for Ditto — the care circle) is a top retention driver; lack of support features is a top churn driver. The care circle IS the support feature. `[F]` [bmc-mental][jmir-retention]
3. **Health-literacy progress feels rewarding.** Turning comprehension into an interactive, slightly game-like experience (you understand more each visit) drives engagement; intimidation drives churn. `[F]` [bluebrix][i-jmr]
4. **The emotional anchor: "this place holds my whole journey."** CaringBridge users show 3x connection to family/friends, 4x less loneliness, 2x sense of purpose vs national average — the relationship, not the tool, is why they return. `[F, vendor-reported]` [caringbridge-stribune][caringbridge-startribune]
5. **Caveat (intellectual honesty):** frequency of engagement does not reliably predict clinical outcomes. Retention ≠ health impact. Don't over-claim outcomes from usage. `[F]` [i-jmr]

> **Core retention thesis for Ditto:** the summary gets the patient in; the recurring journey (between-visit logging + next-visit prep) and the care circle (people checking in) are what make them stay. Build the loop, not just the artifact. `[R]`

---

## 3. Playbook: winning the family / care circle (the mechanics that compound)

The family loop is where the moat and the growth engine are the same thing. Below: the mechanics, each with the proof product and why it compounds.

| Mechanic | How it works | Proof products | Why it compounds |
|---|---|---|---|
| **Free-for-invitees, effort-only-for-anchor** | Only the patient (or first caregiver) sets it up; everyone invited joins free with one tap/code. CircleCare: only creator subscribes, invited family free. Connected Caregiver, Jointly: invite "as many as you want," no extra cost. | CircleCare, Jointly/Carers UK, Connected Caregiver, Lotsa | Removes the #1 friction to network growth (cost/decision per invitee). Each invite is a pure expansion, not a sale. `[F]` [circlecare][carersuk-jointly][lotsa] |
| **Differentiated roles (involved vs informed)** | Distinct permission tiers: who *manages* care vs who is *kept informed*. Kin ships **Manager / Viewer**. CareLineLive assigns role-scoped visibility (family sees meds/visits; GP sees clinical only). Caily lets members pick "Caregiver" vs "Family & Friends." | Kin, CareLineLive, Caily, Jointly | Lets you invite the *whole* circle (10+ people) without overwhelming or over-exposing — more members = more loop surface, while keeping the anxious-daughter-abroad and the hands-on-spouse both served. `[F]` [kin-hit][carelinelive][caily] |
| **Value-per-member rises with each join** | Shared calendar means each added person can cover a task/ride/meal; group messaging means one update replaces N phone calls; shared info means no single point of failure. Lotsa's calendar + task feed is the canonical example; CaringBridge replaces the repeated "how is she?" call. | Lotsa, CaringBridge, Jointly | Classic network effect: the Nth member makes the tool more valuable for members 1..N-1 (more coverage, less repetition). This is the compounding mechanism. `[F]` [lotsa][caringbridge-support] |
| **The emotionally urgent trigger (diagnosis)** | Diagnosis is the moment a family *needs* to mobilize and is most willing to adopt a tool. CaringBridge, Lotsa, Belong all anchor on a health crisis. Every 12 minutes a new CaringBridge page starts — the crisis is the on-ramp. | CaringBridge, Lotsa, Belong | The trigger is involuntary and high-intent; you don't manufacture demand, you meet a family at the one moment they will organize around a tool. Oncology delivers this trigger reliably. `[F]` [caringbridge-stribune][lotsa] |
| **The update as the viral unit** | The patient/anchor posts an update (or shares a visit summary); recipients who aren't members get pulled in to follow. CaringBridge: ~1,600 messages/hour, 300k+ daily sender/receivers — the update is what spreads. | CaringBridge, Kin (share summary by text) | Each shared update is an impression + invite to a non-member, often at an emotional peak (good/bad news). For Ditto the visit summary IS a natural, valuable share-unit — better than a generic "journal post." `[F]` [caringbridge-stribune][kin-tc] |

### What the failures teach
- **Public stranger-communities are heavy and tend to get acquired, not scaled solo.** PatientsLikeMe → UnitedHealth (2019); Belong monetizes via pharma/hospital licensing, not the patient. A *private circle* (Ditto's model) is lighter and more defensible than a public forum. `[F][I]` [plm-wiki][belong-not-just]
- **Single-condition patient apps without a family loop get absorbed by the supply chain.** Vinehealth (UK oncology symptom tracker, NHS-approved) was acquired by Sciensus (pharma supply co, Jan 2024) — the data, not the relationship, was the prize. A tracker alone is a feature; a family network is a company. `[F]` [vinehealth-mdn]
- **One-off payment, no loop = no compounding.** Jointly charges £2.99 one-off and has modest reach despite Carers UK's brand — proof that a great coordination feature without an engineered growth loop and recurring hook plateaus. `[F][I]` [carersuk-jointly]

> **Care-circle thesis for Ditto:** the visit summary is the highest-quality share-unit in this whole category (more valuable and more frequent than a journal post or a calendar task). Wrap it in free-for-invitees + Manager/Viewer roles + a shared journey timeline, trigger on diagnosis, and the loop compounds. Out-build the circle, not the summary engine. `[R]`

---

## 4. Competitors for the relationship / family layer (table)

Players trying to own the patient + family relationship. EU emphasis. Traction figures vendor-reported unless noted.

| Player | Wedge / lead use case | Who they serve | Family/circle mechanic | Geography | Traction (date) | Threat to Ditto's relationship layer |
|---|---|---|---|---|---|---|
| **CaringBridge** [caringbridge-stribune][caringbridge-propublica] | Free health-journey journal + care coordination; "no one goes through a health crisis alone." | Patient + family/friends in any serious illness. | Update feed = viral unit; supportive-comment loop; Planner/calendar; private pages. | US-origin, 240+ countries. | 1M+ pages since 1997; ~300k daily users; new page every 12 min; $10.7M revenue FY (nonprofit, filed Mar 2025). | 🟡 Adjacent. Owns the *emotional update* job, not visit comprehension. No AI summary, no cross-provider record. Closest spiritual analog to Ditto's circle. |
| **Lotsa Helping Hands** [lotsa] | Care-coordination calendar (meals, rides, tasks) around a caregiver. | Family/friends/volunteers around a caregiver. | Free community; calendar + task feed; "tell a friend" invite. | US-origin. | Long-established; partners w/ disease orgs (e.g. LLS). | 🟡 Adjacent. Owns logistics, not comprehension. Mechanic to copy: task feed = value-per-member. |
| **Jointly (Carers UK)** [carersuk-jointly] | Coordination app "designed by carers for carers." | UK family carers + their circle. | "Circle of care," invite unlimited free, group messaging, meds, events. | UK. | Backed by Carers UK brand; £2.99 one-off; modest reach. | 🟡 Low-moderate. Charity trust + circle model, but no AI, no recurring hook, weak loop. |
| **Belong.Life (Belong Cancer)** [belong-prnews][belong-not-just] | World's largest cancer social network; AI-personalized community + navigation. | Cancer patients AND caregivers. | Anonymous peer community; caregiver groups; hospital-licensed engagement. | Israel-origin, global. | ~200k cancer patients/caregivers (Feb 2026 est.); 24k breast, 16k lung. | 🟡 Adjacent-strong. Owns cancer community/peer relationship. Public-community model; B2B2C licensing. Different relationship (strangers) than Ditto's private circle. |
| **Outcomes4Me** [outcomes4me][o4m-mika] | AI cancer-care navigation: guidelines, genomics, trial matching, symptom tracking, peer community. | Cancer patients (+ pharma as customer). | Peer community; data shared w/ care team. | US + EU (acquired Germany's **Mika Health**, Jun 2025). | 280k+ patients; Mika +100k; $38M raised; TIME Best Inventions 2025. | 🟡→🔴 Closest cancer-relationship competitor with EU footprint via Mika (Germany). Patient-owned, condition-deep, expanding EU. Watch. |
| **Patronus (Berlin)** [patronus-eustartups] | Senior emergency smartwatch + **family app**; AI daily companion roadmap. | Elderly + their family. | Family app connecting relatives to the elderly person. | Germany / DACH. | 50,000 family members connected; €11M raised (Apr 2026). | 🟡 Adjacent. Owns elderly-safety family relationship, not patient comprehension. Proves EU family-app demand + reimbursable angle. |
| **Caily / CircleCare / Connected Caregiver / Caring Village** [caily][circlecare] | Family care-circle coordination (meds, tasks, info hub). | Family caregivers. | Circle + code-invite, role tiers, free invitees, med reminders. | US-origin (apps global). | Fragmented, small individually. | 🟡 Low individually; collectively prove the circle/role/invite mechanics Ditto should adopt. |
| **Cera / Birdie** [cera-tc][birdie-eustartups] | AI-driven *professional* home-care operating systems. | Care agencies + (indirectly) families/elderly. | Caregiver-facing apps; some family visibility. | UK / Europe. | Cera ~$500M ARR, 10k carers, $407M+ raised; Birdie 700+ providers, 35k people. | 🟢 Not direct. B2B professional-care platforms, not consumer patient/family relationship. Adjacent ecosystem. |
| **Kin Health** [kin-tc][kin-hit] | (See Brief C — direct summary clone) Record visit → summary → **share with care circle (Manager/Viewer)**. | Patients + family/caregivers. | Text-invite, Manager/Viewer roles, patient delete-control. | US. | $9M seed (May 2026, Maveron). | 🔴 Most direct relationship-layer threat: same wedge (visit comprehension) + same care-circle loop. US-only today. The one to watch + out-build. |

---

## 5. Patient-direct players & their use cases (table)

Players that try to win the patient with a DIFFERENT lead use case than summaries (then could expand toward the relationship). Catalog of how they acquire and hold the patient.

| Player | Lead use case (the hook) | What holds the patient | Geography | Traction (date, vendor-reported) | Relationship/family angle | Source |
|---|---|---|---|---|---|---|
| **Ada Health** | AI symptom assessment / triage ("what might this be?"). | Recurring self-assessment; partnerships embed it (Bayer, AXA, Novartis, Sutter). | Berlin / global. | 11M downloads, 23M+ assessments; $120M Series B (Bayer-led). | Weak — individual triage, no circle. | [ada-fierce][ada-pharmaphorum] |
| **K Health** | AI chat → diagnosis suggestion → connect to doctor (virtual primary care). | Becomes your primary-care front door; payer/health-system partners. | US (48 states). | 10M+ AI interactions, 3.1M doctor/nurse visits; $418M raised; Cedars-Sinai. | Weak — individual care, no family loop. | [khealth-statnews][khealth-fierce] |
| **Belong.Life** | Cancer peer community ("people like me"). | Community engagement, AI personalization, caregiver groups. | Israel / global. | ~200k patients/caregivers. | **Strong** — caregiver groups built in. | [belong-prnews] |
| **Outcomes4Me / Mika** | Cancer navigation: guidelines, trial matching, symptom tracking. | Personalized journey + peer community + data value. | US + Germany (Mika). | 280k + 100k patients. | Moderate — peer community, care-team sharing. | [outcomes4me][o4m-mika] |
| **OWise** | Personalized cancer support: symptom tracking + consultation question-prep + share with team/loved ones. | Recurring tracking; visit-prep; data sharing. NHS-listed, CE-marked. | NL-origin → UK/US. | "Thousands"; 90% recommend; peer-reviewed improves patient-doctor interaction. | **Moderate-strong** — explicitly share with loved ones + team; closest EU spiritual cousin. | [owise][owise-nip] |
| **Vinehealth** | Oncology symptom tracking + meds + team communication. | Longitudinal PRO data; NHS playbook. | UK. | NHS-approved; **acquired by Sciensus Jan 2024**. | Weak — patient-clinician, not family. | [vinehealth-mdn] |
| **Vivante Health (Cylinder)** | Chronic GI/digestive condition management + 24/7 care team. | Coaching + condition program; employer-distributed. | US. | $77.9M raised; Fortune 500 / UnitedHealthcare distribution. | None meaningful (B2B2C employer). | [vivante-mobi][cylinder] |
| **Tandem Technology** | AI for prescriptions (prior-auth, pharmacy routing). | B2B infra reaching patients via providers. | US. | ~$1B valuation (Jan 2026), $137M+ raised. | None — infrastructure. | [tandem-bbg][tandem-tfn] |

**Read:** AI health companions (Ada, K Health) win the *individual* with triage/Q&A but have no family loop — they are front-door rivals for attention, not relationship rivals. The cancer-companion cluster (Belong, Outcomes4Me/Mika, OWise) is where patient-direct + relationship overlap most, and where the EU oncology contest will be. `[I]`

---

## 6. Tandem profile (disambiguation + the relevant one)

**Merlijn flagged "Tandem" as doing extremely well. There is no prominent caregiver/family-*relationship* app named Tandem. The two "Tandem"s genuinely doing extremely well are both clinician/infrastructure plays, not patient/family relationship plays.** `[F][I]`

| Candidate | What it is | Wedge | Traction (date) | Why it's winning | Relevance to relationship/family layer |
|---|---|---|---|---|---|
| **Tandem Health (Stockholm)** — *most likely referent* | EU ambient AI medical scribe / "AI-native operating system for clinical workflows." Listens to consultations, drafts notes into clinical systems. Founded 2023. | The clinician's documentation burden (~40% of clinician time on admin). | **€40-42.6M Series A, Jul 2025** (Kinnevik-led). Tens of thousands of clinicians, **1,000+ hospitals/clinics** across Europe; **Accurx partnership → 200k+ NHS professionals**; "one of the largest AI rollouts in healthcare globally." Operating in Nordics, UK, FR, ES, DE, IT, EE, NL. | EU-native, multi-country, multi-language; rode the Accurx distribution rail into the NHS; well-capitalized by a top Nordic investor; timing (clinician-burnout + EU AI demand). | **Competes for the CLINICIAN, not the patient/family.** Roadmap mentions "patient consultation summaries" + "care coordination," so it could drift patient-side — but today it is a B2B scribe. Covered as a scribe by Brief C. Not a relationship-layer competitor *yet*. `[F]` [tandem-eustartups][tandem-kinnevik][tandem-healthcareit] |
| **Tandem Technology (New York)** | AI for prescriptions: automates prior-authorizations and pharmacy routing; free to providers/patients. Founder Sahir Jaggi. | The broken prescription workflow (slow, manual, costly prior-auth). | **~$1B valuation (unicorn), $100M round led by Accel, ~Jan 2026**; $137M+ total (General Catalyst, Thrive). "Expects to reach millions of patients in 2026" (no live-deployment metrics disclosed — marketing vs reality gap flagged). | Hot category (AI + healthcare admin), top-tier investors, fast valuation step-up. | **Infrastructure, no patient/family relationship.** Not relevant to the relationship layer. `[F]` [tandem-bbg][tandem-tfn][tandem-pymnts] |
| Tandem Careplanning / Tandem Care | Home-care services marketplace / agency. | Professional in-home care delivery. | Small; no notable funding signal. | n/a | Not a consumer family-relationship app at scale. `[F]` [tandem-careplanning] |
| Tandem Diabetes (Mobi) | Insulin-pump + companion app (medical device). | Diabetes device management. | FDA-cleared Android Nov 2025. | n/a | Device company, unrelated. `[F]` [tandem-mobi] |

**Verdict on Tandem:** 🟡 **Most probably Tandem Health (the Swedish scribe) — the EU healthcare-AI breakout Merlijn would have heard about. But it is a clinician-side scribe, not a patient/family-relationship product, so it belongs to the summary/scribe agent's scope (Brief C), not this dive.** If Merlijn specifically meant a *family/relationship* Tandem, none is doing extremely well — recommend confirming which Tandem he means before treating it as a relationship-layer threat. The strategic point stands: the impressive Tandem (Health) validates that *EU-native, multi-country, distribution-rail-riding* health AI can scale fast — a model Ditto should study for the patient side. `[I][R]`

---

## 7. What Ditto should do (recommendations)

`[R]` — for Merlijn's synthesis, not to action blindly.

1. **Reframe internally: Ditto is a patient + family relationship company; the recorded visit is the wedge.** Stop optimizing the summary as the product; optimize the loop. The summary is the highest-quality, most-shareable, most-frequent emotional unit in the whole category — use it as the viral unit (like CaringBridge's update, but better), not as the destination.
2. **Engineer the care-circle loop to compound — copy the proven mechanics now:** (a) **free-for-invitees** (only the patient sets up), (b) **Manager / Viewer / Informed roles** (so the whole circle joins without overwhelm — Kin already ships this; match and exceed it), (c) **value-per-member that rises** (shared journey timeline, "questions for next visit," task/appointment coverage so the 5th relative adds value), (d) **trigger on diagnosis** (the involuntary high-intent moment). Make the share-summary action a one-tap invite to a non-member.
3. **Add a recurring between-visit hook or churn is structural.** A one-shot summary has ~zero retention. Add self-monitoring (side-effects/symptoms, the strongest evidence-backed retention lever), next-visit question-prep (OWise's proven feature), and a living journey timeline. This is also what makes the circle worth checking daily.
4. **Acquire via condition-depth + trusted referrers + local-language SEO — never paid installs.** Own oncology long-tail search in NL/local languages (a structural EU moat US clones can't cheaply copy). Build a frictionless clinician/oncology-nurse hand-off card. Pursue EU oncology-charity partnerships (KWF, Macmillan/CRUK, Deutsche Krebshilfe) for trust-laundered distribution.
5. **Out-build Kin on the circle before it reaches the EU; watch Outcomes4Me/Mika (Germany) as the cancer-relationship EU entrant.** Kin is the most direct relationship-layer threat (same wedge + same loop) but US-only today — Ditto's window is the EU head-start + oncology depth + GDPR/consent trust. Outcomes4Me's Mika acquisition puts a cancer-companion in Germany; treat it as the EU cancer-relationship contest to win.
6. **Make "patient-owned, cross-provider, consent-first, family-shareable" the explicit, demonstrated product spine.** This is the one thing institution-bound scribes (incl. Tandem Health if it drifts patient-side) structurally cannot do. The summary lands in one provider's portal; Ditto's circle spans providers and travels with the patient and the family. That is the moat — build and message it as such.

---

## 8. Confidence & gaps

| Item | Confidence | Note |
|---|---|---|
| Care-circle loop is both moat and growth engine | **High** | Convergent across CaringBridge, Lotsa, Belong, Kin; classic network-effect logic. |
| Specific compounding mechanics (free-invitee, roles, value-per-member, diagnosis trigger) | **High** | Each sourced to a live product; mechanics are observable. |
| Self-monitoring as #1 retention lever; one-shot summary doesn't retain | **High (general), Medium (for Ditto specifically)** | Strong literature; not specific to recorded-visit apps. |
| Direct-paid-installs is the failure mode | **Medium-High** | BCG + practitioner consensus; not a controlled study. |
| "Tandem doing extremely well" = Tandem Health (scribe) | **Medium** | Best inference from the evidence; no prominent relationship-Tandem exists. **Recommend Merlijn confirm.** |
| Traction figures for all players | **Low-Medium** | Almost all vendor-reported / press-release; not independently audited. Treat as directional. |
| No dominant EU oncology patient+family-relationship player | **Medium** | English + EU-startup-press search; possible under-count of small NL/DE/FR/Nordic local apps (same gap flagged in Brief C). |
| Kin's exact role permissions | **Medium** | App-store + press confirm Manager/Viewer + text-invite + delete-control; granular scope not published. |

**Gaps to close next:** (a) native-language sweep (NL/DE/FR/Nordic) for local oncology patient+family apps; (b) confirm with Merlijn which "Tandem" he means; (c) Ditto's own care-circle funnel metrics (invite-acceptance, members-per-patient, between-visit DAU) to know if the loop already compounds — this is internal-data, for the product agent; (d) whether Outcomes4Me/Mika or Belong is actively localizing into NL.

---

## 9. Sources

- **Acquisition / retention playbook**
  - [stackmatix] https://www.stackmatix.com/blog/healthtech-patient-acquisition
  - [bcg] https://www.bcg.com/publications/2025/acquisition-in-consumer-health-has-its-own-formula
  - [adm-nurx] https://www.accelerateddigitalmedia.com/insights/case-studies/nurx-patient-acquisition/
  - [evokad] https://evokad.com/marketing-strategies-healthcare-patient-acquisition/
  - [pmc-selfmonitor] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6062090/
  - [i-jmr] https://www.i-jmr.org/2024/1/e51974
  - [jmir-retention] https://www.jmir.org/2022/4/e35120/
  - [bmc-mental] https://link.springer.com/article/10.1186/s44247-024-00105-9
  - [bluebrix] https://bluebrix.health/blogs/patient-engagement-2-0-the-health-literacy-upgrade
- **Family / care-circle products & mechanics**
  - [caringbridge-stribune] https://www.startribune.com/caringbridge-ensures-that-no-one-has-to-go-through-a-health-crisis-alone/570250282
  - [caringbridge-support] https://support.caringbridge.org/
  - [caringbridge-propublica] https://projects.propublica.org/nonprofits/organizations/421529394
  - [caringbridge-startribune] https://www.caringbridge.org/
  - [lotsa] https://lotsahelpinghands.com/how-it-works
  - [carersuk-jointly] https://www.carersuk.org/help-and-advice/technology-and-equipment/jointly-app-for-carers/
  - [circlecare] https://circlecare.app/
  - [caily] https://www.caily.com/blog/circles-of-care-the-power-of-team-caregiving
  - [carelinelive] https://carelinelive.com/our-solution/care-circle-portal/
  - [kin-tc] https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/
  - [kin-hit] https://hitconsultant.net/2026/05/21/kin-health-raises-9m-seed-patient-ambient-ai/
- **Relationship/family-layer competitors**
  - [belong-prnews] https://www.prnewswire.com/news-releases/belonglife-surpasses-100-000-cancer-patients-and-caregivers-solidifying-position-as-worlds-largest-social-cancer-network-300700142.html
  - [belong-not-just] https://cancer.belong.life/not-just-a-cancer-app/
  - [plm-wiki] (PatientsLikeMe → UnitedHealth 2019) https://www.crunchbase.com/organization/patientslikeme
  - [outcomes4me] https://www.prnewswire.com/news-releases/outcomes4me-secures-21m-in-funding-to-accelerate-ai-driven-innovation-and-drive-global-expansion-to-transform-cancer-care-302468806.html
  - [o4m-mika] https://outcomes4me.com/press-release/outcomes4me-acquires-germanys-mika-health-app-to-accelerate-ai-driven-patient-empowerment-globally/
  - [patronus-eustartups] https://www.eu-startups.com/2026/04/berlin-based-patronus-raises-e11-million-for-senior-friendly-emergency-smartwatch-and-family-app/
  - [cera-tc] https://techcrunch.com/2025/01/12/uk-in-home-healthcare-provider-cera-raises-150m-to-expand-its-ai-platform/
  - [birdie-eustartups] https://www.eu-startups.com/2022/06/london-based-birdie-raises-e28-4-million-to-support-more-personalised-home-care-for-the-elderly/
- **Patient-direct (different use case)**
  - [ada-fierce] https://www.fiercebiotech.com/medtech/ada-health-hits-120m-series-b-top-up-for-symptom-assessment-ai-app
  - [ada-pharmaphorum] https://pharmaphorum.com/news/bayer-backs-ada-healths-symptom-checker-in-90m-financing
  - [khealth-statnews] https://www.statnews.com/2025/11/20/k-health-expands-access-primary-care-ai-virtual-care/
  - [khealth-fierce] https://www.fiercehealthcare.com/health-tech/digital-primary-care-startup-k-health-raises-50m-equity-funding-round
  - [owise] https://owise.uk/
  - [owise-nip] https://www.nipcharity.org/blog/owise-your-personalised-app-for-navigating-breast-cancer
  - [vinehealth-mdn] https://www.medicaldevice-network.com/news/sciensus-acquires-oncology-symptom-tracker-app-vinehealth/
  - [vivante-mobi] https://www.mobihealthnews.com/news/vivante-health-bags-6m-digital-gi-health-platform
  - [cylinder] http://www.vivantehealth.com/
- **Tandem disambiguation**
  - [tandem-eustartups] https://www.eu-startups.com/2025/06/swedish-startup-tandem-secures-e42-6-million-to-reduce-admin-burden-on-clinicians/
  - [tandem-kinnevik] https://www.kinnevik.com/insights/tandem-health-funding-round/
  - [tandem-healthcareit] https://www.healthcareittoday.com/2025/07/25/tandem-health-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe/
  - [tandem-bbg] https://www.bloomberg.com/news/articles/2026-01-26/ai-for-prescriptions-startup-tandem-lands-1-billion-valuation
  - [tandem-tfn] https://techfundingnews.com/tandem-1b-valuation-100m-round/
  - [tandem-pymnts] https://www.pymnts.com/healthcare/2026/tandem-technology-raise-100-million-dollars-prescription-automation/
  - [tandem-careplanning] https://caregiverapp.tandem.care/
  - [tandem-mobi] https://beyondtype1.org/tandem-mobi-available-on-android/
- **Market context**
  - [carers-eu] https://pmc.ncbi.nlm.nih.gov/articles/PMC8775661/ (EU caregiver support ratio 6:1 → 2:1 by 2050)
  - [carers-uk-num] https://www.carersuk.org/ (~10.6M UK unpaid carers)
  - [nccn] https://www.nccn.org/patientresources/patient-resources/additional-resources/advocacy-and-support-groups
  - [csc] https://www.cancersupportcommunity.org/
  - [cancer-advocacy] https://www.aacr.org/patients-caregivers/patient-advocacy/
