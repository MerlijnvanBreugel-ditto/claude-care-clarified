import json
comp = json.load(open('prod_completed.json'))['issues']
np = [i for i in comp if not i.get('project')]
print("NO-PROJECT completed issues:", len(np))
for i in sorted(np, key=lambda x: x.get('completedAt','')):
    labs = ",".join(i.get('labels',[]))
    print(f"{i['id']:9} | {i.get('completedAt','')[:10]} | {labs[:38]:38} | {i['title'][:70]}")
