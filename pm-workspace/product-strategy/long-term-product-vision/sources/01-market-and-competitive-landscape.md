# Source Synthesis 01 — Market & Competitive Landscape

> Distills: `product-strategy/market-trend-analysis/` (00-scope, 02-map-v2, phase2-A/B/C, briefs G/H/K1/K2/K3) and `specs/care-brain/competitive-analysis.md`.
> A synthesis for the long-term vision, not a copy. Originals carry full citations.

## The one thing

The patient-friendly summary is commoditizing from every direction and will be a free byproduct of NL/BE portals around **2027-28**. The defensible ground is the patient-owned, family-shareable, cross-provider, consent-first relationship: a **network moat, not a feature moat**. The recorded visit is the wedge, not the product.

## Who is taking the artifact (and how fast)

| Vector | Players | Status |
|---|---|---|
| Portal / EHR | ChipSoft HiX "Patiëntvriendelijke brief"; **ZAS Antwerp live (~40k letters/yr, Apr 2026)** | Shipping now in NL/BE; standard-of-care ~2027-28. The real artifact threat. |
| Incumbent EHR | Epic "Ask Emmie" | Patient-direct 2026-27, no confirmed EU deploy yet |
| Scribes | Abridge ("Abridge for Patients" consumer app ships today), Ambience, Nabla, DAX | Abridge already built Ditto's shape (US-only, deprioritized). Others stay B2B. |
| B2C translators | Simply Onno (DE, 60k+ summaries), mein-arztbefund, Befunddolmetscher | Real consumer traction on comprehension. Document-only, single-shot, no circle. |
| Foundation labs | ChatGPT Health, Claude for Healthcare, Gemini Health Coach (all Jan 2026) | Sherlocked "explain my record" at billion-user scale. US-first, individual, horizontal. |
| Scheduling incumbent | Doctolib (Consultation Assistant + Doctolib Parents) | The one combining distribution + patient summary + patient AI. Watch hardest. |
| Direct EU analog | Clareco CoPilot (NL/BE) | Pre-traction. The only true recording→patient-summary EU match found. |
| Direct US analog | Kin Health ($9M, May 2026) | Same wedge + care-circle loop. Geography protects for now. |

**The open gap that still holds**: patient-initiated + cross-provider + recording-based + multilingual + oncology-deep + family-shareable. Nobody owns this. The threat is commoditization, not a built clone.

## What the labs cannot easily do (the structural gaps)

1. **US-first**: EHR connectors are US/FHIR-gated; EU connectivity (MedMij/PGO, EHDS) is harder and not their priority.
2. **Individual, not family**: all ground in *your* data for *you*. None has a care-circle / multi-member loop.
3. **Horizontal, not condition-deep**: none is built for the oncology journey.
4. **Ungrounded & not GDPR-safe**: ~50% of chatbot health answers are "problematic" (BMJ Open); general LLMs are not GDPR-compliant.

## AI trend signals to ride

- **Voice going primary** (OpenAI merged voice into the main UI; patient comfort with AI listening 21%→60% in two years). Direct tailwind for a spoken-visit product.
- **Agentic is the dominant frame but clinically hype-ahead-of-reality** (only 3% of orgs have agents live; Gartner: 40%+ agentic projects cancelled by 2027). The viable surface is **low-risk action** (prep questions, reminders, family updates, route-the-right-summary), not diagnosis.
- **Generative UI** moving to production: value migrates from fixed screens to a trusted data graph + actions an assistant renders against.
- **Thin-wrapper risk is real and VC-validated as fatal**; the escape is vertical + regulated + proprietary data + embedded workflow. Ditto's care-circle + EU trust + oncology depth is that profile.

## The trust battleground (an opening)

Scribe hallucination scandals (Ontario AG: all 20 approved scribes hallucinating, ~5,000 doctors) and consent lawsuits make verified, provider-sourced, consent-first, EU-native a real wedge. **OpenEvidence ($12bn) withdrew from EU/UK in May 2026 over AI-Act uncertainty** — the best-funded clarity player vacated Ditto's home market. A Rotterdam company built EU-native inherits ground the giants are fleeing. Caveat: consumers under-value privacy, so sell trust B2B/B2B2C and usefulness B2C.

## Reimbursement landscape (the money)

- **Reimbursement is achievable at Class I** (95% of German DiGA are Class I). The wall is a clinical RCT, not certification.
- **Path 1 (stay light)**: NL B2B channels (DBC-embedded, facultatieve prestatie, the €2.8B IZA transformation pot, supplementary insurance) + the forming **diga.nl** provisional scheme. Class-I-friendly, near-term.
- **Path 2 (go clinical, DiGA)**: ~€1.5M-3.5M over 2-3 years, ~€227/90 days after haircut, and **no live oncology-companion DiGA exists** (Mika and CANKADO both failed to convert). Poor base rate.
- **Hello 24/7** proves the insurer-reimbursed care-circle model in NL: €5.83/mo, reimbursed 100% by Zilveren Kruis + Menzis via supplementary insurance.
- The "care intelligence layer" ambition (interpret/flag/triage) is the exact tipping point into Class IIa + AI-Act high-risk. Decide intended-purpose deliberately.

## Implications for the vision

- Do not build the moat on the summary. Build on relationship, trust, oncology depth, and patient-owned cross-provider data.
- The labs leave three doors open: EU, family, and condition-depth. The vision should walk through all three.
- Reimbursement is a viable channel but a poor spine. Monetization must work without it.
- Trust/consent is a B2B/B2B2C asset (the OpenEvidence vacancy), not primarily a consumer selling point.
