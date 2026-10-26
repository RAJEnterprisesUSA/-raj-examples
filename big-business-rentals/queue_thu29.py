"""Thursday Oct 29: TREND REMIX #11 Pumpkin Head Illusion (5pm) and EP. 38 The Delivery (8pm)
on all four platforms (everywhere rule). Captions per each platform's charter."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

T = "big-business-rentals/halloween/BB_Trend_PumpkinHeadIllusion.mp4"
E = "fb_safe/BB_Chronicles_Ep38_TheDelivery.mp4"
D5, D8 = "2026-10-29T17:00:00-07:00", "2026-10-29T20:00:00-07:00"
POSTS = [
 ("fb", D5, T, "the pumpkin head illusion is all about the angle. and a real party table in the back. 🎃\n\n#pumpkinhead #halloween #lasvegas #animation #partyrentals", None),
 ("ig", D5, T, "The pumpkin head illusion, Las Vegas party edition: it is all about the angle, and a real party table in the back. 🎃\n\n#pumpkinhead #halloween #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", D5, T, "The pumpkin head illusion. The secret is the table. 🎃\n\n#pumpkinheadillusion #halloween #forcedperspective #lasvegas", None),
 ("yt", D5, T, "It is all about the angle, and a real party table in the back. The cat does not like magic.\n\n#pumpkinhead #halloween #comedy",
  "The pumpkin head illusion, explained 🎃 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 38: delivery day. four chairs ordered, five showed up. 🪑\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 38: delivery day before the Las Vegas Halloween party, and something extra came in with the chairs. 🪑\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #deliveryday #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 38: four chairs ordered. Five showed up. 🪑\n\n#thebigbusinesschronicles #deliveryday #halloween #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 38: four chairs ordered, five delivered, and Mr. Big Business finally won one. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 38: The Delivery 🪑 he finally won one #Shorts"),
]
if __name__ == "__main__":
    ok = 0
    for ch, due, path, text, extra in POSTS:
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + path}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, due, path.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{len(POSTS)} queued")
