# Learning: Jira Ticket Naming & Descriptions

**Date:** 2026-03-03
**Verdict:** Corrected
**Context:** Feature Measurement workflow — first run on DPMA-1964

## What Went Wrong

Created tickets with redundant context:
- Titles included epic name prefix ("CC V2 | Define Business Metrics — Enhanced Sharing P1")
- Descriptions repeated epic reference, feature name header, and classification that Jira already shows

## Why

Over-specifying for clarity. But in Jira, the parent epic is always visible — repeating it in child ticket titles and descriptions is noise that makes tickets harder to scan.

## Rule

**Jira tickets are children of epics. Don't repeat what the parent already provides.**
- Titles: Short, action-oriented. "Define Business Metrics", not "CC V2 | Define Business Metrics — Enhanced Sharing P1"
- Descriptions: Jump straight into content. No title header, no epic reference, no classification metadata — Jira has that context.
- Same applies to markdown templates: don't bake in fields that Jira manages.
