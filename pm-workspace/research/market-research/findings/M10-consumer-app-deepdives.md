# M10 — Deep-Dive Profiles: The Most Successful Consumer Health & Wellness Apps

**Module:** M10 (Consumer-App Deep-Dives — retention benchmarks)
**Prepared for:** ditto.care — EU/NL health-tech, building from AI appointment summaries toward a daily "Living Health Companion"
**Author:** Consumer-product research analyst
**Date / access date:** 2026-06-10
**Scope:** Click-to-expand "deep dive" overlays for the market-research deck. Profiles of category-leading consumer health/wellness apps across (1) cycle/pregnancy/women's health, (2) meditation/mental wellness, (3) symptom tracking & emotional journaling, (4) fitness/nutrition "super apps" & wearables — with scale, retention, business model, geography, and the habit/retention mechanism behind each.

> **Sourcing conventions.** Inline citations use `[Source, year](url)`. **Tier 1 (T1)** = analyst / company-verified / financial-grade; **Tier 2 (T2)** = reputable press; **Tier 3 (T3)** = blog / vendor stat-aggregator / app-store self-report (explicitly **FLAGGED**). Confidence tags (high/med/low). **US→EU flag** marks data drawn from US-skewed samples that may not transfer to ditto's EU/NL context. Where figures come from stat-aggregator pages (Business of Apps, GetLatka, ElectroIQ, Sacra), they are flagged T2/T3 and treated as order-of-magnitude reliable, exact-decimal indicative. **Nothing here is fabricated**: any metric I could not source is marked *unconfirmed*.

---

## Key takeaways

- **Cycle/women's health is the strongest consumer-health retention category, and it is EU-rooted.** Flo (UK/Lithuania) hit **~77M MAU, ~5M paid subs, ~$275M revenue (2025)** and **Europe's first femtech unicorn** at ~$1B ([Business of Apps, 2026](https://www.businessofapps.com/data/flo-statistics/); T2, med). Clue (Berlin) crossed **1M paid subs**, doubling in ~a year ([Clue, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform); T1, med). The category leaders ditto should benchmark are *its own neighbors*, not US apps.
- **The wearable "data moat" is real and quantified — and it is a subscription moat, not just a sensor moat.** Oura reports **>80% of members renew after year one** ([Forerunner, 2025](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company); T2, med); Whoop reports **>50% of members still use it daily at 18 months** ([ringingthebell, 2025](https://ringingthebell.substack.com/p/whoop-vs-oura-the-10-billion-question); T3, med). Both reached **~$1B revenue and ~$10–11B valuations in 2025** ([CNBC, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html); T2, high). The flywheel is *passive capture → compounding data → better coaching → renewal*.
- **Meditation peaked and is decaying; it is now an AI story.** Calm fell to **~3.5M subs / ~$210M revenue in 2025** (down ~24% YoY) and Headspace to **~2M subs / ~$140M** ([Business of Apps, 2026](https://www.businessofapps.com/data/calm-statistics/); T2, low-med). The growth narrative shifted to AI companions — Headspace's **Ebb** has processed **7M+ messages** and is offered by **2,000+ employers** ([HIT Consultant, 2025](https://hitconsultant.net/2025/12/08/headspace-updates-ebb-ai-with-voice-mode-and-enhanced-memory-to-deepen-mental-health-support/); T2, med).
- **The journaling/symptom-tracking space splits sharply: gamified/emotional companions retain, clinical loggers churn.** Finch (gamified self-care pet) reports **~10M MAU, ~$30M ARR, 54%/37% D1/D7 retention** — Duolingo-class ([Sparrow/Deconstructor of Fun, 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl); T3 FLAG, med). Clinical symptom loggers (Bearable ~900K users, MindDoc ~3M) are useful but show no public evidence of comparable stickiness — they are the *effort-today-for-deferred-payoff* failure mode.
- **The fitness "super apps" win on network and identity, not features.** Strava reached **180M registered users, ~$500M ARR, ~$2.2B valuation (2025)** on a social-graph moat ([Business of Apps, 2026](https://www.businessofapps.com/data/strava-statistics/); [getLatka, 2025](https://getlatka.com/companies/strava); T2/T3, med). MyFitnessPal (**~220M registered, 30M+ MAU, ~$310M**) retains on its food database moat but is declining ([Business of Apps, 2026](https://www.businessofapps.com/data/myfitnesspal-statistics/); T2, med).
- **Fitbit is the cautionary tale: a wearable without a subscription/coaching loop erodes.** App MAU slid from ~48M (2021) toward ~42M, with the dedicated-app daily-use base far smaller ([Business of Apps, 2026](https://www.businessofapps.com/data/fitbit-statistics/); T2, low-med). Hardware ubiquity ≠ engagement; the moat is the *recurring interpreted-insight*, not the device.
- **What every winner shares (and what ditto can borrow):** a **daily-relevant, anticipatory question with a changing answer**, **compounding personal data** as a switching cost, **passive capture** (wearables) or **near-zero-effort logging** (one-tap mood/cycle), and **social/streak reinforcement**. ditto's episodic appointment summary must be wrapped in a daily, predictive, compounding loop or it inherits the 90-day churn curve.

---

## 1. Cycle / pregnancy / women's health

The single strongest retention category in consumer health, for structural reasons: the underlying biology *changes daily*, the user has a *daily-relevant, emotionally charged question* the app uniquely answers, and each logged cycle compounds prediction accuracy (a switching cost). **Three of the four leaders are EU-rooted** — the most transferable peer set for ditto.

| App | Scale (2024–26) | Retention | Why it wins | URL |
|---|---|---|---|---|
| **Flo** (UK/Lithuania) | ~77M MAU; >300M registered; ~48.6M downloads in 2025; ~5M paid subs; ~$275M revenue 2025; ~$1B valuation, Europe's first femtech unicorn | ~60% of MAU use Flo >1 yr (≈2× H&F norm) [(prior M7)](https://flo.health/) | Daily cycle prediction + AI assistant; anticipatory "fertile window / is this normal"; data compounds per cycle | [flo.health](https://flo.health/) |
| **Clue** (Berlin, DE) | ~10M+ MAU in 190 countries; **1M paid subs (doubled in ~1 yr, 2025)**; 530M+ cycles tracked; 13B+ de-identified data points | "Subscriber retention substantially above industry averages" (company) | Science/privacy-led brand; refuses to disclose data to US authorities (trust moat); research dataset | [helloclue.com](https://helloclue.com/) |
| **Natural Cycles** (Sweden) | >3M users (2024); first **FDA-cleared** birth-control app; raised $55M (2024); Oura integration since 2022 | 98% of Oura-integration survey users said they'll keep tracking (self-report) | *Usage is the product*: daily temperature entry gates a regulated contraceptive claim — irreplaceable | [naturalcycles.com](https://www.naturalcycles.com/) |
| **Ovia** (US, Labcorp) | 22M+ family/parenthood journeys since 2012; B2B2C via 305+ employer/payer/health-system clients | No reliable public DAU/MAU/retention (*unconfirmed*) | Distribution moat (employer benefit), not D2C habit; full continuum fertility→pregnancy→parenting | [oviahealth.com](https://www.oviahealth.com/) |

**Sources & tiers:** Flo — [Business of Apps, 2026](https://www.businessofapps.com/data/flo-statistics/) (T2, med); [GetLatka, 2025](https://getlatka.com/companies/flo.health) (T3 FLAG — note GetLatka's ARR figure ($157.6M) diverges from Business of Apps' $275M revenue, likely ARR-vs-gross-billings; med). Clue — [helloclue, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform) (T1 company, med); [Newsweek, 2024](https://www.newsweek.com/period-tracking-app-refuses-disclose-data-american-authorities-1982841) (T2, high). Natural Cycles — [Tech.eu, 2024](https://tech.eu/2024/05/29/worlds-first-contraceptive-app-natural-cycles-raises-55m/) (T2, high); [Oura, 2024](https://ouraring.com/blog/oura-partners-with-fda-cleared-birth-control-app-natural-cycles/) (T1 company, med). Ovia — [Ovia 2025 recap](https://www.oviahealth.com/blog/reflecting-on-2025-ovia-health-by-labcorps-year-of-growth-and-innovation/) (T1 company, low — engagement metrics unconfirmed).

**Mechanism (why this category dominates):** (1) **daily internal trigger** — the cycle question recurs every day and is anxiety-charged; (2) **anticipatory reward** — the app forecasts something *not yet known* (next period, fertile window, due date), the literal definition of a variable reward; (3) **life-stage urgency** — TTC / avoiding pregnancy / pregnancy compresses the effort-to-payoff calculus in the product's favor; (4) **compounding data** — each logged cycle is a switching cost. **US→EU flag: low** for this category (Flo, Clue, Natural Cycles all EU).

---

## 2. Meditation / mental wellness

Meditation retains via **ritual + immediate felt reward + streaks**, but lacks the *predictive, irreplaceable* data moat of cycle tracking — so it peaked (MAU ~2019, revenue ~2021) and is now declining. The 2024–26 narrative is **AI companions** bolted onto the content libraries to manufacture a daily conversational trigger.

| App | Scale (2025) | Retention/engagement | Why it wins (and the decay) | URL |
|---|---|---|---|---|
| **Calm** (US) | ~3.5M paid subs (−500K YoY); ~$210M revenue (−24% YoY); ~$2B valuation (2020 Series C, stale) | DAU/MAU not disclosed; declining subs signals churn pressure | Sleep Stories + celebrity voices + streaks; "Spotify of sleep" content moat; bedtime ritual trigger | [calm.com](https://www.calm.com/) |
| **Headspace** (US, Headspace Health w/ Ginger, ~$3B valuation) | ~2M paid subs (−300K YoY); ~$140M revenue; ~85M lifetime downloads; MAU ~14.6% of members | Member MAU ~14.6% (low daily stickiness for the category) | Structured courses + B2B/employer channel; **Ebb** AI companion: 7M+ messages, 2,000+ employers | [headspace.com](https://www.headspace.com/) |
| **Ebb (Headspace AI, 2026 notable)** | Embedded in Headspace; 7M+ messages since late-2024 launch; voice mode + memory added Dec 2025 | Heavy use for stress/anxiety/sleep; retention TBD (*unconfirmed*) | AI-driven daily conversational trigger — the category's bet to recover a *recurring* reason to open | [headspace.com/ai](https://www.headspace.com/ai) |

**Sources & tiers:** Calm — [Business of Apps, 2026](https://www.businessofapps.com/data/calm-statistics/) (T2, med); [Sacra](https://sacra.com/c/calm/) (T2, med — valuation stale). Headspace — [Business of Apps, 2026](https://www.businessofapps.com/data/headspace-statistics/) (T2, med); MAU% from [JMIR Formative Research, 2026](https://formative.jmir.org/2026/1/e86904) (T1, med). Ebb — [HIT Consultant, 2025](https://hitconsultant.net/2025/12/08/headspace-updates-ebb-ai-with-voice-mode-and-enhanced-memory-to-deepen-mental-health-support/) (T2, med); [Fast Company, 2024](https://www.fastcompany.com/91206737/headspace-mental-health-generative-ai-chatbot-ebb-exclusive) (T2, high).

**Mechanism:** strong *habit/streak* loop and *immediate* affective reward (calm now), but the answer doesn't materially change day-to-day, there's no compounding personal-data moat, and value is substitutable (free YouTube/Spotify). Hence subscriber erosion despite brand strength. **US→EU flag: med** — both are US-led, EU penetration lower; mindfulness norms differ. **Lesson for ditto:** a pure content/ritual loop is not durable without predictive, personalized, compounding value.

---

## 3. Symptom tracking & emotional journaling

This space splits cleanly. **Gamified emotional companions retain at Duolingo-class rates; clinical symptom loggers are valuable but churn-prone** because they demand effort *today* for a payoff that is deferred/abstract. (The founder's "Behave"-type journaling = the real apps below: Finch, Daylio, How We Feel, Stoic on the companion side; Bearable, MindDoc on the clinical-logger side.)

| App | Scale | Retention | Why it retains / churns | URL |
|---|---|---|---|---|
| **Finch** (US, self-care pet) | ~10M MAU; ~$30M ARR; bootstrapped (no VC); >$1M/mo Android alone | **54% D1 / 37% D7** (≈ Duolingo 51%/35%) — RETAINS | Gamified pet you nurture *by* self-care; daily checklist + rewards + "Good Vibes" micro-social; evolving pet = compounding investment | [finchcare.com](https://finchcare.com/) |
| **Daylio** (CZ) | ~18M lifetime downloads; 4.75★ / 420K ratings | No public retention (*unconfirmed*); strong rating signal | Near-zero-effort one-tap mood + activity logging; low friction = the only logger that beats the effort tax — RETAINS (qualitatively) | [daylio.net](https://daylio.net/) |
| **How We Feel** (US, non-profit) | App Store Cultural Impact Award; Yale-backed (Marc Brackett); friend check-ins added 2025 | No public MAU/retention (*unconfirmed*) | Emotion-granularity (Mood Meter) + social check-ins; free/non-profit limits scale but high craft — MIXED | [howwefeel.org](https://howwefeel.org/) |
| **Stoic** (DE) | ~4M+ users; AI-powered insights | No public retention (*unconfirmed*) | Morning/evening prompted journaling ritual + AI pattern insights + mood tracking — habit-led, RETAINS qualitatively | [getstoic.com](https://www.getstoic.com/) |
| **Bearable** (UK) | ~700K–900K users | >75% feel "more in control" (self-report); no retention data (*unconfirmed*) | Powerful all-in-one symptom/med/trigger correlation for chronic-illness; high value but high logging effort — CHURN-PRONE | [bearable.app](https://bearable.app/) |
| **MindDoc / MoodPath** (DE) | ~3M users; 4.7★ / 26K reviews | No public retention (*unconfirmed*) | CBT-based mood monitoring + screening; clinically credible but assessment-driven, effort-heavy — CHURN-PRONE | [minddoc.com](https://minddoc.com/) |

**Sources & tiers:** Finch — [Deconstructor of Fun, 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl) (T3 FLAG, med); [Sparrow, 2024](https://blog.sparrowapps.io/p/finch-how-a-self-care-app-hit-30m-arr-without-vc-money) (T3 FLAG, med). Daylio — [Similarweb / Wikipedia](https://en.wikipedia.org/wiki/Daylio) (T3 FLAG, low-med). How We Feel — [Yale Medicine](https://medicine.yale.edu/news-article/the-how-we-feel-app-helping-emotions-work-for-us-not-against-us/) (T1/T2, med). Stoic — [App Store](https://apps.apple.com/us/app/stoic-journal-mental-health/id1312926037) (T3 FLAG self-report, low). Bearable — [bearable.app](https://bearable.app/) (T3 self-report, low). MindDoc — [App Store](https://apps.apple.com/us/app/minddoc-mental-health-support/id1052216403) (T3 self-report, low).

**Mechanism (the split):** *Retainers* (Finch, Daylio, Stoic) win by either **gamifying the investment** (Finch's pet = a living streak), **eliminating the effort tax** (Daylio one-tap), or **wrapping logging in a daily ritual with AI feedback** (Stoic). *Churners* (Bearable, MindDoc) ask for **structured, effortful, clinical logging** whose payoff is deferred and abstract — the exact failure mode that afflicts most health loggers and the trap an episodic appointment-summary product can fall into. **US→EU flag: low-med** — Daylio (CZ), Stoic (DE), MindDoc (DE), Bearable (UK) are EU-rooted; Finch/HWF are US.

---

## 4. Fitness & nutrition "super apps" + wearables

Two distinct moats here. **Super apps** (MyFitnessPal, Strava, Samsung Health) retain on a *data/network asset* — a food database or a social graph. **Wearables** (Whoop, Oura) retain on *passive capture + a subscription coaching loop* — the founder's "data moat" question. The answer: **the moat is real and quantified, but it is the recurring interpreted insight + subscription switching cost, not the sensor itself** (Fitbit proves a device without that loop erodes).

| App | Scale (2025) | Retention | Why it wins | URL |
|---|---|---|---|---|
| **Whoop** (US, wearable) | 2.5M+ members; ~$1.1B revenue run-rate (+103% YoY); $10.1B valuation; cash-flow positive | **>50% of members use daily at 18 months; record-low churn** | Subscription-ONLY (no device fee at entry) → switching cost; recovery/strain coaching; passive 24/7 capture; data flywheel | [whoop.com](https://www.whoop.com/) |
| **Oura** (Finland, wearable) | 5.5M+ rings sold (~3M in 2025); ~$1B revenue (2x YoY); on pace >5M paid members Q2'26; $11B valuation | **>80% of members renew after year 1** | Passive sleep/readiness capture + daily "Readiness Score"; ~52% smart-ring share + IP-enforcement moat; 80% hardware / 20% subscription mix | [ouraring.com](https://ouraring.com/) |
| **MyFitnessPal** (US, super app) | ~220M registered; 30M+ MAU; ~$310M revenue (−5.7% YoY) | Sticky via logged-data history; revenue declining | Largest food database (logging moat) + barcode scan; calorie-tracking habit; integrations hub | [myfitnesspal.com](https://www.myfitnesspal.com/) |
| **Strava** (US, super app/network) | 180M registered (+35M YoY); 76M "customers"; ~$500M ARR; ~$2.2B valuation (2025) | Network effects drive retention (kudos/segments) | Social graph + segment leaderboards = identity & accountability; the "Facebook of fitness" — hardest moat to copy | [strava.com](https://www.strava.com/) |
| **Samsung Health** (KR) | ~64–65M MAU; 1B+ downloads; AI "proactive intelligence" (2025) | No public retention (*unconfirmed*) | Pre-installed on Galaxy (distribution moat) + Galaxy Watch sensor loop; AI health companion direction | [samsung.com/.../samsung-health](https://www.samsung.com/global/galaxy/apps/samsung-health/) |
| **Apple Fitness+** (US) | Subs not disclosed (*unconfirmed*); ~17% fitness-app share; expanded +28 markets (Dec 2025) | Not disclosed (*unconfirmed*) | Apple Watch lock-in + content; bundled in Apple One; ecosystem moat | [apple.com/apple-fitness-plus](https://www.apple.com/apple-fitness-plus/) |
| **Zwift** (US/UK, indoor cycling) | ~750K–900K est. subscribers; 1M+ active (2024); ~37.5K concurrent peak (2025, down from 49K in 2021) | Declining concurrency post-pandemic | Gamified virtual-world workouts + group rides (social) on a subscription; niche but loyal | [zwift.com](https://www.zwift.com/) |

**Sources & tiers:** Whoop — [Yahoo Finance / Whoop, 2025](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html) (T2, high); daily-use stat [ringingthebell, 2025](https://ringingthebell.substack.com/p/whoop-vs-oura-the-10-billion-question) (T3 FLAG, med). Oura — [CNBC, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html) (T2, high); [BusinessWire, 2025](https://www.businesswire.com/news/home/20250922351288/en/) (T1 company, high); renewal stat [Forerunner, 2025](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company) (T2, med). MyFitnessPal — [Business of Apps, 2026](https://www.businessofapps.com/data/myfitnesspal-statistics/) (T2, med). Strava — [Business of Apps, 2026](https://www.businessofapps.com/data/strava-statistics/) (T2, med); [getLatka, 2025](https://getlatka.com/companies/strava) (T3 FLAG, med). Samsung Health — [Samsung Newsroom, 2025](https://news.samsung.com/global/samsung-introduces-next-gen-galaxy-watch-features-for-ai-powered-everyday-health-companion) (T1 company, med). Apple Fitness+ — [Apple Newsroom, 2025](https://www.apple.com/newsroom/2025/12/apple-fitness-plus-expands-to-28-new-markets/) (T1 company, med — subs unconfirmed). Zwift — [Zwift Insider / the5krunner, 2025](https://zwiftinsider.com/level-stats-2025/) (T3 FLAG, low-med). Fitbit decline — [Business of Apps, 2026](https://www.businessofapps.com/data/fitbit-statistics/) (T2, low-med).

**Mechanism — does the "data moat" work like Oura/Whoop?** Yes, with a precise structure: **passive capture removes the effort tax** (no daily logging), **the daily score is an anticipatory reward** (today's readiness/recovery is unknown until you check), **longitudinal data compounds** into better personalization and a switching cost (leaving = losing your baseline), and crucially **a subscription locks in recurring revenue and re-engagement**. Whoop made the subscription the *entire* model; Oura attaches a membership to the device. **Fitbit is the counter-example:** ubiquitous hardware, weak interpreted-insight + subscription loop → eroding app engagement. **US→EU flag: med** — Oura (Finland) is the most EU-transferable; Whoop/Strava/MFP are US but globally distributed.

---

## What these winners share (and what ditto can borrow)

1. **A daily-relevant trigger with a *changing* answer.** Cycle phase, readiness score, mood-of-the-day. ditto's appointment summary is episodic; it must generate a daily question whose answer moves ("Given your visit + today's data, here's what to watch / ask / do today").
2. **Anticipatory / predictive value.** Flo forecasts the cycle; Oura forecasts recovery. Users open to learn something *not yet known*. ditto should turn passive records into a forward-looking nudge (upcoming refills, follow-ups, what to flag next visit).
3. **Compounding personal data = switching cost.** Each cycle/night/log makes tomorrow better and raises the cost of leaving. ditto's longitudinal health record + visit history is exactly this asset — but only if the app *re-surfaces* it daily (Daylio/Bearable churn because users never revisit the log).
4. **Passive capture or near-zero-effort logging.** Wearables win by capturing without asking; Daylio wins by one-tap. ditto should minimize manual entry — ingest from clinicians, wearables, and pharmacies; ask for at most one tap.
5. **Social / streaks / accountability.** Strava's graph, Finch's pet, meditation streaks. A light social or self-accountability layer (gentle streaks, family/partner sharing as in TTC apps) multiplies retention.
6. **Subscription as a re-engagement and switching-cost mechanism (Whoop/Oura), not just monetization.** The recurring relationship *is* part of the moat.

**Net for ditto:** the appointment summary is high-value but episodic — the symptom-tracker failure mode at the visit level. Wrapping it in a **daily, predictive, compounding, low-effort, lightly-social loop** is the difference between the cycle-tracker retention curve (~60% past a year) and the median-health-app 90-day churn curve.

---

## Sources

**Tier 1 — company-verified / regulatory / analyst / peer-reviewed**
- [helloclue — 1M paid subscribers, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform)
- [Oura — Natural Cycles partnership, 2024](https://ouraring.com/blog/oura-partners-with-fda-cleared-birth-control-app-natural-cycles/)
- [BusinessWire — Oura 5.5M rings / $1B revenue, 2025](https://www.businesswire.com/news/home/20250922351288/en/)
- [Apple Newsroom — Fitness+ +28 markets, 2025](https://www.apple.com/newsroom/2025/12/apple-fitness-plus-expands-to-28-new-markets/)
- [Samsung Newsroom — Galaxy Watch / Samsung Health, 2025](https://news.samsung.com/global/samsung-introduces-next-gen-galaxy-watch-features-for-ai-powered-everyday-health-companion)
- [Ovia Health — 2025 recap](https://www.oviahealth.com/blog/reflecting-on-2025-ovia-health-by-labcorps-year-of-growth-and-innovation/)
- [JMIR Formative Research — Headspace Ebb AI companion study, 2026](https://formative.jmir.org/2026/1/e86904)
- [Headspace AI principles](https://www.headspace.com/ai)

**Tier 2 — reputable press / financial press**
- [CNBC — Oura $11B valuation, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [Yahoo Finance — Whoop $10.1B / 103% growth, 2025](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html)
- [Business of Apps — Flo statistics, 2026](https://www.businessofapps.com/data/flo-statistics/)
- [Business of Apps — Calm statistics, 2026](https://www.businessofapps.com/data/calm-statistics/)
- [Business of Apps — Headspace statistics, 2026](https://www.businessofapps.com/data/headspace-statistics/)
- [Business of Apps — MyFitnessPal statistics, 2026](https://www.businessofapps.com/data/myfitnesspal-statistics/)
- [Business of Apps — Strava statistics, 2026](https://www.businessofapps.com/data/strava-statistics/)
- [Business of Apps — Fitbit statistics, 2026](https://www.businessofapps.com/data/fitbit-statistics/)
- [Tech.eu — Natural Cycles $55M raise, 2024](https://tech.eu/2024/05/29/worlds-first-contraceptive-app-natural-cycles-raises-55m/)
- [Newsweek — Clue refuses US data disclosure, 2024](https://www.newsweek.com/period-tracking-app-refuses-disclose-data-american-authorities-1982841)
- [Fast Company — Headspace Ebb launch, 2024](https://www.fastcompany.com/91206737/headspace-mental-health-generative-ai-chatbot-ebb-exclusive)
- [HIT Consultant — Ebb voice mode update, 2025](https://hitconsultant.net/2025/12/08/headspace-updates-ebb-ai-with-voice-mode-and-enhanced-memory-to-deepen-mental-health-support/)
- [Forerunner Ventures — Oura $11B perspective (renewal stat), 2025](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company)
- [Sacra — Calm](https://sacra.com/c/calm/) · [Sacra — Oura](https://sacra.com/c/oura/) · [Sacra — Whoop](https://sacra.com/c/whoop/)
- [Yale Medicine — How We Feel](https://medicine.yale.edu/news-article/the-how-we-feel-app-helping-emotions-work-for-us-not-against-us/)

**Tier 3 — blog / stat-aggregator / app-store self-report (FLAGGED — order-of-magnitude reliable, exact decimals indicative)**
- [GetLatka — Flo](https://getlatka.com/companies/flo.health) · [GetLatka — Strava](https://getlatka.com/companies/strava) · [GetLatka — Calm revenue](https://getlatka.com/blog/calm-revenue)
- [ringingthebell — Whoop vs Oura (daily-use stat), 2025](https://ringingthebell.substack.com/p/whoop-vs-oura-the-10-billion-question)
- [Deconstructor of Fun — Finch retention, 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl)
- [Sparrow — Finch $30M ARR, 2024](https://blog.sparrowapps.io/p/finch-how-a-self-care-app-hit-30m-arr-without-vc-money)
- [Zwift Insider — level stats 2025](https://zwiftinsider.com/level-stats-2025/) · [the5krunner — Peak Zwift 2026](https://the5krunner.com/2026/01/23/peak-zwift-2026-indoor-cycling-trends/)
- [Wikipedia — Daylio](https://en.wikipedia.org/wiki/Daylio) · [App Store — Stoic](https://apps.apple.com/us/app/stoic-journal-mental-health/id1312926037) · [bearable.app](https://bearable.app/) · [App Store — MindDoc](https://apps.apple.com/us/app/minddoc-mental-health-support/id1052216403)

---

## Deep-dive blocks (ready-to-embed overlays)

### Block 1 — Cycle / pregnancy / women's health
The strongest retention category in consumer health, and the most directly relevant to ditto because three of the four leaders are EU-rooted (Flo UK/Lithuania, Clue Berlin, Natural Cycles Sweden). Flo reached ~77M MAU, ~5M paid subscribers and ~$275M revenue as Europe's first femtech unicorn; Clue crossed 1M paid subscribers, doubling in roughly a year; Natural Cycles turned daily temperature logging into an FDA-cleared contraceptive claim. They win on a daily-relevant, anxiety-charged, *predictive* question (cycle phase, fertile window, due date) and on data that compounds per cycle into a switching cost. Ovia shows the alternative path — a B2B2C employer-distribution moat rather than a D2C habit.
- [Flo — flo.health](https://flo.health/)
- [Clue — helloclue.com](https://helloclue.com/)
- [Natural Cycles — naturalcycles.com](https://www.naturalcycles.com/)
- [Ovia — oviahealth.com](https://www.oviahealth.com/)
- [Flo scale, Business of Apps 2026](https://www.businessofapps.com/data/flo-statistics/)
- [Clue 1M subs, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform)

### Block 2 — Meditation / mental wellness
The cautionary category: brand-famous but past peak. Calm fell to ~3.5M subscribers / ~$210M revenue (−24% YoY) and Headspace to ~2M / ~$140M in 2025 — proof that a content + ritual loop without predictive, compounding, personalized value erodes once novelty fades and free substitutes exist. The 2024–26 pivot is AI companions: Headspace's Ebb has handled 7M+ messages and is offered by 2,000+ employers, an attempt to manufacture a *daily conversational trigger* the static library never had. For ditto, the read is that engagement requires a changing, personalized answer — not just a polished library.
- [Calm — calm.com](https://www.calm.com/)
- [Headspace — headspace.com](https://www.headspace.com/)
- [Headspace Ebb AI — headspace.com/ai](https://www.headspace.com/ai)
- [Calm scale, Business of Apps 2026](https://www.businessofapps.com/data/calm-statistics/)
- [Ebb 7M+ messages, HIT Consultant 2025](https://hitconsultant.net/2025/12/08/headspace-updates-ebb-ai-with-voice-mode-and-enhanced-memory-to-deepen-mental-health-support/)

### Block 3 — Symptom tracking & emotional journaling
The clearest "retain vs churn" split in the deck. Gamified/ritualized emotional companions retain at Duolingo-class rates — Finch (~10M MAU, ~$30M ARR, 54%/37% D1/D7) turns self-care into nurturing a virtual pet; Daylio wins on one-tap, near-zero-effort logging; Stoic wraps journaling in a morning/evening ritual with AI insights. Clinical symptom loggers — Bearable (~700–900K users) and MindDoc (~3M) — are genuinely useful for chronic illness and mood screening but demand effortful structured logging for deferred, abstract payoff, the exact failure mode an episodic record product must avoid. The lesson: gamify the investment, eliminate the effort tax, or wrap logging in a daily ritual with feedback.
- [Finch — finchcare.com](https://finchcare.com/)
- [Daylio — daylio.net](https://daylio.net/)
- [How We Feel — howwefeel.org](https://howwefeel.org/)
- [Stoic — getstoic.com](https://www.getstoic.com/)
- [Bearable — bearable.app](https://bearable.app/) · [MindDoc — minddoc.com](https://minddoc.com/)
- [Finch retention, Deconstructor of Fun 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl)

### Block 4 — Fitness & nutrition "super apps" + wearables
The founder's "data moat" question answered: it works, and it is a *subscription + interpreted-insight* moat, not just a sensor. Whoop (2.5M+ members, ~$1B run-rate, $10.1B valuation) reports >50% of members still using it daily at 18 months on a subscription-only model; Oura (5.5M+ rings, ~$1B revenue, $11B valuation) reports >80% first-year renewal. Both win on passive capture (no logging effort), a daily anticipatory score, and compounding longitudinal data. The super apps win differently — Strava (180M registered, ~$500M ARR, ~$2.2B) on its social graph, MyFitnessPal (~220M registered, 30M+ MAU) on its food-database moat. Fitbit is the counter-example: ubiquitous hardware but a weak insight/subscription loop, and its app engagement is eroding. ditto's transferable play: passive ingestion + a daily predictive score + a subscription relationship.
- [Whoop — whoop.com](https://www.whoop.com/)
- [Oura — ouraring.com](https://ouraring.com/)
- [Strava — strava.com](https://www.strava.com/) · [MyFitnessPal — myfitnesspal.com](https://www.myfitnesspal.com/)
- [Samsung Health](https://www.samsung.com/global/galaxy/apps/samsung-health/) · [Apple Fitness+](https://www.apple.com/apple-fitness-plus/) · [Zwift](https://www.zwift.com/)
- [Oura $11B + renewal, CNBC 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [Whoop $10.1B, Yahoo Finance 2025](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html)
