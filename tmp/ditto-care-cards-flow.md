# Ditto Care Cards — Complete Flow & Design Documentation

## Overview

Ditto Care Cards is a guided card-creation experience that helps people send meaningful, personalized digital cards to someone they care about. The flow is designed to feel like a conversation — not a form — progressively deepening the user's emotional intent before they ever start writing.

The product philosophy: **the hardest part of reaching out isn't writing — it's knowing where to start.** Ditto solves that by guiding users through intent → context → composition, so the message writes itself.

---

## The 8-Step Flow

```
Landing → Recipient → Intent → Deepening → Card Style → Photo/Abstract → Compose → Preview → Success
```

### Step 0: Landing

**Screen:** `LandingScreen.tsx`
**Purpose:** Emotional hook. Set the tone before any interaction.

- Hero headline with Bricolage Grotesque display type
- Floating mini-card shapes in the background with 3D perspective drift (not random bouncing — parallax-style rotation for depth)
- Single CTA: "Create a Card"
- No navigation chrome — this is the front door

**Design notes:**
- Floating cards use `perspective(800px)` and `rotateX/rotateY` transforms for subtle depth
- Cards include faint message lines and a signature divider to look like real card previews, not colored rectangles
- Opacity at 0.5–0.6 with backdrop blur for layered depth

---

### Step 1: Recipient Name

**Screen:** `RecipientScreen.tsx`
**Purpose:** Personalize everything that follows.

- Headline: "Who is this for?"
- Single text input for the recipient's first name (max 40 chars)
- Auto-focused, large serif-style input (28px mobile / 32px desktop)
- The name flows through to writing cues, card preview, and final send button

**Design notes:**
- Minimal screen — one input, one action
- Bottom-border-only input styling (no box) for editorial feel
- Font: Bricolage Grotesque at medium weight

---

### Step 2: Intent Selection

**Screen:** `IntentSelectionScreen.tsx`
**Component:** `IntentTile.tsx`
**Purpose:** Identify the emotional category of the message.

Four intent options:

| Intent | Label | Accent Color | Description |
|--------|-------|-------------|-------------|
| `THINKING_OF_YOU` | Thinking of them | Coral `#E8916E` | Presence without pressure |
| `SHARE_MEMORY` | Share a memory | Teal `#58B6D2` | Identity-reinforcing nostalgia |
| `OFFER_HELP` | Offer help | Mint `#E0FBD5` | Specific, actionable support |
| `EXPRESS_LOVE` | Express love | Lavender `#BEAEF8` | Direct emotional expression |

**Design notes:**
- Each tile has a light tinted background derived from its accent color (8% opacity wash)
- Left-edge gradient accent strip for visual differentiation
- Color indicator dot at 20px diameter
- Selected state: accent-colored border ring + subtle scale animation
- Grid: 1 column on mobile, 2 columns on desktop

---

### Step 3: Deepening Question

**Screen:** `PromptSelectionScreen.tsx`
**Component:** `PromptCard.tsx`
**Purpose:** Narrow the emotional context before writing.

Each intent has a unique deepening question with 3–4 options:

- **Thinking of them:** "What made you think of them?" → reminded / worrying / matter / just because
- **Share a memory:** "What kind of memory?" → laughed / character / small / tradition
- **Offer help:** "What kind of support?" → practical / emotional / checking in / open-ended
- **Express love:** "What do you want them to feel?" → appreciated / proud / not alone / loved

**Design notes:**
- Options are card-like tiles (not radio buttons) with generous padding
- Selected option gently expands while others recede (scale animation)
- Context banner at top shows the selected intent with its accent color
- Writing cues support `{name}` interpolation — replaced with the recipient's actual name

---

### Step 4: Card Style

**Screen:** `CardStyleScreen.tsx`
**Purpose:** Choose between photo-backed or abstract-art card background.

Two options presented as mini card previews (not icons):
- **Photo card** — shows a sample card with a photo background
- **Abstract card** — shows a sample card with an abstract gradient background

**Design notes:**
- Each option is a realistic mini card preview with the Ditto logo and sample text visible
- Users see *outcomes*, not categories
- Tapping either navigates to the respective sub-flow

---

### Step 5a: Photo Upload & Crop

**Screen:** `PhotoUploadScreen.tsx`
**Processor:** `PhotoProcessor.ts`
**Purpose:** Upload a photo and fine-tune how it appears on the card.

Features:
- Drag-and-drop or tap-to-upload
- **Landscape detection:** If the uploaded image is landscape, a toggle appears asking if the user wants a landscape or portrait card
- **Manual crop repositioning:** iOS-style drag-to-reposition. The photo is shown at full scale within the card frame; users drag to adjust the focal point
- Overlay mode toggle (dark/light text)
- Live card preview updates in real-time

**Technical details:**
- `PhotoProcessor.ts` handles canvas-based cropping with `cropPosition` offsets
- Portrait cards: 5:8 aspect ratio
- Landscape cards: 8:5 aspect ratio
- Touch and mouse events for drag interaction
- Orientation and crop position persist in `CardStyleData`

### Step 5b: Abstract Picker

**Screen:** `AbstractPickerScreen.tsx`
**Data:** `abstractBackgrounds.ts`
**Purpose:** Choose from curated abstract gradient backgrounds.

- Grid of abstract background swatches
- Each is a CSS gradient defined in the data layer
- Selected background gets a ring indicator
- Overlay defaults to "light" mode for abstract backgrounds

---

### Step 6: Compose

**Screen:** `MessageScreen.tsx`
**Purpose:** Write the message with contextual guidance.

- **Writing cues** from the selected deepening option appear above the textarea as gentle prompts
- Cues use `{name}` interpolation (e.g., "What would Sarah say if you brought this up?")
- **Stationery-styled textarea:** warm background, soft border radius, paper-like feel
- **"Sign as" input** for the sender name
- **Live card preview** on desktop (side-by-side layout) — text appears on the card as the user types
- Character guidance: subtle, not enforced

**Design notes:**
- Textarea background uses `bg-card` with warm border
- On desktop: content column + card preview with a shared background zone
- Sender name defaults to "Mom" (configurable)

---

### Step 7: Preview

**Screen:** `FinalPreviewScreen.tsx`
**Purpose:** Final review before sending.

- Full-size card preview with gentle floating animation (subtle Y-axis bob)
- "Send to {name}" button with intent accent color
- **Send animation:** Card flies upward with scale-down and slight rotation, then cross-dissolves to "Sending..." state

**Design notes:**
- Card uses `AnimatePresence` for the departure animation
- Exit: `y: -300, scale: 0.8, rotate: -2` over 0.7s with custom easing
- 800ms delay before transitioning to success screen

---

### Step 8: Success

**Screen:** `SuccessScreen.tsx`
**Purpose:** Emotional payoff — celebrate the act of reaching out.

- The user's actual card appears first, animating in
- Card floats briefly, then transitions to confirmation copy
- "Your card is on its way to {name}"
- Two actions: "Done" and "Send Another"

**Design notes:**
- Shows the real card (not a generic icon) as the hero element
- Brand-colored accents in the confirmation state
- "Send Another" resets the entire flow

---

## Design System

### Typography

| Usage | Font | Weight | Size |
|-------|------|--------|------|
| Display titles | Bricolage Grotesque | 600–700 | 28–36px |
| Body / UI | Bricolage Grotesque | 400–500 | 15–17px |
| Card messages | Instrument Serif (italic) | 400 | 14–18px |

### Color Palette

**Base:**
- Background: `hsl(36 33% 97%)` — Warm Linen
- Foreground: `hsl(20 12% 14%)` — Near-black warm
- Muted foreground: `hsl(20 8% 36%)` — WCAG AA compliant (~5:1 contrast)

**Brand:**
- Navy: `#0D164F` / `hsl(232 84% 19%)` — Primary brand
- Coral: `#E8916E` — Thinking of You
- Teal: `#58B6D2` — Share a Memory
- Mint: `#E0FBD5` — Offer Help
- Lavender: `#BEAEF8` — Express Love

### Interaction Patterns

- **Progress bar:** Thin 2px bar at top of every step screen, animated width based on current step / 7
- **Back button:** 44×44px minimum tap target, `ChevronLeft` icon + "Back" label
- **Primary CTA:** Full-width on mobile with frosted-glass sticky footer (`backdrop-blur-xl bg-background/80`); `max-w-sm` left-aligned on desktop
- **Screen transitions:** Slide in from right (`x: 100%`), slide out left (`x: -100%`), 300ms with custom cubic-bezier easing `[0.32, 0.72, 0, 1]`
- **Selection feedback:** Scale animations on tap (`whileTap: { scale: 0.97 }`)

### Accessibility

- All muted text meets WCAG AA 4.5:1 contrast minimum
- Touch targets: 44×44px minimum throughout
- Focus-visible outlines on interactive elements
- Semantic HTML structure with proper heading hierarchy (single H1 per screen)

---

## State Architecture

All card state lives in `CardFlowController.tsx` via a single `CardState` object:

```typescript
interface CardState {
  intent: IntentOption | null;
  selectedDeepening: string | null;
  cardStyleData: CardStyleData;
  message: string;
  senderName: string;
  recipientName: string;
}

interface CardStyleData {
  style: "photo" | "abstract" | null;
  photoDataUrl: string | null;
  abstractBg: AbstractBackground | null;
  overlayMode: "dark" | "light";
  brightness: number;
  filterEnabled: boolean;
  orientation: "portrait" | "landscape";
  cropPosition: { x: number; y: number };
}
```

Navigation is managed via a `Screen` union type with a `backMap` for deterministic back-navigation. `AnimatePresence` with `mode="wait"` ensures clean transitions between screens.

---

## File Map

```
src/components/care-card/
├── CardFlowController.tsx    — State + routing orchestrator
├── CardPreview.tsx           — Reusable card render (portrait + landscape)
├── FloatingCards.tsx          — Landing page background animation
├── IntentTile.tsx            — Intent selection tile component
├── NavHeader.tsx             — Back button + progress bar
├── PhotoProcessor.ts         — Canvas-based photo crop/process
├── PrimaryButton.tsx         — Standardized CTA button
├── PromptCard.tsx            — Deepening option tile component
└── screens/
    ├── LandingScreen.tsx
    ├── RecipientScreen.tsx
    ├── IntentSelectionScreen.tsx
    ├── PromptSelectionScreen.tsx
    ├── CardStyleScreen.tsx
    ├── PhotoUploadScreen.tsx
    ├── AbstractPickerScreen.tsx
    ├── MessageScreen.tsx
    ├── FinalPreviewScreen.tsx
    └── SuccessScreen.tsx

src/data/
├── abstractBackgrounds.ts    — Abstract gradient definitions
├── brandColors.ts            — Brand color constants (hex + HSL)
└── cardVisuals.ts            — Intents, deepening options, writing cues
```
