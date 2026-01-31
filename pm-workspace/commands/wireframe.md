# Wireframe Command

Generate wireframe specifications from PRDs.

## Usage

```
/wireframe [feature/PRD name]
/wireframe --from=[prd-file]
/wireframe [feature] --screens=[screen1,screen2]
/wireframe [feature] --flow-only
```

## Description

The `/wireframe` command generates detailed wireframe specifications from PRDs. It creates screen layouts, component inventories, interaction patterns, and technical questions for engineering review.

## Options

### Default
```
/wireframe "User onboarding"
```
Generate wireframes for all screens in the feature.

### --from
```
/wireframe --from=./data/prds/prd-oauth-login.md
```
Use specific PRD file as input.

### --screens
```
/wireframe "Checkout" --screens="cart,payment,confirmation"
```
Generate wireframes for specific screens only.

### --flow-only
```
/wireframe "Password reset" --flow-only
```
Generate only the user flow diagram, not full wireframes.

### --responsive
```
/wireframe "Dashboard" --responsive
```
Include responsive breakpoint specifications.

### --annotated
```
/wireframe "Settings page" --annotated
```
Include detailed annotations for each component.

## Output

### Wireframe Specification
```markdown
# Wireframe Specification: [Feature Name]

## Overview
- PRD Reference: [link]
- Screens: [count]
- Flows: [count]

## Information Architecture
[Sitemap and navigation structure]

## User Flows
[Flow diagrams with decision points]

## Screen Specifications

### Screen: [Screen Name]
[Layout diagram]
[Component inventory]
[Interaction patterns]
[States and edge cases]

## Technical Questions
[Questions for engineering]

## Handoff Checklist
[Completion checklist]
```

### Screen Layout (ASCII)
```
┌─────────────────────────────────────────────────────┐
│  [Header]                              [User Menu]  │
├─────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────────────────────────────┐  │
│  │         │  │                                 │  │
│  │ Sidebar │  │         Main Content            │  │
│  │         │  │                                 │  │
│  └─────────┘  └─────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│  [Footer]                                           │
└─────────────────────────────────────────────────────┘
```

### Component Inventory
```markdown
| # | Component | Type | States | Notes |
|---|-----------|------|--------|-------|
| 1 | Login form | Form | default, error, loading | [notes] |
| 2 | Submit button | Button | default, hover, disabled | [notes] |
```

## Examples

### Feature Wireframes
```
/wireframe "User profile settings"
```

### From Specific PRD
```
/wireframe --from=./prds/prd-notifications.md
```

### Specific Screens
```
/wireframe "E-commerce" --screens="product-list,product-detail,cart"
```

### User Flow Only
```
/wireframe "Forgot password" --flow-only
```

### With Responsive Specs
```
/wireframe "Landing page" --responsive
```

## $ARGUMENTS

The feature or PRD to create wireframes for:
- "User authentication"
- "Dashboard redesign"
- "Mobile checkout flow"
- PRD file path

## Input Sources

Wireframe generator pulls from:

1. **PRD** (required)
   - User stories → Screens
   - Requirements → Components
   - Edge cases → States

2. **Discovery Insights** (optional)
   - Competitive patterns
   - User expectations

## Output Location

Wireframes are saved to:
```
pm-workspace/data/wireframes/
└── wireframe-[feature-name]-[date].md
```

## Workflow Integration

```
PRD → /wireframe → Review → /mockup
```

The wireframe spec serves as input for the Stitch mockup creator.

## Technical Questions

Wireframes include technical questions like:
- "Can we lazy-load this list?"
- "What's the max items to display?"
- "Is real-time update required?"
- "What permissions are needed?"

These should be answered before mockup creation.

## Tips

1. **Start from approved PRD** - Don't wireframe moving targets
2. **Focus on function** - Visual design comes later
3. **Document all states** - Empty, loading, error, success
4. **Include edge cases** - Long text, no data, errors
5. **Ask technical questions early** - Avoid design rework

## Related Commands

- `/draft-prd` - Create PRD first
- `/mockup` - Create visual mockups from wireframes
