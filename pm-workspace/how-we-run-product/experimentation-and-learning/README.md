# Experimentation & Learning: How We Iterate on Features

> *"Discovery shouldn't stop when you start building. The best teams run continuous discovery during Build — weekly user touchpoints, not just at kickoff."*
> — **Teresa Torres**

This page covers **product-level iteration** — how we learn from shipped features and iterate based on evidence. For **growth experimentation** (A/B testing, Statsig, funnel optimization), see [Introducing Experimentation at Ditto](https://dittocare.atlassian.net/wiki/spaces/DG/pages/566689794/Introducing+Experimentation+at+Ditto).

## The distinction

| | Product Iteration (this page) | Growth Experimentation (Niek's page) |
|---|---|---|
| **Question** | Did this feature solve the problem? Should we iterate, double down, or kill? | Which variant converts better? What moves the metric? |
| **Method** | Hypothesis → ship → evaluate → decide | A/B test → statistical significance → roll out |
| **Tools** | Mixpanel dashboards, user interviews, support tickets | Statsig, Mixpanel |
| **Cadence** | Week 1 + Week 2 post-launch | Continuous, experiment-level |
| **Owner** | Product (Merlijn) | Growth (Niek) |

They feed each other: product iteration surfaces insights that become growth experiment hypotheses, and growth experiments validate product assumptions at scale.

## Post-Launch Evaluation

Every shipped feature goes through two checkpoints.

### Week 1: Health Check

| Question | What you're checking |
|---|---|
| Tracking firing correctly? | Data integrity |
| Critical bugs or confusion? | Immediate issues |
| Early adoption vs. target? | Directional signal |
| User feedback (support, reviews)? | Qualitative signal |

**Decision:** Kill / Fix / Continue

### Week 2: Impact Check

| Question | What you're checking |
|---|---|
| Hit [success criteria](../discovery/hypothesis-template.md)? | Did hypothesis hold? |
| Behavior change observed? | Is the mechanism working? |
| If miss: discoverability or value problem? | Root cause diagnosis |
| User feedback themes? | Qualitative patterns |

**Decision:** Double down / Iterate / Deprioritize / Done

### Logging Results

After Week 2, add an entry to the Learning Log:

| Field | Capture |
|---|---|
| **Hypothesis** | What we believed |
| **Result** | What happened (with numbers) |
| **Why** | Our best explanation |
| **Next** | What we'd do differently |

## Continuous Discovery During Build

Don't wait until launch to learn. During Build:
- Weekly user touchpoint (even 15 min with one user)
- Check assumptions against real behavior
- Surface risks early — cheaper to pivot during build than after launch

## The Iteration Loop

```
Ship → Week 1 Health → Week 2 Impact → Learning Log → Decision
                                                          │
                                          ┌───────────────┼───────────────┐
                                          │               │               │
                                    Double down       Iterate          Kill
                                    (Exploit mode)    (next cycle)     (log why)
```

## Anti-Patterns

| Anti-Pattern | Why it's dangerous | Fix |
|---|---|---|
| **Ship = done** | Shipping is the beginning; impact is done | Enforce Week 1 + Week 2 completion |
| **Celebrating ship** | Creates wrong incentives | Celebrate impact, not releases |
| **Skipping Week 2** | Week 1 is noise; Week 2 is signal | Require Week 2 before closing feature |
| **No learning logged** | Wasted experiment | Block "Done" status without Learning Log entry |
| **Discovery stops at Build** | Assumptions change | Weekly user touchpoints during Build |

---

*Every release is a lesson. The question is whether you bother to read it.*
