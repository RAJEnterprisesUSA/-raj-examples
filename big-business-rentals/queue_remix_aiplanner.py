"""TREND REMIX #24 "We Let the AI Plan the Party" on all four platforms. Run ONLY after the owner approves, with the approved time:
python3 queue_remix_newmajority.py 2026-11-09T18:30:00-08:00"""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_AIPlansTheParty.mp4"
VIDEOS = [
 ("fb", "an ai to help run your family? we let it plan the party. it ordered one chair for nine. 🪑\n\n#lasvegas #ai #family #comedy #partyrentals", None),
 ("ig", "An AI to help run your family? We let it plan the party. It scanned the photos, ordered one chair for nine guests, and seated the cat at the head of the table. AI can plan the party. It can't carry the chairs. 🪑\n\n#ai #family #lasvegas #comedy #partyrentals", IG_PIN_TREND),
 ("tt", "We let the AI plan the party. 🪑\n\n#ai #aiapp #family #comedy", None),
 ("yt", "It ordered one chair for nine guests and seated the cat at the head of the table.\n\n#ai #comedy #partyrentals", "We let the AI plan the party. 🪑 #Shorts"),
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
