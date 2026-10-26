"""Saturday Oct 31: PRICE LIST (1pm, FB feed + IG Story), TREND REMIX #13 The Merger (5pm, first news remix) and
EP. 40 The Halloween Party, the Season One finale (8pm), videos on all four platforms (everywhere rule).
Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

F = RAW + "big-business-rentals/flyers2026/"
T = "big-business-rentals/halloween/BB_Trend_TheMerger.mp4"
E = "fb_safe/BB_Chronicles_Ep40_TheHalloweenParty.mp4"
D1, D5, D8 = "2026-10-31T13:00:00-07:00", "2026-10-31T17:00:00-07:00", "2026-10-31T20:00:00-07:00"
IMAGES = [
 ("fb", "Real prices, no guessing.\n\nFolding chairs are $2, 6 ft rectangle tables are $10, 6 ft round tables are $15, or get a table with 6 chairs for $22. Everything is delivered and picked up across Las Vegas, and full-service setup starts at $265. Questions? The chat on our website answers right away.\n\n#LasVegas #PartyRentals #VegasEvents #TablesAndChairs #LasVegasParty",
  F + "BB26_PriceList_Sat31.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_PriceList_Sat31_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", D5, T, "big merger news this week, party rental edition: two small parties, one long table. 🤝\n\n#lasvegas #merger #partyrentals #animation #comedy", None),
 ("ig", D5, T, "Big merger news this week, Las Vegas party rental edition: two small parties became one long table, and the board approved. 🤝\n\n#merger #partyrentals #lasvegas #comedy #animation", IG_PIN_TREND),
 ("tt", D5, T, "Big merger news this week. Party rental edition. 🤝\n\n#merger #businessnews #partyrentals #comedy", None),
 ("yt", D5, T, "Two small parties merged into one long table, and the board approved.\n\n#merger #partyrentals #comedy",
  "The merger, party rental edition 🤝 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 40, the season one finale: the halloween party. full cast, one missing seat, and the extra chair on the truck. 🎃\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 40, the Season One finale: the whole cast at the Las Vegas Halloween party, and the extra chair saved the night. 🎃\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #seasonfinale #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 40, Season One finale: the host had no seat. The extra chair was on the truck. 🎃\n\n#thebigbusinesschronicles #halloween #seasonfinale #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 40, the Season One finale: the whole cast at the Halloween party, and the extra chair saved the night. Season Two is coming soon.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 40: The Halloween Party 🎃 Season One finale #Shorts"),
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
