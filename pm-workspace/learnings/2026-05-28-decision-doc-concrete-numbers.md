# Learning — Decision docs need decision-grade numbers, not framing

**Date:** 2026-05-28
**Workflow:** Ad-hoc one-pager (mobile dev hiring proposal)
**Artifact:** `pm-workspace/specs/mobile-dev-hiring-decision.md` (+ `.docx`)

## What I drafted

A one-page internal proposal to hire a temp mobile dev via emagine for 3 months. Tables for stalled Linear tickets and for the emagine vs Dutch-recruiter comparison. Recommendation, why-now, and ask.

## What Merlijn changed (and why each change matters)

| Pattern | My version | Merlijn's version | Why it matters |
|---|---|---|---|
| **Total spend** | "~€50/hr vs ~€100/hr" | Added "Total investment: 25k vs 50k" row | The total is what gets decided. Rates are an input; totals are the ask. |
| **Cost of waiting scope** | Only stalled Linear tickets | Added Auth0 migration row — €500+/month + missing phone verification | Ongoing infra burn is part of the case for hiring. Cost-of-waiting ≠ only delayed features. |
| **Status framing** | Literal Linear states ("Backlog", "Triage") | "In progress for 4 weeks", "Delay of two weeks" | Stakeholders care about duration of pain, not workflow labels. |
| **Off-ramp clause** | "3 months, flexible" | "3 months, flexible, stop when full-timer starts" | Makes the temp commitment a risk-bounded option, not a fixed contract. |
| **Comparison label** | "Dutch recruiter" | "Dutch recruiter payroll" | Names the actual alternative model honestly. |
| **Name spellings** | "Imagine", "Patrick" | "emagine", "Patryk" | Voice-dictation artifacts. Cross-check against Linear before writing. |
| **Recruiter window** | "~4 weeks" | "~1.5 weeks" | Tighter urgency than I assumed. |

## Root-cause reflection

I optimized for **structure and framing** (TL;DR, comparison tables, clean prose) but under-delivered on **decision-grade content** (totals in €, ongoing costs, delay durations). A clean structure with abstract numbers is still abstract. For any investment proposal, the work isn't done until the bottom-line € appears next to each option.

I also defaulted to ticket-system vocabulary instead of business vocabulary. Stakeholder docs need translation, not transcription.

## Rules I'm committing going forward

1. **Show the total €.** Always multiply rate × duration into a single bottom-line spend number for every option compared. Memory: [[investment-proposal-essentials]].
2. **Ask about ongoing costs explicitly.** Cost-of-waiting tables must include at least one item that costs us money every day we wait, not just delayed features. Default question for hiring/vendor proposals: *"Any monthly burn or in-flight migrations I should add to the cost-of-waiting list?"*
3. **Translate ticket status into delay duration.** Never paste raw Linear status names into stakeholder docs. Memory: [[status-as-delay-framing]].
4. **Off-ramp clause on every temp engagement.** Spell out how it ends.
5. **Cross-check dictated names against Linear assignees.** Memory: [[ditto-team-and-vendor-names]].
