# Medication Management Apps — Market Teardown + Mechanism Analysis

**Status:** active · **Owner:** Merlijn (via Mewtwo) · **Created:** 2026-06-23
**Scope:** The most-used medication management / reminder apps — the global top 20 plus MedApp (added for NL relevance) — ranked with sourced usage data, each dismantled into its three core mechanics — medication entry, reminders, and the "taken" check — plus what it means for a possible Ditto medication feature.
**Companion artifact (visual teardown with real screens):** https://claude.ai/code/artifact/477cf961-7671-454d-8acb-6e3021e4e2fd

> **Reading convention.** Every quantitative claim is tagged `[FACT]` (a cited number from a named source) or `[INFERENCE]` (an estimate from indirect signals). `[RECOMMENDATION]` marks a judgment call. Download/MAU estimates in this category are genuinely unreliable — read the **Caveats** before quoting any figure externally.

## Executive summary

The medication-reminder category is crowded and commoditised. Three platform apps (Apple Health, Samsung Health, NHS App) reach hundreds of millions but no one publishes how many use the *medication* tab; a long tail of dedicated apps (MyTherapy, Medisafe, dozens of indie pill reminders) competes on near-identical mechanics; and pharmacy/PBM apps bolt medication onto an ordering rail. Underneath the branding, every one of these apps does only three jobs: **get a medication into the app, nudge the patient, and let them tick it off.** The differentiation lives in how well each does the third job and whether it pulls a caregiver into the loop.

Three findings drive the Ditto decision: (1) a pill reminder is a commodity, not a moat — the whole field already exists and none of it *owns* the job; (2) the EU incumbent to beat is **MyTherapy**, not Medisafe (free, #1 Medical in NL, pharma-funded, owned by listed Redcare Pharmacy); (3) in the Netherlands specifically the real footprint is the **pharmacy apps** (MedGemak, Service Apotheek) whose moat is DigiD-linked dispensing integration, not the reminder. The category monetises B2B everywhere; consumer pill-reminder subscriptions don't sustain a business. **[RECOMMENDATION]** If Ditto touches medication, the wedge is the *understood* medication list — why each drug was prescribed, in the patient's words, tied to the conversation and the care circle — not another reminder.

## The 20 most-used, ranked

Ranked by real global reach of the *medication function*, weighting active reach over lifetime downloads. † = discontinued/dormant. \* = cumulative or unverified vendor figure.

| # | App | Company | Category | Usage (sourced) | NL / EU | Monetization |
|---|-----|---------|----------|-----------------|---------|--------------|
| 1 | Apple Health — Medications | Apple | Platform sub-function | ~1.4B active iPhones; med-feature share unknown `[INFERENCE]`; advanced features US-only `[FACT]` | Basic logging only in NL `[FACT]` | Free (hardware) |
| 2 | Samsung Health (Medications) | Samsung | Platform sub-function | 77M MAU (Apr 2026) `[FACT]`; med tracking launched US Dec 2023, EU Oct 2024 `[FACT]` | NL named in rollout; med-feature use unverified `[INFERENCE]` | Free (hardware) |
| 3 | NHS App | NHS England | Platform sub-function | 39M registered (Dec 2025) `[FACT]`; 67.8M repeat scripts/yr `[FACT]` | UK only — EU benchmark `[FACT]` | Free (public) |
| 4 | MyFitnessPal | Francisco Partners | Sub-function | 220M registered, ~30M MAU `[FACT, 2024]`; med tracking incidental `[INFERENCE]` | Available; med use negligible | Freemium (~$19.99/mo) |
| 5 | Flo | Flo Health | Sub-function | 77M MAU, 380M+ downloads `[FACT, 2024]` | Widely used; med = pill sub-feature | Freemium (~$49.99/yr) |
| 6 | GoodRx | GoodRx Holdings | Pharmacy sub-function | 6.4M monthly active consumers Q1 2025 `[FACT]` | US only `[FACT]` | Free + Gold (~$9.99/mo) + B2B/ads |
| 7 | Walgreens | Walgreens | Pharmacy super-app | ~60M lifetime downloads\* `[FACT]` | US only `[FACT]` | Free (retail) |
| 8 | CVS Pharmacy (MedRemind) | CVS Health | Pharmacy super-app | 14.1M monthly users `[FACT, 2024]` | US only `[FACT]` | Free (retail) |
| 9 | **MyTherapy** | smartpatient GmbH (Redcare) | **Dedicated** | 12M+ users, vendor `[FACT]`; **#1 Medical in NL** `[FACT, SimilarWeb 2026-06-20]` | **Strong, real NL/EU footprint** `[FACT]` | Consumer free; B2B pharma PSP |
| 10 | Medisafe | Medisafe Inc. | **Dedicated** | "13M+" cumulative\* `[FACT]`; ~6M Android installs `[FACT]` | Available, Dutch supported, US-centric; NL use low `[INFERENCE]` | **Hard paywall since 1 Jan 2026**; B2B pharma + data |
| 11 | MedGemak | PharmaPartners / MijnGezondheid.net | NL pharmacy portal | 1.1M downloads `[FACT]` | **NL-native, DigiD-linked** `[FACT]` | Free (pharmacy/GP) |
| 12 | Service Apotheek | Ncontrol / Mosadex | NL pharmacy | ~720k downloads `[FACT]` | **NL-native, DigiD + caregiver auth** `[FACT]` | Free (pharmacy) |
| 13 | **MedApp** | MedApp Nederland B.V. | NL medication + delivery | ~1,300 Play ratings\* `[FACT]`; total downloads undisclosed `[INFERENCE]` | **NL-native; connected pharmacy + home delivery, all insurers** `[FACT]` | Free (pharmacy/delivery) |
| 14 | Pharmacy2U | Pharmacy2U | UK pharmacy | >500k customers; 500k scripts/mo `[FACT]` | UK only `[FACT]` | Free (NHS dispensing) |
| 15 | Express Scripts | Evernorth / Cigna | US PBM | >4M downloads `[FACT]` | US only `[FACT]` | Free (PBM) |
| 16 | Walmart Pharmacy | Walmart | US pharmacy | ~580k downloads `[FACT]` | US/CA only `[FACT]` | Free (retail) |
| 17 | Amazon Pharmacy / PillPack | Amazon | No standalone app | No install figure; $2B 2024 sales `[FACT]` | US only `[FACT]` | Fulfilment |
| 18 | Round Health † | Circadian Design (→ Alto) | **Dedicated** | ~15k iOS ratings; downloads unknown `[INFERENCE]`; abandoned | Delisted | Was free + IAP |
| 19 | Pill Reminder — All in One | Sergio Licea (indie) | **Dedicated** | Play 100k+ bucket; ~27k iOS ratings `[FACT]` | Installable, no Dutch | One-time $1.99 |
| 20 | Dosecast | Montuno Health | **Dedicated** | "1M+" unverified\* `[FACT-claim]`; tiny iOS rating base | EU adoption negligible `[FACT/INF]` | Freemium + B2B enterprise |
| 21 | Mango Health † | Valeris (ex-TrialCard) | **Dedicated** | B2B since Apr 2022; ~100k+ installs at peak (stale) `[FACT]` | US only | B2B pharma PSP |

**Dead / dormant, flagged so they aren't mistaken for live competitors:** **CareZone** — ~3.5M members at peak, acquired by Walmart 2020 (~$200M), app pulled ~2021, Walmart Health shut Apr 2024 `[FACT]`. **MyMeds** — consumer app frozen 2020, pivoted to B2B adherence analytics `[FACT]`. **Pillboxie** — abandonware since 2017, still sold at €1.99 in NL `[FACT]`. **Capsule** — operating but diminished (~13% layoffs 2022, US metros only) `[FACT]`.

## The three mechanics, per app

Concise decomposition. **A = Entry, B = Reminders, C = Check.** Full visuals in the companion artifact.

- **Apple Health** — A: search a drug, pick type/shape/colour. B: per-dose schedule + opt-in Critical-Alert follow-ups. C: one tap → filled ✓ Taken. *Advanced interactions US-only.*
- **GoodRx** — A: add to "medicine cabinet" (Rx-aware). B: named reminders, day checkboxes, per-med toggles, refill reminders. C: per-med Missed/Taken or "Took all." *No adherence purpose beyond price/refill.*
- **MyTherapy** — A: database search or barcode; inventory tracks refills. B: per-time reminders across meds + 20+ measurements. C: daily to-do checklist; confirming triggers a reward image; shareable doctor reports. *The EU benchmark.*
- **Medisafe** — A: multi-screen guided form (dose, schedule, pill image, days-limit). B: timezone-aware alarms, refill, drug-interaction warnings; **Medfriend** alerts a buddy 30 min after a missed dose. C: take/skip (skip asks a reason), "Take all," swipe actions.
- **Dosecast** — A: drug-database pick or manual, attach pill image. B: phone+Watch with take/skip/postpone, refill decrement. C: timestamped log; late & missed auto-recorded; editable history.
- **Pill Reminder — All in One** — A: FDA drug-DB search or manual, photo per med. B: flexible windows, pre-alarms, auto-snooze, Critical Alerts. C: Taken/Missed from lock screen; double-dose protection.
- **Pillboxie** — A: build a visual token (pill shape + colour). B: **drag the pill into a pillbox slot** to set time. C: check off → pill greys out. *Tactile, much-copied; frozen since 2017.*
- **Service Apotheek (NL)** — A: meds sync from the dispensing record; add via scan/search/manual. B: "Innames" recurring or one-time schedules; refill reminder 2 weeks before run-out. C: "Genomen / Overgeslagen" (taken/skipped). *DigiD, caregiver authorisation.*
- **Samsung Health** — A: search/scan, Elsevier interaction warnings (US). B: per-dose reminders. C: mark taken (~⅔ of US adopters use it 3×/week). *Android; iOS app stale.*
- **NHS App** — A: meds from GP record. B: order repeat prescriptions — no per-dose dosing reminder. C: **no taken-tick**; it is an ordering rail, not adherence.
- **Walgreens** — A: scan Rx barcode, bundle meds. B: customisable schedules. C: actionable alert → Taken/Skipped on iPhone & Watch.
- **CVS Pharmacy (MedRemind)** — A: auto from Rx history. B: MedRemind custom times + caregiver missed-dose alert. C: mark taken. *Sister app CVS Caremark has no tick.*
- **Express Scripts** — A: auto-populated from benefit. B: refill + auto-refill, delivery tracking, optional daily dose push. C: **none** — order-centric.
- **MedGemak (NL)** — A: meds from NL pharmacy record via DigiD. B: "inneemwekker" intake alarm. C: log intake against the dispensed list.
- **MedApp (NL)** — A: live inventory of what's at home; meds added manually or via the connected pharmacy. B: reliable reminders across pills, injections and inhalations + low-stock refill alerts. C: "Registreer je innames" — tick each intake on the daily list; plus a medical diary for complaints/side-effects. *Connected pharmacy + home delivery, partners with all insurers; free.*
- **MyFitnessPal** — GLP-1 dose logging bolted onto food tracking; med tracking incidental.
- **Flo** — contraceptive/pill reminder with a "Taken on time" check; narrow sub-feature.
- **Round Health †** — A: search, scheduled vs as-needed. B: **reminder windows, not fixed alarms** (3 nudges across a span). C: swipe → satisfying check animation. *Folded into Alto Pharmacy.*
- **Mango Health †** — A: guided form (frequency, time, quantity, form & colour). B: refill lead-time + interaction severity. C: mark taken **for points** — levels, streaks, weekly raffle. *Pivoted to B2B PSP.*
- **CareZone †** — A: **snap a photo of the prescription label** (human-transcribed). C: shared family care-circle list. *Killed after ~3.5M members.*
- **Amazon Pharmacy / PillPack** — A: auto from Rx history. B: refills synced to one delivery; dose reminders **delegated to Alexa**. C: no in-app tick — adherence is physical, via pre-sorted packets.
- **Visible / Epsy (condition-specific, below the top-20 on scale but sharp models)** — Epsy: "Have you logged your medication? → Taken / Not Taken / Taken Late," nudges tuned to seizure-risk timing. Visible: add a med, it joins the day's pacing trackers with one green check.

## Cross-cutting patterns

1. **Entry is a database-search problem.** Good apps resolve a name to a real drug (Apple, MyTherapy, Pill Reminder, Dosecast); pharmacy apps skip entry by syncing the dispensed list. Manual-only entry (Pillboxie) reads as dated.
2. **The check is the product.** Taken/skipped/"took all"/late-logging is where these apps live or die. Apps that omit it (Express Scripts, CVS Caremark) are ordering tools wearing a medication costume.
3. **Reminders compete on escape velocity.** Plain push is table stakes; the differentiators are Critical Alerts that break Focus, reminder *windows* (Round), and caregiver escalation on a missed dose (Medfriend, CVS).
4. **The caregiver loop is the moat attempt.** Every app reaching for defensibility adds a second person — Medfriend, CVS caregiver alerts, MyMeds' Circle of Care, CareZone's family list, NL's DigiD authorisation. Reminders are commodity; the relationship is not.
5. **Nobody sustains this on consumer subscriptions.** Survivors monetise B2B (pharma PSPs, payers, pharmacy fulfilment). The two best consumer apps died as consumer products: Round → Alto, Mango → pharma PSP, CareZone absorbed and shut. Medisafe's Jan-2026 paywall is the live test; MyTherapy stays free because pharma pays.

## Implications for Ditto (the decision)

`[RECOMMENDATION]`

1. **The reminder rail is not a wedge.** Dozens of interchangeable apps plus three platform sub-features already own it, and none owns it. Consistent with the market-deep-dive thesis: our spine is the understood conversation, not the alarm. See [[project_long_term_vision_v2]].
2. **The EU slot is taken — by MyTherapy, not Medisafe.** Benchmark against MyTherapy (free, #1 Medical NL, Redcare-backed) and assume the generic-reminder job is already solved for our users.
3. **In NL the real incumbents are the pharmacy apps.** MedGemak (1.1M) and Service Apotheek (720k) are DigiD-linked and wired into dispensing; MedApp adds a consumer-facing pharmacy + home-delivery layer across all insurers. The moat is the dispensing/delivery integration, not the reminder. Integrate with that rail; don't rebuild it.
4. **If we touch medication, the angle is the understood list, not the tick.** None of these explain *why* each medication was prescribed, in the patient's own words, tied to the conversation that started it, with the caregiver inside that understanding. That is adjacent to our spine and to the oncology beachhead, where regimens are dense and timing matters. See [[project_current_strategy_2026q2]].

## Risks & caveats

- **Vendor "X million users" claims are cumulative registrations** and overstate active use, often ~10× (Medisafe "13M" vs ~6M Android installs).
- **Google Play publishes only coarse buckets** (100k+, 1M+, 5M+); treat as ranges.
- **Third-party estimators disagree** (AppBrain, SimilarWeb, Sensor Tower) and with vendors; several figures here come from indexed snippets, not fully rendered pages.
- **Platform med-feature usage is unmeasurable from outside** — ranks 1–3 are reach-based judgment, flagged.
- **NL *active* usage is unverified** for most apps except where a store rank exists (MyTherapy #1 NL Medical) or the app is NL-native (MedGemak, Service Apotheek).
- **Not fully nailed down (low confidence):** BENU/Belgian apps, the MedMij/Ivido/Quli NL data-exchange ecosystem, France's MaPharma. Candidates for a v2.

## Sources (accessed 2026-06-23)

**Dedicated apps** — Medisafe: medisafe.com; play.google.com/store/apps/details?id=com.medisafe.android.client; paywall reported Feb 2026. MyTherapy: smartpatient.eu/blog/smartpatient-at-ten; App Store id662170995; SimilarWeb Medical NL rank (2026-06-20); Redcare/Shop Apotheke acquisition (Crunchbase 2021-01-07). Mango Health → PatientLink: PRNewswire (Sep 2019), PatientLink launch (28 Apr 2022). CareZone: CNBC/HIT Consultant (Jun 2020); Walmart Health shutdown (30 Apr 2024). Dosecast / Round Health / Pillboxie / Pill Reminder — All in One / MyMeds: respective App Store / Google Play / AppBrain listings.

**Platform / big-tech** — Apple Health Medications (US-only): support.apple.com/guide/iphone/iph2fcefa8d6; macrumors.com/guide/ios-16-health-app. Samsung Health: news.samsung.com (Oct 2024 update; FR/DE/IT/NL/PL list; "2/3 use 3×/week"); VivaTech 2026 (77M MAU, Apr 2026); play.google.com/store/apps/details?id=com.sec.android.app.shealth (1B+ installs). MyFitnessPal: businessofapps.com/data/myfitnesspal-statistics; electroiq.com/stats/myfitnesspal-statistics. Flo: flo.health/newsroom; businessofapps.com/data/flo-statistics; Tech.eu (30 Jul 2024).

**Pharmacy / PBM / NL-EU** — GoodRx: en.wikipedia.org/wiki/GoodRx; GoodRx Q1 2025 earnings. Walgreens: brainstation.io/magazine/walgreens-60-million-app-downloads; Statista 2020-2024. CVS: statista.com/statistics/1481701; CVS Health app press (14.1M monthly; MedRemind via pharmacytimes.com). Express Scripts: express-scripts.com/mobile-app. Amazon Pharmacy: statista.com/statistics/1482777; Business Insider ($2B 2024); aboutamazon.com (PillPack + Alexa). Walmart Pharmacy: appbrain.com/app/walmart-pharmacy-app/ca.walmart.pharmacy. Service Apotheek: appbrain.com (~720k); serviceapotheek.nl/serviceapotheek-app/handleiding (DigiD/caregiver/Genomen-Overgeslagen). MedGemak: appbrain.com (1.1M); patientenfederatie.nl/apps/medicijngebruik/medgemak. MedApp: medapp.nl/de-app; App Store id1527313551 (NL Medical); play.google.com/store/apps/details?id=nu.medapp.apotheek (~1,300 ratings). NHS App: gov.uk/government/news/nhs-app-hits-over-30-million-sign-ups; digitalhealth.net (39M, Dec 2025); england.nhs.uk (2.7M prescriptions feature). Pharmacy2U: pharmacy2u.co.uk/our-services/our-app.

**Visuals** — Real in-app flows via Mobbin (cited per card in the artifact: Apple Health, GoodRx, Epsy, Visible). App Store / Google Play screenshots via the iTunes Lookup API and live Play HTML.
