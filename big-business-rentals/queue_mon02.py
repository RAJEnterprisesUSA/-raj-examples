"""Monday Nov 2 (PST -08:00): PRICE IT (1pm, FB feed + IG feed, Flyer 2026, fresh outdoor Friendsgiving yard), TREND REMIX
#15 Big Bang extra chair (5pm, first fresh nightly build) and EP. 42 The Carry (8pm), videos on all four platforms.
Run ONLY after the owner approves."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

F = RAW + "big-business-rentals/flyers2026/"
T = "big-business-rentals/halloween/BB_Trend_BigBangExtraChair.mp4"
E = "fb_safe/BB_Chronicles_Ep42_TheCarry.mp4"
D1, D5, D8 = "2026-11-02T13:00:00-08:00", "2026-11-02T17:00:00-08:00", "2026-11-02T20:00:00-08:00"
IG_PIN_SETUP = "Follow for more Las Vegas party setups."
IMAGES = [
 ("fb", "How much would you pay for this Friendsgiving setup? 🦃\n\nThree long tables, string lights and a sunset over the mountains. The decor is inspo; the tables and chairs underneath it are the part we bring, delivered and picked up across Las Vegas. Message us your date and headcount.\n\n#LasVegas #Friendsgiving #Thanksgiving #PartyRentals #SetupInspo",
  F + "BB26_PriceIt_FriendsgivingYard.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "How much would you pay for this Las Vegas Friendsgiving setup? Setup inspo: the tables and chairs underneath it are the part we bring. 🦃\n\n#lasvegas #friendsgiving #thanksgiving #partyrentals #setupinspo",
  F + "BB26_PriceIt_FriendsgivingYard.png", {"instagram": {"type": "post", "shouldShareToFeed": True, "firstComment": IG_PIN_SETUP}}),
]
VIDEOS = [
 ("fb", D5, T, "scientists may know why matter survived the big bang: a tiny bit was left over. party physics works the same way. 🌌\n\n#lasvegas #science #bigbang #animation #partyrentals", None),
 ("ig", D5, T, "Scientists may know why matter survived the Big Bang. Las Vegas party physics works the same way: one extra chair saves the night. 🌌\n\n#bigbang #science #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", D5, T, "Party physics: one extra chair saves the night. 🌌\n\n#science #bigbang #physics #comedy", None),
 ("yt", D5, T, "One tiny bit of matter was left over, and one extra chair saves the party.\n\n#science #bigbang #comedy",
  "Why matter survived the Big Bang, party edition 🌌 #Shorts"),
 ("fb", D8, E, "the big business chronicles ep. 42: dad moves eight chairs in one trip. the kids have other ideas. 🪑\n\n#lasvegas #family #animation #comedy", None),
 ("ig", D8, E, "The Big Business Chronicles EP. 42: Dad moves eight chairs in one trip, Lil copies Dad, and Baby copies Lil, but more. 🪑\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", D8, E, "The Big Business Chronicles EP. 42: Baby does whatever big bro does. But more. 🪑\n\n#thebigbusinesschronicles #siblings #family #comedy", None),
 ("yt", D8, E, "The Big Business Chronicles EP. 42: Dad moves eight chairs in one trip, the kids try to copy him, and the family holiday party gets a date. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 42: The Carry 🪑 Baby does it bigger #Shorts"),
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
