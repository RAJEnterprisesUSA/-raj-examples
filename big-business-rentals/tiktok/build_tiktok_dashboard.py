"""TikTok performance dashboard (charter WEEKLY step 1): one row per post.

Pulls every SENT TikTok post that went out through Buffer and writes tiktok/dashboard.csv with
the charter's columns. Buffer reports views, average watch time, likes (Reactions), comments
and shares. Watched full %, 3-second hold, saves, new followers and profile views exist only
in TikTok Studio, so those columns stay blank here and get filled from the owner's Studio
screenshots. Posts the owner publishes natively in the app are not in Buffer at all; add
them to tiktok/native_posts.csv (same columns) and this script merges them in.
"""
import csv, json, pathlib, statistics, subprocess

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
TT = "6ab81da7ea19ca0bdef9436e"
HERE = pathlib.Path(__file__).parent
COLS = ["date", "pillar", "series_part", "ai_or_real", "length_s", "hook_text", "views",
        "avg_watch_s", "watched_full_pct", "hold_3s_pct", "likes", "comments", "shares",
        "saves", "new_followers", "profile_views", "notes"]

# caption-prefix -> (pillar, ai_or_real) for posts whose type the lane keywords cannot tell
KNOWN = [
    ("nobody sees this part", ("real moment", "real")),
    ("another drop off", ("real moment", "real")),
    ("small backyard party", ("real moment", "real")),
    ("cleaning every chair", ("real moment", "real")),
    ("every chair gets tested", ("real moment", "real")),
    ("if you have the event", ("owner post", "real")),
    ("las vegas patry rentals", ("owner post", "unclear")),
    ("so what do you bring to the table", ("owner AI sketch", "AI video")),
    ("rajenterprises", ("RAJ (retired)", "n/a")),
    ("no chat bot for your website", ("RAJ (retired)", "n/a")),
    ("quick question for the shop owners", ("RAJ (retired)", "n/a")),
    ("property managers", ("RAJ (retired)", "n/a")),
    ("are you a trades business owner", ("RAJ (retired)", "n/a")),
    ("it's saturday. your office is closed", ("RAJ (retired)", "n/a")),
    ("someone is searching for your business", ("RAJ (retired)", "n/a")),
    ("ramadan mubarak", ("personal", "n/a")),
]
LANE_KEYS = [
    ("PRICE IT (old lane)", "AI image", ("how much would you pay",)),
    ("Chronicles episode (old 21-26s)", "animation", ("ep. ", "chronicles", "intern", "derrick")),
    ("pink awareness (old lane)", "animated graphics", ("\U0001F380", "breast", "mammogram", "screening", "pink october")),
    ("trend remix (old lane)", "animation", ("costume walk", "face only", "robbed", "roadster", "black cat", "porch reveal")),
    ("gag reel (old lane)", "animation", ("\U0001F480", "\U0001F47B", "pumpkin", "skeleton", "fog", "broom", "candy", "pinata",
                                          "photo booth", "tablecloth", "dj", "mummy", "frankenstein", "zombie", "ghost", "conjure")),
    ("countdown card (old lane)", "graphic carousel", ("nights", "saturdays left", "3-0", "2-9", "2-8")),
    ("referral card (old lane)", "graphic carousel", ("$100", "referr", "word of mouth", "paid to be popular", "golden ticket",
                                                     "wanted: people", "now hiring", "receipt", "local plug", "text that pays", "easiest math", "planners. djs")),
    ("tip/business card (old lane)", "graphic carousel", ("swipe", "tip no", "party math", "playbook", "layouts", "forget to rent",
                                                         "stop guessing", "quote in minutes", "venue", "one room", "party day", "weekend", "psa:", "whole week", "4-weekend", "invited 50")),
]

def classify(text):
    t = text.lower()
    for key, val in KNOWN:
        if key in t:
            return val
    for pillar, kind, keys in LANE_KEYS:
        if any(k in t for k in keys):
            return pillar, kind
    return "unclassified", "unclear"

Q = """query($input: PostsInput!, $after: String){
  posts(input:$input, first: 50, after: $after){
    edges{ node{ id text sentAt metrics{ name value } } }
    pageInfo{ hasNextPage endCursor }
  }
}"""

def fetch_all():
    inp = {"organizationId": ORG, "filter": {"status": ["sent"], "channelIds": [TT]},
           "sort": [{"field": "dueAt", "direction": "desc"}]}
    out, after = [], None
    while True:
        body = json.dumps({"query": Q, "variables": {"input": inp, "after": after}})
        r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H",
                            "Content-Type: application/json", "-d", body],
                           capture_output=True, text=True)
        p = json.loads(r.stdout)["data"]["posts"]
        out += [e["node"] for e in p["edges"]]
        if not p["pageInfo"]["hasNextPage"]:
            return out
        after = p["pageInfo"]["endCursor"]

def main():
    rows = []
    for n in fetch_all():
        m = {x["name"]: x["value"] for x in (n.get("metrics") or [])}
        pillar, kind = classify(n["text"])
        rows.append({
            "date": (n.get("sentAt") or "")[:10], "pillar": pillar, "series_part": "",
            "ai_or_real": kind, "length_s": "", "hook_text": n["text"].split("\n")[0][:80],
            "views": int(m.get("Video Views", 0) or 0),
            "avg_watch_s": m.get("Avg. Watch Time (sec)", ""),
            "watched_full_pct": "", "hold_3s_pct": "",
            "likes": int(m.get("Reactions", 0) or 0), "comments": int(m.get("Comments", 0) or 0),
            "shares": int(m.get("Shares", 0) or 0), "saves": "", "new_followers": "",
            "profile_views": "", "notes": "via Buffer; pillar inferred from caption",
        })
    native = HERE/"native_posts.csv"
    if native.exists():
        with native.open() as f:
            rows += list(csv.DictReader(f))
    rows.sort(key=lambda r: r["date"], reverse=True)
    with (HERE/"dashboard.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader(); w.writerows(rows)
    views = [int(r["views"]) for r in rows if str(r["views"]).strip() != ""]
    print(f"{len(rows)} posts -> tiktok/dashboard.csv")
    print(f"median views {statistics.median(views):.0f}, posts with 5 views or fewer "
          f"{sum(v <= 5 for v in views) / len(views):.0%}, posts with 1+ comment "
          f"{sum(int(r['comments'] or 0) > 0 for r in rows)}")

if __name__ == "__main__":
    main()
