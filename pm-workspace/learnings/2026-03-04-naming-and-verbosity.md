# Learning: Event Naming Convention & Output Verbosity

**Date:** 2026-03-04
**Verdict:** Corrected
**Context:** Feature Measurement workflow — tracking plans across DPMA-1964, DPMA-1966, DPMA-1903

## What Went Wrong

1. **Naming:** Used `snake_case` for event names (e.g., `care_circle_follow_request_sent`) when the tracking sheet uses Title Case with dash separator (e.g., `Care Circle - Follow Request Sent`).
2. **Verbosity:** Workflow file and ticket descriptions were too wordy. Merlijn wants sharp, to-the-point output.

## Rule

- **Event names:** Title Case with feature prefix and dash separator — match the tracking sheet exactly. Properties stay `snake_case`.
- **Output:** Cut the filler. Tables > prose. If it can be said in one line, don't use three. Workflow files should be scannable reference docs, not essays.
