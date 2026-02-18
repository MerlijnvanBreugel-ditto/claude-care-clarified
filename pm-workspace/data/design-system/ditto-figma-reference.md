# Ditto Patient Mobile App - Design System Reference

**Figma File**: https://www.figma.com/design/3oVeF0pzTzzLk06yqVKVwf/Ditto-Patient-Mobile-App
**Last Updated**: 2026-02-01

---

## Brand Identity

Ditto is a healthcare app that helps patients manage their medical journey - recording doctor conversations, scanning documents, and tracking appointments. The design language is **calm, trustworthy, and accessible**.

---

## Color System

### Primary Colors
| Token | Hex | Usage |
|-------|-----|-------|
| **Primary/Default** | `#0D164F` | Main brand color, text, buttons, active states |
| **Primary/Yellow** | `#F3DE70` | Accent, highlights, calendar icons |
| **Primary/Purple** | `#BEAEF8` | Secondary accent, decorative elements |
| **Color/Brand/Accent** | `#B2DCF5` | Light blue accent |

### Neutral Colors
| Token | Hex | Usage |
|-------|-----|-------|
| **Grey/000** | `#FFFFFF` | Card backgrounds, surfaces |
| **Grey/800** | `#82828A` | Secondary text |
| **Grey/900** | `#666670` | Tertiary text, inactive icons |
| **Color/Grey/900** | `#000000` | High contrast text |

### Secondary Colors
| Token | Hex | Usage |
|-------|-----|-------|
| **Secondary/Off-white** | `#EFE9DE` | Warm neutral backgrounds |

### Semantic Colors (Observed)
| Color | Hex | Usage |
|-------|-----|-------|
| Green tint | `#E0FBD5` | Success states, positive feedback |
| Orange | `#E8916E` | Warnings, attention |
| Background | `#F1F1F1` | Page backgrounds |

### Gradient Background
The app uses a subtle gradient background on main screens:
```css
background: linear-gradient(
  179.32deg,
  rgba(247, 221, 90, 0.1) 0.22%,    /* Yellow tint */
  rgba(217, 252, 209, 0.1) 21.77%,   /* Green tint */
  rgba(32, 185, 214, 0.1) 64.62%,    /* Blue tint */
  rgba(217, 252, 209, 0.1) 99.77%    /* Green tint */
);
```
Plus a subtle noise texture overlay at 5% opacity.

---

## Typography

### Font Family
**Uncut Sans** - A modern, friendly sans-serif typeface

### Type Scale
| Style | Font | Size | Weight | Line Height | Usage |
|-------|------|------|--------|-------------|-------|
| **Headline/H1** | Uncut Sans | 32px | Regular (400) | 100% | Page titles |
| **Headline/H3** | Uncut Sans | 20px | Medium (500) | 100% | Card titles, section headers |
| **Body/Body 3** | Uncut Sans | 14px | Medium (500) | 22px | Body text, descriptions |
| **Label/Normal** | Uncut Sans | 14px | Semibold (600) | 100% | Labels, tags, buttons |
| **Menu (caption)** | Uncut Sans | 13px | Medium (500) | 100% | Tab bar labels, captions |

---

## Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Tight spacing, icon padding |
| **s** | 8px | Small gaps, inline spacing |
| **sm** | 12px | Medium gaps |
| **m** | 16px | Standard padding, margins |
| **l** | 24px | Large padding, card padding |
| **150** | 6px | Button gaps |
| **200** | 8px | Tab bar top padding |
| **300** | 12px | Card gaps |
| **550** | 22px | Large border radius |

---

## Border Radius

| Size | Value | Usage |
|------|-------|-------|
| Small | 8px | Input fields, small buttons |
| Medium | 12px | Buttons, tags |
| Large | 22px | Cards, modals |
| Pill | 42-48px | Tags, badges |
| Full | 100px | Pills, indicators |

---

## Shadows

### Tab Bar Shadow
```css
box-shadow: 0px -2px 12px 0px rgba(0, 0, 0, 0.1);
```

### Card Shadow (subtle or none)
Cards typically use white background without heavy shadows, relying on the gradient background for visual separation.

---

## Components

### Status Bar
- Standard iOS status bar
- Time: SF Pro Semibold, 17px
- Follow Apple HIG: https://developer.apple.com/design/human-interface-guidelines/status-bars

### Page Header
- Title: Uncut Sans Regular, 32px, Primary/Default (#0D164F)
- Right actions: 44x44px touch targets with 24px icons
- Padding: 16px horizontal, 24px vertical

### Tab Bar
- Height: 90px (including home indicator area)
- 4 tabs: Home, Carepath, Loved ones, Settings
- Icon size: 24px
- Label: Uncut Sans Medium, 13px
- Active state: Primary/Default (#0D164F)
- Inactive state: Grey/900 (#666670)
- Home indicator: 134px wide, 5px tall, Primary/Default color

### Appointment Card
- Background: White (#FFFFFF)
- Border radius: 22px
- Padding: 24px
- Gap between elements: 12px
- Date badge: Uncut Sans Medium, 14px
- Title: Uncut Sans Medium, 20px
- Subtitle: Uncut Sans Medium, 14px
- Icon badges: 30px with overlaid icon

### Timeline
- Vertical line connecting appointment cards
- Timeline dots: 8px circles
- Color: Primary/Default with transparency

### Actions Menu (Bottom Sheet)
- White background with large border radius
- "Actions" header in Grey/900
- List items with icons on right
- Cancel button at bottom
- Grabber handle at top: 36px wide, 5px tall

### Input Fields
- Height: 86px (including label area)
- Border radius: 8-12px
- Label above field
- Placeholder text in Grey/800

### Buttons
- **Primary Button**
  - Background: Primary/Default (#0D164F)
  - Text: White, Uncut Sans Medium
  - Height: 60px
  - Border radius: Large
  - Full width or auto

- **In-card Button**
  - Smaller, fits within cards
  - Height: 42px
  - Can include emoji

### Navigation Bar
- Height: 60px
- Back arrow, title, optional right actions
- Used in sub-screens

### Tags/Badges
- Background: rgba(13, 22, 79, 0.05) - 5% Primary
- Border radius: 42px (pill)
- Padding: 4px 8px
- Text: Uncut Sans Semibold, 14px
- Can include icons

---

## Illustrations

The app uses friendly, hand-drawn style illustrations featuring:
- Hands holding phones
- Medical documents with hearts
- Recording microphones
- Soft, muted colors matching the brand palette
- Dashed circular decorative elements

---

## Key Screens (Node IDs for Reference)

| Screen | Node ID | Description |
|--------|---------|-------------|
| Carepath Overview | 10619:33427 | Main timeline view |
| Carepath with Actions | 10752:28093 | With bottom sheet |
| Settings | 11342:10519 | Profile and settings |
| Edit Details | 11342:10748 | Form inputs |
| Recording Flow | Section 10476:8548 | Voice recording |
| Document Scanner | Section 10482:11157 | Scan documents |
| Onboarding | Section 10476:9365 | First-time user flow |

---

## File Structure (Sections)

- **Home** - Main dashboard screens
  - Carepath - Timeline of medical events
  - Settings - User profile and preferences
  - Send flower - Care network features
  - Home (V3) - Latest home screen iterations
- **Recording flow** - Voice recording during appointments
- **Document scanner** - Scan and OCR medical documents
- **Start event** - Add new appointments
- **Translations** - Multi-language support
- **Splash screen & onboarding** - First-time user experience
- **AI feedback** - User feedback on AI features
- **Activation** - User activation flows
- **Appointment preparation** - Pre-appointment features

---

## Design Principles

1. **Calm & Trustworthy** - Soft colors, generous whitespace, friendly illustrations
2. **Accessible** - High contrast text, large touch targets (44px min)
3. **Healthcare-appropriate** - Professional but not clinical
4. **Dutch-first** - Primary language is Dutch, with English support
5. **iOS-native feel** - Follows Apple HIG for status bar, navigation

---

## Usage Notes for Mockups

When creating mockups for Ditto:

1. **Always use** the gradient background with noise overlay
2. **Cards** should be white with 22px border radius
3. **Primary actions** use the deep navy (#0D164F)
4. **Yellow (#F3DE70)** for calendar/time-related icons
5. **Purple (#BEAEF8)** sparingly for decorative accents
6. **Typography** must be Uncut Sans (or similar geometric sans-serif)
7. **Spacing** follows the 4-8-12-16-24 system
8. **Tab bar** always visible on main screens
9. **Illustrations** should be hand-drawn style, soft colors
