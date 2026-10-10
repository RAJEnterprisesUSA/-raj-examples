"""Swap pinned first comments to the cross-linked texts (owner, Oct 9).

FB comments now link to Instagram; IG comments now link to Facebook.
Rewrites firstComment on every still-scheduled FB/IG feed post (post or
reel). Stories and posts without a comment are skipped. Idempotent.
"""
import json, subprocess, time

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CH_FB = "6aabfb63ea19ca0bde696947"
CH_IG = "6aabfaf0ea19ca0bde6965d6"

FC_FB = ("If you're planning anything this season, follow us on Instagram too. "
         "Real setups, open dates, and what's available before it books up.\n"
         "instagram.com/bigbusiness_rentals_events")
FC_IG = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
         "Booking December now. We are on Facebook too: "
         "facebook.com/profile.php?id=61589138907701")

Q = """query($input: PostsInput!, $after: String){
  posts(input:$input, first: 50, after: $after){
    edges{ node{ id channelId text dueAt
      assets{ __typename ... on ImageAsset{ source } ... on VideoAsset{ source } }
      metadata{ __typename
        ... on InstagramPostMetadata{ type shouldShareToFeed firstComment }
        ... on FacebookPostMetadata{ type firstComment } } } }
    pageInfo{ hasNextPage endCursor }
  }
}"""
MUT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename
  ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""


def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": q, "variables": v})],
                       capture_output=True, text=True)
    return json.loads(r.stdout)


def assets_input(assets):
    out = []
    for a in assets or []:
        if a["__typename"] == "ImageAsset":
            out.append({"image": {"url": a["source"]}})
        elif a["__typename"] == "VideoAsset":
            out.append({"video": {"url": a["source"]}})  # no thumbnailUrl on edits
    return out


if __name__ == "__main__":
    inp = {"organizationId": ORG, "filter": {"status": ["scheduled"]},
           "sort": [{"field": "dueAt", "direction": "asc"}]}
    posts, after = [], None
    while True:
        d = gql(Q, {"input": inp, "after": after})
        p = d["data"]["posts"]
        posts += [e["node"] for e in p["edges"]]
        if not p["pageInfo"]["hasNextPage"]: break
        after = p["pageInfo"]["endCursor"]

    ok = fail = skip = 0
    for n in posts:
        md = n.get("metadata") or {}
        tn = md.get("__typename", "")
        if n["channelId"] == CH_IG and tn == "InstagramPostMetadata" \
           and md.get("type") in ("post", "reel") and md.get("firstComment"):
            if md["firstComment"] == FC_IG: skip += 1; continue
            meta = {"instagram": {"type": md["type"],
                                  "shouldShareToFeed": bool(md.get("shouldShareToFeed", True)),
                                  "firstComment": FC_IG}}
        elif n["channelId"] == CH_FB and tn == "FacebookPostMetadata" \
             and md.get("type") in ("post", "reel") and md.get("firstComment"):
            if md["firstComment"] == FC_FB: skip += 1; continue
            meta = {"facebook": {"type": md["type"], "firstComment": FC_FB}}
        else:
            skip += 1; continue
        inp2 = {"id": n["id"], "text": n["text"],
                "assets": assets_input(n["assets"]), "metadata": meta}
        d = gql(MUT, {"input": inp2})
        try:
            r = d["data"]["editPost"]
            if r["__typename"] == "PostActionSuccess":
                ok += 1; print("OK  ", n["id"], n["dueAt"][:16])
            else:
                fail += 1; print("FAIL", n["id"], r.get("message", "")[:140])
        except Exception:
            fail += 1; print("FAIL", n["id"], json.dumps(d)[:140])
        time.sleep(3)
    print(f"done: {ok} swapped, {skip} skipped, {fail} failed")
