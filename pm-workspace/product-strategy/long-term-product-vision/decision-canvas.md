# Ditto Decision Canvas — June 2026

**Status:** draft for founder alignment (weekend of June 6–7) and the product strategy session. Distills [`long-term-product-vision.md`](./long-term-product-vision.md) + sources 08–14 into the decisions we actually have to make. Roadmap picks are deliberately not in this document; Merlijn reviews the full project backlog and the strategy session decides.

---

## 1. Five years out (2031, aspirational)

When serious illness enters a family, Ditto is the first thing they reach for and the place the whole family lives for the duration. Every conversation with every doctor is captured, understood, and remembered. Anyone in the circle can ask anything, at any hour, and get an answer grounded in mum's actual care, not in the internet's averages. The family knows how she is really doing today without making her repeat it. Nothing about the illness is faced alone or left unexplained.

What is true in 2031:
- Half of newly diagnosed oncology patients in the Netherlands start using Ditto within a week of diagnosis; hospitals hand it over in the consult room.
- The product fires every day, not per appointment: it listens, synthesizes, and answers, in Dutch, on EU soil, from your own record.
- Insurers and hospitals pay for it; families never do.
- The same trusted layer is expanding across Europe and across severe disease paths, via partners.

---

## 2. The routes

| Route | Focus | One-sentence claim | What's in | What's explicitly out |
|---|---|---|---|---|
| **A — Care OS** | Care admin & operations | Ditto runs the family's care: everything needed to manage, coordinate, and hand off the care of a loved one, in one place | Shared calendar & tasks, med management, circle coordination & handoffs, proxy access, document hub | Diagnosis or clinical advice, peer communities of strangers, consumer social feed |
| **B — Care companion** *(merges daily companion + treatment companion + trusted answers)* | Understanding & daily support; context-aware generation | An always-there companion that checks in, listens, answers anything from your own care, and walks you and your family through every phase of treatment | Proactive (voice) check-ins, smart synthesis of how you're doing, ask-anything grounded in your own consults, care-path programs (oncology first), event-anchored windows (pre-scan, post-infusion), pre-appointment prep, automatic symptom capture from speech; consented RWD products; wearable enrichment later | Triage ("go to the ER"), treatment recommendations, generic health content, open-web answers, horizontal any-condition app, consumer payment |
| **D — Verified care record** | Data management | The patient-owned memory of everything that happened in your care, portable across providers and borders | Longitudinal consult archive, letter/photo ingestion, structured history, sharing & export, EHDS front-end (2029) | Interpretation-free raw data dumps (Caren's mistake), being the clinicians' system of record |
| **E — Care network for family & loved ones** | The social side of care | The private network where a family carries illness together: one update, the right version for everyone, help that actually arrives | Tell-once updates, audience-adapted versions, help dispatch, second-pair-of-ears, non-broadcast mode | Public sharing, communities of strangers, engagement mechanics for their own sake |

Read: four routes after the merge. Trusted answers folded into B because context-aware generation makes them one capability, and the treatment-path packaging is B's beachhead form, not a separate product. They compose rather than compete: D is the substrate, B the daily surface, E the social layer, A the caregiver-led variant. The session question remains which becomes the **spine**.

---

## 3. Where we stand: the five challenges

1. **No proven growth engine inside the product.** K≈0.012, ~1.4 circle members per patient; Core MAU ~2.1K against the 5K June target. The circle thesis is designed, not demonstrated.
2. **Massive commoditization of AI summaries.** ChatGPT Health (~230M weekly health questions), Microsoft, Oracle, Apple, plus four funded copycats of our exact action in 8 months (Mirror, Neatly, Kin, Hedy). The standalone summary fails the "does a 100× better model help or hurt you" test.
3. **Heavy dependence on appointments.** The disease is lived 24/7; we show up only around visits. Between-visit and in-visit presence is where the unmet, unowned territory is.
4. **Monetization unresolved.** Patients don't pay (zero survivors of consumer-paid health, ever); B2B path is early; engagement without a payer is the Babylon trap (they lost money on every active user).
5. **Trust assumed, not measured, and a sharp regulatory line.** Execs overestimate their own trust asset (89% vs 39% in PwC's data); one bad AI answer to a frightened patient spends years of it. And candidate features drift into MDR/AI-Act high-risk territory the moment "inform" becomes "advise."

---

## 4. Decisions

| # | Decision | Status |
|---|---|---|
| D1 | **Narrow and defensible:** severe disease paths only (oncology first), EU/NL first. Depth, trust, and the EU stack are the moat | **Decided** (board-aligned) |
| D2 | **Expansion only via B2B partnerships** (new geographies, new disease paths, new segments); opportunistic B2B inbound welcome; no broad consumer GTM | **Decided** (board-aligned) |
| D3 | **Speed goes up.** Faster decision cadence, ship weekly, fast experimentation as the default way of answering questions | Proposed |
| D4 | **The safe lane is a hard line:** inform/educate/organize, grounded in the patient's own care. No diagnosis, no triage, no treatment advice. This is what keeps us fast (non-device) and trustworthy | Proposed |
| D5 | **How far and how fast to expand feature scope *within* the safe lane** (the real risk-appetite question) | **Open — for the session** |

---

## 5. Critical open questions (the eigenquestions)

Each carries a draft answer, written to be challenged, not to be agreed with.

| # | Question | Draft answer |
|---|---|---|
| Q1 | **What's the core problem we're solving?** | **Feeling in control while seriously ill.** The red thread through everything: you understand what was said, you know what to do next, you can ask credible questions, you have an overview of your symptoms, and your loved ones can actually offer help. Every feature serves this or doesn't belong |
| Q2 | **What are the core actions?** | Candidates: record-and-understand the conversation (the proven want), daily check-in with synthesis back, ask-anything grounded in your own care, tell-once update to the circle. Episodes are the proven anchor; the daily surface is the open experiment (source 12) |
| Q3 | **Who is the primary user?** | Patient-primary with the partner as built-in second user in oncology; caregiver-primary in neuro. The spokesperson pattern hints the real unit of adoption may be the circle-with-a-designated-author. Interviews + own data decide |
| Q4 | **Are daily health habits realistic for people who don't want to be ill?** | The honest draft: daily *work* is refuted, and patients say it plainly ("Breast cancer happened to me, but I do not want to think about it daily"). Engagement must hand back control, not demand attention; anything pushed for our growth rather than their need will fail. Whether AI-delivered daily *value* (received, not submitted) escapes this is the central experiment |
| Q5 | **Who pays, for what outcome?** | Hospital or insurer (NL precedents exist: Untire via VGZ, SkinVision via CZ); pharma RWD later and only consented; never the patient |
| Q6 | **What is the North Star?** | Draft: adoption depth in the beachhead (% of newly diagnosed NL oncology patients active in week one) plus per-episode ownership (consults recorded, summaries re-opened, shares answered). Not raw DAU |

---

## 6. How we answer them — max two weeks (done by June 19)

| Step | When | What |
|---|---|---|
| **1. Founder alignment** | **This weekend (June 6–7)** | Walk this canvas against sources 11–14 (the research is the input, not background reading); decide or explicitly defer: route spine, D3–D5, Q1, Q6. Output: a marked-up canvas with decisions logged |
| **2. Own data** | Days 1–3 | Step-0 Mixpanel/Porygon pull: retention by care path, summary re-opens, circle size & activity, pre-scan re-engagement. Never yet done; cheapest evidence we have |
| **3. Market research — systematic, standardized, fully agentic** | Week 1 | One pipeline per remaining open question, same shape every time: fan-out agent sweep → 3-vote adversarial verification → standard synthesis template (the sources 12–14 method, now the house standard). Queue: NL payer/reimbursement scan, MDR/AI-Act legal prep (input for Łukasz), competitor monitoring as a recurring agent job |
| **4. User research** | Starts inside the window | Screener + recruiting live in week 1, first interviews in week 2; guide built from sources 11–13 incl. the 8 uncovered windows. Interviews continue past June 19; early signal feeds the session |
| **5. Concierge pilot (wizard-of-oz)** | Go/no-go at founder alignment; design + recruiting within the two weeks | The only method that truly answers Q4: ~30 patients get the daily companion *delivered manually* (team + AI behind the curtain: check-ins, synthesis, grounded answers over e.g. WhatsApp/voice) before any product is built. Measures: do they keep responding past week 3, what do they ask at 3am, does the circle engage. The answer itself takes a cohort cycle (~4–6 weeks), so only design, recruiting, and protocol fit inside the two weeks |
