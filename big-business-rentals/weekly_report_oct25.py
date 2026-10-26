"""Week of Oct 19-25 report under the four platform charters. Pulls every SENT post from
Buffer with metrics and saves them to reports/week3_posts.json for analysis."""
import json, subprocess, pathlib
API="https://api.buffer.com"; ORG="6a8284ed71811e26a813241c"
NAMES={"6aabfb63ea19ca0bde696947":"fb","6aabfaf0ea19ca0bde6965d6":"ig","6ab81da7ea19ca0bdef9436e":"tt","6ac2ff576a5c39ccb618d238":"yt"}
Q="""query($input: PostsInput!, $after: String){ posts(input:$input, first:50, after:$after){
 edges{ node{ id channelId text sentAt dueAt metricsUpdatedAt metrics{ name value unit } assets{ source } } }
 pageInfo{ hasNextPage endCursor } } }"""
rows=[]; after=None
while True:
    v={"input":{"organizationId":ORG,"filter":{"status":["sent"]},"sort":[{"field":"dueAt","direction":"desc"}]},"after":after}
    d=json.loads(subprocess.run(["curl","-sS","--max-time","90",API,"-H","Content-Type: application/json","-d",json.dumps({"query":Q,"variables":v})],capture_output=True,text=True).stdout)
    p=d["data"]["posts"]; batch=[e["node"] for e in p["edges"]]
    rows+=batch
    if not p["pageInfo"]["hasNextPage"] or batch[-1]["dueAt"]<"2026-10-12": break
    after=p["pageInfo"]["endCursor"]
for r in rows: r["ch"]=NAMES.get(r["channelId"],"?")
out=pathlib.Path(__file__).parent/"reports"; out.mkdir(exist_ok=True)
json.dump(rows,open(out/"week3_posts.json","w"),indent=1)
print(len(rows),"posts; metric names by channel:")
seen={}
for r in rows:
    for m in r["metrics"] or []: seen.setdefault(r["ch"],set()).add(m["name"])
for k,v in seen.items(): print(k,sorted(v))
