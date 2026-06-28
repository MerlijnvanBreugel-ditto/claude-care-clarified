# Release Process

> Parent page. Restructures the existing "Shipping & Release" page into an overview plus four phase subpages.

**Released ≠ Done.** Done = users know, users use, impact validated.

This tree covers the product side of shipping: getting a change ready, releasing it, and making sure the team and our users know it happened. The engineering mechanics (branching, PRs, CI, deploys) live in [Ways of Working](https://dittocare.atlassian.net/wiki/spaces/DP/pages/219512846) and [Code changes quality](https://dittocare.atlassian.net/wiki/spaces/DP/pages/480641033). Post-launch evaluation (Week 1/2 checks) lives in Experimentation & Learning.

## The four phases

| Phase | Question it answers | Owner |
|---|---|---|
| **1 · Before — Quality gate** | Is this safe and measurable enough to ship? | Product + Engineering |
| **2 · Ship — Deploy & document** | Is it live, and is it written down? | Engineering |
| **3 · Tell the team** | Does everyone internal know what shipped? | Feature owner |
| **4 · Tell users** | Do users discover and understand it? | Product + Marketing |

```
[Discovery → Go/No-Go] → 1 Quality gate → 2 Ship → 3 Tell the team → 4 Tell users → LEARN
```

## One-page release checklist

Everything that must be true for a release to count as done. Detail lives in the phase subpages.

| # | Must be true | Phase | Owner |
|---|---|---|---|
| 1 | Critical changes reviewed (technical design + IS) | 1 | Eng lead |
| 2 | Success hypothesis + tracking defined and verified | 1 | Product + Growth |
| 3 | Functional spec written (why / what / how) | 1 | Feature owner |
| 4 | QA walkthrough video recorded and posted in Linear | 1 | QA / builder |
| 5 | Rollback path and guardrail metrics written down | 1 | Engineering |
| 6 | Deployed; release entry auto-created in Linear | 2 | Engineering |
| 7 | App-store release notes published (EN + NL) | 2 | Product |
| 8 | Major release annotated in Mixpanel | 2 | Growth |
| 9 | Posted to #releases (auto) and surfaced in weekly digest | 3 | Auto / feature owner |
| 10 | User comms sent per tier (in-app, email where relevant) | 4 | Product + Marketing |

## Why this exists

We have shipped without tracking and lost weeks of evaluation. We shipped Care Circle after a three-week delay and the team did not know it was live. This process fixes both: nothing ships without a way to measure it, and nothing ships silently.

_Process serves velocity. If this doc slows you down, fix the doc._
