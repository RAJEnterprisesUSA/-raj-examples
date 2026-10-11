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

D = "2026-10-12T{:02d}:00:00-07:00"

CARD_LANES = [
 (8, "BB_Caro_Mon_LinenMath", 6,
  "Why do tablecloths never fit?",
  "The one you bought floats at half-mast. Swipe for the two numbers that fix every table, then send this to whoever is still using bed sheets.",
  "#partytips #linens #tablesetting #lasvegas #partyrentals"),
 (14, "BB_Caro_Mon_Contacts", 5,
  "Your contacts list is worth money.",
  "Somebody saved in your phone is planning a party right now. Send them our way, have them drop your name, and you collect up to $100 after their event wraps. Send this to the one who is always planning something. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #lasvegas #sidehustle #partyrentals #vegas"),
 (16, "BB_Caro_Mon_19Nights", 4,
  "19 nights. The costume is not the hard part.",
  "The costume takes an hour. The tables, chairs and party room take one call, if you make it before the rush does. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]
TIKTOK_PICK = "BB_Caro_Mon_LinenMath"
TIKTOK_PICK_N = 6

FOOTAGE_REELS = [
 (10, "big-business-rentals/user-videos/BB_Real_PartyDayFlow.mp4",
  cap("Nobody sees this part.",
      "The wipe-down, the stacks, the straps, the room getting its look. Then the part everybody remembers. Real setups, real parties, all over Las Vegas. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #behindthescenes #eventsetup #vegas"),
  "Nobody sees this part. #Shorts",
  "The wipe-down, the stacks, the straps, the room getting its look. Then the part everybody remembers. Real party rentals in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PartyRentals #BehindTheScenes #LasVegas #Setup"),
 (12, "big-business-rentals/user-videos/BB_Real_VenueWalk.mp4",
  cap("This is the room everybody asks about.",
      "Real walkthrough, no filter: seats 40, holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE and we will DM you open dates. Questions? The chat on bigbusinesspartyrentals.com answers right away.",
      "#lasvegas #partyvenue #venuetour #eventspace #vegas"),
  "The room everybody asks about. #Shorts",
  "Real walkthrough of our private Las Vegas venue: seats 40, holds 80 standing, 3 hours $625, 4 hours $800, tables, chairs and setup included.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #LasVegas #PartyVenue #VenueTour #EventSpace"),
]

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_HolidayGlam.png",
 cap("How much would you pay for this setup?",
     "December dinner party energy: emerald linen, gold chargers, candlelight and the tree glowing in the corner. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the room underneath it? That is us.",
     "#priceit #holidayparty #lasvegas #partyrentals #decemberparty"))

ESPANOL = (15, "BB_Caro_Mon_Posada", 5,
 cap("¿La posada es en tu casa este año?",
     "Diciembre se llena primero y las fechas buenas se apartan desde octubre. Mesas, sillas y manteles entregados, instalados y recogidos en todo Las Vegas, tú pones los tamales. Y si viene mucha gente, nuestro salón privado recibe 40 sentados y 80 de pie. Envía esto a la familia que siempre organiza la posada. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
     "#posada #diciembre #lasvegas #fiestasenfamilia #rentademesas"))

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
