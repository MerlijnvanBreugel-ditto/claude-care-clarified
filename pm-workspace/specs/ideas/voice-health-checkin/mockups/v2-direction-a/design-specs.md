# Direction A v2: On-Brand Immersive

**Design Philosophy**: Ditto's exact design system (navy #0D164F, yellow #F3DE70, purple #BEAEF8) applied to the immersive breathing orb paradigm. Warm but brand-safe.

**Version**: 2.0
**Date**: 2026-02-06
**Status**: Ready for Stitch Generation

---

## Overview

Direction A v2 takes the winning immersive wellness paradigm from the panel review and applies **strict Ditto brand adherence**. The breathing orb becomes the interface, navigation is hidden during check-in, and the 4-dimension extraction model is implemented — but all using Ditto's established color palette and design language.

### Design Principles

1. **Immersive but Branded**: Full-screen experience using Ditto's navy/yellow/purple palette
2. **Orb as Identity**: The breathing orb uses Ditto's brand colors as its gradient
3. **Warm Within Constraints**: Rounded corners (20px+) and warm shadows, but with brand colors
4. **Trust Through Familiarity**: Users recognize Ditto immediately
5. **Accessible by Default**: VoiceOver, Reduce Motion, high contrast support

---

## Color System

### Brand Colors (Ditto Core)

| Token | Hex | Usage |
|-------|-----|-------|
| `navy-primary` | `#0D164F` | Orb gradient stop, text, UI elements |
| `yellow-accent` | `#F3DE70` | Orb highlights, celebration accents |
| `purple-soft` | `#BEAEF8` | Orb secondary gradient, soft accents |
| `grey-800` | `#82828A` | Secondary text |
| `grey-900` | `#666670` | Inactive states |

### Background Colors (Warm Variants)

| Token | Hex | Usage |
|-------|-----|-------|
| `bg-warm-white` | `#FFFBF5` | Primary background (not pure white) |
| `bg-cream` | `#FFF8F0` | Card backgrounds |
| `bg-gradient-start` | `#F5F3FF` | Immersive mode gradient start (purple tint) |
| `bg-gradient-end` | `#FFFBF5` | Immersive mode gradient end (warm white) |

### Orb Color States

| State | Gradient | Description |
|-------|----------|-------------|
| Idle | `#BEAEF8` → `#0D164F` | Purple to navy, gentle |
| Listening | `#F3DE70` → `#BEAEF8` | Yellow to purple, vibrant |
| Thinking | `#9B8FD0` → `#666670` | Muted purple to grey |
| Responding | `#F3DE70` → `#FF8A70` | Yellow to warm coral glow |
| Complete | `#7BC47F` → `#F3DE70` | Green to yellow celebration |

---

## Typography

### Font Family
- **Primary**: Inter (Ditto's brand font)
- **Headings**: Inter, weight 600-700
- **Body**: Inter, weight 500 (never 400)
- **Emotional text**: Inter, weight 600, slightly larger tracking

### Type Scale

| Style | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `display` | 36px | 700 | 1.2 | "How are you today?" |
| `h1` | 28px | 600 | 1.3 | Screen titles |
| `h2` | 22px | 600 | 1.4 | Section headers |
| `h3` | 18px | 600 | 1.4 | Dimension card titles |
| `body` | 16px | 500 | 1.6 | Transcript, AI responses |
| `small` | 14px | 500 | 1.5 | Supporting text |
| `caption` | 12px | 500 | 1.4 | Timestamps, hints |

### Status Text Style
- Font: Inter, 20px, weight 600
- Color: `navy-primary` (#0D164F)
- Tracking: 0.02em (slightly loose)
- Center aligned below orb

---

## Orb Design Specifications

### Core Properties

| Property | Value |
|----------|-------|
| Idle size | 180px diameter |
| Listening size | 200px diameter |
| Thinking size | 160px diameter |
| Responding size | 220px diameter |
| Position | Center screen, vertical offset -60px from center |
| Shape | Perfect circle with gradient |

### Gradient Specifications

**Idle State**:
```css
background: radial-gradient(circle at 40% 30%,
  #BEAEF8 0%,
  #9B8FD0 35%,
  #0D164F 100%);
box-shadow: 0 16px 48px rgba(13, 22, 79, 0.20);
```

**Listening State**:
```css
background: radial-gradient(circle at 40% 30%,
  #F3DE70 0%,
  #BEAEF8 60%,
  #9B8FD0 100%);
box-shadow: 0 20px 60px rgba(243, 222, 112, 0.35);
/* Pulse animation: scale 1.0 to 1.15 based on amplitude */
```

**Thinking State**:
```css
background: radial-gradient(circle at 50% 50%,
  #9B8FD0 0%,
  #82828A 50%,
  #666670 100%);
box-shadow: 0 12px 32px rgba(155, 143, 208, 0.15);
animation: gentle-rotate 1.5s ease-in-out infinite;
```

**Responding State**:
```css
background: radial-gradient(circle at 40% 30%,
  #F3DE70 0%,
  #FF8A70 40%,
  #BEAEF8 100%);
box-shadow: 0 24px 72px rgba(243, 222, 112, 0.45);
/* Expanded glow effect */
```

**Complete State**:
```css
/* Morph to checkmark shape */
background: radial-gradient(circle at 40% 30%,
  #7BC47F 0%,
  #F3DE70 100%);
box-shadow: 0 20px 60px rgba(123, 196, 127, 0.35);
animation: checkmark-morph 800ms ease-out;
```

### Animation States

| State | Animation | Duration | Easing |
|-------|-----------|----------|--------|
| Idle | Breathing (scale 1.0 ↔ 1.05) | 4s | ease-in-out |
| Listening | Amplitude pulse (scale 1.0 - 1.15) | Real-time 60fps | linear |
| Thinking | Gentle rotation (0° → 360°) + contract | 1.5s | ease-in-out |
| Responding | Glow expansion + subtle pulse | 2s | ease-in-out |
| Complete | Morph to checkmark | 800ms | cubic-bezier(0.4, 0.0, 0.2, 1) |

### Inner Texture Details

**Idle/Thinking**: Small dots that subtly animate (representing AI "thoughts")
- 8-12 dots
- Color: rgba(255, 255, 255, 0.3)
- Size: 4-8px
- Animation: Slow drift

**Listening**: Waveform texture that responds to voice
- Horizontal lines
- Color: rgba(255, 255, 255, 0.5)
- Height: Varies with amplitude

**Responding**: Radiating glow lines
- 12-16 lines emanating from center
- Color: rgba(255, 255, 255, 0.4)
- Animation: Pulse outward

---

## Background Gradient Specifications

### Immersive Mode Gradient

The full-screen background shifts subtly with orb state:

**Idle Background**:
```css
background: linear-gradient(180deg,
  #F5F3FF 0%,    /* Soft purple tint */
  #FFFBF5 100%   /* Warm white */
);
```

**Listening Background** (warmer):
```css
background: linear-gradient(180deg,
  #FFF8F0 0%,    /* Warm cream */
  #FFFBF5 100%   /* Warm white */
);
```

**Thinking Background** (muted):
```css
background: linear-gradient(180deg,
  #F5F0EB 0%,    /* Cool grey-cream */
  #EDE5DE 100%   /* Muted beige */
);
```

**Responding Background** (bright):
```css
background: linear-gradient(180deg,
  #FFF5EB 0%,    /* Warm peachy */
  #FFE8D9 100%   /* Soft apricot */
);
```

**Complete Background** (celebration):
```css
background: linear-gradient(180deg,
  #FFF8ED 0%,    /* Warm yellow tint */
  #FFFBF0 100%   /* Soft cream */
);
/* Add subtle sparkle overlay */
```

### Gradient Transition
- Duration: 600ms
- Easing: ease-in-out
- Syncs with orb state change

---

## Transcript Area Styling

### Container

| Property | Value |
|----------|-------|
| Position | Fixed bottom, 24px margin |
| Width | 90% of screen, max 500px |
| Background | rgba(255, 251, 245, 0.85) |
| Backdrop filter | blur(20px) |
| Border radius | 20px |
| Padding | 16px 20px |
| Shadow | 0 8px 24px rgba(13, 22, 79, 0.08) |
| Max height | 30% of viewport |
| Overflow | Scroll (hidden scrollbar) |

### Text Styling

**User Text** (what they said):
- Font: Inter, 16px, weight 500
- Color: `#0D164F` (navy)
- Margin bottom: 12px
- Recording indicator: Yellow dot (#F3DE70) with pulse

**AI Text** (response):
- Font: Inter, 16px, weight 500
- Color: `#666670` (grey)
- Margin bottom: 12px
- Streaming cursor: Blinking yellow bar

### Behavior
- Fades in from bottom (200ms) when user starts speaking
- Auto-scrolls as text appears
- Dims slightly (opacity 0.8) when not active focus
- Maximum 2-3 conversation exchanges visible

---

## Button Styling

### Finish Button

**Default State**:
```css
background: transparent;
border: 2px solid rgba(13, 22, 79, 0.15);
color: #0D164F;
font: Inter, 16px, weight 600;
border-radius: 9999px; /* pill shape */
padding: 14px 28px;
box-shadow: 0 4px 12px rgba(13, 22, 79, 0.05);
```

**Hover/Active State**:
```css
background: rgba(13, 22, 79, 0.05);
border-color: rgba(13, 22, 79, 0.25);
transform: scale(0.98);
```

### Position
- Center bottom, 32px from bottom edge
- Above hint text
- Width: auto, min 160px

### Hint Text Below Button
- "or say 'I'm done'"
- Font: Inter, 14px, weight 500
- Color: rgba(13, 22, 79, 0.5)
- Margin top: 8px

---

## Component Specifications

### Close Button (Top Left)

| Property | Value |
|----------|-------|
| Icon | X (close) |
| Size | 24px |
| Color | `#0D164F` |
| Background | rgba(255, 255, 255, 0.6) |
| Backdrop filter | blur(10px) |
| Border radius | 12px |
| Padding | 10px |
| Position | Fixed top-left, 16px margin |

### Timer (Top Right)

| Property | Value |
|----------|-------|
| Font | Inter, 14px, weight 500 |
| Color | rgba(13, 22, 79, 0.6) |
| Background | rgba(255, 255, 255, 0.6) |
| Backdrop filter | blur(10px) |
| Border radius | 12px |
| Padding | 8px 12px |
| Position | Fixed top-right, 16px margin |

### Status Text (Below Orb)

| Property | Value |
|----------|-------|
| Font | Inter, 20px, weight 600 |
| Color | `#0D164F` |
| Text align | Center |
| Margin top | 32px from orb |
| Animation | Fade in/out 300ms |

**Status Messages**:
- Idle: "How are you today?"
- Listening: "I'm listening..."
- Thinking: "Let me think about that..."
- Responding: (empty, text streams below)
- Complete: "Great check-in!"

---

## Session Summary (4 Dimensions)

### Layout Structure

**Success Banner**:
- Background: `#FFF8F0` (cream)
- Border: 2px solid `#F3DE70` (yellow)
- Border radius: 20px
- Padding: 20px
- Text: "Great check-in! 1 min 24 sec"
- Icon: Checkmark in yellow circle

### Dimension Cards

Each dimension has a card:

**Card Structure**:
```
Background: #FFFBF5 (warm white)
Border radius: 20px
Padding: 20px
Shadow: 0 4px 16px rgba(13, 22, 79, 0.06)
Border left: 4px solid [dimension color]
```

**Dimension Colors**:
| Dimension | Accent Color | Border Color |
|-----------|--------------|--------------|
| BODY | Soft coral #FF8A70 | 4px left border |
| MIND | Calm purple #9B8FD0 | 4px left border |
| ACTIONS | Active green #7BC47F | 4px left border |
| CONTEXT | Warm amber #FBBF24 | 4px left border |

### Dimension Card Header
- Title: Inter, 18px, weight 700, uppercase, tracking 0.05em
- Color: Dimension accent color
- Margin bottom: 16px
- Icon: 20px, dimension color

### Symptom Rows (in BODY card)

**Structure**:
```
Name | Severity
─────────────────────
[Severity bar: 10 segments]
Location, duration, details
```

**Styling**:
- Name: Inter, 16px, weight 600, `#0D164F`
- Severity: Inter, 16px, weight 700, `#0D164F`
- Bar: Height 8px, radius 4px
  - Filled: `#FF8A70` (coral)
  - Empty: rgba(255, 138, 112, 0.15)
- Details: Inter, 14px, weight 500, `#82828A`

### Save Button

**Primary CTA**:
```css
background: #0D164F; /* Navy */
color: #FFFFFF;
font: Inter, 18px, weight 600;
border-radius: 16px;
padding: 18px 32px;
box-shadow: 0 8px 24px rgba(13, 22, 79, 0.20);
width: 100%;
margin-top: 24px;
```

**Hover/Active**:
```css
background: #1A2566; /* Lighter navy */
transform: translateY(-2px);
box-shadow: 0 12px 32px rgba(13, 22, 79, 0.30);
```

---

## Screen Specifications

### 1. Immersive Check-in Screen (Idle)

**Layout**:
- Full screen, no navigation
- Background: Warm gradient (#F5F3FF → #FFFBF5)
- Close button: Top left
- Timer: Top right (starts at 0:00)
- Breathing orb: Center, 180px, purple-navy gradient
- Status text: "How are you today?" (navy, 20px, below orb)
- Hint text: "Tap the orb or just start speaking" (grey, 14px)
- Finish button: Bottom, ghost style, "I'm finished"
- Secondary hint: "or say 'I'm done'" (grey, 12px)

**Orb Animation**: Gentle breathing (scale 1.0 ↔ 1.05, 4s cycle)

### 2. Immersive Check-in Screen (Listening)

**Changes from Idle**:
- Background: Shifts warmer (#FFF8F0 → #FFFBF5)
- Orb: Expands to 200px, yellow-purple gradient
- Orb animation: Pulses with voice amplitude (real-time)
- Status text: "I'm listening..."
- Transcript area: Fades in from bottom
  - Shows user's speech in real-time
  - Yellow dot pulse indicator
  - Semi-transparent white background, blur 20px
- Timer: Running

### 3. Immersive Check-in Screen (Thinking)

**Changes**:
- Background: Muted (#F5F0EB → #EDE5DE)
- Orb: Contracts to 160px, muted purple-grey gradient
- Orb animation: Gentle rotation + subtle contract
- Status text: "Let me think about that..."
- Transcript area: Shows completed user text, no indicator

### 4. Immersive Check-in Screen (Responding)

**Changes**:
- Background: Bright warm (#FFF5EB → #FFE8D9)
- Orb: Expands to 220px, yellow-coral gradient with glow
- Orb animation: Radiating glow lines, subtle pulse
- Status text: Empty (text below instead)
- Transcript area: AI response streams word-by-word
  - AI text in grey
  - Blinking yellow cursor while streaming
- New button appears: "Tap to respond" (ghost, above finish button)

### 5. Immersive Check-in Screen (Complete)

**Changes**:
- Background: Celebration gradient (#FFF8ED → #FFFBF0)
- Orb: Morphs from circle to checkmark (800ms animation)
  - Green-yellow gradient
  - Glow effect
- Status text: "Great check-in!"
- Subtext: "Here's what I captured."
- Button: "See Summary" (primary navy button)
- Finish button hidden

### 6. Session Summary Screen

**Header**:
- Back button (top left)
- Title: "Check-in Complete" (navy, 28px, center)
- Edit button (top right)

**Success Banner** (see above for specs)

**Scrollable Content**:
- BODY card
  - Symptoms with severity bars
  - Vitals
- MIND card
  - Mood
  - Cognitive state
  - Stress level
- ACTIONS card
  - Medications (with checkmarks)
  - Self-care notes
- CONTEXT card
  - Sleep data
  - Environmental observations

**Footer**:
- "View Full Transcript" link (navy, 16px, center)
- "Save Check-in" button (primary, full width)

### 7. Home Integration

**Check-in FAB** (triggers portal transition):
- Position: Bottom right, 24px margin
- Size: 64px diameter
- Background: `#0D164F` (navy)
- Icon: Orb symbol (simplified 3-circle icon) in `#F3DE70` (yellow)
- Shadow: 0 8px 24px rgba(13, 22, 79, 0.25)
- Animation: Subtle breathing (scale 1.0 ↔ 1.03)

**Recent Check-in Cards** (updated for 4 dimensions):
```
Background: #FFFBF5
Border radius: 20px
Padding: 16px
Shadow: 0 4px 12px rgba(13, 22, 79, 0.06)

Timestamp: Inter, 14px, weight 600, #0D164F
Body: Inter, 14px, weight 500, #82828A
Mind: Inter, 14px, weight 500, #82828A
Actions: Inter, 14px, weight 500, #82828A
Context: Inter, 14px, weight 500, #82828A
Preview: Inter, 14px, weight 500, #666670, italic
```

---

## Portal Transition Animation

### Home → Immersive (700ms)

**Sequence**:
1. **0ms**: User taps FAB
   - Haptic: Medium impact
   - FAB pulses once

2. **0-200ms**: Home content scales down and fades
   - Scale: 1.0 → 0.85
   - Opacity: 1.0 → 0.0
   - Tab bar slides down

3. **100-400ms**: Gradient expands from FAB position
   - Radial gradient expands
   - Shifts from navy (#0D164F) to warm gradient

4. **300-600ms**: Orb materializes
   - Scale: 0.0 → 1.0 (spring easing, slight overshoot)
   - Opacity: 0.0 → 1.0
   - Rotation: 0° → 360° (single spin)

5. **500-700ms**: UI elements fade in
   - Close button, timer, status text
   - Opacity: 0.0 → 1.0
   - Translate Y: 10px → 0px

**Easing**: cubic-bezier(0.4, 0.0, 0.2, 1)

### Immersive → Home (700ms, reverse)

Same sequence in reverse when user completes or exits.

---

## Accessibility Specifications

### VoiceOver Support

| Element | Announcement |
|---------|--------------|
| Close button | "Exit check-in" |
| Orb (idle) | "Health companion orb, currently idle. Tap to begin or start speaking." |
| Orb (listening) | "Listening to your health check-in. Recording in progress." |
| Orb (thinking) | "Processing your response. Please wait." |
| Orb (responding) | "AI is responding. [AI text content]" |
| Finish button | "Finish check-in" |
| Transcript area | Live region, announces text as it appears |

### Reduce Motion

When enabled:
- Disable orb breathing animation
- Replace with static orb + state icon overlay:
  - Idle: No icon
  - Listening: Microphone icon
  - Thinking: 3 dots
  - Responding: Speaker icon
  - Complete: Checkmark
- Disable portal transition animation
  - Instant cut instead
- Disable gradient shifts
  - Static gradient per state

### High Contrast Mode

- Orb gains visible 2px border: `#0D164F`
- Transcript area gains 1px border: rgba(13, 22, 79, 0.3)
- Buttons gain increased border: 3px
- Text contrast increases to WCAG AAA (7:1 minimum)

### Haptic Feedback

| Event | Haptic Type | Intensity |
|-------|-------------|-----------|
| Tap FAB (enter immersive) | Impact | Medium |
| Start listening | Impact | Light |
| AI starts responding | Impact | Light |
| Check-in complete | Success | Medium |
| Swipe past exit threshold | Warning | Light |
| State change | Selection | Light |

---

## Stitch Prompt (Copy-Pasteable)

```
Create a mobile app screen for an immersive voice health check-in interface. This is for Ditto, a healthcare companion app.

EXACT SPECIFICATIONS:

1. LAYOUT (iPhone 14 Pro, 393x852):
   - Full screen, NO navigation bar, NO tab bar
   - Top left: Small close button (X icon), frosted glass background (white 60% opacity, blur 10px), 24px icon, 12px border radius
   - Top right: Timer display "0:34", same frosted glass style, Inter font 14px medium, navy text
   - Center: Large breathing orb, 200px diameter, positioned slightly above true center (60px offset up)
   - Below orb (32px gap): Status text "I'm listening..." in Inter 20px semibold, navy #0D164F, center aligned
   - Bottom third: Floating transcript card (see specs below)
   - Bottom center: Ghost button "I'm finished", pill shape, transparent with 2px navy border, Inter 16px semibold
   - Below button: Hint text "or say 'I'm done'" in grey, Inter 14px

2. BREATHING ORB DESIGN (CRITICAL):
   - Size: 200px diameter, perfect circle
   - Gradient: Radial gradient from top-left (40% 30%) to bottom-right
     - Start: #F3DE70 (Ditto yellow)
     - Middle: #BEAEF8 (Ditto purple)
     - End: #9B8FD0 (muted purple)
   - Glow shadow: 0 20px 60px rgba(243, 222, 112, 0.35)
   - Inner texture: Horizontal waveform lines in white 50% opacity, suggesting voice activity
   - Animation state: Pulsing (showing it's responsive to voice input)

3. BACKGROUND GRADIENT (WARM):
   - Linear gradient, top to bottom:
     - Start: #FFF8F0 (warm cream)
     - End: #FFFBF5 (warm white, NOT pure white)
   - Subtle, calming, NOT pure white

4. TRANSCRIPT CARD (BOTTOM):
   - Width: 90% of screen width, centered
   - Position: 24px from bottom of screen (above finish button which is 32px from bottom + button height)
   - Background: rgba(255, 251, 245, 0.85) - semi-transparent warm white
   - Backdrop filter: blur(20px)
   - Border radius: 20px
   - Padding: 16px 20px
   - Shadow: 0 8px 24px rgba(13, 22, 79, 0.08) - warm navy tint
   - Content:
     "I woke up with a headache again this morning, but it's not as bad as yesterday. Maybe a 4 out of 10. I took some advil and..."
     [with pulsing yellow dot at the end indicating recording]
   - Text: Inter 16px medium, navy #0D164F
   - Max height: 30% of screen, scroll if needed

5. TYPOGRAPHY (ALL INTER FONT):
   - Status text: Inter 20px semibold, #0D164F
   - Transcript: Inter 16px medium, #0D164F
   - Button: Inter 16px semibold, #0D164F
   - Hint text: Inter 14px medium, rgba(13, 22, 79, 0.5)
   - Timer: Inter 14px medium, rgba(13, 22, 79, 0.6)

6. COLORS (DITTO BRAND - EXACT):
   - Navy: #0D164F (primary brand color)
   - Yellow: #F3DE70 (accent)
   - Purple: #BEAEF8 (soft accent)
   - Warm white background: #FFFBF5 (NOT #FFFFFF)
   - Grey text: #82828A

7. CORNER RADIUS (WARM AESTHETIC):
   - Cards: 20px minimum
   - Buttons: 9999px (pill)
   - Small elements: 12px minimum
   - NEVER use corners less than 12px

8. SHADOWS (WARM-TINTED):
   - All shadows use warm navy tint: rgba(13, 22, 79, X)
   - Orb glow: rgba(243, 222, 112, 0.35)
   - Card shadow: rgba(13, 22, 79, 0.08)
   - Button shadow: rgba(13, 22, 79, 0.05)

9. STATE: LISTENING
   - This screen shows the "listening" state
   - Orb should feel alive and responsive
   - User is currently speaking (transcript showing real-time)

10. STYLE REQUIREMENTS:
    - Clean, modern, immersive
    - Healthcare companion, NOT clinical
    - Warm and trustworthy
    - Brand-adherent (Ditto colors)
    - Generous whitespace
    - Focus on the orb as THE interface element

CRITICAL:
- The orb is the hero element - make it beautiful and prominent
- Use ONLY Ditto's brand colors (navy, yellow, purple)
- Background must be warm (#FFFBF5), never pure white
- All corners must be rounded (20px+ for cards)
- Shadows must have warm/navy tints, never grey
- This is immersive - no tab bar, no navigation chrome
- Inter font for all text, weights 500-700 only

Generate a polished, production-ready mobile UI mockup.
```

---

## Accessibility Notes

1. **VoiceOver**: Every element has meaningful labels. Orb state changes are announced via ARIA live regions.

2. **Reduce Motion**: All animations can be disabled. Orb becomes static with state icon overlays.

3. **High Contrast**: Borders and shadows increase. Text meets WCAG AAA standards.

4. **Haptic Feedback**: Tactile feedback for state changes helps users with visual impairments.

5. **Keyboard Navigation** (iPad): Space to toggle recording, Enter to finish, Escape to exit.

6. **Voice-Only Path**: Entire check-in can be completed without touching screen. "I'm done" ends session.

---

## Summary

Direction A v2 delivers the immersive wellness experience that won the panel review, but stays true to Ditto's brand identity. The breathing orb uses Ditto's exact colors (navy, yellow, purple), the typography is Inter throughout, and the design feels like a natural extension of the existing app. This direction prioritizes **trust through brand familiarity** while embracing the emotional calm of the immersive paradigm.

**Best for**: Users who value brand consistency, clinical trust, and want to feel confident they're using "Ditto" even in this new paradigm.
