"""List every scheduled YouTube post in Buffer and flag charter problems
(phone, URL, the word "free", more than 3 hashtags, health/awareness content)."""
import json, re, subprocess, sys

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
YT = "6ac2ff576a5c39ccb618d238"
Q = """query($input: PostsInput!, $after: String){ posts(input:$input, first:50, after:$after){
 edges{ node{ id text dueAt status assets{ source thumbnail }
   metadata{ __typename ... on YoutubePostMetadata{ title category { __typename } } } } }
 pageInfo{ hasNextPage endCursor } } }"""

def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": q, "variables": v})], capture_output=True, text=True)
    return json.loads(r.stdout)

rows, after = [], None
while True:
    d = gql(Q, {"input": {"organizationId": ORG, "filter": {"status": ["scheduled"], "channelIds": [YT]},
                          "sort": [{"field": "dueAt", "direction": "asc"}]}, "after": after})
    if "data" not in d or not d["data"]:
        print(json.dumps(d)[:800]); sys.exit(1)
    p = d["data"]["posts"]
    rows += [e["node"] for e in p["edges"]]
    if not p["pageInfo"]["hasNextPage"]: break
    after = p["pageInfo"]["endCursor"]
json.dump(rows, open(sys.argv[1] if len(sys.argv) > 1 else "yt_queue.json", "w"), indent=1)
for n in rows:
    t = n["text"]; md = n.get("metadata") or {}
    flags = [f for f, rx in [("phone", r"702-706"), ("url", r"\.com"), ("free", r"\bfree\b")] if re.search(rx, t, re.I)]
    tags = len(re.findall(r"#\w+", t))
    print(n["dueAt"], n["id"], "cat", "", "|", (md.get("title") or "")[:60], "|", flags, "tags", tags)
