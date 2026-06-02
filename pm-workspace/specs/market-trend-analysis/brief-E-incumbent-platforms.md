# Brief E: Incumbent Platforms — Can They Already Own the Front Door?

*Workstream E of the Ditto market/trend scan. Scan date: 2026-05-30. Focus: do large incumbent health platforms already deliver — or are they fast-moving to deliver — patient-friendly visit summaries and AI health understanding in EU/UK?*

---

## Executive Summary

- **Epic/MyChart is the most credible near-term threat in the EU.** It is already live in Dutch hospitals (ETZ Tilburg, UMCG Groningen, Amsterdam UMC) with AI patient summaries and is rolling out Emmie, a 24/7 EHR-backed AI assistant that explains labs, answers visit questions, and handles scheduling. 85% of Epic's global customers are already live with its generative AI suite. [Inference: EU rollout of Emmie lags the US but is structurally inevitable given Epic's EU headquarters build-out near Bristol.]
- **Apple Health+ is coming in 2026 but is a wellness play, not a visit-summary play.** Its AI coaching ambition is real, but there is no evidence it will handle post-visit clinical summaries. ChatGPT Health integration is the more direct overlap — it already lets users link MyChart portals and summarize visit notes.
- **Google is moving fast on consumer health AI but remains provider-adjacent.** Its "Personal Health Agent" research and Fitbit enhancements are lifestyle-layer plays. Clinical summarization partnerships (Hackensack Meridian) are B2B, US-only. No direct EU patient-summary product.
- **MedMij/PGO is structurally mandated in NL but chronically under-adopted and offers no AI layer.** 1,000 new users/day sounds significant; against a Dutch adult population of ~14M it is negligible. PGOs show raw data pulled from EHRs — no summarization, no AI, no narrative. Roadmap items for patient-friendly language arrive H2 2026.
- **The NHS App is deploying AI for triage and discharge letter drafting, not patient-facing visit summaries.** "My Companion" is a planned condition-information tool, not a recording-to-summary pipeline. UK ambient scribing market is active (19 approved suppliers) but outputs go to clinicians, not patients.
- **Ditto's window is real but compressing.** Epic's Emmie is the clearest encroachment vector, especially in NL where Epic penetration is already high. The gap to close: Epic requires hospital IT adoption; Ditto deploys directly to patients. Speed and independence are the moat — for now.

---

## Platform Scan

| Platform | Patient-summary capability today | AI moves (2025–2026) | EU / NL availability | Threat read |
|---|---|---|---|---|
| **Epic / MyChart** | AI-generated plain-language summaries of imaging results and after-visit instructions live in MyChart. Emmie explains labs, answers clinical questions in chat and SMS. 85% of Epic customers live with genAI. | Emmie broadened to billing + scheduling; MyChart Central (single login across orgs, Nov 2025); AI agents framework for custom hospital bots. [1][2][3] | **Yes — NL now.** ETZ Tilburg + UMCG Groningen among first global sites for AI Patient Summaries [4]. Amsterdam UMC on MyChart. UK, Denmark, Finland, Norway deployments ongoing. New EU HQ campus approved near Bristol. | **HIGH** — same job to be done (explain the visit in plain language), same oncology/complex-care user base, already in NL hospitals. Constraint: requires hospital adoption; Ditto is patient-direct. |
| **Apple Health / Health+** | Today: wearable + records aggregation, no visit summaries. ChatGPT Health integration (launched 2026) lets users link Apple Health + patient portals and ask questions about visit summaries. [5][6] | Health+ subscription (AI wellness coach + personalized nutrition, iOS 26/2026). Revamped Health app with four major upgrades in iOS 26. Siri integration for contextual health Q&A. [7][8] | Health app: global. Health+: US launch first — EU timing unconfirmed. ChatGPT Health: US-initial. | **MEDIUM** — ChatGPT Health is a real overlap (visit note Q&A). Health+ itself is wellness coaching, not visit-summary. EU lag gives Ditto a runway window. |
| **Google Health / Fitbit** | No direct patient-facing visit summary product. Lab summarization agent (Hackensack Meridian) is B2B, US. AI Mode in Search handles health questions from the general population (~1B health queries/day). [9][10] | "Personal Health Agent" research (Fitbit + AI coach); Fitbit + CGM + medical record linking announced at The Check Up 2026; $10M clinician AI training. [11] | Health Connect: Android global. Fitbit + medical record linking: US-focused. No EU patient-summary product identified. | **LOW (now) / MEDIUM (2027+)** — no EU patient visit-summary product today. Long-term, a Google-native health agent that reads your linked records is directionally threatening. |
| **MedMij / PGO (NL)** | Raw data access: GP notes, medication lists, lab results pulled from EHRs. No AI layer, no plain-language summaries. "Patient-friendly terms" project is on the 2026 roadmap, not live. 1K new users/day; ~4,600 certified providers. [12][13] | Granular data services (test phase 2026); new data types (pathology, screening, paramedical) expected late 2026; questionnaire modules H2 2026. No AI summarization announced. | **NL-only by design.** EU equivalents (EHDS) exist but are early-stage. | **LOW** — MedMij is a data plumbing layer, not a patient experience layer. Ditto complements it rather than competes. Risk: if a well-funded PGO app adds AI summarization on top of MedMij data, that could crowd Ditto's NL turf. |
| **NHS App (UK)** | Appointment booking, prescription ordering, GP record access, test results. No patient-facing visit summary today. AI Discharge Summary tool (AI-DSUM) live in 2 London trusts — outputs to clinicians, not patients. [14][15] | "My Companion" (condition Q&A, not yet launched). Rapid Health AI triage rolling to 200 practices (2026). 19 approved ambient voice (AI scribe) suppliers — all clinician-facing. [16][17] | **UK only** (NHS-specific). | **LOW (UK today)** — no patient-facing visit summary product, no near-term roadmap item matching Ditto's core use case. Ambient scribing outputs stay in EHR. Ditto's UK opportunity is precisely in this gap. |

---

## Implications for Ditto

**The core threat is Epic, not Apple or Google.** Epic is building toward the same outcome Ditto already delivers — plain-language explanations of clinical encounters, available in the patient's pocket. The difference is deployment model: Epic requires a hospital IT decision; Ditto is patient-initiated. That asymmetry is Ditto's moat, but it is not permanent. As Epic's EU penetration deepens and Emmie expands to European hospitals, the overlap will grow.

**Three strategic responses worth considering:**

1. **Speed on oncology depth.** Epic's Emmie is general-purpose; Ditto can go deeper on oncology-specific comprehension (treatment plans, clinical trials, side-effect navigation). Condition-specific depth is harder for a horizontal platform to replicate quickly.

2. **Institutional partnership as a hedge.** Rather than waiting for hospitals to choose Epic's patient AI, Ditto can position as the patient-owned layer that coexists with MyChart — complementary to the EHR rather than a competitor. Several NL academic hospitals already use Epic; Ditto partnerships there are both revenue and defensibility.

3. **MedMij/PGO as a distribution lever, not a competitor.** MedMij delivers raw data; Ditto provides understanding. A PGO integration (pulling structured records into Ditto for richer context) could strengthen Ditto's product while differentiating from Epic's closed ecosystem.

**The UK timing is favorable.** The NHS App has no patient-facing summary ambition in its near-term roadmap. Ambient scribing is clinician-output only. Ditto entering UK oncology centers now faces no incumbent offering the same job. That window will close within 2–3 years.

---

## Sources

1. [Epic AI for Patients — epic.com](https://www.epic.com/software/ai-patients/)
2. [Epic Emmie — Ask Emmie EHR-backed AI chatbot (TechTarget)](https://www.techtarget.com/patientengagement/feature/Epics-Ask-Emmie-offers-EHR-backed-AI-chatbot-option-for-patients)
3. [Epic UGM 2025: AI tools roundup (Fierce Healthcare)](https://www.fiercehealthcare.com/ai-and-machine-learning/epic-rolls-out-ai-charting-and-more-built-automation-clinicians-and)
4. [Epic European Group Meeting 2025 — Dutch hospitals AI Patient Summaries (Epic)](https://www.epic.com/epic/post/healthcare-innovators-showcase-real-world-outcomes-at-egm-2025/)
5. [Apple Health + ChatGPT 2026 integration (Gadget Hacks)](https://apple.gadgethacks.com/news/apple-health-chatgpt-game-changing-2026-integration/)
6. [OpenAI launches ChatGPT Health (Medical Economics)](https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot)
7. [Health+ subscription service expected 2026 (MacRumors)](https://macrumors.com/2025/11/10/ai-apple-health-service-still-coming/)
8. [Apple Health revamped app coming iOS 26 (9to5Mac)](https://9to5mac.com/2026/01/11/apple-health-new-features-and-overhaul-coming-ios-26-4/)
9. [Google Health AI updates — The Check Up 2026 (Google Blog)](https://blog.google/innovation-and-ai/technology/health/google-check-up-health-ai-updates-2026/)
10. [Google Check Up 2026 — UCI Institute for Future Health](https://futurehealth.uci.edu/healthcare-news/googles-2026-health-ai-updates-highlight-a-shift-toward-more-proactive-and-agentic-care/)
11. [Google Cloud health AI agent partnerships (Healthcare Dive)](https://www.healthcaredive.com/news/google-cloud-ai-agent-partnerships-hackensack-meridian-iks-health/802980/)
12. [MedMij Roadmap 2024–2026 (medmij.nl)](https://medmij.nl/media/medmij-presenteert-geactualiseerde-medmij-roadmap-2025-2026/)
13. [MedMij: wat kun je in een PGO? (medmij.nl)](https://medmij.nl/wat-kun-je-in-een-pgo/)
14. [NHS App AI discharge summary tool rollout (EMJ Reviews)](https://www.emjreviews.com/innovations/news/health-ai-tech-show-nhs-england-rolls-out-ai-discharge-summary-tool/)
15. [AI-assisted discharge letters — NHS FDP (Digital Health)](https://www.digitalhealth.net/2025/08/ai-assisted-tool-on-fdp-will-help-write-hospital-discharge-letters/)
16. [NHS App AI doctor feature — Healthwatch Devon](https://www.hwdpt.org/news/2025-06-26/nhs-app-future-will-include-ai-doctor)
17. [AI tool — 1M patients book via NHS App (Digital Health)](https://www.digitalhealth.net/2026/04/ai-tool-allows-a-million-patients-to-book-appointments-via-nhs-app/)
