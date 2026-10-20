"""Queue owner-approved TikTok week 1 posts (approved Oct 20: "ok queue the rest of the weeks
tiktok post."). TikTok channel only, 1pm Pacific, one post per day, no AI toggle (owner rule),
captions per the charter: one line plus hashtags, no phone, prices or sales lines."""
import json, subprocess, time

API = "https://api.buffer.com"
TT = "6ab81da7ea19ca0bdef9436e"
RAW = ("https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/"
       "claude/photo-to-logo-editing-krxiu5/big-business-rentals/tiktok/")
MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
 ... on PostActionSuccess { post { id dueAt } } ... on MutationError { message } } }"""

POSTS = [
    ("2026-10-21T13:00:00-07:00", "TT_Chronicles_HalloweenArc_Pt1_CheapChair.mp4",
     "Who in your family always ends up on the worst chair?",
     "#thebigbusinesschronicles #halloweenparty #animation #lasvegas"),
    ("2026-10-24T13:00:00-07:00", "TT_GuessTheTheme_OldVegas_Pt1.mp4",
     "Three clues, one party theme. What is it?",
     "#guessthetheme #partytheme #vintagevegas #lasvegas"),
    ("2026-10-25T13:00:00-07:00", "TT_GuessTheTheme_OldVegas_Pt2.mp4",
     "Who guessed it? Which detail gave it away?",
     "#guessthetheme #oldvegas #partyinspo #lasvegas"),
]

def gql(inp):
    body = json.dumps({"query": MUT, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H",
                        "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

if __name__ == "__main__":
    ok = 0
    for due, f, line, tags in POSTS:
        inp = {"channelId": TT, "text": f"{line}\n\n{tags}", "mode": "customScheduled",
               "schedulingType": "automatic", "dueAt": due,
               "assets": [{"video": {"url": RAW + f}}]}
        d = gql(inp)
        if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
            time.sleep(90); d = gql(inp)
        cp = (d.get("data") or {}).get("createPost") or {}
        if cp.get("__typename") == "PostActionSuccess":
            ok += 1; print("OK  ", cp["post"]["id"], due, f)
        else:
            print("FAIL", f, json.dumps(d)[:240])
        time.sleep(3)
    print(f"done: {ok} of {len(POSTS)} queued")
