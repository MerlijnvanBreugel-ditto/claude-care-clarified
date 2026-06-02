# Growth Frameworks Research — Routing Ditto's Funnel Model

**Version:** 1.0
**Created:** 2026-04-21
**Status:** Research memo — informs v3+ of the funnel leverage model (last revised 2026-04-22)
**Sibling artifacts:** `v2-interactive.html`, `README.md`

## Why this memo exists

The v2 model works as a sensitivity narrative but is still a hand-rolled steady-state formula. Before we invest more engineering in it, we should position it against what practitioners and econometricians actually use. The question is not "is our model right?" but **"what class of model is this, what is the next class up, and when do we graduate?"**

This memo answers:
1. Where v2 sits on the growth-modeling maturity ladder
2. Which practitioner frameworks it inherits from and what they add
3. Which mathematical traditions we could borrow rigor from
4. Which tools exist for the next stages
5. How to link the model to experiments (the part we care about most)
6. A staged roadmap v2 → v6, with the "graduate when" triggers
7. A reading/listening list, ranked

Length: long on purpose. Skip to §6 for the roadmap if short on time.

---

## 1. The growth-modeling maturity ladder

Every team that builds a funnel model converges on one of these levels. The jump between levels is not about sophistication for its own sake — it's about which *decisions* the model can support.

| Level | What it is | Decisions it supports | Where v2 sits |
|---|---|---|---|
| **L0 — Flat funnel** | Static % through each step | "What step is worst?" | — |
| **L1 — Steady-state formula** | Funnel + retention lifetime + K-factor, single cohort | "Where does MAU leverage live at equilibrium?" | **v2 is here** |
| **L2 — Decomposed steady-state** | Multiple user segments, heterogeneous retention, multi-loop | "Which *kind* of user drives MAU, which loop moves which kind?" | v4 (blocked on Porygon segmentation data) |
| **L3 — Markov / cohort-transition model** | State machine with per-state transition probabilities, time-inhomogeneous | "What's the counterfactual if we lift a specific transition? What's the transient MAU path, not just steady state?" | **v3 (shipped, synthetic-calibrated)** |
| **L4 — Econometric (MMM / structural TS)** | Regression of observed MAU on spend/releases/seasonality, with priors | "How much MAU did *channel X* cause? Diminishing returns? Saturation?" | v5 |
| **L5 — Causal / experiment-bound** | Each parameter in the model is tied to an actual A/B test's estimated effect, with uncertainty | "How confident are we a given initiative moves MAU by Y?" | v6 (north star) |

**The key realization:** L1 is exactly the level where most PM-built funnel models live — and most of them are not built as deliberately as ours. Our actual strategic question ("where does leverage live and what should we build?") is well-served by L1–L2. Moving to L3+ is worthwhile only when we need *counterfactuals per initiative with uncertainty bands*. Today we don't. We will.

---

## 2. Practitioner frameworks — what each adds

### 2.1 AARRR (Dave McClure, 2007) — the funnel skeleton
**What it is:** Acquisition → Activation → Retention → Referral → Revenue.
**What it adds:** A shared vocabulary. Every funnel model is a refinement of AARRR.
**What our model inherits:** The five stages are all present (Inflow = Acquisition; P(reg) and P(act|reg) = Activation; r₁/r₂ = Retention; K = Referral; Revenue not modeled).
**Limit:** It's a funnel, not a loop. Doesn't handle compounding. Its own author has since said "growth is loops, not funnels." Which brings us to:

### 2.2 Growth Loops (Reforge — Brian Balfour, Kevin Kwok, Casey Winters, ~2018)
**What it is:** A system where each action generates more actions. Classes: acquisition loops (content, viral, paid), engagement loops (retention), monetization loops.
**What it adds:** Makes compounding explicit. The distinction between *inputs* (campaigns, features) and *loops* (self-sustaining systems) is the single most important framing move since AARRR.
**What our model inherits:** K is a loop. r₁/r₂ is a retention loop. `1/(1−K)` is literally the geometric series sum of loop compounding.
**Limit (today):** v2 models one loop (Care Circle). Ditto has at least four plausible loops: viral (Care Circle), content (shared summaries shown to non-users), partnership (Menzis referral chain), retention (summary generation begets next visit). **The largest gap in our model right now.**
**Where to go deeper:** Reforge "Growth Loops" essay (Kwok/Balfour, still the canonical explainer). Lenny × Casey Winters podcast episode on loops (2023).

### 2.3 Racecar Growth Model (Elena Verna, 2022)
**What it is:** Growth = Engine (loops that compound) + Turbo boosters (things that amplify the engine, e.g., paid) + Brake releases (things that remove friction). Plus "fuel" (product value) and a "driver" (team).
**What it adds:** A *causal hierarchy*. Turbo boosters without a working engine are wasted. Brake releases (activation fixes, onboarding, churn reduction) multiply whatever engine you have.
**What this tells us about our current priorities:**
- **Engine:** r₁/r₂ + K → weak today (K≈0.012, r₁=54% cliff). **Engine is our bottleneck.**
- **Turbo:** Inflow (insurer deals, paid, ASO) → linear lift, but linear ≠ waste.
- **Brake release:** P(reg), P(act|reg) → each point here multiplies everything downstream. This is why Activation sensitivity looks so large in our bars.
- **Practical implication:** The "where does leverage live?" answer from our v2 sensitivity bars is *already* a Racecar reading: brake releases (Activation, Registration) are currently our biggest near-term levers; the engine (loops + retention) is a longer play.
**Where to go deeper:** Elena Verna's Reforge course "Growth Series" (racecar is the core model). Lenny × Elena Verna episode (2024) "Why most growth models are wrong."

### 2.4 Four Fits (Brian Balfour, 2017)
**What it is:** Product–Market, Market–Channel, Channel–Model, Model–Product. All four must align or growth breaks.
**What it adds:** Explains *why* a working funnel can stall. If channel economics don't match monetization, the loop breaks at scale.
**Relevance to Ditto:** Menzis is a channel bet. B2B2C channel economics are fundamentally different from paid/organic. The model doesn't distinguish — and should, per-cohort, in v3+.
**Where to go deeper:** Reforge "Four Fits" essay. Balfour on Lenny's podcast (multiple episodes).

### 2.5 DHM Framework (Darius Contractor / Dan Hockenmaier, popularized by John Biddle at Grammarly, ~2020)
**What it is:** Delight × Hard to get elsewhere × Margin. A scoring lens for which feature to build for growth.
**What it adds:** A fast gut-check on *which* strategy bundle to prioritize once you know the leverage. Our initiative-presets tab is a DHM-compatible scoring surface — we just haven't coded D, H, M yet.
**Relevance:** Care Brain = very D, uncertain H (competitors will copy), high M (sticky). Menzis partnership = medium D, very H (we have exclusivity), medium M.
**Where to go deeper:** Biddle on Lenny's podcast "Inside Grammarly's growth."

### 2.6 Sean Ellis PMF score + retention curves
**What it is:** "How would you feel if you couldn't use this product?" >40% "very disappointed" = PMF. Combined with user-retention curves that *flatten* (not decay to zero).
**What it adds:** A test for whether the *product* is healthy before blaming the funnel. If the retention curve doesn't flatten, no amount of acquisition fixes growth.
**Relevance to Ditto:** Our r₁ = 54% cliff is the signal. The shape of the curve from M0→M1→M2→M12 for our "committed" cohort is the single most important diagnostic we're not yet visualizing. **Action: pull cohort retention by tenure bucket and plot flattening.** (Feeds v3 heterogeneous-retention model.)
**Where to go deeper:** Sean Ellis original post. Andrew Chen "The only metric that matters" (retention flattening).

### 2.7 Growth Accounting (Jonathan Hsu / Social Capital, ~2017)
**What it is:** Decomposes MAU growth into New + Resurrected + Retained − Churned. QGR (quick ratio) = (New + Resurrected) / Churned.
**What it adds:** Makes flow vs. stock explicit. Forces the question "are we growing because of new users or because old ones aren't leaving?" Answerable from our data today.
**Relevance:** A clean diagnostic overlay on the v3 trajectory. Mathematically simple; strategically revealing. Feeds into v4 alongside the retention-curve upgrade; Porygon CSV 2.1 captures exactly this decomposition.
**Where to go deeper:** Jonathan Hsu's original Medium series "Diligence at Social Capital." Reforge has internalized this under "engagement accounting."

---

## 3. Mathematical/econometric lineage

Where our hand-rolled formula connects to standardized, literature-backed methods.

### 3.1 Markov cohort models
**What it is:** Each user is in one of N states (new, active, dormant, churned, committed). Transitions happen each period with probabilities `P(i→j)`. MAU = sum of users in "active" states.
**Why it matters:** Our two-tier retention (r₁, r₂) is a *degenerate* Markov model with two states and hand-picked transition probabilities. A proper Markov model fits the transition matrix from cohort data and handles heterogeneity naturally.
**Payoff for v4:** Can answer "what if we lift registration→activation by 5pp" *including the transient effect on MAU* (not just steady state). We can run scenarios over 12 months, not just equilibrium.
**Implementation effort:** Medium. One analyst-week to fit the transition matrix from our Mixpanel cohort data; another week to build the simulator. The hard part is choosing states that are both observable and behaviorally meaningful.
**Literature:** Fader & Hardie "Customer-Base Analysis" (2009+). The Pareto/NBD and BG/NBD models are specific Markov specifications for CLV. Their Python package `lifetimes` fits them out of the box.

### 3.2 Survival analysis (Kaplan-Meier, Cox proportional hazards)
**What it is:** Probability of "surviving" (staying active) past time t. Handles censoring (users who haven't churned yet but might).
**Why it matters:** Our r₁/r₂ split is a crude two-step hazard. Real retention is a continuous hazard function. Kaplan-Meier curves would show us the *shape* of our retention — and flattening, per §2.6, is the thing we actually want to measure.
**Payoff:** A single chart per Life Moment segment telling us which segments reach the flat tail and at what tenure. Feeds directly into v3's committed-cohort slider.
**Implementation effort:** Low. `lifelines` Python package. One afternoon with a data scientist.
**Literature:** Lifelines docs are well-written. Cam Davidson-Pilon's book "Survival Analysis with Python" if going deep.

### 3.3 Renewal theory / Palm calculus
**What it is:** Mathematics of arrival/renewal processes. Our `L = 1 + r₁/(1−r₂)` is a *renewal reward* formula under a specific assumption (geometric tail).
**Why it matters:** Mostly theoretical, but it tells us *when our formula is wrong*: whenever the tail isn't geometric (i.e., whenever retention varies with tenure — which is always, in reality).
**Payoff:** Modest. Academic rigor for documentation; probably doesn't change decisions.
**Skip unless:** We write a whitepaper.

### 3.4 Marketing Mix Modeling (MMM)
**What it is:** Regression of observed MAU/sales on spend across channels, with adstock (carryover effects) and saturation (diminishing returns). Answers "if I spend €1 more on Meta, what's the MAU lift?"
**Why it matters:** The only way to honestly estimate channel contributions when Adjust attribution is 94% broken (per README). MMM sidesteps per-user tracking.
**Payoff for v5:** Replaces our hand-slider on Inflow with an estimated curve per channel including saturation. Turns "increase inflow by 1000" into "€X extra spend on Menzis co-marketing yields 1000 incremental installs with 60% confidence."
**Open-source tools:**
  - **Robyn** (Meta, 2021) — R-based, semi-automated, uses Prophet for trend + ridge regression + Nevergrad hyperparam optimization. Production-grade.
  - **LightweightMMM** (Google, 2022) — Python/JAX, Bayesian (NumPyro). Nicer uncertainty quantification, smaller sample tolerance.
  - **PyMC-Marketing** (PyMC Labs, 2023) — Python/PyMC, full Bayesian, actively developed.
**Implementation effort:** Medium-high. Needs weekly data on spend/installs/MAU for 18+ months (we have this in Mixpanel + finance). Two analyst-weeks to set up + ongoing maintenance.
**When to graduate:** When we're spending meaningfully on paid channels and can't attribute them. We're not there yet, but Menzis scale-up will get us there within 12 months.

### 3.5 Bayesian structural time series (BSTS / CausalImpact)
**What it is:** Model an MAU time series as level + trend + seasonality + regression on "release events." Ask "what would MAU have been without the Care Circle v2 launch?"
**Why it matters:** Post-hoc estimation of launch effects without needing a holdout group. Complementary to A/B testing — works when A/B isn't feasible (full rollouts, partnership launches).
**Payoff for v5:** Every shipped initiative gets a retrospective MAU lift estimate that we feed back into the model priors.
**Tooling:** Google's `CausalImpact` R package (also Python port). PyMC's `pymc-experimental` has a BSTS module.
**Literature:** Brodersen et al. 2015, "Inferring causal impact using Bayesian structural time-series models" — clear paper.

### 3.6 Uplift modeling
**What it is:** Instead of "who will convert?" (classification), "who will *convert because of the treatment*?" (causal ML). Splits users into persuadables, sure-things, lost-causes, sleeping-dogs.
**Why it matters:** When we run targeting experiments (e.g., which users should get a Care Circle invite nudge), uplift tells us who to target for maximum *incremental* effect.
**Payoff:** Operational, not modeling — optimizes *rollout* not *analysis*.
**Tooling:** `causalml` (Uber), `econml` (Microsoft).
**When to graduate:** After we have a steady A/B cadence and want to segment treatment effects. Probably 2027.

---

## 4. Tooling landscape

| Category | Tool | Use case for Ditto | Horizon |
|---|---|---|---|
| **Product analytics** | Mixpanel (have) | Raw cohort/funnel data; source-of-truth for retention curves | today |
| | Amplitude | Same; better growth accounting dashboards out of box; possible replacement | evaluate |
| **Experimentation** | Statsig / Eppo / GrowthBook | A/B test orchestration with sequential stats; feeds effect sizes into model priors | v5 |
| **MMM** | Robyn (Meta) | Channel attribution when tracking breaks | v5 |
| | LightweightMMM (Google) | Same; Bayesian; lower data need | v5 |
| | PyMC-Marketing | Full Bayesian; research-grade | v5+ |
| **Causal inference** | CausalImpact (Google) | Post-launch lift estimation | v5 |
| | causalml / econml | Uplift + treatment-effect heterogeneity | v6 |
| **Survival / cohort math** | lifelines (Python) | Retention-curve shape analysis | v3 |
| | lifetimes (Python) | CLV / Pareto-NBD for committed-cohort sizing | v3 |
| **Simulation / viz** | Observable / D3 | Interactive model (what v1/v2 are) | today–v4 |
| | Streamlit / Dash | If model graduates beyond browser | v4+ |
| **Sensitivity / optimization** | SALib (Python) | Sobol indices instead of our hand-rolled bars | v3 |

---

## 5. Experiment linkage — the high-leverage piece

**The gap:** Our v2 sliders are free-floating. A PM can drag "registration rate +5pp" without any link to whether a 5pp lift is actually achievable. The result: the model can justify anything.

**The fix (v5–v6):** Each slider's realistic range is set by observed effect sizes from actual experiments.

### Proposed pipeline
1. **Experiment tagger.** Every shipped A/B experiment gets tagged with the parameter(s) it moved (`regRate`, `actRate`, `r1`, `inviteRate`, etc.). Lightweight: one column in the Linear experiment ticket.
2. **Effect-size database.** A flat table: `experiment_id | param | observed_lift | ci_low | ci_high | sample_size | cohort`. Populated from Statsig/Mixpanel output.
3. **Slider bounds.** Each slider in the model shows, under its track, the realized range from historical experiments: "regRate: median observed lift +1.2pp, 90th percentile +3.1pp." The PM can still override but now knows when they're extrapolating.
4. **Initiative → effect mapping.** Each preset declares its parameter lifts with *uncertainty*, not point estimates. "Care Circle v2: inviteRate +5pp (95% CI: +1pp to +9pp)." The sensitivity bars become *distributions*, not single values.
5. **Backcasting.** Every quarter, overlay modeled MAU vs. observed MAU. Persistent gaps reveal model bugs or unmodeled loops.

### What this unlocks
- Every strategic debate (`"We should do Care Brain before Care Circle v2"`) is now a comparison of confidence-weighted expected MAU lift per engineering week. This is the A-purpose from the original brief (prioritization), finally rigorous.
- A/B tests become *model updates*, not isolated decisions. Compounds team learning over time.
- Claim: this is more valuable than any of the math upgrades in §3. **Experiment linkage is the single highest-leverage move we can make in the model's evolution.** (Internal consistency check: this contradicts "v5 = MMM" — resolved by treating v5 as "experiment linkage + MMM for the untracked channels," not MMM alone. Updated in §6.)

---

## 6. Roadmap v2 → v6 (revised 2026-04-22)

| Version | What changes | When to start | Effort | Graduates when |
|---|---|---|---|---|
| **v2 (retired as live)** | Three-cohort decomposition: activated flow + passive × multiplier + committed floor. Steady-state closed form only. Retained as A-B reference. | — | — | — |
| **v3 (shipped 2026-04-22): Discrete-time Markov cohort simulator** | Python model (`model/`). State vector `[s_0..s_11, s_loyal]`; three-tier retention (r₁, r₂, r_loyal); 24-month trajectory + asymptote; passive as multiplier; CSV calibration hooks for Porygon data. **Pulled forward from v4** because the inflow-drop artifact in v2 made every slider misleading. | — | 1 PM-week | Trajectory visible; the cliff artifact is gone |
| **v4: Fit retention + Life Moment split + passive as its own cohort** | Replace three-tier with per-tenure retention fit from Porygon 1.2 cohort matrix. Split passive into its own cohort curve from 2.2. Add Life Moment segmentation from 2.4. Add growth accounting decomposition (New/Resurrected/Retained/Churned) from 2.1 for back-check against observed flows. Optional: Sobol sensitivity via SALib. | When Porygon returns Tier 1 + 2 data | 2–3 analyst-weeks | Retention is per-tenure-month not three-tier; Life Moment cohorts visible |
| **v5: Experiment linkage + MMM for untracked inflow + uncertainty** | Sliders show realized-experiment ranges; presets carry CIs; MMM (Robyn or LightweightMMM) replaces hand-slider on Inflow with channel saturation curves. Monte Carlo uncertainty bands on trajectories. | When Menzis scaling produces attributable spend OR Adjust attribution is fixed | 4–6 weeks, needs DS hire or vendor | Paid channels >30% of inflow OR attribution fully breaks |
| **v6: Causal / counterfactual** | CausalImpact for post-launch lifts; uplift modeling for targeting. Every shipped initiative updates the model. | After v5 steady | Ongoing; needs DS capacity | North-star state |

**What happened to the original v3 scope.** v2 was a steady-state closed form — when we dropped Inflow 5,000 → 1,000 in the UI, the scenario number jumped 1,745 → 349 instantaneously. That's the correct asymptote but it misrepresents the transient, making every slider look catastrophic or heroic. We pulled the Markov cohort simulator forward from v4 to fix this specific artifact; the retention-curve-fitting, Life Moment segmentation, and growth-accounting pieces originally scoped for v3 moved into v4 because they need Porygon data that doesn't exist yet.

**The critical insight in this roadmap:** v3 is shipped and cheap — it's a correct structural model on synthetic-calibrated baseline. v4 is the *data upgrade* — it needs Porygon to fill CSV templates. v5 is the *strategic upgrade* — it links the model to experiments. v6 is the long game.

**Decision proposal:** Send `porygon-data-requests.md` to Porygon now. Plan v4 for Q3 2026 after Tier 1 data returns. v5 held back until Menzis scale-up forces the issue (probably Q4 2026 or Q1 2027).

---

## 7. Reading/listening list (ranked by ROI for this specific problem)

### Must-do (the 80/20 of the framework content)
1. **Lenny's Podcast — Casey Winters, "Growth loops"** (2023). 90 min. Covers why funnels ≠ loops and the loop taxonomy. Directly relevant to our §2.2 gap.
2. **Lenny's Podcast — Elena Verna, "Why most growth models are wrong"** (2024). ~100 min. Racecar model from the source.
3. **Reforge essay — "Growth Loops are the new Funnels"** (Kwok/Balfour). ~20 min read. Canonical loops framing.
4. **Jonathan Hsu — "Diligence at Social Capital" Medium series** (2017). ~90 min read. Growth accounting from first principles. **Do before v3.**
5. **Andrew Chen — "The only metric that matters for a new startup"** blog post. ~10 min. Retention curve flattening. Reinforces §2.6.

### Strongly recommended (second pass, before v4/v5)
6. **Lenny's Podcast — John Biddle, "Inside Grammarly's growth"** (2023). DHM framework applied.
7. **Lenny's Newsletter — "The definitive guide to growth models"** (2023 issue, search archive). Surveys racecar + loops + accounting.
8. **Fader & Hardie — "Customer-Base Analysis: An Overview"** (2009 paper, free online). Foundation of Markov/probabilistic CLV. ~40 min read. Do before v4.
9. **Brodersen et al. — "Inferring causal impact using Bayesian structural time-series models"** (2015). 20 min. Do before v5.
10. **Robyn documentation + tutorial** (Meta, facebookexperimental/Robyn on GitHub). ~2h to get through the basic tutorial.

### Nice-to-have (reference material, not sequential)
11. **Balfour — Four Fits series** (Reforge blog, 4 posts). Frames Menzis channel-fit question.
12. **Sebastian Deterding / Lenny on PMF definitions** (pod + newsletter).
13. **Cam Davidson-Pilon — "Survival Analysis with Python"** (free online book). Reference for v3.
14. **Sequoia — Growth stage memos** (periodically published). Calibrates what "good" looks like at our stage.
15. **Shishir Mehrotra — "The Rituals of Rituals" / growth at YouTube/Coda** (Lenny pod). Indirect but sharpens the team/process side of the Racecar "driver."

### Explicitly deprioritized
- Gartner, Forrester, McKinsey growth content — too generic.
- Academic MMM literature — Robyn/LightweightMMM docs cover the applied 80%.
- "Growth hacking" era content (pre-2017) — largely superseded.

---

## 8. Short answer to "what do we do next?"

1. **v3 is shipped.** Python cohort stock-and-flow simulator lives in `model/`. Fixes the inflow-drop artifact. Still uses synthetic initial state and a hypothesized `r_loyal = 0.91` — both swap-in-ready via `calibration.py` once Porygon responds.
2. **Send `porygon-data-requests.md` to Porygon now.** Tier 1 (stock by tenure, cohort retention matrix, loyal-tail retention) unblocks real v3 calibration. Tier 2 enables the v4 upgrade.
3. **Pull retention curves by Life Moment now** (independent of the model) — this is a diagnostic Ditto should have regardless.
3. **Start the experiment-effect-size database** as a one-column addition to Linear experiment tickets. Zero engineering cost, compounds monthly.
4. **Read items 1–5 from §7** before scoping v3.
5. **Revisit v5/MMM decision Q4 2026** — trigger is Menzis scale-up producing meaningful paid spend.

The v2 model is fit for its current purpose (sensitivity narrative). The biggest unlock is not in the math — it's in linking sliders to real experiment data so the model stops being a *what-if toy* and starts being a *what-will-happen forecaster with error bars*.
