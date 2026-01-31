# PM Workspace

A comprehensive Product Management workspace powered by AI agents for discovery, analysis, documentation, and design.

## Overview

This workspace provides a suite of specialized agents and commands to support the full PM workflow:

```
Discovery → Analysis → PRD → Wireframe → Mockup
```

## Quick Start

```bash
# Run full discovery on a topic
/discover "AI-powered note-taking apps"

# Analyze a competitor
/analyze-competitor "Notion"

# Process user feedback
/synthesize-feedback

# Generate a PRD
/draft-prd "Smart search feature" --comprehensive

# Create wireframes
/wireframe "Search results page"

# Generate mockups
/mockup "Search interface"
```

## Agents

| Agent | Description | Use Case |
|-------|-------------|----------|
| `market-researcher` | Analyzes market size, trends, and opportunities | Market sizing, trend analysis |
| `competitive-analyst` | Maps competitor features, pricing, positioning | Competitive intelligence |
| `feedback-synthesizer` | Extracts insights from user feedback | Voice of customer analysis |
| `insights-synthesizer` | Combines research into strategic insights | Cross-source synthesis |
| `prd-generator` | Creates structured PRDs | Feature documentation |
| `wireframe-designer` | Designs ASCII/text wireframes | Low-fidelity design |
| `stitch-mockup-creator` | Generates visual mockups via Stitch | High-fidelity design |

## Commands

| Command | Description |
|---------|-------------|
| `/discover` | Run full discovery (market + competitive + feedback) |
| `/analyze-competitor` | Deep dive on a single competitor |
| `/synthesize-feedback` | Process and analyze user feedback |
| `/draft-prd` | Generate lean or comprehensive PRD |
| `/wireframe` | Create text-based wireframes |
| `/mockup` | Generate visual mockups |

## Templates

- `prd-lean.md` - 1-2 page PRD for small features
- `prd-comprehensive.md` - Full PRD for major initiatives
- `competitive-analysis.md` - Competitor deep-dive template
- `user-insights.md` - User research synthesis template

## Directory Structure

```
pm-workspace/
├── agents/              # Agent definitions
│   ├── market-researcher.md
│   ├── competitive-analyst.md
│   ├── feedback-synthesizer.md
│   ├── insights-synthesizer.md
│   ├── prd-generator.md
│   ├── wireframe-designer.md
│   └── stitch-mockup-creator.md
├── commands/            # Command definitions
│   ├── discover.md
│   ├── analyze-competitor.md
│   ├── synthesize-feedback.md
│   ├── draft-prd.md
│   ├── wireframe.md
│   └── mockup.md
├── templates/           # Document templates
│   ├── prd-lean.md
│   ├── prd-comprehensive.md
│   ├── competitive-analysis.md
│   └── user-insights.md
└── data/                # Working data
    ├── research/        # Market research outputs
    ├── competitors/     # Competitive analysis
    ├── feedback/        # Raw user feedback (input)
    └── prds/            # Generated PRDs (output)
```

## Workflow

### 1. Discovery Phase

Start with `/discover` to gather market intelligence:

```bash
/discover "project management tools"
```

This runs three agents in parallel:
- Market researcher → market sizing and trends
- Competitive analyst → competitor mapping
- Feedback synthesizer → user insights

Then synthesizes findings into unified strategic insights.

### 2. Analysis Phase

Deep dive on specific competitors:

```bash
/analyze-competitor "Asana"
/analyze-competitor "Monday.com"
```

### 3. Documentation Phase

Generate PRDs from insights:

```bash
# Quick feature
/draft-prd "Task templates" --lean

# Major initiative
/draft-prd "Real-time collaboration" --comprehensive
```

### 4. Design Phase

Create wireframes and mockups:

```bash
/wireframe "Task creation flow"
/mockup "Task creation dialog"
```

## Data Inputs

### User Feedback

Place feedback files in `data/feedback/`:
- CSV files with columns: `date`, `source`, `feedback`, `sentiment`
- JSON arrays of feedback objects
- Markdown files with structured feedback

### Competitive Data

The competitive analyst can:
- Fetch live data from competitor websites
- Use pre-saved analysis in `data/competitors/`
- Search G2, Capterra, Product Hunt

## Best Practices

1. **Start with discovery** - Good inputs produce good outputs
2. **Be specific** - "AI writing assistant for sales emails" > "AI tool"
3. **Iterate** - Run discovery again as you learn more
4. **Connect insights** - Reference discovery in PRDs
5. **Version outputs** - Files are date-stamped for tracking

## Integration

This workspace integrates with:
- Web search for market research
- Stitch for mockup generation
- Standard markdown for all documents
