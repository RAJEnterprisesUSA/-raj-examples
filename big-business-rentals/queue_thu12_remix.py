"""Thu Nov 12 5pm TREND REMIX #26 Party Physics #3 "Once in 10 Billion" on all four platforms. Run ONLY after the owner approves, with the approved time:
python3 queue_remix_newmajority.py 2026-11-09T18:30:00-08:00"""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_OnceInTenBillion.mp4"
VIDEOS = [
 ("fb", "physicists saw something that happens 1 in 10 billion. rarer: a party where every guest has a chair. 🌌\n\n#lasvegas #science #physics #animation #partyrentals", None),
 ("ig", "Physicists finally saw something that happens 1 in 10 billion. We ran our own experiment. The rarest event of all: a party where every guest has a chair. With us, every time. 🌌\n\n#partyphysics #science #lasvegas #comedy #partyrentals", IG_PIN_TREND),
 ("tt", "Party physics #3: 1 in 10 billion. 🌌\n\n#science #physics #partyphysics #comedy", None),
 ("yt", "Unc carried a table the right way, Vaeh smiled, and every guest got a chair.\n\n#science #comedy #partyrentals", "1 in 10 billion: party physics edition 🌌 #Shorts"),
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
