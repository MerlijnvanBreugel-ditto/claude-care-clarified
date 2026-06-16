# Lessons from Tony Fadell's *Build* — applied to ditto & the two prototypes

**Compiled:** 2026-06-16 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Source:** Tony Fadell, *Build: An Unorthodox Guide to Making Things Worth Making* (2022). Fadell led the iPod and iPhone product teams at Apple and founded Nest.
**Scope:** the lessons most relevant to ditto's mission, focused on the two prototypes — **A** ([grounded contextual chat](prototype-A-grounded-contextual-chat/spec.md)) and **B** ([voice-first "ditto today" note](prototype-B-voice-daily-note/spec.md)).

> **A note on fidelity.** This is an applied synthesis of *Build*'s ideas, not a quotation. Framings are paraphrased from memory of the book; treat the *concepts* as Fadell's and the *applications to ditto* as ours. Where a lesson reinforces something already in the corpus, it's cross-linked (`M17`, `S3`, `reused/13`).

---

## How to read this

*Build* is organised as "Build Yourself → Your Career → Your Product → Your Business → Your Team → Your CEO." The richest material for two early prototypes is **Build Your Product** and **Build Your Business**, so those dominate. Each lesson below has: **the idea**, **what it means for ditto's mission**, and **→ A / → B** concrete applications, ending with a per-prototype **Fadell test** and a distilled top-10.

---

## Part I — Build Your Product (the core)

### 1. Start with *why* — the story is the product's foundation
**The idea.** Fadell insists every product begins with a *why*, not a *what*. The "why" must survive being told as a simple story; if you can't explain why it should exist in a sentence, you don't understand it yet. The story is not marketing you bolt on at the end — it *is* the product, and it should drive every decision.

**For ditto's mission.** The why is already strong and validated (`reused/13`): *people hit by a serious diagnosis don't understand or remember their care, can't see the whole picture, and carry it alone — at the moment they're least able to.* Lead with that human "why," never with "an AI health app."

**→ A.** The story is *"finally understand — and act on — what your doctor actually told you, in plain language you can trust."* Not "a medical chatbot." Every feature (pills, citations, due-dates) must serve that one sentence or be cut.
**→ B.** The story is *"get what's in your head out — even on your worst day — and let ditto make sense of it for you."* Not "a voice journaling app." The "why" is relief from the daily, lonely cognitive load.

### 2. Painkiller, not vitamin (and definitely not a "nice-to-have")
**The idea.** Fadell ranks products: **painkillers** (solve acute, real pain — people *need* them), **vitamins** (good for you, easy to skip), and nice-to-haves (die first). Aim to be a painkiller. This is the single biggest predictor of whether anyone will actually use the thing.

**For ditto's mission.** Comprehension failure + anxiety + "what was I supposed to do?" are genuine, repeated pains — this is the corpus's own "vitamin-vs-painkiller" test (`S3`, `reused/13`). The risk is shipping a vitamin that *feels* clever but isn't *needed*.

**→ A.** Painkiller = the panic of "I don't remember what the oncologist said / what I'm supposed to do." Anchor v0 on *that*, not on "ask me anything about hypertension" (a vitamin) (`research A §implications`).
**→ B.** Painkiller = "I'm overwhelmed and exhausted and I just need to offload this without effort." The zero-energy capture *is* the analgesic. If a healthy, energetic person is the only one who'd use it, it's a vitamin — design for the worst day, not the best.

### 3. Make the intangible tangible — prototype the *experience* before the product
**The idea.** Fadell's most actionable tool: before building, **make the intangible tangible** — write the press release, sketch the user manual, storyboard the journey, mock the moments. Force the fuzzy idea into something concrete you can react to. "Mock it up, then mock it up again."

**For ditto.** This is exactly why the specs carry **ASCII wireframes and narrated flows** rather than prose alone — and why a low-fi clickable mock is the natural next step. Write the App Store description and the first-run script *now*.

**→ A.** Mock the *answer*, not the architecture: storyboard the exact chat exchange → the pill that appears → the detail panel → "Save to home." Write the one-paragraph "press release": *"Ask ditto what your doctor said; it answers in plain language, shows your follow-ups as tappable reminders with the right dates, and links every claim to a trusted source."*
**→ B.** Storyboard the 60-second ramble: the card, the tap, the fade-in transcript, the pills accreting, "stop," "here's what we understood." Mock it as a clickable/paper prototype before writing real-time-STT code — the *feel* (calm, understood) is the product, and it's cheap to test fake.

### 4. The product is the **whole journey** — design the "virtual product"
**The idea.** Fadell: the product isn't the object — it's the entire experience, including the parts before you own it (the ad, the store, the box) and after (setup, support, the second week). Map the **customer journey** end-to-end and design every touchpoint, especially the unglamorous ones (Nest obsessed over the unboxing *and* the installation *and* support calls).

**For ditto.** The "product" includes: how a newly-diagnosed patient first hears about ditto (likely *at the clinic*, via a clinician or patient org — the B2B2C channel, `reused/14`), onboarding when they're frightened, the empty state, the bad-day state, and what happens when extraction is wrong.

**→ A.** Design the **empty state** ("you have no visits yet") and the **wrong-answer recovery** (how a patient corrects a mis-extracted date) as carefully as the happy path. The "box" is the first answer that nails *"what did my doctor say?"*
**→ B.** Design the **cold-start** ("I don't know what to say"), the **bad-day state** (trailing off, long pauses, pure emotion with no facts), and the **caregiver-carrying-it** state (`reused/13 §4`). The journey includes the moment *after* "stop" — what you do with the entry is part of the product.

### 5. Disrupt on **one or two axes** — be evolutionary on the rest
**The idea.** Fadell: real disruption usually needs a new **technology** *and* often a new **business model**, but you **cannot disrupt everything at once** — pick your battles and be deliberately evolutionary/familiar everywhere else, or you overwhelm users and yourself. He distinguishes **disruptive vs evolutionary vs execution** innovation.

**For ditto.** The disruptive axis is the **AI comprehension layer** (grounded, contextual, patient-grade — the white space, `M11`). Do **not** simultaneously try to disrupt the regulatory model (stay non-device, `M14`) *and* the business model *and* the interaction paradigm. Be familiar where you can.

**→ A.** Disrupt on *grounded-contextual answers + generative-UI action pills*. Be **evolutionary** on everything else: it still looks like a chat app people already understand; citations look like links; saved items look like a to-do list. Don't also invent a novel navigation model.
**→ B.** Disrupt on *live extraction + effortless voice capture*. Be **evolutionary** elsewhere: it's "a notes app you talk to" (a familiar mental model — Granola/AudioPen, `research B`), not a strange new ritual. One disruption (live pills), familiar everything else.

### 6. It takes **three generations** — V1 is for learning, not perfection
**The idea.** Fadell: products rarely succeed on V1. V1 proves the concept and teaches you; V2 fixes what you learned; V3 is usually where it actually gets good and profitable. Plan for the arc — ship V1 to *learn*, not to win, but make it real enough to teach you something true.

**For ditto.** Treat these prototypes as **V1s whose job is to kill or confirm a hypothesis**, not to be the finished companion. The corpus already names the riskiest hypotheses to test (`reused/13 §5`): *will the seriously ill open a daily app?* (B) and *will patients trust & act on a grounded companion?* (A).

**→ A.** V1 = does the pill/cited-answer loop produce **comprehension + action capture + trust**? Don't gold-plate cross-provider ingestion or voice yet (V2/V3 in the spec's "later").
**→ B.** V1 = does effortless voice capture **retain** where logging churns (~70%/100d, `research B`)? Don't build trends/correlations yet — that's the V2 reward. Ship the loop, measure D7/D30.

### 7. Data-driven *and* opinion-driven decisions — know which you're making
**The idea.** Fadell: there are **data-driven** decisions (you have the numbers; let them decide) and **opinion-driven** decisions (no data exists yet; you must lead with vision, taste, and conviction). The biggest, most important calls are usually opinion-driven — and you cannot A/B-test your way to a first version. But you must be honest about which kind you're making and not hide an opinion behind fake data.

**For ditto.** The decision to build a *daily companion* is **opinion-driven** — there's no data yet that the seriously ill will form the habit (`reused/13 §5–6`). That's allowed — but name it, hold the conviction, and design the prototype to *generate the data* that will make the next decision data-driven.

**→ A.** Opinion call: that patients want grounded answers over their *own* record (vs. generic Q&A). Test it — the pill-interaction and source-open rates become the data.
**→ B.** Opinion call: that live extraction *reassures* rather than *distracts* — the corpus flags this as **unstudied** (`research B §2`). This is a pure taste/vision bet for V1; build it, then let the prototype produce the missing data.

### 8. Win the **first 90 seconds** — the first impression is the product
**The idea.** Fadell (and the Apple lineage): the first run, the first delight, the "moment" decides everything. Engineer one unmistakable *aha* early, fast, with no setup tax.

**For ditto.** First-run with a frightened, tired user has *no* tolerance for friction or a cold empty state. Seed the very first experience from data ditto already has (the existing appointment summary).

**→ A.** The aha = the first time it answers *"what did my doctor say I need to do?"* correctly, in plain language, with a tappable, correctly-dated follow-up. Seed it from an existing summary so the first answer is already personal.
**→ B.** The aha = *"I rambled for 40 seconds and it understood me"* — the calm summary that proves it listened. Must land in under a minute, zero setup. Seed the first nudge from the last visit so the first card already feels personal (`research B §5`).

### 9. Make the complex simple — be the "Rosetta Stone," let the product do the work
**The idea.** Fadell's Nest thesis: take something complicated and intimidating (programming a thermostat) and make it *learn so the user doesn't have to* (Auto-Schedule). Don't expose complexity — absorb it. The product should do the hard thinking; the user should feel calm and capable.

**For ditto.** This *is* ditto's mission expressed as a design principle: medical jargon → plain language; a scatter of visits/meds → one understandable picture. The intelligence should hide, not show off.

**→ A.** Don't make the patient parse a wall of text — the LLM does the synthesis and hands back a *tappable, dated action* and a *plain-language sentence with a source*. The complexity (extraction, grounding, date math) is absorbed; the user sees calm clarity. (This is the "absorb complexity" twin of `M17 #1/#8`.)
**→ B.** The user just talks; ditto does *all* the structuring (categorisation, timing, dedup). No fields, no taxonomy shown — the pills are the gentle evidence that the hard work happened invisibly. Auto-Schedule for your health day.

### 10. Friction is the enemy — remove steps until it hurts, then remove one more
**The idea.** Fadell obsesses over removing friction and steps; every tap, every decision you push onto the user is a tax. The best products feel effortless because someone agonised over deleting the work.

**For ditto.** Effortlessness isn't a nicety here — it's survival. The corpus is blunt: the manual-logging **effort-tax drives ~43% dropout / ~70% abandonment** (`research B §3`, `M15`). Friction is literally the churn mechanism.

**→ A.** "Save to home" should be **one tap**; due-dates should be **pre-filled** (editable), never typed; citations **one tap** to open. Never make the patient assemble the action themselves.
**→ B.** **One action**: tap → talk. No form, no fields, no category-picking, no mandatory prompt. The whole design ethos ("abstract the interface away") is Fadell's anti-friction principle taken to its logical end.

### 11. Sweat the details — design is *how it works*, and empathy is the method
**The idea.** Fadell (Jobs's lineage): "design is not how it looks, it's how it works." The details — the ones users never consciously notice — are where trust and delight live. The method is **empathy**: feel what the user feels, especially their frustration and fear.

**For ditto.** The details *are* the trust. For a frightened patient, a single wrong med name or a notification at the wrong moment breaks everything.

**→ A.** Details that matter: the **source snippet** under each action ("from your visit on 9 Jun: '…in two weeks'"); refuse-when-unsure copy that's reassuring not robotic; never fabricating a date (`research A §3`). These invisible details *are* the product's credibility.
**→ B.** Details: the transcript fading from the *middle* and scrolling up; pills that **never** ping or jump mid-ramble; white pills with icon-only colour so it's calm not busy; confirming a med at the summary, not interrupting. Empathy = designing for someone with no energy and real fear.

### 12. Tell the story to the **rational, the emotional, and the fearful (lizard) brain**
**The idea.** Fadell on storytelling/selling: a great narrative speaks to the *rational* mind (the facts), the *emotional* mind (how it feels), and the *lizard* brain (fear, anxiety, "what could go wrong"). Use **analogy** to make the unfamiliar familiar ("1,000 songs in your pocket"). People decide emotionally and justify rationally.

**For ditto.** Patients act from fear and overwhelm. The messaging — and the in-product copy — must soothe the lizard brain (safety, "you're not alone, we've got this") while giving the rational mind the cited facts.

**→ A.** Analogy candidates: *"a friend who was in the room with you, remembers everything the doctor said, and explains it plainly."* Rational = citations + dates; emotional = calm clarity; lizard = "this is not advice; here's when to call your team" (safety reduces fear).
**→ B.** Analogy: *"a calm place to put down what you're carrying."* Emotional/lizard brain is the *whole point* — the felt reward is *being understood and unburdened* (`research B §3`). Copy must never sound clinical or judgmental.

---

## Part II — Build Your Business

### 13. Shipping is a heartbeat — deadlines force the decisions vision can't
**The idea.** Fadell: a company needs a **heartbeat** — a release cadence. Deadlines are not bureaucracy; they *force* the hard prioritisation and prevent endless polishing. You learn nothing until you ship.

**→ ditto / both.** Set a hard date for a *testable* V1 of each prototype (even fake-backend / wizard-of-oz, echoing `reused/13 §6`'s concierge step). The deadline is what turns the long open-questions lists into a shippable subset. Don't wait for the perfect grounding corpus or perfect STT — ship enough to learn the one thing each V1 must learn (lesson 6).

### 14. Marketing is part of the product, and you are *always* selling
**The idea.** Fadell: don't hand the story to a marketing team at the end — the founders own it from day one, and the product itself is the most important marketing. You're always selling: to users, clinicians, investors, your own team.

**→ ditto.** The clinician/patient-org channel (`reused/14` B2B2C) means the *first* audience to "sell" is the care team who will recommend ditto. The prototype's story must make sense to *them* too ("it helps your patients understand and follow the plan — and it never gives advice").
**→ A/B.** Bake the story into the empty states and onboarding — the product teaches its own "why."

### 15. The business model is a disruption lever — but de-risk it, don't bet the prototype on it
**The idea.** Fadell: changing the business model is often *required* for true disruption (razor/blades, services) — but it's a separate, hard bet. Recurring revenue and "captive" follow-on value are powerful.

**→ ditto.** The corpus is clear that **B2B2C / reimbursement** is the survivable model and **pure D2C is the hard path** (`S3`, `M1`). *But* per lesson 5, don't try to prove the novel business model *and* the novel product in the same V1. Prototype to validate the *experience*; run the monetisation/regulatory probes in parallel (`reused/13 §6 Step 2`), not inside the prototype.

### 16. Solve a real problem you understand deeply — and avoid the two startup deaths
**The idea.** Fadell warns about building a solution in search of a problem, and about the two ways young companies die: never finding product-market fit, or finding it and failing to scale/execute. Stay obsessed with the real, felt problem.

**→ ditto.** The problem is real and well-evidenced (the whole `healthcare-life-changing-moments` round). The danger for *these* prototypes is the *cool-demo trap* — building the impressive thing (live pills! generative UI!) and forgetting it must relieve a real painkiller (lesson 2). Both specs' success metrics are designed to catch this (do users actually *use* the pills / *return* daily?).

---

## Part III — Build Your Team & Yourself (mission-level)

### 17. Be mission-driven; small teams of A-players move fastest
**The idea.** Fadell: the best teams are small, mission-driven, and made of people who care about the *why*. Money-first cultures build vitamins; mission-first cultures build painkillers.

**→ ditto.** The mission (dignity and understanding for the seriously ill and their families) is a genuine A-player magnet — use it. Keep the prototype team tiny and obsessed with the patient's worst day.

### 18. Get the assist / find the mentors — you can't see your own blind spots
**The idea.** Fadell on mentorship and "the shit umbrella": seek people who've built the thing before; let the founder absorb chaos so makers can make.

**→ ditto.** For the regulatory line (non-device, `M14`), the STT-safety line (`research B §2`), and grounding safety (`research A §6`) — get expert "assists" early rather than learning the expensive way. These are named open questions in both specs.

---

## The "Fadell test" for each prototype (use before building)

**Prototype A — grounded contextual chat**
- [ ] Is it a **painkiller** (the panic of "what did my doctor say / what do I do") — not a vitamin ("ask anything")?
- [ ] Is the **why** a one-sentence story a frightened patient would repeat?
- [ ] Are we disrupting on **one axis** (grounded-contextual + pills) and evolutionary elsewhere (it's still a chat)?
- [ ] Does the **first answer** deliver an aha in <90 seconds, seeded from real data?
- [ ] Does the product **absorb the complexity** (synthesis, dates, grounding) so the patient feels calm and capable?
- [ ] Is every **detail** that builds trust handled (source snippet, no fabricated dates, refuse-when-unsure)?
- [ ] Is V1 scoped to **learn one thing** (trust + action capture), not to be complete?

**Prototype B — voice daily note**
- [ ] Is it a **painkiller** for the *worst, lowest-energy day* — not a tool for the motivated well day?
- [ ] Is the experience **one action** (tap → talk), friction deleted to the bone?
- [ ] Does the first ramble produce the aha — *"it understood me"* — in under a minute?
- [ ] Is the disruption **one axis** (live extraction) wrapped in a familiar "notes app you talk to"?
- [ ] Do the **details** keep it calm not creepy (peripheral pills, no nagging, audio deleted)?
- [ ] Is it honestly an **opinion-driven** bet (live extraction reassures), and does V1 generate the missing data?
- [ ] Is V1 scoped to learn **retention** (does the seriously ill return), not to ship trends?

---

## The ten lessons that matter most for ditto (distilled)

1. **Painkiller, not vitamin** — design for the worst day; relieve real pain or nothing else matters.
2. **Start with the why** — a one-sentence human story drives every feature; cut what doesn't serve it.
3. **Absorb the complexity** — be the Rosetta Stone; the AI does the hard thinking so the patient feels calm. (This *is* the mission.)
4. **Delete friction to the bone** — effortlessness is survival here, not polish (the churn mechanism is the effort-tax).
5. **Win the first 90 seconds** — one seeded, real aha, zero setup.
6. **Disrupt on one axis** — the comprehension/AI layer; be evolutionary (familiar) on everything else; stay non-device.
7. **It takes three generations** — these are V1s to *learn*; scope each to kill or confirm one hypothesis.
8. **Name your opinion-driven bets** — the daily-habit and live-extraction bets have no data yet; hold conviction *and* design V1 to produce the data.
9. **Make the intangible tangible** — storyboard/mock the experience (and write the press release) before building; the *feel* is the product.
10. **Sweat the trust details** — source snippets, no fabricated dates, refuse-when-unsure, calm-not-creepy pills; in health, the invisible details *are* the credibility.

**If you keep only one:** *Make a painkiller that absorbs the complexity and feels effortless on the patient's worst day — and ship a V1 whose only job is to prove they'll come back.*

---

*Cross-references: prototype specs ([A](prototype-A-grounded-contextual-chat/spec.md), [B](prototype-B-voice-daily-note/spec.md)) · mechanics [`M17`](../research/market-research/findings/M17-table-stakes-mechanisms.md) · playbook [`S3`](../research/market-research/synthesis/S3-proven-mechanics-playbook.md) · strategy [`reused/13`](../research/market-research/reused/13-synthesis-final.md) & [`reused/14`](../research/market-research/reused/14-moat-and-platform-strategy.md).*
