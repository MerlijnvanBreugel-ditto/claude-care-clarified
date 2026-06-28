# Phase 3 · Tell the team

The problem this fixes: the team loses track of what shipped and when. Care Circle went live and most of the team didn't know. Internal communication is now automatic where it can be, and a habit where it can't.

## Auto-post to #releases

A GitHub action posts each Linear release note into the **#releases** Slack channel automatically (owner: Iman). No one has to remember. The Linear entry from Phase 2 is the source, so if the entry is good, the post is good.

## Weekly release digest

A weekly Slack routine compiles everything released that week into one digest and builds an artifact that ingests the Figma frames included in those releases (owner: Merlijn). It gives the team one place to see the week at a glance, paired with the visuals.

## Walkthrough video library

The QA walkthrough videos from Phase 1 accumulate in Linear into a browsable library of how every new feature works. This is the team's self-serve answer to "what does the new thing actually do."

## Friday demo

The Friday session is split in two: first a visual overview of what shipped and was released, then demos and wins.

## When to post a team-wide update, and who

Not every change needs a broadcast. The auto-post to #releases covers everything; a **team-wide update** is the louder signal for things that matter.

| | Triggers a team-wide update | Release-log only |
|---|---|---|
| **What** | Any user-facing feature, or any change expected to move a core metric | Internal, infra, or invisible changes |

**Who posts:** the feature owner (the problem owner on the release). The PM backstops if they don't. The builder records the walkthrough video.

> Open team decisions tracked in OPS-145 (trigger), OPS-146 (template), OPS-147 (ownership). The rows above are the proposed defaults to confirm.
