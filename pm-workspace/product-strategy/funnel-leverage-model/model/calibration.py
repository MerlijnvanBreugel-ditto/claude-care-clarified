"""Loaders for the Porygon CSV templates in ../porygon-data-templates.

Each loader:
  • reads the CSV (pandas)
  • checks whether any value rows are actually filled (templates ship empty)
  • returns None if empty, or a parsed numeric artifact if filled

Call `load_calibration()` to get back a single `Calibration` bundle that you
can pass into the simulator to override synthetic initial state and retention.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd


TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "porygon-data-templates"


# Map the activated-stock CSV's six tenure buckets onto the simulator's 13-slot
# stock vector. Buckets span integer-month ranges; we spread each bucket's
# users uniformly across the months it covers. Monthly resolution from Porygon
# (1.1b) would let us drop the uniform assumption.
BUCKET_SPANS = {
    "0-1m":   [0],
    "1-3m":   [1, 2],
    "3-6m":   [3, 4, 5],
    "6-12m":  [6, 7, 8, 9, 10, 11],
    "12-24m": [12],          # goes into the loyal bucket
    "24m+":   [12],          # also loyal
}


@dataclass
class Calibration:
    initial_stock: Optional[np.ndarray] = None     # length 13
    initial_passive: Optional[float] = None
    r_loyal: Optional[float] = None
    # Retained for diagnostics / printing; not consumed by the simulator yet:
    cohort_retention: Optional[pd.DataFrame] = None
    growth_accounting: Optional[pd.DataFrame] = None

    def is_empty(self) -> bool:
        return (
            self.initial_stock is None
            and self.initial_passive is None
            and self.r_loyal is None
            and self.cohort_retention is None
            and self.growth_accounting is None
        )


def _read_csv_if_filled(path: Path, value_cols: list[str]) -> Optional[pd.DataFrame]:
    """Return the dataframe if at least one value cell is non-empty, else None."""
    if not path.exists():
        return None
    df = pd.read_csv(path)
    # value_cols may be absent in odd templates — intersect with actual cols
    cols = [c for c in value_cols if c in df.columns]
    if not cols:
        return None
    has_values = df[cols].notna().any().any() and df[cols].apply(
        lambda col: col.astype(str).str.strip().ne("")
    ).any().any()
    return df if has_values else None


def load_stock_by_tenure(path: Path = TEMPLATES_DIR / "1.1-stock-by-tenure.csv") -> tuple[Optional[np.ndarray], Optional[float]]:
    """Return (activated_stock_vector_length_13, passive_total) or (None, None)."""
    df = _read_csv_if_filled(path, ["n_users"])
    if df is None:
        return None, None

    df = df.copy()
    df["n_users"] = pd.to_numeric(df["n_users"], errors="coerce").fillna(0)

    stock = np.zeros(13)
    for _, row in df[df["population"] == "activated"].iterrows():
        bucket = row["tenure_bucket"]
        users = float(row["n_users"])
        slots = BUCKET_SPANS.get(bucket, [])
        if not slots:
            continue
        per_slot = users / len(slots)
        for idx in slots:
            stock[idx] += per_slot

    passive_total = float(df[df["population"] == "passive"]["n_users"].sum())
    passive = passive_total if passive_total > 0 else None
    return stock, passive


def load_loyal_tail_retention(path: Path = TEMPLATES_DIR / "1.3-loyal-tail-retention.csv") -> Optional[float]:
    """Return a weighted average of the 12-24m and 24m+ retention rates."""
    df = _read_csv_if_filled(path, ["retention_rate"])
    if df is None:
        return None

    df = df.copy()
    df["retention_rate"] = pd.to_numeric(df["retention_rate"], errors="coerce")
    df["n_active_start"] = pd.to_numeric(df.get("n_active_start"), errors="coerce")
    filled = df.dropna(subset=["retention_rate"])
    if filled.empty:
        return None

    # Weight by starting N if we have it; else unweighted mean.
    if filled["n_active_start"].notna().any():
        w = filled["n_active_start"].fillna(0)
        if w.sum() > 0:
            return float(np.average(filled["retention_rate"], weights=w))
    return float(filled["retention_rate"].mean())


def load_cohort_retention(path: Path = TEMPLATES_DIR / "1.2-cohort-retention.csv") -> Optional[pd.DataFrame]:
    df = _read_csv_if_filled(path, ["survival_fraction", "n_still_active"])
    if df is None:
        return None
    df = df.copy()
    df["survival_fraction"] = pd.to_numeric(df["survival_fraction"], errors="coerce")
    df["n_still_active"] = pd.to_numeric(df["n_still_active"], errors="coerce")
    df["n_cohort_start"] = pd.to_numeric(df.get("n_cohort_start"), errors="coerce")
    return df


def load_growth_accounting(path: Path = TEMPLATES_DIR / "2.1-growth-accounting.csv") -> Optional[pd.DataFrame]:
    df = _read_csv_if_filled(path, ["new_users", "resurrected", "retained", "churned"])
    if df is None:
        return None
    return df


def load_calibration() -> Calibration:
    """Load every template that has been filled. Returns an empty Calibration
    (all Nones) when the templates haven't been populated yet — which is the
    current state on 2026-04-22."""
    initial_stock, initial_passive = load_stock_by_tenure()
    return Calibration(
        initial_stock=initial_stock,
        initial_passive=initial_passive,
        r_loyal=load_loyal_tail_retention(),
        cohort_retention=load_cohort_retention(),
        growth_accounting=load_growth_accounting(),
    )


def apply_calibration(params, cal: Calibration):
    """Return a Parameters copy with any non-None calibration values merged in."""
    updates = {}
    if cal.initial_stock is not None:
        updates["initial_stock"] = cal.initial_stock
    if cal.initial_passive is not None:
        updates["initial_passive"] = cal.initial_passive
    if cal.r_loyal is not None:
        updates["r_loyal"] = cal.r_loyal
    if not updates:
        return params
    return params.with_updates(**updates)
