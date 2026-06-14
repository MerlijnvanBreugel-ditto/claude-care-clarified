# Reference Images Directory

This directory stores visual references for the mockup workflow. The expert design panel **reviews actual images**, not just URLs.

## Directory Structure

```
pm-workspace/data/references/
├── README.md                    # This file
├── warm-human-style-guide.md    # Core aesthetic definition
│
├── competitors/                 # Downloaded competitor screenshots
│   ├── duolingo/               # Duolingo app screenshots
│   │   ├── home.png
│   │   ├── lesson-complete.png
│   │   └── streak-celebration.png
│   └── airbnb/                 # Airbnb app screenshots
│       ├── home.png
│       ├── listing-detail.png
│       └── booking-confirmation.png
│
├── inspiration/                 # Mobbin screenshots (downloaded)
│   └── [app]-[screen].png      # e.g., headspace-meditation-home.png
│
└── figma-exports/              # Your exported Figma screens
    └── [feature]-[variant].png # e.g., onboarding-v2.png
```

## How to Add Reference Images

### 1. Competitor Screenshots (Manual)

Download screenshots from competitor apps and organize by app:

```bash
# Create app directory
mkdir -p pm-workspace/data/references/competitors/[app-name]

# Add screenshots with descriptive names
# Example naming: [screen-type]-[variant].png
#   home.png
#   onboarding-step-1.png
#   celebration-streak.png
```

**Recommended competitors for warm/human aesthetic:**
- Duolingo (playful, character-driven)
- Airbnb (warm, human-centered)
- Headspace (calm, illustrated)
- Calm (soothing, nature-inspired)

### 2. Mobbin Screenshots (Automated)

The product-designer agent will download Mobbin screenshots automatically:

```bash
# Agent downloads to:
pm-workspace/data/references/inspiration/[app]-[screen].png

# Example:
pm-workspace/data/references/inspiration/headspace-home.png
pm-workspace/data/references/inspiration/duolingo-lesson.png
```

### 3. Figma Exports

Export screens from your Figma file for comparison:

```bash
# In Figma: Select frame → Export → PNG (2x)
# Save to:
pm-workspace/data/references/figma-exports/[feature]-[state].png
```

## Using References in the Mockup Workflow

### For the Product Designer Agent

When generating mockups, the agent will:

1. **Before generation**: Review reference images in `competitors/` and `inspiration/`
2. **During generation**: Include specific visual references in Stitch prompts
3. **After generation**: Download generated mockups locally for visual comparison

### For the Expert Panel

The panel reviews **actual PNG files**, not URLs:

```markdown
## Expert Panel Review Process

1. View generated mockup: data/mockups/[feature]/direction-a/v1.png
2. Compare to reference: data/references/competitors/duolingo/home.png
3. Assess gap: "Our corners are 8px, Duolingo uses 20px - too sharp"
```

### Comparison Table Template

| Aspect | Our Mockup | Reference (Duolingo) | Gap | Fix |
|--------|------------|---------------------|-----|-----|
| Corner radius | 8px | 20px | Too sharp | Increase to 20px |
| Background | #FFFFFF | #FFFBF5 | Too cold | Use warm white |
| Shadow | Gray | Warm peach tint | Missing warmth | Add rgba(255,150,100,.1) |
| Typography | 400 weight | 600 weight | Too thin | Use medium/semibold |

## Naming Conventions

### Screenshot Files
```
[app-name]-[screen-type]-[optional-state].png

Examples:
duolingo-home.png
duolingo-lesson-complete.png
airbnb-listing-detail.png
headspace-meditation-playing.png
```

### Generated Mockup Files
```
data/mockups/[feature]/direction-[a|b|c]/v[version].png

Examples:
data/mockups/onboarding/direction-a/v1.png
data/mockups/onboarding/direction-a/v2.png  # After iteration
data/mockups/dashboard/direction-c/v1.png
```

## Recommended Reference Collection

To get the best results from the mockup workflow, collect these references:

### Duolingo (5-7 screenshots)
- [ ] Home screen (shows warmth, gamification)
- [ ] Lesson in progress (engagement)
- [ ] Lesson complete celebration (joy)
- [ ] Streak celebration (reward)
- [ ] Profile/stats (data visualization)
- [ ] Onboarding step (welcome)

### Airbnb (5-7 screenshots)
- [ ] Home/search screen (warmth)
- [ ] Listing detail (human photography)
- [ ] Booking confirmation (trust)
- [ ] Profile page (personal touch)
- [ ] Review section (social proof)

### Headspace (3-5 screenshots)
- [ ] Home meditation picker (calm)
- [ ] Session in progress (focus)
- [ ] Completion screen (achievement)

## Image Requirements

- **Format**: PNG (preferred) or JPG
- **Resolution**: 2x for retina (@2x) - typically 750x1334 for mobile
- **File size**: Compress large images (<500KB preferred)
- **Naming**: Lowercase, hyphens, no spaces

## Troubleshooting

### "Panel can't see images"
- Ensure images are downloaded locally (not just URLs)
- Check file exists: `ls pm-workspace/data/references/competitors/`
- Verify PNG format: `file [image].png`

### "References look different from our app"
- This is intentional for Direction B/C
- Direction A should match your Figma closely
- Directions B/C draw inspiration from these references

### "Too many reference images"
- Curate to 15-20 most relevant
- Organize by feature or aesthetic
- Remove duplicates or similar shots

---

**Quick Start**: Add 3-5 Duolingo screenshots and 3-5 Airbnb screenshots to `competitors/`. The agent will download Mobbin inspiration automatically during `/mockup` runs.
