# The Magic Experience Vision

**Date**: 2026-04-15
**Status**: Strategic crunch, contrarian draft
**Method**: Three parallel virtual panels (Craftsmen, Contrarians, AI-Natives) + synthesis
**Author**: Mewtwo
**Parent**: [Unicorn Strategy](unicorn-strategy.md), [Care Brain MVP Spec](care-brain-mvp-spec.md)
**Purpose**: Answer the question: "What does the Ditto experience look like if it goes from 'useful' to 'this changes things fundamentally'?"

---

## The Diagnosis

Merlijn's instinct is right. The current summary is useful but not defensible, and the planned Care Brain — Q&A, health profile, adapted sharing, prep — is a better summary with extras bolted on. That's not a unicorn. That's a premium feature set on a commoditizing category.

Three converging reasons this is true:

| # | Observation | Consequence |
|---|---|---|
| 1 | ChatGPT already does grounded transcript Q&A. Apple Intelligence will summarize voice recordings natively in 12-18 months. | The "AI summarizes a thing" category has a shelf life measured in quarters. |
| 2 | Ditto invests ~80% of engineering on the processing pipeline (commodity) and ~20% on the relationship layer (defensible). | Effort is concentrated on the part that's depreciating fastest. |
| 3 | Care Circle growth is 50 invites/day on 35K users — 0.14% daily sharing rate. That's not a network effect; it's a broadcast mailing list. | The "care graph moat" is a hope, not a fact. |

"Useful" is a ceiling. To break through it, the product has to stop being about the recording and start being about the relationship over time.

---

## The Magic Formula

Every product that makes people say "how does it know?" shares three properties — and only three:

1. **Removal of a step the user assumed was their job.** Shazam removed the search. Nest removed the thermostat. Stripe removed configuration. Magic is the absence of effort, not a better version of effort.
2. **Articulation of knowledge they already had but couldn't name.** Oura doesn't tell you new facts. It gives language to a vague feeling. Superhuman confirms a suspicion. Magic is: the product put words on your fuzzy intuition.
3. **Anticipation — it happens before you ask.** Spotify's Discover Weekly. Waze rerouting you. The Airbnb host who noticed you mentioned a birthday. Magic is: the product was already thinking about you.

For Ditto specifically, the user is not browsing. They're leaving an appointment where a doctor just said something that might change their life, hands shaking, trying to remember the name of a medication, needing to tell their daughter. In that moment, every tap is a tax. Every screen is a decision.

**Magic here is not delight. It is relief.**

---

## The Contrarian Reframe

The panels converged, from three different directions, on a single uncomfortable truth: **Ditto is building for the wrong person, doing the wrong job.**

Today's frame: *"A patient records an appointment. We make the summary understandable. They can share it."*

Three reframes that each reorganize the product around something defensible:

### Reframe A — Ditto is the family's shared medical memory.

The person in real pain after the appointment is not the patient. It's the daughter pacing the hallway. The partner at home. The son in London. They are currently running a broken game of telephone with sticky notes and WhatsApp. Nobody owns this.

**The job being done**: "I need to know that the right thing is happening to someone I love — without calling them at 9 PM to re-interrogate what the doctor said."

**The magical experience**: Mom records her oncology appointment. Dad sees the update instantly, with action items. Daughter in Amsterdam sees a version framed for her ("nothing to panic about, here's what changed"). Son in London gets the same in English. Nobody forwarded anything. The family is synchronized automatically.

**Why it's defensible**: Multi-user medical data sharing is a regulatory minefield. Healthcare incumbents build for clinical workflows. Consumer companies don't touch health data. Ditto sits in the only empty quadrant.

### Reframe B — Ditto is the patient's immune system against medical errors.

Medical errors are the third leading cause of death. The dramatic ones aren't surgical mistakes — they're coordination failures. The specialist doesn't know what the GP prescribed. The follow-up scan never gets scheduled. The drug interaction nobody caught.

**The job being done**: "I need to be certain nothing is falling through the cracks between my doctors."

**The magical experience**: Ditto notices your cardiologist prescribed a beta-blocker last week and your pulmonologist just mentioned starting a medication that interacts with it. A card appears: "Your doctors may not know about each other's prescriptions. Here's a summary to bring to your next appointment." The patient walks in informed. An error is prevented.

**Why it's defensible**: Ditto has all the raw data (recordings, extracted meds, conditions, care team, timeline). Nobody else does. The regulation risk terrifies big incumbents. The information is already in the recordings — Ditto just surfaces what was said.

### Reframe C — Ditto is Europe's patient data layer (the EHDS play).

EHDS rolls out in phases starting late 2026. Patients will have a legal right to portable health data. The regulation creates a right without creating a product.

**The job being done**: "My medical data is mine, scattered, unusable — and now it needs to become a coherent story I can carry and share."

**The magical experience**: Your Ditto profile isn't just what was extracted from appointments. It's your full medical record — labs, imaging, prescriptions, GP notes — pulled automatically via EHDS APIs, translated into language you understand, shareable with anyone you choose.

**Why it's defensible**: First mover advantage on consumer-facing EHDS integration. Apple Health is US-centric, Google has EU trust problems, EHR vendors ship terrible consumer UIs. Generational opportunity.

---

## Which Reframe Wins

**Pick A (family shared memory) as the primary lens. B and C stack on top.**

Reasoning:
- A is the only one that creates real network effects (every patient brings 3-7 circle members; circle members become patients).
- A is the hardest to copy and the most emotionally load-bearing.
- B (error prevention) is best expressed as a feature inside A — the family's shared brain catches what fragmented doctors miss.
- C (EHDS) is the platform play that makes A 10x more valuable over time. Prepare for it, but it's the 2027 move.

**The one-line positioning**: *"Ditto is the health layer for everyone who cares about you. One recording, everyone informed, nothing falls through the cracks."*

---

## The Seven Magical Moments

Scaled, specific, emotionally honest. Each is describable in a single scene. Each has a "tell-your-daughter" line that would make her sign up tomorrow.

| # | Moment | Magic Mechanism | "Oh shit" line |
|---|---|---|---|
| 1 | **The Share That Writes Itself.** Patient just got hard news. Taps Share. Sees three preview cards — full-detail for partner, softer version for daughter, one-liner for employer. All adapted automatically. Three taps, done. | Removes the most painful micro-task of health life: figuring out how to tell each person. | "It wrote the message to my daughter better than I could have. It even knew not to scare her." |
| 2 | **The Summary That Caught What You Missed.** Patient opens Ditto the second they leave the room. Summary is already there. Third bullet highlights a medication change the patient didn't register in the moment. | Anticipation + articulation. "Someone was paying attention when I couldn't." | "It caught a medication change I completely missed. I didn't even hear the doctor say it." |
| 3 | **The Question You Were Afraid to Ask.** Below the summary: a chip reading "What happens if I miss a dose?" — the exact thing the patient has been wondering for three appointments but felt too embarrassed to ask. | Anticipation + removal (no need to formulate, no judgment). | "It knew exactly what I was worried about. I didn't have to ask." |
| 4 | **The Family Dashboard.** Daughter Sanne opens Ditto — not to receive a summary, but to see a living view of her father's care: last visit, current meds, upcoming appointments, open action items, things to ask about next time. | Turns circle members into daily actives. Removes the 9 PM phone call. | "I stopped calling my dad to ask what the doctors said. I just open the app." |
| 5 | **The Pattern Nobody Saw.** After four appointments, a card appears: "You've mentioned fatigue in your last three visits. Different treatments each time. Worth raising whether these are connected." | Reasoning across time that fragmented healthcare can't do. The restraint IS the magic — it observes, doesn't diagnose. | "Three doctors missed it. The app connected the dots." |
| 6 | **The Cross-Doctor Catch.** "Your cardiologist prescribed a beta-blocker on April 3. Your pulmonologist just mentioned starting you on something that interacts. They may not know about each other. Here's what to bring up." | Coordination that only the continuous companion can provide. | "Ditto caught a drug interaction my doctors didn't." |
| 7 | **The Living Briefing Before Every Visit.** Day before an appointment, a card appears unprompted: "Tomorrow with Dr. Visser. Last scan showed improvement. Two open questions from February. Medication changed in March. Three questions you might want to ask." | The product initiates. Waiting-room anxiety becomes prepared calm. | "I walked in prepared instead of panicked. I would never have remembered to ask about the thing from February." |

Every one of these is technically buildable today with current models. The constraint is product judgment, not capability.

---

## The One Moment to Ship First

**Moment 1: The Share That Writes Itself.**

Not because it's technically impressive. Because it's the only moment that simultaneously:

- Hits the point of greatest emotional need with the lowest cognitive demand (relief, not features)
- Turns one user into three (adapted shares are product demos delivered to people who love the patient)
- Is the only moment on this list that BigTech cannot easily add in 12 months (audience-adapted medical reframing requires the care graph; they don't have it)

**This is the first feature to ship, not the third.** The current plan puts it in weeks 14-20 of the Care Brain build. The adapted share is the emotional climax of the product and the engine of viral growth. It should be week 1-6, before Q&A, before the health profile, before anything else.

The risk is that it ships on top of a summary that isn't yet warm enough, voice-consistent enough, or fast enough to anchor it. So the real priority order is: *fix the summary's emotional tone first (2 weeks), then ship adapted sharing (4 weeks), then everything else.*

---

## What the Current Roadmap Is Getting Wrong

Three mistakes worth naming, each grounded in the panel work:

**1. The summary is treated as solved.**

The roadmap says "existing summarization, upgraded with brain context." But the summary is the first impression for every single user. If it reads like a medical document translated into simpler words — instead of a warm, clear account from someone who was in the room with you — no amount of Q&A or health profile compensates. The team is building the nervous system before nailing the heartbeat. Fix the voice of the first summary before anything else ships.

**2. The emotional climax is in the third act.**

Adapted sharing is the feature that generates "I cannot live without this" reactions and triggers family-side growth. The roadmap puts it in weeks 14-20. That is the wrong sequencing. The feature that produces the emotional peak should be shipped FIRST, then everything else compounds from that trust.

**3. Appointment prep is overbuilt.**

Prep is a nice-to-have retention feature for power users. It does not grow the care graph. It does not create switching costs beyond what the profile already gives. It's a year-three feature being built in a 12-week sprint. **Kill it from MVP.** (The craftsmen liked it as Moment 7 here, but even they agreed it's not in the top tier of "change things fundamentally.") The engineering budget should go to the Circle Member Dashboard instead — the feature that actually activates the care graph.

---

## The AI-Native Shift That's Missing

The "AI is crude oil, we're the refinery" framing was right in 2023. In 2026, it's becoming dangerous — because extraction prompt quality is converging to commodity. Every model update makes tuned extraction less necessary. The refinery is depreciating.

**The real 2026 moat isn't processing quality. It's agentic follow-through + longitudinal memory + permission to act.**

What Ditto isn't exploiting enough:

| Capability | What it unlocks | Example |
|---|---|---|
| **Persistent long-horizon memory** | The brain knows your full medical story across years, not just one appointment. Switching cost compounds with every visit. | "Based on your six oncology appointments, here's your medication history and why each change was made." |
| **Agentic follow-through** | The AI initiates. Checks in. Closes loops. Most of the value in healthcare is not understanding — it's making sure things happen. | "Two weeks after your visit: Dr. Jansen asked you to track BP. Have you? If you share a reading, I can tell you if it's trending right." |
| **Generated UI** | No home screen. The product surface is a stream of contextual moments, composed for you in this moment. | Three days before cardiology: the app opens straight to a prep card. Day after a hospital visit: it opens to "three things that changed." |
| **Real-time multimodal** | The AI is there DURING the appointment (with consent), tracking whether your questions got answered. | Post-visit: "Dr. Bakker discussed the medication change but didn't address your concern about fatigue. Here's how to raise it next time." |

**The reframe**: *"AI is a brain. We're building its memory and agency for healthcare."*

---

## The Architecture That Makes Magic Affordable

*This section integrates two additional inputs: a recent conversation with Yuri on Care Brain architecture (Granola: "Ditto Brain - architecture") and Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern. The magic moments above are buildable. The question is whether they're buildable without drowning a 10-person team in pipeline maintenance.*

### The architectural reframe (from the Yuri conversation)

The instinct Merlijn voiced — "we might need an agentic framework instead of end-to-end pipelines" — is half right. Yuri's correction is load-bearing:

> **Stop thinking in product features. Think as a personal health assistant. What's on the assistant's internal checklist? Each checklist item becomes a specialized, validated pipeline.**

This collapses the false choice between "end-to-end pipelines" and "full agentic." The answer is both, layered:

- **Agentic orchestrator** at the top — infers intent, sequences calls, handles the chat fallback.
- **Specialized micropipelines** underneath — each one does one job well, is independently evaluable, and emits typed data.
- **General-purpose chat** as the escape hatch only — heavily constrained, no treatment advice.

This is also what makes the 40-jobs-to-be-done horizon tractable. You don't build 40 features. You build one plugin framework and 40 pipelines, each small, each reviewed separately, each testable.

### The Karpathy wiki, corrected for healthcare

Karpathy's insight: replace RAG with a persistent, LLM-maintained wiki that compounds every time new sources arrive. Entity pages, cross-references, lint passes. The LLM does the bookkeeping humans abandon.

**The correction Yuri is right about**: the canonical store cannot be markdown. Users modify their own data. Deterministic logic needs structured access. Source of truth must be a **relational/structured health graph (DB)**. The markdown wiki is a *projection* the LLM reads — dynamically rendered from the DB when the assistant needs context.

This gives Ditto three retrieval modes, each appropriate to a different magical moment:

| Retrieval mode | What it's for | Example magic moment |
|---|---|---|
| **Fact (deterministic)** | "Give me all current medications." No similarity, no inference. SQL. | Cross-doctor drug interaction check (Moment 6). |
| **Typed filter** | "All conversations labeled with 'diabetes'." Structured metadata query. | Pattern detection across appointments (Moment 5). |
| **Similarity (RAG)** | "Have I mentioned fatigue recently?" Only when neither fact nor filter fits. | Suggestion anticipation (Moment 3). |

Most "AI-native health app" attempts dump everything into embeddings and hope. Ditto should do the opposite — treat the DB as primary, the LLM wiki as a living context projection, and RAG as the last-resort third option.

### The combined model

```
                      Inputs
    (recordings, documents, voice notes, labs,
     sensor data, messages, calendar events)
                         │
                         ▼
                ┌─────────────────┐
                │  Event bus       │ ← triggers pipelines
                └─────────────────┘
                         │
           ┌─────────────┼─────────────┐
           ▼             ▼             ▼
       Pipeline A    Pipeline B    Pipeline N
     (summarize)   (extract     (adapt_for_
                    meds)         daughter)
           │             │             │
           └─────────────┼─────────────┘
                         ▼
              ┌────────────────────┐
              │  Health graph (DB)  │ ← source of truth
              │  + audit log        │
              └────────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │  Wiki projection    │ ← LLM's working memory
              │  (auto-generated    │
              │   markdown pages)   │
              └────────────────────┘
                         │
                         ▼
              Surfaces: summary card,
              timeline, share preview,
              prep brief, dashboard
```

Each pipeline is a plugin. Each plugin has a trigger, a typed input filter, a reader, a processor (deterministic or LLM or mixed), and a typed output. Yuri's framing exactly.

### Why this architecture is what makes magic cheap

| Magic moment | The pipeline(s) that produce it | Trigger |
|---|---|---|
| 1. The Share That Writes Itself | `adapt_for_audience` (one per circle role) | `summary_ready` |
| 2. The Summary That Caught What You Missed | `prioritize_deltas_vs_history` | `recording_processed` |
| 3. The Question You Were Afraid to Ask | `suggest_from_context` | `summary_ready` + profile context |
| 4. The Family Dashboard | `compose_circle_view` (per audience) | scheduled + on-data-change |
| 5. The Pattern Nobody Saw | `scan_recurring_symptoms` | `new_summary` (stateful across history) |
| 6. The Cross-Doctor Catch | `check_medication_interactions` | `new_prescription_detected` |
| 7. The Living Briefing Before Every Visit | `compose_prep_brief` | `appointment_approaching` (time-based) |

None of these require new infrastructure if the plugin framework is in place. Each is days of pipeline work plus an eval harness.

**The Karpathy contribution**: the `compose_prep_brief` pipeline doesn't re-read 40 transcripts. It reads the LLM wiki for this patient — which has already been updated incrementally by every prior pipeline run. The entity page for "Dr. Visser" already exists. The medication timeline is already current. The open questions from February are already on a log page. The LLM just composes.

### What this implies for the 6-month plan

Good news: the Care Brain MVP spec (Direction C: Nervous System) already points here. Event bus, worker framework, Health Profile Store, typed pipelines. The architectural skeleton is right. The new additions from this crunch:

1. **Add the wiki projection layer.** After every pipeline, the LLM maintains (not generates from scratch) the patient's markdown wiki — entity pages for doctors, conditions, medications; a chronological log; an index. Used as context for every downstream query. This is ~2 weeks of engineering and removes a huge future tax.
2. **Formalize the plugin contract.** Every pipeline declares: trigger, input filter, output type, eval suite, tier (free/premium). Ship the framework first, then 4 pipelines, then 4 more. Yuri's roadmap: don't start with 40.
3. **Three-mode retrieval, explicitly.** Facts first. Filter second. Similarity last. Log which mode each pipeline uses. Avoid defaulting to RAG for everything.
4. **Monetization alignment.** Premium = more pipelines unlocked (Yuri's suggestion). This maps cleanly to the business case. Free tier: recording, summary, basic Q&A, basic share. Premium: cross-doctor checks, pattern detection, proactive follow-up, adapted sharing per audience, family dashboard.

### The risk Yuri flagged (and how to contain it)

Every pipeline costs ongoing maintenance: prompts, evals, monitoring, regression runs. Two pipelines already consume significant team time. Forty pipelines without discipline is a death spiral.

**Containment**:
- Shared eval harness (already planned) is the single biggest leverage point. Every pipeline gets evals for free.
- Pipeline versioning. Old versions retire, not accumulate.
- Auto-generated documentation from pipeline contracts, so a new engineer can onboard a pipeline in an afternoon.
- Hard rule: no pipeline ships without eval coverage and a retirement criterion.

### The strategic conclusion

The architectural decision is not a 2027 problem. It's the decision that determines whether the 7 magical moments ship in a year or in three. The conversation with Yuri and the Karpathy pattern both point to the same shape:

- **Pipeline plugin framework** (the assistant's checklist made real)
- **Typed health graph in a relational DB** (source of truth)
- **LLM-maintained wiki projection** (context that compounds)
- **Three-mode retrieval** (facts → filter → similarity)
- **Eval-first pipeline contract** (scale without dying)

This is the architecture that makes the magic experience affordable. Everything in the roadmap resequencing above assumes this foundation.

---

## The Reordered 6-Month Bet

Based on the crunch, the current 12-week Care Brain plan needs three adjustments, not a rewrite:

| Change | From | To | Why |
|---|---|---|---|
| **Sequence** | S1-S2 Summary+Q&A → S3-S4 Profile → S5 Prep+Sharing | S1 Summary voice fix → S2-S3 Adapted sharing + Circle Dashboard → S4-S5 Profile → S6 Q&A | Ship the emotional peak and care graph activator first. Everything else compounds from trust. |
| **Kill** | Appointment prep (S5) | Dropped from MVP, revisit post-Series A | Lowest leverage feature, highest engineering cost relative to impact. Contrarians unanimous. |
| **Add** | — | Circle Member Dashboard (Phase 2 of adapted sharing) | The only feature that turns circle members from passive recipients into daily actives. Converts broadcast → graph. |

Everything else in the spec is fine. Architecture (event bus, workers, profile store), eval harness, Gate reviews, synthetic personas — all solid. The work is sequencing, not rearchitecting.

---

## The 5-Year Vision (as a Direction Check)

*Tuesday morning, 2031. Anna, 68, Den Haag.*

She wakes up. Ditto surfaces a card: "Your blood sugar has trended slightly high this week. Probably the prednisone Dr. de Vries started last Wednesday. Should normalize Friday. I'll keep watching." She didn't ask. The AI saw her CGM data, her medication timeline, and decided she'd want to know. It also decided her daughter Lisa doesn't need to see this — not clinically significant.

At 10, her rheumatology appointment. Ditto has pre-briefed the clinic with what changed since her last visit. Doctor starts the conversation two steps ahead. During the appointment, Ditto listens. When a biologic is mentioned, it silently checks formulary coverage.

After the appointment, there's no summary. There's a conversation. "Dr. Bakker wants to try adalimumab. Your insurance covers it with prior auth. I can start that process. Main things to watch: injection reactions, infection signs. I'll check in weekly. She also wants bloodwork in 4 weeks — three labs available near you next week, want me to book one?" Anna says yes. Ditto handles the paperwork, books the lab, updates her timeline.

That evening, Lisa opens Ditto: "Mom's rheumatologist switched her to a new medication. Routine for her condition. She's in good spirits. Labs next week." Lisa calls her mother to chat, not to interrogate.

**That's the destination**: not an app you open, but a presence that knows your health, acts on your behalf, and connects everyone who cares about you with exactly what they need. The summary is the starting point. The endpoint is the most trusted health relationship a person has outside their own doctor.

The 6-month bets above — adapted sharing, circle dashboard, longitudinal profile, early agentic follow-up hooks — are the three pillars this vision requires. Ship them, and 2031 is expansion of surface, not reinvention.

---

## Four Cheap Experiments to Validate Before Pivoting the Roadmap

Before committing to a reshuffle, run these in the next 2-4 weeks:

| # | Experiment | What it validates | Cost |
|---|---|---|---|
| 1 | **Wizard-of-Oz adapted shares.** Manually write 20 adapted shares (partner, daughter, friend versions) for real recordings. Send to 10 patients. Measure: did circle members react differently than to a regular summary? Did they sign up? | Whether adapted sharing produces the "missionary" reaction or just "that's nice." | 2 PM-days. |
| 2 | **Circle Member Dashboard clickable prototype.** Figma prototype of Sanne's view of her father's care. Test with 5 family caregivers (recruit via user research notebook). Measure: is this the product they wish existed? | Whether the caregiver-first framing is actually the right reframe. | 3 designer-days + interviews. |
| 3 | **Agentic follow-up, fake-it-till-you-make-it.** 5 patients, one month. After each appointment, manually craft a follow-up message at day 3, day 14. Measure: engagement, emotional response, whether they want it to continue. | Whether the "AI that does, not just answers" shift produces magic or annoys. | 1 PM-day/week + prompt tuning. |
| 4 | **Summary voice test.** Two versions of the same summary: current template vs. a warm, voice-consistent, Doctor-attributed version. A/B test with 100 users. Measure: time-on-summary, tap-through to suggestions, NPS delta. | Whether the "first summary is the heartbeat" hypothesis is load-bearing. | 1 prompt-engineer-day. |

If 2 of 4 validate strongly, the roadmap reshuffle is justified. If they don't, the current plan is probably fine and the "feels useful not magical" gap is about execution polish, not strategy.

---

## The One Line

**"Ditto is the health layer for everyone who cares about you."**

Everything else is downstream.

---

## What to Do With This Doc

1. **Read it with a skeptical eye.** The panels are strong but they're still simulated founders, not real ones.
2. **Pressure-test reframe A (family shared memory)** with the user research notebook — look for caregiver pain signals. If weak, reconsider.
3. **Run experiment 2** (Circle Member Dashboard prototype) within 2 weeks. It's the highest-leverage learning available for <1 week of work.
4. **Decide on the sequencing change** (ship adapted sharing first, kill prep) before Sprint 1 starts. If you wait until mid-sprint, the team will fight the change.
5. **Send me your pushback.** You asked for contrarian. Now push back on the contrarian. Where is this wrong?

---

*Three panels, one synthesis. The real test is what you do with it Monday morning.*
