# Source Synthesis 02 — Growth & Retention Diagnosis

> Distills: `product-strategy/code-red-mau-improvement/` (founders-notes, retention + virality research) and `product-strategy/funnel-leverage-model/` (README, growth-frameworks-research).
> A synthesis for the long-term vision, not a copy.

## The Code Red diagnosis (May 2026)

Growth is **linear, not exponential**. Core MAU ~2,080 against a 5K-by-June / 50K-by-year-end Series A milestone (~36% behind pace). Root causes: D30 retention ~30%, care-circle invite acceptance ~28%, so churn offsets acquisition and MAU plateaus. The product's dependence on appointments as the activation trigger is the named core vulnerability.

## The two problems behind the gap

1. **Acquisition mismatch**: performance marketing pulls too broad a group, many "too healthy" to feel the pain.
2. **Activation dependency**: even for the right users, the aha moment (a summary) needs an external event (an appointment) Ditto doesn't control. Funnel: ~10% set a trackable appointment, ~4% complete the next step.

## The frequency problem (the heart of it)

Ditto sits in Reforge's **"Forgettable Zone"** (used less than monthly). The standard retention playbook fails there. Three legitimate escapes, all with healthcare equivalents:

| Escape | Mechanism | Ditto equivalent |
|---|---|---|
| Own the unavoidable event | TurboTax (77% annual retention) | Medical appointments happen; be the obvious tool |
| Latch onto a daily behavior | Airlines + credit cards; Calm + sleep | Calendar integration; care circle as daily social layer |
| Add between-visit utility | Wysa/Ginger | Symptom tracking, medication, next-visit prep |

Correct benchmark: consumer-transactional "GOOD" is ~30% annual retention, "GREAT" ~50%. Ditto should not be held to a daily-habit-app standard, but it does need a between-visit reason to open.

## Retention beats virality (the funnel model)

The v3 cohort model's load-bearing findings:
1. **Retention has the biggest compounding leverage.** +10% on r₂ lifts 12-month MAU ~15% vs ~10% for any funnel-conversion knob. Retention protects every acquisition dollar.
2. **The care-circle loop is mathematically tiny at current K ≈ 0.012.** Doubling invite rate lifts MAU ~1%. The leverage hides in the untracked invite→install leakage, not the invite rate.
3. The activated base is inflow-heavy short-run (s_0 ≈ 38% of activated MAU), so quality-of-inflow matters.

## Virality reality (low-frequency, finite-network)

- The care circle is a **finite, closed graph** (5-10 people). Each patient recruits their whole circle once, then the loop closes. It is a **receiver network, not a propagation network**. Growth comes from new patients, not circle members recruiting their own circles.
- Cycle time is crippling (a ~90-day appointment cycle gives ~4 share triggers/year). K-factor is the wrong primary metric.
- What actually works: **notification-pull virality** (the update creates the install pull), **institutional/HCP referral** (CaringBridge's ~500 hospital partnerships were the real engine), **shareable web summary** (no-install read), and the **slow cross-life-event loop** (a circle member becomes a patient later).
- Self-monitoring is the strongest retention lever found: ~80% retained at 40 weeks vs ~60% for non-users.

## Merlijn's own strategic anchors (founders-notes)

- **Patient retention is the prerequisite, not care circle.** Care circle amplifies a working loop; it doesn't create one. If patients stop creating summaries, followers have no reason to return.
- Skeptical the k=0.35 figure is real organic virality (invites are pushed during onboarding).
- The deeper question: are we attracting the right people, and is the core valuable enough to retain them? The Uber analogy: a product can earn its place through reliability at the moment of need, even if rare. Open question whether low retention is a frequency problem or a value problem.
- Narrow targeting (oncology) may yield higher-quality users who activate/retain better; test, don't assume.

## Implications for the vision

- **Fix retention before adding frequency.** Every route in the vision is gated on this.
- The honest path to higher frequency is between-visit utility (symptoms, meds, coordination) or shifting to a higher-frequency user (the caregiver) or window (active treatment), not engineering the viral loop.
- Track new patients/month and circle fill-rate, not K-factor.
- Move the share trigger to appointment-day; make the circle-member experience worth having (they are the long-term acquisition pipeline).
