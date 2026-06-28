# C2 — The Personal Health Record as MULTIPLIER (not destination)

> Market Deep Dive · Part II · Synthesis chapter. Created 2026-06-09 by Mewtwo.
> Rules on v2's thesis: owning data is low value alone; integrating it multiplies the intelligence layer. Draws on F3 (PHR/data integration) and F4 (EHDS).
> Shared framing (Part III covers it): money in this space is B2B everywhere; none of these is a standalone business for Ditto; the recurring understood-conversation moment is Ditto's rare asset and the till. Integrate, don't own the data layer.

## 1. Verdict up front

**The evidence upholds the thesis, strongly. Owning the record is not a business; integrating it to multiply intelligence is the whole game in 2026.** Three clinching datapoints:

- **OpenAI did not build a record — it connected one.** ChatGPT Health (Jan 2026) plugs into a patient's medical records via **b.well** so the AI can reason over the full picture. The most-watched company in AI executed v2's exact thesis in a single quarter: the value is the reasoning on top, not the vault underneath.
- **The 18-year PHR graveyard is consistent and recent.** Google Health, HealthVault, Vivy, Dossia all died of the same four-part failure: data without insight, no frequency, no actionable job, gatekept integration. Even Apple's records feature never became sticky, and Apple *shelved* its AI health coach (Mulberry) in Feb 2026.
- **Even a free, state-handed record draws no demand.** Germany's ePA flipped to opt-out and went <1% → ~70M accounts in weeks, yet active use (logging in, uploading, sharing) "remains far less widespread." NL's MedMij PGOs: ~207k users despite a national mandate and free access. Removing integration cost does not create demand for a bare record.

## 2. Where value accrues (the value chain)

| Layer | What it is | Who pays | Verdict for Ditto |
|---|---|---|---|
| **Own the record** (consumer vault/PGO) | Patient-facing "your data in one place" | Almost nobody | **Graveyard.** Free utility at best, never a business. The trap to avoid. |
| **Pipe the record** (B2B aggregation infra) | Retrieve, normalize, dedupe, deliver FHIR | Payers, health systems, AI platforms | **A real business, but a rented moat** (b.well, Particle, Health Gorilla). $40-50M rounds. Not Ditto's lane and not its strength. |
| **Reason over the record** (intelligence) | AI that uses the longitudinal record to advise | TBD (consumer subs, enterprise) | **The frontier, just opened.** ChatGPT Health is the proof shot. This is where Ditto plays. |

The pattern: the consumer vault dies; value moved *underneath* it (plumbing) and *on top* of it (intelligence). Ditto sits on top, using the plumbing as a free input.

## 3. EHDS reality

EHDS is two economies in one name. The money is in **secondary use** (pooled data sold to pharma/research via national access bodies — IQVIA, TriNetX, Datavant, Owkin, Aridhia already own it). That track is off-mission, penalty-heavy (fines to €20M/4% of turnover), and contradicts Ditto's trust position. **Primary use** (a patient moving their own verified record) is what would multiply Ditto, but it is EU-project-stage, gated to **~2029** (Group 1) and **~2031** (images/labs).

| Question | Answer |
|---|---|
| Can anyone own the consumer "bring your record anywhere" broker role? | **No.** The one consumer primitive (xShare "Yellow Button") is being built as a *public good apps embed*, not a proprietary moat. The EU is publicly funding both record-sharing *and* comprehension (Gravitate Health) — validation the jobs are real, warning the concepts are not defensible. |
| Near-term move if record-ingestion matters? | **A MedMij integration for NL** — real, available today, doable by a small team. Ingests a verified NL record without invoking EHDS or any "launching partner" status. |
| Timeline read | EHDS is a **2029+ architecture signal, not a 2026 opportunity.** "Launching partner" is close to a distraction. |

Cheap insurance, not a roadmap line: keep the data model EEHRxF-aware so Ditto can embed the xShare primitive and ingest cross-border records when primary use goes live ~2029.

## 4. White space + risks for Ditto

| | |
|---|---|
| **Play** | Integrate the record as fuel for the intelligence layer. Treat ePA/MedMij/EHDS as free inputs. **Never pitch as "another PGO"** — that ecosystem already proved consumers will not show up for the rail itself. |
| **Why it compounds** | Ditto already has the frequency the PHR graveyard never had: the medical conversation, repeated (weekly in oncology). The record makes each *understood moment* smarter — better summaries, sharper follow-up prep, richer family/coordination updates, safer "what should I do" advice. The moment gives the record a reason to be opened; they reinforce each other. |
| **Risk 1 — rented moat / data-tap shutoff** | Particle v. Epic: Epic cut off Particle's data access in 2024; an oncology network reported 2,800+ patients' care harmed. In EU form, the gatekeepers are national nodes (MedMij/MyHealth@EU) and provider EHRs. The regulatory tailwind mitigates but does not eliminate this. **Flag for Merlijn: who can turn off Ditto's data tap, and what is the fallback?** |
| **Risk 2 — record + AI is necessary but not sufficient** | Apple shelving Mulberry, and ePA's 70M-accounts-but-inert reality, both warn that bolting AI onto a record does not auto-create trust or a return visit. Ditto's edge is that it starts from an *already-frequent, already-trusted* moment and adds the record to deepen it — not the reverse. **That sequencing is the bet.** |

## 5. Verdict against the 4 core questions

| Question | Answer |
|---|---|
| **What** | Integrate the record as a multiplier for the intelligence layer. Do not own the data layer, do not build a destination vault. |
| **Who** | Severe-disease patients (oncology first) and their loved ones — people who already return for the conversation moment and whose full longitudinal picture makes the intelligence dramatically better. |
| **Moat** | The intelligence and the trust relationship, *not* the record or the rail. The plumbing is rentable and the sharing/consent primitives are commoditising public goods. The defensible asset is product quality on top of an already-frequent, trusted moment. |
| **Monetize** | Not the record (it pays zero, everywhere). Money is B2B; the recurring understood-conversation moment is the asset that monetizes (Part III). The record makes that moment worth more, not less. |

**Merlijn's named trade-off — data-portability vs adding intelligence to data users already give Ditto:** the evidence resolves it cleanly toward **intelligence-first**. F3 shows owning/porting the record is a graveyard and the value is the reasoning on top; F4 shows EHDS portability is a 2029+ signal, not a 2026 prize, and the consumer broker role cannot be owned. Going all-in on data integration now would slow the one thing that is differentiating and available today — intelligence on the data users already put into Ditto. **Build the intelligence; do the cheap MedMij integration when record-ingestion measurably sharpens it; design EEHRxF-aware for 2029. Integrate, don't own. Thesis upheld.**
