# Workflow: Update Product Analytics (from Slack / Porygon)

> Refreshes the key product figures in pm-workspace from the live analytics in Slack #insights (the Porygon Mixpanel agent). Produces/updates `data/product-analytics.md` and reconciles the core-figures into `context/product-context.md`.

## When to Use

- "Update product analytics" / "refresh the figures from Porygon" / "update core figures from Slack"
- Before a strategy session, board update, investor doc, or OKR review
- After a notable spike, launch, or campaign that Porygon has analysed

## Triggers it pairs with

- This is the **figures-from-Mixpanel** half. The broader `product-context.md` refresh also pulls Linear + Granola; run those separately if a full context refresh is needed.

## Where the data lives (don't rediscover this each time)

- Channel: **#insights**, `channel_id = C0A2P2KHGQY`.
- Bot: **Porygon** (`U0AEK67PWGY`). Numbers live in **thread replies**, not the parent question. "Cursor" bot posts corrections.
- Tools: Slack MCP (`slack_read_channel`, `slack_read_thread`; load via ToolSearch). Porygon era ≈ April 2026 → now.
- See memory `reference_porygon_insights.md` for definitions and data traps.

## Steps

### 1. Scope the channel
Page `slack_read_channel` (concise) from now back through the Porygon era. Large pulls overflow context — save to a temp file and parse. Build a **thread index**: `ts | #replies | date | who | question`. Skip chit-chat / operational / duplicate threads.

### 2. Fan out by theme (parallel)
Do NOT read all threads in the main context. Dispatch **parallel sub-agents**, one per theme, each given the channel_id + a curated list of thread `ts`. Themes that worked:
1. Core MAU, OKRs & daily/weekly dashboard time series
2. Retention (by definition: within-month / next-month / deep / follower)
3. Activation & funnel (D14, skip-removal, onboarding intent, manual-appt→summary gap)
4. Care circle (size, invite funnel, V2 compounding, K-factor)
5. Acquisition / channels / geo / unit economics (incl. UK)
6. Usage / content / personas (sources, disease areas, oncology wedge)
7. Features & experiments (Customer.io, Discover, calendar, notifications, profiles)

Each agent prompt must say: read ALL replies per thread, extract **verbatim numbers only (no invention)**, tag each with date + window + caveat, mark the most-recent authoritative value `(LATEST)`, return a tight markdown digest (it is data, not a human message). Use parallel `Agent` calls, or the `Workflow` tool for the fan-out if the user opted into orchestration.

### 3. Synthesize
Pick the most-recent authoritative value for each headline metric. Keep every number **dated and caveated**. Preserve Cursor's corrections over Porygon's originals when they conflict.

### 4. Write `data/product-analytics.md`
Living key-figures reference. Sections: North Star (Core MAU), Acquisition, Activation, Retention, Care Circle, Content/Personas, Features/Experiments, Geo/Partners, OKR scorecard, Data caveats. Header = "As of <date>, source: #insights / Porygon". Tables over prose. No single em dashes.

### 5. Reconcile `context/product-context.md`
Update the "Numbers That Matter" table + OKR notes + data caveats to the dated Porygon reads. Add a pointer to `data/product-analytics.md`. **Flag divergences** between Porygon's raw reads and the official OKR-page figures (especially retention definition and care circle size) rather than silently overwriting — ask Merlijn which is canonical.

### 6. Update registry & close
Update `registry/registry.json` (`ref-007` product-analytics.md `updated` date; bump `last_updated`). Surface: headline table, the divergences to confirm, and open data gaps (e.g. cost-per-MAU, attribution). Then the standard feedback prompt.

## Output
- Updated `data/product-analytics.md` (dated, caveated).
- Reconciled core figures in `context/product-context.md`.
- A short report: headline figures + divergences to confirm + open data gaps.
