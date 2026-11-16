"""Weekly report No. 4 (Mon Nov 9 to Sun Nov 15) helper: pulls sent posts from Buffer and prints per-post views + medians by format."""
import json, datetime, zoneinfo, statistics
from queue_everywhere_oct24 import gql
Q = """query($input: PostsInput!, $after: String){ posts(input:$input, first: 50, after: $after){
  edges{ node{ id channelId text status sentAt dueAt metrics{ name value } } } pageInfo{ hasNextPage endCursor } } }"""
CH={'6aabfb63ea19ca0bde696947':'FB','6aabfaf0ea19ca0bde6965d6':'IG','6ab81da7ea19ca0bdef9436e':'TT','6ac2ff576a5c39ccb618d238':'YT'}
LA=zoneinfo.ZoneInfo("America/Los_Angeles"); lo=datetime.datetime(2026,11,9,tzinfo=LA); hi=datetime.datetime(2026,11,16,tzinfo=LA)
rows=[]; after=None
for _ in range(6):
    d=gql(Q,{"input":{"organizationId":"6a8284ed71811e26a813241c","filter":{"status":["sent"]},"sort":[{"field":"dueAt","direction":"desc"}]},"after":after})
    p=d["data"]["posts"]
    for e in p["edges"]:
        n=e["node"]; dt=datetime.datetime.fromisoformat((n["sentAt"] or n["dueAt"]).replace("Z","+00:00")).astimezone(LA)
        if lo<=dt<hi: rows.append((dt,n))
    if not p["pageInfo"]["hasNextPage"] or (rows and min(r[0] for r in rows)<lo): break
    after=p["pageInfo"]["endCursor"]
def fmt(t):
    t=(t or "").lower()
    if "chronicles ep." in t: return "episode"
    for k in ["spy","1 in 10 billion","party physics","majority","gavel","ai plan","answer in one word","one table","turkey"]:
        if k in t: return "remix"
    return "promo"
def views(n):
    m={x["name"]:x["value"] for x in (n["metrics"] or [])}
    return m.get("Views") or m.get("Video Views") or m.get("Impressions") or 0
out=[]
for dt,n in sorted(rows,key=lambda r:r[0]):
    out.append({"day":dt.strftime("%a %H:%M"),"ch":CH[n["channelId"]],"fmt":fmt(n["text"]),"views":views(n),"text":(n["text"] or "")[:60].replace("\n"," ")})
json.dump(out,open("reports/week4_posts.json","w"),indent=1)
for ch in ["YT","IG","FB","TT"]:
    for f in ["episode","remix","promo"]:
        v=[o["views"] for o in out if o["ch"]==ch and o["fmt"]==f]
        if v: print(ch,f,"n=",len(v),"median",statistics.median(v),"max",max(v))
print("--- top 10")
for o in sorted(out,key=lambda o:-o["views"])[:10]: print(o["views"],o["ch"],o["day"],o["fmt"],o["text"])
