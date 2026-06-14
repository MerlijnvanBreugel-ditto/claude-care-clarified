# Care Circle V2 Mockups

Generated mockups for the Care Circle V2 feature using Google Stitch with warm/human aesthetic.

## Stitch Project

- **Project ID**: 4268194311103954043
- **Project Name**: Care Circle V2 - Mockups
- **URL**: https://stitch.withgoogle.com/projects/4268194311103954043

## Design Directions

### Direction A: On-Brand + Warm
Follows the Ditto brand guidelines while applying warm/human aesthetic from the style guide.
- Warm cream backgrounds (#FFFBF5)
- 20px corner radius
- Warm-tinted shadows
- Hand-drawn illustrations

### Direction B: Partly On-Brand
Uses the same color palette but explores innovative layout patterns inspired by Mobbin research.
- Stacked card designs
- Speech bubble UI elements
- More playful interactions

### Direction C: Full Duolingo Energy
Maximum warmth and playfulness - shows what's possible with full commitment to joy.
- Friendly mascot character
- Bright warm colors
- Celebration moments
- 24px+ corner radius everywhere

## Screens Generated

### Onboarding Flow
| Screen | Direction A | Direction B | Direction C |
|--------|-------------|-------------|-------------|
| Role Selection | ✓ | - | ✓ |
| Social Proof | - | ✓ | - |
| Intention Setting | ✓ | - | - |

### Invitation Flow
| Screen | Direction A | Direction B | Direction C |
|--------|-------------|-------------|-------------|
| Visual Picker | ✓ | - | - |
| Card Preview | ✓ | - | - |
| Support Card | - | - | ✓ |

### Profile & Home
| Screen | Direction A | Direction B | Direction C |
|--------|-------------|-------------|-------------|
| Profile Page (Follower View) | ✓ | - | - |
| Profile Setup | ✓ | - | - |
| Follower Home (Empty) | ✓ | - | - |
| Follower Home (Active) | - | - | ✓ |
| Patient Home (Active) | ✓ | - | - |

### Reactions & Engagement
| Screen | Direction A | Direction B | Direction C |
|--------|-------------|-------------|-------------|
| Update View with Reactions | ✓ | - | - |
| Help Offer | - | ✓ | - |
| Connection Celebration | - | - | ✓ |

## Reference Images

Located in `pm-workspace/data/references/`:
- `competitors/duolingo/` - Duolingo app screenshots for warmth reference
- `competitors/airbnb/` - Airbnb app screenshots for trust/warmth
- `warm-human-style-guide.md` - Target aesthetic definition

## Expert Panel Review

See `expert-panel-review.md` for detailed feedback from:
- **Jony Ive** - Simplicity, inevitability
- **Paula Scher** - Typography, boldness
- **Mike Kresch** - Calm design, accessibility
- **Alan Dye** - Platform conventions
- **Alex Schleifer** - Storytelling, emotion

### Panel Recommendation
**Direction A** with celebration moments from **Direction C**

## Warm/Human Checklist

All mockups verified against:
- [ ] Corner radius ≥20px
- [ ] Background warm (#FFFBF5, not #FFF)
- [ ] Shadows warm-tinted
- [ ] Typography weight ≥500
- [ ] Hand-drawn illustrations where appropriate

## Next Steps

1. Download all generated screens locally
2. Iterate on Direction A based on panel feedback
3. Create final recommended versions
4. Export code for development

## Files

```
care-circle-v2/
├── README.md                 # This file
├── expert-panel-review.md    # Design panel feedback
├── comparison.md             # Direction comparison
├── manifest.json             # All screens with Stitch URLs
│
├── direction-a-on-brand/
│   ├── 01-role-selection.png
│   ├── 02-intention-setting.png
│   ├── 03-invitation-visual-picker.png
│   ├── 04-invitation-preview.png
│   ├── 05-profile-page.png
│   ├── 06-patient-home.png
│   ├── 07-follower-home-empty.png
│   └── 08-update-reactions.png
│
├── direction-b-partly/
│   ├── 01-social-proof.png
│   └── 02-help-offer.png
│
├── direction-c-duolingo/
│   ├── 01-role-selection.png
│   ├── 02-connection-celebration.png
│   ├── 03-support-card.png
│   └── 04-follower-home.png
│
└── recommended/
    └── (Final versions after iteration)
```
