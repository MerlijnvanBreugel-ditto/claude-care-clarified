# Warm/Human Design Style Guide

Target: **"Duolingo for health"** - warm, approachable, human.

## Target Feel

> "Like a friendly helper, not a medical app."

Users of Ditto are often tired, anxious, or overwhelmed by their health situation. The design should make them feel **cared for**, not clinical. Every screen should feel like a supportive friend, not a hospital form.

---

## Core Principles

### 1. Warmth Over Sterility
- Healthcare doesn't have to feel cold
- Replace clinical blue/white with warm, inviting tones
- Add personality through illustrations and micro-copy

### 2. Friendliness Over Formality
- Conversational tone in UI copy
- Rounded shapes that feel soft and approachable
- Celebrate progress, no matter how small

### 3. Calm Over Chaos
- Generous whitespace (breathing room)
- One primary action per screen
- Progressive disclosure - don't overwhelm

---

## Color Palette

### Background Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `bg-warm` | `#FFFBF5` | Primary background (NOT pure white `#FFF`) |
| `bg-cream` | `#FFF8F0` | Card backgrounds |
| `bg-soft` | `#FEFCF9` | Secondary surfaces |

### Primary Colors
| Token | Hex | Feeling |
|-------|-----|---------|
| `primary` | `#FF6B4A` | Warm coral - friendly, energetic |
| `primary-soft` | `#FF8A70` | Hover/light variant |
| `primary-deep` | `#E55A3A` | Active/pressed state |

### Accent Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `accent-yellow` | `#FFD93D` | Celebrations, highlights |
| `accent-green` | `#7BC47F` | Success, progress |
| `accent-purple` | `#9B8FD0` | Calm, meditation features |

### Semantic Colors (Warm-Tinted)
| Token | Hex | Notes |
|-------|-----|-------|
| `success` | `#4ADE80` | Soft green, not harsh |
| `warning` | `#FBBF24` | Warm amber |
| `error` | `#F87171` | Soft coral-red, not alarming |
| `info` | `#60A5FA` | Soft blue |

### What to AVOID
- Pure white (`#FFFFFF`) - too sterile
- Pure black (`#000000`) - too harsh
- Cold grays (`#6B7280`) - use warm grays instead
- Medical blue (`#0066CC`) - too clinical

---

## Corner Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | `12px` | Small elements, chips |
| `radius-md` | `16px` | Buttons, inputs |
| `radius-lg` | `20px` | Cards, containers |
| `radius-xl` | `24px` | Hero cards, modals |
| `radius-pill` | `9999px` | Pills, tags |

### Critical Rule
> **NEVER use corner radius less than 12px.** Sharp corners feel cold and institutional.

| Bad | Good |
|-----|------|
| 4px radius | 16px radius |
| 8px radius | 20px radius |
| Square corners | Generous rounding |

---

## Shadows

Use **warm-tinted shadows**, not gray:

```css
/* GOOD - Warm shadows */
box-shadow: 0 4px 12px rgba(255, 150, 100, 0.10);
box-shadow: 0 8px 24px rgba(255, 150, 100, 0.12);
box-shadow: 0 16px 32px rgba(255, 150, 100, 0.15);

/* BAD - Cold gray shadows */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
```

### Shadow Scale
| Level | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0 2px 8px rgba(255, 150, 100, 0.08)` | Subtle lift |
| `shadow-md` | `0 4px 16px rgba(255, 150, 100, 0.10)` | Cards |
| `shadow-lg` | `0 8px 24px rgba(255, 150, 100, 0.12)` | Elevated cards |
| `shadow-xl` | `0 16px 32px rgba(255, 150, 100, 0.15)` | Modals, popovers |

---

## Typography

### Font Family
- **Primary**: Rounded sans-serif (e.g., Nunito, Quicksand, Poppins)
- Avoid: Sharp geometric fonts (Helvetica, Arial, Roboto)

### Font Weights
| Use | Weight | Notes |
|-----|--------|-------|
| Body | 500 (Medium) | Never use 400/Regular - feels thin |
| Headings | 600-700 | Bold but friendly |
| Emphasis | 700 | Strong but not aggressive |

### Type Scale
| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| `display` | 32-40px | 700 | Hero headlines |
| `h1` | 28px | 600 | Page titles |
| `h2` | 22px | 600 | Section headers |
| `h3` | 18px | 600 | Card titles |
| `body` | 16px | 500 | Main content |
| `small` | 14px | 500 | Supporting text |
| `caption` | 12px | 500 | Labels, hints |

---

## Illustrations

### Style Requirements
- **Hand-drawn quality** - slightly wobbly lines, not perfect vectors
- **Soft, muted colors** - not flat bold primaries
- **Characters with expressions** - faces that show emotion
- **Small imperfections** - makes it feel human-made

### Character Guidelines
- Round, soft body shapes
- Large, expressive eyes
- Friendly, approachable poses
- Show diverse representation
- Emotions should be clear (happy, encouraging, celebrating)

### When to Use Illustrations
- Empty states - make them feel welcoming, not broken
- Onboarding - guide with friendly characters
- Celebrations - mark achievements with joy
- Error states - soften the blow with empathy

### What to AVOID
- Flat, corporate illustrations (Humaaans-style)
- Generic stock illustrations
- Perfectly geometric vector art
- Faceless, abstract figures

---

## Icons

### Style
- **Rounded strokes** (2-3px weight)
- **Filled or duotone** preferred over line-only
- **Soft corners** - never sharp

### What to AVOID
- Sharp, angular icons
- Thin 1px stroke icons
- Generic system icons
- Medical/clinical iconography

---

## Components

### Buttons
```
Primary Button:
- Background: #FF6B4A (warm coral)
- Text: White, weight 600
- Radius: 16px (minimum)
- Padding: 16px 24px
- Shadow: 0 4px 12px rgba(255, 107, 74, 0.25)
- Hover: Scale 1.02, shadow increases
```

### Cards
```
Card:
- Background: #FFFBF5 or #FFF8F0
- Radius: 20px (minimum 16px)
- Shadow: 0 4px 16px rgba(255, 150, 100, 0.10)
- Padding: 20px
- Border: None (shadows only) or 1px rgba(255, 150, 100, 0.15)
```

### Inputs
```
Input Field:
- Background: #FFFBF5
- Border: 2px solid rgba(255, 150, 100, 0.2)
- Radius: 12px
- Focus: Border becomes primary color
- Padding: 14px 16px
```

---

## Emotional Design Checklist

Before finalizing any screen, ask:

- [ ] Does this feel warm and welcoming?
- [ ] Would a tired, anxious person feel comforted?
- [ ] Are there any sharp corners or cold colors?
- [ ] Is the typography friendly (rounded, medium+ weight)?
- [ ] Do shadows have warm tints?
- [ ] Is there an illustration opportunity we're missing?
- [ ] Does the background avoid pure white?
- [ ] Would this screenshot well for marketing (Airbnb test)?

---

## Reference Apps

### Duolingo (Primary Inspiration)
- Playful character-driven design
- Bold, joyful colors
- Celebration of small wins
- Gamification that feels rewarding

### Airbnb
- Warm photography and illustrations
- Human-centered copy
- Generous whitespace
- Trust-building through warmth

### Headspace
- Calm, soothing color palette
- Soft illustrations with character
- Mindful whitespace
- Gentle transitions

### Calm
- Muted, nature-inspired palette
- Soft gradients
- Tranquil typography
- Ambient design elements

---

## Anti-Patterns (What Makes Designs Look "AI-Generated")

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| Pure white backgrounds | Feels sterile, clinical | Use `#FFFBF5` or warmer |
| Sharp corners (<12px) | Feels institutional | 16-24px radius |
| Flat shadowless cards | Lacks depth, feels dead | Warm-tinted shadows |
| Generic icons | No personality | Custom or warm-styled icons |
| Gray color schemes | Cold, corporate | Warm grays or accent colors |
| Stock illustrations | Impersonal, forgettable | Hand-drawn style with character |
| Perfect symmetry | Feels machine-made | Subtle organic variation |
| Thin typography (400 weight) | Weak, clinical | 500+ weight |

---

## Quick Reference

When prompting Stitch or any design tool:

```
WARM VISUAL STYLE (CRITICAL):
- Corner radius: 20-24px (NEVER less than 16px)
- Background: Off-white #FFFBF5 (never pure white)
- Shadows: Warm-tinted 0 8px 24px rgba(255, 150, 100, 0.12)
- Typography: Rounded sans-serif, weight 500-600
- Include hand-drawn style illustrations with friendly characters

AVOID (makes designs look AI-generated):
- Pure white backgrounds
- Sharp corners (<16px)
- Flat shadowless cards
- Generic icons
- Gray color schemes
- Thin typography
```

---

**Remember**: When a tired patient sees your design, they should think:
> "This app understands me. I feel taken care of."
