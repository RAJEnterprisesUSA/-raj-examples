"""Queue THURSDAY OCT 8 at the standing times (Vegas local, -07:00).

Current routing (CLAUDE.md): every card lane runs FB feed post + IG story
(story9 9:16) + IG feed carousel (4:5, firstComment) + TikTok photo carousel
(story9). PRICE IT = FB + IG feed. Videos = FB + IG + TikTok + YouTube.
Feed posts carry the pinned firstComment; stories never do.
Paces requests 3s apart and backs off 90s on RATE_LIMIT.
"""
import json, subprocess, time

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "tt": "6ab81da7ea19ca0bdef9436e", "yt": "6ac2ff576a5c39ccb618d238"}
CONTACT = "\U0001F4DE 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com"
FC_FB = ("If you're planning anything this season, follow the page. "
         "We post real setups, open dates, and what's available before it books up.\n"
         "facebook.com/profile.php?id=61589138907701")
FC_IG = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
         "Booking December now.")

def cap(opening, para, tags):
    return f"{opening}\n\n{para}\n\n{CONTACT}\n\n{tags}"

MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
 ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""

def gql(inp):
    body = json.dumps({"query": MUT, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

def create(channel, due, text, assets, ptype="post", yt_title=None, yt_cat="23",
           first_comment=False):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": due, "assets": assets}
    if channel == "fb":
        md = {"type": ptype}
        if first_comment and ptype in ("post", "reel"): md["firstComment"] = FC_FB
        inp["metadata"] = {"facebook": md}
    elif channel == "ig":
        md = {"type": ptype, "shouldShareToFeed": ptype != "story"}
        if first_comment and ptype in ("post", "reel"): md["firstComment"] = FC_IG
        inp["metadata"] = {"instagram": md}
    elif channel == "yt":
        inp["metadata"] = {"youtube": {"title": yt_title, "madeForKids": False,
                                       "privacy": "public", "categoryId": yt_cat}}
    d = gql(inp)
    if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
        print("  rate limited, 90s backoff"); time.sleep(90); d = gql(inp)
    time.sleep(3)
    try:
        cp = d["data"]["createPost"]
        return ("OK  " if cp["__typename"] == "PostActionSuccess"
                else "FAIL " + json.dumps(d)[:220])
    except Exception:
        return "FAIL " + json.dumps(d)[:220]

def feed_frames(stem, n):
    if n == 1:
        return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week5/{stem}.png"}}]
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week5/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def story_frames(stem, n):
    if n == 1:
        return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}.png"}}]
    return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def vid(p): return [{"video": {"url": RAW + p}}]

D = "2026-10-08T{:02d}:00:00-07:00"

CARD_LANES = [
 # (hour, stem, n, opening, para_feed, para_story, tags)
 (8, "BB_Caro_Thu_TableMath", 6,
  "How many tables does your party need?",
  "Swipe for the ten second math nobody does until the chairs show up. Send this to whoever is hosting next.",
  "Tap through for the ten second math nobody does until the chairs show up. Send this to whoever is hosting next.",
  "#partytips #tablemath #partyplanning #lasvegas #partyrentals"),
 (10, "BB_Caro_Thu_Loaded", 5,
  "Vegas, this weekend is loaded.",
  "Hockey is back tonight, the rodeo is in town and Sunday is football brunch. Swipe to see how one call covers the whole weekend, then comment QUOTE and we will DM you a price today.",
  "Hockey is back tonight, the rodeo is in town and Sunday is football brunch. Tap through to see how one call covers the whole weekend, then comment QUOTE and we will DM you a price today.",
  "#lasvegas #partyrentals #vegasweekend #eventrentals #watchparty"),
 (12, "BB_Venue_Thu_SoldOut", 1,
  "The rodeo sold out. Your afterparty should not.",
  "Our private venue seats 40 and holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE and we will DM you open dates this weekend.",
  "Our private venue seats 40 and holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE and we will DM you open dates this weekend.",
  "#lasvegas #partyvenue #privateevent #rodeoweekend #vegas"),
 (14, "BB_Caro_Thu_WeekendPlug", 5,
  "Everybody is planning something this weekend.",
  "Rodeo crews, watch parties, birthday dinners. Send them our way, have them drop your name, and you collect up to $100 after their event wraps. Send this to the planner of your crew. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "Rodeo crews, watch parties, birthday dinners. Tap through, then send them our way, have them drop your name, and you collect up to $100 after their event wraps. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #lasvegas #sidehustle #partyrentals #weekendplans"),
 (16, "BB_Caro_Thu_23Nights", 4,
  "23 nights till Halloween.",
  "Three weekends left and the Saturday parties are claiming dates first. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "Three weekends left and the Saturday parties are claiming dates first. Tap through, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_HockeyNight.png",
 cap("How much would you pay for this setup?",
     "Hockey is back in Vegas tonight and this fan cave is ready for puck drop. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the room underneath it? That is us.",
     "#priceit #hockeynight #lasvegas #partyrentals #fancave"))

VIDEOS = [
 # (hour, path, fbig_type, yt_cat, caption, yt_title, yt_text)
 (17, "big-business-rentals/halloween/BB_Halloween_Reel_DJBones.mp4", "reel", "23",
  cap("The DJ came highly recommended. \U0001F480",
      "He really felt the music. Then the beat dropped and so did his head. One table, one drop, zero wobble. Send this to the friend who loses it when the beat drops.",
      "#djbones #halloween #funnyreels #lasvegas #partyrentals"),
  "DJ Bones loses his head to the beat \U0001F480 #Shorts",
  "The DJ came highly recommended. Then the beat dropped and so did his head. One table, one drop, zero wobble. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Skeleton #DJ #FunnyShorts #LasVegas #PartyRentals"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_ScreeningExplained.mp4", "story", "22",
  cap("A mammogram takes about 20 minutes, start to finish. \U0001F380",
      "No mystery and no horror story: a tech positions you, compression lasts a few seconds per picture, and you are done in about 20 minutes. Experts recommend starting at age 40, so ask your doctor what schedule fits you. Send this to someone who keeps putting it off. Sources: American Cancer Society, USPSTF.",
      "#breastcancerawareness #pinkoctober #mammogram #earlydetection #lasvegas"),
  "The mammogram, explained in 26 seconds \U0001F380 #Shorts",
  "About 20 minutes, start to finish. No mystery, no horror story. Experts recommend starting at age 40. Ask your doctor what schedule fits you. Sources: American Cancer Society, USPSTF.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #Mammogram #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep18_TheFlyer.mp4", "reel", "23",
  cap("The flyer fell. Twice. Then the intern appeared from nowhere. \U0001F602",
      "EP. 18: Mr. Big Business versus one piece of paper. Four pieces of tape later the record still is not improving. What should Tyler fix next? Best answer gets the next episode credit.",
      "#thebigbusinesschronicles #comedy #funnyreels #lasvegas #partyrentals"),
  "EP. 18: The Flyer \U0001F602 Tyler saves the day #Shorts",
  "THE BIG BUSINESS CHRONICLES: the flyer fell twice, the intern appeared from nowhere, and four pieces of tape did what Mr. Big Business could not. Record: 0 wins, 4 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #Intern #FunnyShorts #LasVegas #PartyRentals"),
]

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for hour, stem, n, opening, pf, ps, tags in CARD_LANES:
        due = D.format(hour)
        run(f"FB  {stem}", create("fb", due, cap(opening, pf, tags), feed_frames(stem, n),
                                  "post", first_comment=True))
        run(f"IGs {stem}", create("ig", due, cap(opening, ps, tags), story_frames(stem, n), "story"))
        run(f"IGp {stem}", create("ig", due, cap(opening, pf, tags), feed_frames(stem, n),
                                  "post", first_comment=True))
        run(f"TT  {stem}", create("tt", due, cap(opening, pf, tags), story_frames(stem, n)))

    hour, img_path, text = PRICEIT
    due = D.format(hour)
    pi_assets = [{"image": {"url": RAW + img_path}}]
    run("FB  PriceIt", create("fb", due, text, pi_assets, "post", first_comment=True))
    run("IGp PriceIt", create("ig", due, text, pi_assets, "post", first_comment=True))

    for hour, path, ptype, yt_cat, text, yt_title, yt_text in VIDEOS:
        due = D.format(hour)
        run(f"FB  {path.rsplit('/',1)[1]}", create("fb", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"IG  {path.rsplit('/',1)[1]}", create("ig", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"TT  {path.rsplit('/',1)[1]}", create("tt", due, text, vid(path)))
        run(f"YT  {path.rsplit('/',1)[1]}", create("yt", due, yt_text, vid(path),
                                                   yt_title=yt_title, yt_cat=yt_cat))
    print(f"done: {ok} OK, {fail} failed")
