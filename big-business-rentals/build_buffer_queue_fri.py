"""Queue FRIDAY OCT 9 at the standing times (Vegas local, -07:00).

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
    return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def vid(p): return [{"video": {"url": RAW + p}}]

D = "2026-10-09T{:02d}:00:00-07:00"

CARD_LANES = [
 (8, "BB_Caro_Fri_ChairMath", 6,
  "How many chairs do you actually need?",
  "Swipe for the two rules that save every host. Questions? The chat on bigbusinesspartyrentals.com answers right away. Send this to whoever is hosting next.",
  "#partytips #chairmath #partyplanning #lasvegas #partyrentals"),
 (10, "BB_Caro_Fri_Scramble", 5,
  "The party is tomorrow and there are no tables yet.",
  "It happens every Friday in Vegas. One call fixes it: tables, chairs and linens delivered, set up and picked up around your schedule. Skip the wait, chat with us at bigbusinesspartyrentals.com, or comment QUOTE and we will DM you a price today.",
  "#partyrentals #lasvegas #lastminuteparty #eventrentals #vegas"),
 (12, "BB_Venue_Fri_After", 1,
  "Where is everybody going after?",
  "The whole city is out tonight. Our private venue seats 40 and holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE and we will DM you open dates this weekend.",
  "#lasvegas #partyvenue #afterparty #privateevent #vegas"),
 (14, "BB_Caro_Fri_FindersFee", 5,
  "Talking about parties pays now.",
  "Somebody out tonight is already planning their next event. Send them our way, have them drop your name, and you collect up to $100 after their event wraps. Send this to the friend who knows everybody. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #lasvegas #findersfee #partyrentals #sidehustle"),
 (16, "BB_Caro_Fri_22Nights", 4,
  "4 Saturdays left. One is Halloween.",
  "22 nights out and the good dates go first. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]
TIKTOK_PICK = "BB_Caro_Fri_22Nights"   # one carousel per day on TikTok
TIKTOK_PICK_N = 4

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_RodeoNight.png",
 cap("How much would you pay for this setup?",
     "Rodeo weekend calls for a backyard that matches the energy: hay bales, lanterns and long tables under the desert sunset. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the setup underneath it? That is us.",
     "#priceit #rodeoweekend #lasvegas #partyrentals #westernparty"))

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Halloween_Reel_TableclothGhost.mp4", "reel", "23",
  cap("The tablecloth would not stay still. \U0001F47B",
      "Easy job, they said. Then it started gliding. Turns out he works here, and honestly the table has never looked better. Send this to whoever believes in ghosts.",
      "#tableclothghost #halloween #funnyreels #lasvegas #partyrentals"),
  "The tablecloth would not stay still \U0001F47B #Shorts",
  "Easy job, they said. Then the tablecloth started gliding. Turns out he works here. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Ghost #FunnyShorts #LasVegas #PartyRentals"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_KnowYourNormal.mp4", "story", "22",
  cap("Many breast cancers are found by women who notice a change themselves. \U0001F380",
      "Know your normal: how things usually look and feel and what changes with your cycle, so anything new stands out fast. A change does not mean cancer, it means make the call. Check once a month, same week every month. Send this to a woman you love. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #knowyournormal #earlydetection #lasvegas"),
  "Know your normal. It matters. \U0001F380 #Shorts",
  "Many breast cancers are found by women who notice a change themselves. Know your normal so anything new stands out fast. A change means make the call. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #KnowYourNormal #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep19_TheAudition.mp4", "reel", "23",
  cap("He held seating auditions. One chair lied on the resume. \U0001F602",
      "EP. 19: three solid chairs, one red imposter, and a final verdict from the committee of one. Wobbles stays, as decoration. What costume should Wobbles wear? Best answer gets the next episode credit.",
      "#thebigbusinesschronicles #lilwobbles #comedy #lasvegas #funnyreels"),
  "EP. 19: The Audition \U0001F602 one chair lied on the resume #Shorts",
  "THE BIG BUSINESS CHRONICLES: seating auditions for the Halloween party. Three solid chairs, one red imposter, and the committee has spoken. Record: 0 wins, 5 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
