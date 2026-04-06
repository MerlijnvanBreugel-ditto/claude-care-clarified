# CC V2 — P1 Tracking Events (Sheet Format)

> Copy these rows into the [Care Circle tracking sheet](https://docs.google.com/spreadsheets/d/19st40l2ZYNNaF5TZ8MXZlssCjmiaJ7cLhYmT36k73ac/edit?gid=1641519238#gid=1641519238).
> Format matches existing sheet columns exactly.

## CSV — Ready to paste

```csv
Implementation Version,Implemented,Event Name,Legacy Name,KPI,Trigger,Event Definition,Property Type,Property Name,Property Definition,Data Type,Sample Values,Platform,Implemented?,Notes
,,,,,,,,,,,,,,
,,**DPMA-1966 — Social Engagement (Emoji Reactions)**,,,,,,,,,,,,
,,Care Circle - Reaction Given,,Reaction Rate,Follower taps emoji on a shared event,Follower adds a reaction to a shared care event,Event Property,emoji_id,Which emoji was used,String,"heart,hug,strength,thinking_of_you",,Must Have,
,,,,,,,,event_type,Type of event reacted to,String,"preparation,document,recording",, Must Have,
,,,,,,,,time_since_event_shared_hours,Hours since event was shared,Number,0-720,,Must Have,
,,,,,,,,care_circle_size,Total followers of the sender,Number,1-20,,Must Have,
,,Care Circle - Reaction Revoked,,Revocation Rate,Follower removes their reaction,Follower takes back a previously given reaction,Event Property,emoji_id,Which emoji was revoked,String,"heart,hug,strength,thinking_of_you",,Must Have,
,,,,,,,,time_since_reaction_given_seconds,Seconds between giving and revoking,Number,0-86400,,Must Have,
,,Care Circle - Event Details Opened of Following (EXTEND),,Reaction Rate (denominator),ALREADY TRACKED - add properties,Extend with reaction context for viewed-but-not-reacted rate,Event Property,has_reactions,Whether event has reactions at view time,Boolean,"true,false",,Must Have,Extend existing event
,,,,,,,,reaction_count,Number of reactions on this event,Number,0-20,,Must Have,Extend existing event
,,,,,,,,viewer_has_reacted,Whether this viewer already reacted,Boolean,"true,false",,Must Have,Extend existing event
,,,,,,,,,,,,,,
,,**DPMA-1964 — Enhanced Sharing Options**,,,,,,,,,,,,
,,Care Circle - Own Event Shared with Care Circle (EXTEND),,Share Personalization,ALREADY TRACKED - add properties,Extend with personal message and section properties,Event Property,has_personal_message,Whether a personal message was attached,Boolean,"true,false",,Must Have,Extend existing event
,,,,,,,,personal_message_length,Character count of the personal message,Number,0-500,,Must Have,
,,,,,,,,included_sections,Which summary sections were included,String[],"what_the_doctor_said,details,action_items",,Must Have,Format TBD with engineering
,,,,,,,,shared_section_count,Number of sections included in share,Number,1-6,,Must Have,
,,,,,,,,,,,,,,
,,**DPMA-1963 — Enhanced Follower User Profiles**,,,,,,,,,,,,
,,Profile - Editor Opened,,Profile Fill Rate,Patient opens profile editor,Patient opens the profile editing screen,Event Property,has_existing_bio,Whether bio already has content,Boolean,"true,false",,Must Have,
,,,,,,,,existing_question_count,Number of questions already added,Number,0-10,,Must Have,
,,,,,,,,is_first_edit,Whether this is the first time editing,Boolean,"true,false",,Must Have,
,,Profile - Bio Updated,,Profile Fill Rate,Patient saves bio content,Patient writes or edits their bio text,Event Property,bio_character_count,Length of bio in characters,Number,0-2000,,Must Have,
,,,,,,,,is_first_bio,Whether this is the first bio entry,Boolean,"true,false",,Must Have,
,,,,,,,,profile_question_count,Number of FAQ questions at time of bio save,Number,0-10,,Must Have,
,,Profile - Question Added,,Profile Depth,Patient adds a new FAQ question,Patient creates a new question on their profile,Event Property,question_number,Which question number (1st; 2nd; etc),Number,1-10,,Must Have,
,,,,,,,,answer_character_count,Length of the answer in characters,Number,0-2000,,Must Have,
,,,,,,,,total_questions_after,Total questions after adding this one,Number,1-10,,Must Have,
,,Profile - Visibility Changed,,Profile Visibility,Patient toggles profile public/private,Patient changes whether followers can see their profile,Event Property,new_visibility,New visibility state,String,"public,private",,Must Have,
,,,,,,,,previous_visibility,Previous visibility state,String,"public,private",,Must Have,
,,,,,,,,bio_character_count,Bio length at time of toggle,Number,0-2000,,Must Have,
,,,,,,,,question_count,Number of questions at time of toggle,Number,0-10,,Must Have,
,,Profile - Viewed,,Profile View Rate,Follower views a patient's profile page,Follower opens the profile of someone they follow,Event Property,viewer_role,Who is viewing,String,"follower,self",,Must Have,
,,,,,,,,bio_character_count,Bio length of the viewed profile,Number,0-2000,,Must Have,
,,,,,,,,question_count,Number of questions on viewed profile,Number,0-10,,Must Have,
,,,,,,,,is_profile_public,Whether profile is set to public,Boolean,"true,false",,Must Have,
,,,,,,,,is_first_view,Whether this is the first time viewing this profile,Boolean,"true,false",,Must Have,
,,,,,,,,,,,,,,
,,**DPMA-1903 — Improved Invitation Flow**,,,,,,,,,,,,
,,Care Circle - Follow Request Sent (EXTEND),,Invite Source,ALREADY TRACKED - add property,Extend with source screen property,Event Property,source,Where the invite was initiated from,String,"activation_panel,home,onboarding,care_circle_tab,deeplink",,Must Have,Extend existing event
,,Care Circle - Follow Request Accepted,,Accept Rate,ALREADY TRACKED,Already tracked with request_age_hours and follower_count_after,,,,,,,,Must Have,No changes needed — confirm existing properties are firing
```

## Summary by Epic

| Epic | P1 Events | New | Extend Existing |
|---|---|---|---|
| DPMA-1966 (Reactions) | Reaction Given, Reaction Revoked, Event Details Opened (extend) | 2 | 1 |
| DPMA-1964 (Sharing) | Own Event Shared (extend) | 0 | 1 |
| DPMA-1963 (Profiles) | Editor Opened, Bio Updated, Question Added, Visibility Changed, Viewed | 5 | 0 |
| DPMA-1903 (Invitations) | Follow Request Sent (extend), Follow Request Accepted (confirm) | 0 | 1 + 1 confirm |
| **Total** | **10 events** | **7 new** | **3 extend + 1 confirm** |
