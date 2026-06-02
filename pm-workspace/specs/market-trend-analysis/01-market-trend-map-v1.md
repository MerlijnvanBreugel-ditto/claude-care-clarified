# Market & Trend Map (v1) — Outside-In Synthesis

> Synthesis of Phase 1 briefs A–E. Created 2026-05-30. Status: v1, pre-Phase-2.
> Outside-in only. Feeds Merlijn's combined overview alongside the product + company-strategy agent outputs.
> Sources live in the per-stream briefs (A–E) in this folder; each carries numbered citations.

## The one thing

The patient-friendly visit summary, Ditto's core artifact, is being commoditized from three directions at once. The defensible ground is not the summary. It is the **patient-owned, cross-provider, family-shareable, consent-first care relationship** — and the demand for exactly that is now validated, not hypothetical.

## Convergence: three forces closing on the summary

| Direction | Who | Status | What it means |
|---|---|---|---|
| **From above** (incumbents) | Epic "Emmie" + AI Patient Summaries | **Live in Dutch hospitals** (ETZ Tilburg, UMCG, Amsterdam UMC). 85% of Epic customers on its genAI suite. | The in-portal, institution-delivered summary is being taken by the EHR. Same job, same cohort. |
| **From beside** (scribes) | Abridge, Nuance/Microsoft DAX, Suki, Heidi | Patient-facing after-visit summaries now a standard feature. **DAX into NL/BE early 2026.** | The *artifact* is taken, but via the institution's EHR. They take the summary, not the relationship. The recording step risks being bypassed. |
| **Head-on** (startups) | **Kin Health** ($9M seed, May 2026, Maveron), Hedy AI, Medcorder | Direct: record → plain summary → share with family. Care-circle loop included. | The category and the care-circle thesis are both validated by funded entrants. US-dominated; **geography is currently Ditto's main protection.** |

**Implication:** stop treating the summary as the moat. It is becoming a free EHR/scribe byproduct. Compete on what none of the three hold: a patient-initiated, cross-provider, multilingual, family-shareable, consent-first layer with the care circle as the relationship.

## Demand is validated (Stream D)

Every vector points at the same user, the same moment, the same problem:
- **Literacy/recall:** only 12% of US adults health-literate; patients forget 40–80% of a visit immediately, half of the rest wrong. ~$236B/yr cost. Cognitive, not just educational.
- **Caregivers:** 63M in US (+45%/decade), $1T unpaid labor. NL 1.9M informal caregivers, €17–30B/yr — a parity signal, not a lagging one.
- **Chronic burden:** 76% of US adults have ≥1 chronic condition; 65+ is fastest-growing and the worst-served on literacy.
- **Adoption:** consumer health-AI use 16%→32% in a year; EU 12–24mo behind. Killer use case is convenience, not accuracy (only 18% rate chatbots highly accurate) — a window for provider-sourced, verified output.
- **Behavior:** 31–38% of summary-engagers already share with someone. Care-circle behavior exists without prompting. Bottleneck is quality (29% cite jargon), not willingness.

**Read:** NL/EU is an ideal beachhead. Ditto's use case sits on top of structural, quantified, growing demand.

## The money (Stream B)

- **DiGA is the only mature EU scheme** (~56–59 apps, >1M prescriptions, 73M+ covered). France (PECAN) and Belgium (mHealthBELGIUM) live but small. **NL has no app-on-prescription route** (digital care funded inside insurer/NZa tariffs).
- **Precedent that matters: Mika**, a reimbursed cancer *companion* (not a treatment), under DiGA's "structural and procedural improvements" track that explicitly pays for health literacy, adherence, care coordination, patient sovereignty. **Near-exact match to Ditto's profile and oncology wedge.**
- **Sword Health bought into DiGA via Kaia** ($285M, Jan 2026). The EU care-layer prize is won via reimbursement, not app-store revenue.
- **Trend:** access broadening, evidence bar rising together (DiGA 2.0, Feb 2026: real-world outcome reporting, ≥20% price-at-risk, 6 apps delisted, prices down ~46%).
- **Honest gap:** Ditto as-is is likely Class I / borderline non-device and qualifies for nothing today. DiGA is reachable but means CE-marked oncology care-companion + prospective study (est. 18–36 months, 6–7 figures). Faster money: the Dutch B2B route inside existing hospital/insurer tariffs.

## The rules (Stream A)

- **Near-term, cheap, mandatory:** AI Act **Article 50 transparency stays at 2 Aug 2026** — patient-facing AI must perceivably disclose it is AI. (Digital Omnibus pushed the *high-risk* deadlines to Dec 2027 / Aug 2028, not yet in the Official Journal.)
- **The classification cliff is the central strategic fork.** A non-diagnostic summary can stay Class I / out-of-scope. The moment the product "provides information used for diagnostic or therapeutic decisions," it becomes Class IIa (notified body) **and** AI-Act high-risk. The "care intelligence layer" ambition is exactly what trips this. **The same threshold that triggers the regulatory burden is the one that unlocks DiGA reimbursement.** So the A and B findings are the same decision.
- **You can't outsource AI-Act compliance to your LLM vendor** — building on a GPAI model means Ditto inherits the full system obligations.
- **EHDS** (in force Mar 2025) is a 2029+ portability/data tailwind — an architecture signal, not 2026 work.

## The trust battleground (Stream A, incident scan)

- Ontario AG (12 May 2026): *all 20* approved AI-scribe vendors hallucinating, ~5,000 doctors affected. Whisper/Nabla up to 8/10 transcripts with hallucinations. BMJ: 49.6% of chatbot health answers problematic. Pennsylvania v. Character.AI (5 May): bots posing as doctors.
- **The scribe/transcription cluster is Ditto's exact failure-mode exposure** (cf. the internal medication stop/continue inversion incident). One bad output is existential.
- **But it is also the positioning wedge:** provider-sourced, verified, consent-first, EU/GDPR-native. The US field faces consent lawsuits; EU trust is a timely, defensible edge.
- Caveat: a few incident stats came from secondary aggregators (primary blocked); re-verify in Phase 2.

## Foresight (the predictor)

### Timing / S-curve stage

| Trend | Stage | Window |
|---|---|---|
| Incumbent (Epic) patient-summary AI | Early-majority US; **entering NL now** | Encroachment on home turf is immediate |
| Scribe → patient summary | Early, ~12mo old, accelerating; DAX NL/BE early 2026 | ~12–18mo before standard |
| Direct consumer clones (Kin etc.) | Very early (seed) | ~18–36mo before category consolidates |
| EU consumer health-AI adoption | Early; 12–24mo behind US | Steep climb imminent |
| EU reimbursement (DiGA) | Maturing + tightening | Enter while the bar is still climbable |

### Two-by-two scenario (the two biggest uncertainties)

Axes: **Speed of encroachment on the patient relationship** (slow ↔ fast) × **Is clinical-grade/reimbursement table stakes for the EU care layer?** (no ↔ yes).

| | Encroachment SLOW | Encroachment FAST |
|---|---|---|
| **Reimbursement NOT required** | *Open field* — current path works; win on growth, retention, care-circle love. | *Race for the relationship* — summary free everywhere; winner owns the patient + family relationship and the experience. **(Most likely)** |
| **Reimbursement REQUIRED** | *Build the moat deliberately* — time to pursue CE/DiGA while incumbents lag in EU. | *Squeezed* — Epic + scribes own the artifact and DiGA-grade is needed to monetize. Go clinical fast or get boxed in. |

**Most-likely landing:** encroachment is **fast on the artifact** (Epic in NL now, DAX early 2026) but the **patient relationship is still open** (all incumbents/scribes deliver via the institution; none own patient-as-buyer + family loop). Reimbursement gates the *big* prize but is not required for a near-term B2B-tariff or consumer play. Ditto sits in **"Race for the relationship," with reimbursement as an optional-but-valuable second act.**

### Trend → implication → threat/opportunity ledger

| # | Signal | T/O | Horizon | So what for Ditto |
|---|---|---|---|---|
| 1 | Epic Emmie/AI summaries live in NL hospitals | 🔴T | 12–18mo | Don't compete on the in-portal summary; differentiate on patient-owned + cross-provider + family. |
| 2 | Scribes (DAX) into NL/BE producing patient summaries | 🔴T | 12–18mo | Artifact commoditizes; the recording step is bypassable. Accelerate the relationship/care-circle moat. |
| 3 | Kin Health funded clone with care-circle loop | 🟠T | 12–36mo | Care circle is not unique forever. Speed in EU while geography protects. |
| 4 | Demand validated; EU 12–24mo behind US | 🟢O | now–3yr | Confidence to push; ride the adoption curve into NL/EU. |
| 5 | Mika: reimbursed non-curative cancer companion (DiGA) | 🟢O | 1–3yr | A real EU monetization path exists for exactly Ditto's profile. Germany as a reimbursement beachhead. |
| 6 | Classification cliff = reimbursement gate | 🟠T+O | 1–3yr | Decide the fork deliberately; don't drift into Class IIa by accident, don't forgo reimbursement by neglect. |
| 7 | AI Act Article 50 transparency, 2 Aug 2026 | 🔴T | <12mo | Ship the AI-disclosure UX now. Cheap, mandatory. |
| 8 | Scribe hallucination scandal + consent lawsuits | 🟢O / 🔴T | now–3yr | Make verified/provider-sourced/consent-first the brand. One Ditto error is existential: invest in guardrails. |
| 9 | EHDS portability/data access | 🟢O | 3–5yr | Architecture signal for cross-provider + model training. Not 2026 work. |
| 10 | Sword/Kaia → DiGA land-grab | 🟠T | 3–5yr | The big EU care-layer prize ultimately requires clinical-grade. |

## Recommended Phase 2 deep dives (pick 2–3)

1. **The classification × reimbursement fork (A×B).** A device-classification read on Ditto's actual feature set + the DiGA structural/procedural study-design path, incl. a Mika teardown. Gates the entire EU monetization ceiling. *Highest stakes.*
2. **The home-turf encroachment race (C×E).** Native-language EU competitor sweep (Phase-1 English search under-counts regional players) + Epic Emmie NL rollout pace + DAX NL/BE timing, to size how fast the artifact commoditizes and where the relationship gap stays open.
3. **Trust positioning (A incidents).** Turn the scribe-hallucination/consent landscape into a defensible "verified, consent-first" position + the guardrail bar Ditto must hold (tie to the internal inversion incident).

## Deferred (Merlijn's calls)
Capital/M&A; tech/product trends (wearables ladder, generative UX, agentic); defensibility as Merlijn's own strategic conclusion drawn from this map.
