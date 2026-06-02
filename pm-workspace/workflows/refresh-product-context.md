# Workflow: Refresh Product Context

> Pulls the current state of Ditto from the live integrations (Linear, Granola, Slack) and reconciles it into the foundation doc, the registry, and Mewtwo's memory. Run it on a cadence so `product-context.md` never drifts months behind reality again.

## When to Use

- On a regular cadence (monthly is a good default; the prior gap was Feb to May 2026).
- Before a strategy off-site, board prep, or investor update, when the foundation doc needs to be trustworthy.
- After any major shift (a Code Red, a reorg, a north-star change, a new market launch).
- When Merlijn says "refresh the Ditto context" or "update everything on Ditto."

## Sources & How to Verify They Are Live

Run one cheap call per source first. If a call fails with an auth error, tell Merlijn to reconnect that integration before proceeding (subagents inherit the session's MCP connections, so fix it here).

| Source | Verify call | What it covers |
|---|---|---|
| Linear | `get_user("me")`, `list_teams` | OKRs, initiatives, projects, cycles, status updates, people |
| Granola | `get_account_info` | Strategy decisions, meeting timeline, verbatim action items |
| Slack | `slack_read_user_profile` | Announcements, growth numbers, team changes, channel map |

MCP tools are deferred. Load schemas first with ToolSearch, e.g.:
`select:mcp__claude_ai_Linear__list_projects,mcp__claude_ai_Granola__query_granola_meetings,mcp__claude_ai_Slack__slack_search_public_and_private`

## Steps

### 1. Load Current State

Read, in order: `context/product-context.md` (note its "Last updated" date, that is the baseline), `registry/registry.json`, and the memory index `MEMORY.md`. Everything after the baseline date is "new."

### 2. Verify Integrations

Run the three verify calls above. Confirm all are authenticated as `merlijn@ditto.care` before fanning out.

### 3. Parallel Fan-Out (one agent per source)

Dispatch three `general-purpose` agents in a single message (they are independent, no shared state). Give each: today's date, the baseline date, the Ditto one-liner, the exact MCP tool names to load via ToolSearch, an explicit READ-ONLY instruction (no writes, no Slack sends), and a request for a tight structured markdown report (not raw JSON).

| Agent | Primary tools | Must return |
|---|---|---|
| **Linear** | `list_initiatives`, `list_projects`, `get_status_updates`, `list_issues`, `list_cycles`, `list_users`, `get_document` | Initiatives, active projects, current cycle, recent status updates (quoted), people/roles, OKRs/KRs with status, north star |
| **Granola** | `query_granola_meetings` (primary), `list_meetings`, `get_meetings` | Dated meeting timeline, strategy shifts, decisions (verbatim), team/hiring changes, partnerships, AI quality, north star/OKRs. Preserve `[[n]](url)` citations. |
| **Slack** | `slack_search_channels`, `slack_search_public_and_private`, `slack_read_channel` | Channel map (name + ID), org/growth updates with numbers, product direction, partnerships, team joiners/leavers, AI quality, all with dates + source channel |

### 4. Triangulate and Reconcile

- **Confirm across ≥2 sources** before treating a fact as settled. Note single-source claims as such.
- **Flag conflicts** rather than picking silently (e.g. metric values that disagree because of definition differences or broken instrumentation). Prefer the most recent official readout, and say which source and date it came from.
- **Separate vocabulary from reality**: internal codenames (e.g. "Care Brain", "Life Moments") may not match the team's spoken language ("care circle"). Write the doc in the team's language, keep codenames for internal strategy docs, and note the mapping.
- **Distinguish metrics that look alike**: cumulative registrations vs Core MAU is the classic trap.

### 5. Propose Before Overwriting

Per Merlijn's standing preference (draft locally, validate together, then publish), present a short changelog of what will change and the open questions, then apply. Do not bulk-regenerate without showing the diff of intent first. For a routine cadence run with no surprises, a concise "here is what changed" before applying is enough; for a major shift, pause for confirmation.

### 6. Apply Updates

See the Update Targets table below. For the live metrics block (Core MAU, retention, activation, care circle size, partner regs), **do not re-derive numbers here**. Run the `update-product-analytics.md` workflow (wf-006), which pulls dated, caveated figures from Slack #insights / Porygon into `data/product-analytics.md` and reconciles the core figures into `product-context.md`. This workflow owns the qualitative/strategic state; that one owns the numbers.

After any edit to `registry.json`, **validate it parses** (`python3 -c "import json; json.load(open('pm-workspace/registry/registry.json'))"`). A broken registry silently breaks every downstream workflow.

### 7. Surface Contradictions, Do Not Rewrite History

If the research contradicts a dated, point-in-time artifact (a decision doc, a meeting deck, a spec), **flag it for Merlijn**. Do not silently edit dated artifacts, they are a record of what was true then. Only the living docs (foundation, registry, memory) get rewritten.

### 8. Output a Changelog

Close with: what changed (table), the substantive shifts since the baseline, contradictions flagged, and any sections still unfillable from these sources (e.g. placeholders). Convert relative dates to absolute.

### 9. Feedback

Offer the feedback prompt (as defined in CLAUDE.md).

## Update Targets

| File | What to refresh |
|---|---|
| `context/product-context.md` | The full rewrite: north star, current strategic context, OKRs, strategy/positioning, segmentation, shipped product, partnerships, tech stack, team roster, data caveats. Bump "Last updated". (Live metric values come from wf-006, not from here.) |
| `data/product-analytics.md` | Owned by wf-006 (Update Product Analytics). Run it for the dated, caveated numbers; this workflow consumes its output. |
| `registry/registry.json` | The `ctx-001` entry (summary, status, `updated`), top-level `last_updated`. Add any new artifacts discovered. Validate JSON after. |
| `memory/MEMORY.md` + memory files | Correct stale facts, add new durable non-derivable facts (current strategy, north star, naming caveats). One fact per file, update the index. Do not duplicate what the foundation doc now records. |
| `memory/reference_ditto_names.md` | New team members and any partner/vendor name garbles surfaced (voice dictation mangles these). |

## Guardrails

- **No single em dashes in copy** (Mewtwo house style). Use colons, commas, parentheses, periods.
- **Tables for comparisons, bullets only for discrete items.**
- **Read-only research.** Agents never send Slack messages, create Linear issues, or write files.
- **Don't conflate metrics.** State the definition next to the number.
- **Cite the source and date** for any contested figure.

## Quality Gates

- [ ] All three integrations verified live before fan-out
- [ ] Each fact in the rewrite is traceable to a source (≥2 for settled claims)
- [ ] Metric definitions stated; cumulative vs Core MAU not conflated
- [ ] Conflicts flagged, not silently resolved
- [ ] `registry.json` validated as parseable after edits
- [ ] Point-in-time artifacts flagged, not rewritten
- [ ] `product-context.md` "Last updated" bumped; changelog presented to Merlijn
- [ ] Open questions listed for Merlijn to confirm
