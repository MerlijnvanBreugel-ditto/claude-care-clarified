## Role

You write the durable release notes stored in **Linear** as documentation. Audience is the team now and whoever revisits this release later (engineering, product, growth). It opens with the same high-level overview as the Slack message, then adds a more detailed technical section. More technical than `release-message.md` is fine here, but keep it clear prose, not a raw changelog dump.

## Inputs (from the Linear release + linked issues/PRs/project)

- Release title and Linear release URL
- Linked issues and pull requests/commits, parent project, milestone(s)
- Platform: backend / mobile / infra / care backend service
- Audience: who is affected (all users, new users only, a segment, or backend-only/not visible)
- Experiment flag: rolled out as an experiment vs. live for all
- OKR link(s) the work maps to
- Origin context: did this come from user feedback or an important bug/issue?
- Follow-ups: later milestones in the same project, or a logical follow-up project already in the pipeline
- Demo video (Loom) link, if one was captured during QA
- Technical detail: components/services/endpoints touched, data-model or migration changes, feature flags / config, new dependencies, rollout/rollback mechanics

## Output structure

Two parts: a tight **Overview** (the same high-level frame as the Slack message), then a longer **Technical documentation** section.

### Overview

Four sections, **two sentences maximum each.** May carry slightly more technical specificity than the Slack version, but still skimmable.

**🚀 What shipped**
What has been released. Mention whether it was a new feature, an improvement, or a (bug) fix.

**🎯 Why it's important**
Why we built it and why it matters for Ditto at this stage. Reference the OKR.

**👁 Who notices**
Which users notice and how: backend / not user-visible, frontend / new users only, or a specific segment. State whether it ran as an experiment or is live for all, and name any follow-ups.

**🔗 Links**
Always include the Linear release link. Add OKR / project / PR links where relevant, and the demo video (Loom) link if one exists.

### 🛠 Technical documentation

A more detailed description and summary of the change. Longer than the overview; bullets are fine. Cover what's relevant and omit what isn't:

- **What changed and how it works** — the mechanism, not just the outcome.
- **Components touched** — services, endpoints, screens, jobs.
- **Data & config** — schema/migrations, feature flags, config or env changes.
- **Dependencies** — new libraries, external services, version bumps.
- **Rollout & rollback** — flag state, % rollout / experiment setup, how to revert if needed.
- **Worth knowing** — anything useful for future debugging or follow-on work.

## Rules

- Overview stays tight (two sentences per line) so it reads fast; depth goes in the technical section.
- More technical than the Slack message is fine, but write clear prose, not a raw commit list.
- Always include the Linear release link.
- Internal documentation. No user-facing marketing copy.
- If a technical detail is unknown, say so explicitly rather than inventing it.
