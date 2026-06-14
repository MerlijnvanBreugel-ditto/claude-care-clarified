# /measure-feature

> Given a refined epic, generates 3 measurement Jira tickets: business metrics with baselines/targets, a tracking plan with event catalog, and an implementation spec that blocks release until verified.

## Usage

```
/measure-feature [epic key or spec path]
/measure-feature DPMA-1964
/measure-feature --from=pm-workspace/specs/care-circle-v2.md
```

## What It Does

1. Loads `pm-workspace/context/product-context.md`
2. Reads `pm-workspace/workflows/feature-measurement.md`
3. Checks registry for related artifacts
4. Loads the epic spec (from Jira or file path)
5. Extracts problem, segment, success criteria, classification
6. Generates business metrics (with Mixpanel baseline lookup)
7. Generates tracking plan (events, properties, dashboard spec)
8. Presents both for Merlijn's approval
9. Creates 3 Jira tickets under the epic
10. Updates registry
11. Offers feedback prompt

## $ARGUMENTS

Epic reference or spec file path. Examples:
- `DPMA-1964` (Jira epic key)
- `--from=pm-workspace/specs/care-circle-v2.md`
- `"Onboarding to Aha epic"`
