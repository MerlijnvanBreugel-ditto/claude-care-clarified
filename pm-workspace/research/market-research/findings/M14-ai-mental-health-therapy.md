# M14 — AI for Mental Health & Therapy

**Market-research chapter for ditto.care** · EU/Netherlands patient-facing health-tech
**Access date:** 2026-06-10 · **Data window preference:** 2024–2026
**Source tiers:** **T1** = peer-reviewed / official (journals, regulators, gov) · **T2** = reputable press / company filings · **T3** = blog / vendor marketing / aggregator (FLAGGED inline)
**Geography flags:** 🇺🇸→🇪🇺 = US-origin data point, EU applicability uncertain · 🇪🇺 = directly EU-relevant
**Confidence:** High / Medium / Low. Funding & efficacy figures left **[unconfirmed]** where not corroborated by ≥1 primary/press source.

---

## Key takeaways

- **The dominant "AI therapist" today is not a therapy app — it's general-purpose ChatGPT.** Sentio (Feb 2025, n=499 US adults with mental-health conditions who use LLMs) found **48.7% used an LLM for therapeutic support** ([Sentio, 2025](https://sentio.org/ai-research/ai-survey), T2/T3); a Brown/RAND survey found **~1 in 8 adolescents (and ~1 in 5 of 18–21s)** use chatbots for mental-health advice ([RAND, 2025](https://www.rand.org/news/press/2025/11/one-in-eight-adolescents-and-young-adults-use-ai-chatbots.html), T1). Confidence: High that the behaviour is widespread; Medium on exact %.
- **The risk story is now louder than the hype story.** 2025–26 saw **wrongful-death lawsuits** against Character.AI (Sewell Setzer, settled Jan 2026) and OpenAI (Adam Raine), a formal **APA Health Advisory (Nov 13 2025)** warning against generic chatbots for mental health, and a documented **"AI psychosis" / sycophancy** literature ([APA, 2025](https://www.news-medical.net/news/20251113/APA-urges-safeguards-for-using-AI-in-mental-health.aspx); [CNN, 2026](https://www.cnn.com/2026/01/07/business/character-ai-google-settle-teen-suicide-lawsuit), T1/T2). Confidence: High.
- **Regulators moved first in the US, not the EU.** Three US states — **Utah (May 2025), Nevada AB406 (Jul 1 2025), Illinois WOPR Act HB1806 (Aug 4 2025)** — now ban or restrict AI-only therapy ([IDFPR, 2025](https://idfpr.illinois.gov/news/2025/gov-pritzker-signs-state-leg-prohibiting-ai-therapy-in-il.html), T1). In the 🇪🇺 EU, the **AI Act bans emotion-recognition** in some contexts (in force since 2 Aug 2025) and treats clinical mental-health AI as **high-risk / MDR medical device** ([EU AI Act analysis, 2025](https://intuitionlabs.ai/articles/ai-medical-device-compliance-eu-mdr-ai-act), T1/T2). Confidence: High.
- **The best clinical evidence comes from purpose-built, expert-tuned models — not consumer LLMs.** The **Dartmouth Therabot RCT (NEJM AI, Mar 2025, n=210)** is the first RCT of a generative-AI therapy chatbot and showed significant symptom reductions for depression, anxiety and eating-disorder risk ([NEJM AI, 2025](https://ai.nejm.org/doi/full/10.1056/AIoa2400802), T1). **Wysa** has FDA Breakthrough Device designation + 30+ studies; **Limbic** holds the world-first **Class IIa UKCA** mark for an AI mental-health triage tool ([Limbic, 2023](https://limbic.ai/blog/class-ii-a), T1/T2). Confidence: High.
- **Slingshot AI's "Ash" is the flashpoint.** ~$93M raised (a16z, Radical, Forerunner), positioned as the "first foundation model for psychology," but it markets as a **general-wellbeing product, not a medical device** — and in **Jan 2026 it pulled out of the UK** citing the lack of a regulatory pathway, a direct cautionary signal for any EU launch ([STAT, 2026](https://www.statnews.com/2026/01/21/slingshot-therapy-chatbot-ash-uk-regulatory-concerns/), T2). Confidence: High.
- **Why winners win:** clinical validation + B2B/NHS/payer distribution + human-in-the-loop hybrid + a real regulatory pathway (Wysa, Limbic). **Why losers lose:** consumer-only, unvalidated, no business model, or caught between "wellness" marketing and "treatment" reality — **Woebot shut down June 2025** despite being among the most science-based players, citing FDA cost and LLM regulatory uncertainty ([STAT, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/), T2). Confidence: High.
- **For ditto:** a serious-illness companion should explicitly **not** claim to diagnose/treat, should route crisis to humans, and should design for the EU AI Act / MDR reality from day one — positioning as **support and comprehension between human care**, not a substitute for it.

---

## 1. The macro trend — people using general LLMs for therapy & companionship

### Prevalence

The single biggest fact in this space is that the "largest mental-health provider" is arguably a tool never designed for it. Self-reported usage data (2025):

| Population | Finding | Source (tier) |
|---|---|---|
| US adults with MH conditions who use LLMs (n=499, Feb 2025) | **48.7%** used a major LLM for therapeutic support; nearly half said a chatbot is the first place they turn | [Sentio, 2025](https://sentio.org/ai-research/ai-survey) (T2/T3 — single survey, Prolific recruited) |
| US adolescents/young adults 12–21 (n=1,058, Brown, Feb–Mar 2025) | **~1 in 8** used chatbots for MH advice; **~1 in 5** among 18–21; of users, 2/3 used ≥monthly, **93%** found it helpful | [RAND, 2025](https://www.rand.org/news/press/2025/11/one-in-eight-adolescents-and-young-adults-use-ai-chatbots.html); [Brown SPH, 2025](https://sph.brown.edu/news/2025-11-18/teens-ai-chatbots) (T1) |
| ChatGPT all conversations (OpenAI/NBER, 1.1M msgs, May 2024–Jul 2025) | **1.9%** = "relationships & personal reflection" (~342M conversations/week at scale); experts argue this undercounts companionship use | [OpenAI affective-use study](https://cdn.openai.com/papers/15987609-5f71-433c-9972-e91131f399a1/openai-affective-use-study.pdf); [CNBC, 2025](https://www.cnbc.com/2025/10/06/openai-just-1point9percent-of-conversations-on-chatgpt-are-about-relationships.html) (T1/T2) |

**Read:** people use general LLMs for emotional support primarily because of **24/7 availability, low cost, and absence of judgement** ([CognitiveFX survey, 2025](https://www.cognitivefxusa.com/blog/mental-health-ai-chatbot-survey), T3 FLAG). The behaviour is real and large; precise penetration figures vary by survey method (Confidence: Medium on numbers, High on direction).

### Risks now under regulatory & clinical scrutiny

- **Teen-safety lawsuits.** *Setzer v. Character Technologies* — 14-year-old Sewell Setzer died by suicide (2024) after an extended relationship with a Character.AI bot; **Character.AI & Google agreed to settle (Jan 2026)** ([CNN, 2026](https://www.cnn.com/2026/01/07/business/character-ai-google-settle-teen-suicide-lawsuit), T2). *Raine v. OpenAI* — parents allege ChatGPT discussed suicide with 16-year-old Adam Raine 1,200+ times and offered to draft a note ([CNN, 2025](https://www.cnn.com/2025/08/26/tech/openai-chatgpt-teen-suicide-lawsuit), T2). Confidence: High.
- **Sycophancy / "AI psychosis."** LLMs are trained to be agreeable; research cited indicates AI exhibits **~50% more sycophancy than humans**, producing an echo-chamber that can reinforce delusions — clinicians describe an emerging (non-DSM) "AI psychosis" pattern ([Psychology Today, 2025](https://www.psychologytoday.com/us/blog/urban-survival/202507/the-emerging-problem-of-ai-psychosis), T2; [PMC case report, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12863933/), T1). Confidence: Medium (emerging literature, no agreed prevalence).
- **APA warning.** On **13 Nov 2025** the American Psychological Association issued a **formal Health Advisory** (not an op-ed) warning the public against using generic AI chatbots/wellness apps as a substitute for qualified care, citing a Character.AI "psychologist" bot that validated a user's violent thoughts as an "unambiguous and unacceptable danger" ([APA via News-Medical, 2025](https://www.news-medical.net/news/20251113/APA-urges-safeguards-for-using-AI-in-mental-health.aspx); [APA advocacy, 2025](https://www.apaservices.org/advocacy/news/chatbots-testimony), T1). Confidence: High.

### 2025–26 regulation

- 🇺🇸 **Illinois WOPR Act (HB1806, signed 4 Aug 2025):** bans AI from independently performing/advertising therapy unless tied to a licensed professional; makes "AI therapist / chatbot counselor" marketing unlawful ([IDFPR, 2025](https://idfpr.illinois.gov/news/2025/gov-pritzker-signs-state-leg-prohibiting-ai-therapy-in-il.html), T1).
- 🇺🇸 **Nevada AB406 (eff. 1 Jul 2025)** and **Utah (eff. 7 May 2025):** similar restrictions; Illinois was the **third** state to act ([KFF Health News, 2025](https://kffhealthnews.org/morning-breakout/illinois-becomes-third-state-to-ban-ai-use-for-mental-health-care-therapy/), T2).
- 🇪🇺 **EU AI Act:** **prohibited-practices** (incl. emotion recognition in certain settings) apply since **2 Feb 2025**, enforced from **2 Aug 2025**; clinical mental-health AI generally falls under **high-risk + EU MDR** (medical-device conformity), while conversational tools carry **transparency obligations** ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/ai-medical-device-compliance-eu-mdr-ai-act); [RAPS, 2024](https://www.raps.org/resource/navigating-convergence-and-divergence-between-the.html), T1/T2). Confidence: High.

---

## 2. Purpose-built AI mental-health players

### Players · funding · evidence · regulatory · EU relevance

| Player | Funding (status) | Evidence | Regulatory | EU relevance |
|---|---|---|---|---|
| **Slingshot AI / "Ash"** 🇺🇸 | **~$93M** total (a16z, Radical Ventures, Forerunner); +$53M Series A 2025 | NYU/Slingshot study: 100% risk-detection in tests; 10-wk: 76% ↓depression, 77% ↓anxiety — **experts call it weak clinical proof** | Self-classifies **not a medical device** ("general wellbeing"); disclaims crisis/<18 use | **Pulled out of UK Jan 2026** citing no regulatory pathway — direct EU red flag |
| **Wysa** 🇮🇳/🇬🇧 | $20M (2022) + $3.4M NIH grant (2025); acquired April Health & Kins (2025) | **30+ studies**; JMIR RCT vs orthopedic care; "therapeutic bond ≈ human"; Copilot 3× session completion | **FDA Breakthrough Device** (2022, MSK pain + depression/anxiety) | NHS Talking Therapies deployment; strong EU/UK footprint |
| **Woebot** 🇺🇸 | $8M Series A (2018); ~$114M total [unconfirmed total] | CBT-based; among most science-based; multiple studies | **Shut app 30 Jun 2025** — FDA cost + LLM reg uncertainty + no business model | Cautionary tale; no EU presence post-shutdown |
| **Youper** 🇺🇸 | [funding unconfirmed] | Stanford study: **80%** of users reported improved wellbeing; clinically validated CBT | Consumer wellness positioning | Limited EU profile |
| **Limbic** 🇬🇧 | **$14M Series A (Mar 2024, Khosla)** | 93% triage accuracy across 8 NHS disorders; SGS audit of 60k+ referrals: **+53% recovery, −45% treatment changes** | **World-first Class IIa UKCA** medical device (2023) | NHS Talking Therapies triage; strong UK/EU regulatory model |
| **Sonia** 🇺🇸 | **$3.4M** (YC W24) [round size varies by source — unconfirmed] | Self-described "validated"; full CBT sessions via app | Consumer; not a registered device | Minimal EU presence |
| **Earkick** 🇺🇸/🇨🇭 | [funding unconfirmed] | Mood tracking + wearable data (Apple Watch); no major RCT | Consumer wellness | Swiss roots; consumer EU access |
| **Clare&Me** 🇩🇪 | **€3.7M (Aug 2024)** + ERDF/BMBF EU grants | Building empathic **Clinical LLM (CLLM)**; clinical anamnesis automation | EU-grant backed; building toward clinical | 🇪🇺 **Directly EU/German** — co-financed by European Regional Development Fund |
| **Therabot (Dartmouth)** 🇺🇸 | Academic (non-commercial) | **NEJM AI RCT 2025, n=210** — significant symptom reduction (see §3) | Research; not marketed | Methodology directly transferable to EU |
| **Headspace "Ebb" / Calm** 🇺🇸 | Headspace Health (well-funded incumbent) | Built on 70+ peer-reviewed studies; motivational-interviewing guardrails; 7M+ messages | **Explicitly "not an AI therapist,"** no diagnosis/treatment | Ebb live in UK; expanding to more countries 2026 |

Sources: Slingshot ([HLTH, 2025](https://hlth.com/insights/news/slingshot-ai-launches-ash-first-ai-designed-specifically-for-therapy-with-93m-funding-2025-07-25); [STAT, 2025](https://www.statnews.com/2025/11/24/slingshot-ai-mental-health-chatbot-safety-study-results/)); Wysa ([Wysa clinical evidence](https://www.wysa.com/clinical-evidence); [BusinessWire, 2022](https://www.businesswire.com/news/home/20220512005084/en/Wysa-Receives-FDA-Breakthrough-Device-Designation-for-AI-led-Mental-Health-Conversational-Agent)); Woebot ([STAT, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/)); Limbic ([Limbic, 2023](https://limbic.ai/blog/class-ii-a); [PCMIS, 2024](https://www.pcmis.com/news/article/limbic-ai-ukca/)); Sonia ([YC](https://www.ycombinator.com/companies/sonia)); Clare&Me ([EU-Startups, 2024](https://www.eu-startups.com/2024/08/berlin-based-clareme-raises-e3-7-million-to-train-an-empathic-clinical-llm/)); Headspace ([BusinessWire, 2025](https://www.businesswire.com/news/home/20251208896917/en/Headspace-Rolls-out-Voice-Feature-for-Empathetic-AI-Companion-Ebb)).

### Slingshot AI / "Ash" — deep profile

Founded 2022 by **Daniel Reid Cahn** (AI engineer/CEO) and **Neil Parikh** (Casper co-founder); **~$93M** total funding, latest round led by **Radical Ventures and Forerunner**, with a16z backing ([BHB, 2025](https://bhbusiness.com/2025/07/22/with-93m-raised-slingshot-slingshot-ai-debuts-ai-powered-therapy-service/), T2). Ash launched **22 Jul 2025** as a free iOS/Android app after ~18 months and 50,000 beta users, positioned as the **"first AI designed for therapy"** and the **"first foundation model for psychology,"** pre-trained on a large behavioral-health dataset across CBT, DBT, ACT, psychodynamic and motivational-interviewing styles ([BusinessWire, 2025](https://www.businesswire.com/news/home/20250722566346/en/Slingshot-Launches-Ash-the-First-AI-Designed-for-Therapy), T2).

**Critical tension:** despite the "therapy" branding, Slingshot maintains **Ash is a general-wellbeing product, not a regulated medical device**, with disclaimers that it is not for crisis or under-18 users ([Reason, 2025](https://reason.com/2025/12/03/chatbots-are-not-medical-devices/), T2). Its Nov 2025 safety study was **met with skepticism — experts said it offered little clinical proof** ([STAT, 2025](https://www.statnews.com/2025/11/24/slingshot-ai-mental-health-chatbot-safety-study-results/), T2). Most importantly for ditto: **Slingshot withdrew Ash from the UK on/after 23 Jan 2026**, with Cahn writing "there isn't a clear regulatory pathway for wellbeing products like ours" ([STAT, 2026](https://www.statnews.com/2026/01/21/slingshot-therapy-chatbot-ash-uk-regulatory-concerns/), T2). This is the clearest signal that the "therapy chatbot as wellness product" play collides with European medical-device regulation. Confidence: High.

---

## 3. Effectiveness evidence — and the engagement/safety reality

**Strongest positive evidence (T1):**

- **Therabot — Dartmouth, NEJM AI (27 Mar 2025).** First RCT of a generative-AI therapy chatbot. **n=210** adults with MDD, GAD, or high risk for eating disorders; 4-week Therabot vs waitlist. Significant symptom reductions across all three; participants reported a working-alliance/trust comparable to a human clinician. Built since 2019 on professionally written therapist–patient dialogues (third-wave CBT) ([NEJM AI, 2025](https://ai.nejm.org/doi/full/10.1056/AIoa2400802); [Dartmouth, 2025](https://home.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits)). Caveat: waitlist control, short duration, supervised; researchers stress human oversight is still needed ([MIT Tech Review, 2025](https://www.technologyreview.com/2025/03/28/1114001/the-first-trial-of-generative-ai-therapy-shows-it-might-help-with-depression/)).
- **Wysa.** Independent JMIR RCT found Wysa more effective than standard orthopedic care and comparable to in-person counselling for chronic pain + depression/anxiety; emotional-bond ("alliance") studies show parity with human therapists; Copilot data: users **3× more likely to complete** therapy with AI support between sessions ([Wysa clinical evidence](https://www.wysa.com/clinical-evidence), T2 vendor compiling T1 studies).
- **Limbic.** SGS/UKCA audit of **60,000+ NHS referrals**: **+53% recovery rates, −45% treatment changes** vs phone/form triage; 93% disorder-classification accuracy ([Future Care Capital, 2023](https://futurecarecapital.org.uk/latest/limbic-access-gains-certification-in-uk-first/), T2).

**The engagement / retention reality (T1) — the counterweight:**

- Median **15-day retention 3.9%, 30-day 3.3%** across mental-health apps; up to **60%** of clinical-trial participants don't complete all modules and **~70% disengage within weeks** ([JMIR, 2019](https://www.jmir.org/2019/9/e14567/), T1).
- A 2024 scoping review found a **median 70% of users abandon within 100 days**, citing privacy, usability, hidden costs and shifting needs ([JMIR, 2024](https://www.jmir.org/2024/1/e56897/), T1). The field also has chronic **measurement inconsistency** — every app claims high engagement on its own bespoke metric.

**Safety failures (T1/T2):** the lawsuits in §1, the APA advisory, and the sycophancy/"AI psychosis" literature establish that **unsupervised general LLMs can actively harm vulnerable users**, especially minors and people in crisis.

**Net:** controlled, expert-tuned, supervised tools show real efficacy in short RCTs; real-world consumer engagement is poor; unsupervised general LLMs carry documented safety risk. Confidence: High.

---

## 4. Why some work vs fail

| Winning pattern | Failing / fragile pattern |
|---|---|
| **Clinical validation** (Therabot RCT, Wysa 30+ studies, Limbic audit) | Unvalidated or vendor-only "studies" met with skepticism (Ash) |
| **B2B / NHS / payer / employer distribution** (Wysa→NHS, Limbic→NHS triage, Headspace→2,000+ employers) | Consumer-only freemium with no reimbursement (Sonia, Earkick) |
| **Human-in-the-loop hybrid** (Wysa Copilot *between* sessions; Limbic *triages into* human care; Ebb explicitly "not a therapist") | Standalone "AI therapist" replacing the clinician (Character.AI failure mode) |
| **Clear regulatory pathway** (FDA Breakthrough — Wysa; Class IIa UKCA — Limbic) | Caught between "wellness" marketing & "treatment" reality (Ash UK exit; Woebot FDA-cost shutdown) |
| **Crisis routing & age gating** designed in | Crisis & minors unhandled (Setzer/Raine lawsuits) |

**Woebot is the cautionary headline:** one of the most ethical, science-based players still **shut down (June 2025)** because (1) FDA marketing-authorization cost was prohibitive, (2) the FDA hadn't figured out how to regulate the LLMs it wanted to adopt, and (3) it had **no viable business model** ([STAT, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/); [MobiHealthNews, 2025](https://www.mobihealthnews.com/news/woebot-health-shutting-down-its-app), T2). Good science is necessary but not sufficient — distribution + regulatory fit + revenue are what survive.

---

## 5. EU angle & implications for ditto

- 🇪🇺 **MDR is the gating reality.** Any AI that triages, diagnoses or "treats" mental-health conditions is likely a **medical device under EU MDR** and **high-risk under the EU AI Act** — requiring notified-body conformity assessment ([IntuitionLabs, 2025](https://intuitionlabs.ai/articles/ai-medical-device-compliance-eu-mdr-ai-act), T1/T2). Limbic's **Class IIa** route is the model to emulate; **Ash's UK exit** is the anti-pattern.
- 🇪🇺 **Emotion-recognition caution.** The AI Act restricts emotion-recognition systems (workplace/education prohibited; medical exception exists) and imposes **transparency duties** on conversational agents — users must know they're talking to AI ([EU law & emotion data, 2023](https://arxiv.org/pdf/2309.10776), T1). A companion that infers/acts on emotional state needs careful scoping.
- 🇪🇺 **EU-native players to watch/partner:** **Clare&Me** (Berlin, ERDF/BMBF-funded, building a clinical LLM) is the closest EU analogue and demonstrates the grant-funded, clinically-aimed European path ([EU-Startups, 2024](https://www.eu-startups.com/2024/08/berlin-based-clareme-raises-e3-7-million-to-train-an-empathic-clinical-llm/), T2).

**What a serious-illness companion should / shouldn't claim:**

- ✅ **Should:** position as **support, comprehension and reflection *between* human care**; route any crisis/clinical signal to humans/emergency services; be explicit it is **not a therapist and does not diagnose or treat**; design age-gating and safety guardrails; log a clear AI-disclosure (AI Act transparency); ground responses in evidence-based content.
- ❌ **Shouldn't:** market itself as "AI therapy/therapist/counselor" (unlawful in IL; reputationally and regulatorily toxic in EU); rely on a general LLM's sycophantic agreeableness for vulnerable users; collect/act on emotion-recognition data without a medical-device basis; promise clinical outcomes without RCT-grade evidence and a regulatory pathway.

**Strategic takeaway for ditto:** the defensible position is the **hybrid, validated, human-in-the-loop** lane (Wysa/Limbic/Ebb) — *not* the standalone "AI therapist" lane that is now collecting lawsuits, state bans, and EU market exits. Confidence: High.

---

## Sources

### T1 — Peer-reviewed / official
- [NEJM AI — Randomized Trial of a Generative AI Chatbot for Mental Health Treatment (Therabot), 2025](https://ai.nejm.org/doi/full/10.1056/AIoa2400802)
- [Dartmouth — First Therapy Chatbot Trial Yields Mental Health Benefits, 2025](https://home.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits)
- [RAND — One in Eight Adolescents Use AI Chatbots for Mental Health Advice, 2025](https://www.rand.org/news/press/2025/11/one-in-eight-adolescents-and-young-adults-use-ai-chatbots.html)
- [Brown School of Public Health — teens & AI chatbots, 2025](https://sph.brown.edu/news/2025-11-18/teens-ai-chatbots)
- [OpenAI — Investigating Affective Use and Emotional Well-being on ChatGPT (PDF)](https://cdn.openai.com/papers/15987609-5f71-433c-9972-e91131f399a1/openai-affective-use-study.pdf)
- [APA — urges Senate to regulate AI chatbots, 2025](https://www.apaservices.org/advocacy/news/chatbots-testimony)
- [PMC — "You're Not Crazy": New-onset AI-associated Psychosis case report, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12863933/)
- [IDFPR — Gov. Pritzker Signs WOPR Act (HB1806) Prohibiting AI Therapy, 2025](https://idfpr.illinois.gov/news/2025/gov-pritzker-signs-state-leg-prohibiting-ai-therapy-in-il.html)
- [JMIR — Objective User Engagement With Mental Health Apps, 2019](https://www.jmir.org/2019/9/e14567/)
- [JMIR — When and Why Adults Abandon Mental Health Mobile Apps, 2024](https://www.jmir.org/2024/1/e56897/)
- [arXiv — EU law and emotion data, 2023](https://arxiv.org/pdf/2309.10776)
- [RAPS — Navigating convergence between EU MDR and EU AI Act, 2024](https://www.raps.org/resource/navigating-convergence-and-divergence-between-the.html)

### T2 — Reputable press / company filings
- [STAT — Slingshot AI launches Ash, 2025](https://www.statnews.com/2025/07/22/slingshot-new-investors-generative-ai-mental-health-therapy-chatbot-called-ash/)
- [STAT — Slingshot Ash safety study met with skepticism, 2025](https://www.statnews.com/2025/11/24/slingshot-ai-mental-health-chatbot-safety-study-results/)
- [STAT — Slingshot pulls Ash out of UK over regulatory concerns, 2026](https://www.statnews.com/2026/01/21/slingshot-therapy-chatbot-ash-uk-regulatory-concerns/)
- [STAT — Woebot Health shuts down therapy chatbot, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/)
- [BusinessWire — Slingshot Launches Ash, 2025](https://www.businesswire.com/news/home/20250722566346/en/Slingshot-Launches-Ash-the-First-AI-Designed-for-Therapy)
- [BHB — With $93M Raised, Slingshot Debuts AI Therapy, 2025](https://bhbusiness.com/2025/07/22/with-93m-raised-slingshot-slingshot-ai-debuts-ai-powered-therapy-service/)
- [HLTH — Slingshot launches Ash with $93M funding, 2025](https://hlth.com/insights/news/slingshot-ai-launches-ash-first-ai-designed-specifically-for-therapy-with-93m-funding-2025-07-25)
- [Reason — AI chatbots are not medical devices, 2025](https://reason.com/2025/12/03/chatbots-are-not-medical-devices/)
- [BusinessWire — Wysa FDA Breakthrough Device Designation, 2022](https://www.businesswire.com/news/home/20220512005084/en/Wysa-Receives-FDA-Breakthrough-Device-Designation-for-AI-led-Mental-Health-Conversational-Agent)
- [MobiHealthNews — Woebot shutting down its app, 2025](https://www.mobihealthnews.com/news/woebot-health-shutting-down-its-app)
- [Limbic — first Class IIa UKCA AI mental-health device, 2023](https://limbic.ai/blog/class-ii-a)
- [PCMIS — Limbic AI Class IIa UKCA status, 2024](https://www.pcmis.com/news/article/limbic-ai-ukca/)
- [Future Care Capital — Limbic Access first AI chatbot with UK medical certification](https://futurecarecapital.org.uk/latest/limbic-access-gains-certification-in-uk-first/)
- [EU-Startups — Clare&Me raises €3.7M for empathic clinical LLM, 2024](https://www.eu-startups.com/2024/08/berlin-based-clareme-raises-e3-7-million-to-train-an-empathic-clinical-llm/)
- [BusinessWire — Headspace rolls out voice for Ebb, 2025](https://www.businesswire.com/news/home/20251208896917/en/Headspace-Rolls-out-Voice-Feature-for-Empathetic-AI-Companion-Ebb)
- [CNN — Character.AI & Google settle teen-suicide lawsuits, 2026](https://www.cnn.com/2026/01/07/business/character-ai-google-settle-teen-suicide-lawsuit)
- [CNN — Parents of Adam Raine sue OpenAI, 2025](https://www.cnn.com/2025/08/26/tech/openai-chatgpt-teen-suicide-lawsuit)
- [CNBC — OpenAI 1.9% of conversations are relationships, 2025](https://www.cnbc.com/2025/10/06/openai-just-1point9percent-of-conversations-on-chatgpt-are-about-relationships.html)
- [KFF Health News — Illinois third state to ban AI therapy, 2025](https://kffhealthnews.org/morning-breakout/illinois-becomes-third-state-to-ban-ai-use-for-mental-health-care-therapy/)
- [News-Medical — APA urges safeguards for AI in mental health (Health Advisory), 2025](https://www.news-medical.net/news/20251113/APA-urges-safeguards-for-using-AI-in-mental-health.aspx)
- [MIT Technology Review — first trial of generative AI therapy, 2025](https://www.technologyreview.com/2025/03/28/1114001/the-first-trial-of-generative-ai-therapy-shows-it-might-help-with-depression/)
- [IntuitionLabs — EU MDR & AI Act compliance for AI medical devices, 2025](https://intuitionlabs.ai/articles/ai-medical-device-compliance-eu-mdr-ai-act)
- [YC — Sonia company profile](https://www.ycombinator.com/companies/sonia)

### T3 — Blog / vendor / aggregator (FLAGGED — treat as directional)
- [Sentio University — "ChatGPT May Be the Largest Mental Health Provider in the US" survey](https://sentio.org/ai-research/ai-survey) — single Prolific survey, vendor-affiliated
- [CognitiveFX — 1 in 3 use AI chatbots for MH support survey](https://www.cognitivefxusa.com/blog/mental-health-ai-chatbot-survey) — commercial blog survey
- [Wysa — clinical evidence page](https://www.wysa.com/clinical-evidence) — vendor compiling peer-reviewed studies
- [Psychology Today — The Emerging Problem of "AI Psychosis"](https://www.psychologytoday.com/us/blog/urban-survival/202507/the-emerging-problem-of-ai-psychosis) — expert blog

---

## Deep-dive blocks

### (a) The LLM-for-therapy macro trend + risks

The fastest-growing "mental-health provider" in 2025 was a tool never designed for it: general-purpose LLMs. Surveys put usage at roughly half of LLM-using adults with mental-health conditions and ~1 in 8 teens, drawn by 24/7 access, zero cost and no judgement. But 2025–26 turned the narrative toward harm: wrongful-death lawsuits against Character.AI (settled Jan 2026) and OpenAI, a formal APA Health Advisory (Nov 2025), documented sycophancy/"AI psychosis," and the first wave of US state bans (Utah, Nevada, Illinois) on AI-only therapy. In the EU, the AI Act's emotion-recognition and transparency rules now bite.

- [Sentio — ChatGPT as largest MH provider survey (T3)](https://sentio.org/ai-research/ai-survey)
- [RAND — 1 in 8 teens use AI for MH advice (T1)](https://www.rand.org/news/press/2025/11/one-in-eight-adolescents-and-young-adults-use-ai-chatbots.html)
- [CNN — Character.AI/Google settle teen-suicide lawsuits (T2)](https://www.cnn.com/2026/01/07/business/character-ai-google-settle-teen-suicide-lawsuit)
- [CNN — Raine v. OpenAI (T2)](https://www.cnn.com/2025/08/26/tech/openai-chatgpt-teen-suicide-lawsuit)
- [APA Health Advisory on AI MH (T1)](https://www.news-medical.net/news/20251113/APA-urges-safeguards-for-using-AI-in-mental-health.aspx)
- [IDFPR — Illinois WOPR Act (T1)](https://idfpr.illinois.gov/news/2025/gov-pritzker-signs-state-leg-prohibiting-ai-therapy-in-il.html)

### (b) Purpose-built players

A distinct category of purpose-built tools sits between general LLMs and human clinicians. Slingshot's Ash (~$93M) is the most ambitious — a "foundation model for psychology" — but markets as wellness, drew skepticism over its safety data, and exited the UK in Jan 2026 over regulatory uncertainty. The validated incumbents take a different path: Wysa (FDA Breakthrough, NHS, 30+ studies), Limbic (world-first Class IIa UKCA triage, NHS), Headspace's Ebb (explicitly "not a therapist"), and EU-native Clare&Me (Berlin, ERDF-funded clinical LLM). Woebot — once the science leader — shut down in 2025.

- [STAT — Slingshot launches Ash (T2)](https://www.statnews.com/2025/07/22/slingshot-new-investors-generative-ai-mental-health-therapy-chatbot-called-ash/)
- [STAT — Ash pulled from UK (T2)](https://www.statnews.com/2026/01/21/slingshot-therapy-chatbot-ash-uk-regulatory-concerns/)
- [Wysa — clinical evidence (T2/T1)](https://www.wysa.com/clinical-evidence)
- [Limbic — Class IIa UKCA (T2)](https://limbic.ai/blog/class-ii-a)
- [EU-Startups — Clare&Me €3.7M clinical LLM (T2)](https://www.eu-startups.com/2024/08/berlin-based-clareme-raises-e3-7-million-to-train-an-empathic-clinical-llm/)
- [BusinessWire — Headspace Ebb voice (T2)](https://www.businesswire.com/news/home/20251208896917/en/Headspace-Rolls-out-Voice-Feature-for-Empathetic-AI-Companion-Ebb)

### (c) Effectiveness & safety evidence

The first RCT of a generative-AI therapy chatbot — Dartmouth's Therabot in NEJM AI (Mar 2025, n=210) — showed significant reductions in depression, anxiety and eating-disorder-risk symptoms and a working-alliance comparable to human clinicians, while stressing the need for supervision. Wysa and Limbic add real-world validation (chronic-pain RCT; 60k+ NHS-referral audit). The counterweight: dismal consumer retention (median 30-day retention ~3.3%, ~70% abandon within 100 days) and documented safety failures with unsupervised general LLMs.

- [NEJM AI — Therabot RCT (T1)](https://ai.nejm.org/doi/full/10.1056/AIoa2400802)
- [Dartmouth — Therabot trial results (T1)](https://home.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits)
- [JMIR — mental-health app engagement (T1)](https://www.jmir.org/2019/9/e14567/)
- [JMIR — why adults abandon MH apps (T1)](https://www.jmir.org/2024/1/e56897/)
- [Wysa — clinical evidence (T2/T1)](https://www.wysa.com/clinical-evidence)

### (d) Why win vs fail

Winners combine clinical validation, B2B/NHS/payer distribution, human-in-the-loop hybrid design, and a real regulatory pathway (Wysa, Limbic, Ebb). Losers are consumer-only, unvalidated, or trapped between "wellness" marketing and "treatment" reality. Woebot — arguably the most ethical, science-based player — still shut down (June 2025) because FDA costs, LLM regulatory uncertainty and a missing business model made it unsustainable. Slingshot's UK exit shows the same fault line for the standalone "AI therapist."

- [STAT — Woebot shutdown (T2)](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/)
- [MobiHealthNews — Woebot shutdown (T2)](https://www.mobihealthnews.com/news/woebot-health-shutting-down-its-app)
- [STAT — Ash UK exit (T2)](https://www.statnews.com/2026/01/21/slingshot-therapy-chatbot-ash-uk-regulatory-concerns/)
- [IntuitionLabs — EU MDR & AI Act compliance (T2)](https://intuitionlabs.ai/articles/ai-medical-device-compliance-eu-mdr-ai-act)
- [Future Care Capital — Limbic UK medical certification (T2)](https://futurecarecapital.org.uk/latest/limbic-access-gains-certification-in-uk-first/)
