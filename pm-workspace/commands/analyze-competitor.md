# Analyze Competitor Command

Deep-dive competitive analysis on specific companies or products.

## Usage

```
/analyze-competitor [company/product name]
/analyze-competitor [company1, company2, company3]
/analyze-competitor [company] --features
/analyze-competitor [company] --pricing
/analyze-competitor [market] --landscape
```

## Description

The `/analyze-competitor` command provides detailed competitive intelligence on specific companies or products. It can analyze single competitors in depth or compare multiple competitors.

## Options

### Single Competitor Analysis
```
/analyze-competitor "Notion"
```
Full analysis of one competitor.

### Multiple Competitor Comparison
```
/analyze-competitor "Notion, Coda, Confluence"
```
Side-by-side comparison of multiple competitors.

### --features
```
/analyze-competitor "Slack" --features
```
Focus on feature comparison and capability mapping.

### --pricing
```
/analyze-competitor "Salesforce" --pricing
```
Focus on pricing model, tiers, and value proposition.

### --landscape
```
/analyze-competitor "CRM market" --landscape
```
Map the entire competitive landscape for a market.

### --track
```
/analyze-competitor "Figma" --track
```
Set up ongoing monitoring for competitor changes.

## Output

### Single Competitor Report
```markdown
# Competitive Analysis: [Company Name]

## Company Overview
- **Founded**: [Year]
- **Headquarters**: [Location]
- **Employees**: [Count]
- **Funding**: [Amount]
- **Valuation**: [Amount]

## Product Analysis
[Detailed product breakdown]

## Strengths
1. [Strength 1]
2. [Strength 2]

## Weaknesses
1. [Weakness 1]
2. [Weakness 2]

## Opportunities to Exploit
1. [Opportunity 1]
2. [Opportunity 2]

## Threat Level: [High/Medium/Low]
```

### Comparison Report
```markdown
# Competitive Comparison

## Feature Matrix
| Feature | Us | Comp A | Comp B |
|---------|-----|--------|--------|
| [Feature] | ✅ | ⚠️ | ❌ |

## Pricing Comparison
| Tier | Us | Comp A | Comp B |
|------|-----|--------|--------|
| Free | [X] | [X] | [X] |
| Pro | $X | $X | $X |

## Positioning Map
[Visual positioning analysis]

## Win/Loss Analysis
[Where we win vs each competitor]
```

## Examples

### Analyze Major Competitor
```
/analyze-competitor "Stripe"
```

### Compare Direct Competitors
```
/analyze-competitor "Webflow, Framer, Squarespace"
```

### Feature Deep Dive
```
/analyze-competitor "GitHub Copilot" --features
```

### Pricing Analysis
```
/analyze-competitor "Intercom" --pricing
```

### Market Landscape
```
/analyze-competitor "AI writing tools market" --landscape
```

## $ARGUMENTS

Company name, product name, or market to analyze. Can include:
- Single company: "Notion"
- Multiple companies: "Notion, Coda, Obsidian"
- Product name: "ChatGPT"
- Market segment: "No-code platforms"

## Data Gathered

- Company information (Crunchbase, LinkedIn)
- Product features (website, docs, app stores)
- Pricing (pricing pages, G2)
- Reviews (G2, Capterra, TrustRadius)
- News (recent announcements, funding)
- Social presence (Twitter, LinkedIn activity)

## Tips

1. **Start with direct competitors** before indirect
2. **Update regularly** - competitive landscape changes
3. **Use --features** before planning new features
4. **Check --pricing** before pricing decisions
5. **Save outputs** to `pm-workspace/data/competitors/`

## Related Commands

- `/discover` - Full discovery including competitive analysis
- `/draft-prd` - Use competitive insights in PRD
