# Shipping Timeline — Interactive Scroll Experience

## What This Is

A full-screen, vertically scrollable timeline that visualizes everything Ditto shipped from January 2025 to February 2026. The scroll is time-synced: each pixel of scroll equals the same amount of real time. The content accelerates as velocity increases — the investor scrolls at a constant pace, but the items come faster and faster. The data does the convincing.

**Core stats:** 860 items shipped in 14 months. Velocity grew from 54/month to 155/month.

## Tech Stack

React + Tailwind CSS (built in Lovable). Framer Motion for all animations. Single-page app, no routing needed.

---

## 1. Scroll Mechanic

The total scrollable height maps linearly to time (Jan 1 2025 → Feb 28 2026). Every item is positioned at its exact completion date on this timeline.

- In February 2025 (11 items): the screen is sparse, items trickle in
- In July 2025 (86 items): noticeable acceleration, items come in clusters
- In November 2025 (155 items): items flood the screen, cascading past in a dense stream
- In January 2026 (147 items): the avalanche continues

The contrast between slow months and fast months is the entire point. Do not normalize or spread items evenly. Let the real density speak.

**Total scroll height:** Make the full timeline roughly 15,000–20,000px tall so that dense months feel truly packed. Tune this so peak months (Nov 2025, Jan 2026) show 8-15 items simultaneously entering the viewport.

---

## 2. Sticky Header

A fixed header bar at the top, always visible. Contains:

### Live Counter
A large, prominent animated number: **"Items shipped: XXX"**
- Starts at 0
- Ticks up smoothly (odometer-style animation, not jumping) as items scroll past a horizontal trigger line near the top third of the viewport
- Use a spring/tween animation so the number rolls up satisfyingly
- This is the single most important element — it must feel alive

### Current Date
Show the current timeline position as **"Month Year"** (e.g., "November 2025"). Transitions smoothly between months with a subtle crossfade.

### Velocity Indicator
A small horizontal bar or mini-chart showing items/month for the current month. As months get denser, this bar grows wider or a small sparkline pulses higher. Keep it subtle — the counter is the star.

### Pillar Breakdown
Four small colored dots or mini-bars showing the live distribution of items across the four pillars as you scroll. This shifts from Foundation-heavy early on to more balanced later.

---

## 3. Item Cards

Each shipped item appears as a compact horizontal card/pill that animates into view.

### Card Content
- **Ticket ID** (small, muted): e.g., "DPMA-647"
- **Title** (primary text): e.g., "Take things under control"
- **Type badge** (tiny pill): Epic / Story / Bug / Task
- **Pillar color**: left border or background tint

### Card Sizing by Type
- **Epics**: Larger cards, bolder text, slightly more padding. These are the headline milestones.
- **Stories**: Standard size
- **Bugs & Tasks**: Compact/smaller. Still visible but clearly supporting work.

### Layout
- Items appear on alternating sides of a central vertical timeline line, or
- Items flow in a single column with slight horizontal stagger for visual rhythm
- Cards should never overlap — stack naturally with small gaps
- In dense months, the gaps shrink, creating a visual "compression" effect

---

## 4. Animations

**This section is critical. The scroll experience must feel buttery smooth and premium.**

### Item Entry Animation
Each card animates in as it crosses into the viewport:
- Fade in from 0 to 1 opacity
- Slide in slightly from the side (alternating left/right, ~20px)
- Duration: 300ms with an ease-out curve
- Use Framer Motion's `whileInView` with `viewport={{ once: true }}`

### Dense Month Cascade
When many items appear in quick succession during scroll:
- Stagger the animations by 30-50ms each
- The rapid-fire stagger creates a "cascade" or "waterfall" effect
- This is where the "wow" moment happens — items pour onto the screen

### Counter Animation
- Use a smooth spring animation for the number
- When scrolling through dense sections, the counter accelerates visibly
- Consider a subtle glow or pulse on the counter during high-velocity sections

### Timeline Line
- A thin vertical line runs down the center/side of the page
- The line has a subtle glow that intensifies based on current month velocity
- In sparse months: dim, calm
- In peak months: brighter, pulsing subtly

### Month Transitions
- When crossing into a new month, show a subtle horizontal divider or a month label that fades in
- No hard breaks — the flow should feel continuous

### Scroll Feel
- Use CSS `scroll-behavior: smooth` on the container
- All animations must be GPU-accelerated (transform and opacity only)
- Use `will-change: transform, opacity` on cards
- Target 60fps at all times — no jank, no layout thrashing

---

## 5. Auto-Categorization into Four Pillars

Every item is auto-categorized into one of four pillars based on keyword matching on the item title. Assign a distinct color to each.

### Clarity — Making care more understandable
**Keywords:** AI, consultation, summary, summarize, summarization, OCR, document, transcript, recording, understand, simplification, feedback on AI, AI output, AI failure, AI improvement, event detail, event view
**Examples:** "New AI Consultation", "Direct document/screenshot to understandable summary", "Switch transcription service to Ditto AI"

### Connection — Connecting to caregivers and sharing
**Keywords:** care network, share, sharing, invite, connect, doctor, data sharing, caregiver
**Examples:** "Build Care Network v1", "Data sharing via server", "Redo Invite Page"

### Convenience — Making it easier to use
**Keywords:** onboarding, navigation, flow, UX, UI, activation, review, appointment, preparation, registration, funnel, upgrade, force update, reimagine, improve flow, videos, comms, explanatory
**Examples:** "Improve flow and navigation", "Onboarding", "Move Registration higher up in the funnel", "Appointment Preparation"

### Foundation — Tech fundamentals, reliability, polish
**Keywords:** infrastructure, security, tech debt, maintenance, bug, fix, backend, Android, iOS, release, pre-production, CI/CD, observability, migration, performance, inbox, burning, cost, pilot, launch, post-launch, on par, backward compatible, security Q, pre-prod, app-store, play store
**Examples:** "Infrastructure", "Security Q2", "Android on par with iOS", "Technical Observability"

### Fallback
If no keywords match, assign to **Convenience** as default (improving the product experience).

### Priority
If multiple pillars match, use this priority: Clarity > Connection > Convenience > Foundation. AI-related items should almost always be Clarity.

---

## 6. Opening Section (Hero)

Before the timeline scroll begins, show a clean full-viewport hero:

- **Headline:** "860 items shipped in 14 months"
- **Subline:** "Scroll to experience our velocity"
- A subtle downward arrow or chevron with a gentle bounce animation
- Minimal, clean, lots of whitespace
- Consider showing the four pillar colors as small dots with labels as a legend

Scrolling past this hero starts the timeline at January 2025.

---

## 7. Closing Section

After the last item (February 2026), show a summary viewport:

- **Final counter** prominently displayed: "860 items shipped"
- **Velocity growth:** "54/mo → 155/mo — 3x acceleration"
- **Pillar breakdown:** Four horizontal bars showing total items per pillar with counts. This shows strategic balance — not just speed, but doing the right things.
- **Monthly velocity chart:** A small bar chart showing all 14 months side by side. The growth curve is the visual exclamation point.

Keep it factual. No marketing copy. The numbers are the pitch.

---

## 8. Data Structure

Feed the timeline a JSON array. Each item has this shape:

```json
{
  "id": "DPMA-647",
  "date": "2025-06-24",
  "title": "Take things under control",
  "type": "Epic",
  "pillar": "Foundation"
}
```

Types are: `Epic`, `Story`, `Bug`, `Task`

Pillars are: `Clarity`, `Connection`, `Convenience`, `Foundation`

### Monthly velocity reference (for the velocity indicator):

| Month | Items |
|-------|-------|
| Jan 2025 | 54 |
| Feb 2025 | 11 |
| Mar 2025 | 18 |
| Apr 2025 | 34 |
| May 2025 | 46 |
| Jun 2025 | 66 |
| Jul 2025 | 86 |
| Aug 2025 | 26 |
| Sep 2025 | 23 |
| Oct 2025 | 96 |
| Nov 2025 | 155 |
| Dec 2025 | 73 |
| Jan 2026 | 147 |
| Feb 2026 | 25 |

---

## 9. Visual Style

- **Dark theme** — dark background (near-black or very dark navy), light text. Dark themes feel more premium and make the colored pillar cards pop.
- **Typography:** Clean sans-serif (Inter or system font). Large bold counter. Compact card text.
- **Pillar colors:** Four distinct, vibrant-but-not-neon colors. Good contrast on dark backgrounds. Suggested starting point:
  - Clarity: blue (#60A5FA)
  - Connection: amber/orange (#FBBF24)
  - Convenience: emerald (#34D399)
  - Foundation: slate/cool gray (#94A3B8)
- Override these colors with brand colors when available.
- **Timeline line:** Thin (1-2px), semi-transparent white, with a glow effect that intensifies with velocity.
- **Cards:** Slightly rounded, subtle background (dark card on darker background), left border colored by pillar. Subtle shadow or glow on entry.

---

## 10. Responsive

- Desktop-first (this is for investor meetings and screen-shares)
- On mobile: single column, no alternating sides, slightly smaller cards
- The sticky header should collapse to just the counter + date on small screens
- Touch scrolling must feel smooth and natural on iPad (common in pitch settings)

---

## 11. Performance

- 860 items is a lot of DOM. Use virtualization or render-on-scroll (only mount items within ±1 viewport of current scroll position)
- Alternatively, use Framer Motion's `LazyMotion` to reduce bundle size
- All animations on `transform` and `opacity` only — never animate layout properties
- Test on a mid-range laptop to ensure 60fps during dense sections
