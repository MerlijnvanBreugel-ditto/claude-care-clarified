# Phase 4 · Tell users

A shipped feature users never discover is a feature you didn't ship. What we activate depends on the size of the release.

## Communication matrix

| Channel | Explore bet | Exploit improvement | Polish |
|---|---|---|---|
| **App update** (store notes) | ✓ | ✓ | ✓ |
| **In-app "What's new"** | ✓ | ✓ | ✓ |
| **Email** | ✓ | — | — |
| **Push notification** | ✓ | — | — |
| **Socials** (Insta) | ✓ | ✓ | — |
| **LinkedIn** | ✓ | ✓ | — |

## In-app "What's new" via Firebase

"What's new" content is managed through Firebase remote config, so we can publish an in-app announcement without a new app release or mobile-dev involvement (PRO-934). This decouples user-facing messaging from the release train. Mobile only builds the rendering once; content updates are ours to ship.

## Monthly new-features email

Once a month, an email goes to all users summarising what's new. Where it adds clarity, we record a short walkthrough video to show the feature, but the video is optional and never blocks the email.

## App-store notes

Published in Phase 2 (EN + NL). They are the baseline channel for every release, including Polish.
