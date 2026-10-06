"""Owner directive Oct 5 night: every tap-through story set ALSO runs as a
post on IG (feed carousel, 4:5 originals) and TikTok (photo carousel, 9:16
story9 versions), at the same standing time as its story slot.

Queues the Tue Oct 6 and Wed Oct 7 card lanes. Captions come from the
queued IG story posts ("Tap through" becomes "Swipe" for the feed/TikTok
copy). IG feed posts carry the pinned firstComment. TikTok has no metadata.
"""
import json, subprocess, time

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CH_IG = "6aabfaf0ea19ca0bde6965d6"
CH_TT = "6ab81da7ea19ca0bdef9436e"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
IG_COMMENT = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
              "Booking December now.")

# original 4:5 path for each story9 basename stem
ORIG = {
    "BB_Caro_": "big-business-rentals/daily-posts/week5/",
    "BB_Venue_": "big-business-rentals/venue/",
}

Q = """query($input: PostsInput!, $after: String){
  posts(input:$input, first: 50, after: $after){
    edges{ node{ id channelId text dueAt
      assets{ __typename ... on ImageAsset{ source } }
      metadata{ __typename ... on InstagramPostMetadata{ type } } } }
    pageInfo{ hasNextPage endCursor }
  }
}"""
MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
  ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""


def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": q, "variables": v})],
                       capture_output=True, text=True)
    return json.loads(r.stdout)


def orig_url(name):
    for stem, folder in ORIG.items():
        if name.startswith(stem):
            return RAW + folder + name
    return None


if __name__ == "__main__":
    inp = {"organizationId": ORG, "filter": {"status": ["scheduled"]},
           "sort": [{"field": "dueAt", "direction": "asc"}]}
    stories, after = [], None
    while True:
        d = gql(Q, {"input": inp, "after": after})
        p = d["data"]["posts"]
        for e in p["edges"]:
            n = e["node"]
            md = n.get("metadata") or {}
            if n["channelId"] == CH_IG and md.get("type") == "story" \
               and n["dueAt"][:10] in ("2026-10-06", "2026-10-07") \
               and n["assets"] and n["assets"][0]["__typename"] == "ImageAsset":
                stories.append(n)
        if not p["pageInfo"]["hasNextPage"]: break
        after = p["pageInfo"]["endCursor"]

    print(len(stories), "story sets to mirror")
    ok = fail = 0
    for n in stories:
        text = n["text"].replace("Tap through", "Swipe")
        names = [a["source"].rsplit("/", 1)[1] for a in n["assets"]]
        ig_assets = [{"image": {"url": orig_url(x)}} for x in names]
        tt_assets = [{"image": {"url": RAW + "big-business-rentals/story9/" + x}} for x in names]
        if any(a["image"]["url"] is None for a in ig_assets):
            print("SKIP no original for", names[0]); continue
        jobs = [
            {"channelId": CH_IG, "text": text, "mode": "customScheduled",
             "schedulingType": "automatic", "dueAt": n["dueAt"],
             "assets": ig_assets,
             "metadata": {"instagram": {"type": "post", "shouldShareToFeed": True,
                                        "firstComment": IG_COMMENT}}},
            {"channelId": CH_TT, "text": text, "mode": "customScheduled",
             "schedulingType": "automatic", "dueAt": n["dueAt"],
             "assets": tt_assets},
        ]
        for inp2 in jobs:
            d = gql(MUT, {"input": inp2})
            try:
                r = d["data"]["createPost"]
                ch = "IG" if inp2["channelId"] == CH_IG else "TT"
                if r["__typename"] == "PostActionSuccess":
                    ok += 1; print("OK  ", ch, n["dueAt"][:16], text.split("\n")[0][:40])
                else:
                    fail += 1; print("FAIL", ch, n["dueAt"][:16], r.get("message", "")[:140])
            except Exception:
                fail += 1; print("FAIL", json.dumps(d)[:140])
            time.sleep(3)
    print(f"done: {ok} created, {fail} failed")
