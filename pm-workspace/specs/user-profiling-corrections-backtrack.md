# User Profiling Canvas — Corrections & Documentation Gap Analysis

**Date**: 2026-03-16
**Purpose**: Track what was wrong in the canvas output, why the sources didn't capture it, and what documentation needs updating.

---

## Corrections from Merlijn

| # | What the canvas said | What's actually true | Severity |
|---|---|---|---|
| 1 | "Can't upload PDFs" listed as top functional complaint and unaddressed gap | **PDF upload is built and shipped.** Users can upload PDFs and existing documents. | High — misrepresents product capability |
| 2 | "No multi-language support" listed as major gap for language barrier patients | **Ditto translates summaries to Turkish, Arabic, and English.** Transcription is limited to Dutch and English conversations, but the output supports more languages. | High — misrepresents a shipped feature |
| 3 | "All-or-nothing sharing" listed as current state, with DPMA-1964 as fix in pipeline | **Users CAN control what to share** — they can select which sections to include and add a personal message. What they CAN'T control is **who** they share with — all followers see the same thing. DPMA-1964 addresses the who, not the what. | High — inverts the actual gap |
| 4 | "Health document vault" listed as not built (BIGB-58) | **Partial vault exists** — user profile with FAQ questions and shareable text functions as a basic vault. Not a full document storage system, but more than "nothing." | Medium — understates current capability |
| 5 | "Medication management" listed as parking lot only (BIGB-44) | **A medication feature exists** (shipped). Logistics coordination, symptom diary, and multi-condition management are NOT built, but basic medication management is. | High — misrepresents product capability |
| 6 | "Auto-group events into care journeys" (BIGB-65) listed as weak evidence, parking lot | **Event labeling feature idea exists** — both automatic labeling and manual user labeling were considered. Not shipped, but more developed than "weak evidence, parking lot." | Low — idea maturity understated |
| 7 | "Fear of recording — afraid to ask doctor" listed as unaddressed | **Feature idea existed on the idea board**: a sheet/explainer for the doctor explaining why the patient wants to record. Not shipped, but was a documented idea. | Medium — missed existing idea |

---

## Root Cause Analysis: Why Were These Wrong?

### Source-level gaps

| Source | What it should have contained | What it actually contained | Why the gap exists |
|---|---|---|---|
| **Product Context** (`product-context.md`) | Current feature list, shipped capabilities | High-level product description only: "recording, AI summaries, Care Circle v2 in development" | Document was written at setup (2026-02-17) and never updated with shipped features. Contains [TODO] placeholders. |
| **Feature Ideas Overview** (`feature-ideas-overview.md`) | Status of each idea including "shipped" | Ideas listed as "Parking lot" or "PAUSED" — no "shipped" status for PDF upload, multi-language, medication, or sharing controls | Document is a snapshot from 2026-02-07. No mechanism to update it when features ship. Captures ideas, not shipped state. |
| **User Research Synthesis** (`01-user-research-synthesis.md`) | Current product state to contextualize needs | Lists "Can't upload PDFs directly" as a barrier, citing AYA interview | Research synthesis was written before the feature shipped. Never revised. |
| **Completed Features Log** (`completed-features-jan2025-feb2026.md`) | What was actually built | 860 items with epic titles, but titles are technical/internal ("Revise Event Detail screen", "Maintenance Q4") — not mapped to user-facing capabilities | No feature→capability mapping exists. You'd need domain knowledge to know "DPMA-1489 Appointment Preparation - phase 1" means sharing controls were improved. |
| **Confluence** (11 pages read) | Current product state | Strategy, research, and brand docs describe the vision, not current shipped state. Care Circle v2 PRD describes the target, not what's live. | Confluence is forward-looking (plans, specs, research). No "current product capabilities" page exists. |
| **BIGB Jira Board** (via feature-ideas-overview.md) | Idea statuses including shipped | Ideas marked "Parking lot" even when features may have shipped | Jira idea board is not updated when ideas ship via the DPMA delivery board. Two boards, no sync. |

### Structural issues

1. **No "current product state" document exists.** Product-context.md was meant to be this but was never filled in. The canvas had to infer current state from research documents, which describe problems — not solutions.

2. **Research documents are never revised when features ship.** The user research synthesis (2026-02-02) says "Can't upload PDFs" because that was true at the time. When PDF upload shipped, nobody went back to update the research document.

3. **Two Jira boards are disconnected.** BIGB (ideas/discovery) and DPMA (delivery) don't cross-reference. An idea can ship on DPMA without its BIGB status being updated.

4. **Completed features log uses internal epic names**, not user-facing capability names. You can't grep for "PDF upload" or "multi-language" in the log — you'd need to read each epic description to understand what capability it delivered.

5. **No feature→persona mapping was ever created.** Even if shipped features were documented, there's no mapping of "this feature serves these user segments" — which is exactly what the canvas tried to build from scratch.

---

## Documentation Updates Needed

### Confluence updates

| Page | What to update | Priority |
|---|---|---|
| **Product Canonical Description** (or new page) | Add "Current Product Capabilities" section listing all shipped user-facing features with brief descriptions | High |
| **Strategy - Reaching Focus Patients** | Note which capabilities currently serve each focus area (pregnancy, neuro, oncology) | Medium |
| **Care Circle v2 PRD** | Clarify what's CC v1 (shipped) vs CC v2 (in development) — current sharing controls, section selection, personal messaging are v1 | Medium |
| NEW: **Shipped Features → User Capability Map** | Create a living document mapping internal epics to user-facing capabilities and which personas they serve | High |

### Local file updates

| File | What to update | Priority |
|---|---|---|
| `pm-workspace/context/product-context.md` | Fill in [TODO] sections. Add shipped feature inventory. | High |
| `pm-workspace/data/research/feature-ideas-overview.md` | Add "Status: Shipped" for PDF upload, multi-language translation, medication management, sharing controls, event labeling idea. Cross-ref DPMA epics. | High |
| `pm-workspace/data/research/feature-ideas-user-insights.md` | Add notes where user problems have been addressed by shipped features (e.g., PDF upload no longer a barrier) | Medium |
| `pm-workspace/specs/ideas/activation-strategy/01-user-research-synthesis.md` | Update section 2.3 "Functional Barriers" — PDF upload is resolved, sharing controls partially resolved | Medium |

### Process improvement

| Issue | Suggested fix |
|---|---|
| Research docs go stale | Add a "Resolved by" column to barrier/problem tables. When a feature ships, mark the barrier as resolved with the DPMA epic link. |
| BIGB ↔ DPMA disconnect | When a DPMA epic ships that addresses a BIGB idea, update BIGB status to "Shipped" with link. Could be a checklist item in the shipping workflow. |
| No current-state doc | Add "Update product capabilities doc" to the shipping checklist (pm-workspace/how-we-run-product/shipping-and-release/README.md) |
| Completed features log is unreadable | Create a quarterly "capabilities changelog" in plain language alongside the raw Jira export |

---

## Impact on Canvas

These corrections change the coverage assessment for several personas:

| Persona | Before correction | After correction |
|---|---|---|
| Language Barrier Patient | "Major Gap — zero dedicated features" | Partial — translations exist (Turkish, Arabic, English) but no dedicated UX, content, or onboarding |
| Self-Manager | "PDF upload is top barrier" | PDF upload is resolved; activation gap remains the main issue |
| Cancer / Severe Care | "All-or-nothing sharing" | Section-level sharing exists; who-to-share-with is the actual gap |
| Chronic Disease | "No medication management" | Basic medication feature exists; advanced features (diary, multi-condition) are gaps |
| All patient personas | "No document vault" | Partial vault via user profile; full vault (BIGB-58) still not built |

---

*This document should be used to update Confluence pages and local files, then archived.*
