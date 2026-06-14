# Direction B v2: Warm Wellness Hybrid

**Design Philosophy**: Ditto's colors exist but warmer. Soft gradient backgrounds (cream/peach), organic blob-shaped orb, particle effects. Partly off-brand.

**Version**: 2.0
**Date**: 2026-02-06
**Status**: Ready for Stitch Generation

---

## Overview

Direction B v2 is the **compromise direction** — it keeps Ditto's brand colors visible but **warms them significantly** and adds organic, wellness-inspired elements. The orb becomes blob-shaped (not a perfect circle), backgrounds use soft gradients with peach/cream tones, and particle effects add life. This direction partially steps away from strict brand adherence to create a warmer, more human experience.

### Design Principles

1. **Warm Brand Evolution**: Ditto colors are present but warmer, softer
2. **Organic Shapes**: Blob orb instead of perfect circle
3. **Particle Life**: Subtle floating particles add warmth
4. **Gradient Richness**: Multi-stop gradients with warm tones
5. **Human Imperfection**: Slightly wobbly shapes, hand-drawn feel

---

## Color System

### Brand Colors (Warmed Variants)

| Token | Hex | Usage | Notes |
|-------|-----|-------|-------|
| `navy-warm` | `#1A2566` | Text, UI (lighter than Ditto's #0D164F) | Warmer navy |
| `yellow-warm` | `#FFD93D` | Orb highlights, accents | More golden yellow |
| `purple-soft` | `#C5B8F5` | Orb gradient, soft accents | Lighter purple |
| `coral-accent` | `#FF8A70` | Warm highlight color | New warm tone |
| `peach-soft` | `#FFB5A0` | Gradient stops | New warm tone |

### Background Colors (Rich Warmth)

| Token | Hex | Usage |
|-------|-----|-------|
| `bg-cream` | `#FFF8F0` | Primary background |
| `bg-peach-light` | `#FFE8D9` | Warm gradient start |
| `bg-apricot` | `#FFDFC8` | Warm gradient mid |
| `bg-soft-white` | `#FFFBF5` | Gradient end |
| `bg-lavender-light` | `#F5F0FF` | Thinking state background |

### Orb Blob Color States

| State | Gradient | Description |
|-------|----------|-------------|
| Idle | `#C5B8F5` → `#FFB5A0` → `#1A2566` | Purple to peach to navy |
| Listening | `#FFD93D` → `#FF8A70` → `#C5B8F5` | Golden yellow to coral to purple |
| Thinking | `#B8A8E8` → `#9B8FD0` → `#82828A` | Muted purple-grey |
| Responding | `#FFD93D` → `#FFB5A0` → `#FF8A70` | Golden yellow to peach to coral glow |
| Complete | `#7BC47F` → `#A8E6A3` → `#FFD93D` | Green to light green to yellow |

---

## Typography

### Font Family
- **Primary**: Nunito (rounded sans-serif, warm and friendly)
- **Fallback**: Quicksand (if Nunito unavailable)
- **Avoid**: Inter (too geometric for this direction)

### Type Scale

| Style | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `display` | 38px | 700 | 1.2 | "How are you today?" |
| `h1` | 30px | 600 | 1.3 | Screen titles |
| `h2` | 24px | 600 | 1.4 | Section headers |
| `h3` | 19px | 600 | 1.4 | Dimension card titles |
| `body` | 17px | 500 | 1.6 | Transcript, AI responses |
| `small` | 15px | 500 | 1.5 | Supporting text |
| `caption` | 13px | 500 | 1.4 | Timestamps, hints |

### Status Text Style
- Font: Nunito, 22px, weight 700
- Color: `#1A2566` (warm navy)
- Tracking: 0.01em
- Center aligned below orb
- Slight text shadow for warmth: 0 2px 4px rgba(255, 181, 160, 0.15)

---

## Orb Blob Design Specifications

### Core Properties

| Property | Value |
|----------|-------|
| Idle size | ~190px width, ~180px height (organic blob) |
| Listening size | ~220px width, ~210px height |
| Thinking size | ~170px width, ~165px height |
| Responding size | ~240px width, ~230px height |
| Position | Center screen, vertical offset -60px |
| Shape | **Organic blob** (not perfect circle) |

### Blob Shape Specifications

The orb is NOT a perfect circle. It's a **soft, organic blob**:

```css
/* Approximate SVG path for blob shape */
border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
/* OR use blob SVG with 6-8 control points */
/* Slight wobble animation: morph between similar blob shapes */
```

**Blob Characteristics**:
- 6-8 anchor points
- Smooth curves between points
- Slight asymmetry (feels hand-drawn)
- Wobble animation: Morph between 2-3 similar blob shapes (8s cycle)

### Gradient Specifications

**Idle State**:
```css
background: radial-gradient(ellipse at 35% 25%,
  #C5B8F5 0%,
  #FFB5A0 45%,
  #1A2566 100%);
box-shadow:
  0 20px 60px rgba(197, 184, 245, 0.25),
  0 8px 24px rgba(255, 181, 160, 0.15);
```

**Listening State**:
```css
background: radial-gradient(ellipse at 35% 25%,
  #FFD93D 0%,
  #FF8A70 50%,
  #C5B8F5 100%);
box-shadow:
  0 24px 72px rgba(255, 217, 61, 0.35),
  0 12px 36px rgba(255, 138, 112, 0.25);
/* Pulse animation: scale + slight blob morph with amplitude */
```

**Thinking State**:
```css
background: radial-gradient(ellipse at 50% 50%,
  #B8A8E8 0%,
  #9B8FD0 60%,
  #82828A 100%);
box-shadow:
  0 16px 48px rgba(184, 168, 232, 0.20);
animation: gentle-rotate-wobble 2s ease-in-out infinite;
```

**Responding State**:
```css
background: radial-gradient(ellipse at 35% 25%,
  #FFD93D 0%,
  #FFB5A0 40%,
  #FF8A70 100%);
box-shadow:
  0 28px 80px rgba(255, 217, 61, 0.45),
  0 14px 40px rgba(255, 181, 160, 0.30),
  0 0 60px rgba(255, 138, 112, 0.20); /* Extra glow */
/* Expanded glow, subtle pulse */
```

**Complete State**:
```css
/* Morph to rounded checkmark blob shape */
background: radial-gradient(ellipse at 35% 25%,
  #7BC47F 0%,
  #A8E6A3 50%,
  #FFD93D 100%);
box-shadow:
  0 24px 72px rgba(123, 196, 127, 0.40),
  0 12px 36px rgba(255, 217, 61, 0.25);
animation: checkmark-blob-morph 900ms ease-out;
```

### Particle Effects

**Floating Particles Around Orb**:
- Count: 12-16 particles
- Size: 4-10px diameter circles
- Color: rgba(255, 217, 61, 0.4) or rgba(255, 181, 160, 0.3)
- Behavior: Slow float upward and fade out
- Spawn rate: 1-2 per second during active states
- Animation: 3-5s float duration, random horizontal drift

**Implementation**:
```css
/* Particle example */
.particle {
  width: 6px;
  height: 6px;
  background: radial-gradient(circle,
    rgba(255, 217, 61, 0.6) 0%,
    rgba(255, 217, 61, 0) 100%);
  border-radius: 50%;
  animation: float-particle 4s ease-out forwards;
}

@keyframes float-particle {
  0% { transform: translate(0, 0) scale(1); opacity: 0.6; }
  100% { transform: translate(var(--drift-x), -100px) scale(0.3); opacity: 0; }
}
```

### Animation States

| State | Animation | Duration | Easing |
|-------|-----------|----------|--------|
| Idle | Breathing blob morph + wobble | 8s (morph) + 4s (breathing) | ease-in-out |
| Listening | Amplitude pulse + rapid blob morph | Real-time 60fps | linear |
| Thinking | Gentle rotation + slow blob wobble | 2s | ease-in-out |
| Responding | Glow pulse + subtle blob breathing | 2.5s | ease-in-out |
| Complete | Morph to checkmark blob | 900ms | cubic-bezier(0.4, 0.0, 0.2, 1) |

### Inner Texture Details

**Idle/Thinking**: Floating dots that drift slowly
- 10-15 dots
- Color: rgba(255, 255, 255, 0.25)
- Size: 3-6px
- Animation: Slow drift in random directions

**Listening**: Organic waveform texture
- Not straight lines — wobbly, hand-drawn feel
- Color: rgba(255, 255, 255, 0.4)
- Height varies with amplitude
- Slight horizontal wave motion

**Responding**: Soft radiating glow
- Not sharp lines — soft gradient rays
- 8-12 rays
- Color: rgba(255, 255, 255, 0.3)
- Animation: Pulse outward with fade

---

## Background Gradient Specifications

### Immersive Mode Gradient (Rich Multi-Stop)

**Idle Background**:
```css
background: linear-gradient(165deg,
  #FFE8D9 0%,     /* Soft peach */
  #FFDFC8 25%,    /* Warm apricot */
  #FFF8F0 60%,    /* Cream */
  #FFFBF5 100%    /* Soft white */
);
```

**Listening Background** (warmer, more vibrant):
```css
background: linear-gradient(165deg,
  #FFD9C0 0%,     /* Warmer peach */
  #FFE8D9 30%,    /* Soft peach */
  #FFF5EB 70%,    /* Warm cream */
  #FFF8F0 100%    /* Cream */
);
```

**Thinking Background** (cooler, muted):
```css
background: linear-gradient(165deg,
  #F5F0FF 0%,     /* Soft lavender */
  #F0E8F5 30%,    /* Muted purple-pink */
  #F5F0EB 70%,    /* Cool grey-cream */
  #FFFBF5 100%    /* Soft white */
);
```

**Responding Background** (bright, warm):
```css
background: linear-gradient(165deg,
  #FFE4BA 0%,     /* Warm golden */
  #FFD9C0 30%,    /* Peach */
  #FFE8D9 70%,    /* Soft peach */
  #FFF5EB 100%    /* Warm cream */
);
```

**Complete Background** (celebration, soft green tint):
```css
background: linear-gradient(165deg,
  #E8F5E9 0%,     /* Very soft green */
  #FFF5EB 30%,    /* Warm cream */
  #FFFBF5 70%,    /* Soft white */
  #FFFBF5 100%    /* Soft white */
);
/* Add subtle sparkle overlay: small dots in #FFD93D */
```

### Gradient Transition
- Duration: 800ms
- Easing: ease-in-out
- Syncs with orb state change

---

## Transcript Area Styling

### Container

| Property | Value |
|----------|-------|
| Position | Fixed bottom, 24px margin |
| Width | 88% of screen, max 480px |
| Background | rgba(255, 248, 240, 0.90) (warmer) |
| Backdrop filter | blur(24px) |
| Border radius | 24px (more rounded) |
| Border | 1px solid rgba(255, 181, 160, 0.20) (warm border) |
| Padding | 18px 22px |
| Shadow | 0 12px 32px rgba(255, 138, 112, 0.12) (warm shadow) |
| Max height | 32% of viewport |
| Overflow | Scroll (hidden scrollbar) |

### Text Styling

**User Text**:
- Font: Nunito, 17px, weight 600
- Color: `#1A2566` (warm navy)
- Margin bottom: 14px
- Recording indicator: Golden dot (#FFD93D) with pulse + particle trail

**AI Text**:
- Font: Nunito, 17px, weight 500
- Color: `#666670` (grey)
- Margin bottom: 14px
- Streaming cursor: Blinking golden bar with soft glow

### Behavior
- Fades in from bottom (300ms, ease-out)
- Slight bounce on appearance (spring animation)
- Auto-scrolls smoothly
- Dims slightly (opacity 0.85) when not focus
- Glows subtly when active (border becomes more visible)

---

## Button Styling

### Finish Button

**Default State**:
```css
background: linear-gradient(135deg,
  rgba(255, 248, 240, 0.8) 0%,
  rgba(255, 232, 217, 0.8) 100%);
border: 2px solid rgba(255, 181, 160, 0.25);
color: #1A2566;
font: Nunito, 17px, weight 700;
border-radius: 9999px; /* pill */
padding: 16px 32px;
box-shadow:
  0 6px 16px rgba(255, 138, 112, 0.12),
  inset 0 1px 0 rgba(255, 255, 255, 0.5);
backdrop-filter: blur(10px);
```

**Hover/Active State**:
```css
background: linear-gradient(135deg,
  rgba(255, 232, 217, 0.9) 0%,
  rgba(255, 223, 200, 0.9) 100%);
border-color: rgba(255, 181, 160, 0.35);
transform: scale(0.97) translateY(1px);
box-shadow:
  0 4px 12px rgba(255, 138, 112, 0.15);
```

### Position
- Center bottom, 36px from bottom edge
- Above hint text
- Width: auto, min 180px

### Hint Text Below Button
- "or say 'I'm done'"
- Font: Nunito, 15px, weight 600
- Color: rgba(26, 37, 102, 0.5)
- Text shadow: 0 1px 2px rgba(255, 255, 255, 0.5)
- Margin top: 10px

---

## Component Specifications

### Close Button (Top Left)

| Property | Value |
|----------|-------|
| Icon | X (close), rounded stroke |
| Size | 26px |
| Color | `#1A2566` |
| Background | rgba(255, 248, 240, 0.7) |
| Border | 1px solid rgba(255, 181, 160, 0.2) |
| Backdrop filter | blur(12px) |
| Border radius | 14px |
| Padding | 11px |
| Position | Fixed top-left, 18px margin |
| Shadow | 0 4px 12px rgba(255, 138, 112, 0.10) |

### Timer (Top Right)

| Property | Value |
|----------|-------|
| Font | Nunito, 15px, weight 700 |
| Color | rgba(26, 37, 102, 0.65) |
| Background | rgba(255, 248, 240, 0.7) |
| Border | 1px solid rgba(255, 181, 160, 0.2) |
| Backdrop filter | blur(12px) |
| Border radius | 14px |
| Padding | 9px 14px |
| Position | Fixed top-right, 18px margin |
| Shadow | 0 4px 12px rgba(255, 138, 112, 0.10) |

### Status Text (Below Orb)

| Property | Value |
|----------|-------|
| Font | Nunito, 22px, weight 700 |
| Color | `#1A2566` |
| Text align | Center |
| Margin top | 36px from orb |
| Text shadow | 0 2px 4px rgba(255, 181, 160, 0.15) |
| Animation | Fade + gentle float (translate Y -5px → 0) |

**Status Messages**:
- Idle: "How are you today?"
- Listening: "I'm listening..."
- Thinking: "Let me think about that..."
- Responding: (empty, text streams)
- Complete: "Great check-in!"

---

## Session Summary (4 Dimensions)

### Layout Structure

**Success Banner**:
- Background: Linear gradient 135deg (#E8F5E9 → #FFF5EB)
- Border: 2px solid `#A8E6A3` (light green)
- Border radius: 24px
- Padding: 22px
- Shadow: 0 8px 24px rgba(123, 196, 127, 0.15)
- Icon: Checkmark in gradient circle (green → yellow)
- Text: Nunito 19px weight 700

### Dimension Cards

**Card Structure**:
```css
background: linear-gradient(135deg,
  #FFFBF5 0%,
  #FFF8F0 100%);
border-radius: 24px;
padding: 22px;
box-shadow:
  0 6px 20px rgba(255, 138, 112, 0.08),
  inset 0 1px 0 rgba(255, 255, 255, 0.8);
border-left: 5px solid [dimension color];
```

**Dimension Colors**:
| Dimension | Accent Color | Border Color |
|-----------|--------------|--------------|
| BODY | Warm coral #FF8A70 | 5px left border |
| MIND | Soft purple #C5B8F5 | 5px left border |
| ACTIONS | Fresh green #7BC47F | 5px left border |
| CONTEXT | Golden amber #FFD93D | 5px left border |

### Dimension Card Header
- Title: Nunito, 19px, weight 800, uppercase, tracking 0.08em
- Color: Dimension accent color
- Text shadow: 0 1px 2px rgba(255, 255, 255, 0.5)
- Margin bottom: 18px
- Icon: 22px, dimension color with subtle glow

### Symptom Rows (in BODY card)

**Structure**:
```
Name | Severity
─────────────────────
[Rounded severity bar with gradient]
Location, duration, details
```

**Styling**:
- Name: Nunito, 17px, weight 700, `#1A2566`
- Severity: Nunito, 17px, weight 800, `#FF8A70`
- Bar: Height 10px, radius 5px
  - Filled: Gradient (#FF8A70 → #FFB5A0)
  - Empty: rgba(255, 181, 160, 0.15)
  - Shadow on filled: 0 2px 6px rgba(255, 138, 112, 0.20)
- Details: Nunito, 15px, weight 600, `#82828A`

### Save Button

**Primary CTA**:
```css
background: linear-gradient(135deg,
  #1A2566 0%,
  #2A3570 100%);
color: #FFFFFF;
font: Nunito, 19px, weight 700;
border-radius: 20px;
padding: 20px 36px;
box-shadow:
  0 10px 28px rgba(26, 37, 102, 0.25),
  inset 0 1px 0 rgba(255, 255, 255, 0.15);
width: 100%;
margin-top: 28px;
```

**Hover/Active**:
```css
background: linear-gradient(135deg,
  #2A3570 0%,
  #3A4580 100%);
transform: translateY(-3px);
box-shadow:
  0 14px 36px rgba(26, 37, 102, 0.35),
  inset 0 1px 0 rgba(255, 255, 255, 0.15);
```

---

## Screen Specifications

### 1. Immersive Check-in Screen (Idle)

**Layout**:
- Full screen, no navigation
- Background: Warm gradient (#FFE8D9 → #FFDFC8 → #FFF8F0 → #FFFBF5)
- Close button: Top left (warm frosted glass)
- Timer: Top right (0:00, warm frosted glass)
- Breathing blob orb: Center, ~190px, purple-peach-navy gradient
- Floating particles: 12-16 around orb
- Status text: "How are you today?" (navy, 22px, below orb)
- Hint text: "Tap the orb or just start speaking" (grey, 15px)
- Finish button: Bottom, warm gradient ghost style
- Secondary hint: "or say 'I'm done'"

**Orb Animation**: Breathing blob morph (8s) + gentle wobble (4s)

### 2. Immersive Check-in Screen (Listening)

**Changes from Idle**:
- Background: Warmer gradient (#FFD9C0 → #FFE8D9 → #FFF5EB)
- Orb: Expands to ~220px, yellow-coral-purple gradient
- Orb animation: Pulses with amplitude + rapid blob morph
- Particles: More frequent spawning, golden color
- Status text: "I'm listening..."
- Transcript area: Fades in with slight bounce
  - Warm cream background, blur 24px
  - Golden recording dot with particle trail
- Timer: Running

### 3. Immersive Check-in Screen (Thinking)

**Changes**:
- Background: Cooler (#F5F0FF → #F0E8F5 → #F5F0EB)
- Orb: Contracts to ~170px, muted purple-grey gradient
- Orb animation: Gentle rotation + slow blob wobble
- Particles: Slower, more muted colors
- Status text: "Let me think about that..."
- Transcript: Shows completed text

### 4. Immersive Check-in Screen (Responding)

**Changes**:
- Background: Bright warm (#FFE4BA → #FFD9C0 → #FFE8D9)
- Orb: Expands to ~240px, golden-peach-coral gradient with extra glow
- Orb animation: Soft glow pulse + subtle breathing
- Particles: Bright golden, frequent
- Status text: Empty
- Transcript: AI response streams with golden cursor + glow
- New button: "Tap to respond" (warm gradient ghost)

### 5. Immersive Check-in Screen (Complete)

**Changes**:
- Background: Celebration (#E8F5E9 → #FFF5EB → #FFFBF5) with golden sparkle overlay
- Orb: Morphs to checkmark blob (900ms), green-light green-yellow gradient
- Particles: Golden sparkles burst
- Status text: "Great check-in!"
- Subtext: "Here's what I captured."
- Button: "See Summary" (primary gradient button)

### 6. Session Summary Screen

**Header**:
- Back button (warm frosted glass)
- Title: "Check-in Complete" (navy, 30px, Nunito)
- Edit button (warm frosted glass)

**Success Banner** (gradient card with green-cream gradient)

**Scrollable Content**:
- BODY card (coral left border)
- MIND card (purple left border)
- ACTIONS card (green left border)
- CONTEXT card (golden left border)

All cards have gradient backgrounds and warm shadows.

**Footer**:
- "View Full Transcript" link (navy, 17px, Nunito)
- "Save Check-in" button (gradient navy button)

### 7. Home Integration

**Check-in FAB**:
- Position: Bottom right, 24px margin
- Size: 68px diameter
- Background: Gradient (warm navy → lighter navy)
- Icon: Simplified blob orb symbol in golden yellow
- Shadow: 0 10px 30px rgba(26, 37, 102, 0.30)
- Animation: Gentle breathing + particle emission

**Recent Check-in Cards**:
```css
background: linear-gradient(135deg,
  #FFFBF5 0%,
  #FFF8F0 100%);
border-radius: 24px;
padding: 18px;
box-shadow: 0 6px 18px rgba(255, 138, 112, 0.08);
border-left: 4px solid [dimension color];
```

---

## Portal Transition Animation

### Home → Immersive (800ms)

**Sequence**:
1. **0ms**: User taps FAB
   - Haptic: Medium impact
   - FAB emits particle burst
   - FAB pulses once

2. **0-250ms**: Home content scales + fades + blurs
   - Scale: 1.0 → 0.80
   - Opacity: 1.0 → 0.0
   - Blur: 0px → 10px
   - Tab bar slides down with bounce

3. **100-500ms**: Warm gradient expands from FAB
   - Radial gradient expands
   - Particles trail the expansion
   - Shifts to immersive gradient

4. **350-700ms**: Blob orb materializes
   - Scale: 0.0 → 1.0 (spring easing, overshoot)
   - Opacity: 0.0 → 1.0
   - Blob morph: Circle → organic blob
   - Particles spawn around orb
   - Rotation: 0° → 360° (single gentle spin)

5. **600-800ms**: UI elements fade in
   - Close, timer, status text
   - Opacity: 0.0 → 1.0
   - Translate Y: 15px → 0px
   - Gentle bounce on arrival

**Easing**: cubic-bezier(0.34, 1.56, 0.64, 1) (spring bounce)

### Immersive → Home (800ms, reverse)

Same sequence in reverse with gentle bounce.

---

## Accessibility Specifications

### VoiceOver Support

| Element | Announcement |
|---------|--------------|
| Close button | "Exit check-in" |
| Orb (idle) | "Health companion, currently idle. The breathing orb is ready. Tap to begin or start speaking." |
| Orb (listening) | "Listening to your health check-in. Recording in progress." |
| Orb (thinking) | "Processing your response. Please wait." |
| Orb (responding) | "AI is responding. [AI text content]" |
| Finish button | "Finish check-in" |
| Transcript area | Live region, announces text as it appears |
| Particles | Decorative, hidden from screen readers |

### Reduce Motion

When enabled:
- Disable blob morph animation (static organic blob)
- Disable particle effects
- Replace with static blob + state icon overlay
- Disable portal transition (instant cut with fade)
- Disable gradient shifts (static per state)
- Keep gentle breathing (accessibility-safe)

### High Contrast Mode

- Orb gains visible 3px border: `#1A2566`
- Transcript area border increases: 2px solid rgba(26, 37, 102, 0.4)
- Buttons gain 3px borders
- Text contrast increases to WCAG AAA
- Particles become more visible or disabled

### Haptic Feedback

| Event | Haptic Type | Intensity |
|-------|-------------|-----------|
| Tap FAB (enter immersive) | Impact | Medium |
| Particle burst | Notification | Light |
| Start listening | Impact | Light |
| AI starts responding | Impact | Light |
| Check-in complete | Success | Medium |
| Swipe exit threshold | Warning | Light |
| State change | Selection | Light |

---

## Stitch Prompt (Copy-Pasteable)

```
Create a mobile app screen for an immersive voice health check-in interface with ORGANIC, WARM design. This is for Ditto healthcare app, Direction B - Warm Wellness Hybrid.

EXACT SPECIFICATIONS:

1. LAYOUT (iPhone 14 Pro, 393x852):
   - Full screen, NO navigation bar, NO tab bar
   - Top left: Close button (X icon), warm frosted glass (cream 70% opacity, blur 12px), 26px icon, 14px border radius, subtle warm border
   - Top right: Timer "0:34", same frosted glass, Nunito 15px bold, warm navy text
   - Center: Large ORGANIC BLOB orb (NOT perfect circle), ~220px width, positioned slightly above center (60px offset up)
   - 12-16 floating particles around orb (golden yellow dots, 4-10px, slowly floating upward)
   - Below orb (36px gap): Status text "I'm listening..." in Nunito 22px bold, warm navy #1A2566
   - Bottom third: Floating transcript card (see below)
   - Bottom center: Warm gradient ghost button "I'm finished", pill shape
   - Below button: "or say 'I'm done'" in grey, Nunito 15px

2. ORGANIC BLOB ORB (CRITICAL - NOT A CIRCLE):
   - Size: ~220px width, ~210px height
   - Shape: ORGANIC BLOB with 6-8 smooth curves, slightly asymmetric (use border-radius: 60% 40% 30% 70% / 60% 30% 70% 40% or similar)
   - Gradient: Radial from top-left (35% 25%)
     - Start: #FFD93D (golden yellow)
     - Middle: #FF8A70 (warm coral)
     - End: #C5B8F5 (soft purple)
   - Glow shadow:
     - 0 24px 72px rgba(255, 217, 61, 0.35)
     - 0 12px 36px rgba(255, 138, 112, 0.25)
   - Inner texture: Organic waveform lines (wobbly, hand-drawn feel) in white 40% opacity
   - The blob should look SOFT, WARM, ORGANIC - not geometric

3. FLOATING PARTICLES:
   - 12-16 particles around the blob orb
   - Size: 4-10px diameter circles
   - Color: Golden yellow with gradient (rgba(255, 217, 61, 0.4) to transparent)
   - Behavior: Slowly floating upward with slight horizontal drift
   - Some particles near orb, some farther (depth)
   - Soft glow on each particle

4. BACKGROUND GRADIENT (RICH WARM MULTI-STOP):
   - Linear gradient, 165 degrees:
     - 0%: #FFD9C0 (warm peach)
     - 30%: #FFE8D9 (soft peach)
     - 70%: #FFF5EB (warm cream)
     - 100%: #FFF8F0 (cream)
   - Subtle, warm, inviting, NOT pure white

5. TRANSCRIPT CARD (BOTTOM):
   - Width: 88% of screen, centered
   - Position: 24px from bottom
   - Background: rgba(255, 248, 240, 0.90) - warm semi-transparent
   - Border: 1px solid rgba(255, 181, 160, 0.20) - warm peachy border
   - Backdrop filter: blur(24px)
   - Border radius: 24px (very rounded)
   - Padding: 18px 22px
   - Shadow: 0 12px 32px rgba(255, 138, 112, 0.12) - warm shadow
   - Content: "I woke up with a headache again this morning, but it's not as bad as yesterday. Maybe a 4 out of 10. I took some advil and..."
     [with golden pulsing dot at end + small particle trail]
   - Text: Nunito 17px weight 600, warm navy #1A2566

6. FINISH BUTTON:
   - Background: Linear gradient 135deg (rgba(255, 248, 240, 0.8) → rgba(255, 232, 217, 0.8))
   - Border: 2px solid rgba(255, 181, 160, 0.25)
   - Backdrop filter: blur(10px)
   - Border radius: 9999px (pill)
   - Padding: 16px 32px
   - Text: "I'm finished", Nunito 17px bold, #1A2566
   - Shadow: 0 6px 16px rgba(255, 138, 112, 0.12)
   - Inset highlight: subtle white glow on top edge

7. TYPOGRAPHY (ALL NUNITO FONT - ROUNDED SANS-SERIF):
   - Status text: Nunito 22px bold, #1A2566
   - Transcript: Nunito 17px weight 600, #1A2566
   - Button: Nunito 17px bold, #1A2566
   - Hint: Nunito 15px weight 600, rgba(26, 37, 102, 0.5)
   - Timer: Nunito 15px bold, rgba(26, 37, 102, 0.65)

8. COLORS (WARM VARIANTS):
   - Warm navy: #1A2566 (lighter than standard Ditto navy)
   - Golden yellow: #FFD93D
   - Warm coral: #FF8A70
   - Soft purple: #C5B8F5
   - Soft peach: #FFB5A0
   - Cream backgrounds: #FFF8F0, #FFFBF5

9. CORNER RADIUS (GENEROUS):
   - Transcript card: 24px
   - Button: 9999px (pill)
   - Close/timer: 14px
   - All corners minimum 12px

10. SHADOWS (WARM-TINTED):
    - All shadows use warm peach/coral tints: rgba(255, 138, 112, X)
    - Orb glow: rgba(255, 217, 61, 0.35) + rgba(255, 138, 112, 0.25)
    - Card shadow: rgba(255, 138, 112, 0.12)
    - Button shadow: rgba(255, 138, 112, 0.12)

11. STATE: LISTENING
    - This screen shows "listening" state
    - Blob orb should feel alive, organic, warm
    - Particles actively floating
    - User is speaking (transcript showing)

12. STYLE REQUIREMENTS:
    - ORGANIC shapes (blob, not circle)
    - WARM aesthetic (peach, cream, golden tones)
    - SOFT and FRIENDLY
    - Hand-drawn quality (not perfectly geometric)
    - Particle life (floating elements)
    - Healthcare companion, but WARM not clinical
    - Partly off-brand (warmer than strict Ditto colors)
    - Generous whitespace and rounded corners

CRITICAL:
- The orb MUST be an organic blob shape, NOT a perfect circle
- Include floating particles around the orb
- Use warm peach/cream/golden color palette
- Nunito font (rounded) for all text
- Rich multi-stop gradient background
- All shadows have warm tints (peach/coral)
- This is WARMER and more ORGANIC than standard Ditto
- Immersive full-screen (no tab bar)

Generate a polished, warm, organic, friendly mobile UI mockup.
```

---

## Accessibility Notes

1. **VoiceOver**: Full support with meaningful descriptions. Particles marked as decorative.

2. **Reduce Motion**: Blob morph and particle effects disabled. Static blob with state icons.

3. **High Contrast**: Increased borders and contrast. Particles more visible or removed.

4. **Haptic Feedback**: Enhanced with particle burst haptics for warmth.

5. **Keyboard Navigation** (iPad): Full support.

6. **Voice-Only Path**: Complete check-in without touching screen.

---

## Summary

Direction B v2 is the **warm compromise** — it keeps Ditto's brand colors recognizable but warms them significantly and adds organic, human-feeling elements. The blob orb (not a perfect circle), floating particles, rich warm gradients, and Nunito typography all create a friendlier, more approachable experience than strict brand adherence. This direction is **partly off-brand** but in service of emotional warmth.

**Best for**: Users who want more warmth and humanity than Direction A, but still want some connection to Ditto's visual identity. The organic shapes and particles make this feel alive and caring.
