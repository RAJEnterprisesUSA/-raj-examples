"""Queue SUNDAY OCT 11 cards (queued morning-of; tip slot moved 8am -> 9am).

Routing: card lanes = FB feed post + IG feed carousel (cross-linked
firstComments). TikTok gets exactly ONE card carousel (today: GameDay
business, story9 frames; pick rotation Fri countdown / Sat tip / Sun
business). PRICE IT = FB + IG feed (SunBrunch, freshly generated per the
Oct 10 never-repeat rule). EN ESPANOL 3pm = Quince carousel, FB + IG feed,
Spanish cross-linked firstComments. Videos queued separately once rendered.
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

def feed_frames(stem, n):
    if n == 1:
        return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week5/{stem}.png"}}]
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week5/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def story_frames(stem, n):
    return [{"image": {"url": RAW + f"big-business-rentals/story9/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

D = "2026-10-11T{:02d}:00:00-07:00"

CARD_LANES = [
 (9, "BB_Caro_Sun_BrunchMath", 6,
  "Hosting the 10am game? Do the brunch math.",
  "Morning guests show up hungry. Swipe for the three numbers that keep the table ahead of them, then send this to whoever is hosting kickoff.",
  "#partytips #brunch #watchparty #lasvegas #partyrentals"),
 (10, "BB_Caro_Sun_GameDay", 5,
  "Your crew is coming at 10am. Is your dining room ready?",
  "The group chat picked your house for the game. Tables, chairs and linens delivered, set up and picked up around your schedule, so you host the win instead of working it. Skip the wait, chat with us at bigbusinesspartyrentals.com, or comment QUOTE and we will DM you a price today.",
  "#gameday #watchparty #lasvegas #partyrentals #vegas"),
 (12, "BB_Venue_Sun_Masquerade", 1,
  "Adults deserve Halloween too.",
  "Halloween lands on a Saturday this year. Masks on, kids at grandma's, and a private venue that seats 40 and holds 80 standing, 3 hours for $625 or 4 hours for $800 with tables, chairs and setup included. Comment VENUE for open October dates. Questions? The chat on bigbusinesspartyrentals.com answers right away.",
  "#halloween #masquerade #lasvegas #partyvenue #adulthalloween"),
 (14, "BB_Caro_Sun_SundayDinner", 5,
  "Every party starts at Sunday dinner.",
  "Somebody at the table today is announcing a baby shower, a birthday or a quince. Send them our way, have them drop your name, and you collect up to $100 after their event wraps. Send this to the family group chat. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#referral #sundaydinner #lasvegas #partyrentals #sidehustle"),
 (16, "BB_Caro_Sun_20Nights", 4,
  "20 nights left. Zero excuses.",
  "Three Saturdays stand between you and Halloween, and the last one is Halloween night itself. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]
TIKTOK_PICK = "BB_Caro_Sun_GameDay"
TIKTOK_PICK_N = 5

PRICEIT = (13, "big-business-rentals/inspo/BB_PriceIt_SunBrunch.png",
 cap("How much would you pay for this setup?",
     "Game day brunch, Vegas style: a big screen in the backyard, waffles on black linens and juice pitchers ready before the 10am kickoff. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the setup underneath it? That is us.",
     "#priceit #gamedaybrunch #lasvegas #partyrentals #watchparty"))

ESPANOL = (15, "BB_Caro_Sun_Quince", 5,
 cap("¿Ya tienen todo para la quinceañera?",
     "La fecha se acerca y las sillas no se rentan solas. Mesas, sillas y manteles entregados, instalados y recogidos por nosotros, en todo Las Vegas. Envía esto a una familia que está planeando su quince. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
     "#quinceañera #lasvegas #fiestaslasvegas #rentadesillas #quinceañeras"))

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

    hour, stem, n, text = ESPANOL
    due = D.format(hour)
    run(f"FB  {stem}", create("fb", due, text, feed_frames(stem, n), "post",
                              first_comment=True, spanish=True))
    run(f"IGp {stem}", create("ig", due, text, feed_frames(stem, n), "post",
                              first_comment=True, spanish=True))
    print(f"done: {ok} OK, {fail} failed")
