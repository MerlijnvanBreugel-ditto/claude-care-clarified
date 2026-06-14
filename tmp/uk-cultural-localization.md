# UK Cultural Localisation

Source: `tmp/ditto-receive-en.json`
Scope: strings whose content, references, or framing assume a Dutch healthcare context (NL law, Dutch institutions, NL-only healthcare roles, EU-only data residency, Dutch awards/partners). These need rewriting, not just translating.

Decision required from you on a few of them — flagged with **🟡 decide**.

---

## 1. Recording legality — Netherlands → UK

Three strings tell users that recording a doctor's conversation is allowed "in the Netherlands". UK law is similar but the framing should match the audience, and the Medical Council guidance differs.

**Legal background (UK):** Recording your own medical consultation for personal use is lawful in the UK without the doctor's consent (single-party consent under Data Protection Act 2018 — personal/domestic use exemption). GMC guidance recommends informing the clinician. Sharing the recording is a separate question.

| Key | Current | Suggested rewrite |
|---|---|---|
| `home.recordingInfo.description` / `.explanation` | In the Netherlands you are allowed to record a conversation with your doctor as long as you are part of the conversation. This can help you remember important medical information. | In the UK you can record a conversation with your doctor for your own personal use, as long as you're part of the conversation. It can help you remember important medical information. |
| `recordingInfo.explanation` / `recordingInfo.description` | (same NL string) | (same UK rewrite) |

Bullet points in `home.recordingInfo` / `recordingInfo` are universal and stay:
- "You can record for personal use" ✅
- "You cannot share the recording with others without permission" ✅
- "Open communication with your doctor helps build trust" ✅

🟡 **decide**: include a soft reference to GMC guidance ("Most GPs are comfortable with this — it's helpful to let them know up front") to match UK patient norms?

---

## 2. Terms & Conditions — Dutch law

`onboarding.termsAndConditions.fulltext` contains:

> **10. Dutch law applies** - Any disputes will be resolved under Dutch law in Rotterdam courts.

🔴 **Legal decision needed.** Two paths:

1. **Keep Dutch jurisdiction** (Ditto BV operates from Rotterdam). Legally valid for UK users if disclosed and accepted, but reads oddly. Rewording: *"Ditto is a Dutch company. Any disputes will be governed by Dutch law and resolved in Rotterdam courts."*
2. **Establish UK terms** for UK users — requires legal review and a UK entity or local representative. Out of scope of a translation pass.

Other items in the same string to revisit:

| Item | Note |
|---|---|
| **5. Minimum age** "at least 16 years old" | UK GDPR sets the age of consent for digital services at 13. The 16 floor is stricter (fine), but check if the product intentionally restricts UK 13–15-year-olds. |
| **4. AI processing** "secure EU servers" | ✅ **Keep as-is.** No UK servers exist; data is processed in the EU. Post-Brexit, EU residency is legal under UK GDPR (adequacy decision), so no rewording needed. |
| **General GDPR references** | ✅ Keep "European privacy laws (GDPR)" — UK GDPR is functionally identical and "GDPR" reads as universal to UK users. |

Related strings — no changes recommended:
| Key | Current | Decision |
|---|---|---|
| `onboarding.privacy.description` | We follow European privacy laws (GDPR)… | Keep. |
| `onboarding.privacy.dataInEU` | If you use our AI, your data is processed within the EU and immediately deleted afterwards. | Keep — accurate for UK users too. |
| `privacyPolicy.inbox.body` | Your data stays in the EU and is never linked to your identity. | Keep. |

---

## 3. Healthcare-professional taxonomy

UK and NL primary-care roles differ. Quick map:

| `hcp.type.*` key | Current | UK status | Suggested |
|---|---|---|---|
| `gp` | General Practitioner | ✅ universal — but UK users say "GP" | Keep "General Practitioner" as long form; UI labels elsewhere should use "GP" |
| `specialist` | Specialist | ✅ | Keep |
| `nurse` | Nurse | ✅ | Keep |
| `dentist` | Dentist | ✅ | Keep |
| `physio` | Physiotherapist | ✅ UK form | Keep |
| `pharmacist` | Pharmacist | ✅ | Keep |
| `maternity` | Maternity Caregiver | 🔴 **role doesn't exist in UK** | Drop, or replace with "Maternity Nurse" / "Postnatal Doula". The Dutch *kraamverzorgster* (home maternity carer in the days after birth) has no NHS analogue. |
| `midwife` | Midwife | ✅ — and more central in UK pathway than NL | Keep, possibly promote in ordering |
| `hospital` | Hospital | ✅ | Keep — though typically a *place*, not a *type of HCP*. Worth a separate look. |
| `other` | Other | ✅ | Keep |

**Roles missing from a UK list that you might want to add:**
- Health Visitor (universal NHS role for new parents — culturally important)
- Practice Nurse (distinct from GP)
- Mental Health Practitioner / IAPT therapist
- Optician
- Paramedic

---

## 4. "Doctor's office" / "doctor's practice" — keep broad

✅ **Decision: keep "doctor" terminology throughout.** Ditto is used as much with hospital specialists as with GPs, so narrowing to "GP" / "GP surgery" would be wrong for a large share of UK use.

The only string that needs a small tweak is the NL-flavoured "doctor's practice" framing:

| Key | Current | Suggested |
|---|---|---|
| `activation.step.4.sheet.title` | Use of Ditto in the doctor's practice | Use of Ditto during a doctor's visit |
| `activation.infographic.recording.card.description` | This is a recording of a conversation with the general practitioner, try it out. | This is a recording of a conversation with a doctor — try it out. |
| `question.library.24` | Should I see my general practitioner about this? | Should I see a doctor about this? |

Everywhere else — "doctor's appointment", "doctor's visit", "your doctor" — **keep as-is**. UK English handles "doctor" as a general term naturally, and it covers GPs, specialists, hospital consultants, and dentists. No changes to:

- `home.addEvent.title` ("Doctor's appointment coming up?")
- `home.recordingInfo.title` / `recordingInfo.title`
- `onboarding.notifications.bullet2`
- `home.youtubeVideos.video1.description`
- `home.welcomeCard.description`
- `home.preparationInfo.*`
- `appointment.morning.reminder.body`

`hcp.type.gp` ("General Practitioner") stays — it's the long form for the GP option in the type-of-care picker.

---

## 5. NL-specific specialist reference

`activation.infographic.summary.specialist.description`:

> If the complaints persist, a consultation with an orthomanual physician may be useful.

🔴 **"Orthomanual physician"** (*orthomanueel arts*) is a Dutch medical specialty that doesn't exist in the UK. The example is also taken from a back-pain scenario.

| Suggested replacement | When to use |
|---|---|
| "…a referral to a musculoskeletal physiotherapist may be useful." | Closest NHS analogue for back pain |
| "…seeing an osteopath may be useful." | If keeping the manual-therapy angle (osteopathy and chiropractic exist in UK private care) |
| "…a referral to a specialist may be useful." | Safest generic — keeps the example flexible |

Note: this whole infographic example is a back-pain consultation with physio follow-up. The example holds; only the "orthomanual physician" line needs to change.

---

## 6. Dutch awards and institutions

✅ **Decision: keep these references, but make the Dutch context explicit so UK users understand them as international credibility signals, not as something they're being asked to act on.**

| Key | Current content | Suggested rewrite |
|---|---|---|
| `home.resources.card.nomination.heading` | Help Ditto win the National Healthcare Innovation Prize 🎉 | Help Ditto win the Dutch Healthcare Innovation Award 🎉 |
| `home.resources.card.nomination.body1` | Great news: Ditto is a national finalist! After winning our regional competition, we're now up for the biggest healthcare innovation award in the Netherlands of Zorginnovatie.nl. | Great news: Ditto is a finalist for the biggest healthcare innovation award in the Netherlands — run by Zorginnovatie.nl. |
| `home.resources.card.nomination.body2` | There's a public vote, and yours would mean the world to us. After all, we build Ditto for you. See the pitch by co-founder Tobias that we submitted. | Keep — clarifies it's a public vote. |
| `home.resources.card.nomination.howToVote.body` | Visit Zorginnovatie.nl, find Ditto among the finalists, and enter your email address. After submitting, you need to confirm your email. | Keep. |
| `home.resources.card.nomination.howToVote.deadline` | Voting closes April 14 at 5:00 PM. Don't forget to confirm your vote via email. | Reformat: "Voting closes 14 April at 5pm (CET). Don't forget to confirm your vote via email." *(making it clear it's NL time)* |
| `nomination.inbox.body` | Ditto has been nominated for the Zorginnovatieprijs. Help us with your vote. 🎉 | Ditto has been nominated for the Dutch Healthcare Innovation Award. Help us with your vote. 🎉 |
| `discover.articles.article2.title` | Menzis and Ditto collaborate on understandable health information | Menzis — one of the largest Dutch health insurers — partners with Ditto on understandable health information *(or shorter: "Menzis, a major Dutch health insurer, partners with Ditto on understandable health information")* |
| `discover.articles.article2.source` | Collaboration | Keep, or update to "Partnership". |
| `mumcFeedback.*` | You recently used Ditto during an appointment at Maastricht UMC+. | ✅ **No change needed.** This prompt isn't shown to UK users (not active in UK pilots), so the Dutch hospital name is fine where it is. |

---

## 7. Currency, units, and other locale defaults

Quick scan — no monetary amounts, no imperial vs metric units, no postcodes in the file. The only locale defaults to update are:

| Key | Current | Suggested |
|---|---|---|
| `userInfo.phone.help` | Include country code, e.g. +31 | Include country code, e.g. +44 *(also in translation file — listed there)* |
| `home.resources.card.nomination.howToVote.deadline` | April 14 at 5:00 PM | UK format: 14 April at 5pm *(also in translation file)* |

No date strings are hard-coded outside this Dutch-only block.

---

## 8. URLs and domains

✅ No changes. Both `ditto.care` and `dittocare.com` work for UK users; no `/uk` path needed.

---

## 9. Tone — keep the brand voice

✅ **Decision: preserve Ditto's positivity, freshness, and authenticity.** UK English does not require muting the voice; only fix copy that genuinely reads as wrong, not copy that reads as upbeat.

Things to leave alone (do **not** change in the UK pass):
- "We're super happy you've downloaded our app." — stays
- "You're all set!" — stays
- Exclamation marks throughout — stay
- "Help Ditto win the Dutch Healthcare Innovation Award 🎉" — stays (after the Dutch reframing above)
- "Good luck with your appointment today." — stays

Things that genuinely read as off and **should** be fixed (already in the translation file):
- "Start yourself with Ditto" — awkward English, not a tone issue
- "Most Doctors already know Ditto" — capitalisation typo
- "You have received health care update!" — missing article + spacing
- "Keep an eye out on the Play Store updates" — broken idiom

That's the bar: fix the things that are wrong, not the things that are merely cheerful.

---

## 10. Worth a separate decision — sample questions library

`question.library.1` through `.48` is a flat list of patient questions. They are mostly universal and read fine for UK ("What is going on?", "Why am I in pain?", "What treatment options are available?"). A few to flag:

| Key | Current | Note |
|---|---|---|
| `question.library.14` | Can you refer me to a specialist at the hospital? | ✅ Highly relevant in NHS context (referral gateway). Keep. |
| `question.library.18` | Is there a patient organization for people with the same illness as me? | Spelling: organisation. ✅ Concept works in UK (e.g. Macmillan, Diabetes UK). |
| `question.library.24` | Should I see my general practitioner about this? | "GP" preferred — listed above. |
| `question.library.34` | What is the NIPT blood test? | NIPT is offered privately in UK and partially via NHS. Concept fine. |
| `question.library.41` | I saw in the hospital portal that there were more abnormalities — what does that mean? | UK NHS uses NHS App / Patient Knows Best / Trust-specific portals. "Hospital portal" is generic enough. ✅ |

---

## Summary — after your decisions

| Category | Strings affected | Status |
|---|---|---|
| Recording legality (NL → UK) | 4 | ✅ Rewrite to UK framing |
| Terms & Conditions (Dutch law) | 1 (large block) | 🔴 Legal review still needed |
| HCP taxonomy: "Maternity Caregiver" | 1 | 🟡 Drop or rename (no UK equivalent role) |
| "Doctor's practice" reframing | 3 | ✅ Keep "doctor" broad; only tweak the NL-flavoured framing in 3 strings |
| Orthomanual physician | 1 | 🔴 Replace (specialty doesn't exist in UK) |
| Dutch awards (Zorginnovatieprijs) | 7 keys | ✅ Keep, reframe as "Dutch Healthcare Innovation Award" |
| Menzis partnership | 1 | ✅ Keep, add "Dutch health insurer" context |
| Maastricht UMC+ feedback | 1 | ✅ No change — not active in UK |
| Country code default | 1 | ✅ +31 → +44 |
| Data residency (EU servers) | 3 | ✅ No change — accurate for UK users too |
| Tone | many | ✅ No change — preserve brand voice |

**Net result:** 3 areas still need a real decision/replacement (T&Cs, Maternity Caregiver, Orthomanual physician). Everything else is either a clean rewrite or "no change".
