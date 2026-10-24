"""Owner Oct 24: "all episodes and remix videos should be posted on each platform."
Fills the gaps so every Chronicles episode and trend remix runs on Facebook, Instagram, TikTok and
YouTube. Captions follow each platform's charter (no phone, links or "free"; hashtag caps; pinned
follow comments on FB/IG; YouTube title + one-line description). Drawn animation: no AI labels."""
import json, subprocess, time

API = "https://api.buffer.com"
ORG = "6a8284ed71811e26a813241c"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "tt": "6ab81da7ea19ca0bdef9436e", "yt": "6ac2ff576a5c39ccb618d238"}
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
FB_PIN = ("Follow the page for more Las Vegas party life. Planning one? "
          "Everything is at bigbusinesspartyrentals.com")
IG_PIN_EP = "Follow so you never miss the next Big Business Chronicles episode."
IG_PIN_TREND = "Follow for more Las Vegas party life."

POSTS = [
 # Sat Oct 24 · 5pm · trend remix Porch Reveal (YouTube already queued)
 ("fb", "2026-10-24T17:00:00-07:00", "big-business-rentals/halloween/BB_Trend_PorchReveal.mp4",
  "the porch reveal everybody is doing, plus the one detail people forget: somewhere for the guests to sit. 🎃\n\n#lasvegas #halloween #porchreveal #animation #partyrentals", None),
 ("ig", "2026-10-24T17:00:00-07:00", "big-business-rentals/halloween/BB_Trend_PorchReveal.mp4",
  "The Halloween porch reveal, Las Vegas edition: the decor gets the views, the seating keeps the guests. 🎃\n\n#lasvegas #halloweendecor #porchreveal #halloweenparty #partyrentals", IG_PIN_TREND),
 ("tt", "2026-10-24T17:00:00-07:00", "big-business-rentals/halloween/BB_Trend_PorchReveal.mp4",
  "Decor gets the views. Seating keeps the guests. 🎃\n\n#porchreveal #halloween #lasvegas #animation", None),
 # Sat Oct 24 · 8pm · EP. 33 (Instagram and YouTube already queued)
 ("fb", "2026-10-24T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep33_TheLightCheck.mp4",
  "the big business chronicles ep. 33: every light worked on the first try. then the cat found the outlet. 💡\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("tt", "2026-10-24T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep33_TheLightCheck.mp4",
  "The Big Business Chronicles EP. 33: every light worked, then the cat found the outlet. 💡\n\n#thebigbusinesschronicles #halloween #animation #comedy", None),
 # Sun Oct 25 · 8pm · EP. 34 The Security Detail, all four
 ("fb", "2026-10-25T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep34_TheSecurityDetail.mp4",
  "the big business chronicles ep. 34: he hired a robot bodyguard to keep the cheap chair out of the halloween party. the cat had other plans. 🤖\n\n#lasvegas #halloweenparty #robot #animation #comedy", None),
 ("ig", "2026-10-25T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep34_TheSecurityDetail.mp4",
  "The Big Business Chronicles EP. 34: he hired a robot bodyguard for the Las Vegas Halloween party, and the cat walked right past it. 🤖\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #robot #comedy", IG_PIN_EP),
 ("tt", "2026-10-25T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep34_TheSecurityDetail.mp4",
  "The Big Business Chronicles EP. 34: he hired a robot bodyguard. The cat walked right past it. 🤖\n\n#thebigbusinesschronicles #robot #halloween #comedy", None),
 ("yt", "2026-10-25T20:00:00-07:00", "fb_safe/BB_Chronicles_Ep34_TheSecurityDetail.mp4",
  "The Big Business Chronicles EP. 34: he hired a robot bodyguard to keep the cheap chair out, and the cat walked right past it. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 34: The Security Detail 🤖 the robot let the cat in #Shorts"),
]

M = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
 ... on PostActionSuccess { post { id dueAt } } ... on MutationError { message } } }"""

def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "90", API, "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": q, "variables": v})], capture_output=True, text=True)
    d = json.loads(r.stdout)
    if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
        time.sleep(90); return gql(q, v)
    return d

if __name__ == "__main__":
    ok = 0
    for ch, due, path, text, extra in POSTS:
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + path}}]}
        if ch == "fb":
            inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig":
            inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt":
            inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public",
                                           "madeForKids": False}}
        d = gql(M, {"input": inp})
        res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"
        ok += good
        print("OK  " if good else "FAIL", ch, due, path.rsplit("/", 1)[-1],
              res.get("post", {}).get("id") if good else json.dumps(d)[:300])
        time.sleep(3)
    print(f"{ok}/{len(POSTS)} queued")
