# Porygon Data Requests — to calibrate the Funnel Leverage Model (v3 / Python)

**Requested by:** Merlijn
**Created:** 2026-04-22
**For:** `pm-workspace/specs/funnel-leverage-model/model/` (Python cohort stock-and-flow simulator)
**Why now:** the current model behaves unrealistically under scenario changes because it has no stock-and-flow structure — dropping installs 5,000 → 1,000 makes MAU "collapse" to 349 instantly, ignoring that today's loyal users decay slowly on their own retention curves. A cohort-based Markov-style simulator fixes this, but it needs *real* tenure and retention data rather than the synthetic distributions we're currently using to prime it.

**How to respond:** Please fill in the CSV templates in `porygon-data-templates/` (paths below). Each template has a header row specifying column names, units, and what "active" means for that query. **Numbers only — please don't interpret.** If a metric is impossible to compute with current tracking, leave the cells blank and note it in the "caveats" column instead of deleting the row.

**Why CSV?** Machine-readable so the Python model can consume it with `pandas.read_csv()` and rerun the entire simulation. Markdown tables require manual transcription; CSV doesn't.

---

## Tier 1 — Blocking: unblocks real calibration

Without these three answers, the Python model runs on assumptions (initial stock derived from baseline steady-state math, loyal retention assumed at 91%). With them, the simulator becomes honest.

### 1.1 Current active-user stock by tenure

**File to fill:** `porygon-data-templates/1.1-stock-by-tenure.csv`

**What we need:** Of today's ~1,677 monthly active users, how many fall into each *tenure-since-activation* bucket? Same breakdown for the ~447 registered-but-never-activated passive viewers (tenure from registration instead).

**Expected columns:**

| column | description |
|---|---|
| `population` | `activated` or `passive` |
| `tenure_bucket` | `0-1m`, `1-3m`, `3-6m`, `6-12m`, `12-24m`, `24m+` |
| `n_users` | count in bucket (current snapshot, e.g. April 2026) |
| `definition_of_active` | your chosen definition; e.g. `summary_created in last 30d` or `app_open in last 30d` |
| `caveats` | any data quality notes |

**Why:** The Python simulator starts from today's actual stock. Without this breakdown, it uses a geometric distribution consistent with r₁/r₂ — which is exactly the assumption we're trying to replace.

---

### 1.2 Cohort retention matrix

**File to fill:** `porygon-data-templates/1.2-cohort-retention.csv`

**What we need:** For each monthly *activation cohort* from Jan 2025 → Mar 2026 (14 cohorts), what fraction was still active at tenure month 1, 2, 3, 4, 5, 6, 9, 12, 18?

**Expected columns (long format):**

| column | description |
|---|---|
| `activation_cohort_month` | `2025-01`, `2025-02`, ... `2026-03` |
| `tenure_month` | integer, months after activation: `1, 2, 3, 4, 5, 6, 9, 12, 18` |
| `n_cohort_start` | size of the original cohort at month 0 (same for all rows of one cohort) |
| `n_still_active` | users from the cohort active in that tenure month |
| `survival_fraction` | `n_still_active / n_cohort_start` |
| `definition_of_active` | one of `summary_created`, `app_open`, or `either`; please pick one and be consistent |
| `caveats` | e.g. `cohort 2026-03 has only 1 month of history — tenure ≥ 2 N/A` |

**Why:** Gives us the per-tenure retention curve S(τ). The simulator replaces its two-tier r₁/r₂ with the fitted curve. Also lets us see whether retention *flattens* at long tenures (the key assumption protecting existing MAU) or keeps decaying.

---

### 1.3 Loyal-tail retention rate

**File to fill:** `porygon-data-templates/1.3-loyal-tail-retention.csv`

**What we need:** For users with 12+ months of tenure, what is the observed *month-to-month* retention rate? Split by two sub-buckets: 12–24m and 24m+.

**Expected columns:**

| column | description |
|---|---|
| `tenure_bucket` | `12-24m` or `24m+` |
| `month_pair` | `2025-10→2025-11`, `2025-11→2025-12`, ... — you choose the windows |
| `n_active_start` | active at start of month_pair |
| `n_still_active_end` | active at end of month_pair |
| `retention_rate` | `n_still_active_end / n_active_start` |
| `caveats` | e.g. sample size warnings |

**Why:** This single number (loyal-tail retention) determines how fast the oldest cohorts decay. v2 implicitly assumed everyone decays at r₂ = 66% forever, which is why inflow drops looked catastrophic. Observed loyal retention of ~90% would dampen the collapse dramatically. We hypothesize ~91% based on earlier conversation — validate or correct.

---

## Tier 2 — Sharpens the model; v3.1 / v4 needs these

### 2.1 Growth-accounting decomposition (Jonathan Hsu / Social Capital style)

**File to fill:** `porygon-data-templates/2.1-growth-accounting.csv`

**What we need:** For each of the last 12 months, decompose MAU into flows.

**Expected columns:**

| column | description |
|---|---|
| `month` | `2025-05`, `2025-06`, ... `2026-04` |
| `new` | first-time active users in this month (never active before) |
| `resurrected` | active this month, inactive last month, active in some earlier month |
| `retained` | active this month AND active last month |
| `churned` | active last month, NOT active this month |
| `MAU_total` | total MAU that month = new + resurrected + retained |
| `quick_ratio` | `(new + resurrected) / churned` |
| `caveats` | notes |

**Why:** Lets us back-check the simulator's flow predictions against observed flows month-by-month. Also surfaces whether the model's one-way retention (no resurrection) is missing meaningful users.

---

### 2.2 Passive-viewer retention curve

**File to fill:** `porygon-data-templates/2.2-passive-retention.csv`

**What we need:** Of users who are *registered but have never activated* (the 447 passive), what fraction persist as summary-viewing users after 1, 2, 3, 6, 12 months from registration?

**Expected columns (same long-format shape as 1.2):**

| column | description |
|---|---|
| `registration_cohort_month` | `2025-04`, ... `2026-03` |
| `tenure_month` | `1, 2, 3, 6, 12` |
| `n_cohort_start` | count of registered-never-activated users in the cohort |
| `n_still_viewing` | from the same cohort, how many viewed a summary this tenure month |
| `survival_fraction` | ratio |
| `definition_of_viewing` | e.g. `summary_viewed OR shared_summary_opened` |
| `caveats` | notes |

**Why:** v2/v3 treats passive users as a flat multiplier of activated. Reality is probably non-flat — passive viewers may churn faster (no value) or slower (Care Circle utility from viewing). Changes how we value Care Circle features.

---

### 2.3 Install trend and seasonality

**File to fill:** `porygon-data-templates/2.3-installs-weekly.csv`

**What we need:** Weekly installs for the last 18 months, blended and per-platform.

**Expected columns:**

| column | description |
|---|---|
| `week_starting` | `YYYY-MM-DD` (Monday) |
| `installs_total` | blended count |
| `installs_ios` | platform split |
| `installs_android` | platform split |
| `installs_ipados` | platform split |
| `caveats` | e.g. `Adjust attribution broken from 2025-08-15 onward` |

**Why:** Our 5,000/month baseline assumes flat inflow. If there's trend or seasonality, the baseline trajectory shouldn't be flat either. Also: gives us a real series to fit if we later move to a BSTS / MMM approach.

---

### 2.4 Per-Life-Moment retention split (if feasible)

**File to fill:** `porygon-data-templates/2.4-life-moment-retention.csv` (only if feasible)

**What we need:** Can cohort retention (1.2) be split by Life Moment — cancer / neurodegenerative / expecting parents / chronic disease / other?

**Expected columns:** Same as 1.2 plus one extra column:

| column | description |
|---|---|
| `life_moment` | `cancer`, `neuro`, `parents`, `chronic`, `other`, `unknown` |
| ...rest identical to 1.2 | |

**Feasibility routes** (pick whichever works; document which you used):
- (a) Onboarding intent question — if it's a Mixpanel user property
- (b) Customer.io segment membership
- (c) Summary-content classification (heavier lift, may require retroactive classifier run)
- (d) Manual classification of a sample of ~200 users if (a)–(c) aren't available

**If this requires a new project rather than a query, flag it as "not feasible with current tracking" and we'll defer to v4.**

**Why:** Context doc says Life Moments "likely differ significantly in retention." If cancer patients retain at 80% while expecting parents retain at 40%, the blended 54% cliff is hiding two completely different dynamics. Changes strategy.

---

## Tier 3 — Later-version refinements (not needed for v3)

These feed into v4+. Include if the data is easy to pull; otherwise skip.

### 3.1 Care Circle loop latency

**File to fill:** `porygon-data-templates/3.1-invite-latency.csv`

**Expected columns:**

| column | description |
|---|---|
| `event` | `invite_sent → install` or `invite_sent → activation` |
| `days_bucket` | `0-1`, `1-3`, `3-7`, `7-14`, `14-30`, `30-60`, `60-90`, `never_within_90d` |
| `n_events` | count |
| `fraction` | % of all invite_sent in this bucket |
| `caveats` | notes |

**Why:** v3 currently treats K as instantaneous. If typical latency is ~14 days install + ~21 days activation, the loop has real lag that affects transient dynamics (but not asymptote).

---

### 3.2 Invite rate by tenure

**File to fill:** `porygon-data-templates/3.2-invite-rate-by-tenure.csv`

**Expected columns:**

| column | description |
|---|---|
| `tenure_bucket` | `0-1m`, `1-3m`, `3-6m`, `6-12m`, `12m+` |
| `n_active_users` | active users in this tenure bucket (30-day snapshot) |
| `n_invites_sent` | invites sent by users in this bucket in the same 30 days |
| `invites_per_user` | `n_invites_sent / n_active_users` |
| `invite_rate` | fraction of users in bucket who sent at least one invite |
| `caveats` | notes |

**Why:** If invites are front-loaded in tenure 0–3m, the Care Circle loop effectively dies for long-tenure users. Matters for how Care Circle v2 lift compounds with retention lift.

---

### 3.3 Non-activated-viewer source split

**File to fill:** `porygon-data-templates/3.3-passive-source.csv`

**Expected columns:**

| column | description |
|---|---|
| `source` | `care_circle_invite` or `direct_install_no_activate` |
| `n_users` | count |
| `fraction` | % of total passive (should sum to 100%) |
| `caveats` | notes |

**Why:** Tells us whether "activate more" or "invite more" is the lever that protects passive MAU.

---

## Delivery notes

- **Preferred format:** Fill in the CSV templates in `porygon-data-templates/` and return them as attachments (or paste in a reply). The Python model will `pandas.read_csv()` each one directly.
- **If a CSV can't be filled** (event missing, tracking broken, query infeasible), leave the rows blank and put the reason in the `caveats` column of the first row. That's better than guessing or silence.
- **Privacy:** All aggregate counts, no user-level data. If N ≤ 5 in any cell, please suppress (leave blank) or roll up to a larger bucket.
- **Definitions:** When a CSV has a `definition_of_active` column (1.1, 1.2, 2.2), please pick one definition per file and keep it consistent across rows.

## Flagging back

Please include a short "Questions / caveats" paragraph at the top of your response if:
- Any column definition is ambiguous (ask before guessing)
- A date window or event is unavailable (tell us what's reliable from when)
- You spot something in the data that contradicts what the model assumes (e.g., "your model assumes registration rate has been stable, but actually it dropped from 42% → 35% between Jan and Apr 2026")

---

## What happens next (for Mewtwo, not Porygon)

Once Tier 1 CSVs land:
1. `model/calibration.py` reads them, replaces synthetic initial stock + three-tier retention with real fitted values
2. `model/main.py` re-runs baseline + stress tests; outputs updated trajectory PNGs
3. README.md changelog updated with "calibrated against real data as of <date>"
4. If Tier 2 lands, growth-accounting decomposition added as a secondary output
5. Tier 3 feeds into v4+ (Markov with invite-latency, per-tenure K)
