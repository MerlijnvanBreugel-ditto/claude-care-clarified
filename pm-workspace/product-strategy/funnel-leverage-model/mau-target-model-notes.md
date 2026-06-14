# MAU Target Model — path to 50k

**File:** `mau-target-model.html` (open by double-click, no server, no dependencies)
**Built:** 2026-06-03 · **Calibrated to:** Porygon, May 2026
**Sibling:** the v3 simulator in `model/` answers *"where does leverage live?"* (sensitivity). This answers *"can we hit 50k by Dec, and how?"* (forecasting). Keep both; they are different tools.

## The question

We're at 2,200 MAU (June), have grown ~20%/mo, and want 50,000 by year-end. At 20% we drift to ~7,700. Which driver, moved how far, bends the line back onto 50k?

## The engine

`MAU_next = MAU_now × m`, where the monthly multiplier decomposes into the five drivers:

```
m = ρ(retention) + ν(installs × reg × act ÷ MAU) × a(1/(1−K))
```

Calibrated so baseline driver values produce **exactly 20%/mo** (overlays the drift line). Six sliders in PM-native units: **organic installs 3,450** (115/day, earned floor) · **paid & partner installs 3,550** (bought, ~parked today) · reg 53% · act 15% · M1 retention 40% · K 0.10. Acquisition is split organic-vs-paid so the bought/earned contribution is honest — only paid counts as bought.

## The headline finding

**No single lever reaches 50k.** And the bar is higher than the slide says:

| Claim | Truth the model surfaces |
|---|---|
| "We need 39%/mo" | That was the *Jan→Dec* rate. From June's 2,200 over six months, 50k needs **~68%/mo**. Five months of drift raised the bar. |
| "Retention is the lever" | Best *quality* lever (compounds, protects everything) but **capped near +26%/mo** — you can't retain more than everyone. |
| "Fix the loop" | Virality is **dead at K=0.10** (amp 1.11×). Only matters if K is rebuilt toward self-sustaining. |
| "Pour in installs" | Organic (~115/day) is a free **earned** floor. Scaling **paid** works on this chart (paid→15k ≈ 46k by Dec on its own) but it's **bought** — a rate you pay for monthly, gone when spend stops. |

**The only realistic recipe:** retention near its ceiling **+** ~2–2.5× the activated inflow (installs × activation) **and/or** a materially stronger loop. The tool makes you assemble that combination and shows bought-vs-earned growth as you go.

## Decisions (resolved via VC + statistician lenses)

- **ρ₀ ≈ 0.92 is a plug, not a measurement** — reverse-solved (`ρ₀ = 1.20 − ν·a`) so baseline = 20%. It absorbs reactivation + the gap between cohort retention (40%) and rolling-30-day MAU persistence. Labeled as such in-tool.
- **50k is the operative goal; 39% is a labeled reference** with a note that drift raised the required rate to ~68%.
- **Acquisition tagged "bought" (purple), the rest "earned"** — the VC's quality-of-growth distinction, made visual in the contribution bars.

## What to distrust (all flagged in the tool)

1. ρ is a plug — don't read the 40% retention slider as ρ.
2. The 20% baseline is a *decelerating* trailing average (May +1.7% WoW); drift is optimistic.
3. Rate-based simplification treats acquisition as a *sustained* rate lever — it isn't.
4. Point estimates, no uncertainty bands; the retention→ρ slope (0.30) is an assumption, not a fit.

## Next, if it earns it

Tie slider ranges to historical experiment effect sizes (what a real onboarding or loop change actually moved), and graduate to the v3 cohort simulator for the transient dynamics this rate model deliberately omits.
