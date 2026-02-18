# DPMA-1964: Enhanced Sharing Personalization

## User Story

As a patient, I want to personalize what I share from my appointment and control who receives it, so I can keep my Care Circle informed in a way that feels personal and appropriate for each relationship.

## Why (Problem)

Current sharing is one-size-fits-all. Users either share the full summary with everyone or don't share at all. This creates friction because:

- Some information is sensitive for certain family members
- Users want to add emotional context ("I'm feeling good about this")
- Different relationships need different levels of detail

**Supports strategic goal**: Make Care Circle more social (Future Direction) and improve the 35-40% share rate.

## Jobs to Be Done

- **Share**: "I want to keep my family informed without repeating myself"
- **Support**: "I want to help my loved one manage their care" (follower side)

---

## Functional Requirements

### P1: Personal Messaging Layer

- User can add a personal note when sharing an appointment
- Personal note appears **above** the structured appointment data
- AI generates a suggested 5-sentence summary when the appointment summary is generated
- User can edit, replace, or remove the AI suggestion before sharing
- Character limit: [TBD - suggest 500 chars]

### P1: Share History (Per-Appointment)

- Each appointment shows who it was shared with and when
- Visible on the appointment detail screen (not a separate view)
- Shows: recipient name, date shared, whether personal message was included

### P1: Edit & Delete Shares

- User can edit their personal message after sharing (marked as "edited" for recipients)
- User can delete a share entirely (removes from recipient's view)
- Confirmation required before delete

### P2: Selective Recipient Selection

- Default: all followers are selected
- User can deselect specific followers before sharing
- Selection UI shows follower names with checkboxes

### P3: Different Updates to Different People

- User can share the same appointment multiple times with different personal messages
- Each share action is independent (not simultaneous multi-version)
- Share history shows all versions sent

### P3: Image Attachments (Optional)

- User can attach images when sharing (camera, photo library, or documents)
- Images appear below the personal message
- Limit: [TBD - suggest 3 images max]
- Supported formats: JPG, PNG, PDF

---

## Success Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Share completion rate | 35-40% | 50%+ |
| Recipient engagement (views) | [baseline TBD] | +20% |
| Personal message usage | N/A | 30%+ of shares |

---

## Out of Scope

- Group/circle presets (user-defined default groups)
- Reactions from followers (separate initiative)
- Messages back from followers (separate initiative)

---

## Open Questions

1. Character limit for personal messages?
2. Max number of images per share?
3. Should AI summary be opt-in or always generated?

---

## Technical Considerations

- Personal messages are end-to-end encrypted (per existing Care Circle encryption)
- Edit/delete requires updating recipient's local cache
- AI summary generation hooks into existing LLM pipeline

---

## References

- [Product Canonical Description](../business-context/DG-Product%20Canonical%20Description-101225-141554.pdf)
- Jira: https://dittocare.atlassian.net/browse/DPMA-1964
