# ditto — Two Prototype Options: Overview & Comparison

**Prepared:** 2026-06-16 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Purpose:** frame the two prototype directions the team is evaluating, the non-negotiables they share, and neutral criteria to decide between (or sequence) them. Specs: [Prototype A](prototype-A-grounded-contextual-chat/spec.md) · [Prototype B](prototype-B-voice-daily-note/spec.md). Research: [A](prototype-A-grounded-contextual-chat/research.md) · [B](prototype-B-voice-daily-note/research.md).

> Grounding: both options are a way to *start* building ditto's "Living Health Companion" daily loop — the strategy from [`reused/13`](../research/market-research/reused/13-synthesis-final.md) ("build = one loop": daily check-in → the circle → reframed summary) and the moat stack from [`reused/14`](../research/market-research/reused/14-moat-and-platform-strategy.md). Both lean on the **innovate-the-intelligence-layer** mechanics from [`S3`](../research/market-research/synthesis/S3-proven-mechanics-playbook.md) / [`M17`](../research/market-research/findings/M17-table-stakes-mechanisms.md).

---

## The two options in one line each

- **A — Grounded contextual chat that "turns into interface."** Ask anything about *your* care; get a grounded, cited, no-advice answer that renders as **savable action pills + clickable resource cards**, with intelligent due-dates. *The "understand & act on my care" wedge.*
- **B — Voice-first "ditto today" daily note.** Open the app, ramble; ditto **listens calmly and structures it live** into minimal pills (symptoms, meds, mood, actions, updates), then offers what to do with it. *The "capture my day at zero energy" wedge.*

## How they map to the strategy

| | Prototype A (chat → interface) | Prototype B (voice daily note) |
|---|---|---|
| Roadmap loop element `[reused/13]` | The **reframed summary** + understanding layer; pulls the appointment forward ("walk in prepared, walk out understanding") | The **daily check-in (habit engine)** — the part that builds frequency, data moat, and the caregiver feed |
| Primary mechanics `[M17]` | #8 grounded-&-cited · #1 anticipatory answer · #7 contextual nudges · #5 compounding data | #10 voice (input) · #2 passive/low-effort capture · #1 anticipatory · #5 compounding data · #4 caregiver sharing |
| ditto-novel piece (the differentiation) | **Generative UI**: chat renders savable action pills + cited cards; **intelligent due-date extraction** | **Live speech → fact-extraction pills**; calm, interface-abstracted capture |
| Frequency | Episodic-to-frequent (around questions/appointments) | **Daily/weekly** by design — the stronger habit substrate |
| Retention risk | Lower novelty risk; risk is "nice utility, not a daily habit" | Higher: voice-journaling/logging churns hard unless effortless + rewarding (see research B) |
| Hardest unknowns | Grounding safety + context plumbing + does generative-UI feel intelligent | STT quality/latency/privacy + does live extraction feel calm not creepy + zero-energy retention |

## Shared non-negotiables (both prototypes must hold these)

1. **No medical advice / non-device.** Clarify, explain, organize, reflect — never diagnose/triage/treat. Stay outside MDR for the prototype (the deliberate posture in `reused/13`; the cautionary tales — Babylon, Woebot, Ash's UK exit — in [`M14`](../research/market-research/findings/M14-ai-mental-health-therapy.md)/[`M15`](../research/market-research/findings/M15-winners-losers-why.md)).
2. **Grounded & refuse-when-unsure.** Answers grounded in the patient's own record + trusted sources, with honest uncertainty and "see your clinician" routing. ~5–13% of unguarded LLM answers to patient questions are unsafe `[M11]` — this is the bar.
3. **EU-native trust.** GDPR-grade consent, EU data residency, AI Act transparency — the moat US incumbents can't cross today (`M11`, `M13`). Crisis routing to humans (esp. B).
4. **Caregiver-as-co-user.** Both should be shareable to the circle on consented proxy rails — the empty market cell (`M4`).
5. **Effortless.** Designed for low energy, low literacy, older users — minimal taps, voice-friendly.

## Neutral decision criteria (for the team)

- **Which job is more urgent & frequent** for the beachhead cohort (newly-diagnosed + caregiver)?
- **Which is more defensible** — A leans on grounding+context (white space, but compute/safety heavy); B leans on the habit/data moat (stronger long-term, harder to retain).
- **Which de-risks the riskiest assumption fastest** — A tests "will patients trust & act on a grounded companion"; B tests "will the seriously ill open a daily app" (the unresolved frequency hypothesis, `reused/13 §5`).
- **Build cost / time-to-testable** — A is mostly LLM + UI; B adds real-time STT + live-extraction UX complexity.
- **They are complementary, not exclusive:** A is the *answer/act* surface, B is the *capture/reflect* surface; the daily note (B) feeds the data that makes the chat (A) more contextual. A sensible end-state runs both on one care graph (`reused/14` D4).

*This doc stays neutral on which to build first; each spec carries its own metrics and open questions so the team can decide from evidence. The two `research.md` files go a level deeper on what already exists for each.*
