"""Wednesday Nov 4 (PST -08:00): CREW ONLY services flyer (11am, FB feed + IG Story, added to the services rotation),
GUESS THE THEME No. 3 Winter Wonderland Pt. 1 (1pm, TikTok via Buffer, AI label ON;
Instagram = Trial Reel the owner posts in the app) and EP. 44 The Teardown (8pm, all four platforms).
Pt. 2 (answer) is queued with Thursday unless the owner approves it now (pass --with-pt2).
The 5pm remix is built by the nightly task Tuesday evening. Run ONLY after the owner approves."""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, M, gql

V = RAW + "big-business-rentals/tiktok/"
E = "fb_safe/BB_Chronicles_Ep44_TheTeardown.mp4"
D8 = "2026-11-04T20:00:00-08:00"
GTT = [("2026-11-04T13:00:00-08:00", "TT_GuessTheTheme_WinterWonderland_Pt1.mp4",
        "Three clues, one party theme. Can you get it before clue 3? ❄️\n\n#guessthetheme #partytheme #partyinspo #lasvegas")]
if "--with-pt2" in sys.argv:
    GTT.append(("2026-11-05T13:00:00-08:00", "TT_GuessTheTheme_WinterWonderland_Pt2.mp4",
        "Winter Wonderland: birch centerpieces, hanging snowflakes and a snowman cake, all under one tent. Who got it on clue 1? ❄️\n\n#guessthetheme #winterwonderland #partyinspo #lasvegas"))
F = RAW + "big-business-rentals/flyers2026/"
D11 = "2026-11-04T11:00:00-08:00"
FB_CREW = ("Already have the tables and chairs, but nobody to set them up?\n\n"
           "Our Las Vegas crew comes to you, sets everything to your layout before guests arrive, then folds, stacks and clears it "
           "after the party. Your equipment, your space, our hands. Tents too. Every job is quoted by crew size, hours and date. "
           "Message us your date, hours and what you have.\n\n"
           "#LasVegasEvents #PartySetup #EventCrew #VegasParty #SetupAndTeardown")
IMAGES = [
 ("fb", FB_CREW, F + "BB26_CrewOnly.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_CrewOnly_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
VIDEOS = [
 ("fb", "the big business chronicles ep. 44: dad folds a table in 2 seconds. the cat is undefeated. 🪑\n\n#lasvegas #family #animation #comedy", None),
 ("ig", "The Big Business Chronicles EP. 44: Dad folds a table in 2 seconds, Baby stacks six chairs, and the cat wins three rounds. 🪑\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy", IG_PIN_EP),
 ("tt", "The Big Business Chronicles EP. 44: she lifted the cat without looking up. 🪑\n\n#thebigbusinesschronicles #siblings #teardown #comedy", None),
 ("yt", "The Big Business Chronicles EP. 44: Dad folds a table in 2 seconds, the kids race to stack chairs, and the cat claims the last one. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
  "EP. 44: The Teardown 🪑 the cat is undefeated #Shorts"),
]
if __name__ == "__main__":
    ok = n = 0
    for ch, text, img, md in IMAGES:
        n += 1
        d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D11,
                              "schedulingType": "automatic", "assets": [{"image": {"url": img}}], "metadata": md}})
        res = (d.get("data") or {}).get("createPost") or {}; good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D11, img.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    for due, f, text in GTT:
        n += 1
        d = gql(M, {"input": {"channelId": CH["tt"], "text": text, "mode": "customScheduled", "dueAt": due,
                              "schedulingType": "automatic", "assets": [{"video": {"url": V + f}}],
                              "metadata": {"tiktok": {"isAiGenerated": True}}}})
        res = (d.get("data") or {}).get("createPost") or {}; good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", "tt", due, f, res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    for ch, text, extra in VIDEOS:
        n += 1
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": D8,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + E}}]}
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, D8, E.rsplit("/", 1)[-1], res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{n} queued")
