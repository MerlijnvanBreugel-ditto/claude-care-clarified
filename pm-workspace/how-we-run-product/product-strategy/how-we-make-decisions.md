# How We Make Decisions

## Explore vs. Exploit

> *"The goal of testing a lot of growth ideas is not to find a lot of things that work. You are trying to learn about a small set of areas that have huge ceiling room for you."*
> — **Brian Balfour**, Reforge (featured on Lenny's Podcast)

Every initiative at Ditto falls into one of two modes. Knowing which mode you're in determines how you staff it, how you measure it, and when you stop.

| | Explore | Exploit |
|---|---|---|
| **Purpose** | Find new points of leverage | Maximize proven leverage points |
| **What it looks like** | Test broadly, learn fast, kill cheap | Go deep, optimize, compound gains |
| **Evidence bar** | Lightweight: 3+ user signals, quick prototype, directional data | Strong: quantitative proof, behavior change observed |
| **Team investment** | Small — PM + designer, short sprints | Full cross-functional — engineering, design, growth |
| **Timeline** | Days to weeks | Weeks to months |
| **Success criteria** | "Did we learn something actionable?" | "Did we move the metric?" |
| **Kill criteria** | No signal after 2 rounds of testing | Below kill threshold after 2 weeks live |
| **Examples at Ditto** | New activation concepts, voice check-in, appointment prep | Care Circle v2 optimization, onboarding funnel, summary quality |

### How to decide which mode

```
Is this a proven lever with known ROI?
  → Yes: EXPLOIT — optimize, go deep, invest cross-functional resources
  → No: EXPLORE — test cheap, learn fast, stay disciplined

Found something promising in Explore?
  → Don't exploit yet. Ask: is this a point of leverage or just a tactic that works?
  → Point of leverage = high ceiling, compounds over time → move to Exploit
  → Just works = nice to have, but limited ceiling → note it, keep exploring
```

### Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| **Premature exploitation** | Found one thing that works, go all-in too early | Discipline: stay in Explore until you find a *leverage point*, not just a tactic |
| **Abandoning Exploit too early** | Diversify before extracting full value | Most teams underestimate depth — commit cross-functional effort before switching |
| **No clear mode** | Team doesn't know if they're exploring or exploiting | State the mode explicitly in every epic and standup |

## RISCE Scoring

Score each feature 1–5 on these dimensions:

| Dimension | Question | Scale |
|---|---|---|
| **R — Reach** | How many users will this affect? | 1 = <5%, 3 = 20-50%, 5 = >50% |
| **I — Impact** | How much will it change behavior? | 1 = Minimal, 3 = Notable, 5 = Transformative |
| **S — Strategic** | How aligned with vision & North Star? | 1 = Tangential, 3 = Supports, 5 = Core to mission |
| **C — Confidence** | How sure are we this will work? | 1 = Guess, 3 = Some signal, 5 = Strong evidence |
| **E — Effort** | How much work to build? | 1 = >1 month, 3 = 1-2 weeks, 5 = <1 week |

**RISCE** = R x I x S x C x E

Higher = prioritize. Use as input to discussion, not as the final answer.

### Quick Filter: Delight x Effort

Before deep scoring, plot ideas on this 2x2:

| | Low Effort | High Effort |
|---|---|---|
| **High Delight** | Ship this week | Explore candidate — full discovery |
| **Low Delight** | Batch in polish sprint | Question it — is this worth it? |

## Go/No-Go Gate

> *"The most important product decision is what NOT to build."*
> — **Melissa Perri**

### When

Before any **Explore bet** moves from Discovery → Ready for Delivery

### Who

Merlijn + one other (rotating: Niek, Ilayda, or Yury)

### Required Artifacts

1. **[Hypothesis](../discovery/hypothesis-template.md)** with mechanism
2. **Evidence summary** — what did we learn in discovery?
3. **Four risks assessment** — where are we still uncertain?
4. **Kill criteria** — what would make us stop?

### Outcomes

| Decision | Meaning |
|---|---|
| Go | Move to Ready for Delivery |
| More discovery | Specific questions to answer first |
| Kill | Document reasoning, add to Learning Log |

## Discovery Evidence Bars

| Mode | Minimum Evidence Required |
|---|---|
| **Explore** | 5+ user interviews, prototype tested with real users, quantitative signal from analytics or survey |
| **Exploit** | 3+ data points (user feedback, analytics trend, or interview quotes) |
| **Polish** (bug fixes, minor tweaks) | Bug report, support ticket pattern, or clear UX issue |

---

*If you can't explain why you're building something in one sentence, you're not ready to build it.*
