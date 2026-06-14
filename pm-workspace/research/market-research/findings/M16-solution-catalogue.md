# M16 — Solution Catalogue: What Already Works in Consumer Health (and Adjacent Apps)

**Module:** M16 (Proven-Mechanic Catalogue — "take a proven mechanic and make it BETTER")
**Prepared for:** ditto.care — EU/NL patient-facing health-tech, building from AI appointment summaries toward a daily "Living Health Companion"
**Author:** Product-strategy research analyst
**Date / access date:** 2026-06-14
**Lens:** Mark Pincus — *don't invent a new behaviour, take a PROVEN behaviour/mechanic and make it better.* This catalogue inventories the mechanics that already retain users in consumer health AND in adjacent consumer apps, so ditto can decide, mechanic by mechanic, what to **Adopt** as-is vs **Innovate** on.

> **Sourcing conventions.** Inline citations use `[Source, year](url)`. **Tier 1 (T1)** = analyst / company-verified / financial-grade · **Tier 2 (T2)** = reputable press · **Tier 3 (T3)** = blog / vendor stat-aggregator / app-store self-report (explicitly **FLAGGED**). Where a figure was carried over from ditto's existing corpus (M1–M15) rather than re-researched, it is tagged **[corpus]**. Anything I could not source is marked *unconfirmed*. Figures are EU-anchored where possible but the named universe is global. Access date for all live URLs: **2026-06-14**.

---

## How to use this catalogue

1. **Read Layer A first** (the Category Map). It groups the market by *job-to-be-done* and *dominant retention mechanic*, names exemplars, and says **why the mechanic works or fails**. This is where the strategy lives.
2. **Use Layer B as a lookup** (the 100+ product master table). Every named product carries a **Category**, **Primary mechanism(s)**, a one-line **why it works**, a **Health / Adjacent** tag, a **Traction signal**, and an **Adopt-or-Innovate flag** for ditto.
3. **The "Adopt / Innovate" flag is the deliverable.** "Adopt" = a proven mechanic ditto should copy more-or-less as-is (cheap, low-risk, expected by users). "Innovate" = a mechanic that works elsewhere but must be *bent* to ditto's wedge (the post-appointment summary → daily companion) to be defensible. "Avoid" = a mechanic that looks attractive but is a known churn or trust trap for ditto's context.
4. **Mind the failure modes.** The most important rows are not the unicorns — they are the *cautionary tales* (Fitbit, Babylon, the clinical-logger churn pattern). Pincus's lens cuts both ways: copy what works, refuse what doesn't.

---

## Key takeaways

- **The single most transferable winning pattern is "anticipatory daily question with a changing answer + compounding personal data."** Cycle apps (Flo, Clue, Natural Cycles) and wearables (Oura, Whoop) own it; meditation and clinical loggers don't, and they churn. ditto's episodic appointment summary must be wrapped in a *daily, predictive, compounding* loop or it inherits the 90-day H&F churn curve. **This is ditto's #1 Innovate target.**
- **Gamification works in health only when the reward is emotional/relational, not point-shaped.** Finch (care-pet, Duolingo-class D1/D7) and Duolingo's streak/loss-aversion machine retain; literal "health points" do not. **Adopt the streak/loss-aversion *frame*, innovate the *reward* (companion warmth, not gold coins).**
- **Grounded answer engines are the fastest-rising mechanic and the one most aligned to ditto's data.** OpenEvidence (>40% of US physicians, ~$12B), Ada, K Health, ChatGPT Health (~40M/wk health users) prove demand for *cited, trustworthy answers*. ditto's differentiator is that its answers can be grounded in **the user's own appointment record**, not the open web. **Innovate hard here — it is the wedge.**
- **AI scribes are the upstream supply of ditto's raw material, and several already ship patient-facing summaries.** Abridge ($5.3B, $100M ARR), Nabla, Heidi, Suki, Dragon Copilot, Corti (EU) capture the consult; the patient-summary layer is mostly an afterthought for them. **ditto's "Adopt the transcript, Innovate the patient experience" position is structurally sound — partner upstream, own the consumer loop.**
- **EU-rooted distribution rails (Doctolib, NHS App, MedMij PGOs, Doctolib/ePA) are the realistic acquisition channel, not US D2C ad spend.** The strongest consumer-health retainers in ditto's own backyard are women's-health (Flo, Clue) and access/PHR rails. **Adopt the EU-trust + integration playbook; avoid the US ad-funnel model that bankrupted Babylon.**

---

# LAYER A — Category Map

Fifteen health/adjacent categories + one "borrow-from-outside" category. For each: the **job-to-be-done (JTBD)**, the **dominant mechanic(s)**, **why it works/fails**, and exemplars.

## A1. Cycle / women's & reproductive health
**JTBD:** "Tell me what my body is doing and what's coming next." **Mechanic:** daily prediction of an unknown (period, fertile window, due date) + per-cycle compounding data + life-stage urgency. **Why it works:** the biology *changes daily*, the question is anxiety-charged, each logged cycle is a switching cost — the textbook variable-reward + data-moat loop. Strongest retention category in consumer health and **EU-rooted**. **Exemplars:** Flo, Clue, Natural Cycles, Ovia, Maven Clinic, Midi Health, Tia, Wisp/Stardust.
**ditto read:** the *gold-standard mechanic to emulate*. ditto's appointment data can power an analogous "what's coming / is this normal" daily forecast for chronic patients. **Innovate.**

## A2. Meditation / sleep
**JTBD:** "Help me calm down / fall asleep now." **Mechanic:** ritual + immediate affective reward + streaks + content library ("Spotify of calm"). **Why it fails to compound:** the answer doesn't change day-to-day, no predictive personal-data moat, value is substitutable (free YouTube/Spotify). Category peaked (~2021) and is decaying; survivors are pivoting to AI companions (Ebb). **Exemplars:** Calm, Headspace, Insight Timer, Balance, BetterSleep, Sleep Cycle, Ebb.
**ditto read:** copy the *bedtime/daily ritual trigger* and audio-first delivery, but never rely on content alone. **Adopt ritual; Avoid content-only model.**

## A3. Mental health & AI therapy / companions
**JTBD:** "Help me feel better / get support I can afford & access now." **Mechanic:** low-friction conversational check-in + CBT framing + (human) marketplace OR (AI) always-on empathetic companion. **Why it works:** stigma + access gap make 24/7 private support uniquely valuable; conversation is a *daily-relevant changing answer*. **Why it's risky:** safety/liability, regulatory scrutiny (Therabot RCT vs. Character.AI harms), clinical-evidence bar. **Exemplars (human):** BetterHelp, Talkspace, Lyra, Quartet, Naluri. **(AI):** Woebot, Wysa, Youper, Clare&Me, Earkick, Sonia, Limbic, Therabot, Character.AI, Slingshot/Ash, Stoic, MindDoc.
**ditto read:** the *empathetic conversational companion* is the closest analog to ditto's "Living Health Companion" tone. **Innovate (tone + grounding); Avoid unsupervised clinical claims.**

## A4. Symptom tracking & checkers
**JTBD:** "What might be wrong with me / should I worry?" **Mechanic:** structured triage Q&A → probable causes + next-step routing (self-care vs. GP vs. ER). **Why it works:** answers an acute, high-anxiety question; **why it churns:** episodic use, no daily reason to return, accuracy/liability scrutiny (Babylon collapse). **Exemplars:** Ada Health, Infermedica/Symptomate, Buoy Health, K Health, Isabel, WebMD Symptom Checker, Your.MD/Healthily, Mediktor, Docus.
**ditto read:** triage is episodic — useful as a *feature*, not a retention engine. **Adopt as a feature; don't build the business on it.**

## A5. Medication adherence & reminders
**JTBD:** "Help me take my meds correctly, on time." **Mechanic:** scheduled reminders + streak/adherence score + caregiver/"Medfriend" loop + refill nudges. **Why it works:** clear daily trigger, measurable behaviour, caregiver social pressure; **why it plateaus:** utilitarian, low emotional reward, easy to ignore. **Exemplars:** Medisafe, MyTherapy, Round Health, Pillsy, Hero, CareZone, Dosecast.
**ditto read:** ditto already knows a patient's meds from the appointment summary — adherence is a *natural daily hook* that flows from its data. **Adopt the reminder loop; Innovate the link to "why" (the appointment context).**

## A6. Digital health coaches (chronic disease)
**JTBD:** "Help me manage my chronic condition day-to-day." **Mechanic:** connected device/data + human or AI coach + structured program + (B2B2C) payer/employer funding. **Why it works:** clinical outcomes + reimbursement create durable LTV; **why it's hard:** CAC and clinical proof are expensive, D2C habit weak without the coach. **Exemplars:** Omada, Virta, Lark, Dario, Hello Heart, Vida, Sword Health, Hinge Health, Kaia, Sweetch, Oviva (EU).
**ditto read:** the *condition-specific daily program* and B2B2C funding model are highly relevant. **Innovate (an AI-coach layered on the patient's real record); study Hinge/Sword/Oviva for EU reimbursement.**

## A7. Fitness & wearables
**JTBD:** "Track and improve my body / activity." **Mechanic:** passive capture → compounding data → daily score (Readiness, Strain, Recovery) → renewal; plus identity & social. **Why it works:** zero-effort logging + a *new number every morning* (anticipatory) + subscription data-moat; **failure mode:** hardware without an interpreted-insight subscription erodes (Fitbit). **Exemplars:** Oura, Whoop, Fitbit, Garmin, Apple Fitness+/Apple Watch, Samsung Health, Strava, Zwift, Peloton, Ultrahuman.
**ditto read:** *passive capture + daily interpreted score* is the most powerful retention mechanic in the catalogue. ditto can't capture biometrics, but can deliver a daily *interpreted-health-state* read from records + symptoms. **Innovate (the "morning health read").**

## A8. Nutrition & food
**JTBD:** "Help me eat better / hit a goal." **Mechanic:** logging (manual or scan) + database moat + score/grade + behaviour-change program. **Why it works:** Yuka's one-scan instant grade is near-zero-friction and *shareable*; **why it churns:** manual calorie logging is effortful, payoff deferred. **Exemplars:** MyFitnessPal, Noom, Yuka, ZOE, Lose It, Cronometer, Lifesum, Foodvisor, Fooducate, Yazio.
**ditto read:** Yuka's "scan → instant grade → share" is a copyable *instant-verdict* pattern. **Adopt the instant-verdict UX; Innovate by grading against the patient's actual conditions.**

## A9. AI health assistants & grounded answer engines
**JTBD:** "Give me a trustworthy, cited answer to my health question." **Mechanic:** LLM + retrieval over vetted medical sources + citations + (for ditto) grounding in the user's own record. **Why it works:** it is the consumerization of "Dr. Google" done right — cited, conversational, fast; fastest-rising mechanic in the market. **Exemplars:** OpenEvidence, ChatGPT/ChatGPT Health, Gemini, Claude/Claude for Healthcare, Perplexity (Health), Glass Health, Consensus, UpToDate, OpenAI/Ada, Docus, K Health.
**ditto read:** **the core wedge.** ditto's answers grounded in the *patient's own appointment record* is a moat no open-web engine has. **Innovate — hardest and most important.**

## A10. Personal health records / aggregation & access
**JTBD:** "Put all my health data in one place I control." **Mechanic:** aggregation across providers + patient-controlled record + (EU) regulated data-exchange rails. **Why it works:** utility + EHDS/MedMij tailwind; **why it's inert:** a record people open only when sick — low daily frequency unless wrapped in insight. **Exemplars:** Apple Health, b.well, Epic MyChart, NHS App, Doctolib, MedMij PGOs (Quli, Ivido, Medicalla), ePA (DE), Hint Health, Healthie.
**ditto read:** ditto IS a PHR-adjacent product; the lesson is **a record alone is inert — the daily insight loop is what converts aggregation into retention.** **Adopt the aggregation rails (EU integration); Innovate the daily-use layer on top.**

## A11. Care navigation & second opinion
**JTBD:** "Help me find the right care / confirm this diagnosis." **Mechanic:** human navigator + expert-network second opinion + benefits steering (B2B2C). **Why it works:** healthcare is bewildering and high-stakes; employers pay for it; **why D2C is hard:** episodic, expensive, trust-heavy. **Exemplars:** Included Health, Transcarent, 2nd.MD, Grand Rounds, Teladoc, Amazon One Medical, Accolade, Docus (2nd opinion).
**ditto read:** navigation is episodic but high-trust; ditto's record gives it the context to *route intelligently*. **Adopt as a feature triggered by the appointment context.**

## A12. Caregiver coordination
**JTBD:** "Help my family/friends coordinate care for a loved one." **Mechanic:** shared status updates + task/meal calendars + group communication + journaling. **Why it works:** multi-stakeholder, emotionally urgent, network effects; **why it's niche:** episodic (around a crisis), hard to monetize D2C. **Exemplars:** CaringBridge, Lotsa Helping Hands, ianacare, Carely, Birdie (EU homecare), Jointly, CircleOf.
**ditto read:** ditto's "share my summary with family" is a natural caregiver bridge. **Adopt the share-with-circle pattern; Innovate by auto-generating updates from appointment summaries.**

## A13. Curated medical content
**JTBD:** "Give me reliable health information to read." **Mechanic:** SEO-optimized, clinician-reviewed library + brand trust. **Why it works:** massive search demand, trust brands (Mayo, Cleveland Clinic); **why it's threatened:** generative answer engines are disintermediating the click. **Exemplars:** Healthline, WebMD, Mayo Clinic, Cleveland Clinic, Patient.info, NHS.uk, Thuisarts.nl (NL), Apotheek.nl (NL).
**ditto read:** content is now a *grounding source*, not a destination. **Adopt clinician-reviewed content as RAG fuel; don't build a content destination.**

## A14. Voice / ambient health
**JTBD:** "Let me interact with health hands-free / let the system listen and act." **Mechanic:** voice agent / ambient capture → action or summary. **Why it's nascent:** accuracy + privacy + trust bars are high; few durable consumer wins yet. **Exemplars:** Hyro, Alexa (health skills/Amazon Health), Google/Gemini Live, Suki (clinician voice), Sonia (voice therapy), Ebb (voice mode).
**ditto read:** voice is a *delivery channel* for the companion (audio daily brief), not a category to own. **Adopt as a delivery mode; watch the space.**

## A15. Longevity / diagnostics / proactive testing
**JTBD:** "Catch problems early / optimize my healthspan." **Mechanic:** comprehensive lab/imaging panels + dashboard + AI interpretation + membership recurring revenue. **Why it works (now):** affluent, motivated cohort + "data about my future self" is anticipatory + recurring testing = renewal; **risk:** overdiagnosis, cost, evidence debate. **Exemplars:** Function Health, Superpower, Neko Health, InsideTracker, Levels, Zero, Hone, Forward (defunct — cautionary).
**ditto read:** the *AI-interpreted personal-results dashboard* is exactly ditto's translate-the-clinical-into-plain-language muscle, applied to labs. **Innovate (interpretation layer); note the affluent-niche ceiling.**

## A16. PROVEN MECHANICS FROM OUTSIDE HEALTH (the borrow-from sources)
The richest source of *better* mechanics, because non-health apps have spent a decade perfecting habit loops with none of health's episodic-use handicap.

| Mechanic | Best-in-class exemplar(s) | What it is | How ditto borrows it |
|---|---|---|---|
| **Streak + loss-aversion + variable reward** | **Duolingo** | Daily streak, streak-freeze, league, owl nudges | Daily "health check-in" streak — but reward = companion relationship, not points. **Innovate.** |
| **Wrapped / personal data narrative** | **Spotify Wrapped**, Strava year-in-review | Periodic shareable summary of *your* data | "Your health year in review" / quarterly health story from records. **Adopt.** |
| **Social graph as the moat** | **Strava** (segments, kudos, clubs) | Identity + peer accountability | Opt-in condition communities / share-with-circle. **Innovate (privacy-careful).** |
| **Streak as relationship, daily prompt** | **BeReal**, **Snapchat streaks** | Time-boxed daily prompt; mutual streaks | A single, well-timed daily prompt ("today's health moment"). **Adopt the once-a-day prompt.** |
| **Flexible doc / second brain** | **Notion** | User-owned, composable knowledge base | "My health" as a living, user-editable document. **Adopt the doc metaphor.** |
| **Conversational, personality-led finance coach** | **Cleo**, **Monzo**, **Robinhood** | Chat persona + nudges + plain-language summaries of complex data + "round-ups" | Cleo's witty money-coach tone + Monzo's plain-language transaction feed → a plain-language *health* feed with a warm AI persona. **Innovate (closest tonal analog to ditto).** |
| **Swipe / low-friction match loop** | **Tinder**, **Hinge** | One-decision-at-a-time, dopamine-light loop | Low-friction daily "one thing to review" card. **Adopt the single-card UX.** |
| **Identity + content + algorithmic feed** | **Instagram/TikTok** | Endless personalized feed | A *finite*, personalized daily health brief (anti-doomscroll). **Adopt the personalization, reject the infinite feed.** |

**ditto read:** the **Cleo/Monzo "personality-led plain-language coach over your own complex data"** model is the single closest non-health analog to the Living Health Companion. The **Duolingo streak-as-relationship** and **Spotify Wrapped data-narrative** are the two most copyable habit mechanics. These three are the priority borrow-from sources.

---

# LAYER B — Master product table (≥100 named products)

**Legend.** Tag = **Health** or **Adjacent** (non-health, clearly marked). Flag = **Adopt** (copy mechanic ~as-is) / **Innovate** (bend to ditto's wedge) / **Avoid** (known trap) / **Watch** (monitor). Traction figures: **[corpus]** = carried from ditto's M1–M15 corpus; otherwise cited inline. *unconf.* = unconfirmed.

### Cycle / women's & reproductive health
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 1 | **Flo** | Cycle/women's | Daily cycle prediction + AI assistant; per-cycle compounding | Anticipatory daily "is this normal" answer | Health | ~77M MAU, ~5M paid, ~$275M rev, ~$1B val (2025) [corpus] | Innovate |
| 2 | **Clue** | Cycle/women's | Science/privacy-led tracking; research dataset | Trust + data moat; EU-rooted | Health | ~10M+ MAU, 1M paid subs (2025) [corpus] | Innovate |
| 3 | **Natural Cycles** | Cycle/contraception | Daily temp entry gates FDA-cleared contraceptive claim | Usage *is* the regulated product | Health | >3M users; first FDA-cleared (2024) [corpus] | Innovate |
| 4 | **Ovia Health** | Pregnancy/parenting | Full fertility→parenting continuum; B2B2C employer | Distribution moat via employers | Health | 22M+ journeys; 305+ clients [corpus] | Watch |
| 5 | **Maven Clinic** | Women's/family virtual care | Care navigation + virtual specialists; B2B2C | Employer-funded full lifecycle | Health | $1.7B+ val; femtech unicorn (2024) [[Maven, 2024](https://www.mavenclinic.com/)] T2 | Watch |
| 6 | **Midi Health** | Menopause/midlife women | Virtual clinicians + insurance-covered | Underserved menopause cohort | Health | $100M+ raised (2024–25) [[Midi, 2025](https://www.joinmidi.com/)] T2 *unconf.* | Watch |
| 7 | **Tia** | Women's whole-health clinics | Hybrid in-person + virtual membership | Bundled women's primary care | Health | ~$130M raised (T2, *unconf.*) | Watch |
| 8 | **Stardust** | Cycle (privacy-first) | Astrology-flavored cycle tracking, privacy stance | Post-*Dobbs* privacy positioning | Health | Topped US App Store 2022 (T3) | Watch |

### Meditation / sleep
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 9 | **Calm** | Meditation/sleep | Sleep Stories + streaks + content library | Bedtime ritual trigger; content moat | Health | ~3.5M subs, ~$210M rev (2025, declining) [corpus] | Adopt(ritual) |
| 10 | **Headspace** | Meditation | Structured courses + B2B; Ebb AI | Employer channel + brand | Health | ~2M subs, ~$140M rev (2025) [corpus] | Adopt(ritual) |
| 11 | **Ebb (Headspace AI)** | Meditation/AI companion | AI conversational daily trigger + voice | Manufactures a recurring reason to open | Health | 7M+ messages; 2,000+ employers (2025) [corpus] | Innovate |
| 12 | **Insight Timer** | Meditation | Largest *free* library + timer + teachers | Free-content + community breadth | Health | ~27M+ users; 120K+ meditations [[ChoosingTherapy, 2024](https://www.choosingtherapy.com/insight-timer-review/)] T3 | Adopt(ritual) |
| 13 | **Balance** | Meditation (personalized) | Adaptive daily plan; free year-1 growth hack | Personalization + aggressive free tier | Health | Apple App of Year 2021; millions DLs (T3) | Watch |
| 14 | **BetterSleep** | Sleep | Soundscapes + sleep tracking + bedtime routine | Audio-first sleep ritual | Health | 60M+ downloads (vendor, T3) *unconf.* | Adopt(ritual) |
| 15 | **Sleep Cycle** | Sleep | Smart alarm + sleep-stage tracking | Passive nightly capture + morning read | Health | Tens of M DLs; long-running (T3) | Adopt |

### Mental health & AI therapy / companions
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 16 | **BetterHelp** | Teletherapy (human) | Marketplace matching to licensed therapists | Access + convenience at scale | Health | ~2.5M users (Teladoc-owned) [[SEC/press, 2025](https://www.sec.gov/Archives/edgar/data/0001803901/000095017025102417/talk-ex99_2.htm)] T2 | Watch |
| 17 | **Talkspace** | Teletherapy (human) | Async + insurance/payer channel | Payor coverage drives growth | Health | ~$59.4M Q3'25 rev (record) [[SEC 8-K, 2025](https://www.sec.gov/Archives/edgar/data/0001803901/000095017025102417/talk-ex99_2.htm)] T1 | Watch |
| 18 | **Lyra Health** | Mental health (B2B2C) | Employer EAP + matched care + outcomes | Employer-funded, measurement-based | Health | $5.6B+ val (2022) [corpus] | Watch |
| 19 | **Quartet Health** | Behavioral health navigation | Payer-led matching to behavioral care | Routing under insurance | Health | Carried in corpus [corpus] | Watch |
| 20 | **Naluri** | Mental+chronic coaching (APAC) | Human coach + chat + lessons | B2B2C emerging-market coaching | Health | Carried in corpus [corpus] | Watch |
| 21 | **Woebot** | AI CBT chatbot | Rules-based CBT conversation | Pioneer of conversational CBT | Health | Wound down consumer app 2025 [corpus] | Avoid(model) |
| 22 | **Wysa** | AI mental-health companion | AI chat + CBT tools + human escalation | Hybrid AI+human, NHS/employer deals | Health | ~6.5M+ users; FDA breakthrough (T3) [corpus] | Innovate |
| 23 | **Youper** | AI emotional-health assistant | AI mood chat + CBT; RCT evidence | Evidence-backed AI companion | Health | Carried in corpus [corpus] | Innovate |
| 24 | **Clare&Me** | AI voice mental-health (EU/DE) | Voice + text AI companion | EU-built voice therapy | Health | Carried in corpus [corpus] | Innovate |
| 25 | **Earkick** | AI mental-health tracker | Passive + chat mood tracking, no signup | Frictionless, privacy-first | Health | Carried in corpus [corpus] | Innovate |
| 26 | **Sonia** | AI voice therapist | Voice-first AI CBT sessions | Voice delivery of structured therapy | Health | Carried in corpus [corpus] | Watch |
| 27 | **Limbic** | AI mental-health triage (UK) | Clinical AI assistant for NHS IAPT | NHS-embedded, regulated AI | Health | UKCA Class IIa; NHS deployments [corpus] | Innovate |
| 28 | **Therabot** | AI therapy (research) | Generative therapy chatbot, RCT-tested | First RCT showing symptom reduction | Health | Dartmouth RCT 2025 [corpus] | Watch |
| 29 | **Character.AI** | AI companions (general) | Open-ended persona chat; heavy DAU | Parasocial engagement (and its harms) | Adjacent | 20M+ MAU; safety scrutiny [corpus] | Avoid(safety) |
| 30 | **Ash / Slingshot AI** | AI therapy app | Purpose-built therapy LLM | VC-backed dedicated therapy model | Health | $93M raise (Slingshot) [corpus] | Watch |
| 31 | **Stoic** | Mood/journaling + stoicism | Guided journaling + mood + ritual | Reflective daily writing habit | Health | Carried in corpus [corpus] | Adopt |
| 32 | **MindDoc (MoodPath)** | Mood tracking (clinical, DE) | Daily mood check-ins + screening | EU clinical mood logger | Health | ~3M users [corpus] | Adopt |
| 33 | **Sanvello** | Self-help mental health | CBT/mindfulness + mood + community | Self-guided + insurance tie-ins | Health | Millions DLs (UnitedHealth-owned) T3 | Watch |
| 34 | **Daylio** | Mood micro-journaling | One-tap mood + activity logging | Near-zero-friction daily log | Health | Tens of M DLs (T3) [corpus] | Adopt |
| 35 | **How We Feel** | Emotion tracking | Emotion-wheel check-ins; non-profit | Emotional-granularity habit | Health | Carried in corpus [corpus] | Adopt |
| 36 | **Finch** | Self-care gamified pet | Care-pet you nurture by self-care acts | Duolingo-class emotional reward loop | Health | ~10M MAU, ~$30M ARR; 54/37% D1/D7 [corpus] | Innovate |

### Symptom tracking & checkers
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 37 | **Ada Health** | Symptom checker (DE) | AI triage Q&A → probable causes | Clinical-grade triage, EU-built | Health | 13M+ users; 30M+ assessments [corpus] | Adopt(feature) |
| 38 | **Infermedica / Symptomate** | Symptom-checker infra (PL) | Triage engine + API for providers | B2B triage rails across EU | Health | 100M+ checks; many payers [corpus] | Adopt(feature) |
| 39 | **Buoy Health** | Symptom checker (US) | Conversational AI triage → navigation | Triage→care routing | Health | Carried; employer deals (T3) | Adopt(feature) |
| 40 | **K Health** | AI primary care | Symptom AI + telehealth + Rx | AI triage *into* a care transaction | Health | $900M+ val; millions users [corpus] | Innovate |
| 41 | **Your.MD / Healthily** | Self-care + checker (UK) | Symptom AI + self-care library | Self-care guidance engine | Health | Carried in corpus [corpus] | Adopt(feature) |
| 42 | **Docus** | AI health + 2nd opinion | AI assistant + doctor network 2nd opinion | AI answer + human verification | Health | Carried in corpus [corpus] | Innovate |
| 43 | **Isabel Healthcare** | DDx checker | Differential-diagnosis engine | Long-standing clinical DDx tool | Health | Clinician-focused (T3) | Watch |
| 44 | **Mediktor** | Symptom checker (ES) | AI triage, multilingual, EU | EU/LatAm triage rails | Health | 100+ deployments (T3) *unconf.* | Adopt(feature) |
| 45 | **Bearable** | Symptom/chronic tracking | Manual multi-factor symptom logging | Correlation insights for chronic | Health | ~900K users [corpus] | Avoid(churn) |

### Medication adherence & reminders
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 46 | **Medisafe** | Med adherence | Reminders + adherence score + Medfriend | Caregiver loop + AI adherence pred. | Health | ~10M+ registered; 650M+ doses [[Medisafe, 2025](https://www.medisafe.com/)] T3 | Adopt |
| 47 | **MyTherapy** | Med adherence (DE) | Reminders + health diary + reports | EU-built pill+symptom combo | Health | 10M+ downloads (vendor) T3 | Adopt |
| 48 | **Round Health** | Med reminders | Elegant "time-window" reminders | Best-in-class reminder UX | Health | Top-rated; niche (T3) | Adopt |
| 49 | **Pillsy** | Smart pill + app | Connected cap + reminders | Hardware-verified adherence | Health | Niche (T3) *unconf.* | Watch |
| 50 | **Hero** | Med dispenser + app | Hardware dispenser + reminders + refill | Physical dispensing automation | Health | $120M+ raised (T2) *unconf.* | Watch |
| 51 | **CareZone** | Med + family health mgmt | Med list scan + shared family records | Caregiver med organization | Health | Acquired by Walmart 2020 (T2) | Watch |
| 52 | **Dosecast** | Med reminders | Cross-platform flexible reminders | Reliable utilitarian reminders | Health | Niche (T3) | Adopt |

### Digital health coaches (chronic)
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 53 | **Omada Health** | Chronic prevention (US) | Connected devices + coach + program; B2B2C | Reimbursed outcomes at scale | Health | IPO 2025; ~$170M+ rev (T2) | Watch |
| 54 | **Virta Health** | Diabetes reversal | Ketogenic program + remote MD + CGM | Outcomes-based diabetes reversal | Health | Carried in corpus [corpus] | Innovate |
| 55 | **Lark** | AI chronic coach | Fully-AI conversational coach; B2B2C | AI-only coaching at low marginal cost | Health | Carried in corpus [corpus] | Innovate |
| 56 | **Dario** | Chronic (multi-condition) | Connected devices + app + coaching | Multi-condition data platform | Health | Carried in corpus [corpus] | Watch |
| 57 | **Hello Heart** | Heart/BP coach | Connected BP cuff + AI nudges | Passive BP capture + nudge loop | Health | Carried in corpus [corpus] | Innovate |
| 58 | **Sword Health** | MSK digital therapy | Sensor-guided PT + AI/clinician; B2B2C | Computer-vision PT at home | Health | ~$4B val; $130M+ ARR (2025) [corpus] | Watch |
| 59 | **Hinge Health** | MSK digital therapy | Wearable-sensor PT + coaching; B2B2C | Largest MSK; IPO 2025 | Health | IPO 2025 (~$2.6B+) [corpus] | Watch |
| 60 | **Kaia Health** | MSK + COPD (DE) | Motion-tracking PT via phone camera | EU-built CV physiotherapy | Health | Carried in corpus [corpus] | Watch |
| 61 | **Vida Health** | Chronic + mental (US) | Combined physical+mental coaching; B2B2C | Whole-person employer coaching | Health | $100M+ raised (T2) *unconf.* | Watch |
| 62 | **Sweetch** | AI behavior-change | Hyper-personalized AI nudges | Just-in-time adaptive prompts | Health | Niche (T3) | Innovate |
| 63 | **Oviva** | Diet/diabetes coach (EU) | Dietitian + app; reimbursed in DE/UK | EU-reimbursed nutrition therapy | Health | 800K+ patients EU (T3) *unconf.* | Innovate |

### Fitness & wearables
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 64 | **Oura** | Wearable (ring) | Passive capture → daily Readiness score | Morning anticipatory score; renewal moat | Health | >80% yr-1 renewal; ~$1B rev, ~$11B val (2025) [corpus] | Innovate |
| 65 | **Whoop** | Wearable (band) | Passive capture → Strain/Recovery | Subscription data-moat; daily read | Health | >50% daily use @18mo; ~$1B rev (2025) [corpus] | Innovate |
| 66 | **Fitbit** | Wearable | Step/HR tracking + badges | Hardware ubiquity *without* insight loop | Health | MAU sliding ~48M→~42M [corpus] | Avoid(model) |
| 67 | **Garmin** | Wearable/sport | Multi-sport tracking + Body Battery | Athlete loyalty + on-device value | Health | Tens of M devices; profitable (T2) | Adopt |
| 68 | **Apple Watch / Fitness+** | Wearable + fitness content | Rings/streaks + workouts + health data | Ecosystem lock-in + daily rings | Health | Hundreds of M devices (T2) [corpus] | Adopt(rings) |
| 69 | **Samsung Health** | Wearable/phone health hub | Aggregation + tracking on Galaxy | Default Android health aggregator | Health | Carried in corpus [corpus] | Watch |
| 70 | **Strava** | Fitness social | Social graph: segments, kudos, clubs | Identity + peer accountability moat | Adjacent-ish | 180M registered; ~$500M ARR (2025) [corpus] | Innovate(social) |
| 71 | **Zwift** | Fitness (virtual cycling) | Gamified group rides; multiplayer | Social game layer on exercise | Health | Carried in corpus [corpus] | Watch |
| 72 | **Peloton** | Connected fitness | Live/on-demand classes + leaderboard | Instructor charisma + social ranks | Health | ~$2.7B rev (declining) (T2) | Watch |
| 73 | **Ultrahuman** | Wearable (ring/CGM) | Ring + metabolic CGM + scores | Metabolic-focused wearable | Health | $100M+ raised (T2) *unconf.* | Watch |

### Nutrition & food
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 74 | **MyFitnessPal** | Nutrition logging | Calorie log + huge food database | Food-database moat (but declining) | Health | ~220M registered, 30M+ MAU [corpus] | Adopt(db) |
| 75 | **Noom** | Weight/behavior change | Psychology lessons + coach + logging | CBT-flavored behavior program | Health | Carried in corpus [corpus] | Watch |
| 76 | **Yuka** | Food/cosmetics scanner | Scan → instant grade → shareable | Near-zero-friction instant verdict | Health | ~70–80M users (2025) [[NPR, 2025](https://www.npr.org/2025/05/26/nx-s1-5391915/phone-apps-food-nutrition-health)] T2 | Adopt(verdict) |
| 77 | **ZOE** | Nutrition science (UK) | Microbiome+CGM test → personalized scores | Test-driven personalized nutrition | Health | $100M+ raised (T2) *unconf.* | Innovate |
| 78 | **Lose It!** | Calorie counter | Logging + Snap-It photo recognition | Photo-based food logging | Health | 50M+ users (vendor) T3 | Adopt |
| 79 | **Cronometer** | Micronutrient tracking | Detailed nutrient logging | Precision micronutrient data | Health | Millions; niche-power-user (T3) | Watch |
| 80 | **Lifesum** | Nutrition (EU/SE) | Logging + diet plans + scores | EU-built nutrition tracker | Health | 60M+ users (vendor) T3 | Adopt |
| 81 | **Foodvisor** | Nutrition (FR) | AI photo food recognition | Image-recognition logging | Health | 10M+ DLs (T3) | Adopt |
| 82 | **Fooducate** | Food grading | Barcode → nutrition grade + community | Early instant-grade pioneer | Health | Millions DLs (T3) | Adopt(verdict) |
| 83 | **Yazio** | Nutrition/fasting (DE) | Logging + fasting plans | EU-built diet + fasting combo | Health | 50M+ users (vendor) T3 | Watch |

### AI health assistants & grounded answer engines
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 84 | **OpenEvidence** | Grounded answers (clinician) | RAG over journals (NEJM) + citations | Cited, trusted clinical answers | Health | >40% US physicians; ~$12B val (2026) [corpus] | Innovate |
| 85 | **ChatGPT / ChatGPT Health** | General + health AI | Conversational LLM + (Health) grounding | Default "Dr. Google" replacement | Adjacent/Health | ~40M/wk health users (2026) [corpus] | Innovate |
| 86 | **Gemini** | General AI assistant | LLM + Google health surfaces | Search-integrated answers | Adjacent | Hundreds of M users (T2) [corpus] | Watch |
| 87 | **Claude / Claude for Healthcare** | General + health AI | LLM + healthcare tooling/MCP | Enterprise+dev health grounding | Adjacent/Health | Claude for Healthcare (2025–26) (T2) | Watch |
| 88 | **Perplexity (Health)** | Answer engine | Web RAG + citations | Cited conversational search | Adjacent | Tens of M users (T2) | Watch |
| 89 | **Glass Health** | Clinical AI (DDx) | AI DDx + plan for clinicians | Clinician reasoning assistant | Health | YC-backed; clinician traction (T3) | Watch |
| 90 | **Consensus** | Research answer engine | AI over peer-reviewed papers | Evidence-cited science answers | Health | Millions users (T3) | Adopt(grounding) |
| 91 | **UpToDate** | Clinical reference | Curated, clinician-authored evidence | Gold-standard clinician reference | Health | Wolters Kluwer; ubiquitous (T2) | Adopt(grounding) |
| 92 | **Babylon Health** | AI primary care (defunct) | Symptom AI + telehealth; ad-funnel growth | **Cautionary tale**: scaled CAC, collapsed | Health | Bankrupt 2023 [corpus] | Avoid(model) |

### Personal health records / aggregation & access
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 93 | **Apple Health** | PHR/aggregation | On-device aggregation + HealthKit | Default iOS health hub | Health | Hundreds of M devices [corpus] | Adopt(rails) |
| 94 | **b.well** | PHR platform (US) | FHIR aggregation + navigation | White-label health hub | Health | Partner deals (T2) | Watch |
| 95 | **Epic MyChart** | Patient portal | Provider EHR portal + messaging | Embedded in US provider visits | Health | 190M+ records (T2) | Adopt(rails) |
| 96 | **NHS App** | National PHR/access (UK) | Records + Rx + appts; national rail | Government default access app | Health | ~30M+ registered (UK) (T2) *unconf.* | Adopt(rails) |
| 97 | **Doctolib** | Booking/access (EU) | Appointment booking + records; EU rail | Dominant EU booking rail | Health | ~80M+ patients EU (FR/DE/IT) (T2) *unconf.* | Adopt(rails) |
| 98 | **MedMij PGO (Quli/Ivido/Medicalla)** | PHR rail (NL) | Patient-controlled record exchange (NL) | NL regulated PHR standard | Health | NL national framework [corpus] | Adopt(rails) |
| 99 | **ePA "für alle"** | National PHR (DE) | National electronic patient record | German default EHR rail | Health | Rolling out to all insured (2025) [corpus] | Adopt(rails) |
| 100 | **Hint Health** | DPC infrastructure (US) | Direct-primary-care membership infra | Powers DPC subscriptions | Health | B2B infra (T3) | Watch |
| 101 | **Healthie** | Care infra/PHR | EHR + scheduling + patient app API | Dev platform for health apps | Health | B2B infra (T3) | Watch |

### Care navigation & second opinion
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 102 | **Included Health** | Navigation + virtual care | Navigator + expert opinion + care; B2B2C | One front-door for employer members | Health | Merged Grand Rounds+Doctor on Demand (T2) | Watch |
| 103 | **Transcarent** | Health navigation (US) | AI navigation + benefits; B2B2C | AI front door; Accolade acquisition | Health | ~$3B val; 20M+ members (2025) [[CNBC, 2025](https://www.cnbc.com/2025/06/10/transcarent-cnbc-disruptor-50.html)] T2 | Watch |
| 104 | **2nd.MD** | Second opinion | Expert-physician video 2nd opinions | High-stakes diagnosis confidence | Health | Employer-funded (T2) | Adopt(feature) |
| 105 | **Grand Rounds** | Navigation/2nd opinion | Expert matching + navigation (now Included) | Expert-network routing | Health | Part of Included Health (T2) | Watch |
| 106 | **Teladoc** | Telehealth (US) | Virtual visits + BetterHelp + chronic | Scale telehealth incumbent | Health | ~$2.6B rev (declining) [corpus] | Watch |
| 107 | **Amazon One Medical** | Primary care (US) | Membership primary care + Amazon scale | Retail-distributed primary care | Health | Amazon-owned; millions members (T2) | Watch |
| 108 | **Accolade** | Health advocacy (US) | Advocate + navigation; B2B2C | Human advocacy at employer scale | Health | Acquired by Transcarent $621M (2025) [[FierceHealthcare, 2025](https://www.fiercehealthcare.com/health-tech/transcarent-acquire-health-benefits-platform-accolade-621m-deal)] T2 | Watch |

### Caregiver coordination
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 109 | **CaringBridge** | Caregiver/health journal | Shared health-journey updates + support | Non-profit health-update network | Health | Millions of users; non-profit (T2) | Adopt |
| 110 | **Lotsa Helping Hands** | Care coordination | Shared task/meal calendars for circles | Coordinates practical help | Health | Long-running community (T3) | Adopt |
| 111 | **ianacare** | Caregiver support (US) | Caregiver coordination + employer benefit | "I Am Not Alone" caregiver support | Health | Employer deals (T2) *unconf.* | Watch |
| 112 | **Carely** | Family care coordination | Shared family updates + photos | Keeps family aligned on a loved one | Health | Niche (T3) | Adopt |
| 113 | **Birdie** | Homecare platform (EU/UK) | Homecare coordination + family app | EU homecare digitization | Health | $100M+ raised UK (T2) *unconf.* | Watch |
| 114 | **Jointly (Carers UK)** | Caregiver coordination (UK) | Shared notes/tasks for carers | Charity-backed carer tool | Health | Carers UK (T3) | Adopt |
| 115 | **CircleOf** | Care circle app | Care circle tasks + updates | Modern caregiver coordination | Health | Niche (T3) | Watch |

### Curated medical content
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 116 | **Healthline** | Health content | SEO clinician-reviewed library | Massive search traffic | Health | ~80M+ monthly visits (T2) | Adopt(grounding) |
| 117 | **WebMD** | Health content + checker | Content + symptom checker + ads | Legacy "Dr. Google" brand | Health | Tens of M monthly (T2) | Adopt(grounding) |
| 118 | **Mayo Clinic** | Health content | Clinician-authored, high-trust | Top trust brand | Health | Tens of M monthly (T2) | Adopt(grounding) |
| 119 | **Cleveland Clinic** | Health content | Clinician content + health essentials | High-trust health-system brand | Health | Tens of M monthly (T2) | Adopt(grounding) |
| 120 | **Patient.info** | Health content (UK) | Clinician-reviewed UK-focused info | Trusted UK patient info | Health | Millions monthly (T2) | Adopt(grounding) |
| 121 | **NHS.uk** | Health content (UK) | Authoritative public health info | Government-trust default | Health | National scale (T2) | Adopt(grounding) |
| 122 | **Thuisarts.nl** | Health content (NL) | GP-authored Dutch patient info | NL default plain-language source | Health | NL national; GP-backed (T2) | Adopt(grounding) |
| 123 | **Apotheek.nl** | Medication content (NL) | Pharmacist-authored med info (NL) | Trusted Dutch medicine info | Health | NL national (T3) | Adopt(grounding) |

### Voice / ambient health
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 124 | **Hyro** | Conversational AI (health) | Voice/chat agents for health systems | Automates provider front-desk | Health | Health-system deals (T2) | Watch |
| 125 | **Amazon Alexa (Health)** | Voice assistant | Voice health skills + Amazon Health | Ambient voice at home scale | Adjacent/Health | Hundreds of M devices (T2) | Watch |
| 126 | **Google/Gemini Live** | Voice assistant | Real-time multimodal voice AI | Conversational voice answers | Adjacent | Hundreds of M (T2) | Watch |

### Longevity / diagnostics / proactive testing
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 127 | **Function Health** | Longevity testing | 160+ lab panel + AI dashboard; membership | "Data about my future self" + renewal | Health | 200K+ members; ~$2.5B val, $298M Series B (2025) [[MedCity, 2025](https://medcitynews.com/2025/11/function-health-startup-testing-imaging/)] T2 | Innovate(interp) |
| 128 | **Superpower** | Longevity testing | Annual physical → continuous monitoring | Affluent proactive cohort | Health | $30M Series A, >$300M val (2025) [[FierceHealthcare, 2025](https://www.fiercehealthcare.com/health-tech/new-startup-superpower-scores-30m-launch-personalized-health-testing)] T2 | Watch |
| 129 | **Neko Health** | Body-scan diagnostics (SE) | Full-body scan + AI report; membership | High-touch EU preventive scan | Health | $260M raise; ~$1.8B val (2025) (T2) *unconf.* | Watch |
| 130 | **InsideTracker** | Blood biomarker optimization | Blood tests → personalized action plan | Biomarker-driven recommendations | Health | Long-running; niche (T3) | Innovate(interp) |
| 131 | **Levels** | Metabolic (CGM) | Real-time glucose + food feedback | Closed-loop metabolic feedback | Health | $300M+ val (2021) (T2) | Watch |
| 132 | **Zero** | Fasting/metabolic | Fasting timer + metabolic tracking | "World's most popular fasting tracker" | Health | Millions DLs (vendor) T3 | Watch |
| 133 | **Hone Health** | Hormone/longevity (men) | At-home hormone testing + telehealth Rx | Men's hormone optimization | Health | Niche (T3) | Watch |
| 134 | **Forward Health** | Preventive primary care (defunct) | CarePod kiosks + membership | **Cautionary tale**: shut down 2024 | Health | Shut down 2024 (T2) | Avoid(model) |

### AI scribes (upstream supply — many ship patient summaries)
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 135 | **Abridge** | AI scribe + patient summary | Ambient capture → clinician note + patient summary | Captures consult; ships patient-facing summary | Health | ~$5.3B val; ~$100M ARR; 150+ systems (2025) [[TechCrunch, 2025](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/)] T2 | Innovate(partner) |
| 136 | **Nabla** | AI scribe (FR/EU) | Ambient note + patient instructions | EU-built scribe; patient-summary layer | Health | $120M+ raised (2025) [[Sacra, 2025](https://sacra.com/c/abridge/)] T2 | Innovate(partner) |
| 137 | **Heidi Health** | AI scribe (AU/global) | Ambient note + patient summary | Fast-growing global scribe | Health | ~$86.6M raised (2025) [[Sacra, 2025](https://sacra.com/c/heidi-health/)] T2 | Innovate(partner) |
| 138 | **Suki** | AI scribe (voice) | Voice-first ambient documentation | Voice clinical documentation | Health | ~$168M raised (T2) | Watch |
| 139 | **Corti** | Health AI (EU/DK) | Ambient + clinical decision support | EU clinical-AI infrastructure | Health | EU-funded; deployments [corpus] | Innovate(partner) |
| 140 | **Tortus** | AI scribe (UK) | Ambient documentation + actions | EU/UK clinical scribe | Health | Seed/Series A (T3) *unconf.* | Watch |
| 141 | **Dragon Copilot (Microsoft/Nuance)** | AI scribe (incumbent) | Ambient note + summaries in EHR | Enterprise EHR-embedded scribe | Health | Microsoft-owned; ubiquitous (T2) [corpus] | Watch |
| 142 | **Ambience Healthcare** | AI scribe | Ambient documentation + coding | Unicorn scribe; coding focus | Health | $243M Series C (2025) [[Sacra, 2025](https://sacra.com/c/abridge/)] T2 | Watch |

### Borrow-from-outside-health exemplars (Adjacent)
| # | Product | Category | Primary mechanism(s) | Why it works (1 line) | Tag | Traction signal | Flag |
|---|---|---|---|---|---|---|---|
| 143 | **Duolingo** | Language learning | Streak + loss-aversion + leagues + nudges | Best-in-class daily-habit machine | Adjacent | ~100M+ MAU; public co (T2) | Innovate(streak) |
| 144 | **Spotify (Wrapped)** | Music + data narrative | Personalized year-in-review of *your* data | Shareable personal-data story | Adjacent | 600M+ MAU (T2) | Adopt(wrapped) |
| 145 | **BeReal** | Social (daily prompt) | One time-boxed daily prompt | Single authentic daily moment | Adjacent | Tens of M MAU (T2) | Adopt(daily prompt) |
| 146 | **Snapchat** | Social (streaks) | Mutual streaks + ephemeral content | Streaks as a relationship glue | Adjacent | 400M+ DAU (T2) | Adopt(streak) |
| 147 | **Notion** | Productivity (doc) | User-owned composable docs/db | "Second brain" flexibility | Adjacent | Tens of M users (T2) | Adopt(doc metaphor) |
| 148 | **Cleo** | Fintech AI coach | Witty chat persona over your money data | Personality-led plain-language coach | Adjacent | ~$150M+ ARR (T2) *unconf.* | Innovate(persona) |
| 149 | **Monzo** | Fintech (neobank) | Plain-language feed + nudges + pots | Plain-language complex-data feed | Adjacent | 10M+ customers (UK) (T2) | Innovate(feed) |
| 150 | **Robinhood** | Fintech (investing) | Simplified UI + nudges (and its critiques) | Mass-simplified complex domain | Adjacent | 20M+ users (T2) | Adopt(simplify) |
| 151 | **Hinge** | Dating | One-decision swipe + prompts | Low-friction single-card loop | Adjacent | Tens of M users (Match) (T2) | Adopt(single card) |
| 152 | **Tinder** | Dating | Swipe mechanic; variable reward | Dopamine-light decision loop | Adjacent | Tens of M users (T2) | Adopt(swipe) |

**Total named products: 152** (≥100 requirement met; ~80 reused/categorized from corpus, ~70+ newly added).

---

## Synthesis — the "make it BETTER" shortlist for ditto

Ranked by leverage on ditto's wedge (post-appointment summary → daily Living Health Companion):

1. **Anticipatory daily read** (from cycle apps + Oura/Whoop): a "today's health state / what to watch" card grounded in the user's record. **Innovate — top priority.**
2. **Personality-led plain-language coach** (from Cleo/Monzo, Ebb): warm AI persona translating clinical complexity. **Innovate — closest tonal analog.**
3. **Grounded, cited answers over the user's own data** (from OpenEvidence/Ada): the defensible moat. **Innovate.**
4. **Streak-as-relationship + single daily prompt** (from Duolingo/BeReal/Finch): the habit scaffold, reward = companion warmth not points. **Adopt the frame, innovate the reward.**
5. **Medication + adherence hook** (from Medisafe/MyTherapy): a ready-made daily trigger that flows from the appointment data. **Adopt.**
6. **Share-with-circle / caregiver bridge** (from CaringBridge + auto-summaries): turn the summary into a family artifact. **Adopt.**
7. **"Health Wrapped" data narrative** (from Spotify): periodic shareable personal-health story. **Adopt.**
8. **EU integration rails** (Doctolib / MedMij PGO / ePA / Thuisarts grounding): the realistic acquisition + trust channel. **Adopt.**

**Explicit Avoids:** US ad-funnel D2C growth (Babylon), hardware-without-insight (Fitbit), content-only retention (Calm decay), unsupervised clinical claims (Character.AI safety), capital-intensive physical footprints (Forward).

---

## Sources

**Carried from ditto corpus (M1–M15 — not re-researched):** Flo, Clue, Natural Cycles, Ovia, Calm, Headspace, Ebb, Oura, Whoop, Fitbit, Strava, MyFitnessPal, Finch, Ada, Infermedica, K Health, Wysa, Youper, Woebot, Clare&Me, Earkick, Sonia, Limbic, Therabot, Character.AI, Ash/Slingshot, Stoic, MindDoc, Daylio, How We Feel, Virta, Lark, Dario, Hello Heart, Sword Health, Hinge Health, Kaia, OpenEvidence, ChatGPT/Health, Babylon, Teladoc, Apple Health, MedMij PGO, ePA, Corti, Dragon Copilot, Lyra, Quartet, Naluri, Docus, Your.MD/Healthily figures — see `M1`, `M4`–`M15` findings files for per-claim citations and tiers.

**Newly cited this module (access 2026-06-14):**
- Medisafe — https://www.medisafe.com/ · T3 (vendor self-report)
- Talkspace Q3 2025 8-K — https://www.sec.gov/Archives/edgar/data/0001803901/000095017025102417/talk-ex99_2.htm · T1
- BetterHelp users — https://www.sec.gov/Archives/edgar/data/0001803901/000095017025102417/talk-ex99_2.htm · T2
- Function Health $2.5B / 200K members — https://medcitynews.com/2025/11/function-health-startup-testing-imaging/ · T2; https://athletechnews.com/function-health-raises-298-million-at-2-5-billion-valuation/ · T2; https://sacra.com/c/function-health/ · T2
- Superpower $30M Series A — https://www.fiercehealthcare.com/health-tech/new-startup-superpower-scores-30m-launch-personalized-health-testing · T2; https://sacra.com/c/superpower/ · T2
- Yuka ~70–80M users — https://www.npr.org/2025/05/26/nx-s1-5391915/phone-apps-food-nutrition-health · T2
- Transcarent ~$3B / 20M members / Accolade — https://www.cnbc.com/2025/06/10/transcarent-cnbc-disruptor-50.html · T2; https://www.fiercehealthcare.com/health-tech/transcarent-acquire-health-benefits-platform-accolade-621m-deal · T2
- Abridge $5.3B / $100M ARR — https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/ · T2; https://sacra.com/c/abridge/ · T2
- Heidi Health funding — https://sacra.com/c/heidi-health/ · T2
- Suki funding — https://sacra.com/c/suki/ · T2
- Insight Timer ~27M users — https://www.choosingtherapy.com/insight-timer-review/ · T3
- Maven Clinic — https://www.mavenclinic.com/ · T2 (vendor) *unconfirmed valuation*

**T3 / unconfirmed flags:** vendor download counts (MyTherapy, Lifesum, Yazio, BetterSleep, Foodvisor, Lose It, Medisafe, Insight Timer), and several "*unconf.*"-tagged valuations (Midi, Tia, Vida, Hero, Pillsy, Ultrahuman, ZOE, Neko, Birdie, ianacare, Tortus, NHS App, Doctolib patient counts) are order-of-magnitude indicative only and should be re-verified before use in external materials.
