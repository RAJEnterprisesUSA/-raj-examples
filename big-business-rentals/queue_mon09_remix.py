"""Monday Nov 9 5pm TREND REMIX #21 "It's time." on all four platforms (PST -08:00). Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_ItsTime.mp4"
D5 = "2026-11-09T17:00:00-08:00"
VIDEOS = [
 ("fb", "it's time. not for the tree, for the tables. the pre-christmas saturdays this year are dec 5, 12 and 19. 🎄\n\n#lasvegas #holidayparty #partyrentals #animation #comedy", None),
 ("ig", "It's time. Not for the tree, for the tables. The pre-Christmas Saturdays this year are Dec 5, 12 and 19. 🎄\n\n#lasvegas #holidayparty #partyrentals #animation #comedy", IG_PIN_TREND),
 ("tt", "It's time. 🎄\n\n#itstime #holidayseason #christmas #comedy", None),
 ("yt", "Not for the tree. For the December tables: Dec 5, 12 and 19.\n\n#holidays #comedy #partyrentals", "It's time. 🎄 #Shorts"),
]
if __name__ == "__main__":
    ok = 0
    for ch, text, extra in VIDEOS:
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D5,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + T}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D5, res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    print(f"{ok}/4 queued")
