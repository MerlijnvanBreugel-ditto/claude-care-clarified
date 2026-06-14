"""Baseline parameters and named scenario presets.

Baseline values are the Porygon snapshot taken 2026-04-21 (same as v2 HTML).
r_loyal is a hypothesis pending Porygon 1.3 — conservative ~0.91.
"""

from __future__ import annotations

from model import Parameters


BASELINE = Parameters(
    inflow=5000.0,
    reg_rate=0.35,
    act_rate=0.28,
    r1=0.54,
    r2=0.66,
    r_loyal=0.91,
    invite_rate=0.24,
    invites_per_inviter=1.48,
    invite_to_install=0.15,
    invited_act_rate=0.22,
    passive_multiplier=0.36,
    committed_floor=0.0,
)


# Named initiatives — ported from v2-interactive.html. Each entry describes a
# concrete product bet and the parameter deltas we'd expect if it shipped and
# hit its targets. These are belief inputs; tie them to experiment data in v5.
INITIATIVES = [
    {
        "id": "care-circle-v2",
        "name": "Care Circle v2",
        "tag": "Virality boost",
        "bet": "Better invite flow, viral k jumps.",
        "deltas": {
            "invite_rate": 0.30,
            "invites_per_inviter": 1.8,
            "invited_act_rate": 0.26,
        },
    },
    {
        "id": "onboarding-redesign",
        "name": "Onboarding redesign",
        "tag": "Activation boost",
        "bet": "More installers complete reg + first summary.",
        "deltas": {
            "reg_rate": 0.40,
            "act_rate": 0.32,
        },
    },
    {
        "id": "retain-the-activated",
        "name": "Retain the activated",
        "tag": "Retention boost",
        "bet": "Push notifications + weekly summary lift M0→M1 and stable retention.",
        "deltas": {
            "r1": 0.60,
            "r2": 0.70,
        },
    },
    {
        "id": "menzis-partnership",
        "name": "Menzis push",
        "tag": "Inflow boost",
        "bet": "Insurer partnership funnels new installs.",
        "deltas": {
            "inflow": 7500,
        },
    },
    {
        "id": "quality-over-volume",
        "name": "Quality-only installs",
        "tag": "Inflow trade-off",
        "bet": "Tighter targeting: fewer installs, higher activation + M0→M1.",
        "deltas": {
            "inflow": 3000,
            "act_rate": 0.36,
            "r1": 0.60,
        },
    },
    {
        "id": "journey-page",
        "name": "Journey landing page",
        "tag": "Conversion uplift",
        "bet": "Landing page lifts reg intent before install.",
        "deltas": {
            "reg_rate": 0.42,
            "act_rate": 0.30,
        },
    },
]


# Stress tests — deliberately extreme, used to eyeball the trajectory shape.
STRESS_TESTS = [
    {
        "id": "inflow-drop",
        "name": "Inflow 5k → 1k (the bug v2 got wrong)",
        "deltas": {"inflow": 1000.0},
    },
    {
        "id": "retention-lift",
        "name": "Stable retention r2 0.66 → 0.75",
        "deltas": {"r2": 0.75},
    },
    {
        "id": "viral-loop-2x",
        "name": "Viral loop 2× (invite_rate × 2)",
        "deltas": {"invite_rate": 0.48},
    },
    {
        "id": "passive-off",
        "name": "Passive contribution off (multiplier = 0)",
        "deltas": {"passive_multiplier": 0.0},
    },
]


SENSITIVITY_PARAMS = [
    "inflow",
    "reg_rate",
    "act_rate",
    "r1",
    "r2",
    "r_loyal",
    "invite_rate",
    "invites_per_inviter",
    "invite_to_install",
    "invited_act_rate",
    "passive_multiplier",
]


def apply_deltas(base: Parameters, deltas: dict) -> Parameters:
    """Apply a named initiative's deltas to baseline."""
    return base.with_updates(**deltas)
