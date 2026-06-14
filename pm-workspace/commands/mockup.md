# /mockup

> Dispatches the product-designer agent to generate 3 visual design directions (on-brand, partly on-brand, full Duolingo energy) using Figma + Stitch, then runs an expert panel review to pick the winner.

## Usage

```
/mockup [feature or screen name]
/mockup "Care Circle invitation card" --figma=[figma-url]
/mockup --from=pm-workspace/specs/care-circle-v2.md --figma=[figma-url]
```

## What It Does

1. Dispatches to the `product-designer` agent
2. Agent runs the full design workflow:
   - Mobbin inspiration research
   - Figma design system extraction
   - 3 design directions in Stitch (on-brand warm, partly on-brand, full Duolingo)
   - Downloads all mockups as local PNGs
   - Expert panel review (Jony Ive, Paula Scher, Mike Kresch, Alan Dye, Alex Schleifer)
   - Iterates on recommended direction
3. Saves to `pm-workspace/data/mockups/[feature]/`
4. Updates registry

## Options

- `--figma=[url]` — Figma file to extract design system from (recommended)
- `--from=[file]` — Spec or wireframe file as input
- `--direction=[a|b|c|all]` — Focus on specific direction
- `--iterations=[N]` — Number of iteration rounds (default 2)

## $ARGUMENTS

Feature name, screen name, or spec file path.
