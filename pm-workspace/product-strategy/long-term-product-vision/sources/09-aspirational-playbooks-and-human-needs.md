# Aspirational Playbooks & the Human Needs of the Seriously Ill

> My analysis and a research approach, prompted by the [board inputs](./board-meeting-input-2026-06-03.md). Two questions the board raised: (1) what underlying human needs do seriously ill people have that Ditto could serve, and (2) how did category-defining companies approach vision vs wedge, and functional excellence vs unlocking an overlooked need. Built by Mewtwo, 2026-06-04. **This is analysis + approach, not a finished researched report.** The deep dives are scoped in Part 6. Where I assert company history, treat it as directionally right and verify-before-citing (the founding myths are unreliable — see Part 6).

## The real question

Two threads from the board, and they are the same question from two sides:

- **Depth.** If Ditto serves only functional information needs ("did I take my meds," "is this normal"), it stays shallow and commoditizable. The foundation labs already answer those at billion-user scale. What deeper need earns "do not want to live without"?
- **Frequency.** The unlock is daily-to-weekly use. What recurring behavior carries that need?

The category-definers resolved exactly this tension. The pattern, stated up front:

> **A functional wedge that is 10x better than the alternative gets you used. An emotional or identity need gets you loved. A recurring behavior is the bridge between the two.**

Functional is the door. Emotional is the moat. Frequency is the hinge. Merlijn's "functional vs emotional" is not an either/or — it is a sequence. The winners lead with a functional wedge *because* it is the cheapest way to earn the right to serve the deeper need.

## Part 1 — The functional vs emotional lens

This maps cleanly onto a framework already in our corpus (the four layers of patient need + Antonovsky's Sense of Coherence, in `specs/ideas/activation-and-audience/`). Worth reusing rather than reinventing.

| Layer | The need | Example | Who serves it today | Can a lab copy it? |
|---|---|---|---|---|
| **Informational** | Understand what is happening | "What does this diagnosis mean?" | ChatGPT/Gemini/Google, portals | **Yes, already.** Commoditized. |
| **Psychological** | Manage fear, regain control | "Is what I feel normal? What is next?" | Fragmented; some Q&A | Partly — but needs *your* context + continuity |
| **Relational** | Be supported without exhausting everyone | "Tell the story once; let people help" | WhatsApp + a shared doc; CaringBridge | **No** — needs the care graph, the labs build for one person |
| **Existential** | Meaning, dignity, not being a burden, legacy | "Who am I through this? Will I be remembered?" | Almost no one | **No** — earned only through trust + relationship |

The strategic read: the labs own layer 1 and are climbing into layer 2. Ditto's defensible ground is layers 2–4, reached through the relationship and the accumulated context the labs structurally cannot hold. Functional comprehension is the entry ticket, not the business.

## Part 2 — Underlying human needs of the seriously ill (hypotheses to test)

These are **my hypotheses**, not findings. They are the input list for the user research in Part 6. Framed for oncology and neuro (Parkinson's, dementia), where the journey is long and high-intensity.

| Human need | What it sounds like | Functional surface Ditto could own | Why the labs can't easily serve it |
|---|---|---|---|
| **Control / agency in chaos** | "Everything is happening to me; I have no grip" | The single overview: what happened, what is next, what changed | Requires longitudinal, cross-provider context |
| **Tell the story once** | "I am exhausted re-explaining to everyone" | Audience-adapted share; the circle | A relationship graph, not a chatbot |
| **Calibrate fear** | "Is this normal, or should I worry?" | Context-aware answers grounded in *your* record + credible sources | Needs your data + trust, not generic answers |
| **Not being a burden / reciprocity** | "I hate asking; I want to give back too" | Let the circle help with structured tasks | Multi-person by design |
| **Being seen / witnessed** | "Does anyone understand what this is like?" | Peer connection; circle reactions | Social layer the labs don't build |
| **Realistic hope & meaning** | "I need hope that isn't a lie" | Journey framing, milestones, progress | Editorial + emotional craft, earned trust |
| **Continuity / legacy** | "Will this be remembered? Who tells my story?" | The journey record itself | Deep trust + permanence |
| **Caregiver: competence + permission to rest** | "Am I doing enough? Can I breathe?" | Caregiver mode: shared load, task allocation | The caregiver-as-user the labs ignore |
| **Neuro: identity & dignity through decline** | "I am becoming someone I don't recognize" | Memory aid, role-reversal support | Slow, relational, deeply personal |

The sharp filter for prioritization: **depth × frequency × can-the-labs-copy-it.** A need that is deep, recurs daily-to-weekly, and is structurally hard for OpenAI to serve is Ditto's wedge candidate.

## Part 3 — Category-defining playbooks

For each: the overlooked asset or unmet need they unlocked, whether they were vision-first or wedge-first, the functional-vs-emotional balance, and the frequency engine. The board named the first four; the last three are mine, chosen for their fit to Ditto's exact problem.

| Company | Overlooked asset / unmet need | Vision-first or wedge-first | Functional entry → emotional moat | Frequency engine |
|---|---|---|---|---|
| **Airbnb** | Underutilized assets (spare rooms) + a different need than hotels (belong, live like a local, afford it) | **Wedge-first.** Air mattresses at a sold-out conference (2008). "Belong anywhere" articulated ~2014, after the fact | Cheap place to crash → identity ("belong anywhere") | Episodic, but trip-anticipation + host income |
| **Uber** | Latent supply (idle drivers) + removal of a friction so total it reset expectations | **Wedge-first.** Premium black cars for the founders' own convenience (2010) → UberX mass-market (2012) | Push a button, a car comes → control, never waiting in the rain | Weekly-ish; habit through reliability |
| **Spotify** | A real unmet need between two bad options: CDs (expensive, can't explore) and piracy (free, terrible UX) | **Thesis-first, product-narrow.** Clear early thesis (beat piracy with better-than-free), narrow product first | Instant access to all music → "the soundtrack of my life," identity via playlists | **Daily.** Music is a daily behavior |
| **Headspace / Calm** | An ancient practice (meditation) nobody had made a daily, secular, bite-sized habit | **Mission-ish, product-narrow.** Puddicombe's live events → app (2012); mission clear, product expanded | Guided 10-minute sessions → calm, sleep, mental-health identity | **Daily**, latched onto sleep and stress |

My three, chosen because each solves a problem Ditto literally has:

| Company | Overlooked asset / unmet need | Vision vs wedge | Functional → emotional | Why it's the right parallel |
|---|---|---|---|---|
| **Strava** | The latent social graph of athletes + the need for recognition and accountability | **Wedge-first.** A GPS logging tool for cyclists (2009); segments/leaderboards turned it into a network | Track your ride → "if it's not on Strava it didn't happen," identity + belonging | This is the board's **Route-E reframe**: a logging tool becomes a social/identity layer. Shows how a *care* circle becomes a recognition layer, not a share button |
| **Duolingo** | A high-intent but episodic goal (learn a language) that nobody had engineered into a daily habit | **Mission-first, mechanic-narrow.** Free-education mission; one functional loop, gamified | A lesson → streaks, identity ("I'm a learner"), guilt-as-glue | This is the board's **frequency problem**: how to manufacture daily frequency for an inherently episodic goal. The most direct lesson for Ditto's wound |
| **Oura** | Passive biometric data nobody had turned into a daily meaning-making ritual | **Product-first.** A sleep ring (2015); the "Readiness Score" became the ritual | Raw HRV/sleep data → a daily "how am I" verdict you check every morning | This is the board's **wearables × medical-context** input: plain data becomes a daily ritual only when it's turned into meaning. Ditto's version is data-in-medical-context |

**Healthcare-specific precedents worth a hard look** (not consumer giants, but directly on-point):
- **Flo** (already in our corpus, source 04): owned *one* life moment (the cycle), nailed the daily log, expanded across the female-health journey. The closest existing template for "own oncology-on-treatment first, then expand."
- **PatientsLikeMe**: a peer-support network for the seriously ill that monetized de-identified RWD to pharma. A direct precedent for both the **Route-E social platform** and the **pharmacy/pharma RWD** monetization the board raised — *and* a cautionary tale on data-as-business and privacy backlash. Study what worked and what broke.
- **Revolut** (in our corpus, source 04): the "no consumer product for X" wedge that banking had and healthcare doesn't.

## Part 4 — The pattern across all of them

Three things are consistent; one common belief is wrong.

1. **The grand vision was almost always articulated *after* the wedge worked, not before.** Airbnb's "belong anywhere" and Spotify's "soundtrack to your life" are post-hoc articulations of why a narrow product caught fire. The honest answer to the board's question ("was it from a long-term vision, or build now and expand?") is: **build now and expand — but the winners could name, early, the one overlooked asset or unmet need they were unlocking.** Vision is the *why*; the wedge is the *how*. Leading with the vision as a build plan is the trap.
2. **Every one of them was 10x better than the real alternative for a narrow group** — and the real alternative was usually not the obvious competitor. Airbnb's alternative wasn't hotels, it was "couch surf or can't afford the trip." Spotify's was piracy, not iTunes. Ditto's alternative is not other health apps; it is **Google + calling your daughter.**
3. **Functional excellence was the entry; an emotional or identity need was the moat.** None of them retained on utility alone.
4. **The frequency was engineered, not assumed.** Daily behaviors were either inherent (music, sleep) or manufactured (streaks, readiness scores, leaderboards). For an episodic goal, frequency is a *design problem* (Duolingo), not a reason to give up.

## Part 5 — What this implies for the current five routes

Flagged for Merlijn's synthesis, not a rewrite of the vision:

- **A sixth route is emerging:** the *trusted, context-aware answer engine* ("ChatGPT with your record"). It is the board's clearest articulation of "go to Ditto instead of Google." It overlaps Routes B and D but deserves to be named and scored on its own.
- **Route E should be reframed** from "family network" to "social care platform with peer support" (the Strava lesson). Peers, not only your own family.
- **Route A should be reframed** as a single "Care OS" with a patient mode and a caregiver mode, rather than caregiver-only.
- **Route B should absorb** proactive nudges/guidance ("on-call for health").
- **The wearables × medical-context idea is a new frequency engine candidate** that could sit inside A or C (the Oura lesson), and it carries an MDR flag.
- **The North Star idea** ("50% of newly-diagnosed NL oncology patients use Ditto within a week") is an *adoption-depth* metric for a life moment — a strong complement to Core MAU, and more honest about what winning the wedge looks like.

## Part 6 — Recommended research approach

Two workstreams. Each has a clear deliverable and a clear owner-tool. The decision both serve: **which need × which frequency mechanic × which unlocked asset is Ditto's wedge?**

### WS1 — The human needs of the seriously ill
- **Method:** Jobs-to-be-Done (functional / emotional / social jobs) on oncology and neuro patients *and* their caregivers, layered on the four-layers + Sense-of-Coherence frame we already have.
- **Sources:** the `user-researcher` agent against the Ditto User Insights NotebookLM notebook first (cheap, fast), then a small set of targeted interviews to fill gaps NotebookLM can't.
- **Output:** a needs map ranked by **depth × frequency × can-the-labs-copy-it**, naming the 2–3 wedge-need candidates.

### WS2 — The category-definer playbooks (deep, verified)
- **Method:** the `deep-research` harness on the **early history** (first 2–3 years) of the seven companies, with adversarial verification — these histories are myth-laden, so separate the founding story from what actually drove early traction and retention.
- **Questions per company:** what was the literal first wedge? what overlooked asset/need did it unlock? when and how was the long-term vision articulated relative to traction? what was the frequency mechanic, and was it inherent or engineered? what was the *real* alternative they beat?
- **Output:** a "wedge → vision" pattern doc and a Ditto-specific playbook recommendation (our wedge, our 10x-better-than-Google claim, our engineered frequency, our unlocked asset).

### Sequencing
WS1 and WS2 are independent and can run in parallel. WS1 tells us *which need*; WS2 tells us *how to package it into a habit*. They converge on the wedge decision, which then pressure-tests the six routes.

**I can kick off either or both on your go** — WS2 via the deep-research harness now, WS1 via the user-researcher agent. Say the word and I'll scope the exact prompts.
