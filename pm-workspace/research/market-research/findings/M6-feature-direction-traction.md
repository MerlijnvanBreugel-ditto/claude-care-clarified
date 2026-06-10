# M6 — Feature-Direction Traction Scan

**Scope.** Market traction across the five product directions ditto.care is considering: (1) AI health assistants / general consumer health AI, (2) grounded/cited answer engines (OpenEvidence anchor), (3) digital/AI health coaches, (4) symptom tracking, (5) health journaling & logging. For each: market state, named players with traction/funding, success factors, cautionary tales, and retention/engagement evidence.

**Prepared for:** ditto.care (EU/Netherlands digital-health; AI appointment summaries → "Living Health Companion"). **Access date:** 2026-06-10. **Date bias:** 2024–2026 prioritized.

**Source tiers:** Tier 1 = peer-reviewed / official / analyst; Tier 2 = press; Tier 3 = blog / self-report (FLAGGED). **Confidence:** High / Medium / Low. ⚠️ = US→EU transferability caveat. Most traction/usage data below is US-centric; EU adoption lags and the regulatory bar is higher (see §1 and §6).

---

## Key takeaways

- **General LLMs are the default consumer health AI, not specialist apps.** ~32% of US consumers used an AI chatbot for health info in 2025 (up from 16% in 2024), and **74% of those reached for general tools like ChatGPT/Gemini** rather than provider or payer bots ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/); High). OpenAI says ~1 in 4 of its 800M+ weekly users prompt about health weekly ([Fierce Healthcare, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says); Medium). Any new entrant competes against a free, ubiquitous default.
- **The grounded/cited answer engine is the breakout B2B2C model — but on the clinician side.** **OpenEvidence reached a $12B valuation (Jan 2026), >40% of US physicians as users, ~20M monthly clinical consultations**, by grounding answers in licensed peer-reviewed literature (NEJM, JAMA) ([CNBC, 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html); High). No equivalent consumer-facing grounded engine has reached comparable scale yet — an open lane.
- **"Grounded & cited" is becoming the trust standard.** 2025 medical-RAG research (MedTrust-RAG, MEGA-RAG) explicitly builds *citation-traceability and principled refusal* to cut hallucination — but peer-reviewed work also warns RAG systems "can be dangerous medical communicators" if grounding is shallow ([arXiv 2502.14898, 2025](https://arxiv.org/pdf/2502.14898); High).
- **Digital/AI coaches show real but modest clinical effect and chronic engagement decay.** Lark (35M+ patient interactions, $162M raised) and Omada have payer traction ([MobiHealthNews](https://www.mobihealthnews.com/news/lark-scores-100m-digital-chronic-care-management); Medium), but systematic reviews flag "shallow and transactional engagement" and retention as the central unsolved problem ([Frontiers Digital Health, 2025](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1536416/full); High).
- **Symptom tracking is the weakest stand-alone bet: low accuracy AND low retention.** Symptom checkers give the correct diagnosis first only ~34% of the time and triage accuracy varies wildly ([Semigran, BMJ 2015](https://scholar.harvard.edu/mehrotra/publications/evaluation-symptom-checkers-self-diagnosis-and-triage-audit-study); High). Across mHealth, ~71% of users disengage within 90 days and unguided mental-health apps see ~3.3% 30-day retention ([JMIR 2022 review](https://www.jmir.org/2022/4/e35120/); High).
- **Cautionary tales are concentrated and instructive.** Babylon Health collapsed from a $4.2B SPAC valuation to bankruptcy in 2023 (unprofitable unit economics, disputed AI-safety claims) ([TechCrunch, 2023](https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/)); Woebot shut down its app in 2025, blocked by the lack of an FDA pathway for LLM-based therapy ([STAT, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/)). Both are High confidence.
- **For ditto specifically:** the defensible wedge is *grounded-and-cited* + *habit-forming logging tied to a real-world hook* (the appointment). Pure symptom tracking and undifferentiated chatbots are crowded, low-retention, and regulatorily exposed under the EU AI Act + MDR (medical-use AI is high-risk; compliance by Aug 2026/2027) ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/ai-medical-devices-regulation-2025); Medium). ⚠️

---

## 1. AI health assistants / general consumer health AI

**Market state.** Consumer adoption is rising fast and consolidating around general-purpose LLMs rather than purpose-built health apps. Rock Health's 2025 Consumer Adoption Survey found **32% of respondents used AI chatbots for health information, up from 16% in 2024**, and **64% of those use health AI weekly or more** ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/); Tier 1 analyst; High). Critically for positioning: **74% reached for general tools (ChatGPT 23%, Gemini 15%), vs. just 5% for provider-offered bots and 4% for payer bots** ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/); High). OpenAI states roughly **1 in 4 of its 800M+ weekly users submits a health prompt weekly** ([Fierce Healthcare, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says); Tier 2; Medium). On the clinician side, the AMA reported **66% of physicians used AI for at least one use case in 2024, up from 38% in 2023** ([Rock Health / AMA, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/); High).

| Player | Position | Traction signal |
|---|---|---|
| ChatGPT (OpenAI) | Default general assistant | ~1 in 4 of 800M+ weekly users ask health weekly ([Fierce, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says)) |
| Gemini (Google) | Default general assistant | 15% of AI-health users ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)) |
| Ada Health | Specialist symptom assessment | 11M users / 23M assessments since 2016 ([pharmaphorum](https://pharmaphorum.com/news/study-finds-big-differences-between-top-symptom-spotting-apps)) |
| Provider/payer bots | Embedded | Only 5%/4% of AI-health users ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)) |

**Trust / safety / regulatory posture.** Consumers prioritize AI for *quick answers, side-effect research, and appointment prep* — exactly ditto's adjacency — while trust remains a gating factor for diagnosis-grade queries ([Rock Health, 2026](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/); High). A 2025 empirical study found *source credibility and citation* materially raise patients' intention to adopt ChatGPT-generated health info ([PMC12394881, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394881/); Tier 1; High). ⚠️ EU note: under the EU AI Act, "AI systems intended for medical use" are **high-risk**, and any AI in a CE-marked device must meet both MDR and AI Act requirements (compliance Aug 2026; Aug 2027 for Notified-Body devices) ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/ai-medical-devices-regulation-2025); Medium). A general "information / appointment-prep companion" that avoids diagnosis/triage claims has a much lighter regulatory path than a symptom-checker positioned as a medical device.

**Cautionary tale.** **Babylon Health** built the highest-profile consumer AI-assistant + telehealth combo, went public via SPAC at a **$4.2B valuation (Oct 2021)**, and **filed for bankruptcy in Sept 2023** ([TechCrunch, 2023](https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/); Tier 2; High). Two lessons: its AI-diagnosis-equivalence claims were "widely disputed and the methods of evaluation discredited," and its unit economics were inverted (the founder noted patients used the service 6–7×/year against capitation paying for 2–3×) ([Wikipedia / TechCrunch, 2023](https://en.wikipedia.org/wiki/Babylon_Health); Medium). Vision and overclaiming on safety did not survive contact with economics and scrutiny.

---

## 2. Grounded / cited / truthful answer engines (OpenEvidence anchor)

**Why this matters for trust.** Health answers are only as good as their provenance. 2025 medical-RAG research has converged on *citation-traceability* and *principled refusal* as design primitives: **MedTrust-RAG** requires every reasoning statement to be explicitly traceable to a retrieved document with inline citations, and refuses (via "negative knowledge assertions") when evidence is insufficient rather than synthesizing ([arXiv 2510.14400, 2025](https://arxiv.org/pdf/2510.14400); Tier 1; High). **MEGA-RAG** uses multi-evidence aggregation and self-clarification to cut hallucination in public-health answering ([Frontiers Public Health, 2025](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1635381/full); High). But peer-reviewed work also cautions that RAG "can be dangerous medical communicators" when retrieval is shallow or context is misread ([arXiv 2502.14898, 2025](https://arxiv.org/pdf/2502.14898); High) — grounding is necessary but not sufficient; the *quality and licensing of the corpus* is the moat.

### OpenEvidence — verified traction (anchor case)

| Metric | Value | Source / confidence |
|---|---|---|
| Latest valuation | **$12B** (Series D, Jan 2026, $250M round, co-led Thrive Capital + DST Global) | [CNBC, 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html) / [Crunchbase News, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); High |
| Valuation trajectory | $3.5B (Series B, $210M, Jul 2025) → $6B (Series C, $200M, Oct 2025) → $12B (Jan 2026) | [PRNewswire, 2025](https://www.prnewswire.com/news-releases/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-210-million-round-at-3-5-billion-valuation-302505806.html); [Fierce, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/hlth25-3-months-after-series-b-round-openevidence-raises-lands-200m); High |
| Total raised | ~$700M | [Crunchbase News, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); High |
| Clinician adoption | **>40% of US physicians**; used across 10,000+ hospitals/facilities | [Crunchbase News, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); High |
| Usage volume | ~18M clinical consultations (Dec 2025); **~20M/month (Jan 2026)**; 1M in a single 24h day (10 Mar 2026 record) | [Crunchbase News, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); High |
| Revenue | ~$150M annualized (2025), reportedly +1,803% YoY from $7.9M (2024); ~90% gross margin; advertising-funded, free to verified physicians | [Crunchbase News / Sacra, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); Medium (revenue self/analyst-reported) |

**How it grounds answers.** OpenEvidence answers clinical questions with **cited responses sourced from licensed peer-reviewed literature** — NEJM, JAMA, NCCN, Cochrane and more ([OpenEvidence user guide](https://www.openevidence.com/user-guide/ask-overview); High). It signed **multi-year content agreements with NEJM Group (Feb 2025)** — all content from 1990 forward across NEJM, NEJM Evidence, NEJM AI, NEJM Catalyst, NEJM Journal Watch — and the **JAMA Network (Jun 2025)**, now drawing on 18+ peer-reviewed journals ([OpenEvidence × NEJM](https://www.openevidence.com/announcements/openevidence-and-nejm); [Fierce Healthcare, 2025](https://www.fiercehealthcare.com/ai-and-machine-learning/jama-signs-multi-year-deal-openevidence-inform-ai-powered-medical-search); High). The licensing of premium, paywalled evidence — not the LLM — is the differentiator.

**Expansion.** OpenEvidence is expanding its evidence base and consultation volume (single-day record Mar 2026) and is positioned as a clinician "brain extender"; it remains **clinician-facing, not consumer-facing** ([Crunchbase News, 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); High).

**Consumer-facing grounded-answer attempts.** No consumer entrant has reached OpenEvidence scale. General LLMs are adding citations, and academic prototypes (MedTrust-RAG, MEGA-RAG) and benchmarks with grounding annotations ([ACL Findings 2025](https://aclanthology.org/2025.findings-acl.875.pdf)) target the consumer/public-health register, but a *trusted, cited, patient-language* answer layer is largely **unoccupied** — relevant to ditto's "Living Health Companion." Implication: ditto can borrow OpenEvidence's *grounding architecture* (licensed evidence + inline citations + refusal) while serving patients/loved ones, a register OpenEvidence deliberately does not serve.

---

## 3. Digital / AI health coaches

**Market state.** Analysts size the digital health-coaching market at **~$28.4B by 2032**, driven by AI personalization and preventive-care demand ([SNS Insider via GlobeNewswire, 2025](https://www.globenewswire.com/news-release/2025/12/04/3199453/0/en/Digital-Health-Coaching-Market-Size-Worth-28-40-Billion-by-2032-Drive-by-AI-Driven-Personalization-and-Rising-Demand-for-Preventive-Care-SNS-Insider.html); Tier 1 analyst; Medium — vendor-issued sizing). Profiled players include Noom, Lark, Omada, Naluri, Lyra ([GlobeNewswire, 2025](https://www.globenewswire.com/news-release/2025/03/20/3046609/28124/en/Digital-Health-Coaching-Market-Report-2025-2030-with-Profiles-of-Atlantis-Health-Naluri-Therapeutics-Noom-Lark-Technologies-Omada-Health-Avidon-Health-Quartet-Health-Lyra-Health-mo.html); Medium).

| Player | Traction / funding | Outcome signal |
|---|---|---|
| **Lark Health** | $162M raised over 8 rounds; **35M+ patient interactions** (early 2025); payer partner | ~13% improvement in cardiac self-efficacy, est. $12.9M savings across ~12,000 participants (Heart Health pilot, 2023) — Tier 3 vendor self-report, FLAGGED ([Lark blog](https://www.lark.com/resources/lark-healths-artificial-intelligence-ai-heart-health-program-significantly-improves-cardiac-self-efficacy)) |
| **Omada Health** | Public/scaled; launched OmadaSpark AI nutrition agent (May 2025) | Long-standing DPP/chronic-care outcomes literature; AI agent for food logging + behavioral support ([MobiHealthNews](https://www.mobihealthnews.com/news/lark-scores-100m-digital-chronic-care-management)) |
| **KidneyOnline** (China) | Research deployment | AI nurse-led system **slowed non-dialysis CKD progression** vs. conventional care, retrospective cohort ([JMIR 2024, PMC11629034](https://www.jmir.org/2024/1/e54206); Tier 1; High) |

**Evidence on efficacy & retention.** A 2025 systematic review of human/AI/hybrid coaching found AI coaching reports *positive psychological-wellbeing improvements* (including reduced depressive symptoms), **but flagged "shallow and transactional engagement and retention challenges" as the central weakness** — and argued hybrid (human + AI) models best sustain engagement ([Frontiers Digital Health, 2025](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1536416/full); Tier 1; High). The CKD study is among the stronger efficacy signals, but is retrospective and China-based (⚠️ transfer caution) ([JMIR 2024](https://www.jmir.org/2024/1/e54206); High).

**Success factors.** (1) A clinical wedge with measurable outcomes (CKD, cardiometabolic). (2) Payer/employer reimbursement rather than consumer subscription. (3) Human-in-the-loop to sustain engagement. **Cautionary signal:** vendor-reported outcome numbers (Lark) are Tier 3 and self-selected; independent RCT-grade evidence for *AI-only* coaching at scale remains thin.

---

## 4. Symptom tracking (low-retention / high-churn focus)

**Market state.** Symptom checkers and trackers are abundant but face a **double problem: low accuracy AND low retention.**

**Accuracy (cautionary core).** The landmark Semigran audit (BMJ 2015) found **23 symptom checkers gave the correct diagnosis first only 34% of the time** (correct in top-20 for 58%), with **triage accuracy ranging 33%–78%** ([Semigran, BMJ 2015](https://scholar.harvard.edu/mehrotra/publications/evaluation-symptom-checkers-self-diagnosis-and-triage-audit-study); Tier 1; High). A later systematic review confirmed **primary-diagnosis accuracy 19–37.9%**, triage 48.8–90.1% ([PMC9385087, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385087/); Tier 1; High). Head-to-head, **Ada** scored well (99% condition coverage, 97% safety) while **Babylon's** condition coverage was 51.5% and suggestion accuracy ~32% ([pharmaphorum](https://pharmaphorum.com/news/study-finds-big-differences-between-top-symptom-spotting-apps); Tier 2; Medium).

**Retention (the critical evidence).**

| Metric | Value | Source / confidence |
|---|---|---|
| mHealth disengagement | **~71% of users disengage within 90 days** | [JMIR 2022 literature review (PMC9092233)](https://www.jmir.org/2022/4/e35120/); Tier 1; High |
| Abandonment curve | **Median ~70% discontinue within first 100 days** (sharp early drop) | [JMIR 2024 scoping review (e56897)](https://www.jmir.org/2024/1/e56897); Tier 1; High |
| Unguided mental-health apps | **Median 30-day retention ~3.3%** | [mHealth app-store usage analysis, cited 2024](https://www.jmir.org/2024/1/e59444/); Tier 1; Medium |
| Health & fitness apps | ~3% retention by day 30 (2023) | [Business of Apps benchmarks, 2026](https://www.businessofapps.com/data/health-fitness-app-benchmarks/); Tier 2; Medium |
| Survival analysis | Median user-retention ~51 days (mental-health app); usage peaks at adoption then decays | [JMIR 2020 survival analysis (e16309)](https://mhealth.jmir.org/2020/11/e16309/); Tier 1; High |

**Why symptom trackers stall.** Usage peaks at adoption then declines ("users utilize the app most at the time of adoption and gradually reduce usage"); the modal user is an *abandoner* with a median ~1 day of use ([JMIR 2024 engagement study, PMC11420572](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11420572/); High). Manual symptom logging carries high friction with low perceived payoff between acute episodes, so it lacks a recurring hook. By contrast, **passive / wearable-linked tracking (Strava, Fitbit) retains better because data collection is automatic**, lowering friction ([JMIR 2020 survival analysis](https://mhealth.jmir.org/2020/11/e16309/); High). **Exception:** time-boxed, purpose-bound logging can hit high adherence — an 89% adherence over a 28-day symptom-mapping window — when there is a clear endpoint and reason ([symptom-checker ED usability work; benchmark search, 2026](https://www.businessofapps.com/data/health-fitness-app-benchmarks/); Medium). **Implication for ditto:** stand-alone symptom tracking is a poor retention bet unless (a) passively populated, (b) tied to a recurring real-world event (the appointment), or (c) time-boxed to an episode.

---

## 5. Health journaling & logging

**Market state & engagement patterns.** Health journaling/logging shares the same churn dynamics as symptom tracking but has a more favorable design lever: *self-monitoring can itself drive engagement when fed back meaningfully.* Retention is inconsistently measured across the literature, which obscures comparisons ([JMIR 2022 review](https://www.jmir.org/2022/4/e35120/); High). Key data points:

- **~71% disengage within 90 days; ~70% within 100 days (sharp early drop-off)** — the same curvilinear abandonment seen in symptom apps ([JMIR 2022 review](https://www.jmir.org/2022/4/e35120/); [JMIR 2024 scoping review](https://www.jmir.org/2024/1/e56897); High).
- Abandonment varies by domain: **alcohol/smoking logging churns fastest; physical-activity and mental-health logging persist longer** ([JMIR 2024 scoping review](https://www.jmir.org/2024/1/e56897); High).
- **Self-monitoring with feedback lengthens engagement** — a study on self-monitoring's effect on long-term engagement found logging that is reflected back to the user sustains use better than passive capture alone ([PMC6062090](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6062090/); Tier 1; Medium).

**What makes logging stick (success factors).** (1) **Low friction** — minimize taps, prefer passive/auto-populated entries (the wearable lesson from §4). (2) **Immediate, personalized feedback loop** — logs must visibly produce insight or action, not just accumulate. (3) **A recurring external hook** — calendar events, medication times, or appointments anchor the habit. (4) **Hybrid human/AI touch** sustains engagement vs. transactional bots ([Frontiers Digital Health, 2025](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1536416/full); High).

**What makes it fail (cautionary).** Open-ended manual journaling with no feedback and no external trigger replicates the symptom-tracker decay curve — peak at install, abandonment within weeks. Mental-health-chatbot longitudinal data is sobering: a Stanford-led study of 4,500+ paying Youper users found meaningful early anxiety/depression reductions that **plateaued over time**, underscoring that even engaged, paying cohorts decay without renewed value ([summarized via STAT/secondary, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/); Tier 2; Medium).

**Cross-cutting cautionary tale (coaching + chatbot + logging).** **Woebot Health** — a CBT chatbot used by **1.5M+ people** — shut down its app **30 June 2025**, with the CEO citing the **cost of FDA marketing authorization and the absence of a regulatory pathway for LLM-based tools** (it held a 2021 Breakthrough Device Designation but never got authorization) ([STAT, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/); [Behavioral Health Business, 2025](https://bhbusiness.com/2025/04/23/woe-is-me-woebot-says-farewell-to-signature-app/); High). Contrast: **Wysa** persists with 30+ peer-reviewed studies, FDA Breakthrough designation, and an enterprise clinician-in-the-loop "Copilot" model ([buildmvpfast summary, 2026](https://www.buildmvpfast.com/blog/mental-health-ai-chatbots-woebot-wysa-therapeutic-effectiveness-2026); Tier 3, FLAGGED; Medium). Lesson for ditto: **positioning as a medical device invites a regulatory burden that can kill the product; an information/companion/logging layer that stays clear of diagnosis/therapy claims is more survivable** — especially under the EU AI Act + MDR high-risk regime ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/ai-medical-devices-regulation-2025); Medium). ⚠️

---

## Implications for ditto.care (synthesis)

1. **Compete on grounding, not on being-a-chatbot.** The default is ChatGPT; the durable trust advantage is OpenEvidence-style *licensed, cited, refuse-when-unsure* answers — but in **patient language**, a register OpenEvidence does not serve.
2. **Anchor logging to the appointment.** ditto's existing appointment-summary hook is exactly the recurring external trigger that symptom/journal apps lack; passive population + feedback is the retention play, not manual symptom diaries.
3. **Avoid the medical-device trap.** Diagnosis/triage/therapy claims trigger EU AI Act + MDR high-risk obligations (Aug 2026/2027) and have killed better-funded players (Babylon, Woebot). Position as information/companion/preparation. ⚠️
4. **Expect decay; design against it.** Plan for the ~70% / 90–100-day abandonment curve with hybrid human touch and visible value loops; do not assume logging sticks on its own.

---

## Sources

### Tier 1 — peer-reviewed / official / analyst
- Rock Health, 2025 Consumer Adoption Survey, 2026 — https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/
- Semigran et al., "Evaluation of symptom checkers for self diagnosis and triage: audit study," BMJ 2015 — https://scholar.harvard.edu/mehrotra/publications/evaluation-symptom-checkers-self-diagnosis-and-triage-audit-study
- "Diagnostic and triage accuracy of digital symptom checker tools: systematic review," PMC9385087, 2022 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9385087/
- "Challenges in Participant Engagement and Retention Using Mobile Health Apps: Literature Review," JMIR 2022 — https://www.jmir.org/2022/4/e35120/
- "When and Why Adults Abandon Lifestyle and Mental Health Apps: Scoping Review," JMIR 2024 — https://www.jmir.org/2024/1/e56897
- "Assessing User Retention of a Mobile App: Survival Analysis," JMIR 2020 — https://mhealth.jmir.org/2020/11/e16309/
- "Predicting Long-Term Engagement in mHealth Apps," JMIR 2024 — https://www.jmir.org/2024/1/e59444/
- "Effect of self-monitoring on long-term patient engagement with mobile health applications," PMC6062090 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6062090/
- "Long-Term Efficacy of an AI-Based Health Coaching Mobile App in Slowing CKD Progression," JMIR 2024 — https://www.jmir.org/2024/1/e54206
- Systematic review of human/AI/hybrid health coaching, Frontiers Digital Health 2025 — https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1536416/full
- MedTrust-RAG, arXiv 2510.14400, 2025 — https://arxiv.org/pdf/2510.14400
- MEGA-RAG, Frontiers Public Health 2025 — https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1635381/full
- "Retrieval-augmented systems can be dangerous medical communicators," arXiv 2502.14898, 2025 — https://arxiv.org/pdf/2502.14898
- "Promoting trust and intention to adopt health information generated by ChatGPT," PMC12394881, 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12394881/
- Benchmark with grounding annotations for RAG, ACL Findings 2025 — https://aclanthology.org/2025.findings-acl.875.pdf
- OpenEvidence × NEJM content agreement (official), 2025 — https://www.openevidence.com/announcements/openevidence-and-nejm
- OpenEvidence Ask Overview (official user guide) — https://www.openevidence.com/user-guide/ask-overview

### Tier 2 — press
- CNBC, "OpenEvidence doubles valuation to $12 billion," 2026 — https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html
- Crunchbase News, "OpenEvidence doubles valuation to $12B with $250M Series D," 2026 — https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/
- PRNewswire, "OpenEvidence $210M round at $3.5B valuation," 2025 — https://www.prnewswire.com/news-releases/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-210-million-round-at-3-5-billion-valuation-302505806.html
- Fierce Healthcare, "HLTH25: OpenEvidence raises $200M at $6B," 2025 — https://www.fiercehealthcare.com/ai-and-machine-learning/hlth25-3-months-after-series-b-round-openevidence-raises-lands-200m
- Fierce Healthcare, "JAMA signs multi-year deal with OpenEvidence," 2025 — https://www.fiercehealthcare.com/ai-and-machine-learning/jama-signs-multi-year-deal-openevidence-inform-ai-powered-medical-search
- Fierce Healthcare, "40M people use ChatGPT for healthcare questions," 2025 — https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says
- TechCrunch, "The fall of Babylon," 2023 — https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/
- Wikipedia, "Babylon Health" — https://en.wikipedia.org/wiki/Babylon_Health
- STAT, "Woebot Health shuts down therapy chatbot," 2025 — https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/
- Behavioral Health Business, "Woebot says farewell to signature app," 2025 — https://bhbusiness.com/2025/04/23/woe-is-me-woebot-says-farewell-to-signature-app/
- MobiHealthNews, "Lark scores $100M for digital chronic care management" — https://www.mobihealthnews.com/news/lark-scores-100m-digital-chronic-care-management
- pharmaphorum, "Study finds big differences between top symptom checker apps" — https://pharmaphorum.com/news/study-finds-big-differences-between-top-symptom-spotting-apps
- Business of Apps, "Health & Fitness App Benchmarks 2026" — https://www.businessofapps.com/data/health-fitness-app-benchmarks/
- GlobeNewswire (SNS Insider), "Digital Health Coaching Market $28.40B by 2032," 2025 — https://www.globenewswire.com/news-release/2025/12/04/3199453/0/en/Digital-Health-Coaching-Market-Size-Worth-28-40-Billion-by-2032-Drive-by-AI-Driven-Personalization-and-Rising-Demand-for-Preventive-Care-SNS-Insider.html
- GlobeNewswire, "Digital Health Coaching Market Report 2025-2030," 2025 — https://www.globenewswire.com/news-release/2025/03/20/3046609/28124/en/Digital-Health-Coaching-Market-Report-2025-2030-with-Profiles-of-Atlantis-Health-Naluri-Therapeutics-Noom-Lark-Technologies-Omada-Health-Avidon-Health-Quartet-Health-Lyra-Health-mo.html
- IntuitionLabs, "AI Medical Devices: 2025 Status, Regulation & Challenges," 2025 — https://intuitionlabs.ai/articles/ai-medical-devices-regulation-2025

### Tier 3 — blog / vendor self-report (FLAGGED — treat with caution)
- Lark Health blog, "AI Heart Health Program Improves Cardiac Self-Efficacy" (vendor self-report) — https://www.lark.com/resources/lark-healths-artificial-intelligence-ai-heart-health-program-significantly-improves-cardiac-self-efficacy
- buildmvpfast, "Mental Health AI Chatbots: Woebot & Wysa effectiveness," 2026 (blog) — https://www.buildmvpfast.com/blog/mental-health-ai-chatbots-woebot-wysa-therapeutic-effectiveness-2026

*Note: WebFetch was unavailable in this environment (all hosts returned HTTP 403); figures were extracted from WebSearch result summaries of the cited primary/press pages and cross-checked across multiple independent sources where possible. OpenEvidence funding/valuation/usage figures are corroborated across CNBC, Crunchbase News, PRNewswire and Fierce Healthcare. Revenue figures are analyst/self-reported and tagged Medium confidence.*
