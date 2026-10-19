"""Queue MONDAY OCT 19 cards at the revised standing times (first merged-format day):
morning card 9am · venue 12pm · PRICE IT 1pm (FB+IG+TT pad) · referral 2pm · espanol 3pm ·
countdown 4pm. Videos (trend 5pm, pink 6pm, EP28 8pm) queue separately once rendered."""
import json, subprocess, time

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "tt": "6ab81da7ea19ca0bdef9436e"}
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

def create(channel, due, text, assets, first_comment=False, spanish=False):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": due, "assets": assets}
    if channel == "fb":
        md = {"type": "post"}
        if first_comment: md["firstComment"] = FC_FB_ES if spanish else FC_FB
        inp["metadata"] = {"facebook": md}
    elif channel == "ig":
        md = {"type": "post", "shouldShareToFeed": True}
        if first_comment: md["firstComment"] = FC_IG_ES if spanish else FC_IG
        inp["metadata"] = {"instagram": md}
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

def frames(stem, n):
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week8/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def one(path):
    return [{"image": {"url": RAW + path}}]

D = "2026-10-19T{:02d}:00:00-07:00"

LANES = [
 (9, "BB_Caro_Mon19_SpaceMath", 6, False,
  "Your living room is smaller than you think.",
  "Twenty yeses in the group chat and one couch: about ten square feet per seated guest is the math nobody does. We size the table and chair order to your space, and if the math says no, our private venue seats 40. Comment QUOTE and we will DM you a price today.",
  "#partytips #partyplanning #lasvegas #partyrentals #eventplanning"),
 (14, "BB_Caro_Mon19_NailTech", 5, False,
  "Your nail tech hears every party plan first.",
  "Baby showers, birthdays, quinces: two hours of acrylic is two hours of party intel. If you do nails, or you know who does yours, send the party people our way and collect up to $100 after their event wraps. Send this to your nail tech. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#nailtech #referral #lasvegas #sidehustle #partyrentals"),
 (15, "BB_Caro_Mon19_Diciembre", 5, True,
  "Diciembre se reserva en octubre.",
  "Posadas, cenas de empresa, año nuevo: los sábados de diciembre se apartan primero. Mesas, sillas y manteles entregados, instalados y recogidos en todo Las Vegas, y nuestro salón privado recibe 40 sentados y 80 de pie. Aparta tu fecha hoy. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
  "#diciembre #posadas #lasvegas #rentademesas #fiestas"),
 (16, "BB_Caro_Mon19_12Nights", 4, False,
  "12 nights. Your house or theirs?",
  "Somebody in your circle is hosting Halloween, and the one with the tables and chairs wins the argument. Halloween is a Saturday this year. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]

VENUE = ("BB_Venue_Mon19_HolidayDate",
 "Your holiday party has a date. Claim it.",
 "The December Saturdays are already moving. Private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE for open December dates, or chat with us at bigbusinesspartyrentals.com.",
 "#holidayparty #december #lasvegas #venue #eventspace")

PRICEIT = ("BB_PriceIt_HoopLounge",
 "How much would you pay for this setup?",
 "Hoops watch party at ballroom scale: six rounds of ten, a wall-sized screen and a stadium snack spread. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the room underneath? That is us.",
 "#priceit #watchparty #basketball #lasvegas #partyrentals")

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for hour, stem, n, es, opening, para, tags in LANES:
        due = D.format(hour)
        text = cap(opening, para, tags)
        run(f"FB  {stem}", create("fb", due, text, frames(stem, n), first_comment=True, spanish=es))
        run(f"IGp {stem}", create("ig", due, text, frames(stem, n), first_comment=True, spanish=es))

    vstem, vo, vp, vt = VENUE
    due = D.format(12)
    vtext = cap(vo, vp, vt)
    va = one(f"big-business-rentals/daily-posts/week8/{vstem}.png")
    run(f"FB  {vstem}", create("fb", due, vtext, va, first_comment=True))
    run(f"IGp {vstem}", create("ig", due, vtext, va, first_comment=True))

    pstem, po, pp, pt = PRICEIT
    due = D.format(13)
    ptext = cap(po, pp, pt)
    run(f"FB  {pstem}", create("fb", due, ptext, one(f"big-business-rentals/inspo/{pstem}.png"), first_comment=True))
    run(f"IGp {pstem}", create("ig", due, ptext, one(f"big-business-rentals/inspo/{pstem}.png"), first_comment=True))
    run(f"TT  {pstem}", create("tt", due, ptext, one(f"big-business-rentals/story9/{pstem}.png")))
    print(f"done: {ok} OK, {fail} failed")
