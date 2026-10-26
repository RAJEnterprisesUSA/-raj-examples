"""Monday Oct 26 5pm: trend remix #8 Fan Transition (current Oct 2026 TikTok format) on all four
platforms, replacing the pulled Mannequin Challenge remix."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
P = "big-business-rentals/halloween/BB_Trend_FanTransition.mp4"
D = "2026-10-26T17:00:00-07:00"
POSTS = [
 ("fb", "the fan transition, party setup edition: empty room, tables, linens, chairs, done. 🎉\n\n#fantransition #partysetup #lasvegas #eventrentals #animation", None),
 ("ig", "The fan transition, Las Vegas party setup edition: one blade pass at a time, an empty room becomes the party. 🎉\n\n#fantransition #partysetup #lasvegas #eventdecor #partyrentals", IG_PIN_TREND),
 ("tt", "Fan transition, but make it a party setup. 🎉\n\n#fantransition #partysetup #transformation #lasvegas", None),
 ("yt", "One fan blade at a time: tables, linens, chairs, the details. The cheap chair did not make the cut.\n\n#fantransition #partysetup #lasvegas", "Fan transition: empty room to full party 🎉 #Shorts"),
]
ok = 0
for ch, text, extra in POSTS:
    inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D,
           "schedulingType": "automatic", "assets": [{"video": {"url": RAW + P}}]}
    if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
    elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
    elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
    d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
    good = res.get("__typename") == "PostActionSuccess"; ok += good
    print("OK  " if good else "FAIL", ch, res.get("post", {}).get("id") if good else str(d)[:300])
    time.sleep(3)
print(f"{ok}/{len(POSTS)} queued")
