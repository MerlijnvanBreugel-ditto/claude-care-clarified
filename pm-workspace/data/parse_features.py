import re
import csv

INPUT = "/Users/merlijnvanbreugel/Documents/GitHub/Ditto/claude-care-clarified/pm-workspace/data/completed-features-jan2025-feb2026.md"
OUTPUT = "/Users/merlijnvanbreugel/Documents/GitHub/Ditto/claude-care-clarified/pm-workspace/data/completed-features-jan2025-feb2026.csv"

CLARITY_KW = ['ai', 'consultation', 'summary', 'summarize', 'summarization', 'summarisation',
              'ocr', 'document scanner', 'transcript', 'recording', 'understand', 'simplification',
              'feedback on ai', 'ai output', 'ai failure', 'ai improvement', 'event detail',
              'event view', 'ditto ai', 'gpt', 'claude', 'summary customization']
CONNECTION_KW = ['care network', 'care circle', 'share', 'sharing', 'invite', 'connect',
                 'doctor', 'data sharing', 'caregiver', 'follower', 'following', 'referral',
                 'flower', 'juvoly', 'partner']
CONVENIENCE_KW = ['onboarding', 'navigation', 'flow', 'ux', 'ui styling', 'activation',
                  'review', 'appointment', 'preparation', 'registration', 'funnel', 'upgrade',
                  'force update', 'reimagine', 'improve flow', 'videos', 'comms', 'explanatory',
                  'intro', 'profile setup', 'christmas', 'rebranding', 'scan', 'search',
                  'date selection', 'language', 'file naming', 'timeline view', 'lockscreen',
                  'copy', 'disclaimer', 'label', 'empty state', 'styling']
FOUNDATION_KW = ['infrastructure', 'security', 'tech debt', 'maintenance', 'bug', 'fix',
                 'backend', 'android', 'ios', 'release', 'pre-prod', 'ci/cd', 'observability',
                 'migration', 'performance', 'inbox', 'burning', 'cost', 'pilot', 'launch',
                 'post-launch', 'post lunch', 'on par', 'backward compatible', 'app-store',
                 'play store', 'deploy', 'terraform', 'auth0', 'azure', 'api', 'cleanup',
                 'loadtest', 'postgres', 'encrypt', 'permissions', 'uuid', 'remote config',
                 'adjust', 'analytics', 'mixpanel', 'grafana', 'microservice', 'privacy policy',
                 'crunch', 'infra']

def categorize(title, epic_title=""):
    combined = (title + " " + epic_title).lower()
    # Priority: Clarity > Connection > Convenience > Foundation
    for kw in CLARITY_KW:
        if kw in combined:
            return "Clarity"
    for kw in CONNECTION_KW:
        if kw in combined:
            return "Connection"
    for kw in CONVENIENCE_KW:
        if kw in combined:
            return "Convenience"
    for kw in FOUNDATION_KW:
        if kw in combined:
            return "Foundation"
    return "Convenience"

with open(INPUT, "r", encoding="utf-8") as f:
    lines = f.readlines()

rows = []
current_month = ""
current_epic_id = ""
current_epic_title = ""
in_epics_section = False
past_summary = False

# First pass: collect epics from the Completed Epics section
epic_pattern = re.compile(r'^\- \*\*(\w+-\d+)\*\* \| (\d{4}-\d{2}-\d{2}) \| \*\*(.+?)\*\*')

# Second pass: collect items from monthly sections
month_pattern = re.compile(r'^## (\w+ \d{4})$')
epic_header_pattern = re.compile(r'^### \[(\w+-\d+)\] (.+)$')
item_pattern = re.compile(r'^\- \*\*(\w+-\d+)\*\* \[(Epic|Story|Bug|Task)\] _(\d{4}-\d{2}-\d{2})_ — \*\*(.+?)\*\*')

for line in lines:
    line = line.rstrip()

    # Detect completed epics section
    if line.startswith("## Completed Epics"):
        in_epics_section = True
        continue

    # Detect monthly sections
    month_match = month_pattern.match(line)
    if month_match:
        in_epics_section = False
        past_summary = True
        current_month = month_match.group(1)
        continue

    # Parse epic entries from the Completed Epics list
    if in_epics_section:
        epic_match = epic_pattern.match(line)
        if epic_match:
            eid = epic_match.group(1)
            edate = epic_match.group(2)
            etitle = epic_match.group(3).strip()
            # Remove trailing link/description after " — "
            if " — " in etitle:
                etitle = etitle.split(" — ")[0].strip()
            rows.append({
                "id": eid,
                "date": edate,
                "title": etitle,
                "type": "Epic",
                "epic_id": "",
                "epic_title": "",
                "month": "",
                "pillar": categorize(etitle)
            })
        continue

    if not past_summary:
        continue

    # Parse epic sub-headers in monthly sections
    epic_header_match = epic_header_pattern.match(line)
    if epic_header_match:
        current_epic_id = epic_header_match.group(1)
        current_epic_title = epic_header_match.group(2).strip()
        continue

    # Parse individual items
    item_match = item_pattern.match(line)
    if item_match:
        item_id = item_match.group(1)
        item_type = item_match.group(2)
        item_date = item_match.group(3)
        item_title = item_match.group(4).strip()
        # Clean title: remove trailing description after **:
        if item_title.endswith("**"):
            item_title = item_title[:-2].strip()
        # Remove trailing colon-description
        title_clean = item_title.split("**")[0].strip().rstrip(":")

        rows.append({
            "id": item_id,
            "date": item_date,
            "title": title_clean,
            "type": item_type,
            "epic_id": current_epic_id,
            "epic_title": current_epic_title,
            "month": current_month,
            "pillar": categorize(title_clean, current_epic_title)
        })

# Fix epic months by date
import datetime
month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
               7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
for row in rows:
    if not row["month"] and row["date"]:
        d = datetime.datetime.strptime(row["date"], "%Y-%m-%d")
        row["month"] = f"{month_names[d.month]} {d.year}"

# Sort by date
rows.sort(key=lambda r: r["date"])

# Write CSV
with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "date", "title", "type", "epic_id", "epic_title", "month", "pillar"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Written {len(rows)} rows to CSV")

# Print pillar distribution
from collections import Counter
pillar_counts = Counter(r["pillar"] for r in rows)
type_counts = Counter(r["type"] for r in rows)
print(f"\nBy pillar: {dict(pillar_counts)}")
print(f"By type: {dict(type_counts)}")
