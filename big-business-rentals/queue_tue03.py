"""Tuesday Nov 3 (PST -08:00): VENUE FLYER (1pm, FB feed + IG Story, Flyer 2026 holiday venue with the real room photo),
TREND REMIX #16 Reasons You Don't Need (5pm, fresh nightly build, social pool) and EP. 43 The Tablecloth (8pm), videos
on all four platforms. Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

F = RAW + "big-business-rentals/flyers2026/"
T = "big-business-rentals/halloween/BB_Trend_ReasonsYouDontNeed.mp4"
E = "fb_safe/BB_Chronicles_Ep43_TheTablecloth.mp4"
D1, D5, D8 = "2026-11-03T13:00:00-08:00", "2026-11-03T17:00:00-08:00", "2026-11-03T20:00:00-08:00"
FB_VENUE = ("Host the holidays. Skip the cleanup.\n\n"
            "Our private party room in Las Vegas seats 40 and holds 80 standing, with tables, chairs and setup included. "
            "Four hours is $800 for up to 40 guests, $20 a guest, and three hours is $625 for up to 25, $25 a guest. "
            "Thanksgiving, Friendsgiving and December parties all fit. Message us your date and headcount.\n\n"
            "#LasVegasVenue #VegasEventSpace #Friendsgiving #HolidayPartyVegas #LasVegasParty")
IMAGES = [
 ("fb", FB_VENUE, F + "BB26_Venue_Tue03.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_Venue_Tue03_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", D5, T, "reasons you don't need to rent tables and chairs for thanksgiving. reason three is our favorite. 🦃\n\n#lasvegas #thanksgiving #partyrentals #animation #comedy", None),
 ("ig", D5, T, "Reasons you don't need to rent tables and chairs for Thanksgiving in Las Vegas. All four fall apart. 🦃\n\n#thanksgiving #lasvegas #partyrentals #friendsgiving #comedy", IG_PIN_TREND),
 ("tt", D5, T, "Reasons you don't need to rent tables and chairs. 🦃\n\n#reasonswhy #thanksgiving #hosting #comedy", None),
 ("yt", D5, T, "Four reasons you don't need to rent tables and chairs for Thanksgiving. All four fall apart.\n\n#thanksgiving #hosting #comedy",
  "Reasons you don't need tables and chairs 🦃 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 43: dad nails the tablecloth trick. then the kids want a turn. 🍽️\n\n#lasvegas #family #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 43: Dad nails the tablecloth trick, Lil sends the plates flying, and Vaeh catches every one without looking up. 🍽️\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 43: she caught every plate without looking up. 🍽️\n\n#thebigbusinesschronicles #tableclothtrick #siblings #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 43: Dad nails the tablecloth trick, then every kid takes a turn. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 43: The Tablecloth 🍽️ she never looked up #Shorts"),
]
if __name__ == "__main__":
    ok = n = 0
    for ch, text, img, md in IMAGES:
        n += 1
        d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D1,
                              "schedulingType": "automatic", "assets": [{"image": {"url": img}}], "metadata": md}})
        res = (d.get("data") or {}).get("createPost") or {}; good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D1, img.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
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
