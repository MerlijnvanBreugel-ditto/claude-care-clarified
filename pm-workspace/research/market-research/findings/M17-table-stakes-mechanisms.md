# M17 — The 10 Table-Stakes, Highest-Impact UX/Engagement Mechanisms in Consumer Health (and the "Make It Better" Lens)

**Module:** M17 (Table-Stakes Mechanisms)
**Prepared for:** ditto.care — building from AI appointment summaries toward a daily "Living Health Companion"
**Author:** Product-strategy research analyst
**Date / access date:** 2026-06-14
**Lens:** Mark Pincus — *"take a PROVEN mechanic and make it BETTER."* For each mechanism we ask: is this an **adopt-as-is** table-stake (match the bar, don't reinvent) or an **innovate** mechanism where ditto's edges (LLM intelligence · voice navigation/processing · smart synthesis · curated-resource partnerships) can produce a *better* version?

> **Sourcing conventions.** Inline citations use `[Source, year](url)`. **T1** = peer-reviewed / analyst / company-verified; **T2** = reputable press; **T3** = blog / vendor / self-report (FLAGGED). Confidence tags (high/med/low). **US→EU flag** marks US-sample data that may not transfer to ditto's NL/EU context. Several facts are reused from the M7/M10/M11 corpus (already vetted); new datapoints added where the corpus was thin. Some journal/vendor pages (JMCP, Business of Apps, Flo newsroom) return HTTP 403 to direct fetch — figures from those are snippet-sourced and flagged; orders of magnitude are reliable, exact decimals indicative.

---

## Key takeaways

- **Retention in consumer health is a structural property, not a polish property.** The winning categories sit on a better behavioral substrate: a *daily-relevant, anticipatory question with a changing answer*, fed by *passive capture* and a *compounding personal-data moat*. ~71% of users abandon health apps within 90 days ([Alchemer, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/), T3); the exceptions (Flo ~60% MAU >1yr, Oura >80% yr-1 renewal, Whoop >50% daily at 18mo) all stack these mechanisms.
- **Adopt-as-is (5):** #2 Passive capture, #3 Streaks/identity, #4 Caregiver/social sharing, #6 Variable felt reward, #10 Voice/conversational. These are proven table-stakes where the bar is *execution*, not invention — match best-in-class and move on. ditto can differentiate at the margin (voice especially) but should not try to out-innovate the core pattern.
- **Innovate (5):** #1 Daily anticipatory answer, #5 Compounding data moat, #7 Proactive well-timed nudges, #8 Grounded-and-cited answers, #9 Human-in-the-loop / reimbursed scaffold. These are where ditto's LLM + synthesis + EU clinical-grounding edges can make the mechanism *better than anyone shipping today* — and collectively they are the moat.
- **The single highest-leverage innovate bet is #1 × #5 × #8 fused:** a daily, forward-looking, *cited* answer ("given your last visit and what's changed, here's what to watch/ask today") that gets smarter with every appointment. No incumbent owns patient-grade, grounded, cited, EU-available, *personalized-to-your-records* answers — that white space is the corpus's recurring finding ([M11](./M11-ai-frontdoor-deepdive.md)).
- **The biggest trap is the manual-logging tax + nagging-notification failure mode.** Symptom-tracker / disease-management apps churn (pooled dropout ~43%, [JMIR 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/), T1) precisely because they invert effort-vs-reward. ditto must design every loop on *already-consented data* (its summaries/EHR) and *contextual* nudges, not generic reminders.
- **EU/GDPR reframes two mechanisms.** Passive capture (#2) and social sharing (#4) are harder for ditto than for US peers — but ditto's natural moat (the user's own appointment summaries, consented) is itself a passive-capture and compounding-data asset, turning a constraint into an edge.
- **Human-in-the-loop (#9) is the retention scaffold that consumer-only apps lack and that ditto's clinical context uniquely affords** — the difference between a wellness toy and a reimbursed, trusted companion.

---

## The 10 mechanisms

### 1. Daily-relevant trigger with an anticipatory, changing answer (the cycle-tracker engine)

- **Definition.** A question the user *already re-asks* most days, whose answer the app uniquely holds and which *changes day to day* (forecast, "is this normal", "what changed"). The strongest internal trigger in consumer health.
- **Evidence it works.** Flo retains **~60% of MAU for >1 year** — roughly 2× the Health & Fitness norm — built on the daily "where am I in my cycle / am I fertile" question ([Flo Health, 2024](https://flo.health/newsroom/flo-reaches-22m-monthly-active-users), T1, med, snippet-sourced). Oura's daily "Readiness Score" anchors **>80% year-1 renewal** ([CNBC, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html); [Forerunner, 2025](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company), T1/T2, med). The inverse — apps with no daily-relevant trigger — show ~71% 90-day abandonment ([Alchemer, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/), T3).
- **Best-in-class exemplars.** Flo / Clue (cycle forecast), Oura / Whoop (daily readiness/recovery), Natural Cycles (daily fertility status).
- **Failure mode.** Static dashboards: if the answer doesn't change, the trigger decays to a push-notification nag. Appointment summaries alone are *episodic* — a one-time artifact, structurally the symptom-tracker failure mode at the visit level ([M7](./M7-consumer-health-retention.md)).
- **Verdict.** **Table-stakes** — every retained companion has one. But for a *clinical* companion it is unsolved.
- **ditto's edge — INNOVATE.** LLM synthesis can manufacture the changing daily answer from episodic clinical data: "given your last appointment and what's changed since, here's what to watch / do / ask today." This is the cycle-tracker engine translated to care — ditto's core innovate bet.

### 2. Passive / zero-effort capture (wearables, ambient, one-tap)

- **Definition.** The app acquires data without the user working for it — sensors, ambient capture, EHR ingestion, one-tap logging — removing the effort tax that kills logging apps.
- **Evidence it works.** Wearables that capture 24/7 passively post the category's best retention: Whoop **>50% of members use daily at 18 months, record-low churn** ([M10](./M10-consumer-app-deepdives.md); [ringingthebell, 2025](https://ringingthebell.substack.com/p/whoop-vs-oura-the-10-billion-question), T3, med); Oura **>80% yr-1 renewal** on passive sleep/readiness capture ([CNBC, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html), T2). Contrast: manual-logging disease apps show **pooled dropout ~43%** ([JMIR 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/), T1, high) — the effort tax made visible.
- **Best-in-class exemplars.** Oura, Whoop (sensor); Apple Health / Samsung Health (ambient aggregation); Finch (one-tap mood); MyFitnessPal (barcode/database to cut logging effort).
- **Failure mode.** The manual-logging tax — food/symptom/glucose diaries demand effort *today* for deferred/abstract payoff; users quit when the tax exceeds felt benefit. Also over-capture without insight (Fitbit: device without an interpreted loop erodes).
- **Verdict.** **Table-stakes** — zero-effort input is now expected.
- **ditto's edge — ADOPT AS-IS (with an EU twist).** ditto won't out-build wearables, but its *appointment summaries are themselves a passive-capture asset*: clinical data the user already consented to, ingested with zero logging effort. EU/GDPR makes wearable passive capture harder; ditto's consented-summary capture sidesteps that. Match the bar; don't reinvent.

### 3. Streaks / gamified investment / identity

- **Definition.** Visible, accumulating commitment (streaks, evolving avatar, levels) that converts use into identity ("I'm someone who…") and creates loss-aversion to breaking the chain.
- **Evidence it works.** Duolingo: **over 5M users hold streaks of a year or longer**; **>half of daily learners now have a 7+ day streak (2× the prior year)**; reaching a **10-day streak substantially reduces drop-off**, and **Streak Freeze lifts long-term retention ~10%** — credited with driving **>50M DAU** ([Lenny's Newsletter, 2022](https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth), T2, high; [SQ Magazine, 2026](https://sqmagazine.co.uk/duolingo-statistics/), T3, med). In health, Finch (gamified self-care pet) hits **54% D1 / 37% D7 — on par with Duolingo's ~51%/35%** ([Deconstructor of Fun, 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl), T3, med).
- **Best-in-class exemplars.** Duolingo (streaks), Finch (evolving pet = compounding investment), Calm/Headspace (meditation streaks), Strava (segment achievements).
- **Failure mode.** Streak anxiety / hollow gamification: a broken streak triggers *quitting* (loss aversion backfires); badges with no intrinsic meaning feel manipulative, and in a *health* context can reinforce a "sick person" identity (disease-management apps suffer this). Streak Freeze exists precisely to defuse the backfire.
- **Verdict.** **Table-stakes**, but must be applied gently in a clinical context.
- **ditto's edge — ADOPT AS-IS.** Borrow proven mechanics (gentle streaks, "you've stayed on top of your health N weeks", identity framed as *agency* not illness). This is execution, not invention — adopt Duolingo/Finch patterns, frame around health-ownership identity.

### 4. Social + caregiver sharing / network effects (the "keep loved ones updated" job)

- **Definition.** Sharing status/updates with partners, family, or caregivers — offloading the "is this normal / let me keep my loved ones informed" job and creating network-effect stickiness.
- **Evidence it works.** Strava's social graph (**180M registered, ~76M customers**; kudos/segments) is "the hardest moat to copy" and drives retention via accountability ([M10](./M10-consumer-app-deepdives.md); [Business of Apps, 2026](https://www.businessofapps.com/data/strava-statistics/), T3). In caregiving, apps that enable effortless health-update sharing measurably increase caregiver engagement in health discussions and decision-making ([PMC scoping review, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829719/), T1, med); CarePredict alerts families to anomalies (missed meal, fall) with zero action from the loved one ([CareYaya, 2026](https://www.careyaya.org/resources/blog/ai-for-caregivers), T3). Cycle/TTC apps' partner-sharing is a named retention lever ([M7](./M7-consumer-health-retention.md)).
- **Best-in-class exemplars.** Strava (network), Flo/Natural Cycles (partner sharing), CarePredict / Connected Caregiver (family updates), Cleo/Maven (care-team + family in benefits context).
- **Failure mode.** Privacy backlash and unwanted exposure — health data is far more sensitive than workout data; forced or leaky sharing destroys trust, especially under GDPR. Network features that require *both* sides to adopt can stall (cold-start).
- **Verdict.** **Table-stakes** for a companion serving chronic/elderly patients (the caregiver job is real and underserved).
- **ditto's edge — ADOPT AS-IS.** Implement consented, granular caregiver sharing of summaries/plans ("share this visit summary with my daughter"). The mechanic is proven; ditto should execute it well with GDPR-grade consent, not innovate the pattern itself.

### 5. Compounding personal-data moat (longitudinal, self-improving)

- **Definition.** Each use *visibly* makes tomorrow's answer more personalized/accurate, accumulating a longitudinal record that is a switching cost (leaving = losing your history) and a personalization flywheel.
- **Evidence it works.** Cycle apps' core moat — each logged cycle improves prediction; Natural Cycles' daily temperature history *is* the regulated contraceptive product (FDA-cleared, [M7](./M7-consumer-health-retention.md)). Whoop/Oura's "data flywheel" + subscription switching cost underpins their retention and **$10.1B / $11B valuations** ([M9](./M9-funding-recency-leaderboards.md); [Yahoo Finance, 2025](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html), T2). The losers' defining failure: data that is *never reflected back* as improving personalization, so no switching cost forms ([M7](./M7-consumer-health-retention.md)).
- **Best-in-class exemplars.** Flo / Natural Cycles (cycle history), Oura / Whoop (longitudinal baseline), Function Health (longitudinal labs, **$2.5B val**), Perplexity Health (EHR+labs+wearables via b.well).
- **Failure mode.** A "data graveyard" — accumulating data the user never sees reflected back; or a moat the user can't *feel* (no "based on your last 3 visits…" surfacing), so it provides no perceived switching cost.
- **Verdict.** **Differentiator** — the deepest moat, and the hardest to build.
- **ditto's edge — INNOVATE.** ditto's longitudinal record of *clinical encounters* is a richer, higher-stakes compounding asset than steps or sleep. LLM synthesis can reflect the moat back ("across your last 3 visits, your blood pressure plan changed twice — here's the trend"). This is a core innovate bet, tightly coupled to #1.

### 6. Variable + immediate felt reward

- **Definition.** An immediate, affectively-felt payoff on each use whose magnitude/content *varies* (anticipation), per the Hook Model's variable-reward phase.
- **Evidence it works.** Meditation apps retain on *immediate felt reward* (calm now) + content novelty: Calm reached **~$2B valuation, ~$596M peak revenue** on the in-session payoff ([Sacra](https://sacra.com/c/calm/), T1/2). Oura/Whoop's daily score is a variable reward (you don't know today's number until you check) — driving daily opens. The Hook Model identifies variable reward as the loop-sustaining element; apps whose output is *predictable* (yesterday's identical chart) churn ([Eyal, 2014](https://www.nirandfar.com/how-to-manufacture-desire/), T1 framework; [M7](./M7-consumer-health-retention.md)).
- **Best-in-class exemplars.** Calm/Headspace (felt calm + fresh content), Oura/Whoop (variable daily score), Finch ("Good Vibes" + pet rewards), Duolingo (XP, surprise chests).
- **Failure mode.** Reward that is replaceable (any calming content works → no moat → Calm/Headspace subscriber erosion) or absent/deferred (logging apps: a chart is not a felt reward). Over-engineered variable reward can also feel like a slot machine (manipulative).
- **Verdict.** **Table-stakes** — but pure content-reward without compounding value plateaus (meditation's lesson).
- **ditto's edge — ADOPT AS-IS.** Deliver an immediate felt reward of *reassurance/clarity* ("your results are normal — here's what they mean"), which is the affective payoff patients crave. Proven mechanic; ditto executes it via synthesis quality rather than inventing a new reward type.

### 7. Proactive, well-timed nudges & reminders (contextual, not nagging)

- **Definition.** Anticipatory, context-aware prompts (medication, follow-up, refill, "ask this at your next visit") timed to the moment of need — not generic, scheduled nags.
- **Evidence it works.** Meta-analysis of **29 studies / 2,684 participants** found mobile apps improved medication adherence with **OR = 2.34 (SMD ≈ 0.39)** ([J Med Syst, 2024](https://link.springer.com/article/10.1007/s10916-024-02135-2); [PubMed 39821698](https://pubmed.ncbi.nlm.nih.gov/39821698/), T1, high); an earlier review of 9 RCTs found **OR = 2.12 (95% CI 1.64–2.75)** for self-reported adherence ([JMCP, 2020](https://www.jmcp.org/doi/10.18553/jmcp.2020.26.4.550), T1, med — note self-report bias, 403 to direct fetch, snippet-sourced). A 2026 systematic review confirms medication-reminder tech benefits home-dwelling older adults ([Age and Ageing, 2026](https://academic.oup.com/ageing/article/55/2/afag007/8464951), T1, med).
- **Best-in-class exemplars.** Medisafe (medication reminders), Apple Health follow-up prompts, Oura/Whoop contextual coaching ("you're under-recovered — consider a lighter day"), Flo (fertile-window alerts).
- **Failure mode.** **Notification fatigue / nagging** — generic, mistimed, or too-frequent reminders are the #1 way this backfires; users mute, then churn. Reminders tied to *extrinsic* prescription (vs. internal need) decay fastest ([M7](./M7-consumer-health-retention.md)).
- **Verdict.** **Table-stakes for adherence, differentiator when truly contextual.**
- **ditto's edge — INNOVATE.** LLM context (your summary, meds, upcoming appointments) lets ditto fire *the right nudge at the right moment* ("your repeat prescription runs out Friday — want me to flag a refill?") rather than a dumb daily alarm. Contextual intelligence is exactly where generic reminder apps fail and ditto can win.

### 8. Grounded & cited, trustworthy answers (refuse-when-unsure)

- **Definition.** Answers backed by named, authoritative sources, with honest uncertainty / "see a clinician" guidance — earning trust by being verifiable and refusing to fabricate.
- **Evidence it works.** OpenEvidence — grounded in NEJM/JAMA-licensed literature with citations — reached **~40% of US physicians and a $12B valuation** (Series D, [BusinessWire, Jan 2026](https://www.businesswire.com/news/home/20260121029132/en/), T1, high), proving demand for *cited* clinical answers. The need is acute: **5–13% of unguarded LLM answers to patient questions were "unsafe"** ([npj Digital Medicine, 2026](https://www.nature.com/), T1, high), and in Google AI Overview health citations **YouTube was the most-cited domain (~4.4%) vs ~0.48% peer-reviewed journals** ([M11](./M11-ai-frontdoor-deepdive.md), T3, low — vendor data). Patient-grade grounded-and-cited is a **white space** — best engines today are clinician-only ([M11](./M11-ai-frontdoor-deepdive.md)).
- **Best-in-class exemplars.** OpenEvidence (clinician-only, gold standard for citation), Perplexity Health (cited, EHR-personalized, general-consumer), UpToDate (clinician reference).
- **Failure mode.** **Sycophancy & hallucination** — confidently wrong, uncited, or agreeing with the user's mistaken premise; in health this is a safety event, not a UX glitch. Over-refusal (declining everything) is the opposite failure that kills usefulness.
- **Verdict.** **Differentiator** — no one owns patient-grade, grounded, cited, EU-available answers.
- **ditto's edge — INNOVATE.** This is ditto's defining bet: LLM intelligence + curated-resource partnerships (clinical guidelines, EU sources) + refuse-when-unsure, *personalized to the user's own records*. Combine with #1 and #5 and it is the moat ([M11](./M11-ai-frontdoor-deepdive.md)).

### 9. Human-in-the-loop / clinical embedding / reimbursed outcome (the retention scaffold)

- **Definition.** A human/clinical anchor — escalation to a clinician, embedding in a care pathway, or a reimbursed outcome — that gives the product clinical legitimacy and a recurring, funded reason to exist.
- **Evidence it works.** Wearables prove the *subscription-as-scaffold* point (Whoop's subscription-only model = switching cost + recurring relationship that is "part of the moat", [M10](./M10-consumer-app-deepdives.md)). On the clinical side, GPT-4 *alone* scored ~92% on diagnostic reasoning but **giving physicians the tool didn't reliably improve them** (Goh et al., *JAMA Network Open* 2024 / *Nature Medicine* RCT, [M11](./M11-ai-frontdoor-deepdive.md), T1, high) — i.e., the *human-in-the-loop design* matters more than raw model accuracy. Reimbursed digital therapeutics and payer/employer distribution (Ovia, Cleo, Maven) retain via the funded-pathway scaffold ([M7](./M7-consumer-health-retention.md), [M10](./M10-consumer-app-deepdives.md)).
- **Best-in-class exemplars.** K Health (AI intake → clinician), Maven/Cleo (care-team embedded benefit), Natural Cycles (FDA-cleared regulated outcome), Ovia (payer/employer-distributed).
- **Failure mode.** Pure consumer-only apps lack this scaffold and inherit the churn curve; conversely, *over-medicalizing* (heavy clinician gating) kills the consumer self-serve loop and adds cost. Regulatory/reimbursement complexity can stall the product.
- **Verdict.** **Differentiator and retention scaffold** — the line between wellness toy and trusted, funded companion.
- **ditto's edge — INNOVATE.** ditto is *born* in the clinical encounter (appointment summaries), so human-in-the-loop and care-pathway embedding are native, not bolted-on. Curated-resource + provider partnerships and an EU reimbursement path turn this into a durable scaffold consumer-only peers can't replicate.

### 10. Conversational / voice-based interface (low-friction input + accessibility)

- **Definition.** Natural-language voice/chat as the primary I/O — lowering input friction and dramatically widening accessibility (low vision, low dexterity, low digital literacy, older adults).
- **Evidence it works.** Conversational speech input is **up to 3× faster than keyboard with a ~20.4% lower error rate**, with the efficiency gain *largest among older adults* ([arXiv 2111.03756, 2021](https://arxiv.org/pdf/2111.03756); [PMC7783870, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7783870/), T1, med). Voice is "a natural choice for eye-free, hands-free interaction" for users with visual/mobility impairments ([SAGE, 2020](https://journals.sagepub.com/doi/full/10.1177/2333721420985975), T1). OpenAI's Dec 2025 survey: **3 in 5 US adults** used AI for a health question in the prior 3 months — much of it conversational ([M11](./M11-ai-frontdoor-deepdive.md), T1).
- **Best-in-class exemplars.** ChatGPT/Perplexity voice (conversational health Q&A), ElliQ (voice companion for older adults), Hello Alpha / Ada (conversational intake), Amazon Alexa health skills.
- **Failure mode.** Conversational errors → anxiety and abandonment (older adults take longer to phrase queries, hit higher error rates); privacy fears about always-listening; voice misrecognition in clinical terms is a safety risk ([arXiv 2111.03756](https://arxiv.org/pdf/2111.03756); [Frontiers Psychol, 2025](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1618689/full), T1, med).
- **Verdict.** **Table-stakes for accessibility**, increasingly a baseline expectation as AI-native UX normalizes.
- **ditto's edge — ADOPT AS-IS, but a genuine strength.** Voice navigation/processing is one of ditto's stated edges. The *mechanic* (voice I/O) is proven and should be adopted to best-in-class standard; ditto's differentiation comes from coupling it with grounded synthesis (#8) so the voice answer is *trustworthy*, not just convenient — closer to "adopt-as-is on the interface, innovate on what it says."

---

## Summary table — adopt-as-is vs innovate

| # | Mechanism | Hard datapoint | Verdict | ditto: adopt / innovate |
|---|---|---|---|---|
| 1 | Daily anticipatory changing answer | Flo ~60% MAU >1yr | Table-stakes | **INNOVATE** (LLM synthesis from clinical data) |
| 2 | Passive / zero-effort capture | Whoop >50% daily @18mo | Table-stakes | Adopt-as-is (summaries = consented passive capture) |
| 3 | Streaks / gamified identity | Duolingo: 5M+ year-streaks; Freeze +10% retention | Table-stakes | Adopt-as-is (gentle, agency-framed) |
| 4 | Social / caregiver sharing | Strava ~76M customers; caregiver-app engagement ↑ | Table-stakes | Adopt-as-is (GDPR-grade consented sharing) |
| 5 | Compounding personal-data moat | Oura >80% yr-1 renewal | Differentiator | **INNOVATE** (longitudinal clinical record) |
| 6 | Variable + immediate felt reward | Calm ~$2B on felt reward | Table-stakes | Adopt-as-is (reassurance/clarity payoff) |
| 7 | Proactive, well-timed nudges | Med-adherence OR 2.34 (29 studies) | Table-stakes→diff | **INNOVATE** (contextual, not scheduled) |
| 8 | Grounded & cited answers | OpenEvidence ~40% US MDs, $12B | Differentiator | **INNOVATE** (patient-grade, EU, personalized) |
| 9 | Human-in-loop / reimbursed scaffold | GPT-4 92% solo but didn't lift MDs → design matters | Differentiator | **INNOVATE** (born in the clinical encounter) |
| 10 | Conversational / voice | Voice 3× faster, 20.4% fewer errors | Table-stakes | Adopt-as-is (innovate on *what it says*) |

**One-line rule:** Adopt-as-is the *engagement plumbing* (2, 3, 4, 6, 10) to best-in-class standard; **innovate the intelligence layer** (1, 5, 7, 8, 9) where ditto's LLM + synthesis + EU clinical-grounding + partnerships make a *better* mechanism — and where the moat actually lives.

---

## Sources

### Reused from vetted ditto corpus (M7 / M10 / M11 / M9)
- [M7 — Consumer-Health Retention teardown](./M7-consumer-health-retention.md) (Flo ~60% MAU>1yr; ~71% 90-day abandonment; JMIR dropout meta-analyses; Hook Model)
- [M10 — Consumer-App Deep-dives](./M10-consumer-app-deepdives.md) (Whoop >50% daily@18mo; Oura >80% renewal; Finch 54%/37%; Strava 76M; Calm)
- [M11 — AI Front-door Deep-dive](./M11-ai-frontdoor-deepdive.md) (OpenEvidence ~40% US MDs/$12B; GPT-4 92% diagnostic; 5–13% unsafe answers; patient-grade cited white space; OpenAI 3-in-5 survey)
- [M9 — Funding Recency Leaderboards](./M9-funding-recency-leaderboards.md) (Oura $11B; Whoop $10.1B; Function Health $2.5B)

### T1 — peer-reviewed / analyst / company-verified
- [J Med Syst — Effectiveness of Mobile Health Intervention in Medication Adherence: meta-analysis (OR 2.34), 2024](https://link.springer.com/article/10.1007/s10916-024-02135-2) · [PubMed 39821698](https://pubmed.ncbi.nlm.nih.gov/39821698/)
- [JMCP — Effectiveness of Mobile Apps on Medication Adherence (OR 2.12), 2020](https://www.jmcp.org/doi/10.18553/jmcp.2020.26.4.550) (403 direct fetch; snippet-sourced)
- [Age and Ageing — Medication reminder technologies for home-dwelling older adults: systematic review, 2026](https://academic.oup.com/ageing/article/55/2/afag007/8464951)
- [PMC — Mobile phone apps for family caregivers: scoping review, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829719/)
- [arXiv 2111.03756 — Barriers & design opportunities: voice assistants for older adults' healthcare/QOL, 2021](https://arxiv.org/pdf/2111.03756) (voice 3× faster, 20.4% fewer errors)
- [PMC7783870 — Voice assistants & consumer health access among low-income older adults, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7783870/) · [SAGE version](https://journals.sagepub.com/doi/full/10.1177/2333721420985975)
- [Frontiers in Psychology — Older adults' adoption of AI voice assistants (UTAUT), 2025](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1618689/full)
- [JMIR — Attrition/dropout in app-based chronic-disease interventions (~43%), 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/)
- [Eyal, *Hooked* / Hook Model, 2014](https://www.nirandfar.com/how-to-manufacture-desire/)
- [BusinessWire — OpenEvidence $250M Series D at $12B, Jan 2026](https://www.businesswire.com/news/home/20260121029132/en/)
- [CNBC — Oura $11B valuation / renewal, 2025](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [Sacra — Calm](https://sacra.com/c/calm/)

### T2 — reputable press
- [Lenny's Newsletter — How Duolingo reignited user growth (streak mechanics), 2022](https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth)
- [Yahoo Finance — Whoop $575M / $10.1B, 2025](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html)
- [Forerunner Ventures — Oura $11B & renewal stat, 2025](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company)

### T3 — blog / vendor / self-report (FLAGGED)
- [SQ Magazine — Duolingo statistics 2026](https://sqmagazine.co.uk/duolingo-statistics/) (5M+ year-streaks; Freeze +10%; 7-day streak share)
- [Business of Apps — Strava statistics, 2026](https://www.businessofapps.com/data/strava-statistics/)
- [Deconstructor of Fun — Finch retention, 2024](https://www.deconstructoroffun.com/blog/x0hd2ssr80y5n7gv0w967pg7hwd7tl)
- [ringingthebell — Whoop vs Oura daily-use stat, 2025](https://ringingthebell.substack.com/p/whoop-vs-oura-the-10-billion-question)
- [Alchemer — Healthcare apps 90-day benchmarks, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/) (US-centric)
- [CareYaya — AI for Caregivers guide (CarePredict), 2026](https://www.careyaya.org/resources/blog/ai-for-caregivers)

*Access date for all URLs: 2026-06-14. US→EU flags apply to Alchemer, Duolingo, Whoop/Oura, OpenAI-survey, and US voice-assistant samples; ditto's closest cycle-app comparables (Flo, Clue, Natural Cycles) and Oura are EU-rooted, improving transferability for the core retention mechanisms.*
