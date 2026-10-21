"""Owner-approved Instagram queue cleanup (Oct 20 night, "Keep episodes, delete rest"):
rewrite the 5 Chronicles episode captions to the Instagram charter (one line with Las Vegas and
party keywords, max 5 hashtags, no phone, link, "free" or bait; pinned comment = follow prompt
only), then delete the 26 photo posts and 4 trend Reels. The 4 pink Stories stay."""
import json, subprocess, sys, time

API = "https://api.buffer.com"
PIN = "Follow so you never miss the next Big Business Chronicles episode."
EDIT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename
 ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""
DEL = """mutation($input: DeletePostInput!){ deletePost(input:$input){ __typename } }"""
CAPS = {
    "The intern won without touching a knife.":
      "The Big Business Chronicles EP. 29: Halloween party prep in Las Vegas means a pumpkin carve, and the intern wins without touching a knife. 🎃\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #pumpkincarving #partyrentals",
    "The chair got invited before you did.":
      "The Big Business Chronicles EP. 30: the Halloween party invitations went out, and somehow the cheap chair got one. 🎃\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #partyplanning #comedy",
    "The room was perfect for exactly two seconds.":
      "The Big Business Chronicles EP. 31: the Las Vegas Halloween party dry run was perfect for exactly two seconds. 🎃\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #partysetup #comedy",
    "He ordered party supplies. Every box was a chair.":
      "The Big Business Chronicles EP. 32: he ordered the Halloween party supplies, and every single box was a chair. 📦\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #partysupplies #comedy",
    "Every bulb worked. Then the cat found the outlet.":
      "The Big Business Chronicles EP. 33: every party light worked on the first try, then the cat found the outlet. 💡\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #partylights #comedy",
}

def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H",
                        "Content-Type: application/json", "-d", json.dumps({"query": q, "variables": v})],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
        time.sleep(90); return gql(q, v)
    return d

def match(text):
    for k in CAPS:
        if text.startswith(k):
            return k
    return None

if __name__ == "__main__":
    rows = json.load(open(sys.argv[1]))
    only_first = len(sys.argv) > 2 and sys.argv[2] == "first"
    edited = deleted = fail = 0
    for n in rows:
        md = n.get("metadata") or {}
        k = match(n["text"])
        if md.get("type") == "reel" and k:
            if only_first and not k.startswith("The intern"):
                continue
            inp = {"id": n["id"], "text": CAPS[k],
                   "assets": [{"video": {"url": a["source"]}} for a in n["assets"]],
                   "metadata": {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": PIN}}}
            d = gql(EDIT, {"input": inp})
            ok = ((d.get("data") or {}).get("editPost") or {}).get("__typename") == "PostActionSuccess"
            edited += ok; fail += (not ok)
            print("EDIT" if ok else "FAIL", n["id"], k[:40], "" if ok else json.dumps(d)[:200])
        elif not only_first and md.get("type") != "story":
            d = gql(DEL, {"input": {"id": n["id"]}})
            ok = ((d.get("data") or {}).get("deletePost") or {}).get("__typename") == "DeletePostSuccess"
            deleted += ok; fail += (not ok)
            if not ok: print("FAIL delete", n["id"], json.dumps(d)[:200])
        time.sleep(3)
    print(f"edited {edited}, deleted {deleted}, failed {fail}")
