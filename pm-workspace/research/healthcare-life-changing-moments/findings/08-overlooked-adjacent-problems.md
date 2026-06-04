# 08 — Overlooked & Adjacent Problems

**Project:** Life-Changing Healthcare Moments — Mapping the Overlooked Problems & ditto's Category-Defining Opportunity
**File owner:** Contrarian problem-hunter (Phase 1, stream H)
**Date / access date for all URLs:** 2026-05-31
**Geography:** Pan-EU, anchored NL + DACH. US-derived statistics are flagged **(US data — EU applicability uncertain)**.
**Source tiers:** Tier 1 (peer-reviewed / EU bodies) · Tier 2 (patient orgs / guidelines) · Tier 3 (forums / news — texture only, flagged).

---

## Key takeaways

1. **The recall failure is real, large, and proven.** Patients forget **40–80% of medical information immediately**, and **roughly half of what they do retain is wrong** ([Kessels, *J R Soc Med*, 2003](https://journals.sagepub.com/doi/10.1177/014107680309600504)). This is the status-quo failure ditto's appointment summary already attacks — and it is the *headwater* of nearly every other problem below. Confidence: **High**.

2. **There is a whole cluster of problems with the same shape** — each is normalized ("that's just how healthcare is"), dismissed as trivial or unsolvable, yet touches tens of millions of Europeans and is severe at the individual level. The strongest candidates: **proxy/loved-one access**, **care fragmentation / no single overview**, **discharge-cliff comprehension**, **appointment under-preparation**, and **administrative/financial toxicity**.

3. **Low health literacy is the silent multiplier.** ~**46–48% of EU adults have limited health literacy** ([HLS19, M-POHL, 2021](https://m-pohl.net/sites/m-pohl.net/files/inline-files/HLS19%20International%20Report.pdf)). Every comprehension-dependent problem is worse than the headline number for nearly half the population. Confidence: **High**.

4. **Caregivers are the invisible workforce holding the thread** — ~**80% of all long-term care in the EU is delivered by informal carers** ([Eurocarers](https://eurocarers.org/about-carers/)) — yet they are untrained, unsupported, and frequently *legally locked out* of the patient's information. The "I had to be my parent's secretary" problem is structural, not anecdotal. Confidence: **High** (prevalence) / **Medium** (legal-access framing).

5. **The most software-tractable, least-served problems** are the *information-flow* ones: recall, single-overview/coordination, proxy access, and appointment prep. The hardest (financial toxicity, adherence biology) are real but partly non-software. The ranking table at the end scores all of them.

---

## Problem 1 — Information recall & comprehension failure after consultations

**Hard statistic.** Patients forget **40–80% of medical information immediately** after a consultation, and **almost half of the information that is retained is recalled incorrectly** ([Kessels, "Patients' memory for medical information," *Journal of the Royal Society of Medicine* 96(5):219–222, 2003](https://journals.sagepub.com/doi/10.1177/014107680309600504)) — Tier 1. Successor work confirms it: recall is *worse* with spoken-only information (as low as ~14% correctly recalled), and strongly graded by education — patients with less than high school recalled ~38% of recommendations vs ~65% for college graduates ([Laws et al., factors in ambulatory specialty care recall, *PMC*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5794108/); summarized by [AARP, 2018](https://www.aarp.org/health/healthy-living/doctor-patient-study-2018/)) — Tier 1 / Tier 3. Written summaries improve recall by ~**20%** ([Dya Clinical synthesis of consultation-summary evidence](https://www.dyaclinical.com/blog/patient-recall-consultation-summary)) — Tier 3 (vendor, directional).
**Anxiety makes it worse exactly when it matters most** — at diagnosis. In newly diagnosed cancer patients at a fast-track clinic, anxiety measurably degraded recall ("fear and forget") ([van der Velden et al., *Acta Oncologica*, 2018](https://www.tandfonline.com/doi/full/10.1080/0284186X.2018.1512156)) — Tier 1. A question-prompt sheet addressed by the oncologist reduced anxiety, shortened the consultation, *and* improved recall (ibid.).

**Why overlooked.** Normalized as the patient's job ("you should have written it down") and invisible to clinicians, who never see what was lost. The fix (a summary) looks trivial.

**Reach.** Near-universal — essentially every patient in every consultation. In the EU, hundreds of millions of encounters per year.

**Severity.** High at life-changing moments: forgotten/garbled treatment plans drive non-adherence, wrong self-care, missed red-flag instructions, and repeat appointments. The teach-back literature shows correcting comprehension improves adherence and self-management and reduces readmissions in chronic disease ([Dinh et al., teach-back systematic review, *JBI Evidence Synthesis*, 2016](https://pubmed.ncbi.nlm.nih.gov/26878928/)) — Tier 1.

**Confidence: High.**

---

## Problem 2 — Proxy / loved-one access (the "I became my parent's secretary" problem)

**Hard statistic.** **~80% of all long-term care in the EU is provided by informal carers**, who number on the order of **~100 million people (~20% of the population)** by broad estimates, or **~44 million (~12% of adults)** providing care *regularly* by Eurofound's stricter count; the unpaid economic value is **~2.5% of EU GDP** and **50–90% of the cost of formal long-term care** ([Eurocarers, "About carers"](https://eurocarers.org/about-carers/)) — Tier 2. Yet proxy access to the patient's records and portals is gated by "difficult and time-consuming processes" and privacy/consent friction ([family-caregiver portal-access literature, *PMC*](https://pmc.ncbi.nlm.nih.gov/articles/PMC9022132/)) — Tier 1.

**Why overlooked.** The system models care as a 1:1 patient–clinician relationship; the family member who actually coordinates, remembers, and executes has no formal seat, no login, and often no legal standing until a crisis. The labour is invisible and unpaid, so it never shows up in any system metric.

**Reach.** Tens of millions of EU caregivers; effectively every serious-illness patient who relies on a spouse/child to manage logistics.

**Severity.** High — the caregiver is the de facto care-coordinator and memory backup, but operates blind: can't see the records, can't see the plan, re-asks the same questions, and burns out. Informal-care burden in Europe is projected to rise **~+50% by 2050** ([burden-of-informal-care microsimulation, *PMC*, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12008708/)) — Tier 1.

**Confidence: High** on prevalence/economics; **Medium** on the legal-lockout framing (varies by member state and by EHDS rollout).

---

## Problem 3 — Care fragmentation / no single overview across specialists

**Hard statistic.** ~**50 million people in Europe live with multimorbidity** (multiple chronic conditions), and **~37–42% of Europeans aged 50+ have two or more chronic conditions**, rising over time ([Palladino et al., *Health Affairs*, 2019, 38.2%→41.5% across 10 countries](https://www.healthaffairs.org/doi/10.1377/hlthaff.2018.05273); [17-country multimorbidity study, *PLOS One*, 2021](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0246623)) — Tier 1. EU health systems are "disease-oriented," organized around single specialties, producing **contradictory medical advice, over-prescribing, over-hospitalization, and poor satisfaction** — with *no single provider* able to see the whole patient ([WHO/European Observatory, "How to improve care for people with multimorbidity in Europe?"](https://www.ncbi.nlm.nih.gov/books/NBK464548/)) — Tier 1. Fragmented care is associated with cost increases of **>€4,000 per patient** (ibid., directional).

**Why overlooked.** Each specialist is doing their job well within their silo; the gap is *between* them and belongs to no one. Patients and families are silently assigned the integrator role.

**Reach.** ~50M+ multimorbid Europeans; the entire serious-illness population sees multiple specialists.

**Severity.** High — duplicate tests, conflicting advice, dropped balls, and the cognitive load of being your own medical-records integrator at your sickest.

**Confidence: High.**

---

## Problem 4 — Transitions of care: the "discharge cliff"

**Hard statistic.** **78% of patients discharged from the emergency department had deficient understanding of at least one of: diagnosis/cause, ED care, post-ED care, or return instructions**; among elderly patients **21% did not understand their diagnosis and 56% failed to comprehend return instructions** ([Engel et al., ED discharge comprehension, *PMC*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3844327/)) — Tier 1 **(US data — EU applicability uncertain)**. Insufficient transfer of medicines information at hospital-to-primary-care handover is a documented, common safety gap in Europe too ([medicines-information-at-discharge qualitative study, Norway, *PMC*, 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7878245/)) — Tier 1. A follow-up visit within the first week post-discharge is associated with **~42% lower readmission odds** ([readmissions/discharge primer, AHRQ PSNet](https://psnet.ahrq.gov/primer/readmissions-and-adverse-events-after-discharge)) — Tier 1/2 **(US-anchored)**.

**Why overlooked.** Discharge is treated as the end of the episode, not a handoff; the comprehension failure surfaces only as a readmission weeks later, decoupled from its cause.

**Reach.** Every hospital discharge — many millions of EU admissions/year, concentrated in exactly the serious-illness and elderly populations.

**Severity.** High — avoidable readmissions, medication errors, and patients sent home not knowing what worsening looks like.

**Confidence: Medium** (best-quantified studies are US/single-country; EU magnitude likely similar but not directly measured at this granularity).

---

## Problem 5 — Appointment under-preparation & "white-coat silence"

**Hard statistic.** Patients systematically fail to ask the questions that matter — held back by anxiety, intimidation, jargon, fear of seeming "difficult," and time pressure ("white-coat silence") ([Judson et al., "Encouraging Patients to Ask Questions," *JAMA*, 2013](https://jamanetwork.com/journals/jama/article-abstract/1696107)) — Tier 1. Conversely, **question-prompt lists** are an evidence-based fix: addressed by the clinician, they reduce anxiety, shorten consultations, and improve recall in cancer care ([van der Velden et al., *Acta Oncologica*, 2018](https://www.tandfonline.com/doi/full/10.1080/0284186X.2018.1512156); [Brown et al., promoting participation RCT, *PMC*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2375236/)) — Tier 1.

**Why overlooked.** The burden of knowing what to ask is silently placed on the least-expert, most-stressed person in the room; the unasked question is invisible.

**Reach.** Universal across consultations; acute at first specialist/diagnosis visits.

**Severity.** Medium–High — questions remembered only in the car park; misaligned expectations; decisions made without the patient's real concerns surfaced. Strongly couples to Problems 1 and 6.

**Confidence: High** (mechanism and intervention) / **Medium** (EU-specific magnitude).

---

## Problem 6 — Shared decision-making gaps & decision regret

**Hard statistic.** **~1 in 5 cancer-treatment patients experience significant decision regret** — a pooled **20% (95% CI 16–23) across 14 studies and 17,883 localized-prostate-cancer patients** ([Christie et al., decision-regret systematic review & meta-analysis, *European Urology Oncology* / via UroToday](https://www.urotoday.com/recent-abstracts/urologic-oncology/prostate-cancer/142876-decision-regret-in-patients-with-localised-prostate-cancer-a-systematic-review-and-meta-analysis.html)) — Tier 1. A broader surgical review found mean regret prevalence **~14.4%** ([Wilson et al., "Regret in Surgical Decision Making," *World Journal of Surgery*, 2017](https://pubmed.ncbi.nlm.nih.gov/28243695/)) — Tier 1. **Decreased involvement in the decision predicts higher regret** (ibid.) — i.e., the comprehension/involvement gap is causal, not just correlated.

**Why overlooked.** Regret is felt privately, months later; consent is treated as a one-time signature, not a comprehension check. "The patient agreed" masks "the patient didn't understand the options/risks."

**Reach.** Every patient facing a serious treatment choice (surgery vs surveillance, chemo regimens, etc.).

**Severity.** High and durable — long-term regret, worse psychological outcomes, eroded trust.

**Confidence: High** (regret prevalence) / **Medium** on how directly software changes the *decision* (vs. supporting comprehension around it).

---

## Problem 7 — Health / medical literacy as a population-wide multiplier

**Hard statistic.** **~46–48% of adults across the 17 HLS19 countries have limited (problematic or inadequate) general health literacy**, ranging **29–62% between countries** ([HLS19 International Report, M-POHL, 2021](https://m-pohl.net/sites/m-pohl.net/files/inline-files/HLS19%20International%20Report.pdf)) — Tier 1. DACH levels are in the higher-burden band (Germany and Austria ~42–44% limited; Switzerland ~38%) per HLS19 country results. **The Netherlands was *not* in HLS19**; in the earlier HLS-EU survey (2009–12) the NL had among the *lowest* limited-HL rates in Europe (~28–29%) ([HLS-EU, Sørensen et al., *Eur J Public Health*, 2015](https://academic.oup.com/eurpub/article/25/6/1053/2467145)) — Tier 1. *(Note: HLS-EU and HLS19 use different instruments — not directly comparable.)*

**Why overlooked.** It is framed as an "education problem" outside healthcare's remit, and clinicians systematically over-estimate patient understanding.

**Reach.** Nearly half the EU adult population — and over-concentrated in exactly the older, chronically ill, migrant populations facing serious illness.

**Severity.** High as a *multiplier*: it amplifies Problems 1, 4, 5, 6, and 8. Limited HL predicts worse adherence, more ED use, worse outcomes.

**Confidence: High** (prevalence) — with the explicit caveat that NL is from a different (older) survey instrument.

---

## Problem 8 — Administrative & financial toxicity of serious illness

**Hard statistic.** Even under universal healthcare, European cancer patients face heavy non-clinical burden: **56% reported income loss, 86% reported additional treatment-related expenses, and 16% delayed or avoided care (visits, medication, surgery)** in a **2,507-patient pan-European study** ([Witte et al. / financial-toxicity-in-Europe study, *ESMO Open*, 2025](https://www.esmoopen.com/article/S2059-7029(25)01162-7/fulltext)) — Tier 1. German cancer-patient data corroborate substantial patient-level financial burden ([patient-level cost of cancer care, *BMC Cancer*, 2020](https://bmccancer.biomedcentral.com/articles/10.1186/s12885-020-07028-4)) — Tier 1.

**Why overlooked.** Assumed "solved" by universal coverage in the EU, so the residual paperwork/logistics/income load is dismissed; it is also fragmented across employers, insurers, and benefits agencies, belonging to no single actor.

**Reach.** Most serious-illness patients and their households.

**Severity.** High — financial toxicity independently worsens quality of life, mental health, and even adherence (delay/avoid). But: substantially *non-software* (entitlements, money), so partly out of ditto's tractable zone.

**Confidence: Medium–High** (cancer data strong; generalization to other journeys is directional).

---

## Problem 9 — Medication management & adherence complexity

**Hard statistic.** **~50% of patients with chronic disease in developed countries do not adhere to long-term therapy** ([WHO, "Adherence to Long-Term Therapies," 2003](https://www.who.int/news/item/01-07-2003-failure-to-take-prescribed-medicine-for-chronic-diseases-is-a-massive-world-wide-problem)) — Tier 1. Major drivers are *information/comprehension* ones: regimen complexity, poor health literacy, not understanding the benefit, and undiscussed side effects (ibid.) — i.e., the comprehension failure (Problem 1) shows up downstream as non-adherence.

**Why overlooked.** Framed as patient "non-compliance" (a moral failing) rather than a comprehension/coordination/system failure.

**Reach.** Every patient on long-term medication — the core of the serious-illness population.

**Severity.** High clinical and cost impact; partly software-tractable (the comprehension/reminder/overview slice) and partly biological/behavioral (out of scope).

**Confidence: High** (the 50% figure is the canonical WHO benchmark, widely replicated).

---

## Ranked overlooked-problem table

Scoring 1–5 each (5 = highest). **Reach** = how many touched · **Severity** = harm per person · **Overlooked** = how normalized/un-served · **Software-tractable** = how well a focused patient-facing product can move it. **Priority = Reach × Severity × Overlooked × Software-tractable** (max 625).

| # | Overlooked problem | Reach | Severity | Overlooked | SW-tractable | **Priority** | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | **Recall & comprehension after consultations** | 5 | 4 | 5 | 5 | **500** | High |
| 3 | **Care fragmentation / no single overview** | 4 | 5 | 5 | 4 | **400** | High |
| 2 | **Proxy / loved-one access** | 4 | 4 | 5 | 4 | **320** | High / Med |
| 5 | **Appointment under-preparation (white-coat silence)** | 5 | 3 | 5 | 4 | **300** | High / Med |
| 7 | **Health-literacy multiplier** | 5 | 4 | 4 | 3 | **240** | High |
| 4 | **Discharge cliff / transitions of care** | 4 | 5 | 4 | 3 | **240** | Medium |
| 6 | **Shared decision-making / decision regret** | 3 | 5 | 4 | 3 | **180** | High / Med |
| 9 | **Medication management & adherence** | 5 | 5 | 2 | 3 | **150** | High |
| 8 | **Administrative & financial toxicity** | 4 | 4 | 4 | 2 | **128** | Med–High |

**Reading the ranking.** The top tier (recall, fragmentation/overview, proxy access, appointment prep) is exactly where information-flow software has leverage and where the problem is most normalized — the same "looks trivial, is not" shape as ditto's summary. Adherence and financial toxicity score high on reach/severity but lower on *overlooked* (adherence is heavily worked-on) or *software-tractability* (finance is mostly non-software), so they are weaker category bets despite being important. Health literacy is best treated as a **design constraint that multiplies all the others**, not a standalone product.

---

## Sources

All URLs accessed **2026-05-31**.

**Tier 1 — peer-reviewed / EU bodies / WHO**
- Kessels RPC. "Patients' memory for medical information." *J R Soc Med* 96(5):219–222, 2003. https://journals.sagepub.com/doi/10.1177/014107680309600504 (also PubMed https://pubmed.ncbi.nlm.nih.gov/12724430/ ; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC544650/ — 403 on fetch, citation via abstract)
- Factors associated with patient recall in ambulatory specialty care. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC5794108/
- van der Velden NCA et al. "Fear and forget: anxiety and recall in newly diagnosed cancer patients." *Acta Oncologica*, 2018. https://www.tandfonline.com/doi/full/10.1080/0284186X.2018.1512156
- Brown R et al. "Promoting patient participation and shortening cancer consultations: a randomised trial." *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2375236/
- Dinh TTH et al. "Effectiveness of the teach-back method on adherence and self-management in chronic disease: a systematic review." *JBI Evidence Synthesis*, 2016. https://pubmed.ncbi.nlm.nih.gov/26878928/
- HLS19 International Report, M-POHL / WHO, 2021. https://m-pohl.net/sites/m-pohl.net/files/inline-files/HLS19%20International%20Report.pdf ; overview https://m-pohl.net/HLS19
- Sørensen K et al. "Health literacy in Europe: comparative results of the HLS-EU survey." *Eur J Public Health* 25(6):1053–8, 2015. https://academic.oup.com/eurpub/article/25/6/1053/2467145
- WHO/European Observatory. "How to improve care for people with multimorbidity in Europe?" https://www.ncbi.nlm.nih.gov/books/NBK464548/
- Palladino R et al. "Multimorbidity and health outcomes in older adults in ten European health systems, 2006–15." *Health Affairs*, 2019. https://www.healthaffairs.org/doi/10.1377/hlthaff.2018.05273
- "Multimorbidity and its associated factors among adults 50+ in 17 European countries." *PLOS One*, 2021. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0246623
- Engel KG et al. ED discharge comprehension. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3844327/ **(US data)**
- Medicines information at hospital discharge (Norway qualitative study). *PMC*, 2021. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7878245/
- AHRQ PSNet. "Readmissions and Adverse Events After Discharge." https://psnet.ahrq.gov/primer/readmissions-and-adverse-events-after-discharge **(US-anchored)**
- Judson TJ et al. "Encouraging Patients to Ask Questions: How to Overcome White-Coat Silence." *JAMA*, 2013. https://jamanetwork.com/journals/jama/article-abstract/1696107
- Decision Regret in Localised Prostate Cancer: Systematic Review & Meta-analysis (pooled 20%). *Eur Urol Oncol* via UroToday. https://www.urotoday.com/recent-abstracts/urologic-oncology/prostate-cancer/142876-decision-regret-in-patients-with-localised-prostate-cancer-a-systematic-review-and-meta-analysis.html
- Wilson A et al. "Regret in Surgical Decision Making." *World Journal of Surgery*, 2017. https://pubmed.ncbi.nlm.nih.gov/28243695/
- Witte J et al. "Financial toxicity and socioeconomic impact of cancer in Europe." *ESMO Open*, 2025. https://www.esmoopen.com/article/S2059-7029(25)01162-7/fulltext
- Patient-level cost of cancer care (German cancer patients). *BMC Cancer*, 2020. https://bmccancer.biomedcentral.com/articles/10.1186/s12885-020-07028-4
- WHO. "Adherence to Long-Term Therapies: Evidence for Action," 2003. https://www.who.int/news/item/01-07-2003-failure-to-take-prescribed-medicine-for-chronic-diseases-is-a-massive-world-wide-problem
- Burden of informal family caregiving in Europe 2000–2050 (microsimulation). *PMC*, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12008708/
- Characteristics of patients & proxy caregivers using patient portals in serious illness. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC9022132/

**Tier 2 — patient orgs / guidelines / EU networks**
- Eurocarers. "About carers." https://eurocarers.org/about-carers/

**Tier 3 — texture / vendor / news (flagged)**
- Dya Clinical. "Patients Forget 40-80% of What You Tell Them." https://www.dyaclinical.com/blog/patient-recall-consultation-summary
- AARP. "Patients Can't Recall Half of What the Doctor Said," 2018. https://www.aarp.org/health/healthy-living/doctor-patient-study-2018/
- TechTarget. "Patient Recall Suffers as Patients Remember Half of Health Info." https://www.techtarget.com/patientengagement/news/366585219/Patient-Recall-Suffers-as-Patients-Remember-Half-of-Health-Info
