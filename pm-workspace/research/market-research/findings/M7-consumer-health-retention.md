# M7 — Teardown of Consumer-Health Retention: Why Some Categories Win and Most Fail

**Module:** M7 (Consumer-Health Retention)
**Prepared for:** ditto.care — building from AI appointment summaries toward a daily "Living Health Companion"
**Author:** Consumer-product research analyst
**Date / access date:** 2026-06-10
**Scope:** Why menstrual/cycle/pregnancy and meditation apps retain users at category-leading rates, why symptom trackers / quantified-self / disease-management apps churn, and the transferable principles for ditto.

> **Sourcing conventions.** Inline citations use `[Source, year](url)`. **Tier 1** = peer-reviewed, financial analyst, or company-verified metrics; **Tier 2** = reputable press; **Tier 3** = blog / vendor / self-report (explicitly FLAGGED). Confidence tags: (high/med/low). **US→EU flag** marks data drawn from US samples that may not transfer to ditto's EU/NL context. Several company stat pages (Business of Apps, Flo newsroom, Udonis) and the JMIR/PMC journal pages returned HTTP 403 to direct fetch; figures from those are cited from their search-surfaced snippets and **flagged as snippet-sourced** where the underlying page could not be opened — treat the exact decimals as indicative, the order of magnitude as reliable.

---

## Key takeaways

- **Retention is a category property, not an execution property.** Flo retains ~60% of its monthly active users for more than a year ([Flo Health, 2024](https://flo.health/newsroom/flo-reaches-22m-monthly-active-users); snippet-sourced, Tier 1, med) — roughly **double** the typical Health & Fitness app. Most health apps lose the majority of users within 90 days; medical apps average ~34% and fitness ~31% 90-day retention ([Alchemer, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/); Tier 3, med). The winning categories are not better-built versions of the losers — they sit on a fundamentally better behavioral substrate.
- **The winners share one structural advantage: a daily-relevant, anticipatory question.** "Where am I in my cycle / is this normal / when is my fertile window" and "help me sleep / de-stress tonight" are questions a user *re-asks every day*, and the app's answer changes daily. That is the precondition every churning category lacks.
- **Cycle/pregnancy tracking is the strongest consumer-health retention category in existence.** Flo reports ~70M MAU and ~420M registered users (2024) with ~5M paid subscribers ([Flo Health milestone, 2024](https://flo.health/newsroom/flo-reaches-22m-monthly-active-users); snippet-sourced, Tier 1/2, med); Clue crossed **1M paid subscribers**, more than doubling in ~a year, with "subscriber retention substantially above industry averages" ([Clue / helloclue, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform); Tier 1 company, med).
- **Meditation retains via ritual and felt reward, but is weaker and decaying.** Calm reached ~$596M revenue and a $2B valuation with ~4M+ paid subscribers ([Sacra](https://sacra.com/c/calm/) / [GetLatka, 2024](https://getlatka.com/blog/calm-revenue); Tier 1/2, med); Headspace shows DAU/MAU ~17% and is **past peak** (MAU peaked ~2019, revenue ~2021) ([Sequoia / industry analysis](https://articles.sequoiacap.com/measuring-product-health); snippet-sourced, Tier 2, low-med). Meditation works on habit/streaks + immediate reward, but lacks the *predictive, irreplaceable* data moat of cycle tracking — hence the decay.
- **The losers churn for a structural reason, not a polish reason:** symptom trackers, generic wellness logging, and many disease-management apps demand effort *today* for a payoff that is **deferred, abstract, or never arrives**. App-based chronic-disease interventions show pooled dropout ~43% ([JMIR meta-analysis, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/); Tier 1, high); diabetes-app trials ~29.6% dropout ([Diabetes Res Clin Pract meta-analysis, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0168822724006338); Tier 1, high); and only ~27–34% of mHealth users remain active by months 4–6 ([JMIR literature review, 2022](https://www.jmir.org/2022/4/e35120/); snippet-sourced, Tier 1, med).
- **The Hook Model maps cleanly onto the divide** ([Eyal, *Hooked*, 2014](https://www.nirandfar.com/how-to-manufacture-desire/); Tier 1 framework, high): winners pair a strong *internal trigger* (recurring anxiety/curiosity), a *low-effort action*, a *variable reward* (changing daily answer), and *compounding investment* (your own longitudinal data). Losers break the loop — usually at the reward and the trigger.
- **For ditto, the strategic implication is sharp:** appointment summaries are a high-value but *episodic* artifact (the symptom-tracker failure mode at the visit level). The "Living Health Companion" must manufacture a **daily-relevant, anticipatory question with a changing answer and compounding personal data** — or it will inherit the 90-day churn curve, not the cycle-tracker curve.

---

## 1. The winners — why they retain

### 1.1 Menstrual / cycle & pregnancy tracking

This is the single strongest retention category in consumer health. The reason is structural: the underlying biological process *changes every day*, the user has a *daily-relevant question* whose answer the app uniquely holds, and the data the user contributes makes tomorrow's answer better (compounding).

**Verified scale, retention, monetization:**

| App | Scale | Retention | Monetization | Source (tier, confidence) |
|---|---|---|---|---|
| **Flo** | ~70M MAU; ~420M registered users; ~380M downloads (2024). Later press cites ~75–77M MAU into 2025. | **~60% of MAU use Flo for >1 year** — ~2× the Health & Fitness norm | ~5M paid subscribers (2024); first purely-digital women's-health app to reach unicorn status (~$200M raise, General Atlantic) | [Flo Health milestone, 2024](https://flo.health/newsroom/flo-reaches-22m-monthly-active-users); [General Atlantic, 2024](https://www.generalatlantic.com/media-article/flo-health-secures-more-than-200m-investment-from-general-atlantic-to-revolutionize-womens-health-first-purely-digital-consumer-womens-health-app-to-achieve-unicorn-status/) (Tier 1/2 company-verified; med — exact MAU snippet-sourced) |
| **Clue** | 4.8★ over 2.5M reviews; broad free base skewing to women in their 20s–30s | "Subscriber retention rates substantially above industry averages"; 81% feel more prepared for symptoms, 72% feel greater control of health (self-report) | **1M paid subscribers**, doubled in ~1 year (May 2025) | [Clue / helloclue, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform) (Tier 1 company / Tier 3 self-report for the % stats; med) |
| **Natural Cycles** | >3M users worldwide (May 2024) | Subscription gated on daily/near-daily temperature entry — usage *is* the product | Subscription; raised $55M (2024); FDA-cleared birth control (510(k)), 93% typical-use / 98% perfect-use effective | [Tech.eu, 2024](https://tech.eu/2024/05/29/worlds-first-contraceptive-app-natural-cycles-raises-55m/); [FDA K250561, 2025](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250561.pdf) (Tier 1/2; high) |
| **Ovia** | Suite across fertility/pregnancy/parenting; largely employer/health-plan distributed | No reliable public DAU/MAU/retention figure located | B2B2C (employer & payer benefits) — distinct from D2C subscription | [Ovia Health](https://www.oviahealth.com/) (Tier 1 company; low — metrics unconfirmed) |

> **Note:** Natural Cycles is a *European* company (Sweden) operating EU-wide, the most directly transferable peer for ditto's NL/EU context. Flo (UK/Lithuania), Clue (Germany) are also EU-rooted, reducing the US→EU flag for this category.

**WHY cycle/pregnancy tracking retains (mechanism):**

1. **Frequency of a relevant trigger (daily, internal).** The defining question — *"where am I in my cycle, am I fertile, is this symptom normal, how far along am I"* — recurs daily and is emotionally charged. This is a strong *internal trigger* in Hook-Model terms ([Eyal, 2014](https://www.nirandfar.com/how-to-manufacture-desire/)).
2. **Predictive / anticipatory value.** The app forecasts the next period, fertile window, or due date. Anticipation is the rarest and most defensible retention asset: the user opens the app to learn something *not yet known*, the literal definition of a variable reward.
3. **Anxiety reduction / life-stage urgency.** Trying-to-conceive, avoiding pregnancy, and pregnancy itself are high-stakes, time-bounded life stages. Urgency compresses the effort-to-reward calculus in the product's favor — the same payoff that feels optional in a wellness logger feels essential here.
4. **Data compounding.** Each logged cycle improves the personalization and prediction accuracy. The user's *own historical data* becomes a switching cost and a moat — leaving means losing months of baseline. This is the "investment" phase of the Hook loop, and it is far stronger here than in any logging app whose data the user never revisits.
5. **Network / partner & social proof.** Partner-sharing (TTC), community forums, and "is this normal?" comparison provide *social reward* and offload reassurance the user would otherwise seek from a clinician.

The combination — daily trigger × anticipatory reward × compounding personal data × life-stage urgency — is why ~60% of Flo's MAU persist past a year while the median health app is mostly gone by day 90.

### 1.2 Meditation / mental wellness

Meditation apps are the second-strongest retention category, but the mechanism is weaker — and the data shows decay.

**Verified scale, economics, retention:**

| App | Scale / revenue | Retention / engagement | Source (tier, confidence) |
|---|---|---|---|
| **Calm** | ~$596M revenue (2024); ~140M downloads lifetime; ~$2B valuation; ~4M+ (peak ~5M in 2022) paid subscribers | Subscription churn pressure visible — subscriber estimates declined from 2024→2025 in some trackers | [Sacra](https://sacra.com/c/calm/); [GetLatka, 2024](https://getlatka.com/blog/calm-revenue) (Tier 1/2; med) |
| **Headspace** | ~$3B-scale wellness business (merged Ginger → Headspace Health); revenue past peak (~Jan 2021) | **DAU/MAU ~17%** (users don't meditate daily even when paid); retention curve ~D1 30% / D7 12% / D30 6% — *strong vs. broad app market but modest absolutely*; MAU peaked ~April 2019 | [Sequoia, product-health analysis](https://articles.sequoiacap.com/measuring-product-health); [Udonis stats](https://www.blog.udonis.co/statistics/headspace) (Tier 2/3; low-med — snippet-sourced, exact figures indicative) |

**WHY meditation retains (mechanism):**

1. **Habit / streaks / identity.** Streak counters and daily reminders convert use into an identity ("I'm someone who meditates"). Gamified streaks are explicitly credited as a retention lever for both Calm and Headspace ([Sifars, 2024](https://www.sifars.com/en/blog/calm-headspace-monetization-strategy-ai/); Tier 3, med).
2. **Daily ritual + immediate felt reward.** Unlike a symptom log, a 10-minute session delivers an *immediate* affective payoff (calm, reduced stress). Reward arrives in-session, not deferred — the effort-to-reward ratio is favorable *today*.
3. **Content variety as a renewable variable reward.** Fresh daily content, new courses, celebrity sleep stories — novelty substitutes for the biological novelty that cycle apps get for free. This is why "constantly releasing fresh content" is named as a core retention tactic ([Sifars, 2024](https://www.sifars.com/en/blog/calm-headspace-monetization-strategy-ai/); Tier 3).
4. **The sleep use-case is the killer app.** Sleep stories/soundscapes attach the product to a *nightly, involuntary* trigger (going to bed). This is the closest meditation gets to the cycle app's structural daily trigger.

**Why meditation is weaker than cycle tracking (and decays):** the reward is *replaceable* (any calming content works; no personal data moat), the trigger is *aspirational* not *anxious* (skipping a meditation has no consequence; skipping a fertility log might), and there is little **data compounding** — your 200th session is not more valuable because of your first 199. Hence DAU/MAU ~17% and post-pandemic decline. **Lesson for ditto:** ritual + immediate reward buys engagement, but without anticipatory/compounding value it plateaus and erodes.

---

## 2. The losers / cautionary tales — why they churn

The losing categories — **general symptom trackers, generic quantified-self / wellness logging, and many disease-management apps** — share the inverse profile: effort is required *today*, the reward is *deferred, abstract, or absent*, the trigger is *external and weak*, and the user's data does not visibly compound.

**Verified attrition evidence:**

| Category / benchmark | Figure | Source (tier, confidence) |
|---|---|---|
| Broad app market — health vertical | **~71% of users disengage within 90 days**; medical apps ~34% / fitness ~31% 90-day retention (vs. ~48% macro avg) | [Alchemer healthcare benchmarks, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/) (Tier 3 vendor; med) |
| mHealth apps generally | Only **~33.5% / 29.3% / 27.1%** of users still active ≥2 days/month in months 4 / 5 / 6 | [JMIR literature review, 2022](https://www.jmir.org/2022/4/e35120/) (Tier 1; med — snippet-sourced) |
| App-based chronic-disease interventions | **Pooled dropout 43%** (95% CI 29–57); observational 49% > RCT 40% | [JMIR meta-analysis, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/) (Tier 1; high) |
| Diabetes-management app trials | **Dropout 29.6%** (95% CI 25–34.3; 36 studies, 3,327 participants) | [Diabetes Res Clin Pract meta-analysis, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0168822724006338) (Tier 1; high) |
| Self-guided mental health apps (non-flagship) | Frequently cited as losing the large majority of users within ~30 days; cost-effectiveness/retention questioned | [EA Forum analysis](https://forum.effectivealtruism.org/posts/2gB8mTyyKJw8PczYQ/self-guided-mental-health-apps-aren-t-cost-effective-yet) (Tier 3; low) |

> Note these are partly *clinical-trial* dropout rates (incentivized, supported cohorts) — real-world D2C retention is generally **worse**, so these understate the consumer churn problem. The JMIR review calls attrition "a ubiquitous problem across all app uses."

**WHY they churn (mechanism — the mirror image of the winners):**

1. **No daily-relevant trigger.** A healthy person has no daily reason to open a generic symptom tracker. The trigger is *external* (a push notification nagging you to log) rather than *internal* (a question you already want answered). External-only triggers decay fast.
2. **Effort > reward.** Manual logging (food, symptoms, glucose, mood) is a daily *tax*. The payoff — a chart, a trend, "insight" — is abstract, deferred, and often never materializes into action. The effort-to-reward ratio is inverted vs. meditation's in-session payoff.
3. **No variable or social reward.** Yesterday's log produces today's identical-looking chart. There is no anticipation (you already know what you ate), and most logging is private — no social reassurance loop.
4. **No compounding value.** Critically, in many trackers the user's accumulated data is *never reflected back* as improving predictions or personalization. Without the "your data makes the product smarter about *you*" loop, there is no switching cost and no investment phase — the Hook loop never closes.
5. **Disease-management specifics:** logging is often *prescribed* (extrinsic motivation), tied to an unwell identity people want to avoid reinforcing, and the clinical benefit is long-horizon. The [JMIR scoping review on abandonment, 2024](https://www.jmir.org/2024/1/e56897) (Tier 1) frames abandonment around exactly this effort/relevance/reward mismatch.

**The cautionary parallel for ditto:** an appointment summary, by itself, is an *episodic artifact* consumed once after a visit — structurally the symptom-tracker failure mode at the encounter level (high one-time value, no recurring trigger, no compounding loop). Excellent summaries can win the *first* moment; they cannot, alone, produce a daily companion's retention curve.

---

## 3. Synthesis — the transferable principles

Mapping winners vs. losers onto a small set of orthogonal levers (grounded in the data above and the Hook Model, [Eyal, 2014](https://www.nirandfar.com/how-to-manufacture-desire/)):

| Principle | Cycle/Pregnancy (winner) | Meditation (mid) | Symptom/QS/Disease logging (loser) | Why it drives retention |
|---|---|---|---|---|
| **Frequency of *relevant* trigger** | Daily, internal (anxiety/curiosity) | Daily-ish, ritual/aspirational | Weak, external (nag) | Internal recurring triggers don't decay |
| **Effort-to-reward ratio** | Low effort, high anticipatory payoff | Low effort, immediate felt payoff | High effort, deferred/absent payoff | Users quit when the tax exceeds the felt benefit |
| **Variable reward** | High — the daily answer *changes* | Medium — content novelty | Low — output is predictable | Uncertainty/anticipation sustains the loop |
| **Social reward** | Partner/community/"is this normal" | Some (groups, leaderboards) | Usually none | Reassurance offloads clinician dependence |
| **Life-stage urgency** | Very high (TTC, pregnancy) | Low | Variable; often chronic/low-salience | Urgency collapses the cost-benefit objection |
| **Predictive / anticipatory value** | Core (forecasts cycle/due date) | Weak | Mostly retrospective charts | The reason to open *before* you know the answer |
| **Data compounding** | Strong (history → better prediction + switching cost) | Weak | Often none | Investment phase = moat + reason to return |
| **Identity / streaks** | Moderate ("planning my family") | Strong (gamified streaks) | Weak/negative ("sick person") | Identity makes use self-reinforcing |

### The ditto checklist (apply to every "Living Health Companion" feature)

For any candidate daily feature, score it against these gates — **a feature that fails the first three will inherit the 90-day churn curve, not the cycle-tracker curve:**

1. **Daily-relevant question (internal trigger):** Does it answer a question the user *already re-asks* most days (e.g., "is my health on track today / should I act on this / what changed since my visit")? If the only trigger is our push notification, it will decay.
2. **Changing answer (variable/anticipatory reward):** Does the answer *change day to day* and tell the user something they don't already know? Static dashboards fail.
3. **Effort ≤ reward, felt today:** Is the payoff immediate and the input near-zero (ideally passive/auto-captured from EHR, summaries, wearables — not manual logging)?
4. **Compounding personal data (investment):** Does each day's use *visibly* make tomorrow's answer more personalized/accurate, creating a switching cost? Reflect the moat back to the user ("based on your last 3 visits…").
5. **Life-stage / salience hook:** Can we anchor to a high-salience moment (post-diagnosis, pregnancy, chronic-condition onset, medication change) where urgency favors daily use?
6. **Social / reassurance loop (optional but powerful):** Can we offload "is this normal?" reassurance — via caregiver/partner sharing or safe comparison — the way Flo/Clue do?
7. **Identity, not illness:** Frame the habit around agency ("staying on top of my health") rather than reinforcing a sick identity, which disease-management apps suffer from.

**Strategic read for ditto:** the appointment-summary product is the *entry artifact* (a strong first-touch, life-stage-salient moment). To cross into companion-grade retention, ditto should convert the episodic summary into a **recurring, anticipatory, compounding daily question** — e.g., "given your last appointment and what's changed since, here's what to watch / do / ask today," refreshed daily, getting smarter with every visit and data point. That is the cycle-tracker pattern translated to clinical care. EU note: GDPR/health-data sensitivity makes the *passive-capture* and *partner-sharing* levers harder than for US peers — design the compounding loop on data the user has already consented to share (their own summaries/EHR), which is also ditto's natural moat.

---

## 4. Framework grounding (theory, used to interpret — not to assert)

- **Hook Model** ([Eyal, *Hooked: How to Build Habit-Forming Products*, 2014](https://www.nirandfar.com/how-to-manufacture-desire/); summarized [Amplitude](https://amplitude.com/blog/the-hook-model); Tier 1 framework, high): Trigger → Action → Variable Reward → Investment. The winners close all four loops; the losers break the Reward and Trigger steps. Used here as the explanatory lens, with the *claims* grounded in the retention data above.
- **Retention-curve / benchmark research:** health-app 90-day retention benchmarks ([Alchemer, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/); Tier 3) and peer-reviewed mHealth attrition ([JMIR 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/), [JMIR 2022](https://www.jmir.org/2022/4/e35120/), [JMIR 2024](https://www.jmir.org/2024/1/e56897); Tier 1) establish the baseline against which the winners' ~60%-past-one-year figures are extraordinary.

### Confidence & caveats
- **High confidence:** the *directional* claim that cycle/pregnancy > meditation > symptom/QS/disease-logging on retention, and the peer-reviewed dropout meta-analyses.
- **Medium confidence:** exact MAU/subscriber/retention decimals for Flo, Calm, Headspace — several authoritative pages (Business of Apps, Flo newsroom, Udonis) blocked direct fetch and are cited via search snippets; orders of magnitude are reliable, exact figures indicative.
- **Low confidence / unconfirmed:** Ovia DAU/MAU/retention (no reliable public figure found); Clue's 81%/72% are *company self-report* (Tier 3, FLAGGED).
- **US→EU flags:** Alchemer benchmarks, Sequoia/Udonis Headspace metrics, and several revenue figures are US-centric. Mitigant: ditto's three closest cycle-app comparables (Flo, Clue, Natural Cycles) are EU-rooted, strengthening transferability for the *winning* mechanism specifically.

---

## Sources

### Tier 1 — peer-reviewed / analyst / company-verified metrics
- [Eyal, N. *Hooked / "How to Manufacture Desire"* (Hook Model), 2014](https://www.nirandfar.com/how-to-manufacture-desire/)
- [JMIR — Rates of Attrition and Dropout in App-Based Interventions for Chronic Disease: Systematic Review & Meta-Analysis, 2020 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/)
- [JMIR — Challenges in Participant Engagement and Retention Using Mobile Health Apps: Literature Review, 2022](https://www.jmir.org/2022/4/e35120/)
- [JMIR — When and Why Adults Abandon Lifestyle Behavior and Mental Health Mobile Apps: Scoping Review, 2024](https://www.jmir.org/2024/1/e56897)
- [Diabetes Research and Clinical Practice — Dropout rate in clinical trials of smartphone apps for diabetes management: A meta-analysis, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0168822724006338)
- [FDA 510(k) K250561 — Natural Cycles, 2025](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250561.pdf)
- [Clue / helloclue — Clue Reaches 1 Million Paid Subscribers, 2025](https://helloclue.com/articles/about-clue/clue-reaches-1-million-paid-subscribers-cementing-position-as-leading-data-driven-women-s-health-intelligence-platform) (company-verified subscriber count; % stats are self-report → Tier 3)
- [General Atlantic — Flo Health $200M raise / unicorn, 2024](https://www.generalatlantic.com/media-article/flo-health-secures-more-than-200m-investment-from-general-atlantic-to-revolutionize-womens-health-first-purely-digital-consumer-womens-health-app-to-achieve-unicorn-status/)
- [Flo Health newsroom — MAU milestone, 2024](https://flo.health/newsroom/flo-reaches-22m-monthly-active-users) (company; exact figures snippet-sourced, page blocked direct fetch)
- [Sacra — Calm revenue / valuation / funding](https://sacra.com/c/calm/)

### Tier 2 — reputable press
- [Tech.eu — Natural Cycles raises $55M, 2024](https://tech.eu/2024/05/29/worlds-first-contraceptive-app-natural-cycles-raises-55m/)
- [Tech.eu — Clue cuts workforce 25%, 2023](https://tech.eu/2023/01/19/period-tracking-startup-clue-cuts-its-workforce-by-25-per-cent/)
- [Sequoia Capital — Measuring Product Health (Headspace DAU/MAU, retention-curve context)](https://articles.sequoiacap.com/measuring-product-health)
- [GetLatka — Calm revenue breakdown, 2024](https://getlatka.com/blog/calm-revenue)
- [Statista — Calm IAP revenues 2018–2024](https://www.statista.com/statistics/1243071/calm-iap-revenues-worldwide/)

### Tier 3 — blog / vendor / self-report (FLAGGED — corroborate before quoting)
- [Alchemer — Healthcare Apps 2022 Mobile Customer Engagement Benchmarks](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/) (vendor benchmark; US-centric)
- [Udonis — Headspace Revenue, Users & Downloads statistics](https://www.blog.udonis.co/statistics/headspace) (aggregator; snippet-sourced)
- [Sifars — Calm & Headspace monetization strategy, 2024](https://www.sifars.com/en/blog/calm-headspace-monetization-strategy-ai/) (blog; retention-tactic commentary)
- [EA Forum — Self-guided mental health apps aren't cost-effective… yet](https://forum.effectivealtruism.org/posts/2gB8mTyyKJw8PczYQ/self-guided-mental-health-apps-aren-t-cost-effective-yet) (analysis post)
- [Amplitude — The Hook Model](https://amplitude.com/blog/the-hook-model) (framework explainer)
- [Ovia Health (company site)](https://www.oviahealth.com/) (no public retention metrics)

*Access date for all URLs: 2026-06-10.*
