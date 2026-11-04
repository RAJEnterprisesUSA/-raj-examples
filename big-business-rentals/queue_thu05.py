"""Thursday Nov 5 (PST -08:00): REFERRAL FLYER event coordinators (1pm, FB feed + IG Story) and EP. 45 The Headcount
(8pm, all four platforms). GTT Pt. 2 (1pm TikTok) is already queued; the 5pm remix comes from Wednesday's nightly build.
Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, M, gql
F = RAW + "big-business-rentals/flyers2026/"
E = "fb_safe/BB_Chronicles_Ep45_TheHeadcount.mp4"
D1, D8 = "2026-11-05T13:00:00-08:00", "2026-11-05T20:00:00-08:00"
FB_REF = ("Event coordinators in Las Vegas: your clients ask you who does the tables before anyone else hears about the party.\n\n"
          "Point them to Big Business for tables and chairs delivered and picked up, tents, and setup and teardown crews. When "
          "their event is done, we say thank you with up to $100 for every booking you send. The reward is based on booking "
          "size, there is no limit on referrals, and it is paid after the referred event is completed. Message us and we will "
          "get you set up.\n\n#LasVegasEvents #LasVegasEventPlanner #EventCoordinator #VegasPartyRentals #VegasEvents")
IMAGES = [
 ("fb", FB_REF, F + "BB26_Referral_Thu05.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_Referral_Thu05_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", "the big business chronicles ep. 45: the guest list went from 30 to 101. dad did the math every time. 🪑\n\n#lasvegas #family #animation #comedy", None),
 ("ig", "The Big Business Chronicles EP. 45: 30 guests became 100, plus a cat. Six seats a table, and Dad had the math done every time. What's your headcount this year? 🪑\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", "The Big Business Chronicles EP. 45: she said nothing and posted it. 40 RSVPs. 🪑\n\n#thebigbusinesschronicles #siblings #holidayparty #comedy", None),
 ("yt", "The Big Business Chronicles EP. 45: the family party guest list keeps growing and Dad does the math every time. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 45: The Headcount 🪑 she posted it #Shorts"),
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
