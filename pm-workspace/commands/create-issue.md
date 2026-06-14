# /create-issue

> Turns raw input (user message, bug report, email, voice memo, screenshot context) into a well-structured Linear issue. Defaults to the Product team; clarifies before creating; flags duplicates.

## Usage

```
/create-issue [raw input]
/create-issue [paste WhatsApp / email thread]
/create-issue [bug description + attached screenshot]
```

## What It Does

1. Loads `pm-workspace/workflows/create-issue.md`
2. Parses the raw input — classifies type (bug / feature / ops task / spec iteration)
3. Picks team: **Product by default**, Operations / Partnerships / Marketing only when the input clearly belongs there
4. Searches Linear for likely duplicates (title keywords + project)
5. **If duplicates found → flags first, doesn't create**
6. **If input is vague, contradictory, or missing critical fields → asks Merlijn before creating**
7. Drafts the issue using the matching template (bug / feature / ops / spec iteration)
8. Creates in Linear with appropriate labels, project, assignee
9. Returns the issue URL + a 1-sentence summary of the call

## $ARGUMENTS

Raw input. Anything goes — pasted email, transcript, screenshot description, voice memo, half-formed thought. The workflow does the structuring.

## Defaults

- **Team:** Product
- **Assignee:** Merlijn (unless input names someone else, e.g. "put it on Hester's name")
- **Labels:** `Bug` for bugs; otherwise none unless input specifies
- **Privacy:** redact phone numbers and home addresses unless they're operationally required (flyer ship-to is fine; user phone in a bug ticket is not)
