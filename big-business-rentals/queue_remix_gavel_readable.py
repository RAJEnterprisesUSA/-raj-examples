"""READABLE CUT (25.6s). TREND REMIX #23 "The Gavel Changed Hands" on all four platforms. Run ONLY after the owner approves, with the approved time:
python3 queue_remix_newmajority.py 2026-11-09T18:30:00-08:00"""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_TheGavelChangedHands_Readable.mp4"
VIDEOS = [
 ("fb", "the head of the table is under new leadership. 435 chairs, everybody switch sides. 🪑\n\n#lasvegas #family #animation #comedy #partyrentals", None),
 ("ig", "435 chairs. New seating chart. The head of the table is under new leadership, everybody switched sides of the aisle, and the cat took the big chair. The seats didn't change, who sits in them did. 🪑\n\n#newleadership #seatingchart #family #lasvegas #comedy", IG_PIN_TREND),
 ("tt", "The head of the table is under new leadership. 🪑\n\n#newleadership #seatingchart #family #comedy", None),
 ("yt", "The gavel changed hands, everybody switched sides of the aisle, and the cat took the big chair.\n\n#comedy #family #partyrentals", "435 chairs. New seating chart. 🪑 #Shorts"),
]
if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].startswith("2026-"): sys.exit("pass the approved dueAt, e.g. 2026-11-09T18:30:00-08:00")
    due = sys.argv[1]; ok = 0
    for ch, text, extra in VIDEOS:
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + T}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, due, res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    print(f"{ok}/4 queued")
