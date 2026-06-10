# 10 — Strategic Synthesis & Opportunity Scoring

**Project:** Life-Changing Healthcare Moments — ditto.care
**Date:** 2026-05-31
**Inputs:** findings/01–08b + synthesis/09 (cross-journey pain map)
**Framework:** adapted from `pm-workspace/agents/insights-synthesizer.md` (cross-reference matrix, opportunity scoring, conflict resolution).

---

## Executive summary

### The big picture
There is a real, large, evidence-backed cluster of "looks-trivial, isn't" problems around being seriously ill in Europe — and they are **the same five problems across cancer, dementia, MS and stroke**: understanding what's happening, keeping an overview, involving loved ones, managing daily symptoms/meds, and carrying the emotional load. The EU addressable population is **~34–38M patients (~44–76M with loved ones)**, with a **~4–5M/year newly-diagnosed inflow** (findings/01).

ditto today owns the **thinnest and most episodic slice**: the appointment summary (comprehension, at the moment of the visit). That is a real wedge into a real problem — but it is structurally **low-frequency, single-player, and externally triggered**, so it cannot build a habit, a data moat, or network effects. The strategic move is not to abandon it but to **demote it from "the product" to "the periodic payoff"** of a daily, multi-player loop.

### Top strategic insights
1. **The category is continuity, not transcription.** The market is full of tools that capture the *appointment* (clinician scribes) and infrastructure that will soon hold the *data* (EHDS). Nobody owns the patient's and family's **understanding of their own care, over time, across every provider** (findings/07 whitespace; confirmed by an active 2025 class action alleging Epic MyChart *fragments* records).
2. **Frequency lives in three daily jobs ditto doesn't yet do:** "is this normal — should I call?" (symptom/flare triage), "did I take it?" (meds), and "let the people I love know / ask for help" (the update burden). The first two build a personal data moat; the third is the only **multi-player, network-effect** job (findings/08b).
3. **The loved one is the missing user, not a feature.** ~80% of EU long-term care is informal, yet caregivers are locked out and unsupported. Designing for the patient-and-circle as a unit is both the unmet need *and* the growth engine (each patient seeds 5–20 contacts).
4. **Regulation is a tailwind if ditto stays on the right side of one line.** EHDS (in force 26 Mar 2025; patient summaries EU-wide by 2029) *mandates* patient data access but explicitly **won't explain it** — that's ditto's gap. Staying an *information/comprehension/coordination* tool (output stays with the patient) keeps ditto out of MDR device classification; the moment it gives clinical decision support ("you're fine, don't call") it becomes a regulated medical device (findings/06).

### Recommended direction (one line)
**Build the daily companion for living with a serious illness — a patient-and-loved-ones operating system — and let the appointment summary become its periodic, shareable crystallization.**

---

## Cross-reference matrix (validated across sources)

Insights validated across the market, competitive, and user/clinical evidence are highest-confidence.

| Insight | Market/Epi (01) | Competitive (07) | User/Clinical (02–05, 08, 08b) | Policy (06) | Confidence |
|---|---|---|---|---|---|
| Comprehension failure is universal & severe | ✅ universal reach | ✅ scribes serve clinicians, not patients | ✅ Kessels 40–80%, verified | ◐ EHDS won't explain data | **High** |
| No one owns longitudinal cross-provider overview | ✅ 50M multimorbid | ✅ MyChart fragmentation litigation | ✅ family = integration layer | ✅ EHDS populates, doesn't interpret | **High** |
| Daily symptom/med self-management is unowned & high-frequency | ✅ symptom burden data | ◐ niche/abandoned trackers | ✅ Basch, fatigue >80%, ~50% non-adherence | — | **High** |
| Loved-one layer is unmet AND the growth lever | ✅ ~80% informal care | ✅ caregiver apps US-centric, disconnected | ✅ update burden, hidden patient | ✅ proxy access exists DE/NL | **High** |
| Emotional/existential load is under-served | ✅ depression/anxiety prevalence | ◐ standalone mental-health apps | ✅ 1-in-4 depression, PTSD, limbo | — | **High** |
| Willingness-to-pay is unproven for patient-pay | ◐ TAM only, no SAM/SOM | ⚠️ most patient apps struggle to monetize | ⚠️ inferred, not measured | ✅ DiGA = only clean reimbursement (needs device status) | **Low–Med** |

The first five rows are validated across ≥3 independent evidence streams → **high confidence**. The monetization row is the **weakest link** and is escalated to the red-team (file 12) and open questions (file 11).

---

## Opportunity scoring

Five candidate product directions, scored 1–5 (5 best). **Frequency** and **Compounding** (network/data effects) are weighted heavily per the founder's growth thesis. Regulatory feasibility = how easily it stays out of MDR device classification.

| # | Opportunity | Reach | Severity | **Frequency** | Whitespace | ditto-fit | Reg. feasibility | **Compounding** | WTP | **Weighted** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Daily symptom/mood/"should I call?" companion** | 5 | 4 | **5** | 4 | 4 | 3 | 4 (data moat) | 3 | **★ 4.2** |
| 2 | **Loved-ones circle: update + coordinate + proxy** | 4 | 4 | 4 | 5 | 4 | 4 | **5 (network)** | 3 | **★ 4.3** |
| 3 | **Living health record / cross-provider overview** | 4 | 5 | 3 | 4 | 3 | 4 | 3 (data moat) | 3 | 3.6 |
| 4 | **Comprehension layer (summary + prep + explain results)** — *current* | 5 | 4 | 2 | 3 | 5 | 4 | 2 | 2 | 3.3 |
| 5 | **Integrated: daily loop where #1+#2+#4 compound together** | 5 | 5 | **5** | 5 | 4 | 3 | **5** | 4 | **★★ 4.7** |

**Read:** Opportunities 1 and 2 each beat the current product (#4) decisively on the two axes ditto is starving for — **frequency** and **compounding**. But neither alone is the answer: #1 is a strong single-player data moat with a clinical reward; #2 is the only network-effect engine. **#5 — fusing them, with the appointment summary as the crystallization artifact — is the category-defining bet** and scores highest on every growth axis. The risk it concentrates is **regulatory** (the "should I call?" interpretation) and **monetization**, both addressed below and in file 11.

---

## Conflicting signals & resolution

**Conflict 1 — "Symptom triage is the killer feature" vs "that's a regulated medical device."**
- User/clinical signal: the #1 daily job is "is this normal, should I call?" (high value).
- Policy signal: software *intended to inform clinical management* (triage/advice) is MDSW, likely Class IIa+ under MDR Rule 11 (findings/06).
- **Resolution:** Ship the *interpretation* job as **structured self-tracking + pattern surfacing + question-prompting + "here's what your care team said to watch for"**, keeping the clinical judgment with the patient/clinician (output stays with the user, no diagnosis/triage verdict). This stays non-device while still answering the felt need. Reserve true triage for a later, deliberately CE-marked module (and a DiGA reimbursement play in Germany).

**Conflict 2 — "Caregiver is the primary user" vs "patient owns the data / consent."**
- Resolution: build on existing national proxy mechanisms (DE ePA up to 5 representatives; NL DigiD Machtigen) rather than bespoke consent; make the patient the data owner and the circle permissioned by them. Turns a legal headache into a feature.

**Conflict 3 — Disease-specific depth vs cross-journey breadth.**
- Competitive signal: the only EU patient companions are oncology-only and consolidating (Outcomes4Me + Mika).
- Resolution: the *jobs* are cross-journey (synthesis/09), so build a journey-agnostic core, but **go to market through one beachhead journey** for depth and word-of-mouth density (see file 11).

---

## Strategic themes

- **Growth / category bet:** the integrated daily patient-and-circle companion (#5). *Priority: High.*
- **Innovation bet:** symptom data moat → eventual CE-marked "should I call?" + DiGA reimbursement. *Priority: Medium, sequenced later.*
- **Foundation:** keep and deepen the appointment summary as the crystallization artifact and trust anchor. *Priority: High.*
- **Defensive:** move before AI scribes (Abridge et al.) extend downstream to the patient, and before EHDS-era PHR apps add a thin "explain" layer. *Priority: Medium.*

→ Opportunity #5, its beachhead, and the load-bearing questions are developed in `11-contrarian-founder-lens.md`. Weaknesses in this synthesis are stress-tested in `12-red-team-critique.md`.
