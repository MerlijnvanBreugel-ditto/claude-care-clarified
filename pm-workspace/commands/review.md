# /review

> Without arguments: scans backlog, registry, and learnings for stale items and presents top 5 recommendations. With an artifact: stress-tests it from 6 lenses (User, Dev, Strategy, Growth, Business, Privacy).

## Usage

```
/review                     — Periodic review (backlog, registry, learnings)
/review [artifact]          — Multi-perspective review of a specific artifact
/review --spec=pm-workspace/specs/care-circle-v2.md
```

## Periodic Review

When called without arguments:
1. Scans `pm-workspace/backlog/backlog.json` for accumulated observations
2. Checks `pm-workspace/registry/registry.json` for stale or incomplete artifacts
3. Reviews recent learnings for patterns
4. Presents max 5 prioritized recommendations
5. For each: what, why, suggested next step

## Multi-Perspective Review

When called with an artifact:
1. Loads the artifact
2. Reviews from 6 lenses: User, Mobile Dev, CPO/Strategy, Growth, Business, Privacy/GDPR
3. One sharp paragraph per perspective
4. Flags: 🔴 blockers, 🟡 concerns, 🟢 green lights

## $ARGUMENTS

Nothing (periodic review) or artifact name/path (multi-perspective review).
