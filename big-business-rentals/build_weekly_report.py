"""Weekly Buffer performance report.

Run every Sunday evening (or on demand). Pulls every SENT post with metrics,
groups by channel and content lane (inferred from the caption's first line),
and prints the winners and losers so the next week's content follows the data.
Metrics arrive from Buffer hours after a post goes live; a post with no
metrics yet shows as pending.
"""
import json, subprocess, datetime, collections

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CHANNEL_NAMES = {
    "6aabfb63ea19ca0bde696947": "facebook",
    "6aabfaf0ea19ca0bde6965d6": "instagram",
    "6ab81da7ea19ca0bdef9436e": "tiktok",
    "6ac2ff576a5c39ccb618d238": "youtube",
}

LANES = [
    ("tip",       ("ice do you", "drinks does", "plans for trash", "party math")),
    ("business",  ("already handled", "hired a team", "party weekend")),
    ("venue",     ("deserves a home", "plan b", "one price")),
    ("referral",  ("$100", "word of mouth", "paid to be popular")),
    ("countdown", ("nights till halloween", "lands on a saturday", "nights left")),
    ("gag",       ("pumpkin", "eight legs", "party candy")),
    ("pink",      ("family history", "99%", "1 in 100", "pink october")),
    ("episode",   ("ep. 1", "chronicles", "intern", "save $5", "best chair")),
]

def lane_of(text):
    t = text.lower()
    for lane, keys in LANES:
        if any(k in t for k in keys):
            return lane
    return "other"

Q = """query($input: PostsInput!){
  posts(input:$input){
    edges{ node{ id channelId text status sentAt dueAt metricsUpdatedAt
      metrics{ name value unit }
      metadata{ __typename } } }
    pageInfo{ hasNextPage endCursor }
  }
}"""

def fetch(after=None):
    # PostsInput has no cursor arg; posts(...) returns one page sorted by dueAt.
    inp = {"organizationId": ORG, "filter": {"status": ["sent"]},
           "sort": [{"field": "dueAt", "direction": "desc"}]}
    body = json.dumps({"query": Q, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

cutoff = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat()
rows = []
after = None
for _ in range(1):
    d = fetch()
    data = d.get("data", {}).get("posts")
    if not data:
        print("query failed:", json.dumps(d)[:300]); break
    for e in data["edges"]:
        n = e["node"]
        if (n.get("sentAt") or "") < cutoff: continue
        m = {x["name"]: x["value"] for x in (n.get("metrics") or [])}
        rows.append({
            "channel": CHANNEL_NAMES.get(n["channelId"], n["channelId"][:6]),
            "lane": lane_of(n["text"]),
            "first_line": n["text"].split("\n")[0][:60],
            "sentAt": n.get("sentAt"),
            "metrics": m,
        })
    pi = data["pageInfo"]
    if not pi["hasNextPage"]: break
    after = pi["endCursor"]

if not rows:
    print("No sent posts with data in the last 7 days yet.")
else:
    print(f"{len(rows)} sent posts in the last 7 days\n")
    # per-lane totals for the metrics that matter most
    KEY = ("impressions", "reach", "likes", "comments", "shares", "saves",
           "views", "plays", "engagement", "engagement_rate")
    lanes = collections.defaultdict(lambda: collections.defaultdict(float))
    counts = collections.Counter()
    for r in rows:
        counts[(r["lane"], r["channel"])] += 1
        for k, v in r["metrics"].items():
            if any(key in k.lower() for key in KEY):
                lanes[(r["lane"], r["channel"])][k] += v or 0
    for (lane, ch), met in sorted(lanes.items()):
        n = counts[(lane, ch)]
        mets = " ".join(f"{k}={v:.0f}" for k, v in sorted(met.items()))
        print(f"{lane:10s} {ch:10s} n={n:2d}  {mets}")
    pending = [r for r in rows if not r["metrics"]]
    if pending:
        print(f"\n{len(pending)} posts have no metrics yet (Buffer refreshes with a lag).")
    # top 5 individual posts by best available reach-ish metric
    def score(r):
        m = r["metrics"]
        for k in ("impressions", "reach", "views", "plays"):
            for name, v in m.items():
                if k in name.lower(): return v or 0
        return 0
    top = sorted(rows, key=score, reverse=True)[:5]
    print("\nTop posts:")
    for r in top:
        print(f"  [{r['channel']}] {score(r):.0f}  {r['first_line']}")
