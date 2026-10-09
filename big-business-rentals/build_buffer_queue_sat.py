"""Queue SATURDAY OCT 10 at the standing times (Vegas local, -07:00).

Routing (owner revisions Oct 8 night): card lanes = FB feed post + IG feed
carousel only (firstComment on both; NO stories). TikTok gets exactly ONE
card carousel (today: 22 Nights countdown, story9 frames). PRICE IT = FB +
IG feed (RodeoNight). Videos = FB + IG + TikTok + YouTube; pink routes as
story on FB/IG. Paces 3s, 90s backoff on RATE_LIMIT.
"""
import json, subprocess, time

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "tt": "6ab81da7ea19ca0bdef9436e", "yt": "6ac2ff576a5c39ccb618d238"}
CONTACT = "\U0001F4DE 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com"
FC_FB = ("If you're planning anything this season, follow us on Instagram too. "
         "Real setups, open dates, and what's available before it books up.\n"
         "instagram.com/bigbusiness_rentals_events")
FC_IG = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
         "Booking December now. We are on Facebook too: "
         "facebook.com/profile.php?id=61589138907701")

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
    return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def vid(p): return [{"video": {"url": RAW + p}}]

D = "2026-10-10T{:02d}:00:00-07:00"

CARD_LANES = [
 (8, "BB_Caro_Sat_SpaceMath", 6,
  "Will your party actually fit?",
  "Swipe for the planner rule of thumb before the tables arrive. Send this to whoever keeps saying it will fit.",
  "#partytips #spacemath #partyplanning #lasvegas #partyrentals"),
 (10, "BB_Caro_Sat_RecoveryDay", 5,
  "Why does hosting need a recovery day?",
  "You know the host who never sits down at their own party. Zero lifting for you: tables, chairs and linens delivered, set up and picked up by us. Comment QUOTE, or skip the wait and chat with us at bigbusinesspartyrentals.com.",
  "#partyrentals #lasvegas #stressfreehosting #eventrentals #vegas"),
 (12, "BB_Venue_Sat_December", 1,
  "December parties book in October.",
  "Holiday dinners, friendsmas and company parties claim the good dates early. Our private venue seats 40 and holds 80 standing, with setup included. Comment VENUE for open December dates, or chat with us at bigbusinesspartyrentals.com.",
  "#lasvegas #holidayparty #partyvenue #privateevent #friendsmas"),
 (14, "BB_Caro_Sat_WeekendEars", 5,
  "You will hear about three parties this weekend.",
  "A birthday, a baby shower, somebody's holiday plans. Every one needs tables and chairs, so send them our way, have them drop your name, and collect up to $100 after their event wraps. Send this to the one who hears everything first. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #lasvegas #sidehustle #partyrentals #weekendplans"),
 (16, "BB_Caro_Sat_21Nights", 4,
  "Only 3 Saturdays stand between you and Halloween.",
  "21 nights out, and the last Saturday is the big one itself. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]
TIKTOK_PICK = "BB_Caro_Sat_SpaceMath"   # rotates lanes daily; Sat = tip
TIKTOK_PICK_N = 6

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_BabyShower.png",
 cap("How much would you pay for this setup?",
     "Baby shower season is upon us and this room understood the assignment. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the room underneath it? That is us.",
     "#priceit #babyshower #lasvegas #partyrentals #eventdecor"))

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Halloween_Reel_PhotoBooth.mp4", "reel", "23",
  cap("The photo booth's first customers had no cheeks to smile with. \U0001F480",
      "One serious photo. That was the whole request. Three flashes later the keeper is a headshot in the most literal way. Send this to your crew's worst photo-taker.",
      "#photobooth #halloween #funnyreels #lasvegas #partyrentals"),
  "The photo booth's first customers \U0001F480 #Shorts",
  "One serious photo. That was the whole request. Three flashes later, the keeper is a headshot in the most literal way. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Skeleton #PhotoBooth #FunnyShorts #LasVegas #PartyRentals"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_MindMatters.mp4", "story", "22",
  cap("Today is World Mental Health Day, and the fight is not only physical. \U0001F380",
      "A diagnosis is heavy on the mind too, so support like you mean it: listen more than you advise, show up without being asked, and keep inviting her even mid treatment. And if fear of the screening is the wall, bring a friend and make it a lunch date after. Check on somebody today.",
      "#pinkoctober #worldmentalhealthday #breastcancerawareness #checkonsomebody #lasvegas"),
  "Check the body. Mind the mind. \U0001F380 #Shorts",
  "World Mental Health Day meets Pink October: a diagnosis is heavy on the mind too. Listen, show up, keep inviting her. Check on somebody today.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #WorldMentalHealthDay #BreastCancerAwareness #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep20_TheFirstW.mp4", "reel", "23",
  cap("After 19 episodes, it finally happened. \U0001F602",
      "EP. 20: the party candy kept vanishing, Unc got caught in 4K, and the solution was so smart we are not sure what to do with ourselves. Everybody eats, nobody fights. Does this count as a win? Debate below.",
      "#thebigbusinesschronicles #firstwin #comedy #lasvegas #funnyreels"),
  "EP. 20: THE FIRST W \U0001F602 after 19 episodes #Shorts",
  "THE BIG BUSINESS CHRONICLES: the candy kept vanishing, Unc got caught in 4K, and the fix earned the franchise's first win. Record: 1 win, 5 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
]

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for hour, stem, n, opening, para, tags in CARD_LANES:
        due = D.format(hour)
        text = cap(opening, para, tags)
        run(f"FB  {stem}", create("fb", due, text, feed_frames(stem, n), "post", first_comment=True))
        run(f"IGp {stem}", create("ig", due, text, feed_frames(stem, n), "post", first_comment=True))
        if stem == TIKTOK_PICK:
            run(f"TT  {stem}", create("tt", due, text, story_frames(stem, TIKTOK_PICK_N)))

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
