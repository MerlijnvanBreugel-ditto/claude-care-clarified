"""Driver: run baseline, stress tests, initiatives, and sensitivity; save charts.

Run from the model directory:
    python main.py
Outputs go to ./outputs/.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from baseline import BASELINE, INITIATIVES, STRESS_TESTS, SENSITIVITY_PARAMS, apply_deltas
from calibration import load_calibration, apply_calibration
from model import CohortSimulator, asymptote_closed_form, sensitivity_12m
import plots as p


HORIZON = 24
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def fmt_mau(x: float) -> str:
    return f"{x:,.0f}"


def pct(x: float) -> str:
    return f"{x * 100:+.1f}%"


def print_trajectory_row(label: str, result: dict, baseline_total_0: float):
    total = result["mau_total"]
    marks = [0, 3, 6, 12, 24]
    vals = [total[m] if m < len(total) else total[-1] for m in marks]
    delta_12 = (vals[3] - baseline_total_0) / baseline_total_0
    asymptote = result["asymptote"]
    truncated = label if len(label) <= 42 else label[:39] + "..."
    print(
        f"  {truncated:<44}"
        f"M0 {fmt_mau(vals[0]):>7} | M3 {fmt_mau(vals[1]):>7} | "
        f"M6 {fmt_mau(vals[2]):>7} | M12 {fmt_mau(vals[3]):>7} | "
        f"M24 {fmt_mau(vals[4]):>7} | "
        f"12m Δ {pct(delta_12):>7} | asymp {fmt_mau(asymptote):>7}"
    )


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("=" * 100)
    print("Funnel Leverage Model — v3 (cohort stock-and-flow)")
    print("=" * 100)

    # --- Calibration --------------------------------------------------------
    cal = load_calibration()
    if cal.is_empty():
        print("\n[calibration] No Porygon templates filled yet — using synthetic "
              "steady-state initial stock and hypothesis r_loyal=0.91.")
        print("             Fill CSVs in ../porygon-data-templates/ and rerun "
              "to use real values.")
    else:
        print("\n[calibration] Loaded Porygon data:")
        if cal.initial_stock is not None:
            print(f"   initial activated stock = {cal.initial_stock.sum():,.0f}")
        if cal.initial_passive is not None:
            print(f"   initial passive        = {cal.initial_passive:,.0f}")
        if cal.r_loyal is not None:
            print(f"   r_loyal (observed)     = {cal.r_loyal:.3f}")

    params = apply_calibration(BASELINE, cal)
    sim = CohortSimulator(params)

    # --- Baseline -----------------------------------------------------------
    baseline = sim.simulate(HORIZON)
    baseline_m0 = baseline["mau_total"][0]
    print(f"\nBaseline MAU @ M0 = {fmt_mau(baseline_m0)} | "
          f"M12 = {fmt_mau(baseline['mau_total'][12])} | "
          f"asymptote = {fmt_mau(baseline['asymptote'])}")

    # Cross-check: simulated asymptote must match the closed-form.
    cf = asymptote_closed_form(params)
    err = abs(baseline["asymptote"] - cf) / cf
    print(f"Closed-form check: simulated asymptote {fmt_mau(baseline['asymptote'])} "
          f"vs closed-form {fmt_mau(cf)} (err {err:.2%})")

    # --- Stress tests -------------------------------------------------------
    print("\n" + "-" * 100)
    print("STRESS TESTS — each deviates from baseline on a single axis:")
    print("-" * 100)
    stress_results = []
    for st in STRESS_TESTS:
        scenario = apply_deltas(params, st["deltas"])
        result = sim.simulate(HORIZON, scenario_params=scenario)
        stress_results.append((st["name"], result))
        print_trajectory_row(st["name"], result, baseline_m0)

    # --- Initiatives --------------------------------------------------------
    print("\n" + "-" * 100)
    print("NAMED INITIATIVES — bundles of parameter bets:")
    print("-" * 100)
    initiative_results = []
    for ini in INITIATIVES:
        scenario = apply_deltas(params, ini["deltas"])
        result = sim.simulate(HORIZON, scenario_params=scenario)
        initiative_results.append((ini["name"], result))
        print_trajectory_row(ini["name"], result, baseline_m0)

    # --- Sensitivity --------------------------------------------------------
    print("\n" + "-" * 100)
    print("SENSITIVITY — 12-month MAU change per +10% parameter lift "
          "(ranked by |Δ|):")
    print("-" * 100)
    rows = sensitivity_12m(params, SENSITIVITY_PARAMS, lift_pct=0.10, months=12)
    for r in rows:
        print(f"  {r['param']:<24} "
              f"base {fmt_mau(r['mau_12m_baseline']):>7} -> "
              f"lifted {fmt_mau(r['mau_12m_lifted']):>7} "
              f"({pct(r['pct_delta']):>7}, elasticity {r['elasticity']:+.2f})")

    # --- Charts -------------------------------------------------------------
    print("\n[charts] saving to outputs/")

    fig = p.plot_trajectory(baseline, title="Baseline — 24-month MAU trajectory")
    fig.savefig(OUTPUT_DIR / "baseline-trajectory.png")
    plt.close(fig)

    fig = p.plot_scenario_comparison(baseline, stress_results,
                                     title="Stress tests vs baseline (24m)")
    fig.savefig(OUTPUT_DIR / "stress-tests.png")
    plt.close(fig)

    fig = p.plot_scenario_comparison(baseline, initiative_results,
                                     title="Initiatives vs baseline (24m)")
    fig.savefig(OUTPUT_DIR / "initiatives.png")
    plt.close(fig)

    fig = p.plot_sensitivity(rows)
    fig.savefig(OUTPUT_DIR / "sensitivity.png")
    plt.close(fig)

    fig = p.plot_stock_heatmap(baseline)
    fig.savefig(OUTPUT_DIR / "stock-heatmap.png")
    plt.close(fig)

    print("  - baseline-trajectory.png")
    print("  - stress-tests.png")
    print("  - initiatives.png")
    print("  - sensitivity.png")
    print("  - stock-heatmap.png")
    print("\nDone.")


if __name__ == "__main__":
    main()
