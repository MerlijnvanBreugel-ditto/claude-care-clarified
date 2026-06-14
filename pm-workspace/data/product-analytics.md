# Ditto Care — Product Analytics Snapshot

> As of 2026-05-30. Source: Slack #insights, Porygon (Mixpanel analytics agent), April–May 2026.
> This is the living key-figures reference. Refresh it after each major Porygon pull.
> Every number is dated. Read the **Data caveats** section before quoting anything externally; several core metrics are definition-dependent or instrumented imperfectly.

## How to read this

- **Core MAU** = unique users who view ≥1 summary in a trailing 30-day window (event: `summary_viewed`). This is the North Star, not the cumulative "35,000+ users" vanity figure.
- Porygon switched its source to the Ditto Mixpanel project (4011597) on ~Apr 21, which reset baselines. The daily auto "Conversion" report stopped after May 1; later headline values come from ad-hoc thread answers.
- A mid-April Mixpanel project migration broke user identity for part of the late-April cohorts. Numbers spanning Apr 10–27 are softer than they look.

---

## 1. North Star — Core MAU

| Date | Core MAU | Note |
|---|---|---|
| Mar (plan baseline) | 1,381 | start of Q2 monthly plan |
| 30 Apr (Apr close) | 1,714 | +18.5% MoM |
| 1 May | 1,716 | 51% of May target path |
| 5 May | 1,771 | |
| 18 May | 1,938 | |
| 19 May | crossed 2,000 | |
| 21 May | 2,031 | +21% vs 30d earlier |
| 22 May | **2,086 (all-time high)** | |
| 26 May | 2,035 | |
| **27 May** | **~2,080 (LATEST)** | +1.7% WoW |

- **Target:** 5,000 by Jun 30 ("the signal, not the goal"); 50,000 year-end = Series A milestone.
- **Q2 monthly path:** Mar 1,381 → Apr 2,058 → May 3,066 → Jun 4,568.
- **Pace:** ~45% of the May 4,568 path at May 27; roughly 36% behind Q2 pace. Net new is ~80–160 MAU/week vs the ~440/week required. This gap is what triggered the Code Red (May 21).
- **Caveat:** the MAU report tracks `summary_viewed` despite some labels reading "summaries created."

---

## 2. Acquisition

| Metric | Value | Window | Caveat |
|---|---|---|---|
| Daily organic intake | **~120/day (LATEST)** | 7d to 27 May | clean Adjust=Organic read |
| Organic trend | Mar ~264/d → Apr ~201/d → May ~138/d | monthly avg | averages include media spikes; baseline ~120–140/d |
| Organic decline | **~54% Mar→May** | — | driven by paid shutdown + lost halo |
| Total installs (clean baseline) | ~178/day | 7d to 27 May | |
| Total installs (7d) | 1,181–1,249 | to 27 May | two reads differ |
| Monthly installs | Mar 7,673 → Apr 10,701 → May ~7,061 | — | April inflated by media |
| Download → registration | **~53–54% (LATEST daily)** | May | |
| Registration-rate trend | Mar 15% → Apr 46% → May 53% | — | ~4× improvement |
| Install → summary_viewed (end-to-end) | Mar 2.0% → Apr 4.3% → **May 7.0%** | — | |

**Channel mix (May, Adjust, n≈3,759):** No-consent (ATT opt-out) 52% · Organic 27% · ditto_website 7% · care-circle/viral 5% · Apple Search Ads 2% · partnership 2% · NL newspaper 1% · UK advertorial 1% · Google Ads ~0. True organic estimated ~75–80% of installs.

**Paid spend:** only Apple Search Ads is live (~€1,400/week for ~3 installs/day, CPI ~€8–9). All other paid (Meta, Google) at €0 since April (consumer paid parked under the B2B-only decision).

> **Cost per MAU (April, €70K assumed):** Porygon failed to produce this number. Open data request.

---

## 3. Activation

The activation engine, not acquisition, is the binding constraint.

| Metric | Value | Window | Caveat |
|---|---|---|---|
| **D14 activation** (install → summary_viewed, 14d) | **~6–8% blended (LATEST)** | May | depressed by media spikes |
| D14, organic install-based | ~13% | Apr14–May4 | |
| D14, register-based (mature) | ~27–28% | — | the "good cohort" number |
| D14 by channel | care circle 30% · organic 13% · partnership 13% · Apple SA 12% | Apr14–May4 | |
| Register → summary conversion | ~14–15% | May | flat pre/post skip change (no dilution) |
| Time-to-value (register → first summary) | 55.1h → 29.6h (−46%) | post Customer.io | |
| Onboarding intent step completion | 68% select an intent, 32% skip | May 21 (n=1,577) | |

**Target:** D14 = 25%.

**Onboarding persona split (n=1,577, May 21):** Own care 76% · Other 6.4% · Professional caregiver 5.8% · Loved one 4.9% · Expecting 4.2% · HCP 2.7%.
**Top intents (n=497):** appointment summaries 63% · explain medical letters 36% · medical overview 35% · share with family 28% · understand condition 28%.

**Skip-button removal experiment (v1.9.7/1.9.8, shipped ~May 14, ticket PRO-424):**
- Install → registration: 46% → **55% (+9pp)**.
- Onboarding completion (from install): 39% → **48% (+9pp)**.
- Register → activation quality: 14% → 14% (no dilution — the key de-risking result; forcing registration did not lower user quality).
- Avg time to register: 3.8h → 2.5h (−35%).
- Net D14 lift only ~+1.3pp install-based: registration was never the main barrier.

### The manual-appointment → summary gap (the "~55% gap")
- Manual appt → summary conversion: **~30% (flat, no upward trend)** over 60d (Mar 10–May 8); 70% never reach a summary.
- 68% of registered users never create any appointment; only ~19% add a manual one.
- **The gap is concentrated in first-time users.** Manual appt → summary by segment (Oct'25–May'26):
  - First-timers **7%** (~5× worse than baseline) · baseline 33% · experienced 36% · oncology **69%** · prior-summary creators **69%** · care-circle sharers **70%**.
- Implication: care-circle sharing and a prior summary are the strongest predictors of conversion. The lever is getting first-timers their first summary, not more appointments.

---

## 4. Retention (the leaky bucket)

**Retention is entirely definition-dependent. Do not quote a single "retention number" without saying which one.**

| Definition | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| **M0 within-month** (views 2+ summaries in 30d) | — | — | — | — | — | — |
| Next-month, summary_viewed → summary_viewed | ~40% | ~30% | ~22% | ~14% | — | — |
| Deep creation (summary → summary, post-creation) | 28% | 23% | 19% | 14% | 10% | 3% |
| Light (opens app, post-creation) | 50% | 43% | 36% | 27% | 19% | — |

- **M0 within-month: ~78–79%** (range 73–86%). This is what made KR4 look "above target." It measures repeat views inside a 30-day window, not next-month return.
- **M1 next-month (the meaningful one): ~38–42%** for mature Dec–Feb cohorts. KR target is 60%, so we are **~18pp below** on the definition that matters. (The Mar cohort's "25%" is a migration undercount, not a real drop.)
- **Summary viewers retain ~1.6× better** than app-openers (summary→summary 39% vs app-open→app-open 24%, May 18).
- **Care-circle recipients (followers):** loyal openers (light M1 87%) but almost never create their own summary (deep M1 15%). This "15%" is likely the source of the "~15% Deep Red" figure circulating elsewhere; it is the follower deep-creation number, not blended M1.
- **Channel composition hurts the blend:** newspaper cohorts retain at M0 ~50% vs organic ~80%; broad paid spikes dilute blended retention 5–10pp.
- **Single-summary cliff:** 51% of summary creators make only one summary ever (Oct'25–May'26, n=5,028); ~10% are power users (6+). The ~2,500 single-summary users are the biggest retention opportunity.
- **Reactivation is real and episodic:** at M4 post-summary, 27% open the app but only 14% create. ~25% of activations happen after day 14 (consistent with ~8-week hospital cycles), so single-window activation undercounts true value.

**Target:** M1 retention 60%.

---

## 5. Care Circle (the designated growth loop)

| Metric | Value | Window | Caveat |
|---|---|---|---|
| **Avg circle size**, activated patient MAU with a circle | **1.62 (LATEST)** | 22 May | penetration 12.7% (922/7,284) |
| Avg members added per user | 1.44 | since Mar'26 | canonical `care_circle_member_added` |
| Avg circle size, cancer/oncology patient | ~1.8–2.0 | 22 May | directional; 20% penetration (1.8× non-oncology) |
| Patients with ≥1 follower | **12.7% of patient MAU** | 22 May | 5.1% of all registered |
| Invites sent | 1,758 from 1,125 unique users | 1–27 May | NL 1,706 / UK 23 |
| Invite → follow conversion | **~33% (90d)** | 28 May | ~71% of invites never become a follow request |
| Acceptance (monthly, inviter-level) | 28% of inviters land someone | May | 673 accepted, +34% MoM |
| Members added | 663 across 445 circles | 1–27 May | +33% MoM |
| Members viewing summaries | 1,585 views by 320 unique followers (5.0/follower) | 1–27 May | +79% views MoM |
| Members creating summaries | 9.7% of new joiners | May | still maturing |
| **Target** | **3.4 members** | KR3 | far off; measurement broken (PRO-290) |

**Care Circle V2 compounding (May 13):** follower → creator 22% · follower → inviter 22% (avg 12h after accepting) · 2nd-generation invites grew 6× (9 → 54/week) · `carecircle` install link 0 → 50 installs/week at 93% registration (highest-converting channel). **Viral coefficient K ≈ 0.08–0.10 (up from ~0.05, still < 1)** — the loop compounds but does not yet self-sustain.

**What matters for circle growth:** first-joiner type (patient vs carer) makes no real difference (1.57 vs 1.46). What matters 2.3×: followers who find the owner organically (join request) reach 2+ members at 25% vs invite/deep-link at 11%.

> **"Choose what to share" customization rate is currently UNKNOWN.** Porygon's "0%" answer was fabricated (it invented payload fields that don't exist; the event lacks them). Tracked under PRO-476.

---

## 6. Content, sources & personas

| Metric | Value | Window |
|---|---|---|
| Total summaries created | **2,714** | 30d to 21 May |
| Unique summary creators | 1,521 | 30d to 21 May |
| Source split | **recording 58% · doc-scan 41% · translation 1.2% · QR <0.1%** | 30d |
| summary_viewed events | Apr 7,050 (1,756 users) → May pacing ~10,100 (+39%) | — |
| source = 'juvoly' | 0 in-app events | — (juvoly is a B2B attribution channel, not an in-app source) |
| Per-user intensity | doc scanners ~2.1 summaries/user vs recording ~1.5 | 30d |

**Disease-area mix (recording-based, categorized; ~29% coverage since `summary_categorized` launched ~Apr 27):** Oncology **24.6% (#1)** · Cardiology 11.3% · Orthopedics 10.5% · Neurology 8.6%. Top 4 = 55%. Care setting: hospital/specialist 64% · GP 24% · home care 4%. (Roughly **~50% of active users are cancer patients** per the product-context lens.)

**Oncology persona vs non-oncology (Apr 27–May 20, n=849 categorized, 250 oncology) — the product-market-fit wedge:**
- Summary viewed 86% vs 80%; time-to-first-view 3.9h vs 6.8h (43% faster).
- Re-record rate 31% vs 22%; **week-1 retention 39% vs 18% (>2×)**.
- **Care-circle invite accepted 18% vs 10% (1.8×)** — oncology has the highest care-circle acceptance of any domain.

**Record day (12 May):** 566 `summary_viewed` events / 232 unique users (driven by a 717-install day plus faster product conversion).

**Appointment sharing to care circle:** 899 shares / 341 patients (30d); ~30–33% shared *before* the appointment date; lead-time of preparation shares >72h for 69%; **85% of summary creators re-share to the same circle** (~23h later) — a healthy internal loop.

---

## 7. Feature & experiment readings

| Feature (status) | Reading | Caveat |
|---|---|---|
| **Customer.io** (live Apr 25) | Care-circle invites +59% vol, manual appts +76% vol vs baseline; time-to-first-summary 55.1h→29.6h (−46%); register→summary flat at 15.1% | directional, not A/B'd; **push delivery broken** (374 attempted, 7 delivered = 1.9%, PRO-319) |
| **Discover tab** | 22% of installs view (1,933); 80% tap a card; viewers create summaries 14% vs 5% baseline | lift mostly self-selection, not causal |
| **Calendar sync** (GA ~May 30, v1.9.9) | 25% end-to-end adoption; 86% of calendar-event adders then create a manual appt | flagship activation bet; widens the funnel beyond appointments |
| **Notification center / inbox** | ~8% open rate (7.6%), 46% click-through among openers | doubled since Feb |
| **Profile pages** | supply broken (0.3% fill rate) but demand healthy (465 follower-viewers, +6.5× since launch) | "empty shopfront" |
| **Anonymous recording** (no account, PRO-321) | only ~6.1% of recorders are anonymous (71, Apr21–May11) | supports forcing login; earlier "32%" was a migration artifact |

---

## 8. Geography & partners

**UK launch (Times advertorial, May 23):** 194-download cohort · registration 62% (above NL ~55%) · 30 manual appts (67% future-dated) · 5 users / 8 summaries viewed so far (too early). UK vs NL: registration UK 62% vs NL 52%, but recording adoption NL 19% vs UK 9% and recording→summary NL 62% vs UK 31%. UK O1-KR3 target: 100 UK MAU + 2 referring B2B partners outside NL.

**Partner installs (Q2 to date, Apr 1–May 22, all €0):** 270 via `nl_partnership` — Menzis 153 · Hartklinieken 61 · Ikazia 26 · Huisartsenopleiding 14 · Zorgict 9 · MUMC 5 · Juvoly 2. KR1 target is 2,000 registrations. Three partners went dormant in May. Partner attribution is the named blocker (`adjust_network=nl_partnership` largely returns 0; most partner traffic lands as "organic").

**Pregnancy postcard test (May 19–25, 2,000 cards, €0):** QR scan ~30% → ~72 installs (87% reg rate), 114 "expecting" onboardings (28× baseline rate), higher manual-appt and care-circle invite rates — **but 0% summaries / 0% summary_viewed**. Strong top-of-funnel, broken activation chain (people document past appointments retroactively, with nothing to record).

---

## 9. Q2 OKR scorecard (vs Porygon readings)

| KR | Owner | Target | Latest reading | Status |
|---|---|---|---|---|
| O2-KR1 partner registrations | Bart | 2,000 (Q2) | 270 partner installs to date; attribution largely unmeasurable | offTrack |
| O2-KR2 D14 activation | Niek | 25% | ~6–8% blended / ~13% organic / ~27–28% register-based | atRisk |
| O2-KR3 avg care circle size | ilayda | 3.4 | 1.62 (rigorous reconstruction) / 1.44 members added | atRisk, measurement broken |
| O2-KR4 M1 retention | Merlijn | 60% | ~40% next-month (the meaningful definition) | offTrack |

Core MAU (the O2 outcome) at ~2,080 (May 27) vs 4,568 May path = ~36% behind pace.

---

## 10. Data caveats (read before quoting)

- **Care circle size is instrumented imperfectly.** `follower_count_after` has been non-numeric since a v1.7.11 payload-wrapping bug; sizes are reconstructed from `care_circle_member_added` (which only tracks from Mar 2026, undercounting older circles). Reported averages diverge (1.44 vs 1.62 vs the 2.5–2.7 seen in earlier daily reports). PRO-290.
- **Attribution (Mixpanel ↔ Adjust) is unreliable.** ~52% of May installs are "No User Consent" (ATT opt-out); organic vs paid cannot be cleanly separated; partner attribution is mostly missing. Flagged "potentially not fixable."
- **Retention is definition-sensitive.** M0 within-month (~78%) vs M1 next-month (~40%) vs deep creation (~28%) vs follower deep (~15%) are all real and all different. State the definition.
- **Mid-April Mixpanel migration** broke identity for part of the late-April cohorts (e.g. ~59% of the Easter cohort untrackable); Apr 10–27 windows are soft.
- **Two known fabrications by Porygon, since corrected:** the "choose what to share = 0%" answer (invented fields, PRO-476) and an early "new onboarding +13pp" read (ran on staging, mistook a 100% rollout for an A/B test). Treat single-shot Porygon causal claims as hypotheses until verified.
- **Daily Conversion reports stopped after May 1**; recent headline figures are ad-hoc thread pulls, so the May time series is sparser than April's.
- **"35,000+ users" is cumulative**, not Core MAU (~2,080). Never conflate.
