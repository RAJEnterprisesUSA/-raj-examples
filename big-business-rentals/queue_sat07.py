"""Saturday Nov 7 (PST -08:00): PRICE LIST (1pm, FB feed + IG Story, Thanksgiving seating by headcount) and EP. 46
The Crew Is Back (8pm, all four platforms). The Recount (5pm) is already queued. Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, M, gql
F = RAW + "big-business-rentals/flyers2026/"
E = "fb_safe/BB_Chronicles_Ep46_TheCrewIsBack.mp4"
D1, D8 = "2026-11-07T13:00:00-08:00", "2026-11-07T20:00:00-08:00"
FB_PL = ("Hosting Thanksgiving? Here is the seating math.\n\n"
         "Every set is a 6 ft table and 6 chairs for $22, which works out to $3.67 a seated guest. Twelve guests is 2 sets for $44, "
         "twenty-four is 4 sets for $88, thirty-six is 6 sets for $132, and forty-eight is 8 sets for $176. Chairs are $2 each and "
         "round tables are $15. Everything is delivered and picked up across Las Vegas, delivery is quoted with your order, and "
         "full-service setup starts at $265. Message us your date and headcount.\n\n"
         "#LasVegasPartyRentals #ThanksgivingVegas #Friendsgiving #TableAndChairRentals #VegasEvents")
IMAGES = [
 ("fb", FB_PL, F + "BB26_PriceList_Sat07.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_PriceList_Sat07_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", "the big business chronicles ep. 46: the whole crew is back. 🪑\n\n#lasvegas #family #animation #comedy", None),
 ("ig", "The Big Business Chronicles EP. 46: the whole crew is back for Season Two. Mrs. Never Wrong, Unc, Tyler, Lil Wobbles and the cat, plus the family. Which one is your favorite? 🪑\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", "The Big Business Chronicles EP. 46: he is still the new intern. 🪑\n\n#thebigbusinesschronicles #thecrewisback #family #comedy", None),
 ("yt", "The Big Business Chronicles EP. 46: the whole Season One crew joins the family for the Dec 19 party. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 46: The Crew Is Back 🪑 still the new intern #Shorts"),
]
if __name__ == "__main__":
    ok = n = 0
    for ch, text, img, md in IMAGES:
        n += 1
        d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D1,
                              "schedulingType": "automatic", "assets": [{"image": {"url": img}}], "metadata": md}})
        res = (d.get("data") or {}).get("createPost") or {}; good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D1, img.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    for ch, text, extra in VIDEOS:
        n += 1
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D8,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + E}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D8, E.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    print(f"{ok}/{n} queued")
