"""Queue owner-approved Facebook week 1 posts (Oct 20 night): Wed 5pm Cheap Chair Reel (the
Buffer caption test) and Fri 12pm Chair Guy album. Facebook only. Captions per the Facebook
charter: no link, no phone, no bait, max 5 hashtags, minimal capitals."""
import json, subprocess, time

API = "https://api.buffer.com"
FB = "6aabfb63ea19ca0bde696947"
RAW = ("https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/"
       "claude/photo-to-logo-editing-krxiu5/big-business-rentals/")
PIN = ("Follow the page for more Las Vegas party life. Planning one? Everything is at "
       "bigbusinesspartyrentals.com")
MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
 ... on PostActionSuccess { post { id dueAt } } ... on MutationError { message } } }"""

POSTS = [
    ("2026-10-21T17:00:00-07:00", "reel",
     [{"video": {"url": RAW + "tiktok/TT_Chronicles_HalloweenArc_Pt1_CheapChair.mp4"}}],
     "he had one job: sit down. the cheap chair had other plans. who in your family always ends up on the worst seat?\n\n#lasvegas #halloweenparty #animation #partyfail"),
    ("2026-10-23T12:00:00-07:00", "post",
     [{"image": {"url": RAW + f"facebook/week1/FB_People_ChairGuy_{i:02d}.png"}} for i in range(1, 6)],
     "every party has a chair guy. he volunteered weeks ago and he means well. what did your chair guy show up with?\n\n#lasvegas #partyplanning #groupchat #familyparty"),
]

def gql(inp):
    body = json.dumps({"query": MUT, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H",
                        "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

if __name__ == "__main__":
    for due, ptype, assets, text in POSTS:
        inp = {"channelId": FB, "text": text, "mode": "customScheduled",
               "schedulingType": "automatic", "dueAt": due, "assets": assets,
               "metadata": {"facebook": {"type": ptype, "firstComment": PIN}}}
        d = gql(inp)
        if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
            time.sleep(90); d = gql(inp)
        cp = (d.get("data") or {}).get("createPost") or {}
        print(("OK   " + cp["post"]["id"]) if cp.get("__typename") == "PostActionSuccess"
              else "FAIL " + json.dumps(d)[:240], due, ptype)
        time.sleep(3)
