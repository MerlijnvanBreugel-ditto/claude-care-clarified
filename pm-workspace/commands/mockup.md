# Mockup Command

Generate production-quality mockups using Mobbin inspiration, your Figma design system, and Google Stitch—with expert design panel reviews from world-class designers.

## Usage

```
/mockup [feature/wireframe name]
/mockup --from=[wireframe-file] --figma=[figma-url]
/mockup [feature] --figma=[figma-url] --iterations=[N]
/mockup [feature] --screens=[screen1,screen2]
/mockup [feature] --direction=[a|b|c|all]
```

## Description

The `/mockup` command leverages the `product-designer` agent to:

1. **Research Mobbin** for design inspiration and patterns
2. **Download reference images** locally for visual comparison
3. **Learn your design system** from Figma (colors, typography, components)
4. **Generate 3 design directions** with warm/human aesthetic:
   - **A: On-brand + Warm** — Matches Figma design system with warm styling
   - **B: Partly on-brand** — Same palette, explores new patterns from Mobbin
   - **C: Full Duolingo** — Maximum warmth, playful, friendly mascot
5. **Download all mockups** as local PNG files
6. **Expert design panel review** (reviews actual images, not URLs):
   - **Jony Ive** (simplicity, inevitability)
   - **Paula Scher** (typography, boldness)
   - **Mike Kresch** (calm design, accessibility)
   - **Alan Dye** (platform conventions, precision)
   - **Alex Schleifer** (storytelling, emotion)
7. **Iterate** on the recommended direction based on panel feedback

### Target Aesthetic: Warm/Human (Duolingo/Airbnb)

All designs aim for "Duolingo for health" - warm, approachable, human. Key requirements:
- Corner radius: 20px+ (never <16px)
- Background: Off-white #FFFBF5 (never pure white)
- Shadows: Warm-tinted rgba(255,150,100,0.12)
- Typography: 500+ weight (never 400)
- Illustrations: Hand-drawn style with friendly characters

See: `pm-workspace/data/references/warm-human-style-guide.md`

## Prerequisites

### MCP Servers Required
Add these to your `~/.claude.json`:

```json
{
  "mcpServers": {
    "figma": {
      "type": "http",
      "url": "https://mcp.figma.com/mcp"
    },
    "stitch": {
      "type": "http",
      "url": "https://stitch.googleapis.com/mcp"
    }
  }
}
```

### Authentication

**Figma (OAuth)**:
1. Run: `claude mcp add --transport http figma https://mcp.figma.com/mcp`
2. Type `/mcp` in Claude and select `figma`
3. Select "Authenticate" and click "Allow Access"
4. Complete OAuth flow in browser

**Stitch (official Google MCP)**:
Follow the [official Stitch MCP setup](https://stitch.withgoogle.com/docs/mcp/setup). In short: create/select a Google Cloud project, enable the Stitch API, configure auth (e.g. `gcloud auth application-default login` or service account), then add this MCP with `"type": "http"` and `"url": "https://stitch.googleapis.com/mcp"`.

**If you see "Incompatible auth server: does not support dynamic client registration"** in Claude Desktop: the app expects HTTP MCP servers to support OAuth Dynamic Client Registration (DCR). Google’s Stitch MCP uses Google Cloud auth (ADC/OAuth) and does not support DCR, so Claude cannot complete its built-in HTTP auth flow. Until Claude adds support for Google Cloud auth for HTTP MCP (or Stitch adds DCR), the official Stitch HTTP endpoint will show as not authenticated in Claude. As a workaround, you can use a **stdio** MCP server that uses your gcloud credentials and proxies to Stitch (see [Stitch MCP setup](https://stitch.withgoogle.com/docs/mcp/setup) for any stdio option, or a community proxy that uses ADC).

## Options

### --figma
```
/mockup "Dashboard" --figma=https://figma.com/file/ABC123/Design-System
```
Specify Figma file to extract design system from. Required for design system learning.

### --from
```
/mockup --from=./data/wireframes/wireframe-onboarding.md
```
Use specific wireframe file as input.

### --iterations
```
/mockup "Checkout flow" --iterations=3
```
Number of iteration rounds (minimum 2, default 2).

### --screens
```
/mockup "Checkout" --screens="payment,confirmation"
```
Generate mockups for specific screens only.

### --style
```
/mockup "Landing page" --style=minimal
```
Apply specific design style (overrides Figma if no file provided).

### --export
```
/mockup "Profile" --export=react
/mockup "Profile" --export=html
```
Export format for generated code.

### --dark-mode
```
/mockup "Settings" --dark-mode
```
Include dark mode variants using Figma's dark mode tokens.

### --direction
```
/mockup "Profile" --direction=b
/mockup "Profile" --direction=all
```
Focus iteration on a specific direction (a, b, c) or generate all (default).
- `a` = On-brand only
- `b` = Partly on-brand only
- `c` = Experimental only
- `all` = All 3 directions (default)

### --skip-panel
```
/mockup "Quick test" --skip-panel
```
Skip expert panel review (not recommended, for speed only).

## Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  /mockup "User Dashboard" --figma=figma.com/file/XYZ           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 0: Mobbin Inspiration Research                           │
│  ──────────────────────────────────────                         │
│  • Search Mobbin for relevant patterns                          │
│  • Analyze top results for layout/component ideas               │
│  • Document inspiration for experimental directions             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 0.5: Download Reference Images (NEW)                     │
│  ──────────────────────────────────────────                     │
│  • Download Mobbin screenshots locally                          │
│  • Verify competitor refs exist (duolingo/, airbnb/)            │
│  • Read warm-human-style-guide.md                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Learn Design System from Figma                        │
│  ─────────────────────────────────────────                      │
│  • Extract colors, typography, spacing                          │
│  • Catalog component patterns                                   │
│  • Pull design tokens/variables                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Generate 3 Directions & DOWNLOAD                      │
│  ─────────────────────────────────────────                      │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │ Direction A │ │ Direction B │ │ Direction C │               │
│  │On-Brand+Warm│ │ Partly On-  │ │Full Duolingo│               │
│  │             │ │   Brand     │ │   Energy    │               │
│  │ Figma+warm  │ │ Same colors │ │ Max warmth  │               │
│  │  styling    │ │ new patterns│ │  + mascot   │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                  │
│  For each: Generate → Download PNG → Verify file exists         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: Expert Panel Review (VISUAL)                          │
│  ─────────────────────────────────────                          │
│                                                                  │
│  Panel reviews ACTUAL PNG FILES:                                │
│  • View: data/mockups/[feature]/direction-a/v1.png              │
│  • Compare to: data/references/competitors/duolingo/home.png    │
│                                                                  │
│  Warm/Human Checklist:                                          │
│  □ Corners ≥20px  □ Background warm  □ Shadows warm             │
│                                                                  │
│  🎨 JONY IVE        "Is it inevitable? Does it feel warm?"      │
│  🔤 PAULA SCHER     "Is the typography warm and bold?"          │
│  🧘 MIKE KRESCH     "Does this feel calm and caring?"           │
│  📐 ALAN DYE        "Are corners consistently rounded?"         │
│  💫 ALEX SCHLEIFER  "Does it feel human like Airbnb?"           │
│                                                                  │
│  → Each reviews all 3 directions with visual comparison         │
│  → Panel recommends which direction to iterate on               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Iterate on Recommended Direction (2+ rounds)          │
│  ───────────────────────────────────────────────────            │
│  • Address specific panel feedback                              │
│  • Fix warm/human issues (corners, shadows, colors)             │
│  • Regenerate in Stitch → Download new PNG                      │
│  • Re-review until panel consensus approval                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: Export All Deliverables                               │
│  ────────────────────────────────                               │
│  • All 3 direction mockups as LOCAL PNGs                        │
│  • Comparison document with tradeoffs                           │
│  • Expert panel review summaries                                │
│  • Recommended direction with code export                       │
│  • manifest.json with Stitch URLs + local paths                 │
└─────────────────────────────────────────────────────────────────┘
```

## Reference Images

The workflow now downloads and stores images locally for visual review:

### Input References
Store design inspiration in `pm-workspace/data/references/`:
```
pm-workspace/data/references/
├── warm-human-style-guide.md    # Core aesthetic definition (REQUIRED)
├── competitors/                 # Competitor app screenshots
│   ├── duolingo/               # Warm, playful reference
│   └── airbnb/                 # Human, trustworthy reference
├── inspiration/                 # Mobbin screenshots (auto-downloaded)
└── figma-exports/              # Your Figma screen exports
```

**Before running `/mockup`**, add 3-5 screenshots each to:
- `data/references/competitors/duolingo/` - Duolingo app screenshots
- `data/references/competitors/airbnb/` - Airbnb app screenshots

### Output Images
Generated mockups are **downloaded locally as PNGs** (not just URLs):
```
pm-workspace/data/mockups/[feature]/
├── direction-a/v1.png          # Downloaded PNG
├── direction-b/v1.png          # Downloaded PNG
├── direction-c/v1.png          # Downloaded PNG
└── manifest.json               # Stitch URLs + local paths
```

The expert panel **reviews the actual PNG files**, comparing them visually to reference images.

## Output

Mockups and assets saved to:
```
pm-workspace/data/mockups/[feature-name]/
├── README.md                      # Overview with recommendation
├── mobbin-research.md             # Inspiration findings
├── manifest.json                  # All files with Stitch URLs
├── design-system-extract.md       # Figma tokens extracted
│
├── direction-a-on-brand/
│   ├── v1.png                     # Downloaded PNG (not just URL)
│   ├── v2.png                     # Iteration (downloaded)
│   ├── panel-review.md            # Expert feedback
│   └── stitch-prompt.md           # Reproducible prompt
│
├── direction-b-partly-on-brand/
│   ├── v1.png                     # Downloaded PNG
│   ├── panel-review.md
│   └── stitch-prompt.md
│
├── direction-c-full-duolingo/
│   ├── v1.png                     # Downloaded PNG
│   ├── panel-review.md
│   └── stitch-prompt.md
│
├── recommended/                   # Panel's recommended direction
│   ├── final.png                  # Final version (downloaded)
│   ├── code/
│   │   ├── index.html
│   │   ├── styles.css
│   │   └── components/            # React (if --export=react)
│   └── design-spec.md
│
└── comparison.md                  # Side-by-side with tradeoffs
```

### Comparison Output Example
```markdown
# Design Direction Comparison: User Dashboard

## Quick Reference
| Aspect | A: On-Brand | B: Partly | C: Experimental |
|--------|-------------|-----------|-----------------|
| Design System Match | 100% | ~75% | ~20% |
| Innovation Level | Low | Medium | High |
| Risk Level | Low | Medium | High |

## Expert Panel Picks
- **Jony Ive**: Direction B — "Elegant simplicity without being boring"
- **Paula Scher**: Direction C — "Finally, some typographic courage!"
- **Mike Kresch**: Direction A — "The calmest experience"
- **Alan Dye**: Direction A — "Perfect platform consistency"
- **Alex Schleifer**: Direction B — "Best emotional connection"

## Our Recommendation: Direction B
**Why**: Balances brand consistency with fresh patterns discovered on Mobbin.
The tab navigation pattern from Linear improves discoverability while
maintaining our color system and typography.

## Tradeoffs
- Choosing A: Safe but potentially stale
- Choosing B: Fresh but requires minor design system updates
- Choosing C: Bold but significant brand deviation
```

### Panel Review Output Example
```markdown
# Expert Panel Review: Direction B (Partly On-Brand)

## Jony Ive
- **Simplicity Score**: 5/5
- **Verdict**: "This feels inevitable. The tab pattern reduces cognitive load
  without adding visual noise. I'd remove the shadow on the metric cards."
- **Recommendation**: Flatten the cards

## Paula Scher
- **Typographic Impact**: 4/5
- **Verdict**: "Better hierarchy than Direction A. The bold section headers
  work well. Could push the numbers larger for more impact."
- **Recommendation**: Increase metric number size to 48px

## Mike Kresch
- **Calm Factor**: 5/5
- **Verdict**: "The whitespace is generous. Easy on the eyes. Accessible."
- **Recommendation**: Approved as-is

## Alan Dye
- **Platform Consistency**: 4/5
- **Verdict**: "The tab bar follows iOS conventions nicely. Touch targets
  are appropriate. Minor: the segmented control could be more native."
- **Recommendation**: Use SF Pro for system text

## Alex Schleifer
- **Emotional Connection**: 4/5
- **Verdict**: "The progress visualization tells a story. Users will feel
  accomplished seeing their metrics. Could add subtle celebration moments."
- **Recommendation**: Consider micro-animation on milestone achievement
```

## Examples

### Full Flow with Figma
```
/mockup "User dashboard" --figma=https://figma.com/file/ABC123/Design-System
```
Extracts design system from Figma, generates dashboard mockup in Stitch, reviews, iterates 2x.

### From Existing Wireframe
```
/mockup --from=./data/wireframes/wireframe-onboarding.md --figma=figma.com/file/ABC123
```
Uses wireframe structure with Figma design system.

### More Iterations
```
/mockup "Checkout flow" --figma=figma.com/file/XYZ --iterations=4
```
Runs 4 iteration rounds for higher quality.

### Multiple Screens
```
/mockup "Auth" --screens="login,signup,forgot-password,reset-password" --figma=figma.com/file/XYZ
```
Generates consistent mockups for all auth screens.

### With Code Export
```
/mockup "Product card" --figma=figma.com/file/XYZ --export=react
```
Generates mockup and exports React component code.

## Expert Panel Scoring

Each direction is reviewed by the expert panel:

| Expert | Focus Area | Score (1-5) |
|--------|------------|-------------|
| **Jony Ive** | Simplicity, inevitability, material honesty | X/5 |
| **Paula Scher** | Typography, visual courage, identity | X/5 |
| **Mike Kresch** | Calm design, accessibility, user wellbeing | X/5 |
| **Alan Dye** | Platform conventions, precision, consistency | X/5 |
| **Alex Schleifer** | Storytelling, emotional connection, trust | X/5 |

**Panel Total**: X/25

**Consensus Thresholds:**
- < 15: Panel has significant concerns — iterate
- 15-19: Some experts have reservations — address feedback
- 20-24: Strong approval with minor refinements
- 25: Unanimous enthusiasm — ship it

**Approval Rule**: A direction is approved when all 5 experts score ≥ 3/5

## Tips

1. **Add reference images first** - Add Duolingo/Airbnb screenshots to `data/references/competitors/`
2. **Always provide Figma file** - Results are dramatically better with actual design tokens
3. **Start with wireframes** - Run `/wireframe` first for better structure
4. **Trust the panel** - If Jony says remove something, try it
5. **Show all 3 to stakeholders** - They deserve to see the tradeoffs
6. **Don't skip Mobbin** - The inspiration phase often produces the best ideas for Direction B/C
7. **Review the prompts** - Check `stitch-prompts.md` to understand what worked
8. **Direction B is often best** - It balances innovation with brand safety
9. **Listen to dissent** - If one expert hates it, there's usually a reason
10. **Check warm/human metrics** - Ensure corners ≥20px, background #FFFBF5, shadows warm-tinted

## Troubleshooting

### "Figma MCP not connected"
Run `/mcp` in Claude, select `figma`, and complete OAuth authentication. Ensure MCP is configured in `~/.claude.json`.

### "Stitch MCP not connected" / "Incompatible auth server: does not support dynamic client registration"
Claude Desktop only supports HTTP MCP servers that use **Dynamic Client Registration** (DCR). Google’s official Stitch MCP uses **Google Cloud auth** (no DCR), so when you add `https://stitch.googleapis.com/mcp` you get “not authenticated” and that error. **Options:** (1) Use a client that supports Google Cloud auth for HTTP MCP (if available). (2) Use a **stdio** MCP proxy that runs locally with `gcloud auth application-default login` and forwards to Stitch—see [official Stitch MCP setup](https://stitch.withgoogle.com/docs/mcp/setup) for any recommended stdio flow or community proxy.

### "Stitch API rate limited"
You have 350 generations/month (Standard) or 50/month (Experimental). Check usage at stitch.withgoogle.com.

### "Design system not extracting"
Ensure Figma file has published styles and components. Variables require Figma Pro+.

### "Colors don't match"
Provide exact hex codes in Stitch prompt. Check `design-system-extract.md` for actual values.

## Related Commands

- `/wireframe` - Create wireframes before mockups
- `/draft-prd` - Start with PRD for requirements
- `/discover` - Research before designing

## Agent

This command uses the `product-designer` agent which has access to:
- **WebSearch/WebFetch** for Mobbin inspiration research
- **Figma MCP** for design system extraction
- **Stitch MCP** for mockup generation
- **Expert Design Panel** featuring:
  - Jony Ive (simplicity)
  - Paula Scher (typography)
  - Mike Kresch (calm/accessibility)
  - Alan Dye (platform conventions)
  - Alex Schleifer (storytelling)
- **3 Design Directions** framework (on-brand, partly, experimental)

## $ARGUMENTS

The feature or wireframe to create mockups for:
- Feature name: "User authentication", "Dashboard", "Settings"
- Wireframe file path with `--from`

Required flag:
- `--figma` - URL or file key to your Figma design system file
