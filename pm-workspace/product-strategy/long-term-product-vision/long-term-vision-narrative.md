# Ditto — Long-term Product Vision

*Working narrative, June 2026. Up for debate. The point is to get us aligned enough to make better daily decisions, not to lock a ten-year plan.*

## Why we exist

I want to start with the why, because the vision keeps shifting but the why should be steadier.

Draft mission, up for debate: **clarify and connect care journeys, for you and your loved ones.** It extends "Care. Clarified." with the part I think is actually ours, the loved ones. Note the order: connect only works when it rides on clarify. Once we make a care journey understood, connecting the people around it becomes natural. The other way around, we are just another chat group.

This sits on the belief we started from. The patient is massively underserved, and the patient is the unlock for a system that is otherwise stuck. Scribes took off because the technology finally caught up, but the real gap was never the doctor's note. It was the person walking out of the room with a failing memory, a notepad, and a letter full of Latin that tells them they have cancer. EHRs have not fixed that. They gave us clunky software, fragmentation, and portals that store data without ever explaining it.

## The honest starting point

We have to be clear-eyed about today's product. Summaries cannot be the goal.

Summary tools are a commodity now and they keep getting more reliable. Within about a year, patient-facing summaries are native in the EHR and in the big assistants. When ChatGPT or Gemini ship conversation summaries, that attacks us directly, and "doctors will never allow it" is wishful thinking. A summary is also low frequency. It matters around the appointment and maybe the day after, which is a reason to open Ditto weekly at most. Low frequency is hard to monetize, because consumers do not pay easily for health apps and insurers want to see real activity before they reimburse. Pushing frequency or growth features for their own sake does not fix that. You cannot nudge your way out of a thin value proposition.

But the wedge is genuinely strong, and we should not undersell it:

- Our summaries are better than the alternatives, and people trust them. That trust is the asset, and we have to keep measuring it rather than assuming it.
- We are roughly 10x better than the real alternative, which is forgetting.
- Recordings and summaries hold far more than we unlock today.

The deeper point is this. The thing nobody else owns is not the summary file. It is **the understood medical conversation** - the recorded, explained, remembered version of what was actually said and what it means for you. That is the spine of everything below. Everyone else has the data or the channel. We can own the understanding.

## Two ways to reason, run together

We keep confusing ourselves because we mix two ways of reasoning. Both are valid, and I want to run them at the same time.

**Backwards from a vision.** Imagine the Ditto that should exist in a few years and reason back to what we build now. This keeps us coherent and stops us becoming a pile of features.

**Forwards from jobs to be done.** Watch how people actually struggle in healthcare today and solve one job, then the next, so Ditto solves more and more real problems over time. The care-management jobs people already do badly are concrete:

- booking and landing appointments
- finding their own data
- looking things up online
- making sense of literature
- updating their loved ones

This keeps us useful and grounded, and it keeps us shipping.

Over both sits one hard filter: **monetization.** What actually becomes a business is a real constraint, not an afterthought, and it excludes options no matter how nice the vision or how real the job. The uncomfortable truth is that almost nothing in this space monetizes on patient-pay. The money is B2B everywhere you look: hospitals, insurers, employers, pharma, providers. So the resolution I lean towards is **B2B2C: serve the patient, bill the institution.** We stay patient-first in the product and let an institution that benefits from a better-informed, better-coordinated patient pay for it.

## The six product end states

These are the futures we have been circling. I want them all on the table, then synthesized.

1. **Care Companion.** Ditto supports you along every step of your care journey. Core focus: understanding, making sense of what is happening, knowing what to expect. This is where we are today, and the base of the spine.

2. **Trusted Health Assistant.** Ditto helps prevent illness and get you recovered as well as possible. Core focus: agency, advice and nudges on the medical behaviour you can control. This is a dedicated end state, and when you combine end states it is also the top of the intelligence ladder, what the companion becomes when you keep adding intelligence.

3. **Patient-Owned Record.** You own and understand all your healthcare data in Ditto. Core focus: ingest everything and make it understandable and shareable. Data alone is low value and we would be fighting governments and EHRs, so I do not see this as a destination.

4. **Care Coordination.** Families manage the disease and arrange practical support inside Ditto. Core focus: tasks, agendas, keeping the core care group aligned. There is a real market here if you do it extremely well.

5. **Social Care Platform.** The place for shared understanding among loved ones and peers. Core focus: connection, not being alone, support gestures, updates, peers.

6. **The Front Door of European healthcare** (Nick's addition). The go-to digital solution that does the operational things at once: scheduling, planning appointments, getting a second opinion, finding your data, messaging health professionals. Think of the Doctolib-shaped operator, including prescriptions and the rest of the rails. It does not require personal intelligence, but it can link to it, and if you are the front door you also hold the data and the scheduling, which feeds everything above.

## The synthesis: two layers, plus leans

The mistake in my first version was listing these as five equal bets. They are not the same kind of thing. They stack into two layers.

**The intelligence layer is the spine, and it is our contrarian core.** It runs understanding (Care Companion) to advising to agency (Trusted Health Assistant), and it grows in two directions: up the intelligence ladder, and outward into the day-to-day and weekly needs between appointments where frequency and attachment actually live. The **Patient-Owned Record is not a goal here, it is a multiplier.** If we can integrate it, the assistant finally sees the full picture and every rung of the ladder gets better. So we chase the record as an enabler, not a destination.

**The operational layer is the front door.** Scheduling, prescriptions, messaging, data access. This is not intelligence, it is operations, and it is where Doctolib and the portals live. It stacks under or beside the spine: it brings reach and data, and being the front door is itself a defensible position. I think being honest that some of this is operational and some is intelligence is what was missing before. It makes the whole thing buildable instead of one vague tower.

**Coordination and social are leans, not the spine.** We take the parts of coordination and social that make the companion a more complete experience, we can experiment where there is a real market, but neither becomes the foundation.

One tension to name honestly. The rung where the money is, individualised advising, is also the rung where regulation bites hardest. Advising is the MDR and AI-Act device rung. The companies that survive there route around it by keeping a human or the care circle in the loop, rather than having the AI act alone. That is the line we have to respect as we climb.

## How we get there

The end states say almost nothing about how we actually move, and this is where I like Nick's framing most.

We make bigger bets in shorter cycles, and we learn fast. We cannot set the full course in advance, because we do not know exactly where B is, and we certainly do not know the best path from A to B. What we do have is a current, rough idea of roughly where B sits, and the job is to point ourselves that way, build, integrate, experiment, and update the target as the ground tells us more. Direction over route. That is also why the vision should be held as a heading, not a fixed destination, and why the jobs-to-be-done work matters: it is how we keep moving while the vision stays deliberately a little blurry.

This cuts both ways, and I want to be honest about it. Committing now does close some doors. If we go all in on data integrations and anticipating EHDS, we slow down on adding real intelligence to the data users already put into Ditto. That is a genuine trade-off, not a free choice.

## What we need to decide

This narrative is the input. The strategy session is where we choose. The questions:

0. **Why do we exist?** The mission above, up for debate.
1. **What does Ditto solve or improve?**
2. **Who are we building for?**
3. **What is our moat?**
4. **How do we monetize it?**

And the one tension to resolve, because it shapes all the others: **patient-first versus the fact that every payer is an institution.** My current answer is B2B2C, serve the patient and bill the institution, but I want us to land it together.
