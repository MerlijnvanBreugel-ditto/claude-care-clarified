# Citation Index & Confidence Caveats

> Each brief (`briefs/F1`–`F8`) carries its own inline, graded citation list with source URLs. This index holds the grading scheme and consolidates the figures flagged «unverified» across all eight, so nothing weak slips into a deck or board doc unchecked. Created 2026-06-09.

## Grading scheme

- **[P] Primary** — company filings/sites, regulators (EU Commission, BfArM, MDCG), peer-reviewed journals, court records.
- **[S] Secondary** — reputable press, analyst notes, established trade media.
- **[V] Vendor** — company self-report, marketing, PR, single-source aggregators.

Default confidence: P high, S medium, V treat as directional only.

## Re-verify before external use (consolidated «unverified» flags)

| Brief | Claim / figure | Why flagged | Action before external use |
|---|---|---|---|
| F1 | Acquisition prices (Kaiku, Noona, Vinehealth); active-patient & revenue scale (Kaiku, OWise, Outcomes4Me); Visible price/subs | Not disclosed or vendor-sourced | Drop or label as estimate |
| F1 | **"ePRO extends survival"** | Basch 2017 single-centre showed it; **PRO-TECT 2025 (n=1,191) did NOT replicate (OS HR 0.99)** | Do not claim survival. Claim QoL + fewer ER visits (those held) |
| F2 | Finch ~9M DAU and "beats Duolingo D30"; Rosebud mental-health claims; market size $3.2–5.1B | Single analyst / vendor / methodology-dependent | Directional only; not load-bearing |
| F3 | Withings revenue mix; b.well pricing/revenue; b.well "5 partnerships in 5 months" | Secondary blogs / undisclosed / single source | Verify before any quantified claim |
| F4 | TriNetX & Owkin scale/revenue; Lynx.MD EU footprint | Vendor/secondary; Lynx.MD unconfirmed in EU | Directional; Lynx.MD: do not assert EU presence |
| F4 | Finland friction stats | Survey is 2021, pre-reform | Note the reform's effect is not yet measurable |
| F5 | PEPM/PMPM prices; AON "$6M saved" | Not public / partner-reported, single period, net-of-fees unknown | Label as vendor-reported |
| F6 | Rung-2/3 MDR/AI-Act classifications | Directional; MDCG 2019-11 revised June 2025, still settling | Confirm with a notified body before relying on it |
| F6 | Vida ARR, Ada secondary figures, vendor outcome stats | Aggregator/vendor | Directional only |
| F7 | Strava ARR ($163M–$500M range) | Sources disagree widely | Use a range, not a point |
| F8 | Doctolib 80M patients / ~400k providers; DocPlanner 100M / 210k; Kry ~$215M; Doctena/Jameda volumes | Press/aggregator / vendor / 2022-stale / acquisition-era | Label as reported; refresh Kry |

## Ditto-internal figures to confirm (not external sources)

These are estimates used in `C5`/`C6` pending the real numbers (see `synthesis/17` open forks and the metrics list handed to Merlijn): care-circle size (≈1.4 members), daily-share rate (≈0.14%), viral K (≈0.012), and the gating metric **retention by circle size**. Confirm against Porygon (#insights) / Mixpanel definitions before the social bet is sized.

## Per-brief sources

Full graded citation lists live at the bottom of each of `briefs/F1-symptom-tracking.md` through `briefs/F8-operational-front-door.md`. The direction chapters (`directions/C1`–`C6`) cite the briefs rather than re-citing primary sources.
