"""Queue WEDNESDAY OCT 21 cards at the standing times. Videos queue separately once rendered."""
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

D = "2026-10-21T{:02d}:00:00-07:00"

LANES = [
 (9, "BB_Caro_Wed21_BudgetMath", 6, False,
  "Seating 48 people costs less than dinner.",
  "Real drop-off prices: folding chairs $2, a 6 ft table with six chairs $22, and eight sets seat 48 guests for $176, delivered and picked up anywhere in Las Vegas. You set up, or full-service setup and breakdown starts at $265. Comment QUOTE with your headcount and we will DM your total today.",
  "#partyrentals #prices #lasvegas #budgetparty #tablesandchairs"),
 (14, "BB_Caro_Wed21_Bartender", 5, False,
  "Bartenders hear the party plans first.",
  "Every round comes with a story about a birthday being planned or a venue being hunted. Send the party people our way, have them drop your name, and collect up to $100 after their event wraps. Send this to your favorite bartender. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
  "#bartender #referral #lasvegas #sidehustle #partyrentals"),
 (15, "BB_Caro_Wed21_Precios", 5, True,
  "¿Cuánto cuesta? Precios reales.",
  "Sin misterio: sillas plegables $2, mesas de 6 pies desde $10, y mesa con seis sillas $22, entregadas y recogidas en todo Las Vegas. ¿Quieres que instalemos y recojamos todo? Servicio completo desde $265, y el salón privado desde $625. Envía esto a quien anda cotizando su fiesta. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
  "#precios #rentademesas #lasvegas #fiestas #sillas"),
 (16, "BB_Caro_Wed21_10Nights", 4, False,
  "10 nights. The rush is here.",
  "This is the week everybody calls at once, and Halloween is a Saturday. Tables, chairs and the room go to whoever calls first. Swipe, then comment SPOOKY and we will DM you open October dates.",
  "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
]

VENUE = ("BB_Venue_Wed21_HalloweenSat",
 "The 31st is a Saturday. Book the room.",
 "A private room beats a crowded bar on the biggest party night of fall. Private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE for Halloween availability, or chat with us at bigbusinesspartyrentals.com.",
 "#halloween #venue #lasvegas #halloweenparty #eventspace")

PRICEIT = ("BB_PriceIt_Masquerade",
 "How much would you pay for this setup?",
 "Midnight masquerade: black satin, candelabras, gold chairs and a dance floor built for an entrance. Be honest, wrong answers welcome, drop your number below. The masks are the inspo. The tables, the chairs and the room underneath? That is us.",
 "#priceit #masquerade #halloween #lasvegas #partyrentals")

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
