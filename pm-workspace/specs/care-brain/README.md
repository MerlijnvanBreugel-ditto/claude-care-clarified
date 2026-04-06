# Care Brain: Complete Specification Package

**Last updated**: 2026-04-05
**Status**: Internal drafts for review and prototyping

---

## What this is

A comprehensive specification package for transforming Ditto from a medical conversation summarization tool into a care intelligence platform. The "Care Brain" is an AI backend that powers every surface of the app: understanding conversations, building health profiles, answering questions, and distributing contextual understanding across care circles.

## Documents

### Strategy & Analysis

| File | What it covers |
|---|---|
| [care-brain-strategy.md](care-brain-strategy.md) | Strategic spec. Why now, critical review of ZeroClaw, market intelligence, "brain not chatbot" positioning, 6-month phased plan, multi-perspective review. |
| [business-case.md](business-case.md) | Financial model, TAM, revenue scenarios (B2C + B2B2C), cost model ($0.07/interaction), moat analysis, risk assessment, investment thesis, persona critiques. |
| [competitive-analysis.md](competitive-analysis.md) | Head-to-head analysis of 7 competitors. Confirms unique position: no one builds audience-adapted health sharing for care circles. 18-24 month window. |

### Phase 1 Spec

| File | What it covers |
|---|---|
| [care-brain-phase1-smart-suggestions.md](care-brain-phase1-smart-suggestions.md) | Functional spec for Smart Suggestions: contextual Q&A on summaries via suggestion chips. Interface design, technical approach, tracking plan, multi-perspective review. |

### Architecture Directions (Prototype-Ready)

Three complete architecture specs, each detailed enough for a Claude Code agent to prototype.

| File | Direction | Key idea | Best for |
|---|---|---|---|
| [direction-a-concierge.md](direction-a-concierge.md) | **The Concierge** | Single Claude agent with tools. One brain, many capabilities. | PoC, prompt validation |
| [direction-b-clinic.md](direction-b-clinic.md) | **The Clinic** | Orchestrator + specialist agents. Each expert in one domain. | Production architecture |
| [direction-c-nervous-system.md](direction-c-nervous-system.md) | **The Nervous System** | Event-driven pipelines. Stateless workers, persistent store. | Scale, reliability |

Each direction spec includes:
- Full system prompts (actual text)
- Tool/agent definitions with I/O schemas
- Health Profile JSON schema
- 3 end-to-end request flow scenarios
- API contract
- Cost model
- Prototype scope and timeline

### Presentation

| File | What it covers |
|---|---|
| [presentation.html](presentation.html) | 20-slide internal strategy deck. Open in browser. Arrow keys to navigate. |

## How to use this

**For strategic review**: Start with `care-brain-strategy.md`, then `business-case.md` and `competitive-analysis.md`.

**For prototyping**: Pick a direction (A, B, or C), hand the spec to a Claude Code agent. Each spec is self-contained with actual prompts, schemas, and API shapes. Compare outputs on 10 real Ditto conversations.

**For presenting**: Open `presentation.html` in a browser.

## Related artifacts

- [ZeroClaw JTBD Discovery](../ideas/health-agent/zeroclaw-jtbd-discovery.md) (superseded by this package)
- [Unicorn Thesis](../ideas/activation-and-audience/unicorn-thesis-consumer-layer-healthcare.md) (foundation for business case)
