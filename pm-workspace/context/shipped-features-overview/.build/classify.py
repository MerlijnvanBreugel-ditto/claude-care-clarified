import re
# Generalizable taxonomy (broad buckets, ordered). Returns investment type.
def investment_type(title, labels):
    t=title.lower(); L=set(labels); j=" ".join(labels).lower()
    bug_sig = ("bug" in [x.lower() for x in L]) or t.startswith("fix") or t.startswith("[android]") or t.startswith("[ios]") or any(k in t for k in
        ["doesn't","does nothing","not working","not loading","broken","stalls","fails to",
         "incorrect","wrong category","cursor jumps","rotates 90","dead end","doesn't open","appears only","not visible","doesn't work","fix copy","fix push","fix grammar","fix alignment","fix ui"])
    if "agent:" in j or any(k in t for k in ["agentic","daily brief","daily briefing","outreach automation","b2b outreach","15 fte","15ftes","person research","pipeline presentation","wow workshop","agent —","agent ("]):
        return "AI agents"
    if any(k in t for k in ["privacy","consent","gdpr","deletion","delete user","policy"]): return "Compliance/privacy"
    if bug_sig: return "Bug fix"
    if t.startswith(("research","discovery","investigate","explore","analyze","analyse","map ")) or "research" in L or any(k in t for k in ["[spike]","lyssna","survey","keyword list","correlation","touchpoints","ad-hoc dev environment"]):
        return "Research/discovery"
    if "ai" in [x.lower() for x in L] or any(k in t for k in ["evals","guardrail","explainer","transcription","answer suggestion","smart answer"]): return "AI quality"
    if any(k in t for k in ["customer.io","cio","cio:","welcome series","broadcast","campaign","appointment prep flow","profile completion"]): return "Lifecycle/CRM"
    if any(k in t for k in ["mixpanel","analytics","tracking","track \"","adjust","dashboard","smiirl","porygon","porgon","mau","app store connect api"]): return "Analytics/tracking"
    if any(k in t for k in ["experiment","proposal","triage","risce","runbook","okr","update krs","ship at 80","post-ship","verdict","evaluation","way of working","feature flag","push to 100","rollout","a/b","pilot"]): return "Process/tooling"
    if any(k in t for k in ["auth0","supabase","terraform","staging","domain map","16 kb","16kb","page size","repo","architecture","window based fallback","event pipeline","endpoint","provisioning","environment","skills"]): return "Infra/platform"
    if any(k in t for k in ["l.e.g.o","lego","glass","typography","shadow","dialog","colors","color","toast","assets export","compressed","optimise assets","gradient"]): return "Design system"
    if any(k in t for k in ["asset","video","testimonial","translation","slideshow","image","miniwebsite","handwritten cards","app store images"]): return "Content/creative"
    if any(k in t for k in ["reach out to hospital","company a","patrick collison","walk tobias"]): return "B2B/partner ops"
    if any(k in t for k in ["onboarding wouter","onboarding jasper","reactive google","meeting rhythm","schedule thursday","prep ","prepare ","walkthrough","connect linear","ownership over","[iman]","[wouter]","[niek]","workshop:"]): return "Team/internal ops"
    if "feature" in [x.lower() for x in L] or any(k in t for k in ["[implement","[implementation]","editable summaries","intent question","persona + intent","discover tab","ftue","activation flow","calendar sync","calendar pull","follow-up appoint","skip button","aha moment","geofenc","wearable","multi-profile","storefront","region-aware"]):
        return "New feature"
    if "improvement" in [x.lower() for x in L] or any(k in t for k in ["redesign","rework","enhance","highlight","adjust","improve","clear all","keep screen on"]): return "Improvement"
    if "design-polish" in [x.lower() for x in L]: return "Design polish"
    if "maintenance" in [x.lower() for x in L]: return "Maintenance"
    if any(k in t for k in ["release","check even in","make linear release"]): return "Release ops"
    return "Team/internal ops"

# Pillar keyword fallback (for no-project)
def pillar_kw(title, labels):
    t=title.lower(); L=[x.lower() for x in labels]
    if any(k in t for k in ["summary","summaries","evals","guardrail","transcription","explainer","notes editor","question library","questions library","answer","smart answer"]) or "ai" in L:
        return "Clarity"
    if any(k in t for k in ["care circle","loved one","follower","follow-back","follow request","invite","invitation","sharing","shared with you","reaction","carepath","multi-profile","managed account"]):
        return "Connection"
    if any(k in t for k in ["privacy","consent","gdpr","deletion","delete user","auth0","supabase","terraform","staging","security","16 kb","16kb","domain map","repo","l.e.g.o","lego","glass","typography","shadow","dialog","toast","color","analytics","mixpanel","tracking","adjust","triage","proposal","risce","experiment","a/b","runbook","okr","kr","release","app store","linear","github","brand lead","onboarding wouter","onboarding jasper","skills","workshop","agent","architecture","pipeline","endpoint","fallback","provisioning","environment","meeting","schedule","ownership","gradient","spike","hospital","company a","collison"]):
        return "Fundamentals"
    if any(k in t for k in ["calendar","activation","onboarding","intent","appointment","ftue","customer.io","cio","welcome series","discover","notification","reminder","recording","smiirl","geofenc","wearable","storefront","region","localization","uk app","uk launch","pregnancy","aha"]):
        return "Convenience"
    return "Fundamentals"

# OKR keyword fallback -> (primary, link_source). "—" = no direct KR (BAU/foundational)
def okr_kw(title, labels, pillar):
    t=title.lower(); j=" ".join(labels).lower()
    if "agent:" in j or any(k in t for k in ["agentic","daily brief","outreach automation","b2b outreach","15 fte","15ftes","person research"]):
        return "O1-KR2","Inferred"
    if any(k in t for k in ["experiment","proposal","triage","risce","ship at 80","post-ship","verdict","evaluation","way of working","runbook","pilot","feature flag","push to 100","update krs"]):
        return "O1-KR4","Inferred"
    if any(k in t for k in ["hospital","rotterdam","company a","partner","collison","hcp"]):
        return "O2-KR1","Inferred"
    if any(k in t for k in ["uk ","uk app","uk launch","localization","region","language"]):
        return "O1-KR3","Inferred"
    if pillar=="Connection": return "O2-KR3","Inferred"
    if pillar=="Convenience": return "O2-KR2","Inferred"
    if pillar=="Clarity": return "O2-KR4","Inferred"
    return "—","None (BAU/foundational)"
