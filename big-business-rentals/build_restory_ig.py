"""Re-point every scheduled IG STORY post at the 9:16 padded images.

IG zoom-crops non-9:16 story images, so story-lane posts must use the
story9/ padded versions (build_story_pad.py). This queries scheduled IG
posts of type story and rewrites each image asset URL to
.../big-business-rentals/story9/<basename>, keeping text and metadata.
Idempotent: posts already pointing at /story9/ are skipped.
Run after the Buffer rate limit clears; paces edits 3s apart.
"""
import json, pathlib, subprocess, time

PADDED = {p.name for p in pathlib.Path(__file__).resolve().parent.joinpath("story9").glob("*.png")}

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CH_IG = "6aabfaf0ea19ca0bde6965d6"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"

Q = """query($input: PostsInput!, $after: String){
  posts(input:$input, first: 50, after: $after){
    edges{ node{ id channelId text dueAt
      assets{ __typename ... on ImageAsset{ source } ... on VideoAsset{ source } }
      metadata{ __typename
        ... on InstagramPostMetadata{ type shouldShareToFeed firstComment } }
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
            if "data" in d and d["data"]: break
            print("fetch rate-limited, backing off", wait, "s")
            time.sleep(wait)
            d = gql(Q, {"input": inp, "after": after})
        if "data" not in d or not d["data"]:
            raise SystemExit("Buffer still rate-limited; re-run later.")
        p = d["data"]["posts"]
        out += [e["node"] for e in p["edges"]]
        if not p["pageInfo"]["hasNextPage"]:
            return out
        after = p["pageInfo"]["endCursor"]


if __name__ == "__main__":
    posts = fetch_scheduled()
    ok = fail = skip = 0
    for n in posts:
        md = n.get("metadata") or {}
        if n["channelId"] != CH_IG or md.get("__typename") != "InstagramPostMetadata" \
           or md.get("type") != "story":
            skip += 1; continue
        assets, changed, video = [], False, False
        for a in n["assets"] or []:
            if a["__typename"] != "ImageAsset":
                video = True; break
            src = a["source"]
            name = src.rsplit("/", 1)[1]
            # only remap when the padded file actually exists (and is pushed)
            if "/story9/" not in src and name in PADDED:
                src = RAW + "big-business-rentals/story9/" + name
                changed = True
            assets.append({"image": {"url": src}})
        if video or not changed:
            skip += 1; continue
        meta_ig = {"type": "story", "shouldShareToFeed": False}
        if md.get("firstComment"):
            meta_ig["firstComment"] = md["firstComment"]
        inp = {"id": n["id"], "text": n["text"], "assets": assets,
               "metadata": {"instagram": meta_ig}}
        d = gql(MUT, {"input": inp})
        try:
            r = d["data"]["editPost"]
            if r["__typename"] == "PostActionSuccess":
                ok += 1; print("OK  ", n["id"], n["dueAt"][:16], n["text"][:40])
            else:
                fail += 1; print("FAIL", n["id"], r.get("message", "")[:140])
        except Exception:
            fail += 1; print("FAIL", n["id"], json.dumps(d)[:140])
        time.sleep(3)
    print(f"done: {ok} re-pointed, {skip} skipped, {fail} failed")
