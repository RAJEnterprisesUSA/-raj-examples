"""Queue SATURDAY OCT 24 cards. Run AFTER push."""
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

D = "2026-10-24T{:02d}:00:00-07:00"

LANES = [
 (9, "BB_Caro_Sat24_November", 5, False,
  "November is the new December.",
  "Friendsgiving, work parties and big race weekend guests: November fills quietly while everybody stares at December. A table and six chairs is $22, delivered and picked up, with full-service setup and breakdown from $265. Lock your November date before the holiday rush starts. Comment QUOTE with your date.",
  "#friendsgiving #holidayparty #lasvegas #november #partyrentals"),
 (14, "BB_Caro_Sat24_Teacher", 5, False,
  "Teachers know every party first.",
  "Birthday invites in the backpacks, quinces in the group chat, thirty families per classroom. When a family you send books rentals or the venue and drops your name, you collect up to $100 after their event wraps. Send this to your favorite teacher. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#teacher #referral #lasvegas #teachersofinstagram #sidehustle"),
 (15, "BB_Caro_Sat24_RecomiendaES", 5, True,
  "Recomienda y gana hasta $100.",
  "En tu familia siempre hay una fiesta: quinceañeras, bautizos, posadas, cumpleaños. Cuando alguien que tú mandas reserva mesas, sillas o el salón y da tu nombre, tú cobras hasta $100 al terminar su evento, sin límite de referidos. Envía esto a quien conoce a todo el mundo. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
  "#referidos #ganadinero #lasvegas #fiestas #recomienda"),
 (16, "BB_Caro_Sat24_7Nights", 4, False,
  "7 nights. One week exactly.",
  "Next Saturday, this exact hour, it is Halloween, and the people partying tonight are booking next week before they go home. One week to lock tables, chairs and the room for the finale. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #oneweek #lasvegas #partyrentals"),
]

VENUE = ("BB_Venue_Sat24_The31st",
 "Next Saturday is the 31st.",
 "One week from tonight, the biggest party night of fall. Private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE for Halloween night, or chat with us at bigbusinesspartyrentals.com.",
 "#halloween #venue #lasvegas #halloweenparty #eventspace")

PRICEIT = ("BB_PriceIt_GridironYard",
 "How much would you pay for this setup?",
 "Backyard game day: a big screen on the turf, long silver and black tables for thirty, snack trays down the middle and string lights overhead. Be honest, wrong answers welcome, drop your number below. The screen is the inspo. The tables, the chairs and the layout underneath? That is us.",
 "#priceit #gameday #watchparty #lasvegas #partyrentals")

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
