"""Tuesday Oct 27: TREND REMIX #9 Cat Handshake (5pm) and EP. 36 The Wind Check (8pm)
on all four platforms (everywhere rule). Captions per each platform's charter."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

T = "big-business-rentals/halloween/BB_Trend_CatHandshake.mp4"
E = "fb_safe/BB_Chronicles_Ep36_TheWindCheck.mp4"
D5, D8 = "2026-10-27T17:00:00-07:00", "2026-10-27T20:00:00-07:00"
POSTS = [
 ("fb", D5, T, "the cat handshake, party rental edition: the cat only shakes on good party decisions. 🐈‍⬛🤝\n\n#cathandshake #blackcat #lasvegas #partyrentals #animation", None),
 ("ig", D5, T, "The cat handshake trend, Las Vegas party rental edition: the toughest critic only shakes on good party decisions. 🐈‍⬛🤝\n\n#cathandshake #blackcat #lasvegas #partyrentals #halloween", IG_PIN_TREND),
 ("tt", D5, T, "The cat handshake, but he only shakes on good party decisions. 🐈‍⬛🤝\n\n#cathandshake #blackcat #partyrentals #lasvegas", None),
 ("yt", D5, T, "Setup done early: deal. Chairs delivered and picked up: deal. The cheap chair: absolutely not.\n\n#cathandshake #blackcat #comedy",
  "The cat handshake, party rental edition 🐈‍⬛🤝 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 36: saturday's forecast says vegas wind. the table clips say not today. 🌬️\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 36: Las Vegas wind versus a Halloween party setup, and table clips are the pro move. 🌬️\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #partytips #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 36: Vegas wind took the linen. Then it brought back the cheap chair. 🌬️\n\n#thebigbusinesschronicles #lasvegaswind #halloween #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 36: Vegas wind took the linen, the clips saved the party, and the wind brought the cheap chair back. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 36: The Wind Check 🌬️ gone with the wind #Shorts"),
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
