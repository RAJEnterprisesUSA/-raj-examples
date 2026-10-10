"""Pinned first-comment backfill + standing tool.

Attaches the owner's pinned follow comment to every SCHEDULED Facebook and
Instagram FEED post (type post or reel) via Buffer's metadata.firstComment.
Stories are skipped (stories cannot carry comments). TikTok and YouTube have
no firstComment field. Safe to re-run: posts that already carry the comment
are skipped.

Buffer publishes the first comment automatically when the post goes live;
PINNING it is still manual (open the post, three dots on the comment, Pin).
"""
import json, subprocess, time

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CH_FB = "6aabfb63ea19ca0bde696947"
CH_IG = "6aabfaf0ea19ca0bde6965d6"

FB_COMMENT = ("If you're planning anything this season, follow the page. "
              "We post real setups, open dates, and what's available before it books up.\n"
              "facebook.com/profile.php?id=61589138907701")
IG_COMMENT = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
              "Booking December now.")

Q = """query($input: PostsInput!, $after: String){
  posts(input:$input, first: 50, after: $after){
    edges{ node{ id channelId text dueAt
      assets{ __typename
        ... on ImageAsset{ source thumbnail }
        ... on VideoAsset{ source thumbnail }
      }
      metadata{ __typename
        ... on InstagramPostMetadata{ type shouldShareToFeed firstComment }
        ... on FacebookPostMetadata{ type firstComment }
      }
    } }
    pageInfo{ hasNextPage endCursor }
  }
}"""

MUT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename
  ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""


def gql(query, variables):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": query, "variables": variables})],
                       capture_output=True, text=True)
    return json.loads(r.stdout)


def fetch_scheduled():
    out, after = [], None
    inp = {"organizationId": ORG, "filter": {"status": ["scheduled"]},
           "sort": [{"field": "dueAt", "direction": "asc"}]}
    while True:
        d = gql(Q, {"input": inp, "after": after})
        for wait in (120, 300, 600):
            if "data" in d and d["data"]:
                break
            print("fetch rate-limited, backing off", wait, "s:", json.dumps(d)[:120])
            time.sleep(wait)
            d = gql(Q, {"input": inp, "after": after})
        if "data" not in d or not d["data"]:
            raise SystemExit("Buffer still rate-limited; re-run later. " + json.dumps(d)[:200])
        p = d["data"]["posts"]
        out += [e["node"] for e in p["edges"]]
        if not p["pageInfo"]["hasNextPage"]:
            return out
        after = p["pageInfo"]["endCursor"]


def assets_input(assets):
    a = []
    for x in assets or []:
        if x["__typename"] == "ImageAsset":
            a.append({"image": {"url": x["source"]}})
        elif x["__typename"] == "VideoAsset":
            # editPost rejects thumbnailUrl ("not supported"); send url only
            a.append({"video": {"url": x["source"]}})
    return a


if __name__ == "__main__":
    posts = fetch_scheduled()
    print(len(posts), "scheduled posts")
    ok = fail = skip = 0
    for n in posts:
        md = n.get("metadata") or {}
        tn = md.get("__typename", "")
        ch = n["channelId"]
        if ch == CH_IG and tn == "InstagramPostMetadata" and md.get("type") in ("post", "reel"):
            if md.get("firstComment"):
                skip += 1; continue
            meta = {"instagram": {"type": md["type"],
                                  "shouldShareToFeed": bool(md.get("shouldShareToFeed", True)),
                                  "firstComment": IG_COMMENT}}
        elif ch == CH_FB and tn == "FacebookPostMetadata" and md.get("type") in ("post", "reel"):
            if md.get("firstComment"):
                skip += 1; continue
            meta = {"facebook": {"type": md["type"], "firstComment": FB_COMMENT}}
        else:
            skip += 1; continue
        inp = {"id": n["id"], "text": n["text"],
               "assets": assets_input(n["assets"]), "metadata": meta}
        d = gql(MUT, {"input": inp})
        if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
            print("rate limited, backing off 90s...")
            time.sleep(90)
            d = gql(MUT, {"input": inp})
        time.sleep(3)
        try:
            r = d["data"]["editPost"]
            if r["__typename"] == "PostActionSuccess":
                ok += 1; print("OK  ", n["id"], md["type"], n["dueAt"][:16])
            else:
                fail += 1; print("FAIL", n["id"], r.get("message", "")[:160])
        except Exception:
            fail += 1; print("FAIL", n["id"], json.dumps(d)[:160])
    print(f"done: {ok} commented, {skip} skipped (stories/other/already set), {fail} failed")
