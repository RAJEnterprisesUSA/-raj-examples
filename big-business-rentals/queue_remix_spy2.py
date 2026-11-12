"""TREND REMIX #28 "The Spy, Part 2: Target Big Business" on all four platforms. Run ONLY after the owner approves, with the approved time:
python3 queue_remix_newmajority.py 2026-11-09T18:30:00-08:00"""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_SpyPart2_TargetBigBusiness.mp4"
VIDEOS = [
 ("fb", "part 2: the spy's next target was big business. it did not go well for her. 🕵️\n\n#lasvegas #comedy #animation #partyrentals #techboss", None),
 ("ig", "Part 2: the Spy's next target was Big Business. A fake mustache, a chair disguise and the top secret plans... it was a seating chart. Spy 0, Big Business 1. 🕵️\n\n#spy #part2 #lasvegas #comedy #partyrentals", IG_PIN_TREND),
 ("tt", "Part 2: she picked the wrong business. 🕵️\n\n#spy #part2 #techboss #comedy", None),
 ("yt", "Every disguise failed, and the top secret plans were just a seating chart.\n\n#comedy #spy #partyrentals", "Part 2: the spy picked the wrong business 🕵️ #Shorts"),
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
