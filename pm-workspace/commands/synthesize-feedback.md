# Synthesize Feedback Command

Process and analyze user feedback from multiple sources into actionable insights.

## Usage

```
/synthesize-feedback
/synthesize-feedback [product-area]
/synthesize-feedback --source=[source]
/synthesize-feedback --import=[file]
/synthesize-feedback --segment=[segment]
```

## Description

The `/synthesize-feedback` command processes user feedback data and extracts patterns, themes, and actionable insights. It supports multiple feedback sources and formats.

## Options

### Default (All Feedback)
```
/synthesize-feedback
```
Processes all feedback in `pm-workspace/data/feedback/`.

### By Product Area
```
/synthesize-feedback "search functionality"
```
Filters feedback to specific product area.

### --source
```
/synthesize-feedback --source=intercom
/synthesize-feedback --source=app-reviews
/synthesize-feedback --source=surveys
```
Process feedback from specific source only.

### --import
```
/synthesize-feedback --import=./exports/zendesk-jan-2024.csv
```
Import and process new feedback file.

### --segment
```
/synthesize-feedback --segment=enterprise
/synthesize-feedback --segment=churned
```
Filter by user segment.

### --since
```
/synthesize-feedback --since=2024-01-01
```
Process feedback from specific date.

### --severity
```
/synthesize-feedback --severity=critical
```
Focus on critical issues only.

## Supported Formats

### CSV Format
```csv
date,source,segment,category,sentiment,content,user_id
2024-01-15,support,enterprise,bug,-1,"App crashes when...",user_123
```

### JSON Format
```json
{
  "feedback": [
    {
      "date": "2024-01-15",
      "source": "support",
      "segment": "enterprise",
      "category": "bug",
      "sentiment": -1,
      "content": "App crashes when...",
      "user_id": "user_123"
    }
  ]
}
```

### Supported Sources
- `intercom` - Support tickets
- `zendesk` - Support tickets
- `app-store` - iOS App Store reviews
- `play-store` - Google Play reviews
- `g2` - G2 reviews
- `surveys` - NPS/CSAT surveys
- `slack` - Community feedback
- `custom` - Any CSV/JSON

## Output

### Synthesis Report
```markdown
# Feedback Synthesis Report

## Overview
- **Period**: [date range]
- **Total Items**: [N]
- **Sources**: [list]
- **Overall Sentiment**: [score]

## Top Themes

### Theme 1: [Theme Name]
**Frequency**: [N] mentions
**Sentiment**: [score]
**Severity**: [level]

**Sample quotes**:
> "[Quote 1]"
> "[Quote 2]"

**Recommended action**: [action]

## Feature Requests
| Feature | Requests | Priority |
|---------|----------|----------|
| [Feature] | [N] | High |

## Bug Patterns
| Bug | Count | Severity |
|-----|-------|----------|
| [Bug] | [N] | Critical |

## Churn Signals
[At-risk indicators]

## Recommendations
1. [Recommendation]
2. [Recommendation]
```

## Examples

### Process All Recent Feedback
```
/synthesize-feedback
```

### Focus on Mobile Experience
```
/synthesize-feedback "mobile app"
```

### Import New Support Export
```
/synthesize-feedback --import=./zendesk-export.csv
```

### Enterprise Segment Only
```
/synthesize-feedback --segment=enterprise
```

### Critical Issues Only
```
/synthesize-feedback --severity=critical
```

### Last Month's Feedback
```
/synthesize-feedback --since=2024-01-01
```

## $ARGUMENTS

Optional product area or feature to focus analysis on:
- "onboarding"
- "search"
- "mobile app"
- "pricing"
- "performance"

## Data Location

Store feedback files in:
```
pm-workspace/data/feedback/
├── intercom/
│   └── export-2024-01.csv
├── app-reviews/
│   ├── ios-reviews.json
│   └── android-reviews.json
├── surveys/
│   └── nps-q1-2024.csv
└── custom/
    └── user-interviews.json
```

## Tips

1. **Regular imports** - Set up weekly feedback imports
2. **Segment analysis** - Different segments have different needs
3. **Track trends** - Compare synthesis reports over time
4. **Prioritize by impact** - Focus on high-frequency, high-severity
5. **Quote users** - Include quotes in PRDs for context

## Related Commands

- `/discover` - Full discovery including feedback
- `/draft-prd` - Use feedback insights in PRD
