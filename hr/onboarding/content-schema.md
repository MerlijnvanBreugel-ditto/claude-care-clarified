# Content Schema

The remix contract. The app shell renders whatever this file says. Change the file, change the onboarding. Don't hardcode any of this in the app.

One content file (`content.json`) per hire, plus an optional `readings/` folder for long-form bodies.

## Top-level shape

```jsonc
{
  "contentRef": "brand-lead",        // stable id, matches the folder name and the record's contentRef
  "hire": { ... },                    // who this is for
  "intro": { ... },                   // the 3-view first-open flow
  "chapters": [ ... ],                // the 5 chapters, in display order
  "feedback": { ... }                 // the persistent feedback chapter config
}
```

## `hire`

```jsonc
{
  "name": "April",
  "role": "Brand Lead",
  "startDate": "2026-06-22",          // ISO date; drives the on-track status
  "manager": "Merlijn",
  "collaborators": ["Merlijn", "Ilayda", "Niek"]
}
```

## `intro`

The first-open flow. Three views the hire clicks through, then a readiness prompt. Founder-personal voice. `signedBy` shows on the welcome.

```jsonc
{
  "signedBy": "Merlijn",
  "views": [
    { "id": "mission",  "title": "...", "body": "markdown..." },
    { "id": "why-role", "title": "...", "body": "markdown..." },
    { "id": "why-you",  "title": "...", "body": "markdown..." }
  ],
  "readyPrompt": "Ready to onboard?",
  "readyCta": "Let's go"
}
```

`body` is markdown. Keep each view to something a person reads in under a minute.

## `chapters[]`

```jsonc
{
  "id": "land-and-settle",            // stable; used in item ids and progress
  "title": "Land & Settle",
  "blurb": "One line on what this chapter is for.",
  "icon": "optional-name-or-emoji",   // optional, for the card
  "items": [ ... ]
}
```

Progress for a chapter = completed items / total items. A chapter is "done" when all its items are complete (triggers the celebration).

## `item`

```jsonc
{
  "id": "s1-ns-card",                 // GLOBALLY UNIQUE and STABLE — progress is tracked by this
  "type": "task",                     // task | action | reading | resource
  "title": "Get your NS business travel card",
  "horizon": "week1",                 // day1 | week1 | month1
  "body": "optional markdown shown inline / in a panel",
  "href": "optional external link",
  "readingRef": "readings/brand-current-state.md",  // optional: path to a long-form body
  "celebrateOnComplete": false        // optional; chapter completion celebrates regardless
}
```

### Type semantics

| Type | Meaning | Typical fields |
|---|---|---|
| `task` | A concrete thing to do and check off (set up an account, get the card). | `title`, `horizon`, optional `body`/`href` |
| `action` | A softer, human prompt (have coffee with Niek, introduce yourself in #general). | `title`, `horizon`, optional `body` |
| `reading` | Something to read. Short → inline `body`. Long → `readingRef` (renders a markdown file). External → `href`. | one of `body` / `readingRef` / `href` |
| `resource` | A link worth keeping (Drive folder, deck, brandbook). Opens out. | `title`, `href` |

### Rules

- **Every item has `id`, `type`, `title`, `horizon`.**
- A `reading` must have exactly one of `body`, `readingRef`, or `href`.
- A `resource` must have `href`.
- `id`s must be stable across edits for a given hire — changing an id orphans that hire's completion state. Prefix by chapter for sanity (`s1-`, `s2-`...).
- Completion is always a self-check, for every type.

## `feedback`

Config for the persistent Feedback chapter. Entries are stored on the hire's record (see `PRD.md`), not in this file.

```jsonc
{
  "title": "How can we onboard better?",
  "blurb": "Jot down anything: a gap, a task that didn't fit, something you missed, an idea. Share it live too when you can — this is the easy log.",
  "placeholder": "What would have made this smoother?"
}
```

## On-track status (computed, not stored)

The app derives status from `hire.startDate`, today's date, and each item's `horizon`:

- After day 1: `day1` items expected complete.
- After 7 days: `week1` items expected complete.
- After 28 days: `month1` items expected complete.

Show a friendly summary ("On track for your first week", "2 Week-1 items still open"). Never punitive. No global percentage.
