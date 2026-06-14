# PRD: [Feature Name]

## Document Info

| Field | Value |
|-------|-------|
| Author | [Name] |
| Created | [Date] |
| Last Updated | [Date] |
| Status | Draft / In Review / Approved |
| Priority | P0 / P1 / P2 |
| Target Release | [Version/Date] |
| Stakeholders | [Names] |

---

## Executive Summary

[3-5 sentence summary of the problem, solution, and expected impact. Write this last after completing all other sections.]

---

## 1. Problem Definition

### 1.1 Problem Statement

[Detailed description of the problem we're solving. Be specific about who experiences this problem, when, and why it matters.]

### 1.2 Target Users

| Segment | Description | Size | Priority |
|---------|-------------|------|----------|
| [Primary segment] | [Description] | [N users] | Primary |
| [Secondary segment] | [Description] | [N users] | Secondary |

#### User Personas

**Persona 1: [Name]**
- Role: [Role]
- Goals: [What they're trying to accomplish]
- Pain points: [Current frustrations]
- Quote: "[Representative quote from research]"

### 1.3 User Pain Points

| Pain Point | Severity | Frequency | Evidence |
|------------|----------|-----------|----------|
| [Pain 1] | High/Med/Low | Daily/Weekly/Monthly | "[User quote]" |
| [Pain 2] | High/Med/Low | Daily/Weekly/Monthly | [Data point] |

### 1.4 Current State & Workarounds

[How do users currently solve this problem? What tools/processes do they use?]

### 1.5 Evidence & Research

| Source | Key Finding |
|--------|-------------|
| Market research | [Finding] |
| Competitive analysis | [Finding] |
| User feedback | [Finding] ([N] mentions) |
| Usage data | [Finding] |

### 1.6 Business Impact

- **Revenue opportunity**: [Estimate and rationale]
- **Retention impact**: [How this affects churn]
- **Strategic alignment**: [How this fits product strategy]

---

## 2. Solution Overview

### 2.1 Proposed Solution

[Detailed description of the solution. Explain the approach and why this solution addresses the problem.]

### 2.2 Key Capabilities

| Capability | Description | Priority |
|------------|-------------|----------|
| [Capability 1] | [What it does] | Must Have |
| [Capability 2] | [What it does] | Must Have |
| [Capability 3] | [What it does] | Should Have |
| [Capability 4] | [What it does] | Nice to Have |

### 2.3 Solution Principles

1. **[Principle 1]**: [Why this matters]
2. **[Principle 2]**: [Why this matters]
3. **[Principle 3]**: [Why this matters]

### 2.4 Scope

#### In Scope
- [Item 1]
- [Item 2]
- [Item 3]

#### Out of Scope
| Item | Reason | Future Consideration |
|------|--------|---------------------|
| [Item 1] | [Why not now] | v2 / Never / TBD |
| [Item 2] | [Why not now] | v2 / Never / TBD |

---

## 3. User Stories & Requirements

### 3.1 User Stories

#### Epic: [Epic Name]

---

**US-001: [Story Title]**

> As a [user type], I want to [action], so that [benefit].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] [Additional criterion]

**Priority**: Must Have
**Estimate**: S / M / L / XL

---

**US-002: [Story Title]**

> As a [user type], I want to [action], so that [benefit].

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Priority**: Should Have
**Estimate**: M

---

[Continue for all user stories...]

### 3.2 Functional Requirements

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-001 | [System shall...] | Must | |
| FR-002 | [System shall...] | Must | |
| FR-003 | [System shall...] | Should | |

### 3.3 Non-Functional Requirements

| Category | Requirement | Target |
|----------|-------------|--------|
| Performance | Page load time | < 2 seconds |
| Performance | API response time | < 500ms |
| Scalability | Concurrent users | 10,000 |
| Availability | Uptime | 99.9% |
| Security | [Requirement] | [Target] |
| Accessibility | WCAG compliance | Level AA |

---

## 4. User Experience

### 4.1 User Flow

```
[Entry Point]
      │
      ▼
┌─────────────┐
│  Screen 1   │
│  [Action]   │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌─────────────┐
│  Screen 2   │────▶│  Alt Path   │
│  [Decision] │     │  [Action]   │
└──────┬──────┘     └──────┬──────┘
       │                   │
       ▼                   │
┌─────────────┐           │
│  Screen 3   │◀──────────┘
│  [Success]  │
└─────────────┘
```

### 4.2 Key Screens

| Screen | Purpose | Key Elements |
|--------|---------|--------------|
| [Screen 1] | [Purpose] | [Elements] |
| [Screen 2] | [Purpose] | [Elements] |

### 4.3 Edge Cases & Error States

| Scenario | Expected Behavior | Error Message |
|----------|-------------------|---------------|
| [Edge case 1] | [Behavior] | "[Message]" |
| [Empty state] | [Behavior] | "[Message]" |
| [Error state] | [Behavior] | "[Message]" |
| [Timeout] | [Behavior] | "[Message]" |

### 4.4 Content & Copy

| Location | Copy | Notes |
|----------|------|-------|
| [Page title] | "[Text]" | |
| [CTA button] | "[Text]" | |
| [Error message] | "[Text]" | |
| [Empty state] | "[Text]" | |

---

## 5. Technical Considerations

### 5.1 Technical Questions for Engineering

| # | Question | Context | Impact on Design |
|---|----------|---------|------------------|
| 1 | [Question] | [Why asking] | [What depends on answer] |
| 2 | [Question] | [Why asking] | [What depends on answer] |

### 5.2 Known Technical Constraints

- [Constraint 1]: [How it affects the feature]
- [Constraint 2]: [How it affects the feature]

### 5.3 Dependencies

| Dependency | Team/System | Status | Risk |
|------------|-------------|--------|------|
| [Dep 1] | [Owner] | Ready / In Progress / Blocked | Low/Med/High |
| [Dep 2] | [Owner] | Ready / In Progress / Blocked | Low/Med/High |

### 5.4 Data Requirements

**New data needed:**
- [Data element]: [Source/creation]

**Data migrations:**
- [Migration if needed]

**Analytics events:**
| Event | Trigger | Properties |
|-------|---------|------------|
| [Event name] | [When fired] | [Properties to track] |

### 5.5 Integration Points

| Integration | Purpose | Complexity |
|-------------|---------|------------|
| [System/API] | [Purpose] | Low/Med/High |

---

## 6. Success Metrics

### 6.1 Key Metrics

| Metric | Current | Target | Timeline | Measurement |
|--------|---------|--------|----------|-------------|
| **North Star**: [Metric] | [X] | [Y] | [When] | [How] |
| [Adoption metric] | [X] | [Y] | [When] | [How] |
| [Engagement metric] | [X] | [Y] | [When] | [How] |
| [Business metric] | [X] | [Y] | [When] | [How] |

### 6.2 Guardrail Metrics

[Metrics that should NOT decrease]
- [Metric 1]: Must stay above [X]
- [Metric 2]: Must stay above [X]

### 6.3 Measurement Plan

[How we'll track, who owns reporting, cadence of reviews]

---

## 7. Launch Plan

### 7.1 Timeline

| Milestone | Date | Owner | Status |
|-----------|------|-------|--------|
| PRD Approved | [Date] | PM | |
| Design Complete | [Date] | Design | |
| Tech Spec Complete | [Date] | Eng | |
| Development Complete | [Date] | Eng | |
| QA Complete | [Date] | QA | |
| Launch | [Date] | PM | |

### 7.2 Rollout Strategy

| Phase | Audience | Duration | Success Criteria |
|-------|----------|----------|------------------|
| Internal | Team only | 1 week | No critical bugs |
| Beta | [N] users | 2 weeks | [Metrics] |
| GA 25% | 25% of users | 1 week | [Metrics] |
| GA 100% | All users | - | [Metrics] |

### 7.3 Feature Flags

| Flag | Purpose | Default |
|------|---------|---------|
| [flag_name] | [Purpose] | Off |

### 7.4 Go-to-Market

- **Documentation**: [What needs updating]
- **Training**: [Who needs training]
- **Communication**: [How we'll announce]
- **Support**: [Support team preparation]

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Mitigation strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Mitigation strategy] |
| [Risk 3] | High/Med/Low | High/Med/Low | [Mitigation strategy] |

---

## 9. Open Questions

| # | Question | Owner | Due Date | Status |
|---|----------|-------|----------|--------|
| 1 | [Question] | [Name] | [Date] | Open / Answered |
| 2 | [Question] | [Name] | [Date] | Open / Answered |

---

## 10. Appendix

### A. Research & References
- [Link to discovery insights]
- [Link to competitive analysis]
- [Link to user feedback synthesis]
- [Link to market research]

### B. Design Assets
- [Link to wireframes]
- [Link to mockups]
- [Link to prototype]

### C. Technical Documentation
- [Link to tech spec]
- [Link to API docs]

### D. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Name] | Initial draft |
| 0.2 | [Date] | [Name] | [Changes] |
