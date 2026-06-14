# Data needs — Board deck (Growing Ditto)

Fill-in list for `board-deck.html`. Every yellow `[S…]` placeholder maps to one row below. Hand this to the analyst.

## How to use
- Tokens are **slide-scoped**: `[S{slide}_{METRIC}]`. The slide number matches the `data-slide` attribute and the headers below.
- To fill: open `board-deck.html`, find the token text (e.g. `[S6_MAU_MAY]`), replace it with the value.
- **Charts (SVG):** the visible number is a token in `<text>`, but the **bar/line shape is fixed illustrative geometry**. Each chart has a comment with the redraw recipe. Update both the number and the geometry, or send me the final series and I'll redraw.
- **Granularity:** where it says "monthly Jan–Jun" or "monthly Jan–Dec", give one value per month so the chart can be drawn.

## Definitions (used across slides)
| Term | Definition |
|---|---|
| **MAU (strict / North Star)** | Unique users who view ≥1 summary in a calendar month. Event: `summary_viewed`. |
| **MAU (expanded)** | Strict MAU plus users who engaged via appointment preparation (added / acted on an appointment) without a summary view that month. Confirm the exact union. |
| **D14 activation** | Of installs, the % who view their first summary within 14 days. |
| **Care-circle size** | Average members per active care circle (note PRO-290 measurement caveat). |
| **K-factor** | Viral coefficient = invites sent per user × invite acceptance rate. |

Source vocabulary: **Mixpanel** (event/property), **Linear** (OKR/initiative), **Porygon** (#insights bot), **Confluence** (OKR pace page).

> **OKR wording note:** the 8 KRs below are taken from Linear (O1-KR1..4, O2-KR1..4). Verify the latest phrasing and current values against the Confluence OKR-pace page.

---

## Slide 5 — OKR Overview (2 objectives × 4 KRs)
| Token | Key result | Target | Source | Current value |
|---|---|---|---|---|
| `[S5_MAU_NOW]` | Core MAU (headline) | → 5,000 by Jun 30 | Mixpanel `summary_viewed` | |
| `[S5_O1_HIRES]` | New hires onboarded & fully operational | by Jun 1 | Linear O1-KR1 | |
| `[S5_O1_AGENTS]` | FTE-equivalent AI agents deployed | 15 | Linear O1-KR2 | |
| `[S5_O1_INTL]` | MAU + partners referring outside NL | 100 MAU + 2 partners | Linear O1-KR3 | |
| `[S5_O1_PROCESS]` | Major initiatives following Proposal & Evaluation | 100% | Linear O1-KR4 | |
| `[S5_O2_PARTNER]` | Partner registrations | 2,000 | Linear O2-KR1 / Porygon | |
| `[S5_O2_D14]` | D14 activation | 11% → 25% | Mixpanel / Linear O2-KR2 | |
| `[S5_O2_CIRCLE]` | Average care-circle size | 1.34 → 3.4 | Mixpanel / Linear O2-KR3 | |
| `[S5_O2_RETENTION]` | MAU retention | 40% → 60% | Mixpanel / Linear O2-KR4 | |

*R/Y/G health dots are set in the deck from Linear (R = at risk/off track, Y = at risk, G = on track). Tell me if any flipped.*

## Slide 6 — MAU Since January (strict, looks red)
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S6_MAU_MAY]` | Strict MAU, May | summary_viewed, May | May | Mixpanel | |
| `[S6_MOM_PCT]` | Month-over-month growth | Avg MoM % growth of strict MAU YTD | Derived | Mixpanel | |
| *(chart geometry)* | Strict MAU series | summary_viewed per month | **Monthly Jan–Jun** (Jun = projection) | Mixpanel | Jan __ Feb __ Mar __ Apr __ May __ Jun __ |

## Slide 7 — It's More Orange Than Red (expanded, stacked)
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S7_EXP_MAY]` | Expanded MAU, May | strict + appointment-prep engaged users | May | Mixpanel (define union) | |
| `[S7_EXP_DELTA]` | Uplift vs strict | (Expanded − Strict) / Strict × 100, May | May | Derived | |
| *(chart geometry)* | Strict MAU (teal base) | summary_viewed per month | Monthly Jan–Jun | Mixpanel | Jan __ … Jun __ |
| *(chart geometry)* | Appointments-added increment (orange) | expanded − strict per month | Monthly Jan–Jun | Mixpanel | Jan __ … Jun __ |

## Slide 8 — The Path Back On Course (full-year projection)
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S8_Q3_TARGET]` | End-Q3 (Sep) MAU checkpoint | Planned strict MAU at end of September | Sep | Plan / Mixpanel | |
| *(chart geometry)* | Actual MAU | strict, Jan–May | Monthly Jan–May | Mixpanel | Jan __ … May __ |
| *(chart geometry)* | Plan — back on course | planned strict MAU Jun→Dec | Monthly Jun–Dec | Plan | Jun __ … Dec __ |
| *(chart geometry)* | Drift (if nothing changes) | strict MAU continued at current MoM | Monthly Jun–Dec | Derived | Jun __ … Dec __ |

*Year-end target (50,000) and Jun 30 target (5,000) are fixed strategy. The "drift" line = May value compounded at `[S6_MOM_PCT]`% MoM.*

## Slide 10 — Lever 1 · Audience
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S10_ONCOLOGY]` | Oncology share | % of categorised summaries, oncology | Snapshot | Mixpanel | |
| `[S10_CARDIOLOGY]` | Cardiology share | as above | Snapshot | Mixpanel | |
| `[S10_ORTHO]` | Orthopedics share | as above | Snapshot | Mixpanel | |
| `[S10_NEURO]` | Neurology share | as above | Snapshot | Mixpanel | |
| `[S10_OTHER]` | All other specialties | 100 − top 4 | Snapshot | Derived | |
| `[S10_NL]` | Netherlands share | % of users (or summaries) from NL | Snapshot | Mixpanel `country` | |
| `[S10_UK]` | United Kingdom share | % from UK | Snapshot | Mixpanel `country` | |
| `[S10_ONCO_SUMMARIES]` | Oncology summary uplift | how many more summaries oncology patients create vs avg (e.g. "1.8×" or "+40%") | Snapshot | Mixpanel | |
| `[S10_ONCO_SHARE]` | Oncology sharing uplift | how much more often oncology patients share vs avg | Snapshot | Mixpanel | |

*Confirm: cardiology volume is attributed to the Hartklinieken partnership channel.*

## Slide 11 — Lever 2 · Activation
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S11_REG_BEFORE]` | Registration rate, before | install → registration, pre skip-button removal | Pre-change cohort | Mixpanel | |
| `[S11_REG_AFTER]` | Registration rate, after | install → registration, post change | Post-change cohort | Mixpanel | |
| `[S11_D14]` | D14 activation | latest mature cohort | Latest | Mixpanel | |
| `[S11_CALPULL_ADOPTION]` | Calendar-pull adoption | % of exposed users adopting calendar pull | Latest | Mixpanel (experiment) | |

## Slide 12 — Lever 3 · Care Circle
| Token | Metric | Definition | Granularity | Source | Value |
|---|---|---|---|---|---|
| `[S12_VIEWS_MOM]` | Follower summary-views growth | MoM % growth in summaries viewed by followers | MoM | Mixpanel | |
| `[S12_KFACTOR]` | Care-circle K-factor | invites/user × acceptance rate | Latest | Mixpanel | |
| `[S12_ONCO_RET]` | Week-1 retention, oncology | % retained week 1, oncology cohort | Latest | Mixpanel | |
| `[S12_NON_RET]` | Week-1 retention, non-oncology | as above, non-oncology | Latest | Mixpanel | |
| `[S12_ONCO_ACC]` | Circle invite acceptance, oncology | % invites accepted, oncology | Latest | Mixpanel | |
| `[S12_NON_ACC]` | Circle invite acceptance, non-oncology | as above, non-oncology | Latest | Mixpanel | |

---

## Open reconciliation (flag before the meeting)
Two different "current MAU" figures appear across sources:
- **product-context.md**: Core MAU ≈ 2,080 (27 May, `summary_viewed` 30d).
- **Linear O2**: ≈ 3,066 (May).

Reconcile to one canonical strict-MAU number + definition before filling `[S5_MAU_NOW]` / `[S6_MAU_MAY]` (likely a 30-day-rolling vs calendar-month difference). Confirm which the board number should be.
