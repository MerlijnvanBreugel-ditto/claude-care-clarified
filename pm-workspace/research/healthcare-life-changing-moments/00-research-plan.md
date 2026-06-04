# 00 — Research Plan & Methodology

**Project:** Life-Changing Healthcare Moments — Mapping the Overlooked Problems & ditto's Category-Defining Opportunity
**Owner:** Merlijn van Breugel (ditto.care)
**Date:** 2026-05-31
**Branch:** `claude/healthcare-research-strategy-M8Gqp`

---

## 1. Why this research exists

People hit by a **life-changing diagnosis** — cancer, a neurodegenerative disease, MS or another
sudden autoimmune condition, a stroke or other acute severe event — are dropped into a system
they don't understand, at the moment they are least able to process it. They forget most of what
the doctor says, struggle to involve the people they love, lose the thread across a dozen
specialists, and carry a quiet administrative and emotional load that nobody is accountable for.

ditto has already shipped one answer to one slice of this: a **patient-level summary of a
healthcare appointment**. It looks trivial. It is not — because ~60–80% of what is said in a
consultation is forgotten almost immediately, and roughly half of what *is* remembered is
remembered wrong. A clean summary quietly attacks a status-quo failure that affects nearly
every patient on earth.

**The bet behind this research:** there is a *cluster* of adjacent, overlooked, millions-felt
problems just like that one — problems everyone has normalized, that a focused product company
could own. This research maps that cluster, ranks it, and forms an opinionated view of the
**category ditto can shape.**

## 2. Research questions

1. Across the four journeys, what are the **full lifecycle pain points** in understanding care,
   involving loved ones, managing health, preparing for appointments, and keeping an overview?
2. Which of these are **heavily overlooked** — normalized, under-served, yet high-reach and
   high-severity?
3. What is the **EU context** (regulation, data infrastructure, reimbursement, patient rights)
   that constrains or accelerates a solution?
4. Who is already building here, and **what do they conspicuously fail to solve**?
5. Through a **contrarian, category-defining founder lens**, what is the single biggest
   opportunity, where should ditto start, and what must be true for it to work?

## 3. Scope

- **Journeys (deep-dive):** Cancer/oncology · Neurodegenerative (dementia, Parkinson's, ALS) ·
  MS & autoimmune · Sudden severe diagnosis (stroke, cardiac, type-1 diabetes, acute onset).
- **Geography:** Pan-EU framing, anchored on the **Netherlands + DACH** (DE/AT/CH) for concrete
  statistics and health-system mechanics. US data used only where EU data is thin, and flagged.
- **Sources this round:** external/public only — peer-reviewed literature, EU & national health
  bodies, named patient organizations, company/competitor analysis, and lived-experience
  communities (the last used for qualitative texture, flagged as such). No internal ditto data
  (Granola/Mixpanel/Drive/Linear/Slack) is mined this round.

## 4. Pipeline architecture

```
Phase 0   Methodology (this doc)
Phase 1   Parallel fan-out — ~8 research agents, each writes a cited findings file:
            A Epidemiology & market (EU)        → findings/01
            B Cancer journey                    → findings/02
            C Neurodegenerative journey         → findings/03
            D MS & autoimmune journey           → findings/04
            E Sudden severe journey             → findings/05
            F EU policy & system context        → findings/06
            G Competitive & solution landscape  → findings/07
            H Overlooked & adjacent problems    → findings/08
Phase 1.5 Verification — adversarially re-check the most load-bearing claims
Phase 2   Synthesis — cross-journey pain map (09) + strategic synthesis & scoring (10)
Phase 3   Contrarian founder lens (11)
Phase 4   Red-team critique (12) → refined final synthesis (13)
Phase 5   Self-contained HTML narrative deck (≤30 pages)
Phase 6   Index, commit, push
```

## 5. Source-quality bar

Tiered, and every claim is tagged with its tier and a confidence level:

- **Tier 1 (highest):** peer-reviewed studies/meta-analyses; EU institutions (EUROSTAT, EU4Health,
  EHDS, EMA); national bodies (RIVM/Nivel NL, RKI/G-BA DE); OECD Health at a Glance.
- **Tier 2:** named patient organizations (e.g. national cancer/MS/Alzheimer societies, EU patient
  umbrella groups), professional society guidelines, reputable think tanks.
- **Tier 3 (texture only):** patient communities/forums, news, company self-reporting. Used to
  illustrate lived experience and competitor claims — never as the sole basis for a hard number.

**Citation discipline:** every non-obvious claim carries an inline `[source, year](url)`; all
sources are collected in `sources.md` with access date 2026-05-31. Each finding carries:
- **Confidence:** High / Medium / Low
- **EU-relevance flag:** note when a statistic is US-derived and only directionally applicable.

## 6. Bias & honesty controls

- **US→EU conflation** is the most likely error; flagged explicitly wherever it occurs.
- **Survivorship/selection bias** in community data is assumed; community findings are corroborated
  against Tier 1/2 before being treated as real.
- **Vitamin-vs-painkiller test** applied to every candidate opportunity in synthesis.
- The **red-team phase (12) is mandatory**, not decorative; the final synthesis (13) must visibly
  incorporate its corrections.

## 7. Deliverables

Findings files `01–08`, synthesis files `09–13`, `sources.md`, `README.md` index, and a
self-contained `ditto-narrative-deck.html` (≤30 pages, text-heavy, no external dependencies),
all committed to the feature branch.
