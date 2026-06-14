# Source Synthesis 10 — Rethinking the Core Action: From Appointment Summary to a Weekly-or-Better Companion

> Synthesizes Merlijn's candidate list of frequent-use jobs (board input + 2026-06-04 reflection) against the evidence we already hold: [`research/healthcare-life-changing-moments/`](../../../research/healthcare-life-changing-moments/README.md) (esp. [08b daily JTBD](../../../research/healthcare-life-changing-moments/findings/08b-daily-life-high-frequency-jtbd.md), [09 pain map](../../../research/healthcare-life-changing-moments/synthesis/09-cross-journey-pain-map.md), [13 final synthesis](../../../research/healthcare-life-changing-moments/synthesis/13-synthesis-final.md), the [cancer](../../../research/healthcare-life-changing-moments/findings/02-journey-cancer.md) and [neuro](../../../research/healthcare-life-changing-moments/findings/03-journey-neurodegenerative.md) journeys), the ZeroClaw/care-brain JTBD corpus, [08 Lenny panel](./08-lenny-guest-perspectives.md), and [09 playbooks & human needs](./09-aspirational-playbooks-and-human-needs.md). Focus: oncology, neurodegenerative, and other seriously ill patients **and their surroundings**. Built by Mewtwo, 2026-06-04.

## Bottom line

**Ditto's core functionality must be rethought. The appointment summary is the wedge and the trust artifact, not the product.** The external research reached this independently: the summary is a single-player utility with a rare, external trigger; it cannot build a habit, a data moat, or a network. The flip is to change the unit **from appointment to day/week** and **from patient to patient-and-circle**, with the summary repositioned as the periodic crystallization of a frequent, multi-player relationship.

The bar any new core action must clear (assembled from sources 08, 09, and the research):

1. **Fires daily-to-weekly from an internal trigger** (a felt need, not a calendar event we don't control)
2. **Resolves a real struggling moment** (Moesta), not a feature we like
3. **Clears Delta-4 versus the real alternative** (Shah): the notebook, the pill alarm, WhatsApp, Dr. Google, calling your daughter
4. **Compounds**: builds either a personal-data moat or a network, preferably both
5. **Stays non-device** (outside MDR) until we deliberately decide otherwise — no triage verdicts, "watch-for" framing only

And the decision discipline: **this is not decidable by debate.** The hard requirement is 20 × 1-hour interviews with cancer patients (plus caregivers), with our own usage data pulled first. Plan in §6.

---

## 1 · Merlijn's candidate list, mapped to the evidence

Every item from the board/reflection list, mapped to the evidenced daily JTBD (frequency and evidence from the external research; rank = its position in the research's frequency × reach × hook ranking).

| Candidate (Merlijn's list) | Evidenced JTBD (rank) | Frequency | Evidence anchor | Today's hacky alternative | Compounds via |
|---|---|---|---|---|---|
| Updating loved ones day-to-day; sharing; receiving/asking help; thoughtful pre-appointment messages | **Update + coordinate help** (#1) | Daily–weekly | Caregivers "exhausted responding to everyone," forget "who they told what"; ~73% of CaringBridge sites are caregiver broadcasts | WhatsApp group that can't tell "I'm OK" from "I need a meal Tuesday" | **Network** (the only inherently multi-player job) |
| Symptom tracking; daily logging; personal journaling | **Symptom tracking & interpretation** (#2) | Daily, multi×/day | ~25 distinct symptoms over a chemo course; MS fatigue >80%; clinicians miss between-visit symptoms up to half the time; ePRO monitoring carried a survival signal (+5.2 months median, US-flagged) | Paper notebook, Notes app, or nothing | **Personal-data moat** + clinical reward |
| Medication adherence; reminders | **Meds: "did I take it?" / timing** (#3) | Every dose (3–10+/day) | ~50% non-adherence; ~€125bn + ~200k deaths/yr EU; Parkinson's "off" periods from timing errors; ~95% of carers manage meds in moderate-severe dementia | Dosette box, phone alarm, the partner who reminds | Adherence history; crowded by pill apps — our edge is the regimen extracted from the recorded visit |
| Medication purchasing | *(not researched yet)* | Weekly–monthly | No evidence in corpus; plausible convenience adjacency (NL pharmacy refill rails) and the board's pharmacy/B2B angle | Pharmacy app / paper repeat scripts | Unproven — flag as research gap, not a bet |
| Chat queries; context-aware question asking | **"What does this mean for *me*?"** (#4) | Daily post-diagnosis | 77% of NL adults search health info online; Dr. Google improves accuracy modestly but not anxiety; ZeroClaw jobs 8–11 rated native-fit | Google, forums, generic ChatGPT, 2am scrolling | Q&A history tied to the record; this is the board's sixth route (trusted answers) |
| Reasonable literature research | Extension of #4 | Weekly | Same failure modes: keyword-ranked, not grounded in your case | Same | Same; mind the interpretation/MDR line |
| Podcast-level / infographic explainers of disease mechanics & treatment | **Comprehension (Cluster A), new modality** | Episodic→weekly | 40–80% of consult info forgotten; 47.6% of EU adults limited health literacy; "explain to my child" is a native-fit ZeroClaw job | Leaflets, YouTube | Differentiating content surface; feeds trust, not frequency by itself |
| How am I feeling today (mood) | **Emotional daily load** (#5) | Daily | ~1 in 4 cancer patients clinically depressed; caregiver anxiety/depression 28–94% | Bottling it up; journaling apps | Mood timeline; best as a layer inside the check-in, not standalone |
| Managing day-to-day care tasks | **Practical logistics** (#7) | Weekly clusters | Transport a burden for almost every participant (74% of cancer caregivers, US-flagged); patient = unpaid project manager | Shared calendar + WhatsApp + the one organized relative | Best as the "help dispatch" feature of the circle, not its own product |
| Not being fully dependent on appointments | — | — | This is the frame itself, not a feature: the appointment is an external trigger we don't control | — | — |

Two items on the list are **genuinely new** relative to the corpus: medication *purchasing* and podcast/infographic *explainers*. Neither has evidence yet; the second is cheap to prototype, the first drags in pharmacy logistics and should wait for the interviews.

## 2 · What oncology and neuro add specifically

| | Oncology | Neurodegenerative |
|---|---|---|
| **Who does the daily work** | Patient, with caregiver support (side-effect self-management offloaded home; caregivers' top unmet needs: managing side effects at home ~78%, chemo risks/benefits ~79%) | **The caregiver IS the user**: ~95% manage meds in moderate-severe dementia; proxy/portal access silently broken; 8–12 year journey |
| **The daily rhythm** | On-treatment is weekly-to-daily: ~25 symptoms over a course, "is this normal or do I call?" after every infusion | Clock-driven med timing (Parkinson's "off" periods); BPSD nobody prepared the family for; anticipatory grief as a years-long state |
| **The episodic cliff** | Diagnostic limbo and the survivorship "now what?" cliff (fear of recurrence) | Pre-diagnosis "is it just aging?" limbo (~3.5 years to dementia diagnosis); placement guilt; end-of-life proxy decisions |
| **Implication for the loop** | Patient-led mode, circle supports | Caregiver-led mode, patient is the subject |

Same loop, two modes. This is the board's "Care OS with patient and caregiver modes" grounded in evidence, and it makes **fork 2 (caregiver vs patient) empirically testable rather than philosophical**: run both modes in the research and watch who actually does the work.

## 3 · The convergence: one loop, not a feature list

The research's five universal clusters are one daily cycle, and Merlijn's candidate list snaps onto it almost perfectly:

```
  20-second CHECK-IN  ──────►  GROUNDED INTERPRETATION ────►  TELL-ONCE UPDATE  ────►  HELP DISPATCH
  symptoms · mood · meds      "is this normal for ME?         auto-drafted for the      "what can I do?" becomes
  (daily logging,              what did my team say            circle; thoughtful        meals, lifts, tasks
   journaling, adherence)      to watch for?" (non-device)     pre-appointment notes     (care tasks)
        │                            ▲                              │
        │                            │ ASK-ANYTHING surface         │ circle reads, reacts,
        ▼                            │ (context-aware Q&A,          ▼ contributes
  ACCUMULATING RECORD ◄──────────────┘  explainers, literature)   NETWORK grows
        │
        ▼
  THE APPOINTMENT SUMMARY — now the periodic crystallization of a month of real data,
  shareable to the circle in one tap. The wedge and the trust artifact. Not the product.
```

**Three candidate core actions fall out, and only three:**

| Candidate core action | Compounding mechanic | Strongest evidence | Biggest doubt |
|---|---|---|---|
| **A · The 20-second check-in** (symptom/mood/med confirm, adaptive cadence, caregiver can carry it) | Personal-data moat + clinical reward | Self-monitoring = strongest retention lever in the corpus (~80% vs ~60% at 40 wks); survival signal | "I want to forget I'm sick" — daily may be fantasy |
| **B · The tell-once update** (auto-drafted from check-ins; pre-appointment notes to loved ones) | Network (social variable reward: replies, hearts, offers of help) | Existing behavior proves demand (WhatsApp broadcasts, CaringBridge); only multi-player job | CaringBridge existed for 20 years and stayed niche |
| **C · Grounded ask-anything** (context-aware Q&A + explainers on YOUR record) | Q&A history tied to record; trust engine | 77% NL already search; labs can't ground in your record + circle | Highest lab-overlap; ChatGPT's busiest room |

**My read: A and B are one fused loop, not two products.** The check-in IS the raw material of the update; the update IS the social reward for checking in. C is the surface across it. That fused loop is the concrete content of the A+C route hybrid and the board's Care OS. But this read is exactly what §6 must test, not assume.

## 4 · What would make this wrong (held honestly)

From the research's own red team and the Lenny panel's opposing synthesis:

1. **Daily engagement from the sick is a wounded hypothesis.** Fatigue, depression, and "I don't want to be reminded I'm sick" fight a daily habit; peak need is when people least open apps. The interviews must be allowed to return: *weekly is the ceiling, daily is fantasy.* The loop survives at weekly cadence; the pitch deck version doesn't.
2. **The circle may be a feature, not a company.** CaringBridge and WhatsApp already exist and never became category-defining. Our own K≈0.012 says receiver audience, not network, today.
3. **Monetization is unresolved** (the research's biggest-risk verdict): charging the seriously ill is fraught, loved-one-as-payer is unproven, DiGA needs the device status we're avoiding.
4. **The non-device version may be a vitamin.** The most valuable job ("should I call?") is the regulated one. The "what did my team say to watch for" framing is the legal edge we walk.
5. **The episodic counter-read.** Maybe Ditto should own the unavoidable event brilliantly (TurboTax) instead of chasing frequency at all. If interviews show the hacks are tolerable and the moments are what matter, that is a legitimate answer.

## 5 · Implications for the routes and forks

- **Fork 1 (the spine)** becomes concrete: which core action (A, B, fused A+B, or C) is the spine. Decided by §6, not debate.
- **Fork 2 (caregiver vs patient)**: oncology = patient-led with circle support; neuro = caregiver-led. Both modes go into the research design.
- **Fork 5 (frequency)** gets its honest answer: frequency comes from the illness's own daily rhythm (symptoms, meds, worry, updates), not from manufactured streaks. If that rhythm doesn't carry the product, no gamification will.
- **North Star refinement**: the internal truth metric becomes Tavel's engaged user, e.g. *% of newly diagnosed oncology patients completing ≥4 check-ins/week in week 4*. The board's "50% within a week of diagnosis" is the adoption-depth complement.
- **Wearables (board input)** slots into candidate A as a passive input later (the Oura lesson: data needs a meaning ritual), behind the MDR flag. Not v1.

## 6 · The validation plan (evidence-gated; the hard requirement)

**Step 0 — this week, near-free: our own data.** Pull Mixpanel/Porygon: actual summary-use frequency, retention curve by cohort, and what users already ask Ditto. The external research explicitly flags this as the highest-ROI unmade move. Quantifies the frequency problem we keep describing anecdotally.

**Step 1 — THE HARD REQUIREMENT: 20 × 1-hour interviews, cancer patients.**
- **Who:** 20 oncology patients in NL (≤6 months from diagnosis or on active treatment; recruit via partner hospitals, AYA, in-app Survicate, circle members), **plus** 8–10 caregivers, of which 3–4 neuro caregivers (the fork-2 contrast group).
- **Method:** Moesta switch/forces interviews + day reconstruction: *walk me through yesterday* — symptoms noticed, meds taken/missed, what you googled, who you told what, what you wrote down and where, what help you asked for or didn't. The hacks ARE the demand signal.
- **Close of each interview:** Delta-4 score (understanding your care via Ditto vs your current way, 1–10 both), a willingness-to-pay probe (Ramanujam: pain → value → would you pay, who should pay), and forced ranking of three concept cards (check-in / tell-once update / ask-anything).
- **Pace:** start recruiting this week; ~2 interviews/day gets 10 done before the mid-June Q3 exercise (directional input) and all 20 + synthesis by end of June (decision-grade).
- **Output:** a validated needs map that picks THE core action, with verbatims. This gates the route decision.

**Step 2 — in parallel: the concierge experiment + two spikes.**
- **Wizard-of-oz cohort** (per the research design): ~30 newly diagnosed patients + caregivers running a manual daily check-in + manual circle updates. Primary metrics: D30 check-in retention (target ≥40% checking in ≥4 days/wk), circle size seeded per patient, and whether any invited loved one starts their own circle.
- **Monetization spike:** price-probe patient-pay vs loved-one-as-payer vs insurer B2B2C.
- **Regulatory spike:** formal read that the non-device "watch-for" check-in stays outside MDR; same review covers the wearables/Open Wearables angle the board raised.

**Gate (from the research, kept verbatim in spirit):** do not scale until engagement, a credible payer, and the non-device design are all validated. And the question to hold above every roadmap call:

> *Are we building a companion that happens to make summaries — or a summary tool pretending to be frequent?*

## Source map

- [`research/healthcare-life-changing-moments/`](../../../research/healthcare-life-changing-moments/README.md) — external evidence base (08b daily JTBD, 09 pain map, 02/03 journeys, 12 red team, 13 final synthesis)
- [`08-lenny-guest-perspectives.md`](./08-lenny-guest-perspectives.md) — the decision frameworks applied here (core action, Delta-4, WTP, kill criteria)
- [`09-aspirational-playbooks-and-human-needs.md`](./09-aspirational-playbooks-and-human-needs.md) — functional door / emotional moat / frequency hinge; the needs hypotheses the interviews test
- [`board-meeting-input-2026-06-03.md`](../board-meeting-input-2026-06-03.md) — the candidate list and the trusted-vision reframe
- `specs/ideas/health-agent/zeroclaw-jtbd-discovery.md` + `specs/care-brain/care-brain-master-synthesis.md` — the internal 37/45-JTBD corpus (capability fit per job)
