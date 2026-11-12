"""TREND REMIX #27 "He Had No Idea She Was a Spy" on all four platforms. Run ONLY after the owner approves, with the approved time:
python3 queue_remix_newmajority.py 2026-11-09T18:30:00-08:00"""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_NoIdeaSheWasASpy_Slow.mp4"
VIDEOS = [
 ("fb", "the tech boss had no idea his date was a spy. some people cheat. we won't cheat on you. 🕵️\n\n#lasvegas #comedy #animation #partyrentals #techboss", None),
 ("ig", "The Tech Boss had no idea his date was a spy. Some people cheat. We won't cheat on you: every chair we quote shows up. 🕵️\n\n#techboss #spy #lasvegas #comedy #partyrentals", IG_PIN_TREND),
 ("tt", "He had no idea she was a spy. 🕵️\n\n#techboss #spy #cheating #comedy", None),
 ("yt", "Some people cheat. We won't cheat on you: every chair we quote shows up.\n\n#comedy #spy #partyrentals", "He had no idea his date was a spy 🕵️ #Shorts"),
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
