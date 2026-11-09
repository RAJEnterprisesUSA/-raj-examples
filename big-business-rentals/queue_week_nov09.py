"""Week of Mon Nov 9 to Sun Nov 15 (PST -08:00): 1pm weekly promotion + 8pm Chronicles episode for each day.
5pm remixes are built and queued separately by the nightly task (Monday's: queue_mon09_remix.py).
Run ONLY the days the owner approves, e.g. `python3 queue_week_nov09.py mon tue`. Nothing runs without a day argument."""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, M, gql

F = RAW + "big-business-rentals/flyers2026/"
V = RAW + "big-business-rentals/tiktok/"
IG_PIN = "Follow @bigbusiness_rentals_events for real setups and open dates. Booking December now. We are on Facebook too: facebook.com/profile.php?id=61589138907701"

def feed(fb_text, fb_img, ig_img, ig_story=True, ig_text=""):
    """FB feed post + IG Story (or IG feed post when ig_story is False)."""
    out = [("fb", fb_text, [fb_img], {"facebook": {"type": "post", "firstComment": FB_PIN}})]
    if ig_story: out.append(("ig", "", [ig_img], {"instagram": {"type": "story", "shouldShareToFeed": False}}))
    else: out.append(("ig", ig_text, [ig_img], {"instagram": {"type": "post", "shouldShareToFeed": True, "firstComment": IG_PIN}}))
    return out

def ep(file, fb, ig, tt, yt_desc, yt_title):
    return file, [("fb", fb, None), ("ig", ig, IG_PIN_EP), ("tt", tt, None), ("yt", yt_desc, yt_title)]

H_EP = "\n\n#lasvegas #family #animation #comedy"
DAYS = {
 "mon": dict(date="2026-11-09",
   images=feed("How much would you pay for this Thanksgiving setup? 🦃\n\n"
               "Four long banquet tables, white chairs and room for the whole family. The decor is inspo; the tables and chairs "
               "underneath it are the part we bring, delivered and picked up across Las Vegas. Message us your date and headcount.\n\n"
               "#LasVegas #Thanksgiving #Friendsgiving #PartyRentals #SetupInspo",
               F + "BB26_PriceIt_ThanksgivingHall.png", F + "BB26_PriceIt_ThanksgivingHall.png", ig_story=False,
               ig_text="How much would you pay for this Las Vegas Thanksgiving setup? 🦃\n\n"
                       "Setup inspo: four long tables and white chairs. The tables and chairs underneath it are the part we bring. "
                       "Message us your date and headcount.\n\n#lasvegas #thanksgiving #friendsgiving #partyrentals #setupinspo"),
   episode=ep("fb_safe/BB_Chronicles_Ep46_TheCrewIsBack.mp4",
     "the big business chronicles ep. 46: the whole crew is back. 🪑" + H_EP,
     "The Big Business Chronicles EP. 46: the whole crew is back for Season Two. Mrs. Never Wrong, Unc, Tyler, Lil Wobbles and the cat, plus the family. Which one is your favorite? 🪑\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy",
     "The Big Business Chronicles EP. 46: he is still the new intern. 🪑\n\n#thebigbusinesschronicles #thecrewisback #family #comedy",
     "The Big Business Chronicles EP. 46: the whole Season One crew joins the family for the Dec 19 party. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 46: The Crew Is Back 🪑 still the new intern #Shorts")),
 "tue": dict(date="2026-11-10",
   images=feed("Short on crew for a big event?\n\n"
               "Our Las Vegas setup and teardown crews work for venues, planners and hosts who already have the tables, chairs or "
               "tents. We set everything to your layout before doors open, then fold, stack and clear it after. Every job is quoted "
               "by crew size, hours and date. Message us your date, hours and what needs to be set.\n\n"
               "#LasVegasEvents #EventCrew #SetupAndTeardown #VegasVenues #EventPlanning",
               F + "BB26_LaborCrew.png", F + "BB26_LaborCrew_Story.png"),
   episode=ep("fb_safe/BB_Chronicles_Ep47_TheTent.mp4",
     "the big business chronicles ep. 47: dad raises the tent in seconds. lil wobbles is not a good weight. ⛺" + H_EP,
     "The Big Business Chronicles EP. 47: Dad raises the Dec 19 tent in seconds, Mrs. Never Wrong adds the weights, and the wind takes care of Lil Wobbles. Tent or no tent? ⛺\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy",
     "The Big Business Chronicles EP. 47: she added the weights before anyone asked. ⛺\n\n#thebigbusinesschronicles #tent #family #comedy",
     "The Big Business Chronicles EP. 47: Dad raises the Dec 19 party tent, the wind shows up, and Mrs. Never Wrong was right. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 47: The Tent ⛺ she was right #Shorts")),
 "wed": dict(date="2026-11-11",
   gtt=("TT_GuessTheTheme_HotCocoa_Pt1.mp4",
        "Three clues, one party theme. Can you get it before clue 3? ☕\n\n#guessthetheme #partytheme #partyinspo #lasvegas"),
   episode=ep("fb_safe/BB_Chronicles_Ep48_TheCocoaBar.mp4",
     "the big business chronicles ep. 48: the cocoa bar. dad made the catch. ☕" + H_EP,
     "The Big Business Chronicles EP. 48: Dad sets the Dec 19 cocoa bar in seconds, Unc fills the marshmallow jar with chairs, and somebody put the pot on Lil Wobbles. Marshmallows or whipped cream? ☕\n\n#thebigbusinesschronicles #seasontwo #hotcocoa #lasvegas #comedy",
     "The Big Business Chronicles EP. 48: Baby got the bigger whipped cream beard. ☕\n\n#thebigbusinesschronicles #hotcocoa #family #comedy",
     "The Big Business Chronicles EP. 48: a cocoa bar for Dec 19, a pot on the wrong chair and one big save. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 48: The Cocoa Bar ☕ not one spill #Shorts")),
 "thu": dict(date="2026-11-12",
   images=feed("Caterers: your clients always ask who to call for tables and chairs.\n\n"
               "Send them our way with their date and headcount. We deliver and pick up across Las Vegas, and setup crews are "
               "available. When their event is done, you get a thank-you from us. Reward based on booking size, up to $100 · "
               "No limit on referrals · Paid after the referred event is completed. Message us and we will send you the details.\n\n"
               "#LasVegasCaterers #VegasCatering #LasVegasEvents #EventPros #PartyRentals",
               F + "BB26_Referral_Thu12.png", F + "BB26_Referral_Thu12_Story.png"),
   gtt=("TT_GuessTheTheme_HotCocoa_Pt2.mp4",
        "Hot Cocoa Party: marshmallow jars, peppermint sticks and a long cocoa bar. Who got it on clue 1? ☕\n\n#guessthetheme #hotcocoa #partyinspo #lasvegas"),
   episode=ep("fb_safe/BB_Chronicles_Ep49_TheBuffetLine.mp4",
     "the big business chronicles ep. 49: dad built the buffet line. dad is last in it. 🍽️" + H_EP,
     "The Big Business Chronicles EP. 49: the caterer brings the food, Dad builds the buffet line, Baby cuts in front, and the cat is first in line. First in line or last? 🍽️\n\n#thebigbusinesschronicles #seasontwo #family #lasvegas #comedy",
     "The Big Business Chronicles EP. 49: Baby cut the line. 🍽️\n\n#thebigbusinesschronicles #buffet #siblings #comedy",
     "The Big Business Chronicles EP. 49: Dad builds the buffet line in seconds and still ends up last in it. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 49: The Buffet Line 🍽️ dad is last in it #Shorts")),
 "fri": dict(date="2026-11-13",
   carousel=([F + f"BB26_Carousel_Fri13_{i}.png" for i in range(1, 7)],
     "3 ways to seat 24 for Thanksgiving. Swipe for the floor plans. 🦃\n\n"
     "One long table, two long rows, or a grown-ups table plus a kids' table. Every layout is 4 sets, a 6 ft table and 6 chairs "
     "each, for $88 total, delivered and picked up across Las Vegas with delivery quoted with your order. Want us to set it up? "
     "Full-service starts at $265. Save this for Thanksgiving, then message us your date and headcount.\n\n"
     "#ThanksgivingVegas #Friendsgiving #LasVegasPartyRentals #TableAndChairRentals #HostingTips"),
   episode=ep("fb_safe/BB_Chronicles_Ep50_TheFloorPlan.mp4",
     "the big business chronicles ep. 50: rows, rounds or u-shape. the cat approved it. 📐" + H_EP,
     "The Big Business Chronicles EP. 50: Dad draws the Dec 19 floor plan in seconds, Mrs. Never Wrong moves one table one inch (it blocked the door), and somebody drew Lil Wobbles in. Rows, rounds or U-shape? 📐\n\n#thebigbusinesschronicles #seasontwo #floorplan #lasvegas #comedy",
     "The Big Business Chronicles EP. 50: Unc is reading it upside down. 📐\n\n#thebigbusinesschronicles #floorplan #family #comedy",
     "The Big Business Chronicles EP. 50: three layouts, one inch and a door nobody else saw. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 50: The Floor Plan 📐 she was right again #Shorts")),
 "sat": dict(date="2026-11-14",
   images=feed("Hosting Thanksgiving? Here is the seating math.\n\n"
               "Every set is a 6 ft table and 6 chairs for $22, which works out to $3.67 a seated guest. Twelve guests is 2 sets for $44, "
               "twenty-four is 4 sets for $88, thirty-six is 6 sets for $132, and forty-eight is 8 sets for $176. Chairs are $2 each and "
               "round tables are $15. Everything is delivered and picked up across Las Vegas, delivery is quoted with your order, and "
               "full-service setup starts at $265. Message us your date and headcount.\n\n"
               "#LasVegasPartyRentals #ThanksgivingVegas #Friendsgiving #TableAndChairRentals #VegasEvents",
               F + "BB26_PriceList_Sat07.png", F + "BB26_PriceList_Sat07_Story.png"),
   episode=ep("fb_safe/BB_Chronicles_Ep51_TheKidsTable.mp4",
     "the big business chronicles ep. 51: everybody has a seat. dad got the kids' table. 🦃" + H_EP,
     "The Big Business Chronicles EP. 51: Dad sets the big table and the kids' table, Unc sits on Lil Wobbles, and Baby moves himself up. Big table or kids' table? 🦃\n\n#thebigbusinesschronicles #seasontwo #thanksgiving #lasvegas #comedy",
     "The Big Business Chronicles EP. 51: she will not sit at the kids' table. 🦃\n\n#thebigbusinesschronicles #kidstable #thanksgiving #comedy",
     "The Big Business Chronicles EP. 51: two tables for Thanksgiving, one seat left, and it is at the kids' table. Next episode tomorrow.\n\n#thebigbusinesschronicles #thanksgiving #comedy",
     "EP. 51: The Kids' Table 🦃 dad got demoted #Shorts")),
 "sun": dict(date="2026-11-15",
   images=feed("Only three Saturdays before Christmas: Dec 5, 12 and 19. 🎄\n\n"
               "Hosting the family or the office this year? 36 guests is 6 tables and 36 chairs for $132, 60 guests is 10 tables "
               "and 60 chairs for $220, and full-service setup starts at $265. Everything is delivered and picked up across Las "
               "Vegas, with delivery quoted with your order. Message us your date and headcount.\n\n"
               "#LasVegasHolidayParty #ChristmasParty #VegasEvents #PartyRentals #HolidayParty",
               F + "BB26_Holiday_Sun15.png", F + "BB26_Holiday_Sun15_Story.png"),
   episode=ep("fb_safe/BB_Chronicles_Ep52_TheCalendar.mp4",
     "the big business chronicles ep. 52: dec 19. locked in. 📅" + H_EP,
     "The Big Business Chronicles EP. 52: Dad circles Dec 19 in one stroke, Mrs. Never Wrong circles the 5th and 12th, and Tyler pops out of the 25th. Which Saturday is yours? 📅\n\n#thebigbusinesschronicles #seasontwo #holidayparty #lasvegas #comedy",
     "The Big Business Chronicles EP. 52: where did he even come from? 📅\n\n#thebigbusinesschronicles #december #family #comedy",
     "The Big Business Chronicles EP. 52: three Saturdays, one circled date and an intern in the advent calendar. Next episode tomorrow.\n\n#thebigbusinesschronicles #family #comedy",
     "EP. 52: The Calendar 📅 dec 19 locked in #Shorts")),
}

def post(inp, label):
    d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
    good = res.get("__typename") == "PostActionSuccess"
    print("OK  " if good else "FAIL", label, res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
    return good

def run(day):
    c = DAYS[day]; D1, D8 = c["date"] + "T13:00:00-08:00", c["date"] + "T20:00:00-08:00"; ok = n = 0
    base = lambda ch, text, due: {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due, "schedulingType": "automatic"}
    for ch, text, imgs, md in c.get("images", []):
        n += 1; ok += post(dict(base(ch, text, D1), assets=[{"image": {"url": u}} for u in imgs], metadata=md), f"{day} {ch} 1pm {imgs[0].rsplit('/',1)[-1]}")
    if "carousel" in c:
        imgs, text = c["carousel"]
        for ch, md in (("fb", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
                       ("ig", {"instagram": {"type": "post", "shouldShareToFeed": True, "firstComment": IG_PIN}})):
            n += 1; ok += post(dict(base(ch, text, D1), assets=[{"image": {"url": u}} for u in imgs], metadata=md), f"{day} {ch} 1pm carousel x{len(imgs)}")
    if "gtt" in c:
        f, text = c["gtt"]
        n += 1; ok += post(dict(base("tt", text, D1), assets=[{"video": {"url": V + f}}], metadata={"tiktok": {"isAiGenerated": True}}), f"{day} tt 1pm {f}")
    E, vids = c["episode"]
    for ch, text, extra in vids:
        inp = dict(base(ch, text, D8), assets=[{"video": {"url": RAW + E}}])
        if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
        elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
        n += 1; ok += post(inp, f"{day} {ch} 8pm {E.rsplit('/',1)[-1]}")
    print(f"{day}: {ok}/{n} queued")

if __name__ == "__main__":
    days = [a for a in sys.argv[1:] if a in DAYS]
    if not days: sys.exit("name the approved days, e.g. python3 queue_week_nov09.py mon")
    for d in days: run(d)
