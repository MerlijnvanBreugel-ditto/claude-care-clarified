# 12 — External Evidence: The Core Action

**Status:** synthesis of a fresh external deep-research campaign (2026-06-04): 73 agents, 1,482 searches, 10 product autopsies, 15 load-bearing claims each checked by 3 adversarial fact-checkers (0 killed, 13 corrected; corrections applied throughout, details in the appendix). Raw data with all quotes and URLs: [`research/core-action-evidence-sweep/`](../../../research/core-action-evidence-sweep/). Everything below the "Verified" headers is evidence; everything under "My read" is synthesis and labeled as such.

## Bottom line (my read)

1. **The wedge action is right, and the offline proof is strong.** 67% of German cancer patients want consultation recordings, 5% have ever made one, a quarter of those covertly. When patients get recordings, 60–100% listen back, and in 60% of studies they shared the recording with others. OWise's recording feature was used by 100% of studied patients and was the most-praised function, while half abandoned its symptom diary. NL law is fully on our side (KNMG: the doctor cannot refuse, the hospital cannot ban it).
2. **Daily WORK failed everywhere; daily VALUE via AI is young and points the other way.** [Corrected 2026-06-05 after Merlijn's challenge; the first version over-concluded "episodic beats daily" from pre-AI evidence.] Every autopsied product that assigned patients daily effort (forms, tests, structured diaries) decayed, and engagement anchored to events (appointments, scans, cycles). But those are failures of *manual work and silence*, not of daily need: voice-only check-ins hit 94% over 14 days, passive capture out-retains active asking (73% vs 61% in the same chemo study), proactive AI outreach sustains (Hippocratic, Tucuvi >90% in complex populations), and an AI companion held 47.8 min/day in memory care. No AI-native companion has published 6-month retention yet (all are under ~18 months old). Read: episodes are the proven anchor; an AI-led daily surface built on received value (synthesis, grounded answers, voice) instead of submitted work is the central open experiment, not a refuted idea.
3. **The patient is never the payer.** Every consumer-paid product in this space died or pivoted. Survivors switched the payer to employers, insurers, pharma, or donations. Untire and SkinVision prove NL insurer reimbursement exists. This validates the B2B GTM and warns against any consumer-subscription experiment.
4. **What AI newly enables is direction and effort, not motivation.** The proven shifts: app-initiated beats user-initiated (proactive outreach works where self-logging dies), photo/voice input collapses effort at the moment of least capacity, and grounded interpretation turns a 20-minute re-listen into a 30-second answer. What AI does not fix: distribution, the payer, and the episodic shape of demand.
5. **The window is narrowing.** Five direct competitors to the exact core action launched or scaled in the last 8 months (Mirror UK, Neatly US, Kin US, Hedy, plus incumbent Medcorder), and big tech is commoditizing the generic version (ChatGPT Health at ~230M weekly health questions, Microsoft Copilot Health, Oracle portal Q&A). Nobody combines EU/NL + oncology + the family circle + clinical distribution. That combination is the defensible position, and it is still open.

---

## 1. The user problem, verified in their words

**The update burden is a second job, and inbound support is a tax.** "I had so many people wanting to know how I was and I would lose track of what I had told to whom" (UK patient, set up a WhatsApp group for medical updates only). "Even my daily family text was exhausting" (caregiver). "Support can sometimes become overwhelming when every text, phone call, and update requires emotional energy to answer." The universal workaround is appointing one spokesperson; hospital nurses independently recommend it ("only one person call us"). Confidence: high.

**The treatment week has a predictable shape, and the diary's value is prediction.** Worst days are 3–5 after infusion; "we kept a diary and found that each cycle followed the same pattern... able to plan round good days and let him rest on bad." Confidence: high.

**The 2am loop has moved from Google to ChatGPT.** Googling escalates anxiety and then dies of fatigue ("search results stop offering reassurance... close an article almost immediately, not because of fear, but because of fatigue"). AI chatbots are now the default 3am companion, but they feed the reassurance-seeking loop, and without patient-specific memory they re-suggest strategies the person already tried (22% of the time in a dementia-caregiver study). Confidence: high.

**The cobbled stack is the real competitor.** Notebook plus phone Notes plus six alarms ("I have 6 alarms set on my phone", Parkinson's) plus the binder plus the designated note-taker in the room. The binder fails in a specific way: "It was easier to call me than to look through a very well organized binder." Whatever we build competes with calling the daughter. Confidence: high.

**Recording already happens, awkwardly.** Dutch breast-cancer guidance tells patients to record conversations ("Gesprekken opnemen om later rustig terug te luisteren"). An OWise patient: "I shared the audio with my parents who could not be present at the consult. It was comforting to know that they heard the information firsthand from the surgeon." Chemo brain affects up to 75% of patients during treatment, and the clinically recommended coping tool is literally a recorder. Confidence: high.

**Two corrections to our assumptions.** First, more sharing is not always wanted: dementia caregivers deliberately stop broadcasting ("I simply cannot be bothered to update all the people who haven't bothered to visit"). The circle feature needs a non-broadcast mode and full author control. Second, burden does not drive adoption: in a 117-caregiver study, caregiving burden and hours had NO association with intent to adopt an app; perceived usefulness alone explained 52% of variance (OR 23). Being needed is not enough; the payoff must be obvious in the first session. Confidence: high.

**Dutch specifics.** 80% of NL cancer patients use the hospital portal, ~89% to view results, and 70% want results immediately, even before the doctor explains them ("vandaag zat ik al te kijken of de uitslag niet stiekem wat eerder binnen was"). Only 7% use a cancer-specific app versus 42% general health apps. The most-used Dutch tools are hospital-embedded (MediMapp: 77% uptake where offered, 15–18 logins per care path), and the daily emotional activity lives in closed Facebook/WhatsApp groups that patient orgs themselves point to. Confidence: high.

---

## 2. Why past attempts failed (10 autopsies)

| Product | What it proved | Why it died/stalled | Does AI fix the cause? |
|---|---|---|---|
| **CareZone** (US, ~$200M Walmart IP sale 2020, app dead 2021) | 3.5M members want a med/info organizer | Enter-once product, no weekly pull; revenue lived in a severable pharmacy that a PBM killed; distressed exit dressed as a win | No. Business-structural |
| **Floodlight MS** (Roche, CE-certified) | Passive smartphone measurement is feasible | Patient did the work, Roche got the payoff; no in-the-moment value back; ~10% day-30 retention (reminders tripled it to ~31%) | Partially: AI can collapse effort, cannot manufacture a reason to return |
| **Gesprekshulp bij kanker** (NL, kanker.nl/KWF) | NL patients will record consults; the premise (40–80% forgotten) is the same as ours | Record-and-replay without summary or sharing = 20-minute re-listen for one answer; local-only, no circle; no clinical distribution; ~1K downloads in 5 years | **Yes, on value**: LLM summary+search fixes the replay problem. No, on distribution |
| **OWise** (NL/UK, 13 years) | Recording is the beloved feature (100% used) | Sterilized the loved feature (no export, no share) and monetized the abandoned one (diary, half quit); null RCT because ~20% real-world adherence; ~$340K lifetime funding | Partially: AI could fuse recording and data. Capital/distribution untouched |
| **Untire** (NL, RCT-proven, VGZ-reimbursed) | Clinical proof gets you reimbursement | Bought every user (€22 per trial enrollee via Facebook ads); solo homework for exhausted patients, 58% gone by week 12; patient won't pay "Netflix rates" | No. Distribution and payer problems |
| **War On Cancer / CancerAid** | Cancer communities form fast | Consumer willingness-to-pay near zero; episodic acute-phase usage; founder burnout; CancerAid survived only by pivoting to employer-paid B2B | No. Economic |
| **CaringBridge** (the survivor, 1997–) | The share-broadcast loop is real and durable | Survived BECAUSE nonprofit: episodic usage (sites live ~425 days, ~1/3 of cancer sites end in death) is tolerable on donations; zero-CAC crisis-moment distribution via hospitals and word of mouth | n/a: the lesson is the model, not the tech |
| **Caren by Nedap** (NL, ~740K "active users") | ECD-bundled distribution reaches every family | Pipes raw professional reports without interpretation; family is a passive read-audience checking ~2x/week; paper-letter onboarding; the count is a registration artifact | No. It proves distribution without interpretation also stalls |
| **Outcomes4Me** (US, $38M, alive) | Pharma-data model funds a free patient app | Engagement never required by the business model: median 3 interactions in 12 weeks, NPS -37; solo patient, no second actor, episodic navigation job | Mostly no. The incentive, not the capability |
| **Alexa health / Alexa Together** (big tech) | Voice in millions of homes is not enough | Reactive skills nobody remembers to summon; no payer; strategically orphaned at the first cost squeeze. ElliQ won the same job by being proactive (30 interactions/day) and institution-funded | **Partially**: LLMs fix grounding and enable proactivity; payer and accountability untouched |

**The four killers (my read, pattern across all ten):**
1. **No recurring reason to return.** Episodic demand treated as a daily product. The fix is not forcing a habit; it is owning every episode and being proactive between them.
2. **Effort here, payoff there.** The user does the work, someone else (study, clinician, pharma) gets the value. The payoff must land in the same session, for the patient and the circle.
3. **Patient as payer.** Never worked once, in any geography. Survivors switched payer.
4. **Capture without interpretation or sharing.** Gesprekshulp stored raw audio locally. OWise locked the recording. Caren pipes raw reports. The value is in summarize + share + interpret; capture alone is a feature.

AI materially fixes only #4 and half of #1 (proactivity). #2 is a design choice. #3 is strategy.

---

## 3. The retention base rates any core action must beat (verified)

| Setting | Number | Caveat |
|---|---|---|
| Health/lifestyle apps generally | ~70% of users gone within 100 days (median) | Kidman, JMIR 2024; lifestyle+mental-health apps, no NL data |
| Floodlight MS, real world | 9.7% day-30 retention without reminders; 30.8% with | Reminders alone tripled retention |
| ePRO inside a trial (PRO-TECT, US) | 91.5% weekly completion over a year | Propped by 24h reminders, staff phone calls at 72h (13.9% of completions), and 15% caregiver/staff proxy entry; 42.7% left follow-up by month 12 |
| ePRO in routine care (Texas Oncology) | 72% → 52% in ~10 weeks | And this was inside a subsidized CMS program |
| eRAPID (UK) | 72% week 1 → 58% week 18 | Adherence held only when patients saw a clinician actually read it: "somebody's looking at it" |
| Charité (DE) routine breast cancer | Rises to 75–80% over 12 months | The inversion case: sicker, chemo-treated patients adhere BETTER; healthier and younger drop out |
| Scan-anchored tracking (survivors) | 83% completion, 3x/day for 11 days around a scan | Time-boxed windows beat open-ended habits (~50%) |
| Outcomes4Me (consumer, FIONA) | Median 3 interactions in 12 weeks; NPS -37 | Against a 4.3-star store rating. Store ratings are noise |
| Voice, proactive & institutional | Hippocratic: 89% connect rate, 115M+ interactions; Tucuvi (EU): >90% engagement in complex populations | Outbound calls, B2B-paid. Direction matters |
| Passive vs active capture (chemo) | 73% passive smartphone vs 61% active surveys | Passive sustains; asking decays |

**My read:** three levers reliably move retention: (1) someone visibly responds to what the patient submits, (2) reminders/proactive outreach, (3) time-boxed event windows instead of open-ended habits. All three are design choices we control. Also: sicker patients adhere better, which means retention concentrates in our beachhead segment, but it inverts the assumption that healthy young circle members are the easy growth vector.

---

## 4. What AI newly enables, and what it doesn't

**Direction inversion (strongest evidence).** User-initiated logging decays everywhere; app-initiated contact sustains. ElliQ: proactive, ~30 interactions/day, ~7 months average use (vendor-co-authored study, US). Hippocratic: patients answer AI calls and stay on the line 9.5 minutes; refusal to talk to an AI dropped to 2.7%. The a16z "why now" is a cost curve: ~$0.10/hour for AI contact versus $50+/hour human. Caveat: heavy companion use correlates with worse loneliness; proactivity must serve the care plan, not engagement metrics.

**Input collapse.** Photo: pre-AI photo logging failed (The Eatery: 69% quit after 0–1 photos), AI recognition broke the ceiling (Cal AI: 15M+ downloads and $30M+ revenue per its acquirer MyFitnessPal, though founder-claimed retention and near-break-even ad spend warrant skepticism). Voice: audio-only check-ins hit 94% over 14 days with young cancer survivors ("easy... particularly with it being just audio"); oldest users engage MOST with voice (84% vs 43% youngest, heart-failure app). For chemo brain and caregiver full-hands, eyes-free input is the unlock. Photographing medical letters is already mass behavior via ChatGPT.

**Grounded interpretation with memory.** The new capability is not Q&A (commoditized) but Q&A grounded in YOUR consultations and record. Generic AI fails precisely on missing patient context (lowest score: comprehensiveness 63%; re-suggests tried strategies 22%). The accumulating consult archive is the moat that makes our answers better than ChatGPT's, and it compounds per appointment. Caregivers already use ChatGPT/Gemini at 9:30pm for exactly our jobs (decode jargon, summarize multi-doctor notes); we win only by knowing the patient.

**What AI does not fix:** distribution (Gesprekshulp died next to the validated premise), the payer, episodic demand, and trust/accountability. And positioning kills: products positioned as AI doctor/therapist died on regulation (Babylon $4.2B bankrupt; Woebot retired despite 1.5M users; Yara shut citing crisis-moment danger). Companion/translation/memory positioning survives. MDR line: stay on the interpretation-of-your-own-conversation side, never triage.

**Commoditization threat (12–24 months):** ChatGPT Health (~230M weekly health questions, 48% used it to understand medical terms), Microsoft Copilot Health, Oracle's in-portal grounded Q&A, Apple iOS 27 camera intelligence. Generic "explain this letter" will be free and built-in. What they won't have: the recorded consult, the longitudinal NL oncology context, the family circle, and the hospital relationship.

---

## 5. The competitor swarm (verified, all launched/funded within 13 months)

| Who | Launched | Core action overlap | Model | Gap they leave |
|---|---|---|---|---|
| **Aide Health "Mirror"** (UK) | Oct 2025 | Record consult + plain-English summary + grounded Q&A + family sharing. "UK's first AI scribe for patients, not clinicians" | £9.99/year consumer; NIHR/Innovate UK backed | Chronic-disease focus (founder's father has Alzheimer's), no oncology, UK only, deletes audio immediately |
| **Neatly Health** (US) | Jan 2026 | Record, translate, track across visits, prep questions | Free; anonymized-data monetization | **Targeting oncology explicitly** (ovarian/endometrial study with major CA provider, UCSF conversations). US only |
| **Kin Health** (US) | May 2026 | Record visit, AI summary + action items, share with family, prep questions | Free forever; referral monetization; **$9M seed, Maveron + GoodRx founders** | No condition focus, US only, best-capitalized and most pedigreed |
| **Hedy AI** (US, mature) | scaling 2025 | Real-time jargon translation in 30+ languages during the visit, summaries, Q&A, family sharing | Freemium $12.99/mo; **EU data residency offered for oncology** | No EU base, no clinical distribution |
| **Medcorder** (US, incumbent) | older | Record + transcribe + share with family group chats; markets to cancer | Free-ish, pre-AI-summary generation | Stagnant; proves the demand vocabulary ("Remember every word your doctor says") |
| **Big tech** | 2026 | Generic explain/Q&A on records and letters | Free, bundled | No recording of the consult, no circle, no oncology pathway, no NL |

EU/NL check: no patient-side consult-recording + AI-summary competitor headquartered or launched in the EU was found besides Ditto. EU activity is clinician-side scribes (Tandem $50M, Autoscriber). The patient-side + EU/NL + family-circle position is currently ours alone, with three funded US teams one decision away from Europe.

---

## 6. NL legal ground truth (KNMG, verified)

- A patient may record their own consultation for private use **without the doctor's consent**; informing the doctor is courtesy, not law (KNMG Handreiking, 2017). Covert audio is not a criminal offense (art. 139a Sr). A doctor **cannot refuse**; hospital house-rule bans are **invalid** per KNMG.
- The KNMG itself recommends our exact pattern: the doctor gives an end-of-consult summary that the patient records; some institutions already store consult recordings in the patient portal.
- The legal line is **openbaarmaking** (public disclosure), which needs the doctor's consent. Sharing within the private family circle is private use. Case law (Hoge Raad, Hyves) treats ~20+ people as "public": a design constraint, not a blocker. Circle sharing should stay closed, capped, and never link-public.
- AI cloud processing of the recording = GDPR Art. 9 special-category data, requiring patient consent. When the patient initiates and chooses the app, the patient acts in personal capacity; the vendor's exact status is legally untested. KNMG's April 2026 AI guidance covers the doctor-initiated scenario (don't store externally, destroy after transcript), a different controller posture than ours.
- **Germany is the opposite**: covert recording is criminal (§201 StGB, up to 3 years); bilateral consent required. Any DACH expansion needs a consent-first flow. Belgium sits in between.

---

## 7. What this means for the core action (my read, feeds source 10 v2)

**Restate the bar.** Not "make Ditto daily" and not "accept episodic." The bar is: **own every episode completely, and run the daily surface as an AI-led experiment in received value.** Episodes (appointments, scans, cycles) are the proven anchor and arrive roughly weekly during active treatment. Between them, the evidence forbids assigning daily *work* (forms, manual logs — fails for everyone, including the well-funded) but supports daily *value*: proactive voice check-ins with synthesis back, grounded Q&A on your own case, automatic symptom capture from natural speech. None of this has long-horizon retention proof yet, which is exactly why it is our wizard-of-oz question, not a settled design.

**The loop the evidence supports:**
1. **Capture without effort** at the episode (record the consult, photograph the letter): the beloved, legally frictionless, KNMG-endorsed action.
2. **Interpretation as the instant payoff, same session**: plain-language summary, grounded answers. This is what Gesprekshulp, OWise, and Caren all withheld, and it is the step AI just made possible.
3. **Share to the circle in one tap**, author-controlled (including non-broadcast mode): kills the "who did I tell what" job; the circle's reactions and questions create the inbound pull no solo product has.
4. **Proactive between episodes**: pre-appointment prep nudge, pre-scan window check-ins (the 83%-completion pattern), "your family asked about X." App-initiated, time-boxed, clinically grounded.
5. **The archive compounds**: every consult makes the next answer better, which is the defense against ChatGPT and the data moat for B2B.

**Eigenquestion implications:**
- **Q1 (core actions):** the episode loop above, not a standalone daily check-in. Symptom/med logging is the most-abandoned feature in every product autopsied; if we want between-visit data, derive it passively (from conversations, photos, later wearables), don't assign homework.
- **Q2 (problems):** comprehension at the episode + the update burden + grounded "what does this mean for me" between episodes. These three are validated, high-intensity, and badly served.
- **Q3 (primary user):** patient-primary with the partner as built-in second user in oncology (sicker patients adhere best; caregivers matched patients 84% vs 86% in dyad completion and acted within 48 hours). Caregiver-primary in neuro. The spokesperson pattern suggests the real unit of adoption may be the circle-with-a-designated-author; test in interviews.
- **Monetization:** the patient does not pay. B2B (hospital/insurer) fits the evidence and the existing GTM; Untire (VGZ) and SkinVision (CZ, NN) prove the NL reimbursement route. Hospital-embedded distribution is also the proven adoption lever in NL (MediMapp 77% uptake; physician recommendation is the strongest retention lever found).
- **Metrics:** instrument per-episode ownership (recorded consults per patient, summary re-opens, shares, inbound circle responses, pre-scan re-engagement), and weekly-active during active treatment. A raw DAU target would recreate the mistake every dead product made.

**Speed matters now.** Three funded US teams and one UK team converged on this action within 8 months, one explicitly in oncology. None is in the EU. The 20-interview program and the wizard-of-oz cohort should test the episode loop and the circle dynamics, not whether recording is wanted (that is now proven several times over).

---

## 8. What we still don't know

| Unknown | Why it matters | Cheapest resolution |
|---|---|---|
| Ditto's own retention curves by care path and circle size | The single highest-fidelity evidence, never pulled in this campaign | Step-0 Mixpanel/Porygon pull (internal) |
| Does a summary archive get re-opened before scans/appointments? | The re-engagement mechanic of an episodic product | Own data + interviews |
| Spokesperson vs patient as the account author | Changes onboarding, permissions, growth model | Interviews (ask who holds the phone in the room) |
| The deliberate non-broadcast segment size | Caps the circle thesis | Interviews |
| NL magnitude of the want-to-record gap | German survey may not transfer | Interview screener question |
| Vendor-status under GDPR for patient-initiated AI processing | Legally untested; our controller posture | Legal memo (with Łukasz) |

---

## Verification appendix

15 claims, 45 adversarial votes (3 per claim, lenses: primary source, methodology, independent replication). 0 killed, 13 confirmed-with-correction, 2 confirmed. Material corrections:

| # | Claim | Status | Key correction |
|---|---|---|---|
| 1 | German recording survey (67%/5%/27% covert) | Corrected | Confirmed (Topf, Scholl & Hahlweg, Front. Psychol. 2024, n=287); plus 25.4% answered "maybe" (~92% positive) |
| 2 | 72% listen back, "73% with family" | Corrected | 53.6–100% listen (Tsulukidze 2014 scoping review, 33 studies); sharing: **in 60% of studies patients shared the recording**, not 73% of patients |
| 3 | Belong.Life 70% 1-year retention | Corrected/1 refute | Single unattributed CTO quote, 2020, no methodology. Treat as marketing, do not cite |
| 4 | Gesprekshulp zombie (~1K downloads) | Corrected | Confirmed; no Android update since Apr 2023, iOS since 2020 |
| 5 | OWise recording most-used/most-praised | Corrected | Confirmed: 100% used, 93% useful, n=15, UMC Utrecht 2013–14. Small sample, single site |
| 6 | PRO-TECT 91.5% | Corrected | Confirmed but: active retrieval protocol, 13.9% needed phone calls, ~15% proxy-completed, 42.7% out of follow-up by month 12 |
| 7 | Texas Oncology 72→52% | Corrected | Confirmed (Patt, JCO CCI 2021, n=4,375); ran inside subsidized CMS OCM program, so real-world unsubsidized is likely worse |
| 8 | FIONA median 3 uses, NPS -37 | Confirmed | Vendor-affiliated authors; figures are if anything flattering |
| 9 | 70% quit health apps in 100 days | Corrected | Kidman JMIR Dec 2024; lifestyle/mental-health apps, wide variance, no NL data |
| 10 | Floodlight ~10% day-30 | Corrected | Confirmed (9.7% vs 30.8% with reminders); non-randomized sub-analysis, US cohort |
| 11 | Cal AI numbers | Corrected | 15M+/$30M+ per MyFitnessPal acquisition statement (Mar 2026); retention founder-claimed; ad spend ~$770K/mo, near-break-even; Apple briefly pulled it for deceptive billing |
| 12 | ElliQ ~7 months use | Corrected | Vendor-co-authored study (n=173, 62% response); "30 interactions/day" is from the NY State deployment only |
| 13 | Mirror + Neatly exist as described | Confirmed | Plus Kin Health ($9M, May 2026) and Hedy found in the same sweep |
| 14 | US patients read results before clinicians | Corrected | Confirmed for US (75% of results in 2022, up from 37% in 2017). NL equivalent: portals release results fast and 70% of NL patients WANT immediate release (NFK n=5,672) |
| 15 | Untire numbers | Corrected | ~30,000 cumulative DOWNLOADS (not users); RCT n=799, 58% attrition by week 12; benefit concentrated in high users |

Campaign stats: 3 workflows (13+1, 59, agents), 73 agents total, ~3.6M tokens, 1,482 tool calls, ~23 minutes of wall-clock research. Known gap: Reddit was crawler-blocked; its voice was recovered indirectly and remains thinner than forum evidence. Peer-reviewed Reddit analyses confirm the public register there is emotional, not logistical, so tool behavior is better evidenced from forums and studies anyway.
