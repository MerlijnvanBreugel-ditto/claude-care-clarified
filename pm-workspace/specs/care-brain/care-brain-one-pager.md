# Care Brain — One-Pager

**Date**: 2026-04-15 · **Status**: Committed strategy (not exploratory) · **Author**: Mewtwo + Merlijn

This is the canonical one-pager. Every other Care Brain spec extends from here. If this page and a longer doc disagree, this page wins.

---

## Vision

**Ditto is the care-journey assistant for families facing cancer and neurodegenerative disease. One recording, everyone informed, nothing falls through the cracks.**

**Who we serve (the beachhead, chosen deliberately, everything else is later)**:
Patients on a serious-condition track (oncology primary, neurodegenerative second) and their one to three direct loved ones (partner, adult children). Netherlands first. Ditto's active user base is already 50% oncology, so the wedge is real, not speculative.

**What we're replacing**:
The current workaround — WhatsApp group chats, handwritten notes, follow-up calls to the doctor, a shared family doc that nobody updates. This loses information, creates anxiety, scales terribly, and breaks exactly when families need it most.

**The three jobs-to-be-done we commit to** (the other 42 go to the appendix doc [spec-013]):

| # | Job | In one line |
|---|---|---|
| 1 | **Hold the story** | Capture every appointment and keep the patient's full journey live across months of treatment, sourced and correctable. |
| 2 | **Share without burden** | One recording becomes an adapted update for each loved one, at the right level of detail and the right emotional weight. |
| 3 | **Catch what fragmented care misses** | Across multiple specialists and months, surface drug interactions, unresolved concerns, and patterns individual doctors can't see. |

Everything else in the 45-JTBD list is an extension of these three. We ship these, brilliantly, before we build anything else.

---

## Magical Moments (three, one per job)

**1. The Journey Page** *(for "Hold the story")*
Mara, 68, opens the Journey tab. A chronological page, generated, not templated, tells the story of her cancer in her voice. Diagnosis, treatment decisions, every medication change, every doctor. Her own story, back to her, sourced per claim. *"There's a page about my cancer that only applies to me. Not the internet version."*

**2. The Share That Writes Itself** *(for "Share without burden" — the keystone)*
Leila, 55, just heard her MS is progressing. She taps Share. Three preview cards appear: full detail for her husband, softer framing for her daughter, a one-liner for her employer. Three taps, done. No message composition while her hands are shaking. *"It wrote the message to my daughter better than I could have. It even knew not to scare her."*

**3. The Cross-Doctor Catch** *(for "Catch what's missed")*
"Your cardiologist prescribed a beta-blocker on April 3. Your pulmonologist today mentioned starting you on something that interacts. They may not know about each other. Here's a summary to bring to your next appointment." *"Ditto caught a drug interaction my doctors didn't. My pharmacist later confirmed it was real."*

The full 22-moment catalogue is in [spec-013, section 4](care-brain-master-synthesis.md). The three above are the anchors that carry the one-pager. Everything else expands from them.

---

## Technical Architecture (four decisions — this is the leverage)

1. **Pipeline plugin framework.** Every Ditto job is a specialized pipeline with a typed contract (trigger, input filter, processor, output schema, eval suite, tier, retirement criterion). Jobs are added and retired without touching the orchestrator. This is what makes the horizon affordable for a 10-person team.

2. **Typed health graph as source of truth. LLM wiki as projection.** The patient's data lives in a structured, versioned, audit-logged DB. Users and deterministic logic modify it. The LLM reads a markdown wiki auto-generated and auto-maintained from the graph. One canonical wiki per patient. Multiple per-viewer projections (for-patient, for-partner, for-daughter).

3. **Fact + filter retrieval. Similarity is an escape hatch, not a default.** Queries resolve via DB fact lookups or wiki navigation. If a pipeline reaches for similarity/RAG, it logs a wiki-schema-extension task so the query resolves via fact or filter next time. Monotonically drive similarity usage toward zero.

4. **PR-style review for high-stakes writes.** Medications, conditions, care team: every pipeline-proposed edit goes through an LLM-as-reviewer (fast, cheap) or a patient-in-the-loop confirmation (for sensitive cases). Low-stakes edits commit directly. Every wiki change is a typed, reviewable, reversible diff with a source event ID.

Deeper architecture (events, workers, wiki page schemas, migration sequence) is in [spec-014](care-brain-wiki-architecture.md) and [direction-c-nervous-system.md](direction-c-nervous-system.md). The four decisions above are the commitments. Everything else is implementation.

---

## Commitments

**PMF proxy metric (new, load-bearing)**:
*% of oncology patients who send ≥1 adapted share to a loved one per month, by cohort month.* Target: rising curve over the first 3 months after adapted-share V1 ships. This is the one metric that simultaneously predicts retention, validates the care graph, and confirms the keystone feature resonates.

**Retention commitment**:
Publish the current 90-day retention curve for the oncology cohort within 14 days of this doc. Set a target. If the current curve is below the target, all Tier 0+ architectural work stops until retention is above the line. Building on a leaky bucket is the fastest way to die.

**Moat thesis + 90-day proof point**:
The moat is care-graph density, not AI quality. Proof point: 90 days after adapted-share V1 ships, the median active oncology patient has ≥2 circle members actively reading adapted shares weekly. If below, the moat is a hypothesis, not a fact, and we restrategize. No more assuming network effects — earn them or kill the thesis.

---

## Three Decisions This Quarter (owner + date)

| # | Decision | Owner | By |
|---|---|---|---|
| 1 | Partner-first vs. patient-first as the primary product design lens (the Lenny panel's Thiel fork — is the caregiver the real customer?) | Merlijn + Design | 2026-05-15 |
| 2 | Neurodegenerative as a parallel beachhead or oncology-only first, then expand | Merlijn + CEO | End of Tier 1 ship |
| 3 | Kill-date for the current standalone summary product (vs. maintain as free-tier anchor) | Merlijn + team | Tier 1 GA |

---

## What Lives in the Extensions

This one-pager is the commitment. The corpus is the context. Everything below is extendable from the above without contradicting it:

- Full 45-JTBD catalogue → [spec-013](care-brain-master-synthesis.md) §3
- Full 22 wow-moment catalogue → [spec-013](care-brain-master-synthesis.md) §4 and [spec-012](magic-experience-vision.md)
- Deep architecture (events, workers, schemas, migration, performance, security) → [spec-014](care-brain-wiki-architecture.md) and [direction-c-nervous-system.md](direction-c-nervous-system.md)
- Capability tiers map (Foundation → Magic → Compounding → Network & Platform → Data Sovereignty) → [spec-013](care-brain-master-synthesis.md) §5
- Founder panel commentary (10 voices) → [spec-013](care-brain-master-synthesis.md) §6
- Interface design directions (10 designers, 3 merge directions) → [spec-015](care-brain-interface-design-brainstorm.md)
- Contrarian critique of the whole corpus (Lenny's panel) → [spec-016](care-brain-lennys-panel-critique.md)
- Business case + unit economics → [business-case.md](business-case.md)
- Competitive positioning (ChatGPT Health, Copilot Health, Claude for Healthcare, Apple, Hippocratic AI) → [competitive-analysis.md](competitive-analysis.md)

The one-pager is the spine. Every spec hangs from it and must stay consistent with it. When the one-pager changes, the extensions are re-aligned — not the reverse.

---

Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
