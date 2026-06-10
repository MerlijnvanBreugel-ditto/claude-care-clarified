# C1 — The Intelligence Layer (the ladder: understanding → advising → agency)

> Market Deep Dive · Part II synthesis · Direction C1. Written 2026-06-09 by Mewtwo.
> Draws on F1 (ePRO/tracking), F2 (journaling/narrative), F6 (proactive assistants). The shared monetization framing (money is B2B, the conversation is the till) is argued in Part III; referenced here, not re-litigated. The personal health record is the multiplier that feeds this layer (see C2); referenced, not covered.

This is Ditto's contrarian core: the part big tech and EHRs are worst at, and the part patients trust us for. The ladder is understanding → advising → agency. It is real. The top of it is not free.

## 1. The ladder, rung by rung

| Rung | What it does | (a) Who's already there | (b) Proven frequency engine | (c) Monetization that actually works | (d) Regulatory class |
|---|---|---|---|---|---|
| **0 — Understanding** | Explains what the doctor meant; summarises; reformats info the user already has | Ditto today; plain-language explainers | **Episodic, appointment-gated.** No standalone retention; a reason to open weekly at most | None standalone (the conversation is the till; this rung is the hook) | **Not a device** if it doesn't interpret the individual's data to recommend. AI-Act Art. 50 chatbot disclosure only. Free zone |
| **1 — Advising (generic)** | Generic education, "questions to ask," non-individualised lifestyle nudges | Lark wellness track, Thrive coaching, generic content layers | **Weak alone.** Episodic symptom-checking does not retain (Ada). Generic nudges decay 30–60 days | Thin standalone; rides on a paid base | **Wellness exemption** if no diagnostic/treatment claim. Claim wording is the whole game. Limited-risk |
| **2 — Advising (individualised)** | Interprets *this person's* data to recommend re: their diagnosis / monitoring / treatment | Ada (symptom assessment), Hello Heart (BP guidance), CANKADO (auto recommendations) | **The proven set lives here, but bought, not earned:** human/human-supervised coach in the loop (Omada, Jasper), or connected device as the daily ritual (Hello Heart, mySugr). Tracking + navigator during the active-treatment window | **B2B that survives:** payer/insurer-reimbursed (DiGA), pharma-sponsored programs (Sidekick/Pfizer), reimbursement-code navigation (Jasper/CMS, immature in EU) | **MDR Class IIa** (Rule 11 / MDCG 2019-11) — notified body, ISO 13485, clinical evaluation. **AI-Act high-risk** by the device route |
| **3 — Agency** | *Acts*: titrates, triggers clinical decisions, autonomous recommendation | Insulin-dosing DTx; Woebot (dead, $124M burned chasing FDA) | n/a — nobody has retained-and-monetized a consumer-facing autonomous clinical agent | Trial-grade evidence required before any revenue | **Class IIa–III, full high-risk** conformity + post-market surveillance. The Woebot trap |

The mechanic that pays at Rung 2 is never "the AI." Across F1/F6 it is a human or human-supervised loop, or a device whose measurement *is* the habit. Tracking and journaling (below) are frequency engines that feed this ladder; neither retains or monetizes standalone.

## 2. The key insight: the money-rung is the device-line, and survivors route around it

The rung that unlocks B2B money (Rung 2: interpreting an individual's data) is the exact rung that crosses the MDR device line. MDCG 2019-11 is explicit: software giving "recommendations for diagnosis, prognosis, monitoring and treatment of individual patients" is a medical device. Cross it and you owe a Class IIa conformity assessment and AI-Act high-risk obligations: QMS, clinical evaluation, notified-body audit, post-market surveillance. That is a funded, deliberate commitment, not a feature.

The field's survivors do not beat the line. They **route around it with a human or the care circle in the loop**, so the *person* makes the individualised clinical call and the AI *supports* it:

| Survivor | How they keep the value, dodge the device bill |
|---|---|
| **Wysa** (alive) vs **Woebot** (dead) | Same AI capability. Wysa sits *beside* the therapist (support between sessions, near the wellness line) and thrives B2B; Woebot tried to *be* the therapist, hit high-risk, burned $124M |
| **K Health, Counsel** | AI does intake; a licensed clinician closes the loop inside a trusted provider brand |
| **Jasper** | Human oncology navigator owns the clinical step; "AskJasper" AI is additive, not the spine |
| **Basch/Kaiku ePRO** | The benefit (QoL, fewer ER visits) is the *response*, not the capture: report → severity grade → a clinician acts |

**What it means for how far Ditto climbs device-free:** Ditto can own Rung 0 and climb to Rung 1 (generic advising) with disciplined claim language and an AI-disclosure notice — cheap, CE-exempt. To deliver Rung-2 *value* without paying the Rung-2 *bill*, the individualised clinical recommendation must be made by a human (an oncology nurse/navigator touchpoint) or routed through the care circle / the patient's own clinician, with Ditto's AI doing understanding and generic advising up to the edge. This is also the structure that makes pharma- and payer-money reachable. The cliff at Rung 2-as-a-device is only crossed when it's a financed strategic decision.

## 3. White space for Ditto

The intelligence-layer moves that (a) add between-appointment frequency, (b) stay safe-side of the line, (c) compound on the understood-conversation asset.

| Move | (a) Frequency it adds | (b) Stays safe-side because | (c) Compounds on the conversation because |
|---|---|---|---|
| **The narrative thread: a string of summaries the circle reacts to** (F2's CaringBridge guestbook mechanic) | Event-driven, socially enforced — the medical journey pulls updates out of the author; oncology cadence can be weekly. Frequency Ditto doesn't have to manufacture with streaks | Pure narrative + audience; no individual-data interpretation, no clinical claim | The summary *is* the natural "post"; the care circle *is* the natural guestbook. Ditto already produces the post |
| **"The journey remembers itself": AI memory across appointments** (F2 Rosebud, reframed for illness) | Re-entry loop — "here's what changed since last scan, here's the question to ask next time"; the bridge from understanding into advising | Reflecting *the user's own past entries/summaries* back is memory + generic advising, not individualised diagnosis. Watch the claim line | The summaries are the memory substrate. This is the one genuinely defensible journaling asset, and Ditto is uniquely positioned to own it |
| **Tracking as the treatment-window engine, routed into a responder** (F1 ePRO) | Weekly/daily contact during active treatment — the high-intensity window where cadence is naturally high | Capture + generic triage stays below the line; the *responder* is the care circle or the patient's existing clinician, never a Ditto-employed nurse making the call | The longitudinal symptom record makes summaries and advice sharper; feeds the operational front door ("book a call," "flag at next appointment") |

Tracking (F1) and narrative/journaling (F2) are **frequency engines feeding the ladder, not standalone bets.** Both are treatment-window-gated or event-driven; neither monetizes on patient payment (Bearable caps small; CaringBridge can't charge users; trackers get acqui-hired for their data, not their app). They earn their place only if they raise Core MAU and circle attachment inside an already-paid product and route into a layer that monetizes.

The sharpest single move: **the narrative thread.** It is the highest-leverage idea in F2, it converts an asset Ditto already produces (the summary) into the recurring "post," it rides the medical journey's own cadence, it pulls the care circle in (the v2 mission), and it stays well below the device line.

## 4. Verdict against the 4 core questions

| Question | Plain read on the intelligence layer |
|---|---|
| **What** | Climb the ladder from understanding to advising. Own Rung 0–1 outright (free, CE-light). Reach Rung-2 *value* via a human/care-circle in the loop, not via becoming a device, until a deliberate funded decision. Rung 3 (agency) is off the table near-term — the Woebot trap |
| **Who** | The severely-ill patient (oncology first) and their care circle. The circle is the frequency engine that makes the layer sticky; whether the circle is a *payer* or only a *multiplier* depends on B2B buyer willingness, unresolved by the market alone |
| **Moat** | Not the AI (anyone wraps a frontier model). The defensible assets are: the **trusted, understood conversation** as recurring substrate; **AI memory** that compounds across appointments (switching cost); and trust + GDPR posture. The conversation is the rare asset; the ladder makes it smarter and stickier |
| **Monetize** | Not patient subscription on intelligence alone (every pure-consumer AI assistant pivoted away from D2C). The money is B2B — pharma-sponsored oncology programs are the most reachable EU patron near-term; payer/DiGA-style reimbursement only if/when Ditto commits to a Class IIa device. The central tension stands: v2 is patient-first, every monetization path is B2B |

**Bottom line:** the intelligence layer is Ditto's contrarian core and the only place it can build a moat, but it is structurally a multiplier on the conversation, not a standalone business. Climb to generic advising for free; deliver individualised value through a human-in-the-loop; let tracking and narrative manufacture the between-appointment frequency that the layer needs and that Ditto lacks today. Never charge the patient for the intelligence, and never make the patient's data the product.
