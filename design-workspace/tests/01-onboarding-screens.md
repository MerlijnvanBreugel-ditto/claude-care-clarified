# Test 01: Onboarding Persona + Intent Screens

## Objective
Test write-to-canvas by generating the onboarding prototype screens directly in Figma, using the spec from `pm-workspace/specs/onboarding-persona-intent-mapping.md`.

## Component Library
Source: [Ditto Component Library](https://www.figma.com/design/hbW8xI8q7rIMzC0OgEmK6b/Ditto-Component-Library?node-id=1215-2283) (LEGO section, node `1215:2283`)

### Components to use

| Component | Variant | Node ID | Usage |
|---|---|---|---|
| **NavigationBar** | Type=Onboarding | `940:2579` | Top bar with back button, progress dots, "Overslaan" skip link |
| **MultiRowSelection** | State=Default | `685:1236` | Unselected persona/intent option card (white, shadow, + checkbox) |
| **MultiRowSelection** | State=Selected | `685:1238` | Selected option card (filled navy checkbox with checkmark) |
| **Button** | State=Primary | `15:64` | "Continue" / "Get started" CTA (navy `#0D164F`, rounded-50px, h60) |
| **Button** | State=Secondary | `15:74` | Skip card alternative (grey border `#D0D0D6`, rounded-50px) |
| **Button** | State=Tertiary | `877:1183` | "Skip for now" text-only link |
| **CheckboxButton** | State=Default | `588:657` | Unselected circle (border, + icon) |
| **CheckboxButton** | State=Selected | `588:663` | Selected circle (filled navy, checkmark) |

### Design tokens

| Token | Value |
|---|---|
| Primary | `#0D164F` |
| Accent | `#B2DCF5` |
| Grey/000 (white) | `#FFFFFF` |
| Grey/400 | `#D0D0D6` |
| Secondary/Off-white | `#EFE9DE` |
| Font | Uncut Sans Medium |
| Card radius | 24px (`--l`) |
| Button radius | 50px |
| Card padding | 24px (`--l`) |
| Card shadow | `0px 4px 10.4px rgba(0,0,0,0.06)` |
| Card height | 88px |
| Checkbox size | 44px |

## What to generate

### Screen 1: Persona selection
- **NavigationBar** (Type=Onboarding) — progress dot 1 active, no skip link
- Title: "What describes your situation?" (Uncut Sans Medium, 24px)
- Subtitle: "Pick whatever applies — max 2" (Body 3, 14px)
- 5x **MultiRowSelection** cards for personas + 1x **Button** (Secondary) as skip card
- Privacy note at bottom (small text)
- **Button** (Primary) — "Continue" CTA (disabled state: reduced opacity)

### Screen 2: Intent selection (one variant per persona)
- **NavigationBar** (Type=Onboarding) — progress dot 2 active, "Overslaan" skip link visible
- Title: "What would help you most?"
- Subtitle: "Pick as many as you like"
- **MultiRowSelection** cards filtered by persona mapping from spec
- 1x **Button** (Tertiary) — "I'll figure it out as I go"
- Privacy note
- **Button** (Primary) — "Get started" CTA

### Variants to generate
1. Screen 1 (empty state — all MultiRowSelection in Default)
2. Screen 1 (`own_diagnosis` selected — that card in Selected state)
3. Screen 2 for `expecting` (6 intent cards)
4. Screen 2 for `own_diagnosis` (8 intent cards)
5. Screen 2 for `caregiver` (9 intent cards)
6. Screen 2 for `hcp` (6 intent cards)

## Target
- New Figma file in drafts, or a dedicated page in an existing file
- Use components from the Ditto Component Library (`hbW8xI8q7rIMzC0OgEmK6b`) — instantiate, don't recreate
- Apply design system variables (not hardcoded colors)

## Success criteria
- [ ] All 6 screens generated as separate frames
- [ ] Uses actual components from the Ditto Component Library (node IDs match)
- [ ] NavigationBar (Onboarding variant) on every screen
- [ ] MultiRowSelection cards for all persona/intent options
- [ ] Correct CheckboxButton states (Default/Selected)
- [ ] Primary button CTA on every screen
- [ ] Design tokens applied via variables
- [ ] Auto Layout used throughout
- [ ] Screenshot verification matches intent
