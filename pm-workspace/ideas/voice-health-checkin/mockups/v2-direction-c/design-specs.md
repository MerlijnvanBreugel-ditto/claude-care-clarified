# Direction C v2: Full Duolingo Immersive

**Design Philosophy**: Maximum warmth, playful mascot, celebration moments. Warm coral (#FF6B4A), accent yellow (#FFD93D), soft green (#7BC47F). Hand-drawn illustration style.

**Version**: 2.0
**Date**: 2026-02-06
**Status**: Ready for Stitch Generation

---

## Overview

Direction C v2 is the **boldest departure from Ditto's brand** — it fully embraces the "Duolingo for health" vision with maximum warmth, playful character-driven design, and celebration-focused UX. The orb has a friendly face, illustrations are hand-drawn style, colors are warm and inviting (coral, yellow, green), and every interaction feels like a supportive friend cheering you on.

### Design Principles

1. **Maximum Warmth**: Coral primary, golden yellow accents, soft greens
2. **Character-Driven**: The orb has personality (friendly face, expressions)
3. **Celebration Culture**: Small wins are celebrated with joy
4. **Hand-Drawn Quality**: Illustrations feel human-made, not vector-perfect
5. **Playful but Caring**: Fun without being childish, supportive without being clinical

---

## Color System

### Primary Colors (Warm & Friendly)

| Token | Hex | Usage | Inspiration |
|-------|-----|-------|-------------|
| `coral-primary` | `#FF6B4A` | Primary brand color, orb, buttons | Duolingo coral |
| `coral-light` | `#FF8A70` | Hover states, lighter variant | — |
| `coral-deep` | `#E55A3A` | Active/pressed states | — |
| `yellow-warm` | `#FFD93D` | Accent, celebration, highlights | Duolingo yellow |
| `green-soft` | `#7BC47F` | Success, progress, growth | Soft health green |
| `green-light` | `#A8E6A3` | Light success variant | — |

### Secondary Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `purple-playful` | `#9B8FD0` | Calm moments, thinking state |
| `peach-soft` | `#FFB5A0` | Warm gradient stops |
| `blue-calm` | `#60A5FA` | Info, optional accent |
| `navy-text` | `#2C3E50` | Primary text (warmer than black) |
| `grey-warm` | `#6B7280` | Secondary text |

### Background Colors (Off-White Warm Base)

| Token | Hex | Usage |
|-------|-----|-------|
| `bg-warm` | `#FFFBF5` | Primary background (NOT pure white) |
| `bg-cream` | `#FFF8F0` | Card backgrounds |
| `bg-peach-light` | `#FFE8D9` | Warm gradient start |
| `bg-yellow-light` | `#FFF5E0` | Celebration backgrounds |
| `bg-green-light` | `#E8F5E9` | Success/completion backgrounds |

### Orb Character Color States

| State | Colors | Expression | Description |
|-------|--------|------------|-------------|
| Idle | Coral → Peach → Yellow | Friendly smile | Inviting, ready |
| Listening | Yellow → Coral → Peach | Attentive (eyes wide) | Engaged, curious |
| Thinking | Purple → Lavender → Grey | Thoughtful (eyes looking up) | Processing |
| Responding | Yellow → Golden → Orange | Excited (bright eyes) | Sharing, animated |
| Complete | Green → Light Green → Yellow | Celebrating (big smile) | Joyful, proud |

---

## Typography

### Font Family
- **Primary**: Quicksand (rounded, friendly, playful)
- **Fallback**: Nunito (if Quicksand unavailable)
- **Avoid**: Geometric fonts (too cold), serifs (too formal)

### Type Scale

| Style | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `display` | 40px | 700 | 1.2 | "How are you today?" |
| `h1` | 32px | 700 | 1.3 | Screen titles |
| `h2` | 26px | 600 | 1.4 | Section headers |
| `h3` | 20px | 600 | 1.4 | Dimension card titles |
| `body` | 18px | 500 | 1.6 | Transcript, AI responses |
| `small` | 16px | 500 | 1.5 | Supporting text |
| `caption` | 14px | 500 | 1.4 | Timestamps, hints |

### Status Text Style
- Font: Quicksand, 24px, weight 700
- Color: `#2C3E50` (navy text)
- Tracking: 0.01em
- Center aligned below orb
- Text shadow: 0 2px 6px rgba(255, 107, 74, 0.15)

---

## Orb Character Design Specifications

### Core Properties

| Property | Value |
|----------|-------|
| Idle size | 200px diameter |
| Listening size | 220px diameter |
| Thinking size | 180px diameter |
| Responding size | 240px diameter |
| Position | Center screen, vertical offset -60px |
| Shape | Circle with character face |

### Character Face Details

The orb has a **friendly, expressive face**:

**Face Elements**:
- **Eyes**: Large, round, expressive
  - Default: Two dots or circles
  - Listening: Eyes wide, attentive
  - Thinking: Eyes looking up-right
  - Responding: Eyes bright, sparkles
  - Complete: Eyes happy crescents (^_^)
- **Mouth**: Simple curve
  - Default: Gentle smile
  - Listening: Small "o" shape (interested)
  - Thinking: Thoughtful line
  - Responding: Speaking motion (animated)
  - Complete: Big smile
- **Cheeks**: Optional rosy blush circles (adds warmth)
  - Color: rgba(255, 181, 160, 0.6)
  - Size: 20-30px diameter
  - Position: Mid-face, left and right

**Face Styling**:
- Eyes: `#2C3E50` (navy), 16-20px diameter
- Mouth: 3-4px stroke, `#2C3E50`
- Cheeks (blush): Soft pink circles
- White highlights in eyes for life

### Gradient Specifications

**Idle State**:
```css
background: radial-gradient(circle at 35% 25%,
  #FF6B4A 0%,
  #FFB5A0 50%,
  #FFD93D 100%);
box-shadow:
  0 20px 60px rgba(255, 107, 74, 0.30),
  0 8px 24px rgba(255, 217, 61, 0.20);
```

**Listening State**:
```css
background: radial-gradient(circle at 35% 25%,
  #FFD93D 0%,
  #FF8A70 50%,
  #FFB5A0 100%);
box-shadow:
  0 24px 72px rgba(255, 217, 61, 0.40),
  0 12px 36px rgba(255, 138, 112, 0.25);
/* Pulse with amplitude, face animated */
```

**Thinking State**:
```css
background: radial-gradient(circle at 50% 50%,
  #9B8FD0 0%,
  #C5B8F5 60%,
  #B8A8E8 100%);
box-shadow:
  0 16px 48px rgba(155, 143, 208, 0.25);
animation: gentle-bob 1.5s ease-in-out infinite;
/* Face looks up, thoughtful */
```

**Responding State**:
```css
background: radial-gradient(circle at 35% 25%,
  #FFD93D 0%,
  #FFBF3D 40%,
  #FF8A70 100%);
box-shadow:
  0 28px 80px rgba(255, 217, 61, 0.45),
  0 14px 40px rgba(255, 138, 112, 0.30),
  0 0 60px rgba(255, 191, 61, 0.25); /* Extra golden glow */
/* Face animated speaking, eyes bright */
```

**Complete State**:
```css
/* Morph with celebration animation */
background: radial-gradient(circle at 35% 25%,
  #7BC47F 0%,
  #A8E6A3 50%,
  #FFD93D 100%);
box-shadow:
  0 24px 72px rgba(123, 196, 127, 0.40),
  0 12px 36px rgba(255, 217, 61, 0.30);
animation: celebration-bounce 1s ease-out;
/* Face celebrating: big smile, sparkles around */
```

### Animation States

| State | Animation | Duration | Easing | Face |
|-------|-----------|----------|--------|------|
| Idle | Gentle breathing + slight bob | 4s | ease-in-out | Friendly smile |
| Listening | Pulse with amplitude + face reacts | Real-time 60fps | linear | Eyes wide, interested |
| Thinking | Gentle bob + rotate slightly | 1.5s | ease-in-out | Eyes up, thoughtful |
| Responding | Glow pulse + face talks | 2s | ease-in-out | Mouth animates, eyes bright |
| Complete | Bounce + confetti burst | 1s | cubic-bezier(0.68, -0.55, 0.265, 1.55) | Big smile, happy |

### Confetti & Celebration Effects

**Complete State Celebration**:
- Confetti pieces: 20-30 pieces
- Colors: Yellow, green, coral, peach
- Shapes: Circles, squares, triangles (hand-drawn style)
- Size: 8-16px
- Animation: Burst from orb center, fall with rotation
- Duration: 2s
- Gravity effect

**Sparkles (Responding State)**:
- 6-8 sparkles around orb
- Star shapes (4-point, hand-drawn)
- Color: Golden yellow with white center
- Size: 10-16px
- Animation: Twinkle + rotate
- Random positions around orb

---

## Background Gradient Specifications

### Immersive Mode Gradient (Warm & Playful)

**Idle Background**:
```css
background: linear-gradient(160deg,
  #FFE8D9 0%,     /* Warm peach */
  #FFF5E0 35%,    /* Soft yellow-cream */
  #FFFBF5 75%,    /* Warm white */
  #FFF8F0 100%    /* Cream */
);
```

**Listening Background** (brighter, more energetic):
```css
background: linear-gradient(160deg,
  #FFD9C0 0%,     /* Brighter peach */
  #FFF0D6 30%,    /* Golden cream */
  #FFF8F0 70%,    /* Cream */
  #FFFBF5 100%    /* Warm white */
);
```

**Thinking Background** (calmer, purple tint):
```css
background: linear-gradient(160deg,
  #F0E8F5 0%,     /* Soft lavender */
  #F5F0FF 30%,    /* Light purple-white */
  #FFFBF5 70%,    /* Warm white */
  #FFF8F0 100%    /* Cream */
);
```

**Responding Background** (warm, golden):
```css
background: linear-gradient(160deg,
  #FFE4BA 0%,     /* Golden */
  #FFD9C0 30%,    /* Peach */
  #FFF5E0 70%,    /* Soft yellow-cream */
  #FFF8F0 100%    /* Cream */
);
```

**Complete Background** (celebration, green-yellow):
```css
background: linear-gradient(160deg,
  #E8F5E9 0%,     /* Soft green */
  #FFF5E0 30%,    /* Yellow-cream */
  #FFFBF5 70%,    /* Warm white */
  #FFF8F0 100%    /* Cream */
);
/* Add confetti overlay */
```

### Gradient Transition
- Duration: 700ms
- Easing: ease-in-out
- Syncs with orb state and face expression change

---

## Transcript Area Styling

### Container

| Property | Value |
|----------|-------|
| Position | Fixed bottom, 24px margin |
| Width | 88% of screen, max 500px |
| Background | rgba(255, 248, 240, 0.92) |
| Border | 2px solid rgba(255, 107, 74, 0.15) (coral tint) |
| Backdrop filter | blur(20px) |
| Border radius | 24px |
| Padding | 20px 24px |
| Shadow | 0 12px 32px rgba(255, 107, 74, 0.12) |
| Max height | 32% of viewport |
| Overflow | Scroll (hidden scrollbar) |

### Text Styling

**User Text**:
- Font: Quicksand, 18px, weight 600
- Color: `#2C3E50` (navy text)
- Margin bottom: 16px
- Recording indicator: Animated waveform icon (coral) or pulsing yellow dot with bounce

**AI Text**:
- Font: Quicksand, 18px, weight 500
- Color: `#6B7280` (warm grey)
- Margin bottom: 16px
- Streaming cursor: Animated blinking coral bar with glow

### Behavior
- Fades in from bottom (250ms) with slight bounce
- Character appears letter-by-letter (typewriter effect optional)
- Auto-scrolls smoothly
- Glows when active (border becomes coral)
- Slight shadow animation on appearance

---

## Button Styling

### Finish Button

**Default State**:
```css
background: linear-gradient(135deg,
  rgba(255, 248, 240, 0.85) 0%,
  rgba(255, 232, 217, 0.85) 100%);
border: 3px solid rgba(255, 107, 74, 0.30);
color: #FF6B4A; /* Coral */
font: Quicksand, 18px, weight 700;
border-radius: 9999px; /* pill */
padding: 18px 36px;
box-shadow:
  0 6px 18px rgba(255, 107, 74, 0.15),
  inset 0 2px 0 rgba(255, 255, 255, 0.6);
backdrop-filter: blur(12px);
```

**Hover/Active State**:
```css
background: linear-gradient(135deg,
  rgba(255, 232, 217, 0.95) 0%,
  rgba(255, 223, 200, 0.95) 100%);
border-color: rgba(255, 107, 74, 0.45);
transform: scale(0.96) translateY(2px);
box-shadow:
  0 4px 12px rgba(255, 107, 74, 0.20);
```

### Position
- Center bottom, 40px from bottom edge
- Above hint text
- Width: auto, min 200px

### Hint Text Below Button
- "or say 'I'm done'"
- Font: Quicksand, 16px, weight 600
- Color: rgba(44, 62, 80, 0.5)
- Margin top: 12px

---

## Component Specifications

### Close Button (Top Left)

| Property | Value |
|----------|-------|
| Icon | X (close), rounded stroke, hand-drawn style |
| Size | 28px |
| Color | `#FF6B4A` (coral) |
| Background | rgba(255, 248, 240, 0.85) |
| Border | 2px solid rgba(255, 107, 74, 0.20) |
| Backdrop filter | blur(12px) |
| Border radius | 16px |
| Padding | 12px |
| Position | Fixed top-left, 20px margin |
| Shadow | 0 4px 12px rgba(255, 107, 74, 0.12) |

### Timer (Top Right)

| Property | Value |
|----------|-------|
| Font | Quicksand, 16px, weight 700 |
| Color | rgba(44, 62, 80, 0.65) |
| Background | rgba(255, 248, 240, 0.85) |
| Border | 2px solid rgba(255, 107, 74, 0.20) |
| Backdrop filter | blur(12px) |
| Border radius | 16px |
| Padding | 10px 16px |
| Position | Fixed top-right, 20px margin |
| Shadow | 0 4px 12px rgba(255, 107, 74, 0.12) |

### Status Text (Below Orb)

| Property | Value |
|----------|-------|
| Font | Quicksand, 24px, weight 700 |
| Color | `#2C3E50` |
| Text align | Center |
| Margin top | 40px from orb |
| Text shadow | 0 2px 6px rgba(255, 107, 74, 0.15) |
| Animation | Fade + gentle bounce (scale 0.95 → 1.0) |

**Status Messages**:
- Idle: "How are you today?" (with small heart or sparkle emoji optional)
- Listening: "I'm listening..."
- Thinking: "Let me think about that..."
- Responding: (empty, text streams)
- Complete: "Great check-in!" (with celebration emoji optional)

---

## Session Summary (4 Dimensions)

### Layout Structure

**Success Banner**:
- Background: Linear gradient 135deg (#E8F5E9 → #FFF5E0)
- Border: 3px solid `#7BC47F` (green)
- Border radius: 24px
- Padding: 24px
- Shadow: 0 8px 24px rgba(123, 196, 127, 0.20)
- Icon: Large checkmark in gradient circle (green → yellow), hand-drawn style
- Text: Quicksand 20px weight 700
- Confetti pieces around banner (decorative)

### Dimension Cards

**Card Structure**:
```css
background: linear-gradient(135deg,
  #FFFBF5 0%,
  #FFF8F0 100%);
border: 2px solid [dimension color at 20% opacity];
border-radius: 24px;
padding: 24px;
box-shadow:
  0 6px 20px rgba(255, 107, 74, 0.10),
  inset 0 1px 0 rgba(255, 255, 255, 0.8);
position: relative;
/* Small hand-drawn icon in top-right corner */
```

**Dimension Colors & Icons**:
| Dimension | Accent Color | Icon (Hand-Drawn Style) |
|-----------|--------------|-------------------------|
| BODY | Warm coral #FF6B4A | Heart or body silhouette |
| MIND | Playful purple #9B8FD0 | Brain or thought cloud |
| ACTIONS | Fresh green #7BC47F | Checkmark or pill |
| CONTEXT | Warm yellow #FFD93D | Sun or moon |

### Dimension Card Header
- Title: Quicksand, 20px, weight 800, uppercase, tracking 0.1em
- Color: Dimension accent color
- Text shadow: 0 1px 2px rgba(255, 255, 255, 0.8)
- Margin bottom: 20px
- Icon: 28px, hand-drawn style, dimension color, top-right corner of card

### Symptom Rows (in BODY card)

**Structure**:
```
Name | Severity
─────────────────────
[Fun severity bar with faces/emoji]
Location, duration, details
```

**Styling**:
- Name: Quicksand, 18px, weight 700, `#2C3E50`
- Severity: Quicksand, 18px, weight 800, `#FF6B4A`
- Bar: Height 12px, radius 6px
  - Filled: Gradient (#FF6B4A → #FFD93D)
  - Empty: rgba(255, 107, 74, 0.15)
  - Optional: Small face emoji at end (1-3: happy, 4-7: neutral, 8-10: sad)
  - Shadow on filled: 0 2px 6px rgba(255, 107, 74, 0.25)
- Details: Quicksand, 16px, weight 600, `#6B7280`

### Save Button

**Primary CTA**:
```css
background: linear-gradient(135deg,
  #FF6B4A 0%,
  #FF8A70 100%);
color: #FFFFFF;
font: Quicksand, 20px, weight 700;
border-radius: 20px;
padding: 22px 40px;
box-shadow:
  0 10px 28px rgba(255, 107, 74, 0.30),
  inset 0 2px 0 rgba(255, 255, 255, 0.25);
width: 100%;
margin-top: 32px;
position: relative;
/* Optional: small sparkle icon on right side */
```

**Hover/Active**:
```css
background: linear-gradient(135deg,
  #FF8A70 0%,
  #FFA590 100%);
transform: translateY(-3px) scale(1.02);
box-shadow:
  0 14px 36px rgba(255, 107, 74, 0.40),
  inset 0 2px 0 rgba(255, 255, 255, 0.25);
```

---

## Screen Specifications

### 1. Immersive Check-in Screen (Idle)

**Layout**:
- Full screen, no navigation
- Background: Warm gradient (#FFE8D9 → #FFF5E0 → #FFFBF5 → #FFF8F0)
- Close button: Top left (coral border, warm background)
- Timer: Top right (0:00, coral border)
- Character orb: Center, 200px, coral-peach-yellow gradient with friendly face (smile)
- Status text: "How are you today?" (navy, 24px, below orb)
- Hint text: "Tap the orb or just start speaking" (grey, 16px)
- Finish button: Bottom, warm gradient style with coral border
- Secondary hint: "or say 'I'm done'"

**Orb Animation**: Gentle breathing + slight bob, face smiling

### 2. Immersive Check-in Screen (Listening)

**Changes from Idle**:
- Background: Brighter (#FFD9C0 → #FFF0D6 → #FFF8F0)
- Orb: Expands to 220px, yellow-coral-peach gradient
- Orb face: Eyes wide, small "o" mouth (interested expression)
- Orb animation: Pulses with amplitude
- Status text: "I'm listening..."
- Transcript area: Fades in with bounce
  - Coral border glow
  - Animated waveform or pulsing yellow dot
- Timer: Running

### 3. Immersive Check-in Screen (Thinking)

**Changes**:
- Background: Calmer (#F0E8F5 → #F5F0FF → #FFFBF5)
- Orb: Contracts to 180px, purple-lavender gradient
- Orb face: Eyes looking up-right, thoughtful line mouth
- Orb animation: Gentle bob + slight tilt
- Status text: "Let me think about that..."
- Transcript: Shows completed text

### 4. Immersive Check-in Screen (Responding)

**Changes**:
- Background: Warm golden (#FFE4BA → #FFD9C0 → #FFF5E0)
- Orb: Expands to 240px, golden-yellow-coral gradient with glow
- Orb face: Eyes bright with sparkles, mouth animated (speaking)
- 6-8 sparkles around orb (4-point stars, rotating)
- Orb animation: Glow pulse + face talking
- Status text: Empty
- Transcript: AI response streams with animated cursor
- New button: "Tap to respond" (ghost warm style)

### 5. Immersive Check-in Screen (Complete)

**Changes**:
- Background: Celebration (#E8F5E9 → #FFF5E0 → #FFFBF5) with confetti overlay
- Orb: Bounces, green-light green-yellow gradient
- Orb face: Big happy smile (^_^), eyes crescents
- Confetti burst: 20-30 pieces falling (yellow, green, coral, hand-drawn shapes)
- Status text: "Great check-in!"
- Subtext: "Here's what I captured."
- Button: "See Summary" (coral gradient button with sparkle)

### 6. Session Summary Screen

**Header**:
- Back button (coral border, warm background)
- Title: "Check-in Complete" (navy, 32px, Quicksand)
- Edit button (coral border)
- Optional: Small celebration illustration

**Success Banner** (green-yellow gradient with confetti)

**Scrollable Content**:
- BODY card (coral accent, heart icon)
- MIND card (purple accent, brain icon)
- ACTIONS card (green accent, checkmark icon)
- CONTEXT card (yellow accent, sun icon)

All cards have hand-drawn style icons and warm gradients.

**Footer**:
- "View Full Transcript" link (coral, 18px, Quicksand)
- "Save Check-in" button (coral gradient with sparkle)

### 7. Home Integration

**Check-in FAB**:
- Position: Bottom right, 24px margin
- Size: 72px diameter
- Background: Gradient (coral → light coral)
- Icon: Simplified character orb face (smiling) in yellow/white
- Shadow: 0 10px 30px rgba(255, 107, 74, 0.35)
- Animation: Gentle breathing + occasional wink or blink
- Optional: Small sparkle that appears periodically

**Recent Check-in Cards**:
```css
background: linear-gradient(135deg,
  #FFFBF5 0%,
  #FFF8F0 100%);
border: 2px solid rgba(255, 107, 74, 0.15);
border-radius: 24px;
padding: 20px;
box-shadow: 0 6px 18px rgba(255, 107, 74, 0.08);
border-left: 5px solid [dimension color];
position: relative;
/* Small hand-drawn emoji or icon in corner */
```

---

## Portal Transition Animation

### Home → Immersive (900ms with celebration)

**Sequence**:
1. **0ms**: User taps FAB
   - Haptic: Medium impact
   - FAB bounces with excitement
   - Small sparkle burst from FAB

2. **0-300ms**: Home content scales + fades with bounce
   - Scale: 1.0 → 0.75
   - Opacity: 1.0 → 0.0
   - Slight rotation: 0° → -5°
   - Tab bar slides down with bounce

3. **150-550ms**: Warm gradient expands from FAB
   - Radial gradient expands with pulse
   - Sparkles trail the expansion
   - Shifts to immersive gradient

4. **400-800ms**: Character orb materializes with personality
   - Scale: 0.0 → 1.0 (bounce easing, overshoot)
   - Opacity: 0.0 → 1.0
   - Rotation: 0° → 360° + slight wobble
   - Face fades in: neutral → smile
   - Small sparkles appear around orb

5. **700-900ms**: UI elements fade in with bounce
   - Close, timer, status text
   - Opacity: 0.0 → 1.0
   - Translate Y: 20px → 0px
   - Bounce on arrival
   - Status text waves in

**Easing**: cubic-bezier(0.68, -0.55, 0.265, 1.55) (playful bounce)

### Immersive → Home (900ms, reverse with celebration)

Same sequence in reverse. Orb waves goodbye (face animation) before disappearing.

---

## Accessibility Specifications

### VoiceOver Support

| Element | Announcement |
|---------|--------------|
| Close button | "Exit check-in" |
| Character orb (idle) | "Your friendly health companion is ready. The character is smiling and waiting. Tap to begin or start speaking." |
| Character orb (listening) | "Your companion is listening carefully. Recording in progress." |
| Character orb (thinking) | "Your companion is thinking about what you said. Please wait." |
| Character orb (responding) | "Your companion is responding. [AI text content]" |
| Finish button | "Finish check-in" |
| Transcript area | Live region, announces text |
| Confetti/sparkles | Decorative, hidden from screen readers |

### Reduce Motion

When enabled:
- Disable all bounce animations
- Disable confetti and sparkles
- Character orb face remains but doesn't animate
- Replace state with static face expressions + icons
- Portal transition becomes simple fade
- Gradient shifts disabled (static per state)

### High Contrast Mode

- Orb gains 3px border: `#FF6B4A`
- Character face becomes higher contrast (darker)
- Transcript area border: 3px solid rgba(255, 107, 74, 0.5)
- Buttons gain 4px borders
- Text contrast meets WCAG AAA
- Confetti/sparkles have higher contrast or removed

### Haptic Feedback

| Event | Haptic Type | Intensity | Notes |
|-------|-------------|-----------|-------|
| Tap FAB (enter) | Impact | Medium | Excitement |
| Sparkle burst | Notification | Light | Playful |
| Start listening | Impact | Light | Engaged |
| AI starts responding | Impact | Light | Attention |
| Check-in complete | Success | Medium | Celebration |
| Confetti burst | Notification | Light | Joy |
| Swipe exit threshold | Warning | Light | Caution |
| State change | Selection | Light | Feedback |

---

## Stitch Prompt (Copy-Pasteable)

```
Create a mobile app screen for an immersive voice health check-in with PLAYFUL, CHARACTER-DRIVEN design inspired by Duolingo. Maximum warmth and friendliness. This is Direction C - Full Duolingo Immersive.

EXACT SPECIFICATIONS:

1. LAYOUT (iPhone 14 Pro, 393x852):
   - Full screen, NO navigation bar, NO tab bar
   - Top left: Close button (X), warm frosted glass, coral border (2px #FF6B4A at 20% opacity), 28px icon, 16px radius
   - Top right: Timer "0:34", same style, Quicksand 16px bold
   - Center: Large CHARACTER ORB with friendly face, 220px diameter, positioned slightly above center (60px up)
   - 6-8 sparkles around orb (4-point stars, golden yellow, rotating slowly)
   - Below orb (40px gap): Status text "I'm listening..." in Quicksand 24px bold, navy #2C3E50
   - Bottom third: Transcript card with coral border glow
   - Bottom center: Warm gradient button "I'm finished", coral border, pill shape
   - Below button: "or say 'I'm done'" in grey

2. CHARACTER ORB WITH FACE (CRITICAL):
   - Size: 220px diameter, perfect circle
   - FRIENDLY FACE with expression:
     - Eyes: Two round eyes (16-18px diameter, navy #2C3E50), positioned upper-third
     - Eyes state: WIDE and ATTENTIVE (listening state), with white sparkle highlights
     - Mouth: Small "o" shape (interested/engaged), 3px stroke, navy
     - Cheeks: Two rosy blush circles (25px diameter, soft pink rgba(255, 181, 160, 0.6))
     - The face should look FRIENDLY, ENGAGED, CURIOUS
   - Gradient: Radial from top-left (35% 25%)
     - Start: #FFD93D (golden yellow)
     - Middle: #FF8A70 (warm coral)
     - End: #FFB5A0 (soft peach)
   - Glow shadow:
     - 0 24px 72px rgba(255, 217, 61, 0.40)
     - 0 12px 36px rgba(255, 138, 112, 0.25)
   - The character should feel ALIVE and FRIENDLY

3. SPARKLES AROUND ORB:
   - 6-8 four-point star sparkles
   - Position: Around orb at various distances
   - Size: 10-16px
   - Color: Golden yellow (#FFD93D) with white center
   - Hand-drawn style (slightly irregular)
   - Some sparkles have small twinkle effect

4. BACKGROUND GRADIENT (WARM, BRIGHT):
   - Linear gradient, 160 degrees:
     - 0%: #FFD9C0 (bright warm peach)
     - 30%: #FFF0D6 (golden cream)
     - 70%: #FFF8F0 (cream)
     - 100%: #FFFBF5 (warm white)
   - Warm, inviting, playful, NOT pure white

5. TRANSCRIPT CARD (BOTTOM):
   - Width: 88% of screen, centered
   - Position: 24px from bottom
   - Background: rgba(255, 248, 240, 0.92) - warm semi-transparent
   - Border: 2px solid rgba(255, 107, 74, 0.15) - coral border
   - Backdrop filter: blur(20px)
   - Border radius: 24px
   - Padding: 20px 24px
   - Shadow: 0 12px 32px rgba(255, 107, 74, 0.12) - coral shadow
   - Content: "I woke up with a headache again this morning, but it's not as bad as yesterday. Maybe a 4 out of 10. I took some advil and..."
     [with animated waveform or pulsing dot at end]
   - Text: Quicksand 18px weight 600, navy #2C3E50
   - The card should feel warm and inviting

6. FINISH BUTTON:
   - Background: Linear gradient 135deg (rgba(255, 248, 240, 0.85) → rgba(255, 232, 217, 0.85))
   - Border: 3px solid rgba(255, 107, 74, 0.30) - coral
   - Backdrop filter: blur(12px)
   - Border radius: 9999px (pill)
   - Padding: 18px 36px
   - Text: "I'm finished", Quicksand 18px bold, coral #FF6B4A
   - Shadow: 0 6px 18px rgba(255, 107, 74, 0.15)
   - Inset highlight: subtle white glow on top

7. TYPOGRAPHY (ALL QUICKSAND FONT - ROUNDED, FRIENDLY):
   - Status text: Quicksand 24px bold, #2C3E50
   - Transcript: Quicksand 18px weight 600, #2C3E50
   - Button: Quicksand 18px bold, #FF6B4A
   - Hint: Quicksand 16px weight 600, rgba(44, 62, 80, 0.5)
   - Timer: Quicksand 16px bold, rgba(44, 62, 80, 0.65)

8. COLORS (WARM, DUOLINGO-INSPIRED):
   - Coral primary: #FF6B4A (main brand color)
   - Golden yellow: #FFD93D (accent, celebration)
   - Soft green: #7BC47F (success, not shown in this screen)
   - Warm peach: #FFB5A0, #FF8A70
   - Navy text: #2C3E50 (warmer than black)
   - Warm grey: #6B7280

9. CORNER RADIUS (GENEROUS, FRIENDLY):
   - Cards: 24px
   - Buttons: 9999px (pill) or 20px
   - Small elements: 16px minimum
   - Everything feels SOFT and ROUNDED

10. SHADOWS (WARM CORAL-TINTED):
    - All shadows use coral tint: rgba(255, 107, 74, X)
    - Orb glow: rgba(255, 217, 61, 0.40) + rgba(255, 138, 112, 0.25)
    - Card shadow: rgba(255, 107, 74, 0.12)
    - Button shadow: rgba(255, 107, 74, 0.15)

11. STATE: LISTENING
    - Character orb is ENGAGED and ATTENTIVE
    - Face shows interest (eyes wide, "o" mouth)
    - Sparkles twinkling
    - User is speaking (transcript showing)
    - The character feels ALIVE and CARING

12. STYLE REQUIREMENTS:
    - PLAYFUL and FRIENDLY (Duolingo-inspired)
    - CHARACTER-DRIVEN (orb has personality)
    - WARM color palette (coral, yellow, peach)
    - Hand-drawn quality (sparkles, face)
    - Maximum warmth and approachability
    - Healthcare companion that feels like a FRIEND
    - Generous rounded corners everywhere
    - Celebration-focused aesthetic

CRITICAL:
- The character orb MUST have a friendly, expressive face (eyes, mouth, cheeks)
- Include sparkles around the orb (4-point stars, golden)
- Use warm coral/yellow/peach color palette
- Quicksand font (rounded, friendly) for all text
- Rich warm gradient background
- All shadows have coral tints
- This is MAXIMUM WARMTH - Duolingo for health
- The character should feel ALIVE and FRIENDLY
- Immersive full-screen (no tab bar)

Generate a polished, playful, character-driven, warm mobile UI mockup that makes users smile.
```

---

## Accessibility Notes

1. **VoiceOver**: Full support. Character face and decorative elements properly labeled or hidden.

2. **Reduce Motion**: All bounce animations, confetti, and sparkles disabled. Character face remains static with high-contrast expressions.

3. **High Contrast**: Character face becomes more prominent. All decorative elements have higher contrast or are simplified.

4. **Haptic Feedback**: Enhanced celebration haptics for playful feel.

5. **Keyboard Navigation** (iPad): Full support.

6. **Voice-Only Path**: Complete check-in without seeing character (voice announces state).

---

## Hand-Drawn Illustration Guidelines

### Character Face Illustration
- **Style**: Hand-drawn, slightly wobbly lines
- **Eyes**: Not perfect circles, slight asymmetry
- **Mouth**: Organic curve, not perfectly smooth
- **Cheeks**: Soft watercolor-style blush
- **Personality**: Friendly, approachable, gender-neutral

### Sparkle Illustrations
- **Style**: 4-point stars, hand-drawn
- **Lines**: Slightly irregular, not geometric
- **Sizes**: Varied (10-16px)
- **Colors**: Golden yellow with white centers

### Confetti Pieces (Complete State)
- **Shapes**: Circles, squares, triangles (hand-drawn)
- **Colors**: Yellow, green, coral, peach (brand colors)
- **Style**: Organic, not perfectly geometric
- **Sizes**: 8-16px
- **Animation**: Tumble as they fall

### Dimension Card Icons
- **BODY (heart)**: Simple hand-drawn heart outline
- **MIND (brain/cloud)**: Thought cloud or simplified brain
- **ACTIONS (checkmark)**: Checkmark in circle, hand-drawn
- **CONTEXT (sun/moon)**: Simple sun with rays or crescent moon

All icons should feel hand-crafted, warm, and friendly.

---

## Summary

Direction C v2 is the **boldest, warmest, most playful direction** — fully embracing the "Duolingo for health" vision. The character orb has an expressive face that reacts to the conversation, sparkles and confetti add moments of celebration, and the warm coral/yellow color palette creates maximum approachability. This direction completely departs from clinical healthcare design and treats the health check-in as a moment of connection with a caring friend.

**Best for**: Users who want maximum emotional warmth, find traditional health apps cold and intimidating, and respond well to character-driven, celebration-focused design. This direction makes health tracking feel like a supportive conversation with a friend, not a medical form.

**Trade-off**: Least aligned with Ditto's current brand, but most aligned with the emotional needs of chronically ill patients seeking comfort and support.
