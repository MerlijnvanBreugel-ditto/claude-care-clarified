"""Cohort stock-and-flow simulator for Ditto Care's user funnel.

State vector `s` has 13 components:
    s[0..11]  — activated users by integer tenure in months (0..11)
    s[12]     — "loyal" bucket, absorbing everyone at 12+ months

Monthly step:
    s_new[tau+1] = s_old[tau] * r[tau]      for tau in 0..10
    s_new[12]    = s_old[11] * r[11] + s_old[12] * r_loyal
    s_new[0]     = C_t     (this month's fresh activation cohort)

Per-tenure retention vector r has length 12:
    r[0]      = r1        (the activation-to-M1 cliff, ~0.54)
    r[1..11]  = r2        (the stable-but-still-decaying core, ~0.66)
Self-loop retention in the loyal bucket: r_loyal (~0.91).

Fresh cohort:
    C_t = inflow * reg_rate * act_rate / (1 - K)
    K   = invite_rate * invites_per_inviter * invite_to_install * invited_act_rate

Passive MAU and the committed floor are additive on top. Passive is currently
a multiplier on activated stock — see ../porygon-data-templates/2.2 for the
data needed to split passive into its own cohort curve in v4.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Optional

import numpy as np


N_TENURES = 12          # integer tenure buckets s_0..s_11
LOYAL_IDX = N_TENURES   # the absorbing bucket index in the stock vector
STOCK_LEN = N_TENURES + 1


@dataclass
class Parameters:
    """All knobs the simulator exposes. Units: months."""

    # Acquisition funnel
    inflow: float = 5000.0
    reg_rate: float = 0.35
    act_rate: float = 0.28

    # Three-tier retention
    r1: float = 0.54
    r2: float = 0.66
    r_loyal: float = 0.91

    # Care Circle viral loop
    invite_rate: float = 0.24
    invites_per_inviter: float = 1.48
    invite_to_install: float = 0.15
    invited_act_rate: float = 0.22

    # Secondary MAU contributions
    passive_multiplier: float = 0.36
    committed_floor: float = 0.0

    # Optional calibration overrides
    initial_stock: Optional[np.ndarray] = None    # length STOCK_LEN
    initial_passive: Optional[float] = None

    def viral_coefficient(self) -> float:
        return (
            self.invite_rate
            * self.invites_per_inviter
            * self.invite_to_install
            * self.invited_act_rate
        )

    def cohort_per_month(self) -> float:
        K = self.viral_coefficient()
        if K >= 1.0:
            raise ValueError(
                f"Viral coefficient K={K:.3f} >= 1.0 — the loop is self-sustaining "
                "and the closed-form solution diverges. Cap one of the invite params."
            )
        return self.inflow * self.reg_rate * self.act_rate / (1 - K)

    def retention_vector(self) -> np.ndarray:
        """Length-12 vector of per-step retention rates (tenure tau -> tau+1)."""
        r = np.full(N_TENURES, self.r2)
        r[0] = self.r1
        return r

    def with_updates(self, **deltas) -> "Parameters":
        """Return a copy of self with named fields overridden."""
        return replace(self, **deltas)


class CohortSimulator:
    """Discrete-time time-homogeneous Markov cohort simulator."""

    def __init__(self, params: Parameters):
        self.params = params

    def step(self, stock: np.ndarray, params: Parameters) -> np.ndarray:
        r = params.retention_vector()
        new = np.zeros(STOCK_LEN)
        new[1:N_TENURES] = stock[0 : N_TENURES - 1] * r[0 : N_TENURES - 1]
        new[LOYAL_IDX] = (
            stock[N_TENURES - 1] * r[N_TENURES - 1]
            + stock[LOYAL_IDX] * params.r_loyal
        )
        new[0] = params.cohort_per_month()
        return new

    def steady_state(self, params: Optional[Parameters] = None) -> np.ndarray:
        """Analytical fixed point of the step() recursion."""
        p = params or self.params
        r = p.retention_vector()
        C = p.cohort_per_month()
        stock = np.zeros(STOCK_LEN)
        stock[0] = C
        for tau in range(1, N_TENURES):
            stock[tau] = stock[tau - 1] * r[tau - 1]
        # Loyal bucket: absorbing state of a geometric self-loop.
        # If r_loyal >= 1 the system has no finite steady state for C > 0;
        # for C == 0 it's 0. Callers (prime, asymptote) handle the returned value.
        inflow_to_loyal = stock[N_TENURES - 1] * r[N_TENURES - 1]
        if p.r_loyal >= 1.0:
            stock[LOYAL_IDX] = np.inf if inflow_to_loyal > 0 else 0.0
        else:
            stock[LOYAL_IDX] = inflow_to_loyal / (1 - p.r_loyal)
        return stock

    def prime(self) -> np.ndarray:
        """Return the initial stock: calibrated if provided, else steady state."""
        if self.params.initial_stock is not None:
            stock = np.asarray(self.params.initial_stock, dtype=float)
            if stock.shape != (STOCK_LEN,):
                raise ValueError(
                    f"initial_stock must be length {STOCK_LEN}, got shape {stock.shape}"
                )
            return stock.copy()
        return self.steady_state()

    def simulate(
        self,
        months: int,
        scenario_params: Optional[Parameters] = None,
        initial_stock: Optional[np.ndarray] = None,
    ) -> dict:
        """Run a months-long simulation. Returns a trajectory dict."""
        p_init = self.params
        p_sim = scenario_params or self.params

        if initial_stock is not None:
            s = np.asarray(initial_stock, dtype=float).copy()
        elif p_init.initial_stock is not None:
            s = np.asarray(p_init.initial_stock, dtype=float).copy()
        else:
            # Prime from p_init (today's world), then simulate under p_sim (scenario).
            s = CohortSimulator(p_init).steady_state()

        initial_passive = (
            p_init.initial_passive
            if p_init.initial_passive is not None
            else p_init.passive_multiplier * s.sum()
        )

        stocks = [s.copy()]
        mau_activated = [s.sum()]
        mau_passive = [initial_passive]
        mau_committed = [p_sim.committed_floor]

        for _ in range(months):
            s = self.step(s, p_sim)
            stocks.append(s.copy())
            mau_activated.append(s.sum())
            mau_passive.append(p_sim.passive_multiplier * s.sum())
            mau_committed.append(p_sim.committed_floor)

        mau_activated = np.asarray(mau_activated)
        mau_passive = np.asarray(mau_passive)
        mau_committed = np.asarray(mau_committed)
        mau_total = mau_activated + mau_passive + mau_committed

        steady_stock = self.steady_state(p_sim).sum()
        asymptote = (
            steady_stock
            + p_sim.passive_multiplier * steady_stock
            + p_sim.committed_floor
        )

        return {
            "t": np.arange(months + 1),
            "stock": np.vstack(stocks),
            "mau_activated": mau_activated,
            "mau_passive": mau_passive,
            "mau_committed": mau_committed,
            "mau_total": mau_total,
            "asymptote": asymptote,
            "params_init": p_init,
            "params_sim": p_sim,
        }


def asymptote_closed_form(params: Parameters) -> float:
    """Long-run MAU under params — matches v2's steady-state formula when
    r_loyal == r2. Useful as an independent cross-check against simulate()."""
    C = params.cohort_per_month()
    r1, r2, rL = params.r1, params.r2, params.r_loyal
    # Contribution from s_0..s_11 : C * (1 + r1 * sum_{k=0..10} r2^k)
    geom = (1 - r2**11) / (1 - r2) if r2 != 1 else 11
    prefix = C * (1 + r1 * geom)
    # Contribution from loyal : C * r1 * r2^11 / (1 - rL)
    loyal = C * r1 * (r2**11) / (1 - rL)
    activated = prefix + loyal
    passive = params.passive_multiplier * activated
    return activated + passive + params.committed_floor


def sensitivity_12m(
    baseline: Parameters,
    params_to_vary: list[str],
    lift_pct: float = 0.10,
    months: int = 12,
) -> list[dict]:
    """For each named parameter, simulate a +lift_pct change and report the
    12-month MAU delta vs. baseline. Returns a list of dicts sorted by |delta|."""
    sim = CohortSimulator(baseline)
    base = sim.simulate(months)
    base_mau = base["mau_total"][-1]

    rows = []
    for name in params_to_vary:
        val = getattr(baseline, name)
        new_val = val * (1 + lift_pct)
        # Clamp retention rates to [0, 0.999] to stay physical
        if name in {"r1", "r2", "r_loyal", "reg_rate", "act_rate",
                    "invite_rate", "invite_to_install", "invited_act_rate"}:
            new_val = min(new_val, 0.999)
        scenario = baseline.with_updates(**{name: new_val})
        result = sim.simulate(months, scenario_params=scenario)
        mau = result["mau_total"][-1]
        rows.append({
            "param": name,
            "baseline_value": val,
            "lifted_value": new_val,
            "mau_12m_baseline": base_mau,
            "mau_12m_lifted": mau,
            "abs_delta": mau - base_mau,
            "pct_delta": (mau - base_mau) / base_mau if base_mau else 0.0,
            "elasticity": ((mau - base_mau) / base_mau) / lift_pct if base_mau else 0.0,
        })
    rows.sort(key=lambda r: abs(r["abs_delta"]), reverse=True)
    return rows
