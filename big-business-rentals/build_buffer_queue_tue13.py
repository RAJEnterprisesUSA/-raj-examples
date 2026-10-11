"""Queue MONDAY OCT 12 at the standing times (Vegas local, -07:00).

Business 10am + venue 12pm = the two REAL FOOTAGE cinematic reels (FB reel +
IG reel + YouTube; NOT TikTok, the 4-post cap holds). TikTok carousel pick =
LinenMath tip (story9 frames; data-backed, logged). EN ESPANOL 3pm Posada
with Spanish cross-linked firstComments. Gag/pink/EP22 queued separately
once rendered (build_buffer_queue_mon12_videos.py).
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
FC_FB_ES = ("¿Planeando una fiesta? Síguenos también en Instagram: "
            "montajes reales y fechas disponibles.\n"
            "instagram.com/bigbusiness_rentals_events")
FC_IG_ES = ("Sigue a @bigbusiness_rentals_events para ver montajes reales y fechas "
            "disponibles. También estamos en Facebook: "
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
           first_comment=False, spanish=False):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": due, "assets": assets}
    if channel == "fb":
        md = {"type": ptype}
        if first_comment and ptype in ("post", "reel"):
            md["firstComment"] = FC_FB_ES if spanish else FC_FB
        inp["metadata"] = {"facebook": md}
    elif channel == "ig":
        md = {"type": ptype, "shouldShareToFeed": ptype != "story"}
        if first_comment and ptype in ("post", "reel"):
            md["firstComment"] = FC_IG_ES if spanish else FC_IG
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

def feed_frames(stem, n, week="week6"):
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/{week}/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def story_frames(stem, n):
    return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def vid(p): return [{"video": {"url": RAW + p}}]

D = "2026-10-13T{:02d}:00:00-07:00"

CARD_LANES = [
 (8, "BB_Caro_Tue_CakeMath", 6,
  "How much cake does a party eat?",
  "Everybody wants a slice, nobody wants seven leftover pounds. Swipe for the two numbers that get the order right, then send this to whoever always over-orders.",
  "#partytips #cakemath #partyplanning #lasvegas #partyrentals"),
 (14, "BB_Caro_Tue_WorkPlug", 5,
  "Every job has a party planner.",
  "Somebody at work is about to get handed the holiday party, and they need tables, chairs and a room. Send them our way, have them drop your name, and you collect up to $100 after their event wraps. Send this to your work bestie. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #lasvegas #workbestie #partyrentals #sidehustle"),
 (16, "BB_Caro_Tue_18Nights", 4,
  "18 nights. Two Saturdays. Then the big one.",
  "The 17th, the 24th, then Halloween itself. Every party between now and then needs chairs, and most of them call this week. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]
TIKTOK_PICK = "BB_Caro_Tue_18Nights"
TIKTOK_PICK_N = 4

VENUE_CARD = (12, "BB_Venue_Tue_Company",
 cap("The company party does not need a casino budget.",
     "December and F1 season are already filling the calendar. Our private venue seats 40 and holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE for open dates. Questions? The chat on bigbusinesspartyrentals.com answers right away.",
     "#companyparty #lasvegas #corporateevents #holidayparty #partyvenue"))

FOOTAGE_REELS = [
 (10, "big-business-rentals/user-videos/BB_Real_FunStuff.mp4",
  cap("Tables. Chairs. And then this.",
      "Straight off a real job: the ball pit, the walk outside, and the moment you see the whole thing. Real setups all over Las Vegas. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #bouncehouse #kidsparty #vegas"),
  "Tables. Chairs. And then this. #Shorts",
  "Straight off a real job in Las Vegas: the ball pit, the walk outside, the reveal. Real party rentals, delivered, set up, picked up.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PartyRentals #BounceHouse #LasVegas #KidsParty"),
]

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_HalloweenYard.png",
 cap("How much would you pay for this setup?",
     "Halloween dinner under the moon: three long tables of twelve, jack-o-lanterns down every runner, purple uplights and room left to dance. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the setup underneath it? That is us.",
     "#priceit #halloweenparty #lasvegas #partyrentals #spookyseason"))

ESPANOL = (15, "BB_Caro_Tue_ElVenue", 5,
 cap("\u00bfD\u00f3nde va a ser la fiesta?",
     "En tu sala no caben 60 personas, lo sabemos. Nuestro sal\u00f3n privado recibe 40 personas sentadas y 80 de pie, 3 horas por $625 o 4 horas por $800, con mesas, sillas e instalaci\u00f3n incluidas. Perfecto para cumplea\u00f1os, bautizos y posadas. Env\u00eda esto a quien anda buscando sal\u00f3n. \u00bfPreguntas? Escr\u00edbenos al chat de bigbusinesspartyrentals.com.",
     "#salondeeventos #lasvegas #fiestas #quincea\u00f1era #posadas"))

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

    hour, stem, text = VENUE_CARD
    due = D.format(hour)
    va = [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week6/{stem}.png"}}]
    run(f"FB  {stem}", create("fb", due, text, va, "post", first_comment=True))
    run(f"IGp {stem}", create("ig", due, text, va, "post", first_comment=True))

    for hour, path, text, yt_title, yt_text in FOOTAGE_REELS:
        due = D.format(hour)
        run(f"FB  {path.rsplit('/',1)[1]}", create("fb", due, text, vid(path), "reel", first_comment=True))
        run(f"IG  {path.rsplit('/',1)[1]}", create("ig", due, text, vid(path), "reel", first_comment=True))
        run(f"YT  {path.rsplit('/',1)[1]}", create("yt", due, yt_text, vid(path),
                                                   yt_title=yt_title, yt_cat="22"))

    hour, img_path, text = PRICEIT
    due = D.format(hour)
    pi_assets = [{"image": {"url": RAW + img_path}}]
    run("FB  PriceIt", create("fb", due, text, pi_assets, "post", first_comment=True))
    run("IGp PriceIt", create("ig", due, text, pi_assets, "post", first_comment=True))

    hour, stem, n, text = ESPANOL
    due = D.format(hour)
    run(f"FB  {stem}", create("fb", due, text, feed_frames(stem, n), "post",
                              first_comment=True, spanish=True))
    run(f"IGp {stem}", create("ig", due, text, feed_frames(stem, n), "post",
                              first_comment=True, spanish=True))
    print(f"done: {ok} OK, {fail} failed")
