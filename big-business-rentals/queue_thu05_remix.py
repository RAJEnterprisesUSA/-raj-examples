"""Thursday Nov 5 5pm TREND REMIX #18 PARTY PHYSICS #2 (third kind of magnetism) on all four platforms (PST -08:00).
Run ONLY after the owner approves ("queue it")."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
T = "big-business-rentals/halloween/BB_Trend_PartyPhysics2_Magnetism.mp4"
D5 = "2026-11-05T17:00:00-08:00"
VIDEOS = [
 ("fb", "party physics #2: scientists just confirmed a third kind of magnetism. every party already had three. 🧲\n\n#lasvegas #science #partyphysics #animation #comedy", None),
 ("ig", "Party Physics #2: scientists just confirmed a third kind of magnetism. Every Las Vegas party already has three, and the strongest one is the last empty chair. 🧲\n\n#partyphysics #science #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", "Party Physics #2: the strongest force in the universe is the last empty chair. 🧲\n\n#partyphysics #science #physics #comedy", None),
 ("yt", "Scientists confirmed a third kind of magnetism. At a party, it's the last empty chair.\n\n#science #partyphysics #comedy",
  "Party Physics #2: the third kind of magnetism 🧲 #Shorts"),
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
