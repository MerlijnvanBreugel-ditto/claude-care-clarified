# Discover Command

Run comprehensive product discovery combining market research, competitive analysis, and user feedback synthesis.

## Usage

```
/discover [topic/market]
/discover --market-only [topic]
/discover --competitive-only [company or market]
/discover --feedback-only [product area]
/discover --synthesize
```

## Description

The `/discover` command orchestrates the full discovery phase of the PM workflow:

1. **Market Research**: Analyzes market size, trends, and opportunities
2. **Competitive Analysis**: Maps competitors, features, and positioning
3. **Feedback Synthesis**: Extracts insights from user feedback
4. **Insights Synthesis**: Combines all sources into unified strategic insights

## Options

### Default (Full Discovery)
```
/discover "AI-powered note-taking apps"
```
Runs all three research agents in parallel, then synthesizes.

### --market-only
```
/discover --market-only "productivity software market"
```
Runs only the market-researcher agent.

### --competitive-only
```
/discover --competitive-only "Notion, Roam, Obsidian"
```
Runs only the competitive-analyst agent.

### --feedback-only
```
/discover --feedback-only "search functionality"
```
Runs only the feedback-synthesizer agent on specified product area.

### --synthesize
```
/discover --synthesize
```
Runs only the insights-synthesizer on existing research outputs.

### --output=[path]
```
/discover "market" --output=./pm-workspace/data/research/
```
Specifies where to save research outputs.

## Workflow

### Full Discovery Flow
```
         ┌─────────────────┐
         │   /discover     │
         │   [topic]       │
         └────────┬────────┘
                  │
    ┌─────────────┼─────────────┐
    ↓             ↓             ↓
┌───────┐   ┌───────────┐   ┌──────────┐
│Market │   │Competitive│   │ Feedback │
│Research│   │ Analysis │   │Synthesis │
└───┬───┘   └─────┬─────┘   └────┬─────┘
    │             │              │
    └─────────────┼──────────────┘
                  ↓
         ┌───────────────┐
         │   Insights    │
         │  Synthesizer  │
         └───────┬───────┘
                 ↓
         ┌───────────────┐
         │    Unified    │
         │   Insights    │
         └───────────────┘
```

### Execution

The command spawns agents in parallel where possible:

**Phase 1** (Parallel):
- market-researcher
- competitive-analyst
- feedback-synthesizer

**Phase 2** (Sequential):
- insights-synthesizer (needs Phase 1 outputs)

## Output

### During Execution
```
[Discovery] Starting full discovery for: AI-powered note-taking apps

[Phase 1/2] Running in parallel:
  - market-researcher: Analyzing market...
  - competitive-analyst: Mapping competitors...
  - feedback-synthesizer: Processing feedback...

[Phase 1/2] Complete:
  - Market size: $X.XB TAM
  - Competitors analyzed: N
  - Feedback items processed: N

[Phase 2/2] Running insights-synthesizer...

[Discovery Complete]
```

### Output Files
```
pm-workspace/data/research/
├── market-research-[date].md
├── competitive-analysis-[date].md
├── feedback-synthesis-[date].md
└── insights-synthesis-[date].md
```

### Final Summary
```
# Discovery Summary: [Topic]

## Key Insights
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]

## Top Opportunities
1. [Opportunity] - $X market, low competition
2. [Opportunity] - Strong user demand

## Recommended PRDs
1. [Feature]: [Rationale]
2. [Feature]: [Rationale]

## Next Steps
- [ ] Draft PRD for [top opportunity]
- [ ] Validate [assumption] with users
- [ ] Deep dive on [competitor]
```

## Examples

### Full Market Discovery
```
/discover "B2B SaaS project management tools"
```

### Quick Competitive Check
```
/discover --competitive-only "Monday.com, Asana, ClickUp"
```

### Analyze User Feedback
```
/discover --feedback-only "mobile app experience"
```

### Re-synthesize After Updates
```
/discover --synthesize
```

## $ARGUMENTS

The topic, market, or area to discover. Can be:
- A market category: "productivity software"
- Specific competitors: "Slack, Teams, Discord"
- A product area: "onboarding flow"
- A problem space: "remote team collaboration"

## Data Sources

### Market Research
- Industry reports (searched via web)
- Market databases
- News and announcements

### Competitive Analysis
- Competitor websites
- Review platforms (G2, Capterra)
- Product Hunt, app stores

### User Feedback
- Import from: `pm-workspace/data/feedback/`
- Supported formats: CSV, JSON
- Sources: Support tickets, reviews, surveys

## Tips

1. **Be specific** with your topic for better results
2. **Run full discovery** for new initiatives
3. **Use --competitive-only** for quick competitive checks
4. **Update feedback data** before running feedback synthesis
5. **Re-synthesize** after adding new research

## Related Commands

- `/analyze-competitor` - Deep dive on single competitor
- `/synthesize-feedback` - Process new feedback batch
- `/draft-prd` - Create PRD from discovery insights
