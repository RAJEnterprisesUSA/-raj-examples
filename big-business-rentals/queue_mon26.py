"""Monday Oct 26: trend remix #7 Mannequin Challenge (5pm) and EP. 35 The Headcount (8pm) on all
four platforms (owner's everywhere rule, Oct 24). Captions per each platform's charter."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

T30 = "big-business-rentals/halloween/BB_Trend_MannequinChallenge.mp4"
EP35 = "fb_safe/BB_Chronicles_Ep35_TheHeadcount.mp4"
D5, D8 = "2026-10-26T17:00:00-07:00", "2026-10-26T20:00:00-07:00"
POSTS = [
 ("fb", D5, T30, "2026 is the new 2016, so we brought back the mannequin challenge. one chair could not hold still. 🪑\n\n#mannequinchallenge #2016 #lasvegas #animation #comedy", None),
 ("ig", D5, T30, "2026 is the new 2016, so the Las Vegas party crew tried the mannequin challenge. One chair could not hold still. 🪑\n\n#mannequinchallenge #2016vibes #lasvegas #halloweenparty #comedy", IG_PIN_TREND),
 ("tt", D5, T30, "The mannequin challenge is back. One chair didn't get the memo. 🪑\n\n#mannequinchallenge #2016 #throwback #animation", None),
 ("yt", D5, T30, "2026 is the new 2016, so the party crew froze for the mannequin challenge, and one chair would not stand still.\n\n#mannequinchallenge #2016 #comedy",
  "We tried the mannequin challenge. The cheap chair couldn't. 🪑 #Shorts"),
 ("fb", D8, EP35, "the big business chronicles ep. 35: forty rsvps, and the math worked. then one more came in. 🪑\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, EP35, "The Big Business Chronicles EP. 35: the Las Vegas Halloween party RSVPs kept coming, and the cheap chair took the last seat. 🪑\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #rsvp #comedy", IG_PIN_EP),
 ("tt", D8, EP35, "The Big Business Chronicles EP. 35: one more RSVP. The cheap chair volunteered. 🪑\n\n#thebigbusinesschronicles #rsvp #halloween #comedy", None),
 ("yt", D8, EP35, "The Big Business Chronicles EP. 35: the RSVPs kept coming, and the cheap chair took the last seat. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 35: The Headcount 🪑 the last-minute RSVP #Shorts"),
]

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
              res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{len(POSTS)} queued")
