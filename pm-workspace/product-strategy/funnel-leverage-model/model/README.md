# Funnel Leverage Model — Python

A cohort-based stock-and-flow simulator for Ditto Care's user funnel.

## Why this exists

The earlier HTML model (`v1`, `v2`) was a closed-form steady-state equation. It computed the long-run asymptote of MAU under a given set of parameter values. It did not model *time* — so dropping installs from 5,000 → 1,000 appeared to cause an instantaneous 80% MAU collapse. That's the mathematically correct asymptote, but it misrepresents reality: today's loyal users don't disappear, they decay on their own retention curves.

This Python model fixes that. It simulates the user base month by month. Today's stock (users by tenure) ages forward; new cohorts enter at the top. The model produces a **trajectory** over 24 months plus the long-run asymptote, so you can see both the short-term sensitivity and the long-run consequence of any scenario.

## The math in one paragraph

The activated user base is a vector of tenure buckets `[s_0, s_1, ..., s_11, s_loyal]` where `s_τ` is the number of users at tenure τ months since activation, and `s_loyal` absorbs everyone at 12+ months. Each month, the base ages: `s_{τ+1}^{new} = s_τ^{old} × r_τ` where `r_τ` is the per-tenure retention rate. The loyal bucket is self-looping with rate `r_loyal ≈ 91%` and absorbs the aging `s_11`. New activations enter `s_0`, computed as `Inflow × P(reg) × P(act|reg) × 1/(1−K)` where `K` is the Care Circle viral coefficient. Passive MAU (Care Circle viewers who never activated) is modeled as a multiplier on activated. Total MAU at month `t` = Σ activated + passive + committed floor.

This is a **discrete-time time-homogeneous Markov cohort model** — the simplest member of the family described in `../growth-frameworks-research.md` §3.1.

## What the model does and doesn't do

**Does:**
- Shows MAU trajectory over 24 months under any parameter scenario
- Compares named initiatives (Care Circle v2, Menzis push, etc.) by 12-month MAU lift
- Produces sensitivity rankings using 12-month effects (not asymptote effects, which are misleading)
- Loads real Porygon data when the CSVs in `../porygon-data-templates/` are filled — replaces synthetic initial stock and synthetic loyal retention with real fitted values
- Runs in <1 second; reproducible; unit-tested

**Doesn't:**
- Forecast a specific MAU number at a specific date (no seasonality or trend model yet)
- Split by Life Moment (needs Porygon 2.4 data)
- Model channels (Adjust attribution broken)
- Give uncertainty bands (single point estimate; add bootstrap in a later version)
- Link sliders to experiment effect sizes (that's the v5 upgrade per the research memo)

## How to run

```bash
cd pm-workspace/specs/funnel-leverage-model/model
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

This runs baseline + 4 stress tests + 6 initiative scenarios, prints summary tables, and saves charts to `outputs/`.

For a single quick test:

```bash
python -m pytest tests/
```

## Files

| File | What |
|---|---|
| `model.py` | Core: `Parameters`, `CohortSimulator`, simulation loop |
| `baseline.py` | Baseline values (Porygon 2026-04-21) and named initiative presets |
| `calibration.py` | Loaders for Porygon CSVs — swap in real data when filled |
| `plots.py` | Matplotlib helpers for trajectory charts and sensitivity bars |
| `main.py` | Driver: runs everything, prints tables, saves charts |
| `tests/test_model.py` | Sanity tests (baseline reaches equilibrium, asymptote matches closed-form, mass conservation) |

## Swapping in real data

1. Send `../porygon-data-requests.md` + templates to Porygon
2. Get back filled CSVs — drop them into `../porygon-data-templates/` (same filenames)
3. Re-run `python main.py` — `calibration.py` auto-detects filled cells and uses them instead of synthetic defaults
4. Check `outputs/baseline-trajectory.png` — should match today's observed MAU within 5%

## Scope for this version (v3)

Cohort-based discrete-time Markov model with three-tier retention (r₁ cliff, r₂ stable, r_loyal tail), passive multiplier, committed floor. No Life Moment segmentation yet, no continuous survival, no MMM.

Next version (v4): fit retention curves from Porygon data instead of using a three-tier approximation; Life Moment segmentation; growth-accounting overlay.

See `../growth-frameworks-research.md` §6 for the full roadmap.
