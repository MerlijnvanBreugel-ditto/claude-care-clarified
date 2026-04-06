# Shipping & Release: How We Launch and Communicate

**Released does not equal Done.** Done = users know, users use, impact validated.

This page covers the product activation side of shipping: communication, release notes, and launch coordination. For Build and QC process (code review, testing, deployment), see [Ways of Working](https://dittocare.atlassian.net/wiki/spaces/DP/pages/219512846/Ways+of+Working). For post-launch evaluation (Week 1/2 checks), see [Experimentation & Learning](../experimentation-and-learning/).

## Flow

```
[Discovery → Go/No-Go] → Build → QC → RELEASE → LEARN
                          ↑                        ↑
                    Ways of Working          Experimentation
                    (Confluence)            & Learning page
```

| Phase | What happens | Owner |
|---|---|---|
| **Build** | Development, code review | Engineering ([Ways of Working](https://dittocare.atlassian.net/wiki/spaces/DP/pages/219512846/Ways+of+Working)) |
| **QC** | Design review, functional QA | Design + QA ([Ways of Working](https://dittocare.atlassian.net/wiki/spaces/DP/pages/219512846/Ways+of+Working)) |
| **Release** | Deploy, communicate, activate | Product + Engineering |
| **Learn** | Week 1/2 evaluation | Product + Growth ([details](../experimentation-and-learning/)) |

## Feature Classification

Every feature gets classified before release. This drives the communication plan and learning cadence.

| Type | Definition | Examples |
|---|---|---|
| **Explore** | New capability that didn't exist before | Profile page with FAQ, Voice health check-in |
| **Exploit** | Doubling down on proven mechanics | Personal messages in sharing, invitation flow improvements |
| **Polish** | UX improvements, bug fixes, performance | Layout fixes, speed improvements |

A feature area can be both Explore and Exploit. Care Circle sharing improvements = Exploit. Care Circle profile page = Explore. Classify by the specific feature, not the umbrella.

## Communication Matrix

| Channel | Explore | Exploit | Polish |
|---|---|---|---|
| **App store notes** | Yes | Yes | Yes |
| **In-app notification center** | Yes | Yes | Yes |
| **Push notification** | Yes | — | — |
| **Email** (Customer.io) | Yes (dedicated) | Batched with other improvements | — |
| **LinkedIn** | Yes | — | — |
| **Instagram** | Yes | Yes | — |
| **Internal Slack** (#releases-mobile) | Yes | Yes | Yes |
| **Friday demo** (30 min, whole team) | Yes | Yes | — |

**Channel rationale:**
- **LinkedIn** = professional/investor/partner audience — new capabilities only
- **Instagram** = user community — anything that makes Ditto better
- **Email** = personal — Explore gets its own email, Exploit gets bundled into periodic digest (cadence via Customer.io, TBD)
- **Friday demo** = team alignment — Explore and Exploit, not polish

## Pre-Release Readiness

Release is blocked until learning and activation are ready. This is a gate, not a suggestion.

### Learning ready
- [ ] Success hypothesis defined (what behavior change, what metric, what threshold)
- [ ] Mixpanel tracking implemented and verified in staging
- [ ] Week 1 health check scheduled (date + who)
- [ ] Week 2 impact check scheduled (date + who)

### Activation ready
- [ ] Feature tier classified (Explore / Exploit / Polish)
- [ ] Communication plan filled per matrix
- [ ] Release notes drafted (EN + NL, benefit language)
- [ ] In-app notification content ready (if applicable)
- [ ] Social content prepared (if applicable — LinkedIn for Explore, Insta for Explore+Exploit)

### Deploy
- [ ] Code complete, reviewed, merged
- [ ] QA sign-off
- [ ] Deployed to production
- [ ] Tracking verified in production (not staging — production)

## Release Notes

Release notes are coordinated in the [#releases-mobile](https://dittocare.slack.com/archives/C09JGESEB25) Slack channel. Every release gets notes posted there before publishing to the app stores.

### App Store Release Notes Template

Notes are always written in both EN and NL:

```
EN
We regularly update Ditto to make our app and your experience better. This release includes:
What's new:
• [Feature/improvement in benefit language]
• [Feature/improvement in benefit language]
• Bug fixes and performance improvements
Everyone deserves clarified care. Like Ditto? Leave us a review! Your feedback helps us keep improving.

NL
We werken Ditto regelmatig bij om de app beter te maken. Deze update bevat:
Wat is er nieuw:
• [Feature/verbetering in benefit language]
• [Feature/verbetering in benefit language]
• Bugfixes en prestatieverbeteringen
Iedereen verdient heldere zorg. Ben je blij met Ditto? Laat een recensie achter! Jouw feedback helpt ons Ditto te blijven verbeteren.
```

**Writing guidelines:**
- Lead with benefit, not feature name ("Improved appointment preparation with guided questions" not "Added Questions feature")
- Keep bullet points to 1 line each
- Always include "Bug fixes and performance improvements" as a catch-all
- Always end with the review CTA

## Internal Release Rituals

| Ritual | When | What | Who |
|---|---|---|---|
| **#releases-mobile** | Every release | Release notes + what's in this build | Product + Engineering |
| **Friday demo** | Weekly, 30 min | Live demo of Explore + Exploit features | Whole team |
| **Ad-hoc Slack** | As it happens | Screenshots, GIFs of exciting new things | Anyone |

## Shipping Checklist (for Jira tickets)

```
## Shipping Checklist: [Feature Name]

**Tier:** [Explore / Exploit / Polish]
**Responsible:** [Name]
**Target Release:** [Date]

### Learning Ready
- [ ] Success hypothesis defined
- [ ] Mixpanel tracking implemented and verified in staging
- [ ] Week 1 health check scheduled: [Date] — [Who]
- [ ] Week 2 impact check scheduled: [Date] — [Who]

### Activation Ready
- [ ] Communication plan per matrix
- [ ] Release notes drafted (EN + NL)
- [ ] In-app notification content ready
- [ ] Social content prepared (per tier)

### Deploy
- [ ] Code complete, reviewed, merged
- [ ] QA sign-off
- [ ] Deployed to production
- [ ] Tracking verified in production

### Post-Release
- [ ] Release notes published (app store + in-app)
- [ ] Communication sent per matrix
- [ ] Added to product strategy meeting evaluation table
- [ ] Added to Friday demo queue
- [ ] Week 1 health check: [Date]
- [ ] Week 2 impact check: [Date]
- [ ] Learning logged
- [ ] Decision: [Double down / Iterate / Deprioritize / Done]
```

## Anti-Patterns

| Anti-Pattern | Why it's dangerous | Fix |
|---|---|---|
| **Tracking missing at launch** | Can't measure what you don't track | Block release without tracking verification |
| **No communication plan** | Users don't discover the feature | Fill in matrix before release |
| **Release notes as afterthought** | Missed opportunity to frame value | Write release notes before deploy |
| **Ship without hypothesis** | Can't evaluate success without criteria | Block release without success hypothesis |
| **Skip activation, jump to learning** | Learning is meaningless if users never saw it | Activation readiness is a gate |
| **Same message everywhere** | LinkedIn audience ≠ Instagram audience | Tailor per channel |

---

*Ship to learn, not to celebrate.*
