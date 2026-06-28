# Ditto Onboarding App

A personalized, no-login web app that gives a new hire everything they need for a stellar first month: context, guidance, expectations, and the practical stuff. High-energy, warm, lightly gamified. The goal is that after a month a new hire thinks *"I'm fully onboarded. I know why I'm here, how we work, who my people are, and I've already contributed."*

This folder holds the **spec and the content**, not the built app. Build it in Lovable, by hand, or hand it to a dev. The point is that it is **remixable**: one shell, one content file per hire.

## What's here

| File | What it is |
|---|---|
| `PRD.md` | The product spec. Read this to build the app. |
| `content-schema.md` | The data contract. The shell reads one content file per hire; this defines its shape. |
| `brand-lead/content.json` | The fully-drafted onboarding for April (Brand Lead), in schema form. The live example. |
| `brand-lead/readings/` | Long-form in-app readings referenced by `content.json`. |
| `brand-lead/onboarding-content.md` | The original raw brief. Source of truth for April's plan. Not consumed by the app. |

## How to remix for a new hire

1. Copy `brand-lead/` to a new folder, e.g. `growth-analyst/`.
2. Edit `content.json`: the hire block, the chapters, the items, the welcome. Keep item `id`s stable per hire (progress is tracked by id).
3. Replace anything in `readings/` that was role-specific.
4. Generate a fresh URL token for the hire (see `PRD.md` → Identity & persistence) and send them the link.

Content is the only thing that changes between hires. The app shell, the gamification, and the backend stay the same.

## Status

Spec + April's launch content drafted for Merlijn's review. Items tagged `[confirm]` need a hard fact before April's start date (June 22, 2026).
