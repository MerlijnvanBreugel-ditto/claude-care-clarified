# Mockup Command

Generate visual design specifications for Google Stitch from wireframes.

## Usage

```
/mockup [feature/wireframe name]
/mockup --from=[wireframe-file]
/mockup [feature] --style=[style]
/mockup [feature] --screens=[screen1,screen2]
```

## Description

The `/mockup` command generates visual design specifications and Stitch-ready prompts from wireframe specifications. It creates detailed design specs including colors, typography, component designs, and prompts optimized for Google Stitch.

## Options

### Default
```
/mockup "User dashboard"
```
Generate mockup specs for all wireframed screens.

### --from
```
/mockup --from=./data/wireframes/wireframe-onboarding.md
```
Use specific wireframe file as input.

### --style
```
/mockup "Landing page" --style=minimal
/mockup "Dashboard" --style=material
/mockup "Marketing" --style=bold
```
Apply specific design style.

### --screens
```
/mockup "Checkout" --screens="payment,confirmation"
```
Generate mockups for specific screens only.

### --components
```
/mockup "Design system" --components
```
Generate component library mockups only.

### --dark-mode
```
/mockup "Settings" --dark-mode
```
Include dark mode variants.

### --responsive
```
/mockup "Homepage" --responsive
```
Include responsive variants for all breakpoints.

## Design Styles

| Style | Description | Best For |
|-------|-------------|----------|
| `minimal` | Clean, lots of whitespace | SaaS, productivity |
| `material` | Google Material Design 3 | Android, cross-platform |
| `ios` | Apple Human Interface | iOS apps |
| `bold` | Strong colors, large type | Marketing, landing |
| `enterprise` | Professional, conservative | B2B, enterprise |
| `playful` | Rounded, colorful | Consumer, games |

## Output

### Mockup Specification
```markdown
# Visual Design Specification: [Feature]

## Design Overview
- Style: [style]
- Platform: [platform]
- Wireframe Reference: [link]

## Visual Language
[Color system, typography, spacing]

## Component Designs
[Component specs with Stitch prompts]

## Screen Designs
[Screen specs with Stitch prompts]

## Stitch Prompts
[Ready-to-use prompts for each screen]
```

### Stitch Prompt Example
```
Design a login screen for a modern SaaS productivity app.

Style: Minimal, clean with subtle shadows
Colors: Primary #4F46E5 (indigo), Background #FAFAFA
Typography: Inter font, clean and readable

Layout:
- Centered card on light gray background
- Logo at top
- Email and password inputs
- "Sign in" primary button
- "Forgot password" link below
- "Sign up" secondary link at bottom

Include states:
- Default
- Input focused
- Error state with validation message
- Loading state with spinner

Mood: Professional, trustworthy, simple
```

## Examples

### Full Feature Mockups
```
/mockup "User onboarding flow"
```

### From Specific Wireframe
```
/mockup --from=./wireframes/wireframe-dashboard.md
```

### Minimal Style
```
/mockup "Settings page" --style=minimal
```

### Specific Screens
```
/mockup "Auth" --screens="login,signup,forgot-password"
```

### Component Library
```
/mockup "Design system" --components
```

### With Dark Mode
```
/mockup "App shell" --dark-mode
```

## $ARGUMENTS

The feature or wireframe to create mockups for:
- "User authentication"
- "Dashboard"
- "Mobile app"
- Wireframe file path

## Input Sources

Mockup generator pulls from:

1. **Wireframe Spec** (required)
   - Layouts → Visual layouts
   - Components → Component designs
   - Flows → Screen sequences

2. **PRD** (optional)
   - Brand requirements
   - Accessibility needs

3. **Style Guide** (if exists)
   - Existing colors
   - Typography
   - Component patterns

## Output Location

Mockup specs are saved to:
```
pm-workspace/data/mockups/
└── mockup-[feature-name]-[date].md
```

## Workflow Integration

```
PRD → Wireframe → /mockup → Stitch → Development
```

### Using with Stitch

1. Run `/mockup` to generate specs
2. Copy Stitch prompts from output
3. Paste into Google Stitch
4. Generate and iterate
5. Export final designs

## Stitch Tips

1. **Be specific** - More detail = better results
2. **Include context** - Explain the product and users
3. **Request variants** - Ask for multiple states
4. **Iterate** - Refine prompts based on output
5. **Stay consistent** - Use same style across screens

## Tips

1. **Complete wireframes first** - Mockups need structure
2. **Choose style early** - Consistency matters
3. **Generate components first** - Build a system
4. **Include all states** - Default, hover, error, etc.
5. **Test in Stitch** - Refine prompts based on results

## Related Commands

- `/wireframe` - Create wireframes first
- `/draft-prd` - Start with PRD
- `/discover` - Research before designing
