# Board deck — filled values (June 2026)

Numbers supplied by the analyst (Mixpanel unless flagged). These are now baked into `board-deck.html`. Charts redrawn to the actual series. See `data-needs.md` for token definitions.

## MAU reconciliation (resolved)
| Figure | Meaning | Used for |
|---|---|---|
| **2,162** | Calendar-month May strict MAU (`summary_viewed`, unique users May 1–31) | `S6_MAU_MAY` (chart) |
| **2,169** | Trailing-30d Core MAU as of Jun 2 | `S5_MAU_NOW` (OKR headline) |
| 2,080 | product-context (May 27) — trailing-30d snapshot 5 days earlier, consistent | — |
| **~3,066** | Expanded MAU (strict + appointment-prep users who never viewed a summary) = the Linear O2 figure | `S7_EXP_MAY` |

Difference is rolling-vs-calendar and strict-vs-expanded, not a data error.

## Slide 5 — OKR Overview (updated from Linear health + "Sharpen" 1 Jun)
| KR | Value on slide | Health | Source / note |
|---|---|---|---|
| Core MAU (headline) | 2,106 → 5,000 | pace 🔴 -37% vs May exit | Sharpen 1 Jun O2 dashboard (vs analyst trailing-30d 2,169 — both valid) |
| O1-KR1 · New hires operational | Wouter + Jasper shipping; brand lead TBD | 🟡 | Linear at-risk · Sharpen |
| O1-KR2 · 15 FTE AI agents | 4 of 15 running | 🟡 | Per Merlijn (4 running). Linear at-risk; Sharpen had 0 live |
| O1-KR3 · 100 MAU + 2 partners outside NL | UK active; 0 partners signed | 🟡 | Linear at-risk · Sharpen |
| O1-KR4 · Proposal & Evaluation | Pipeline live | 🟢 | Linear on-track |
| O2-KR1 · 2,000 partner registrations | 298 / 2,000 (forecast ~414) | 🔴 | Sharpen; Linear off-track. Run rate 3.9/day, structurally blocked |
| O2-KR2 · D14 activation 11→25% | 14% (7d), 19% (28d) | 🟡 | Sharpen (register→summary viewed within 14d); 7d dipped -2pp |
| O2-KR3 · Care-circle size 1.34→3.4 | avg 2.6 | 🟡 | Sharpen; intake -27% WoW; payload workaround active |
| O2-KR4 · MAU retention 40→60% | 39% | 🔴 | Per Merlijn (set to 39). Sharpen had Apr→May 20% final; using 39% |

## Slide 6 — Strict MAU since January (`summary_viewed`, calendar month)
Jan 1,140 · Feb 1,200 · Mar 1,460 · Apr 1,751 · May **2,162** · Jun ~2,594 (proj at 20% MoM).
MoM: 17.6% avg YTD / 21.7% ex-Jan→Feb → deck shows **~20%**.

## Slide 7 — Expanded MAU (strict + appointment-prep) ⚠ estimate ±10%
Definition: strict + users with `event_created`(manual) / `recording_saved` / `document_scanned` who didn't view a summary.
`S7_EXP_MAY` ≈ **3,066**, `S7_EXP_DELTA` ≈ **+42%**.
Series (strict + orange increment): Jan 1,140+480 · Feb 1,200+550 · Mar 1,460+740 · Apr 1,751+870 · May 2,162+900 · Jun ~2,594+950.
⚠ Orange values estimated (55% of manual-appt users + 20% of recording/docscan never view a summary). Precise union needs JQL / data eng.

## Slide 8 — Path back on course (full-year)
End-Q3 (Sep) ≈ **18,488**. Year-end ambition ≈ **50,032** (≈50K).
Actual: Jan 1,140 · Feb 1,200 · Mar 1,460 · Apr 1,751 · May 2,162.
Ambition (8.65% WoW ≈ 39% MoM): Jan 1,300 · Feb 1,812 · Mar 2,525 · Apr 3,518 · May 4,903 · Jun 6,832 · Jul 9,520 · Aug 13,267 · Sep 18,488 · Oct 25,764 · Nov 35,903 · Dec 50,032.
Drift (~20% MoM): Jun 2,594 · Jul 3,113 · Aug 3,736 · Sep 4,483 · Oct 5,380 · Nov 6,456 · Dec 7,747 (≈85% below ambition).
Supersedes earlier 57,638 / analyst-recovery numbers.

## Slide 10 — Audience
Specialty (`summary_categorized`, unique users, Apr 27–Jun 2, n=1,252; users can appear in multiple; ~29% coverage):
Oncology **29.5%** · Cardiology 14.4% · Neurology 11.2% · Orthopedics 11.1% · Other 33.8%.
Country (`summary_viewed`, May): NL **97.1%** (2,100) · UK **0.6%** (14) · Belgium 1.0% · Germany 0.8%.
Oncology uplift: **2.2×** week-1 retention (39% vs 18%); **1.8×** invite acceptance (78% vs 53%). Note: oncology *creates* at ~avg rate but *views* ~2× more over time (retention-driven). Copy adjusted to reflect this.
Hartklinieken = named B2B partner in Adjust → cardiology partially attributable. ✓

## Slide 11 — Activation
Registration **45% → 52%** (Apr→May post skip-button removal; v1.9.7+ specifically 55%).
D14 **11%** (May 1–18 mature; doubled from 5.3% in April).
Calendar pull: launched Jun 1, n=5 completed / 8 allowed access → **too early for a rate**; deck shows it qualitatively.

## Slide 12 — Care Circle
Follower views **+46% MoM** (Apr 245 → May 358). K-factor **≈0.10** (~17% send an invite × ~40% acceptance).
Oncology vs non-oncology: W1 retention **39% / 18%**; invite acceptance **78% / 53%**.
Context: invites accepted Apr 361 → May 500 (+38%); CC installs +21%; CC-install D14 ≈30% (3× organic).
Key insight baked into slide: **75% of Core MAU is CC0**; CC0→CC1 **doubles** monthly summary views (2→4). Largest untapped lever.

## Still open
- **Linear/Confluence:** O1-KR1/KR2/KR4 exact values + phrasing; confirm R/Y/G; partner-registration count vs install proxy.
- **Data eng/JQL:** precise expanded-MAU union (S7) — current values directional.
- **Too early:** calendar-pull adoption (S11).

## Strategic tension to discuss (flagged, not resolved in deck)
The plan needs **~47% MoM** to hit 50K, the analyst names **restarting Meta/Google paid as the fastest path to volume**, yet Lever 1's exit decision is **stop broad paid**. Reconcile the year-end target, the paid stance, or both before the board.
