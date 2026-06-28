# PRD — Ditto Onboarding App

## Context & goal

New hires at Ditto land into a fast-moving startup with a lot of context in a lot of heads. The first month decides whether someone feels lost or feels at home. We want a single personalized place that carries a new hire through their first month: why they're here, how Ditto works, who their people are, what we expect, and the practical things that otherwise slip (accounts, the NS card, first coffees).

It should feel **high-energy, warm, and exciting**, not like an HR portal. It should not replace human contact; it guides someone on how to start as effectively as possible, and nudges them toward the team.

**The feeling we're designing for, at the end of month one:** *"I'm fully onboarded. I understand my role, why I'm here, and how I can contribute. I've already contributed. I feel connected to the team, and I'm excited for what's next."*

**Why remixable:** this is the first of many onboardings. The app shell is built once; each hire gets their own content file and their own URL. Changing content must never require touching the app.

## Users

| User | Need |
|---|---|
| **The new hire** (primary) | A warm, clear, motivating guide to their first month. Knows what to do, in roughly what order, and feels progress. |
| **The person who remixes it** (secondary — Merlijn / HR / a manager) | Spin up a new hire's journey by copying a content file and editing it. No code, no app rebuild. |

## Goals & success criteria

- A new hire can open their link on day one and immediately understand why they were hired and what their first month looks like.
- Per-chapter progress and the "on track" status give a felt sense of momentum.
- By the end of month one, all chapters are complete and the hire reports feeling onboarded (qualitative, confirmed in their first month-end 1:1).
- The hire logs feedback on the onboarding itself at least a few times (signal the loop works).
- A second hire can be onboarded by copying one folder and editing one file, with zero app changes.

## Core flows

1. **First open → intro flow.** A new hire opens their personal URL. They see a 3-view click-through: (1) the mission, (2) why this role exists, (3) why we hired *you* and what we hope you bring. It ends on "Ready to onboard?" → entering the dashboard. The intro flow shows once; afterwards it's re-openable from the dashboard but never blocks.
2. **Dashboard.** The home view: a warm hero (hire's name, role, a line from the founder), the 5 chapters as cards with per-chapter progress, the persistent Feedback chapter, and the "on track for your first week / month" status.
3. **Open a chapter.** Chapters can be done in any order. A chapter shows its items (tasks, actions, readings, resources), each with a horizon tag (Day 1 / Week 1 / Month 1) and a checkbox.
4. **Complete an item.** The hire checks it off. State saves to the backend immediately (by token). Readings either expand inline (short) or open a link (long/external); marking complete is still a self-check.
5. **Chapter celebration.** When the last item in a chapter is checked, fire a tasteful celebration: confetti, a warm on-brand message, and a visible bump to that chapter's status.
6. **Log feedback.** From the Feedback chapter, accessible anytime, the hire writes a free-form note (a gap, a task that felt irrelevant, an idea to improve onboarding). It saves to the backend for the team to read.

## Information architecture

- **Intro flow** — 3 views + a readiness prompt. Shown once.
- **Dashboard** — hero, chapter cards, on-track status, feedback entry point.
- **5 chapters** (browse in any order):
  1. **Land & Settle** — practicalities, accounts, the NS card, first coffees. "From team to family."
  2. **Get to Know Ditto** — mission, story, product, users, market, team, culture.
  3. **Understand Your Role** — why the role exists, why we hired you, what we hope you bring, and the honest current state of the brand.
  4. **Hit the Ground Running** — first concrete contributions in week one.
  5. **Shape & Deliver** — the first-month deliverables and how you'll own the role.
- **Feedback chapter** — always present, always accessible. Not part of the 5; it's a meta layer.
- **Item types:** `task` (do something, e.g. set up Slack), `action` (a softer prompt, e.g. have coffee with Niek), `reading` (in-app markdown or external link), `resource` (a link to keep). Every item carries a **horizon**: `day1` / `week1` / `month1`.

## Progress & gamification model

Deliberately light. It motivates; it does not turn a senior hire's first month into a video game.

- **Per-chapter progress.** Each chapter shows completed / total (and a progress bar). No single global "% onboarded" number.
- **On-track status.** Computed from horizon tags against days-since-start. Example logic: by end of day 1, Day-1 items should be done; by end of week 1, Week-1 items; by end of week 4, Month-1 items. The dashboard shows a friendly status like "On track for your first week" or "A couple of Week-1 things still open." Never punitive.
- **Celebration.** On completing a chapter's last item: confetti + a warm on-brand line + the chapter card flips to a "done" state. Tasteful, brief, not childish. Optionally a per-item micro-acknowledgement (a small check animation), no points or badges.

## Identity & persistence

- **No login.** Each hire gets a personal URL containing an **unguessable token** (e.g. `/o/8f3k2j9x...`, a long random slug). The token *is* the identity.
- **Backend store.** The token maps to one record holding the hire's progress and feedback. Progress persists across browsers and devices and never resets on reload.
- **Record shape:**
  ```json
  {
    "token": "8f3k2j9x...",
    "contentRef": "brand-lead",
    "completedItemIds": ["s1-accounts", "s1-ns-card", "..."],
    "introSeen": true,
    "feedbackEntries": [
      { "ts": "2026-06-23T10:14:00Z", "text": "Couldn't find the Figma invite." }
    ]
  }
  ```
- **Privacy.** Content is personal but low-sensitivity (a welcome note, task lists, public brand docs). The unguessable token is the only gate. Don't put anything in here that would be damaging if the link leaked. If needed later: expiry or rotation on the token, and keep real secrets (credentials) out of the content.

## Backend requirements

Minimal and build-agnostic. Any key-value store or a single Supabase table works.

- **Storage:** one record per token (shape above).
- **Two operations:**
  - `GET state(token)` → returns the record (or creates an empty one on first open).
  - `PATCH state(token, delta)` → toggles a completed item, sets `introSeen`, or appends a feedback entry.
- **Feedback view:** a simple internal way to read feedback across hires (a query, an export, or a basic admin page). No per-hire auth needed for v1; gate the admin view however the host platform makes easy.

## Content model / remix workflow

The app loads one content file per hire, identified by `contentRef`. The file's shape is defined in `content-schema.md`. To onboard a new hire: copy a content folder, edit the file, mint a token, send the link. See `README.md` for the step-by-step.

## Non-goals (v1)

- No authentication, accounts, or role-based access.
- No content authoring UI (remixing is editing a file).
- No analytics dashboard or reporting beyond reading feedback.
- No multi-language (April's content is English; Dutch can come later).
- No calendar/HRIS/Slack integrations (tasks link out; they don't automate).

## Open questions / risks

- **Token distribution.** How is the personal link delivered (email from Merlijn? in the offer/welcome mail?). Decide before April's start.
- **Who reads feedback, and when.** Owner + cadence for acting on onboarding feedback.
- **Day-1 logistics specifics.** A few hard facts are tagged `[confirm]` in `brand-lead/content.json` (exact greeter, the precise account list, the NS card process). Confirm before June 22.
- **Tone of the on-track status.** Must stay encouraging, never guilt-tripping, for someone who may have a heavy first week.
