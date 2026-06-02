# 04 · Path 3 — Inbound Reaction Loop

**Prereq**: `01-core-architecture.md`, Path 1 (the outbound shares come from the cascade). Schemas in `05-data-schemas.md`.

**Purpose**: Implement the bidirectional care graph. Circle members can react to shared summaries, offer concrete help, and request calls — all landing in a curated patient inbox with single-tap acceptance and agentic scheduling.

**Why this matters architecturally**: Paths 1 and 2 flow events FROM the patient. Path 3 flows events FROM circle members INTO the patient's graph. This is the mechanism that turns the care graph from a broadcast list into a real network. It's the #1 moat-activation surface in the product.

---

## User story

Leila (55) has just shared the news about her MS progressing to secondary-progressive. Twenty circle members receive adapted updates (via Path 1's adapt_worker). From inside Ditto, each of them composes a reaction — a heartfelt message plus an optional concrete help offer plus an optional "call me" request.

Leila opens Ditto's Circle tab. A curated inbox: each reaction visible as a card, each help offer actionable in one tap, each call request resolvable via an agentic scheduling flow that negotiates a mutual time. Nothing lost in WhatsApp noise. Messages landed with care.

---

## End-to-end flow

### Part A: Circle member composes a reaction

```
1. Circle member views their adapted share (rendered from a previous Path 1 flow)
2. Within the same view, a guided reply flow:
   - Heartfelt message (free-form OR one of 2-3 tone-appropriate suggestions)
   - Optional help offer (structured: transport / meals / company / childcare / errands / other)
   - Optional "call me" CTA (opens calendar slot picker)
3. POST /reactions
   Body: {
     patient_id,
     sender_circle_member_id,
     source_share_id,
     message: { text, tone_hint? },
     help_offer?: { category, scope, when?, where?, notes? },
     call_request?: { proposed_window, proposed_slots[] }
   }
4. Event `circle.reaction_received` emitted
5. reaction_inbox_worker runs (routes and enriches the reaction)
6. help_offer_worker runs (if help offer present — structures the offer, prepares acceptance flow)
```

### Part B: Patient opens the inbox

```
7. GET /patients/{patient_id}/inbox
   Returns curated reactions, help offers, and call requests — see API Shape below

8. Patient acts on items:
   - Thank a reaction: POST /reactions/{id}/thank
   - Accept a help offer: POST /help-offers/{id}/accept (+ optional scheduling)
   - Decline a help offer: POST /help-offers/{id}/decline
   - Accept a call request: POST /call-requests/{id}/accept → triggers scheduling_assistant_worker
```

### Part C: Agentic scheduling for calls

```
9. On POST /call-requests/{id}/accept:
   - scheduling_assistant_worker runs
   - Reads patient's availability (mock calendar for prototype)
   - Reads sender's proposed slots
   - Finds mutual slot (first fit or ranked)
   - Emits `call.scheduled` event
   - Writes ScheduledCall entity
   - Sends confirmation to both patient and sender (in-app card for prototype)
```

---

## Pipelines required

### Existing (reused)

- **`adapt_worker`** — used in Path 1 to produce the outbound shares. For Path 3, its output becomes the source_share for reactions.
- **`translate_worker`** — if sender and patient use different languages, translate the reaction message.

### New pipelines (Path 3)

**`reaction_framing_worker`**
- **Trigger**: called synchronously when a circle member opens the reaction composer (not event-driven); exposed via `GET /shares/{share_id}/reaction-suggestions`
- **Input**: the original adapted share content, the sender's relationship to the patient (role), the emotional weight of the news
- **Context mode**: filter (wiki: care circle page for sender; the share content)
- **Processor**: LLM-based (Sonnet). Generates 2–3 tone-appropriate reaction message drafts. Tone calibrated to the news weight — serious diagnosis gets serious suggestions; routine update gets warm-but-casual.
- **Output**: `ReactionSuggestion[]` (transient — not persisted to graph)
- **Side effects**: none (read-only)
- **Eval criteria**: given scenarios across emotional weights and relationships, produces suggestions that a human reviewer would rate appropriate 85%+ of the time. Adversarial test: do NOT produce suggestions that minimize serious news or catastrophize routine news.

**`reaction_inbox_worker`**
- **Trigger**: `circle.reaction_received`
- **Input**: the incoming reaction, patient's inbox state, sender's circle role
- **Context mode**: fact
- **Processor**: hybrid. Deterministic: typing, routing, enrichment (adds sender metadata, urgency tagging based on help_offer category). LLM: OPTIONAL tone-classification pass if the reaction is free-form (categorize into `warm`, `supportive`, `helpful`, `concerned`, `other`).
- **Output**: `Reaction` entity written to the graph; wiki page `inbox/reactions/{id}.md` created
- **Side effects**: `graph_write`, `wiki_write`, emits `reaction.inbox_updated`

**`help_offer_worker`**
- **Trigger**: `circle.reaction_received` (if reaction has `help_offer`)
- **Input**: the help offer, patient's current accepted help, care circle capacity
- **Context mode**: fact
- **Processor**: deterministic. Structures offer into canonical categories, dedupe-checks against pending offers, tags urgency.
- **Output**: `HelpOffer` entity with `status: pending`
- **Side effects**: `graph_write`, `wiki_write` (updates `inbox/help_offers.md`)
- **Eval criteria**: offers categorized correctly 95%+ on seeded test cases; no duplicate offers slip through dedup.

**`scheduling_assistant_worker`** (agentic)
- **Trigger**: `POST /call-requests/{id}/accept`
- **Input**: patient's mock calendar, sender's proposed slots, both time zones
- **Context mode**: fact
- **Processor**: agentic — deterministic core (slot intersection) wrapped in an LLM layer that can handle conversational tweaks if the first-fit slot is declined. For the prototype, the deterministic core is sufficient; the LLM layer is optional.
- **Output**: `ScheduledCall` entity with confirmed datetime, participants, optional meeting link placeholder
- **Side effects**: `graph_write`, `wiki_write` (updates `inbox/scheduled_calls.md`), emits `call.scheduled`, produces confirmation cards to both sides
- **Eval criteria**: given overlapping proposed slots, always finds a mutual fit. If no mutual fit exists, returns an honest "no overlap" with suggested alternate windows.

**`reaction_digest_worker`** (optional for MVP)
- **Trigger**: scheduled (daily at a patient-configurable time) OR when more than N reactions arrive in a window
- **Input**: recent unread reactions
- **Processor**: LLM (Haiku — summarization task). Produces a short digest: count by tone, standout messages, pending help offers summary.
- **Output**: a transient digest object (not persisted as a separate entity; surfaces in the inbox API response as a "digest" field)
- **Side effects**: none — read-only summarization
- **Skip for first prototype iteration if time-constrained**. The inbox API can ship without it.

---

## API endpoints

### For circle members

**`GET /shares/{share_id}/reaction-suggestions`**
- Returns 2–3 message suggestions from `reaction_framing_worker`
- Optional — the composer can also just show a free-text box

**`POST /reactions`**
- Input (see flow §A step 3)
- Validates sender_circle_member_id belongs to the patient's care circle (auth: patient_id scoping + circle member membership check)
- Emits `circle.reaction_received`
- Returns `reaction_id`

### For patients

**`GET /patients/{patient_id}/inbox`**
- Query: `since=ISO8601` (optional), `category=messages|help_offers|calls` (optional filter)
- Returns the curated inbox (shape below)

**`POST /reactions/{id}/thank`** / **`POST /reactions/{id}/archive`**

**`POST /help-offers/{id}/accept`**
- Body: optional `scheduling` if the acceptance requires a time to be confirmed (e.g., dinner Thursday vs. "anytime next week")
- Triggers a confirmation card back to the sender

**`POST /help-offers/{id}/decline`**
- Optional body: `reason` (nullable — sender sees only that it's declined, not why, unless patient explicitly opts in)

**`POST /call-requests/{id}/accept`**
- Triggers `scheduling_assistant_worker`
- Returns the scheduled time or a "no mutual slot" response with alternatives

**`POST /call-requests/{id}/decline`**

---

## Inbox API shape (example)

```json
{
  "patient_id": "...",
  "generated_at": "...",
  "digest": {
    "new_reactions_count": 12,
    "pending_help_offers_count": 3,
    "pending_calls_count": 1,
    "summary_text": "Today: 12 new reactions, 6 warm messages, 3 help offers, 1 call request from Sanne."
  },
  "reactions": [
    {
      "id": "...",
      "sender": { "id": "...", "name": "Hans", "role": "partner" },
      "tone": "warm",
      "message": "I love you. Dinner tonight — anything you want.",
      "received_at": "...",
      "has_help_offer": true,
      "has_call_request": false,
      "thanked": false
    },
    ...
  ],
  "help_offers": [
    {
      "id": "...",
      "sender": { "id": "...", "name": "Marta", "role": "neighbor" },
      "category": "transport",
      "scope": "rides_this_month",
      "message": "I can drive you to appointments this month.",
      "status": "pending",
      "actions": ["accept", "decline"]
    },
    ...
  ],
  "call_requests": [
    {
      "id": "...",
      "sender": { "id": "...", "name": "Sanne", "role": "adult_child" },
      "proposed_slots": [
        { "datetime": "2026-04-16T19:00:00Z", "duration_min": 30 },
        { "datetime": "2026-04-17T20:00:00Z", "duration_min": 30 }
      ],
      "message": "Mum, can we talk tonight or tomorrow?",
      "status": "pending",
      "actions": ["accept", "decline"]
    }
  ]
}
```

---

## The sacred channel rule

**Reactions are never mixed with other notification types.** The Inbox API returns ONLY reactions/offers/calls for this patient's health journey. Insurance spam, appointment reminders, ad-hoc app notifications — all separate surfaces.

Enforce this in the data model: the `Reaction`, `HelpOffer`, `ScheduledCall` tables have no `notification_type` discriminator. They are what they are. Any other app-level notification goes through a different API.

---

## Privacy rules (important)

- A reaction is private between sender and patient. No other circle member sees it unless the patient explicitly opts to surface a help offer to the wider circle.
- When the patient accepts a help offer, only sender + patient see the confirmation. If the patient wants to coordinate (e.g., "Hans is bringing dinner Thursday, anyone want to join?"), they take an explicit "make visible to circle" action.
- All reaction data lives in the patient's graph scope (enforced by patient_id isolation per `01-core-architecture.md`).
- A circle member can only POST a reaction to shares they have received (auth: membership check).
- Decline reasons are private to the patient by default. Only the fact of decline is visible to the sender.

---

## Wiki page types for Path 3

See schemas doc for full templates.

- `inbox/reactions/{reaction_id}.md` — one per reaction, contains the message, sender, metadata
- `inbox/help_offers.md` — list of pending/accepted/declined help offers
- `inbox/scheduled_calls.md` — list of scheduled calls with participant info
- Updates to `entities/care_circle/{member}.md` — each circle member's page shows their reaction/offer history

---

## Eval suite

Location: `/evals/reaction_loop/`

Minimum test cases:

1. **Simple warm reaction**: "Thinking of you, love." → `reaction_inbox_worker` categorizes `tone: warm`, no help offer, no call request.
2. **Reaction with help offer**: warm message + offer to drive to appointments this month → `HelpOffer` entity with `category: transport, scope: rides_this_month`.
3. **Reaction with call request**: "Can we talk tonight?" + two proposed slots → call_request parsed correctly.
4. **Full accept flow**: patient accepts a help offer → sender receives confirmation card.
5. **Scheduling flow**: patient accepts a call request with two proposed slots; patient's mock calendar has one of the slots free → `scheduling_assistant_worker` confirms that slot.
6. **No mutual availability**: patient's mock calendar has NO overlap with proposed slots → worker returns alternates, not a spurious confirmation.
7. **Reaction framing — serious news**: share describing cancer progression → suggestions are serious, not chipper.
8. **Reaction framing — routine update**: share describing a routine medication change → suggestions are warm-but-casual.
9. **Privacy test**: sender A's reaction to patient P is not returned in sender B's inbox-view (patient scoping + sender isolation).
10. **Sacred channel test**: inbox endpoint returns only health-related reactions — no cross-contamination with a mock "insurance reminder."

---

## Success criteria for Path 3

- [ ] `POST /reactions` accepts a reaction + help offer + call request and emits the event
- [ ] Inbox endpoint returns the full curated structure
- [ ] All four accept/decline/thank endpoints work and mutate state correctly
- [ ] `scheduling_assistant_worker` handles at least one end-to-end call scheduling case with a mock calendar
- [ ] Eval suite passes at thresholds
- [ ] Demo frontend has a minimal Circle tab view that renders the inbox JSON

---

## What you choose

- Whether to ship `reaction_digest_worker` in first iteration or defer (non-blocking)
- Exact tone-classification categories for `reaction_inbox_worker`'s optional LLM pass (agent picks ~4–6 categories; document them)
- Whether `reaction_framing_worker` uses strict templates or free-form generation (either is acceptable; evals will judge)
- How to mock circle-member calendars (a simple JSON file per member is fine)
- How "call me" logistics work — video link generation, phone number exchange, etc. For prototype, return a placeholder; note in repo README that real integration is follow-up work.

---

## What you do NOT have latitude on

- **Privacy**: no reaction leaks outside sender-patient pair. Enforced at the data layer.
- **Sacred channel**: the Inbox API surfaces ONLY health-journey reactions. No mixing.
- **Bilateral confirmation**: every help-offer acceptance / call-request acceptance produces a confirmation to both sides.
- **Grounding for framing suggestions**: `reaction_framing_worker` suggestions must be tonally appropriate to the source share's emotional weight. Do not produce generic suggestions without reading the share context.
- **Sender authentication** in the prototype: a sender's `circle_member_id` must match a member of the patient's care circle to POST a reaction. A hardcoded mapping is fine; no auth check is not.

---

## Out of scope for Path 3

- Real calendar integration (Google Calendar, etc.) — mock files are sufficient
- Real video call generation — return a placeholder meeting link
- Multi-party group chats (a reaction is always 1:1 — sender → patient)
- Real push notifications — in-app state changes are enough
- Payment or financial help offers (help categories are non-monetary for prototype)
- Coordination between multiple circle members on one help offer (e.g., "Hans and Marta both offered dinner Thursday") — simple first-come-first-served is fine

---

## Why Path 3 is architecturally net-new (context for the agent)

Paths 1 and 2 flow events from the patient INTO the graph. Path 3 flows events from circle members INTO the graph. This creates:

- New event types (`circle.reaction_received`, `help_offer.received`, `help_offer.accepted`, `help_offer.declined`, `call.scheduled`)
- New permission checks (sender must be in patient's circle)
- A new "outbound-from-the-graph" flow: confirmations back to senders
- A new category of wiki pages (inbox/*) that isn't about the patient's clinical data — it's about the relationships

Expect Path 3's implementation to reveal edge cases the architecture didn't fully anticipate (e.g., sender-side confirmation cards — how does a circle member see "you're bringing dinner Thursday"?). Note them in `/prototype/OPEN_QUESTIONS.md` as you find them.
