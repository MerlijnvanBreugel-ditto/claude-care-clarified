# Skill: Ditto Design System Rules

## When to use
Always apply these rules when creating or modifying Ditto designs.

## Brand

- Primary palette: deep navy (#1a2e4a), teal accents (#2a6f93), soft backgrounds (#eaf4f7)
- Border color: #ddeaf0 (cards), #c5dde6 (containers)
- Text: #1a2e4a (primary), #5a7a8c (secondary), #8a9eb0 (muted)
- Selection state: border #2a6f93, background #f0f8fc
- Border radius: 14px (cards, buttons), 36px (device frames)
- Font: system font stack (-apple-system, SF Pro, Segoe UI)

## Component Conventions

### Option Cards
- White background, 14px border-radius, 1.5px border
- Padding: 11px 13px
- Gap between cards: 7-8px
- Contains: label text (13px, 500 weight) + optional hint (11px, muted) + check circle
- Selected state: blue border + light blue background + filled check circle
- Skip variant: dashed border, muted label text

### Check Circles
- 22px diameter, 1.5px border, round
- Unselected: border #c5dde6, empty
- Selected: background #2a6f93, white checkmark SVG

### Buttons (CTA)
- Full width, 14px border-radius, 14px padding
- Background: #1a2e4a, white text, 14px font size, 500 weight
- Disabled: opacity 0.28

### Screen Container (Phone Frame)
- Width: 340px, min-height: 620px
- Background: #eaf4f7, border-radius: 36px, 1.5px border #c5dde6
- Padding: 28px 18px
- Flex column layout

### Typography
- Screen title: 20px, 500 weight, #1a2e4a
- Subtitle/hint: 12px, #5a7a8c
- Privacy note: 11px, #8a9eb0, centered

## Layout Rules
- All containers use Auto Layout (vertical, top-aligned)
- Cards stack vertically with 7px gap
- CTA button pushed to bottom (auto margin or fill)
- Privacy note sits between content and CTA
- Back link: 12px, #2a6f93, top of screen 2
