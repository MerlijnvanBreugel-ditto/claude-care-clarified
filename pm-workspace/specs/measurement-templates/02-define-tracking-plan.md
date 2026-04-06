# Define Tracking Plan

> Jira provides epic context, title, and assignee. Don't repeat it here — jump straight into content.

## Dual Tracking Approach

Reference: [Tracking Approach](../../context/tracking-approach.md)

### Existing Events to Extend

| Event Name | New Properties | Type | Purpose |
|---|---|---|---|
| [Event Name - Title Case] | `[property_name]` | [bool/int/string/string[]] | [What question it answers] |

### New Business Events

| Event Name | Trigger | Properties | Question It Answers |
|---|---|---|---|
| [Feature Area - Action] | When [trigger] | `prop1`, `prop2` | [Question] |

### Granular UI Events (existing patterns)

| Event Name | Trigger | Properties | Notes |
|---|---|---|---|
| `button_tapped` / `screen_viewed` | [trigger] | `screen`, `button_id`, `context` | Follows existing tracking |

## Open Questions for Engineering

- [ ] [Technical feasibility question]
- [ ] [Data availability question]

## Dashboard Spec

| Chart | Type | Question It Answers |
|---|---|---|
| [Chart name] | Line / Bar / Funnel / Histogram | [Question] |

## Acceptance Criteria

- [ ] Event names match tracking sheet convention (Title Case, dash separator)
- [ ] Properties cover all segmentation needs
- [ ] Dashboard spec reviewed by Growth (Niek)
- [ ] Engineering confirms technical feasibility of all events
