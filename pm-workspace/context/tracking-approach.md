# Ditto Tracking Approach

> Status: Placeholder — Merlijn to expand with full documentation
> Last updated: 2026-03-03

Ditto uses a **dual tracking approach** in Mixpanel:

## 1. Granular UI Tracking (General)

Every interactive element (buttons, taps, swipes) is tracked with standardized metadata, payloads, and event data. This is the foundation layer — generalizable, consistent, and automatically applied across the app.

**Naming:** Events use Title Case with feature prefix and dash separator (e.g., `Care Circle - Follow Request Sent`, `Invite Sent`). Properties use `snake_case` (e.g., `request_age_hours`, `invite_channel`).

**TODO:** Document standard properties, payload structure, examples.

## 2. Business Insight Tracking (Specific)

Higher-level aggregate events that capture meaningful business moments. These are purpose-built for specific product questions — not tied to individual UI elements but to user journeys and outcomes.

**Example:** "Onboarding Complete" as a single aggregate event that fires when the full onboarding flow is finished, regardless of which specific screens/buttons were involved.

**TODO:** Document existing business events, aggregation rules, dashboard structure, examples.

## Metrics Framework

The canonical metrics framework lives in a [Google Sheet](https://docs.google.com/spreadsheets/d/19st40l2ZYNNaF5TZ8MXZlssCjmiaJ7cLhYmT36k73ac/edit?gid=1484002407#gid=1484002407) (owned by Niek). It defines:

- **Focus metric:** Monthly Active Users
- **L1 metrics** across Reach, Activation, Engagement, Retention, and Business-Specific (Care Circle)
- **L2 metrics** for funnel step-through, channel quality, and referral loop health

Key events referenced: `consult_summary_created`, `care_circle_member_added`, `invite_sent`, `invite_accepted`, `app_open`.

When defining tracking for new features, map new events back to the L1/L2 metrics they feed into.

---

*When defining tracking for new features (via the [Feature Measurement workflow](../workflows/feature-measurement.md)), both layers need to be considered: which granular events already exist and can be reused, and which new business-level events need to be created.*
