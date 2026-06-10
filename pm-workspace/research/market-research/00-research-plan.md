# 00 — Market Research: Plan, Methodology & Framework

**Project:** ditto.care — Holistic Market Research (healthcare · health tech · consumer health)
**Owner:** Merlijn van Breugel (ditto.care)
**Compiled:** 2026-06-10
**Branch:** `claude/market-research-synthesis-ltz3lu`

---

## 1. Why this corpus exists

ditto's earlier research round (`../healthcare-life-changing-moments/`) made the *product/strategy* case
for a "Living Health Companion." This corpus is the complementary **market view**: a holistic, reusable,
fully-cited picture of *what is happening in the market* — at a high level across healthcare, health tech
and consumer health — that the team can discuss together and return to without re-doing the research.

It answers, with evidence:
- What is happening in the broad **healthcare**, **health-tech**, and **consumer-health** markets, and how big are they?
- Which **market trends** matter most right now (patient power, AI/LLM health usage, B2B partnerships, data-as-moat, value-based care)?
- What is happening on the **data side** (EHDS, NL PGO/MedMij/BGZ, DE ePA, FHIR) that enables or constrains a patient companion?
- Who are the **competitors** — and specifically, how does **Kin** (our most direct competitor) compare feature-by-feature to ditto?
- Which **strategic moves** are competitors making (e.g. scribe → billing → workflow automation), i.e. where is the puck going?
- What **traction** do we see on the feature directions we are weighing — AI health assistants, grounded/cited answers (OpenEvidence), digital health coaches, symptom tracking, journaling, logging — including **success cases and cautionary tales**?
- Why are **cycle-tracking and meditation** the most successful consumer-health categories, why do **symptom trackers** churn, and what can we learn?

## 2. The framework (the lens we look through)

Everything is organized around one consistent frame so it reads as a single market view, not a pile of facts:

```
        THREE CONCENTRIC MARKETS                 FOUR FORCES ACTING ON THEM
   ┌─────────────────────────────┐        1. Patient power / consumerization
   │  Healthcare system (payers,  │        2. AI & data (LLMs, grounding, longitudinal data)
   │  providers, regulation)      │        3. Regulation & data rights (EHDS, PGO/BGZ, ePA)
   │   ┌───────────────────────┐  │        4. Capital & business-model shifts (funding, B2B2C)
   │   │  Health tech / digital │  │
   │   │   ┌─────────────────┐ │  │   →  WHERE THE PUCK IS GOING (feature-direction traction)
   │   │   │ Consumer health │ │  │   →  IMPLICATIONS FOR DITTO (where to play, what to avoid)
   │   │   └─────────────────┘ │  │
   │   └───────────────────────┘  │
   └─────────────────────────────┘
```

## 3. Scope

- **Geography:** Mostly **EU-anchored (Netherlands + DACH)**, with **explicit US and global benchmarking**
  where the phenomenon is global (LLM health usage, US scribes, consumer-health apps, Kin).
- **Markets:** healthcare system · health tech / digital health · consumer health & wellness.
- **Sources:** external/public only — analyst reports, funding databases, EU & national bodies, company
  filings/docs, reputable press, peer-reviewed literature, and (flagged) app-store/community texture.
- **Not in scope this round:** internal ditto data (Mixpanel/Granola/Drive/Slack/Linear). Confluence
  competitive research was referenced by the team but is **not reachable from this session** (no Atlassian
  connector); if provided later it can be folded in.

## 4. Pipeline architecture

```
Phase 0   Methodology & framework (this doc)
Phase 1   Parallel fan-out — 8 research agents, each writes one cited findings file:
            M1 Market landscape & sizing
            M2 Macro trends (incl. LLM health usage, B2B partnerships)
            M3 Health data infrastructure (EHDS, PGO/BGZ, ePA)   [extends ../06]
            M4 Competitor landscape (refresh + expand)           [extends ../07]
            M5 Kin deep dive + direct-competitor feature matrix
            M6 Feature-direction traction (assistants, grounded answers, coaches, tracking, journaling)
            M7 Consumer-health retention teardown (cycle, meditation vs symptom-tracker churn)
            M8 Strategic-moves & migration map
Phase 2   Synthesis — market framework & direction (S1) + implications for ditto (S2)
Phase 3   Self-contained HTML deck (~40 slides), reusing the existing template
Phase 4   Index (README), consolidated sources, commit & push
```

## 5. Source-quality bar

Tiered; every non-obvious claim carries an inline `[source, year](url)` and a confidence level:

- **Tier 1 (highest):** peer-reviewed studies; EU & national bodies (EHDS/EC, gematik, Nictiz/MedMij,
  EUROSTAT, OECD); funding databases & analyst houses (CB Insights, Rock Health, Galen Growth, Sifted/Dealroom);
  company filings/official product docs.
- **Tier 2:** reputable tech/health press (STAT, TechCrunch, FierceHealthcare, Sifted, MobiHealthNews), analyst commentary.
- **Tier 3 (texture only):** app-store listings, blogs, company self-reporting, community forums — used for
  qualitative texture and competitor self-claims, never as the sole basis for a hard number; always flagged.

Each finding carries **Confidence (High/Med/Low)** and a **US→EU flag** when a figure is US-derived and only
directionally applicable to Europe.

## 6. Honesty & bias controls

- **US→EU conflation** is the most likely error — flagged wherever it occurs.
- **Vendor self-claims** (funding, MAU, retention) are treated as Tier 3 unless independently corroborated.
- **Negative findings** ("nobody owns X") are labelled as broad-search inferences, not exhaustive proof.
- **The ChatGPT "40M health questions/week" and OpenEvidence traction claims are explicitly re-verified**
  against primary sources; the figure we report is whatever the source actually supports.
- Numbers that cannot be verified are marked **unconfirmed** rather than guessed.

## 7. Deliverables

Findings files `M1–M8`, synthesis `S1–S2`, `sources.md`, this plan, a `README.md` index, the reused
reference material in `reused/`, and a self-contained `market-research-deck.html` (~40 slides, offline,
no external dependencies) — all on the feature branch.

## 8. Relationship to the existing corpus

This folder **builds on, and does not replace**, `../healthcare-life-changing-moments/`. Where that round
already did strong work — EU policy context (`findings/06`), competitive landscape (`findings/07`),
EU epidemiology/sizing (`findings/01`), and daily JTBD + habit/retention theory (`findings/08b`) — this
round **extends and refreshes** it to June 2026 rather than duplicating it. Key reused inputs are mirrored
in `reused/` for self-containment, with provenance noted.
