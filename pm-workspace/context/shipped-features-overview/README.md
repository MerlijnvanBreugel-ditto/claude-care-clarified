# Shipped & Planned — March–May 2026, mapped to OKRs & strategy

**Window:** 2026-03-01 → 2026-05-31 (completed) + Jun–Jul 2026 (planned)
**Source of truth:** Linear, teams **Product (PRO)** + **Agents (AGI)**. Pulled live 2026-05-30.
**Coverage:** 259 completed issues, 61 in-progress issues, 37 active/planned projects. Every row links to its canonical Linear URL.
**Exhaustive data:** [`shipped-mar-may-2026.csv`](./shipped-mar-may-2026.csv) · [`planned-issues-next-2mo.csv`](./planned-issues-next-2mo.csv) · [`planned-projects-next-2mo.csv`](./planned-projects-next-2mo.csv)

## Headline

Q2 was a **foundation quarter**. 46% of everything shipped was Fundamentals (infra, design system, analytics, process tooling), which maps straight to **O1 (build the team, habits & foundation to hyper-scale)**. (AI work — summary quality *and* internal AI agents — is counted under **Clarity**, the AI/intelligence engine, per the current framing.) The growth-loop bets that serve **O2 (5K MAU)** were concentrated in three places: **Care Circle 3.0** (Connection, O2-KR3), **Calendar Integration + Customer.io lifecycle** (Convenience, O2-KR2), and **AI summary quality + Appointment Prep** (Clarity, O2-KR4). The AI feature-stack deepened on two fronts: the **Conversation Explainer pipeline** (provider failover, Gemini fallback, eval/guardrail rework) and a brand-new **Agents team** running an autonomous B2B-outreach cascade (O1-KR2). A third of all issues (87) were quality/BAU work with no direct KR. That is normal for a pre-Series-A team, but it is worth seeing in the open.

## How to read this (method + caveats)

- **Grounded facts** (ID, title, link, project, milestone, release tag, completion date) come verbatim from Linear's API.
- **OKR column** is taken from Linear's own project→KR linkage where it exists (`Linear-linked` / `Project-mapped`). Where Linear has no linkage, it is `Inferred` from theme, or marked **`—` (BAU/foundational)** when the work genuinely serves no single KR. The `OKR_link` column tells you which, so nothing is dressed up as strategic that isn't.
- **Strategy pillar** (Clarity / Connection / Convenience / Fundamentals) is a judgment lens applied on top of the facts. Re-bucket freely in the CSV.
- **Effort** (XS/S/M/L) is heuristic. Linear has no story points, so it is derived from lead time (started→completed) plus scope signals (Feature label, `[IMPLEMENT]` tickets). Treat as a t-shirt size, not hours.
- **Two known gaps.** (1) The Product team migrated to Linear ~Mar 27, so March's big app releases (1.8.0–1.8.2: Care Circle V2 core, invitation flow, reactions) live in **Jira (DPMA)**, not here. Documented separately in [`../shipped-features-overview.md`](../shipped-features-overview.md). (2) Partnerships/Marketing/Operations teams are excluded by scope (Product + Agents only). Say the word and I pull either in.

## The big picture

### By strategy pillar
| Pillar | Issues | Share | Effort split (L/M/S/XS) | What it covers |
|---|---|---|---|---|
| **Fundamentals** | 120 | 46% | 11 / 20 / 79 / 10 | Infra, design system (LEGO/Liquid Glass), analytics, privacy/GDPR, process tooling |
| **Convenience** | 61 | 23% | 8 / 19 / 32 / 2 | Calendar, Customer.io lifecycle, Discover tab, onboarding/activation, FTUE |
| **Clarity** | 46 | 17% | 11 / 4 / 27 / 4 | AI summary quality, Conversation Explainer pipeline, appointment-prep questions, **internal AI agents** |
| **Connection** | 32 | 12% | 7 / 3 / 18 / 4 | Care Circle 3.0, invites, sharing, multi-profile |

> AI = Clarity. Both AI summary quality and the internal AI-agents work are mapped to Clarity (the AI/intelligence engine), per Merlijn's call 2026-05-30.

### By OKR (primary contribution)
| OKR | Issues | Grounded in Linear? | Note |
|---|---|---|---|
| **O2-KR2** D14 activation | 56 | 29 linked/mapped, 27 inferred | Calendar + Customer.io + Discover + website lead-gen |
| **O2-KR3** care circle size | 34 | 25 linked/mapped | Care Circle 3.0, invite-friction removal, multi-profile, Auth0 migration |
| **O2-KR4** M1 retention | 33 | 25 linked/mapped | AI quality, appointment prep, Survicate, persona analytics |
| **O2-KR1** partner regs | 4 | 4 mapped | HCP persona + B2B experiment projects |
| **O1-KR2** 15 FTE AI agents | 26 | 23 linked/mapped | B2B outreach cascade + Triage/RISCE AI + agent POCs |
| **O1-KR4** Proposal & Eval discipline | 13 | 8 linked | Experiment velocity, ship-at-80, analytics foundations |
| **O1-KR3** UK + 2 referring partners | 6 | 2 mapped, 4 inferred | UK launch prep, localization |
| **— (BAU / foundational)** | 87 | n/a | Bug fixes, polish, infra, internal ops, content. No direct KR. |

### By investment type
| Type | # | Type | # |
|---|---|---|---|
| Bug fix | 39 | Analytics/tracking | 15 |
| Team/internal ops | 26 | Infra/platform | 14 |
| AI agents | 26 | Process/tooling | 13 |
| Research/discovery | 21 | Compliance/privacy | 12 |
| Lifecycle/CRM | 20 | AI quality | 10 |
| Design system | 17 | Improvement | 9 |
| New feature | 16 | Content / B2B ops / Release / Polish / Maint. | 21 |

Monthly: **Mar 2 · Apr 112 · May 145** (March low because Linear adoption started late March).

## High-level categorization — by project (the "what shipped" view)

Each project rolls up its completed issues. OKR source in parentheses: `Line` = Linear-linked, `Proj` = project-mapped, `None` = BAU.

| # issues | Pillar | OKR | Project (→ Linear) | Window |
|---|---|---|---|---|
| 18 | Connection | O2-KR3 (Line) | [Care Circle 3.0](https://linear.app/ditto-care/project/care-circle-30-55ab95ddb320) | Apr 16–May 22 |
| 18 | Clarity | O1-KR2 (Proj) | B2B Outreach POC (Agents) — autonomous outreach cascade | May 22 |
| 11 | Fundamentals | — (None) | [UI / LEGO maintenance](https://linear.app/ditto-care/project/ui-lego-maintenance-897e0e77f9de) | Apr 7–May 28 |
| 11 | Convenience | O2-KR2 (Line) | [Calendar Integration](https://linear.app/ditto-care/project/calendar-integration-d7be6e880b53) | Apr 9–May 30 |
| 8 | Convenience | O2-KR2 (Proj) | [Dedicated Discover Tab](https://linear.app/ditto-care/project/dedicated-discover-tab-bd005ca0f7de) | Apr 2–May 12 |
| 8 | Fundamentals | O2-KR4 (Line) | [Implement Survicate](https://linear.app/ditto-care/project/implement-survicate-76685d419334) | Apr 16–May 13 |
| 7 | Convenience | O2-KR2 (Proj) | [Customer.io — Marketing Automation & Push](https://linear.app/ditto-care/project/customerio-marketing-automation-and-push-notifications-83a3b426ab1f) | Mar 31–Apr 16 |
| 7 | Clarity | O2-KR4 (Proj) | AI Quality — Tune Evals and Guardrails | Apr 13–May 21 |
| 7 | Fundamentals | — (None) | [Growth: Team Way of Working](https://linear.app/ditto-care/project/growth-team-way-of-working-wow-38f78290ccf8) | May 8–27 |
| 5 | Fundamentals | O2-KR4 (Line) | [Improved analytics on personas / life moments](https://linear.app/ditto-care/project/improved-analytics-data-on-personas-and-life-moment-audiences-203ad2e547fc) | Apr 15–May 22 |
| 5 | Fundamentals | O1-KR4 (Line) | [Analytics Foundations](https://linear.app/ditto-care/project/analytics-foundations-807340995185) | May 26–28 |
| 4 | Clarity | O1-KR2 (Line) | [15 FTE AI agents](https://linear.app/ditto-care/project/15-fte-ai-agents-93ca13ac7cba) | May 22–28 |
| 3 | Convenience | O2-KR2 (Line) | [Website \| lead generation pages](https://linear.app/ditto-care/project/website-or-lead-generation-pages-d58e1e8ad7ae) | Apr 14–15 |
| 3 | Clarity | O2-KR4 (Line) | [Appointment Preparation](https://linear.app/ditto-care/project/appointment-preparation-96ae98bcaa31) | May 8–20 |
| 3 | Fundamentals | O1-KR4 (Line) | [Ship at 80%: Experiment Velocity Engine](https://linear.app/ditto-care/project/ship-at-80percent-experiment-velocity-engine-411f3367198c) | May 28–29 |
| 2 | Fundamentals | O2-KR3 (Line) | [Migrate Away from Auth0](https://linear.app/ditto-care/project/migrate-away-from-auth0-946ffdc58304) | Apr 20–May 4 |
| 2 | Fundamentals | — (None) | [Move to Liquid Glass UI (iOS 26+)](https://linear.app/ditto-care/project/move-to-liquid-glass-ui-ios-26-0099644d4380) | Apr 9–May 4 |
| 2 | Connection | O2-KR3 (Line) | [Remove confirmation from Care Circle invite flow](https://linear.app/ditto-care/project/remove-confirmation-from-care-circle-invite-flow-2f864e508b16) | May 21–28 |
| 2 | Fundamentals | O1-KR3 (Proj) | [UK launch](https://linear.app/ditto-care/project/uk-launch-2827551d00ad) | May 26–27 |
| 1 each | mixed | mixed | Security Improvements, 15ftes: Person Research, Multi-profile, Staging Backend, Care Circle V2 (2), Growth: Customer.io (2), EXP-B2B experiments (4) | Apr–May |
| **121** | mixed | mixed | **Loose issues** (no project): 28 bug fixes, 12 lifecycle, 11 each design-system/compliance/internal-ops, 9 infra, rest spread | Apr–May |

## AI feature-stack depth (called out explicitly)

Two tracks, both deepening the moat per the Care Brain / care-intelligence direction.

**1. Conversation Explainer pipeline (Clarity, O2-KR4 + foundational).**
- Automatic provider failover so an Azure OpenAI outage no longer needs manual intervention ([PRO-34](https://linear.app/ditto-care/issue/PRO-34)).
- Google Gemini initialised as fallback / shadow provider ([PRO-59](https://linear.app/ditto-care/issue/PRO-59)); Gemini-optimised prompts built for both pipelines ([PRO-139](https://linear.app/ditto-care/issue/PRO-139)).
- A/B harness between old and new AI pipelines ([PRO-60](https://linear.app/ditto-care/issue/PRO-60)); explainer quality + actionability upgrade ([PRO-126](https://linear.app/ditto-care/issue/PRO-126), [PRO-29](https://linear.app/ditto-care/issue/PRO-29)).
- Categorization metadata published to Azure Event Hub ([PRO-187](https://linear.app/ditto-care/issue/PRO-187)); follow-up data contract spec'd ([PRO-390](https://linear.app/ditto-care/issue/PRO-390)).
- The eval/guardrail rework (project *AI Quality — Tune Evals and Guardrails*, 7 issues) is what drove the false-positive rate from ~15% to ~1–2% (per product-context).

**2. Internal AI agents (Fundamentals, O1-KR2).**
- New **Agents team** + **B2B Outreach POC**: a state-machine cascade where coordinator → discovery → research → drafter agents produce personalized outreach packs. 18 completed runs against Macmillan, Diabetes UK, Aviva, Bupa, ACME on May 22.
- **Triage Intelligence + RISCE Scoring (Linear AI)** auto-score and triage incoming ideas (O1-KR4 discipline).
- Daily-briefing agent POC ([PRO-439](https://linear.app/ditto-care/issue/PRO-439)) and single-user B2B-outreach automation ([PRO-440](https://linear.app/ditto-care/issue/PRO-440)); agentic-way-of-working workshop ([PRO-257](https://linear.app/ditto-care/issue/PRO-257)).
- Exploratory: Claude design spike ([PRO-172/173](https://linear.app/ditto-care/issue/PRO-172)).

## Forward view — what's planned for Jun–Jul (next 2 months)

37 active/planned projects, 27 near-term. Full list: [`planned-projects-next-2mo.csv`](./planned-projects-next-2mo.csv); the 61 in-flight issues: [`planned-issues-next-2mo.csv`](./planned-issues-next-2mo.csv).

### In progress now (will land first)
| Project | Pillar | OKR | Target |
|---|---|---|---|
| [Calendar Pull](https://linear.app/ditto-care/project/calendar-integration-d7be6e880b53) (MVP, device-calendar medical scan) | Convenience | O2-KR2 | open |
| [Care Circle 3.0](https://linear.app/ditto-care/project/care-circle-30-55ab95ddb320) | Connection | O2-KR3 | Jul 2 |
| [Conversation Explainer AI Improvements](https://linear.app/ditto-care/project/conversation-explainer-ai-improvements-ac236bd50b60) (M1 live May 22; M2–M5 shadow→promote, transcription A/B) | Clarity | O2-KR4 | Jun 19 |
| [15 FTE AI agents](https://linear.app/ditto-care/project/15-fte-ai-agents-93ca13ac7cba) | Fundamentals | O1-KR2 | Jun 30 |
| [Implement Survicate](https://linear.app/ditto-care/project/implement-survicate-76685d419334) | Fundamentals | O2-KR4 | Jun 5 |
| [Analytics Foundations](https://linear.app/ditto-care/project/analytics-foundations-807340995185) + [Ship at 80% Experiment Velocity](https://linear.app/ditto-care/project/ship-at-80percent-experiment-velocity-engine-411f3367198c) | Fundamentals | O1-KR4 | Jun 9 |
| [Remove confirmation from CC invite flow](https://linear.app/ditto-care/project/remove-confirmation-from-care-circle-invite-flow-2f864e508b16) | Connection | O2-KR3 | (Code-Red auto-accept fix) |
| [Migrate Away from Auth0](https://linear.app/ditto-care/project/migrate-away-from-auth0-946ffdc58304) → Supabase | Fundamentals | O2-KR3 | open |
| Customer.io Post-Summary Flow | Convenience | O2-KR2 | May 30 |

### Planned / backlog with Jun–Jul dates
| Project | Pillar | OKR | Window |
|---|---|---|---|
| [AI Answer Suggestions](https://linear.app/ditto-care/project/ai-answer-suggestions-0c14cc1a4c25) (Care Brain Phase 1) | Clarity | O2-KR4 | Planned |
| Beyond Appointments: Expanding Activation Paths | Convenience | O2-KR2 | Jun 1–30 |
| Create an aha moment during onboarding | Convenience | O2-KR2 | Jun 5–30 |
| Customer.io Profile Completion Flow | Convenience | O2-KR2 | Jun 15–19 |
| Post-Ship Evaluation & Verdict Ritual | Fundamentals | O1-KR4 | Jun 9–16 |
| Concurrent Experiment Operations | Fundamentals | O1-KR4 | Jun 16–30 |
| Log out & account deletion behaviour | Fundamentals | — | Jun 8–Jul 3 |
| Geofencing · Language Expansion · Medical Data Vault | Conv./Fund. | O2-KR4 / O1-KR3 | Jul → Q3 |
| UK launch · Personalized Discovery · Multi-profile · Wearable · Care journeys viz | mixed | mixed | unscheduled |

### What the forward view tells us
- **Growth-loop bets cluster in June** (invite-friction removal, Beyond Appointments, aha-onboarding, Customer.io flows) — directly chasing the O2-KR2/KR3 gap that triggered Code Red.
- **The experimentation machine is being built in parallel** (Ship-at-80, Concurrent Experiments, Post-Ship Verdict, Analytics Foundations) — that is O1-KR4 turning from policy into infrastructure.
- **Mobile is the binding constraint.** Several high-priority items (Calendar Pull gaps, CC deep-link auto-accept, New-in-Ditto announcements) are stalled on mobile capacity — see [`../mobile-dev-hiring-decision.md`](../mobile-dev-hiring-decision.md).

## Next step (not done here)
Performance overlay: join this shipped set to Mixpanel/Porygon reads (summary-view lift, activation, invite-acceptance per feature) to grade *did it move the KR it was mapped to*. The CSV `ID` + `OKR_primary` columns are built to support that join.
