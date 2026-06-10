"""Matplotlib helpers. Each returns a figure; the caller decides where to save."""

from __future__ import annotations

from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 150,
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
})


def plot_trajectory(result: dict, title: str = "MAU trajectory", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4.2))
    else:
        fig = ax.figure

    t = result["t"]
    ax.plot(t, result["mau_total"], label="Total MAU", linewidth=2.2, color="#0f766e")
    ax.plot(t, result["mau_activated"], label="Activated", linewidth=1.3, color="#2563eb", alpha=0.7)
    ax.plot(t, result["mau_passive"], label="Passive", linewidth=1.3, color="#f59e0b", alpha=0.7)
    if result["mau_committed"].max() > 0:
        ax.plot(t, result["mau_committed"], label="Committed", linewidth=1.0, color="#64748b", alpha=0.7)

    ax.axhline(result["asymptote"], color="#64748b", linestyle="--", linewidth=1,
               label=f"Asymptote = {result['asymptote']:,.0f}")
    ax.set_xlabel("Month")
    ax.set_ylabel("MAU")
    ax.set_title(title)
    ax.legend(loc="best", frameon=False, fontsize=8)
    fig.tight_layout()
    return fig


def plot_scenario_comparison(baseline_result: dict, scenarios: list[tuple[str, dict]],
                             title: str = "Scenario comparison"):
    fig, ax = plt.subplots(figsize=(9, 5))
    t = baseline_result["t"]
    ax.plot(t, baseline_result["mau_total"], label="Baseline", linewidth=2.4, color="#0f172a")

    cmap = plt.cm.viridis(np.linspace(0.15, 0.85, max(len(scenarios), 1)))
    for (label, result), color in zip(scenarios, cmap):
        ax.plot(result["t"], result["mau_total"], label=label, linewidth=1.6, color=color)
        ax.axhline(result["asymptote"], color=color, linestyle=":", linewidth=0.7, alpha=0.6)

    ax.set_xlabel("Month")
    ax.set_ylabel("MAU")
    ax.set_title(title)
    ax.legend(loc="best", frameon=False, fontsize=8)
    fig.tight_layout()
    return fig


def plot_sensitivity(rows: Iterable[dict], metric: str = "pct_delta",
                     title: str = "12-month MAU sensitivity (+10% per param)"):
    rows = list(rows)
    # Keep sort order as-passed (already sorted by caller), but flip for horizontal bars
    labels = [r["param"] for r in rows][::-1]
    values = [r[metric] * 100 for r in rows][::-1]
    colors = ["#0f766e" if v >= 0 else "#b91c1c" for v in values]

    fig, ax = plt.subplots(figsize=(8, 0.36 * len(rows) + 1.2))
    ax.barh(labels, values, color=colors, alpha=0.85)
    ax.axvline(0, color="#0f172a", linewidth=0.8)
    ax.set_xlabel("% change in 12-month MAU")
    ax.set_title(title)
    for i, v in enumerate(values):
        ax.text(v + (0.3 if v >= 0 else -0.3), i, f"{v:+.1f}%",
                va="center", ha="left" if v >= 0 else "right", fontsize=8)
    fig.tight_layout()
    return fig


def plot_stock_heatmap(result: dict, title: str = "Activated stock by tenure over time"):
    fig, ax = plt.subplots(figsize=(9, 4.2))
    stock = result["stock"].T  # shape (13, months+1)
    im = ax.imshow(stock, aspect="auto", origin="lower", cmap="viridis")
    ax.set_xlabel("Month")
    ax.set_ylabel("Tenure bucket (0..11, 12=loyal)")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="Users")
    fig.tight_layout()
    return fig
