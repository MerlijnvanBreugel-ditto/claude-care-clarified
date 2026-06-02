# Funnel Leverage Model — Ditto Care

**Current version:** v3 (Python cohort stock-and-flow) — see `model/`
**Updated:** 2026-04-22
**Status:** Calibrated prototype — sensitivity & prioritization tool. Not a forecaster.

## What this is

A calibrated mathematical model of Ditto Care's user funnel. Used for:

1. **Primary:** sensitivity narrative — "where does MAU leverage actually live?"
2. **Secondary:** initiative prioritization — comparing named bundles of parameter changes by 12-month MAU lift.
3. **New in v3:** trajectory over time — "how long until this MAU lift shows up?" — so sliders no longer produce misleading instantaneous cliffs.

Not for forecasting a specific future MAU number. See `growth-frameworks-research.md` for how and when to graduate to a forecasting model.

## Why v3 exists

v2's formula `MAU = 1 / (1 − K) × (1 + r₁ / (1 − r₂))` is the **long-run asymptote** — the MAU the system would reach after infinite time at the current parameters. When Monthly installs were dropped from 5,000 → 1,000 in the UI, the scenario number jumped 1,745 → 349 (−80%) instantly. That's the correct asymptote, but it misrepresents reality: today's activated users don't disappear overnight, they age on their own retention curves.

v3 replaces the closed-form steady-state with a **discrete-time Markov cohort simulator**. Today's activated stock is a vector of tenure buckets `[s_0, s_1, …, s_11, s_loyal]`. Each month, buckets age forward (multiplied by per-tenure retention); new cohorts enter at `s_0`. The model produces a 24-month trajectory plus the asymptote, so both the short-run sensitivity and the long-run consequence of any scenario are visible.

## Files

| File | What |
|---|---|
| `model/` | **Current model (v3).** Python cohort stock-and-flow simulator. See `model/README.md`. |
| `porygon-data-requests.md` | Data request for Porygon — the inputs needed to swap synthetic initial state + retention for real fitted values. |
| `porygon-data-templates/` | CSV templates Porygon fills in. Auto-detected by `model/calibration.py`. |
| `v2-interactive.html` | Previous version — steady-state HTML. Kept for A-B compare. Its number is v3's *asymptote*. |
| `v1-interactive.html` | Original single-cohort HTML. Reference only. |
| `growth-frameworks-research.md` | Research memo: growth modeling frameworks, econometric lineage, tooling landscape, v4–v6 roadmap. Read before extending the model. |
| `README.md` | This file. |

## The v3 math

```
State vector:  s = [s_0, s_1, …, s_11, s_loyal]    (activated users by tenure in months)

Per-month step:
  s_new[τ+1] = s_old[τ] × r[τ]                     for τ in 0..10
  s_new[loyal] = s_old[11] × r[11] + s_old[loyal] × r_loyal
  s_new[0]   = C_t                                 (fresh cohort enters)

Retention vector (three-tier):
  r[0]      = r₁ ≈ 0.54     (activation → M1 cliff)
  r[1..11]  = r₂ ≈ 0.66     (stable core)
  r_loyal   ≈ 0.91          (12+ month self-loop — hypothesis, needs Porygon 1.3)

Fresh cohort:
  C_t = Inflow × P(reg) × P(act|reg) / (1 − K)
  K   = invite_rate × invites_per_inviter × P(invite→install) × P(invited→activate)

MAU:
  MAU_activated(t) = Σ_τ s_τ(t)
  MAU_passive(t)   = passive_multiplier × MAU_activated(t)      (v4 will split this)
  MAU_total(t)     = MAU_activated + MAU_passive + committed_floor

  Asymptote ≡ MAU_total at the fixed point of the step recursion.
```

The long-run asymptote collapses to v2's closed form when `r_loyal == r₂`. So v2 isn't wrong — it's just the `t → ∞` slice of v3.

## Baseline values (Porygon snapshot, 2026-04-21)

Unchanged from v2 except the new `r_loyal` parameter. See `model/baseline.py` for the live values.

| Parameter | Value | Source |
|---|---|---|
| Monthly installs | 5,000 | Normalized, blended iOS+Android+iPadOS |
| Install → Registration (7d) | 35% | Apr 1–10 cleanest window |
| Registration → Activation (14d) | 28% | Combined: manual appt OR recording OR doc scan |
| r₁ (M0→M1) | 54% | summary_created cohort retention |
| r₂ (M1→M12) | 66% | Derived: 33% M2 absolute ÷ 54% M1 |
| **r_loyal (M12+)** | **91%** | **Hypothesis. Validated by Porygon 1.3.** |
| Invite rate (30d) | 24% | Of newly activated users |
| Invites per inviter | 1.48 | Avg |
| Invite → Install | 15% | Untracked — slider estimate |
| Invited → Activation | 22% | ~2× native, from follower-accept data |
| passiveMultiplier | 0.36 | Observed 447 non-activated ÷ 1,230 activated |
| committedFloor | 0 | User-belief slider |

**Synthetic initial state.** v3 primes the simulation from the analytical steady state unless Porygon 1.1 (stock by tenure) is filled — in which case `calibration.py` swaps in real numbers.

## How to run

```bash
cd pm-workspace/specs/funnel-leverage-model/model
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py                  # runs baseline + stress tests + initiatives + sensitivity; saves charts to outputs/
python -m pytest tests/         # sanity tests (8 passing)
```

See `model/README.md` for the full per-file layout.

## Key insights (v3)

1. **Ditto's activated base is inflow-heavy in the short run.** At current baseline, the s_0 bucket (users who activated this month) is ~38% of activated MAU. That's why dropping Inflow 5k → 1k still produces a meaningful M1 hit (~30%), just not v2's 80% cliff. By M12 we're near the new asymptote.
2. **Retention has the biggest compounding leverage.** +10% on `r₂` lifts 12-month MAU by ~15%; +10% on any funnel-conversion knob lifts it by ~10%. The gap widens at 24m+. This matters because most "growth" initiatives aim at conversion, but retention protects every dollar of acquisition.
3. **The Care Circle loop is mathematically tiny at current K ≈ 0.012.** Even doubling invite rate lifts MAU by ~1%. Lifting `invite → install` (currently 15%) is where the leakage is — but we're blind to it because it's untracked (Porygon 3.1 request).
4. **Loyal tail matters asymmetrically.** At r_loyal = 0.91, the loyal bucket is ~2% of MAU today — small. But it's what prevents catastrophic stock collapse in transient scenarios. If Porygon 1.3 returns r_loyal < 0.85, the stock-persistence argument weakens significantly.
5. **Passive viewers aren't free.** They're modeled as a multiplier (0.36× activated) — so they track activated's trajectory. If passive really does retain independently (Porygon 2.2 data), this is under-modeling the near-term MAU and over-modeling the scenario response.

## Known limitations (v3)

- **Passive is a multiplier, not its own cohort.** Decays in lockstep with activated; loses its own retention dynamics. Fix: v4 when 2.2 data lands.
- **No Life Moment segmentation.** Single blended funnel. v4 with Porygon 2.4.
- **Three-tier retention, not continuous hazard.** Good enough to fix the v2 artifact; loses tenure-level detail. v4 when 1.2 cohort matrix lands.
- **No channel split.** Adjust attribution ~94% broken. v5 needs MMM.
- **No uncertainty bands.** Single point estimates. v5+.
- **Viral loop latency assumed zero.** Invites convert instantly in the model. Real latency data in 3.1.
- **Slider bounds are user belief.** Not yet tied to historical experiment effect sizes. v5/v6.

## Planned next versions

See `growth-frameworks-research.md` §6 for the full roadmap.

| v | What changes | Effort | Gated on |
|---|---|---|---|
| **v4** | Fit retention from Porygon 1.2 (replace three-tier with per-tenure curve); split passive into its own cohort (Porygon 2.2); Life Moment segmentation (Porygon 2.4) | 2 analyst-weeks | Porygon data delivery |
| v5 | Experiment-linked slider bounds; MMM (Robyn / LightweightMMM) for channel attribution; Monte Carlo uncertainty bands | 4–6 weeks, needs DS | Adjust attribution fix + experiment log |
| v6 | Causal / counterfactual — CausalImpact for launches, uplift modeling for targeting | Ongoing | v5 in place |

## Related artifacts

- `growth-frameworks-research.md` — frameworks, math lineage, tooling, roadmap
- `pm-workspace/specs/ideas/activation-and-audience/` — activation strategy work feeding parameter estimates
- `pm-workspace/specs/ideas/care-circle-v2/` — initiative already modeled as a preset
- `pm-workspace/specs/ideas/onboarding-to-aha.md` — onboarding redesign preset
- `pm-workspace/specs/care-brain/` — Journey Page initiative preset
