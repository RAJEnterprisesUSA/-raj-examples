"""Monday Nov 9 5pm TREND REMIX #21 "One table, five parties" on all four platforms (PST -08:00). Replaces the pulled "It's
time" tree remix (owner Nov 8: no Christmas-celebration videos). Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_OneTableFiveParties.mp4"
D5 = "2026-11-09T17:00:00-08:00"
VIDEOS = [
 ("fb", "one table. five parties. birthday, friendsgiving, game day, baby shower and office party. 🪑\n\n#lasvegas #partyrentals #tablerentals #animation #comedy", None),
 ("ig", "One table. Five parties. Birthday, Friendsgiving, game day, baby shower and office party, all on one 6 ft table. Which look is yours? 🪑\n\n#lasvegas #partyrentals #eventdecor #animation #comedy", IG_PIN_TREND),
 ("tt", "One table, five looks. 🪑\n\n#onetablefiveways #partyideas #styling #comedy", None),
 ("yt", "Birthday, Friendsgiving, game day, baby shower and office party. One 6 ft table.\n\n#partyideas #comedy #partyrentals", "One table. Five parties. 🪑 #Shorts"),
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
