# Phase 1 · Before — Quality gate

Nothing user-facing ships until it is safe to ship and we can tell whether it worked. This phase is the gate.

## Critical-change review

A change is **critical** if it touches medical content, AI output, payments, auth, or anything that could harm a user or break a core flow. Critical changes get a technical design review from the engineering lead before release. AI changes are tested on dev or against transcripts before they go live.

This is our information-security (IS) discipline applied to product: the riskier the change, the more eyes before it ships. Non-critical changes follow the standard PR flow in [Code changes quality](https://dittocare.atlassian.net/wiki/spaces/DP/pages/480641033) and do not need a separate gate.

## Tracking must be in place

Before any feature goes live, all five must be done. If one is missing at release time, the release is blocked. The cost of shipping untracked is always higher than delaying one day to add it.

| # | Check | Owner | When |
|---|---|---|---|
| 1 | Success hypothesis documented, with a measurable target | Product | Before Go/No-Go |
| 2 | Tracking events defined, with property schema | Growth + Eng | During Build |
| 3 | Events verified firing in staging/TestFlight | Engineering | Before QC sign-off |
| 4 | Mixpanel board/insight created for this feature | Growth | Before release |
| 5 | Week 1 + Week 2 check scheduled | Product + Growth | Before release |

## Functional spec

Each feature gets a short functional spec, written at refinement and updated after release. Three things only: **why** we built it, **what** it does, **how** it works. Specs live in the Knowledge Center; the repo specs continue to serve the agents.

## QA walkthrough video

During QA, record a screen walkthrough of every user-facing feature and post it in Linear. No voiceover needed, just click through it so the behaviour is visible. These accumulate into a running library of feature walkthroughs the whole team can browse (see Phase 3).

## Rollback and guardrails

Write the rollback path and the guardrail metrics **before** the release ships, not during an incident. Guardrails are the signals that tell you a release is causing harm. Where possible, separate deploy from release: ship code behind a flag and expose the feature when you choose to. ([Why: deploy ≠ release](https://www.getunleash.io/blog/release-management-best-practices))
