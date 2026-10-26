"""Friday Oct 30: SAVE-WORTHY CAROUSEL Holiday Seating Cheat Sheet (1pm, IG carousel + FB album),
TREND REMIX #12 Be OK (5pm) and EP. 39 The Night Before (8pm) on all four platforms (everywhere rule).
Captions per each platform's charter. Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

C = [RAW + f"big-business-rentals/flyers2026/BB26_Carousel_Fri30_{i}.png" for i in range(1, 7)]
T = "big-business-rentals/halloween/BB_Trend_BeOK.mp4"
E = "fb_safe/BB_Chronicles_Ep39_TheNightBefore.mp4"
D1, D5, D8 = "2026-10-30T13:00:00-07:00", "2026-10-30T17:00:00-07:00", "2026-10-30T20:00:00-07:00"
IG_PIN_GUIDE = "Follow for more Las Vegas party planning guides."
CAROUSEL = [
 ("fb", "the holiday seating cheat sheet: how many tables you actually need, and what it costs. one table and six chairs seats six guests, so take your count, divide by six and round up.\n\n#lasvegas #holidayhosting #partyplanning #thanksgiving #partyrentals",
  {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "The holiday seating cheat sheet for Las Vegas hosts: guests, tables and the total on one slide, plus two tips for Thanksgiving and December dinners.\n\n#lasvegas #holidayhosting #partyplanning #thanksgivingdinner #partyrentals",
  {"instagram": {"type": "post", "shouldShareToFeed": True, "firstComment": IG_PIN_GUIDE}}),
]
VIDEOS = [
 ("fb", D5, T, "the day before halloween at a party rental company: not okay with any of it. still dancing. 🎃\n\n#lasvegas #halloween #beok #animation #partyrentals", None),
 ("ig", D5, T, "The day before Halloween at a Las Vegas party rental company: not okay with any of it, still dancing. 🎃\n\n#beok #halloween #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", D5, T, "Not okay. Still dancing. The extra chairs are on the truck. 🎃\n\n#beok #halloween #partyrentals #lasvegas", None),
 ("yt", D5, T, "The day before Halloween at a party rental company: not okay with any of it, still dancing.\n\n#beok #halloween #comedy",
  "Not okay. Still dancing. 🎃 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 39: the night before the halloween party. one last check in the dark. he was not alone. 🔦\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 39: the night before the Las Vegas Halloween party, one last flashlight check, and he was not alone. 🔦\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #comedy #animation", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 39: one last check the night before the party. He was not alone. 🔦\n\n#thebigbusinesschronicles #halloween #comedy #animation", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 39: one last flashlight check the night before the Halloween party, and he was not alone. Next episode tomorrow: the finale.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 39: The Night Before 🔦 he was not alone #Shorts"),
]
if __name__ == "__main__":
    ok = n = 0
    for ch, text, md in CAROUSEL:
        n += 1
        d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D1, "schedulingType": "automatic",
                              "assets": [{"image": {"url": u}} for u in C], "metadata": md}})
        res = (d.get("data") or {}).get("createPost") or {}; good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D1, "carousel", res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    for ch, due, path, text, extra in VIDEOS:
        n += 1
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + path}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, due, path.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{n} queued")
