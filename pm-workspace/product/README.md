# ditto — Product Prototypes

**Compiled:** 2026-06-16 · **Branch:** `claude/market-research-synthesis-ltz3lu`

Two prototype directions the team is evaluating to *start* building the "Living Health Companion" daily loop — each with a rough feature spec, the full set of open questions to answer before prototyping, and a deep, cited market-research doc. Built on the market-research corpus in [`../research/market-research/`](../research/market-research/) (esp. mechanisms `M17`, landscape `M11`/`M16`, playbook `S3`, strategy `reused/13`/`reused/14`).

## Start here

- [`00-overview-and-comparison.md`](00-overview-and-comparison.md) — the two options side-by-side, shared non-negotiables, neutral decision criteria.

## The two prototypes

| | Prototype A | Prototype B |
|---|---|---|
| **Name** | Grounded, context-aware chat that "turns into interface" | Voice-first "ditto today" daily/weekly note |
| **Wedge** | Understand & act on *your* care | Capture your day at zero energy |
| **Signature (novel) piece** | Generative-UI **savable action pills** + cited resource cards + intelligent due-dates | **Live speech → fact-extraction pills**, calm/input-first |
| **Spec** | [spec](prototype-A-grounded-contextual-chat/spec.md) | [spec](prototype-B-voice-daily-note/spec.md) |
| **Research** | [research](prototype-A-grounded-contextual-chat/research.md) | [research](prototype-B-voice-daily-note/research.md) |

## Headline findings

- **A — white space confirmed:** no engine is *patient + grounded + cited + aware of your **own record** + EU-available + no-advice*. OpenEvidence/Glass are clinician-only; ChatGPT Health is record-aware but EU-excluded; Perplexity/Comet are EU + cited but only web-context. Generative UI is proven tech but near-absent in patient health — the **application** is the innovation; the **dated, saveable action pill** is the true differentiator (chat-with-citations is becoming table-stakes). Due-date extraction is feasible but safety-fragile → anchor to the appointment timestamp, surface as an editable draft with the source snippet, never fabricate.
- **B — voice verdict:** the market splits into *input-only* (Wispr, Granola, AudioPen — winning commercially) and *intelligent/steering* (Rosebud, Sonia, Wysa — carrying the safety load). ditto's right lane is **"effortless input on the surface, intelligence underneath"** (AudioPen/Granola), *not* an AI therapist (Woebot shutdown, Ash UK exit). **Live extraction pills are genuine white space** but distraction is the core UX risk — keep them peripheral, edit at the summary. The 2025–26 shift is **user-initiated capture + retroactive structuring** (always-listening hit a privacy wall: Limitless/Bee wound down). Effortless-at-zero-energy is validated; voice is the strongest antidote to the logging effort-tax.

## Method & scope

External research only this round (no internal Mixpanel/Granola data — a noted fast-follow). No visual mockups this round (specs carry ASCII wireframes; HTML/Figma can follow once a direction is chosen). Sources tiered (T1/T2/T3) with US→EU flags in each `research.md`.
