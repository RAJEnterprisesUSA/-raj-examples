"""Sunday Nov 1 (Season Two begins; PST, -08:00 after the DST change): HOLIDAY BOOKING FLYER (1pm, FB feed + IG Story),
TREND REMIX #14 "POV: hosting Thanksgiving in 2026" (5pm) and EP. 41 Meet the Family, the Season Two premiere (8pm),
videos on all four platforms (everywhere rule). Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

F = RAW + "big-business-rentals/flyers2026/"
T = "big-business-rentals/halloween/BB_Trend_POVThanksgiving2026.mp4"
E = "fb_safe/BB_Chronicles_Ep41_MeetTheFamily.mp4"
D1, D5, D8 = "2026-11-01T13:00:00-08:00", "2026-11-01T17:00:00-08:00", "2026-11-01T20:00:00-08:00"
IMAGES = [
 ("fb", "November starts today, and the holidays are for family.\n\nHosting Thanksgiving on the 26th, a Friendsgiving or a December Saturday? Seating for 24 is $88 and seating for 48 is $176, delivered and picked up anywhere in Las Vegas, with delivery quoted with your order. Want us to set up and break down too? Full-service starts at $265. Message us your date and headcount, or use the chat on our website.\n\n#LasVegas #Thanksgiving #Friendsgiving #HolidayParty #PartyRentals",
  F + "BB26_Holiday_Sun01.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_Holiday_Sun01_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", D5, T, "pov: hosting thanksgiving in 2026. 47 maybes, a guest list that changes every four minutes, and a turkey with its own seat. 🦃\n\n#lasvegas #thanksgiving #pov #animation #partyrentals", None),
 ("ig", D5, T, "POV: hosting Thanksgiving in Las Vegas in 2026. The guest list keeps growing; the seating does not have to be the stress. 🦃\n\n#pov #thanksgiving #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", D5, T, "POV: hosting Thanksgiving in 2026. 🦃\n\n#pov #thanksgiving #hosting #comedy", None),
 ("yt", D5, T, "Hosting Thanksgiving in 2026: 47 maybes, a guest list that changes every four minutes, and a turkey with its own seat.\n\n#pov #thanksgiving #comedy",
  "POV: hosting Thanksgiving in 2026 🦃 #Shorts"),
 ("fb", D8, E, "the big business chronicles, season two, ep. 41: meet the family. vaeh, lil big business, princess and baby big business are here for the holidays. 🏡\n\n#lasvegas #family #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles Season Two, EP. 41: meet the family. Mr. Big Business brought the kids for the Las Vegas holiday season. Which kid are you? 🏡\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles Season Two: meet the family. Which kid are you? 🏡\n\n#thebigbusinesschronicles #seasontwo #family #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles Season Two, EP. 41: meet the family, and Vaeh set the whole table without looking up. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 41: Meet the Family 🏡 Season Two premiere #Shorts"),
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
