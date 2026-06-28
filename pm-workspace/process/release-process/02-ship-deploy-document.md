# Phase 2 · Ship — Deploy & document

The release goes out and gets written down in the same motion. A release that isn't documented didn't happen, as far as the rest of the company is concerned.

## Cadence

Backend releases go out weekly, Friday afternoon. Releases are rolling, not batched into fixed trains, so velocity stays high. Larger or riskier changes ship behind a feature flag and are exposed when ready (see Phase 1).

## Auto release entry in Linear

After each deployment, a release entry is created automatically in Linear ("Linear releases"). This is the single source of truth for what shipped and when. Everything downstream (the Slack post, the weekly digest, the user comms) reads from it, so the entry has to be accurate.

## App-store release notes

Written in both EN and NL, before deploy, never after. Lead with the benefit, not the feature name.

```
EN
We regularly update Ditto to make our app and your experience better. This release includes:
What's new:
• [Improvement in benefit language]
• Bug fixes and performance improvements
Everyone deserves clarified care. Like Ditto? Leave us a review!

NL
We werken Ditto regelmatig bij om de app beter te maken. Deze update bevat:
Wat is er nieuw:
• [Verbetering in benefit language]
• Bugfixes en prestatieverbeteringen
Iedereen verdient heldere zorg. Ben je blij met Ditto? Laat een recensie achter!
```

Writing guidelines: lead with benefit, one line per bullet, always include the catch-all bug-fixes line, always end with the review CTA.

## Mixpanel annotation

Major releases get a Mixpanel annotation on the day they ship, so later metric shifts tie back to a specific release. This is part of the release checklist, not an afterthought.
