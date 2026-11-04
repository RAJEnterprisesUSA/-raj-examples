"""Wednesday Nov 4 5pm TREND REMIX #17 "The red party and the blue party" on all four platforms (PST -08:00).
Run ONLY after the owner approves ("queue it")."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_RedPartyBlueParty.mp4"
D5 = "2026-11-04T17:00:00-08:00"
VIDEOS = [
 ("fb", "election night: the red party and the blue party both called. we set up both the exact same way. 🪑\n\n#lasvegas #electionnight #partyrentals #animation #comedy", None),
 ("ig", "Election night in Las Vegas: the red party and the blue party both booked tables. Six each, 36 seats each. It's a tie, and everybody still needs a seat. 🪑\n\n#electionnight #lasvegas #partyrentals #animation #comedy", IG_PIN_TREND),
 ("tt", "The red party and the blue party both called. 🪑\n\n#electionnight #redvsblue #partyrentals #comedy", None),
 ("yt", "Six tables each, 36 seats each, and a tie. Everybody still needs a seat.\n\n#electionnight #comedy #partyrentals",
  "The red party and the blue party both called 🪑 #Shorts"),
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
