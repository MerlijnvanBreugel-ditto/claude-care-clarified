# Care Brain — Magic Paths

**Date**: 2026-04-15
**Status**: Extension of the [one-pager](care-brain-one-pager.md) (spec-017)
**Author**: Mewtwo
**Purpose**: Map specific multi-moment user journeys — "paths" — that chain JTBDs and wow moments into lived experiences. Paths are how the product becomes a companion rather than a toolbox. Extendable: path 4+ gets added as a new section in the same template.

---

## Why paths, not moments

The master synthesis catalogues 22 wow moments (beats) and 45 JTBDs (atomic jobs). Both are necessary. Neither is sufficient.

**Magic paths are how beats and jobs come together in real life.** A patient doesn't think "I had a wow moment today." They think "when I left the oncology clinic, Ditto did the impossible: it handled everything." That experience is a path that traverses 4–6 moments in a specific sequence.

This doc maps three paths. Each path has the same anatomy: scene, what happens, JTBDs served, pipelines required (existing + new), new surfaces, architectural notes, missionary line.

---

## Path 1: The Post-Appointment One-Click Cascade

### Scene

Mara, 68, walks out of her oncology appointment. She sits on the hospital bench, shaky from the news about her medication change. She opens Ditto. One screen. Everything is already arranged.

- A follow-up appointment card: Dr. de Jong said "come back in four weeks" — Ditto detected the reference, pulled available slots near her home, is ready to book.
- An action plan: the three things her doctor said to do ("start oxaliplatin Monday," "avoid cold drinks for first week," "call if nausea above 7/10").
- Her pre-prepared questions, with checkmarks next to the ones Dr. de Jong answered and flags next to the ones he didn't. The unanswered ones are already queued for her next visit's prep.
- Three share preview cards: full summary for her husband Hans, softer version for her daughter Sanne, a one-liner for the friends group.

90 seconds later, everything is handled. Without Ditto, Mara would have spent the evening on WhatsApp and the next morning on the phone, and would have forgotten half of it by Tuesday.

### What happens

| Element | What Ditto pre-arranges | What the patient does |
|---|---|---|
| **Follow-up appointments** | Detected from transcript with date hint, provider, reason. Booking slots pulled from nearby facilities if integrated. | Tap "Book" or "Remind me to book" |
| **Action items** | Structured: medication changes, lifestyle actions, warning signs. Each with trigger, timing, source attribution. | Tap "Add to my plan" |
| **Pre-prepared questions** | Matched against the transcript. Resolved questions marked answered; unresolved questions auto-carried to the next appointment's prep. | Tap any question to see the doctor's response (or tap "carry forward" if unresolved) |
| **Adapted shares** | Preview cards per circle role: full for partner, abridged for adult children, one-liner for friends group. | Tap "Send" per card |
| **What was missed** | If the transcript suggests the patient missed something important (e.g., a medication change Mara visibly didn't register), it's surfaced as a distinct "you may have missed this" callout | Tap to expand |

### JTBDs served

This path touches two of the one-pager's three committed JTBDs **in a single flow**:

- **#1 Hold the story** — the summary, the action items, the matched questions are the story made operable
- **#2 Share without burden** — the adapted shares land as part of the cascade, not as a separate task

### Pipelines

**Existing (from direction-c)**:
- `summarize_worker` (creates the summary)
- `extract_worker` (pulls medications, conditions, action items)
- `adapt_worker` per viewer role (for the share cards)
- `translate_worker` (if any circle member uses a different language)

**New**:
- `appointment_detector_worker` — extracts appointment references with structured `(date, provider, reason)` triples; cross-references with patient calendar for conflicts
- `action_items_structured_worker` — action items with `(trigger, timing, source_event_excerpt, urgency)`; this is an extension of `extract_worker` but typed specifically for actionable items
- `pre_question_matcher_worker` — compares pre-visit questions (stored in `open_questions.md` of the wiki) against the transcript, marks resolved/unresolved
- `share_list_suggester_worker` — reads the care graph, suggests who to send what level of share to (defaults + patient customization)

### New UI surface

**The Post-Appointment Cascade screen** — the single most important new surface in Tier 1.

Structure: one scrollable screen, four stacked cards, each card is a single tap from commit.

```
┌────────────────────────────────────────────────────┐
│  Your appointment with Dr. de Jong                  │
│  April 4, 2026  ·  [tap to read full summary]      │
├────────────────────────────────────────────────────┤
│  📅  Next appointment                               │
│  May 2, 10:30  ·  Dr. de Jong, UMCG                 │
│  [Book] [Remind me later]                           │
├────────────────────────────────────────────────────┤
│  ✓  Your plan                                       │
│  • Start oxaliplatin Monday                         │
│  • Avoid cold drinks for first week                 │
│  • Call clinic if nausea above 7/10                 │
│  [Add to my plan]                                   │
├────────────────────────────────────────────────────┤
│  ?  Your questions                                  │
│  ✓ Why the switch?                                  │
│  ✓ Side effects?                                    │
│  ○ How long until I know it's working?  [Carry →]  │
├────────────────────────────────────────────────────┤
│  💌  Share                                          │
│  ┌─ Hans ──────────────┐  Full summary [Send]      │
│  ┌─ Sanne ─────────────┐  Softer version [Send]    │
│  ┌─ Friends ───────────┐  One-liner [Send]         │
└────────────────────────────────────────────────────┘
```

### Architectural notes

- The cascade is NOT a new mega-pipeline. It's a *surface* that reads from the graph/wiki, where each section is populated by an independent typed pipeline triggered on `recording.completed`. Keeps the plugin architecture discipline.
- Every item on the cascade screen has a `source_event_id`. Tap any claim, see the transcript excerpt. This is the trust architecture in the master synthesis Section 7.
- Low-confidence extractions are marked "please confirm" rather than silently auto-filled. Nothing on the cascade screen is executed without a single user tap.
- This is also the best end-to-end demo for every stakeholder (board, Series A, new hire). If Tier 1 is "the cascade works," the thesis is shippable.

### Missionary line

*"I left the oncology clinic, opened Ditto, and 90 seconds later my next appointment was booked, my action list was set, and my husband and daughter had their own updates. Everything I would have forgotten was already handled."*

---

## Path 2: Symptom Tracking via Voice

### Scene

Jan, 74, sits at his kitchen table most mornings with coffee. He taps the voice button on Ditto. "My knee was stiff again when I got out of bed. Worse than yesterday. The vertigo was better though, not much dizzy today." Thirty seconds. Done.

A week later, before his cardiology appointment, Jan opens Ditto and sees a simple chart: knee stiffness trending up over 10 days, vertigo trending down. The chart has three vertical dashed lines marking the days his medication was adjusted. He brings this to his cardiologist. She looks at it for five seconds and adjusts his beta-blocker dose. He didn't have to remember anything.

### What happens

- Patient initiates a voice check-in (zero-friction: one tap, one sentence, one tap to send)
- `symptom_extractor_worker` structures the utterance into typed symptom logs
- Each symptom becomes a time-series data point in the patient's wiki
- A visualization surfaces the trend: per symptom, per week/month
- `symptom_pattern_worker` runs weekly; detects correlations (symptom trending with medication change, for instance)
- The pattern is carried forward into the next appointment's prep briefing automatically

### JTBDs served

- **#1 Hold the story** — extended to include self-reported data between appointments, not just at them
- **#3 Catch what fragmented care misses** — patterns that individual doctors, seeing snapshots, can't detect

### Pipelines

**Existing**:
- `voice_input.received` event (already in direction-c)
- `extract_worker` (base extraction)

**New**:
- `symptom_extractor_worker` — tuned against a finite symptom ontology (fatigue, pain, nausea, cognitive, mood, sleep, etc.) with typed severity (0–10 or qualitative scale), body-region tags, and qualifier tags (morning/evening, triggered/spontaneous)
- `symptom_visualization_worker` — generates chart specs (rendered client-side); not an LLM call per view, but a deterministic pipeline that structures the underlying data
- `symptom_pattern_worker` — scheduled weekly; correlates symptom trends with medication changes, appointments, and other events in the wiki timeline
- `symptom_prep_hook` — extension of `prep_worker` that pulls recent symptom trends into pre-appointment briefings

### New UI surface

**The Symptoms tab** — one primary voice button ("How are you today?"), a timeline/chart beneath.

- One-tap voice is the primary input
- Quick-tap scale is the escape hatch (for cognitive decline, low-energy days)
- Timeline view shows last 30 / 90 days per symptom
- Tap any data point to hear the original voice note + see the transcript
- Patterns card at top ("You've reported knee stiffness 6 of the last 7 days. Trending worse.")

### Architectural notes

- The symptom ontology must be a finite, versioned schema. Not free-form. This is what makes the data comparable over time and supports visualization.
- Confidence scoring per extraction; below threshold → confirmation card before the symptom is logged. Silent wrong logging is a trust-breaker.
- Pattern detection is a scheduled pipeline that reads the wiki's `symptoms/timeline.md` page, not a similarity query. Consistent with the "similarity is an escape hatch" principle.
- Symptoms flow into `prep_worker` so the next appointment's briefing shows them (Path 2 → Path 1 handoff).

### Missionary line

*"I talk to Ditto most mornings. Last week it showed me my knee has been getting worse since the medication change. I brought the chart to my cardiologist. She saw the pattern in seconds."*

---

## Path 3: Inbound Reaction Loop — "Receive Care Without Awkwardness"

### Scene

Leila, 55, just shared the news about her MS progressing. Within hours, twenty people have sent messages. Her husband brought dinner. Her daughter called from London. Her colleague offered to cover her Friday meeting. Her neighbor dropped off homemade bread.

In WhatsApp, this would be chaos — "sending hugs" messages mixed with insurance spam, dinner offers lost in a thread with her book club, her brother's well-meaning but tone-deaf "have you tried diet?" next to her mother's prayer. She'd spend Sunday night trying to respond to everyone and failing.

In Ditto, she opens the Circle tab. Twenty reactions, curated. Six concrete help offers with single-tap accept. Four people asked to call — each one scheduled directly to a slot that works for both of them. Every message held; every offer actionable.

### What the one-pager missed

The one-pager committed to JTBD #2 as "Share without burden." This path reveals the second half of that job: **sharing creates reactions, and reactions need a home, too.** Today, the replies to shared summaries land in WhatsApp, where they get lost in the noise.

This is a close extension of JTBD #2, not a new fourth job (we don't expand the one-pager's committed three — the Lenny panel would not allow it). The refinement: **JTBD #2 is "the family is in sync, in both directions, without burden."**

### What happens

1. Circle member receives an adapted share (via Path 1's cascade).
2. Inside the shared view, they see a guided reply flow — not a blank text box, but three options:
   - A heartfelt message (free-form OR one of three tone-appropriate suggestions composed by `reaction_framing_worker` based on the news context)
   - An offer of help (structured categories: transport · meals · company · childcare · errands · free-form)
   - A "call me" CTA that opens calendar slot matching
3. The reaction is routed through `reaction_inbox_worker` into the patient's wiki inbox.
4. The patient opens Ditto's Circle tab. Each reaction is a card: sender, tone, message, optional help offer, optional call-me CTA.
5. Patient can: thank with one tap, accept a help offer (opens mini-scheduling flow), accept a call invitation (`scheduling_assistant_worker` negotiates a mutual slot), or archive.
6. The sender gets a matching card back when the patient accepts ("You're bringing Leila dinner Thursday. Here's the address.").

### JTBDs served

Extends #2 (Share without burden) into bidirectionality. Also serves an underlying emotional job the 45-list catches only indirectly: *"receive care from the people who love me without losing it in the noise."*

### Pipelines

**Existing (reused)**:
- `adapt_worker` (for the outbound share that triggered the reaction)
- `translate_worker` (if circle member uses different language than patient)

**New** (most of this path is architecturally net-new):
- `reaction_framing_worker` — when a circle member is composing a reaction, generates 2–3 tone-appropriate message suggestions based on the news context and the relationship (partner, adult child, friend, colleague)
- `reaction_inbox_worker` — routes incoming reactions into the patient's wiki inbox with typed metadata (sender, tone, has_help_offer, has_call_request)
- `help_offer_worker` — structures offers into typed categories with optional logistical fields (when, where, for how long, scope)
- `scheduling_assistant_worker` (agentic) — handles "call me" CTAs: finds mutual calendar slots (patient + sender), proposes times, confirms
- `reaction_digest_worker` — if many reactions arrive in a window, bundles them into a digest card so the patient isn't overwhelmed ("Twenty people reacted. Six offered help. Read all / summarize / accept all / triage")

**New event types**:
- `circle.reaction_received`
- `help_offer.received`
- `help_offer.accepted` / `help_offer.declined`
- `call.scheduled`

**New wiki page types**:
- `inbox/reactions/*.md` (one per reaction)
- `inbox/help_offers.md` (the offer queue)
- `inbox/scheduled_calls.md`

### New UI surface

**The Circle tab** on the patient side — a sacred channel, reserved for the health journey. Insurance spam, holiday greetings, and Ditto reactions do not mix.

```
┌────────────────────────────────────────────────────┐
│  Circle                                             │
│  Today: 6 new reactions · 2 help offers · 1 call    │
├────────────────────────────────────────────────────┤
│  💌 Hans (partner)                                  │
│     "I love you. Dinner tonight, anything you want."│
│     [Thank Hans] [Accept dinner]                    │
├────────────────────────────────────────────────────┤
│  💌 Sanne (daughter, London)                        │
│     "Mum. I'm here. Can we talk tonight?"           │
│     [Thank Sanne] [📞 Pick a time]                  │
├────────────────────────────────────────────────────┤
│  🤲 Marta (neighbor)                                │
│     "I can drive you to appointments this month."   │
│     [Thank] [Accept: schedule rides]                │
├────────────────────────────────────────────────────┤
│  💌 Yusuf, Jenny, Pieter, Anne, +16 more            │
│     [Read all] [Summarize] [Thank each with love]   │
└────────────────────────────────────────────────────┘
```

On the **circle member's side**, a matching surface: a guided reaction flow inside the shared summary (not a WhatsApp share-out). When the patient accepts their offer, they see a confirmation card.

### Design discipline

- **Sacred channel.** Never mix with unrelated notifications.
- **Guided but not scripted.** Suggestions are optional. Free-form is always available.
- **Bilateral confirmation.** Help offers are agreements: both sender and patient see the confirmed state.
- **Tone-aware.** A reaction to "my cancer is progressing" is composed differently than a reaction to "my medication is changing." `reaction_framing_worker` understands the emotional weight of the news.
- **Privacy by default.** Reactions are private between sender and patient. The patient can choose to surface a help offer to the wider circle ("Hans is bringing dinner Thursday, anyone want to join?").
- **Cognitive-decline-aware.** If the patient is on the cognitive-adaptation projection, the Circle tab simplifies radically: fewer cards, bigger tap targets, read-aloud on every message.

### Architectural notes — why this is the biggest unlock

Path 3 is architecturally significant because it **flips the graph direction.**

Today, in direction-c:
- Events flow from the patient (recordings, documents, voice) into the graph
- Shares flow outward from the patient to circle members
- Circle members are passive recipients

Path 3 adds:
- Circle members generate events (reactions, help offers, call requests)
- These events flow into the patient's graph
- The circle becomes active participants, not broadcast targets

This is where the care graph becomes a real network, not a broadcast list. **Every reaction, every help offer, every scheduled call increases graph density.** The moat thesis in the one-pager — "median active oncology patient has ≥2 circle members actively reading adapted shares weekly" — becomes much easier to achieve when circle members have a reason to come back (not just to receive, but to offer), and it becomes measurably stronger.

If the care-graph moat thesis is right, Path 3 is the #1 growth lever in the product. It should be treated with that level of seriousness.

### Missionary line

*"After I told my family about my MS progression, twenty people reacted. In WhatsApp they would have been lost in spam. In Ditto they were held — each one visible, each one answered, and six people offered help in ways I could actually accept."*

---

## What This Reveals About the Architecture

### New pipelines (consolidated)

| Pipeline | Path | Existing / New |
|---|---|---|
| `appointment_detector_worker` | 1 | New |
| `action_items_structured_worker` | 1 | New (extension of extract) |
| `pre_question_matcher_worker` | 1 | New |
| `share_list_suggester_worker` | 1 | New |
| `symptom_extractor_worker` | 2 | New (extension of extract) |
| `symptom_visualization_worker` | 2 | New (deterministic) |
| `symptom_pattern_worker` | 2 | New (scheduled) |
| `reaction_framing_worker` | 3 | New |
| `reaction_inbox_worker` | 3 | New |
| `help_offer_worker` | 3 | New |
| `scheduling_assistant_worker` | 3 | New (agentic) |
| `reaction_digest_worker` | 3 | New |

### New event types

`appointment.suggested` · `action_item.created` · `pre_question.matched` · `symptom.logged` · `circle.reaction_received` · `help_offer.received` · `help_offer.accepted` · `help_offer.declined` · `call.scheduled`

### New wiki page types

`inbox/reactions/*.md` · `inbox/help_offers.md` · `inbox/scheduled_calls.md` · `symptoms/timeline.md` · `appointments/pending.md` · `plan/active.md`

### New UI surfaces

- **Post-Appointment Cascade** (Path 1) — the Tier 1 anchor surface
- **Symptoms tab** (Path 2) — the between-appointments daily-active surface
- **Circle tab** (Path 3) — the bidirectional-graph surface, the moat-activation surface

### Where each path sits in the capability map

| Path | Capability tier fit | Why |
|---|---|---|
| Path 1 | Tier 1 anchor | Mostly extensions of existing pipelines; agentic scheduling is optional-v1; shippable end-to-end |
| Path 2 | Tier 2 | Requires the wiki projection layer and pattern detection to be mature |
| Path 3 | Mixed: Tier 1 for inbox + guided replies; Tier 2 for agentic scheduling | The graph-density bet lives here |

---

## What this implies for the one-pager

The one-pager stays committed as-is, with two refinements:

1. **JTBD #2 reframed as bidirectional.** "Share without burden" becomes "the family is in sync, in both directions, without burden." Outbound and inbound are one job.
2. **Path 1 promoted to Tier 1 anchor experience.** Tier 1 is organized around shipping the Post-Appointment Cascade cleanly. It's the single flow that demonstrates the thesis in 90 seconds and is the best end-to-end demo for every stakeholder.

No change to the moat thesis, the PMF proxy, or the retention commitment. Path 3's graph-density argument actually *strengthens* the one-pager's moat thesis — it names the mechanism by which density is produced.

---

## Adding more paths (template)

Any future magic path gets added as a new section with this exact structure:

1. **Scene** — a specific protagonist in a specific moment
2. **What happens** — the step-by-step flow
3. **JTBDs served** — mapping to the one-pager's three (or an explicit note if it reveals a gap)
4. **Pipelines** — existing reused + new required
5. **New UI surface** — if any
6. **Architectural notes** — what's structurally interesting
7. **Missionary line** — the user's own words about the experience

Candidates for Path 4 and beyond (not committed, just noted for future work):

- **The Crisis Handoff** — patient is incapacitated; circle takes over coordination
- **The End-of-Treatment Transition** — moving from active treatment to survivorship; scan anxiety, identity shift
- **The New Specialist Onboarding** — bringing a new doctor into the patient's story without starting from zero
- **The Caregiver Self-Care Path** — circle members' own wellbeing is affected; a version of the wiki for them
- **The Ambient Appointment Prep** — the day before a visit, surfaces arrive passively (notifications, widget updates) without the patient opening the app

Each one deserves the full treatment when it comes up.

---

Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
