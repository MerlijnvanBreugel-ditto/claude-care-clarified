"""Sanity tests for the cohort simulator."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

# Make sibling modules importable when running via `pytest` from anywhere.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from model import (  # noqa: E402
    CohortSimulator,
    Parameters,
    STOCK_LEN,
    asymptote_closed_form,
    sensitivity_12m,
)
from baseline import BASELINE  # noqa: E402


def test_baseline_equilibrium_is_flat():
    """Priming from steady state and simulating under the same params keeps MAU flat."""
    sim = CohortSimulator(BASELINE)
    result = sim.simulate(36)
    mau = result["mau_total"]
    # Max deviation from M0 across 36 months should be negligible (< 0.5%).
    rel_dev = np.max(np.abs(mau - mau[0]) / mau[0])
    assert rel_dev < 0.005, f"Baseline drifts by {rel_dev:.3%}, expected <0.5%"


def test_simulated_matches_closed_form_asymptote():
    """After a long run, simulated MAU converges to the analytical asymptote."""
    sim = CohortSimulator(BASELINE)
    # Start from an empty stock and run for many months.
    empty = np.zeros(STOCK_LEN)
    result = sim.simulate(240, initial_stock=empty)
    final = result["mau_total"][-1]
    cf = asymptote_closed_form(BASELINE)
    assert abs(final - cf) / cf < 0.001, f"simulated {final:.1f} vs closed {cf:.1f}"


def test_closed_form_matches_v2_when_loyal_equals_stable():
    """When r_loyal == r2, the three-tier asymptote collapses to v2's formula
    ATotal * (1 + r1/(1-r2)) * (1 + passive_multiplier) + committed_floor."""
    p = BASELINE.with_updates(r_loyal=BASELINE.r2)
    A0 = p.inflow * p.reg_rate * p.act_rate
    K = p.viral_coefficient()
    ATotal = A0 / (1 - K)
    v2_activated = ATotal * (1 + p.r1 / (1 - p.r2))
    v2_total = (
        v2_activated
        + p.passive_multiplier * v2_activated
        + p.committed_floor
    )
    assert abs(asymptote_closed_form(p) - v2_total) / v2_total < 1e-6


def test_inflow_drop_is_gradual_not_cliff():
    """The v2 bug this model fixes: dropping inflow 5000->1000 must NOT cause
    an instantaneous 80% collapse. Stock persists and decays over months.

    With the baseline parameters, ~38% of activated MAU are users who activated
    in the current month (s_0). Dropping inflow 80% therefore costs ~30% of
    MAU in M1 — much better than v2's 80% cliff, and followed by a gradual
    multi-quarter slide to the new asymptote."""
    sim = CohortSimulator(BASELINE)
    scenario = BASELINE.with_updates(inflow=1000.0)
    result = sim.simulate(24, scenario_params=scenario)
    mau = result["mau_total"]
    m0, m1, m6, m24 = mau[0], mau[1], mau[6], mau[24]

    m1_drop = (m0 - m1) / m0
    # Must be meaningfully less than the v2 cliff (~80%) and under the
    # long-run asymptote drop — i.e., stock is protecting us.
    assert m1_drop < 0.40, f"M1 drop {m1_drop:.2%} is too steep (v2-style cliff)"

    # By M24 we should be approaching the new (lower) asymptote, well below M0.
    m24_drop = (m0 - m24) / m0
    assert m24_drop > 0.50, f"M24 drop only {m24_drop:.2%} — decay too slow"

    # Decay must be monotone: M1 < M6 < M24.
    m6_drop = (m0 - m6) / m0
    assert m1_drop < m6_drop < m24_drop


def test_retention_lift_compounds():
    """Lifting r2 produces a gradual MAU rise that grows over time."""
    sim = CohortSimulator(BASELINE)
    scenario = BASELINE.with_updates(r2=0.75)
    result = sim.simulate(24, scenario_params=scenario)
    mau = result["mau_total"]
    # M1 lift should be modest; M24 lift should be substantially larger.
    m0 = mau[0]
    lift_1 = (mau[1] - m0) / m0
    lift_24 = (mau[24] - m0) / m0
    assert lift_24 > lift_1 * 3, (
        f"Retention lift should compound — got M1 {lift_1:.2%} vs M24 {lift_24:.2%}"
    )


def test_loyal_self_loop_preserves_stock_without_new_cohorts():
    """With r_loyal=1 and inflow=0, the loyal bucket is conserved."""
    sim = CohortSimulator(BASELINE)
    stock = np.zeros(STOCK_LEN)
    stock[-1] = 1000.0
    scenario = BASELINE.with_updates(inflow=0.0, r_loyal=1.0)
    result = sim.simulate(12, scenario_params=scenario, initial_stock=stock)
    assert np.isclose(result["stock"][-1][-1], 1000.0, atol=1e-6)
    assert np.isclose(result["mau_activated"][-1], 1000.0, atol=1e-6)


def test_sensitivity_orders_by_absolute_delta():
    rows = sensitivity_12m(BASELINE, ["inflow", "r1", "r2", "passive_multiplier"],
                           lift_pct=0.10, months=12)
    abs_deltas = [abs(r["abs_delta"]) for r in rows]
    assert abs_deltas == sorted(abs_deltas, reverse=True)


def test_k_below_one_guard():
    bad = BASELINE.with_updates(invite_rate=5.0, invites_per_inviter=5.0,
                                invite_to_install=1.0, invited_act_rate=1.0)
    with pytest.raises(ValueError):
        bad.cohort_per_month()
