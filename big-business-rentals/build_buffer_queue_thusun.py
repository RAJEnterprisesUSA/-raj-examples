"""Queue THURSDAY OCT 15 through SUNDAY OCT 18 card sets at the standing times
(Vegas local, -07:00). Cards = FB feed post + IG feed carousel with cross-linked
firstComments. PRICE IT 1pm = FB + IG (4:5 card) + TikTok (9:16 story9 pad, same
caption) per the Oct 11 TikTok rule. Espanol 3pm with Spanish firstComments.
Videos (gag 5pm, pink 6pm, episode 8pm) queue separately once rendered.
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

def create(channel, due, text, assets, ptype="post", first_comment=False, spanish=False):
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
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week7/{stem}_{i:02d}.png"}}
            for i in range(1, n+1)]

def one(path):
    return [{"image": {"url": RAW + path}}]

# Per day: (date, card_lanes, venue, priceit, espanol)
# card lane = (hour, stem, n, opening, para, tags)
DAYS = [
 ("2026-10-15",
  [(8, "BB_Caro_Thu_TimelineMath", 6,
    "Your party has a secret deadline.",
    "Three dates decide every party: invites out three weeks ahead, final headcount 72 hours out, and nothing left for the morning of. Swipe for the timeline, then send this to somebody planning a November party.",
    "#partyplanning #partytips #lasvegas #partyrentals #eventplanning"),
   (10, "BB_Caro_Thu_NotAProject", 5,
    "Renting tables is not a project.",
    "It is one message: date, guest count, address. We price it fast, it shows up, we set it up and we pick it up. Comment QUOTE and we will DM you a price today. Questions after hours? The chat on bigbusinesspartyrentals.com answers right away.",
    "#partyrentals #lasvegas #tablesandchairs #eventrentals #vegas"),
   (14, "BB_Caro_Thu_Barber", 5,
    "Your barber hears about every party first.",
    "Every birthday, baby shower and reunion gets announced in that chair. If you cut hair, do nails, or just hear everything, send the party people our way and collect up to $100 after their event wraps. Send this to the chair that hears everything. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
    "#referral #barber #lasvegas #sidehustle #partyrentals"),
   (16, "BB_Caro_Thu_16Nights", 4,
    "16 nights out and the group chat is still deciding.",
    "Somebody has to pick the house, and whoever picks the house needs tables, chairs and a plan. Halloween is a Saturday this year. Swipe, then comment SPOOKY and we will DM you open October dates.",
    "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals")],
  ("BB_Venue_Thu_WinterBday",
   "Winter birthdays deserve a real room.",
   "Too cold for the backyard, too many people for the living room. Our private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.",
   "#venue #birthdayparty #lasvegas #eventspace #winterbirthday"),
  ("BB_PriceIt_QuinceBallroom",
   "How much would you pay for this setup?",
   "Quinceañera ballroom: blush and gold, eight tables of ten and a dance floor ready for the vals. Be honest, wrong answers welcome, drop your number below. The decor is the inspo. The tables, the chairs and the room underneath it? That is us.",
   "#priceit #quinceanera #lasvegas #partyrentals #ballroom"),
  ("BB_Caro_Thu_Referidos", 5,
   "¿Conoces a alguien que hace fiestas?",
   "En cada familia hay alguien que organiza todo. Si esa persona eres tú, o la conoces, gana hasta $100 por cada reserva de mesas, sillas o el salón cuando dan tu nombre. Sin límite de referidos, se paga al terminar el evento. Envía esto a la tía que organiza todo. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
   "#referidos #fiestas #lasvegas #rentademesas #dineroextra")),
 ("2026-10-16",
  [(8, "BB_Caro_Fri_RsvpMath", 6,
    "Every guest list tells a little lie.",
    "People say yes in October and go quiet in November. Set for every yes, add two seats past your count, and let the rentals flex with the final number 72 hours out. Swipe for the math, then send this to whoever is still waiting on RSVPs.",
    "#partytips #rsvp #partyplanning #lasvegas #partyrentals"),
   (10, "BB_Caro_Fri_48Hours", 5,
    "The weekend is 48 hours away.",
    "Saturday party, Friday panic? One call today locks tables, chairs and linens for the weekend, delivered, set up and picked up after. You never load a truck. Comment QUOTE and we will DM you a weekend price.",
    "#weekend #partyrentals #lasvegas #saturdayparty #eventrentals"),
   (14, "BB_Caro_Fri_Payday", 5,
    "Today is payday. Here is a second one.",
    "The first check came from work. The second comes from knowing people: send party people our way, have them drop your name, and collect up to $100 after their event wraps. Send this to somebody who knows everybody. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
    "#payday #referral #lasvegas #sidehustle #partyrentals"),
   (16, "BB_Caro_Fri_15Nights", 4,
    "15 nights. Candy is not the plan.",
    "Candy is for the kids at the door, the party is for everybody after, and the setup books before the costume does. Halloween is a Saturday this year. Swipe, then comment SPOOKY and we will DM you open October dates.",
    "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals")],
  ("BB_Venue_Fri_SplitMath",
   "$625 split 25 ways is $25 each.",
   "Three hours in a private venue with tables, chairs and setup included, for less than one night out on the Strip. Seats 40, holds 80 standing, 4 hours for $800. Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.",
   "#venue #lasvegas #partyvenue #birthdayparty #eventspace"),
  ("BB_PriceIt_RooftopGlow",
   "How much would you pay for this setup?",
   "Rooftop glow party: black linens, LED runners, a lit bar and the Vegas skyline doing the decorating. Be honest, wrong answers welcome, drop your number below. The lights are the inspo. The tables, the chairs and the setup underneath? That is us.",
   "#priceit #rooftopparty #lasvegas #partyrentals #vegasnights"),
  ("BB_Caro_Fri_HalloweenES", 5,
   "Halloween cae en sábado este año.",
   "Fiesta grande garantizada, y las fechas buenas de octubre ya se están apartando. Mesas, sillas y manteles entregados e instalados en todo Las Vegas, también el 31. Y si necesitas lugar, el salón privado recibe 40 sentados y 80 de pie. Envía esto al grupo que todavía no decide dónde es la fiesta. Escríbenos al chat de bigbusinesspartyrentals.com.",
   "#halloween #fiestas #lasvegas #rentademesas #octubre")),
 ("2026-10-17",
  [(8, "BB_Caro_Sat_WeatherMath", 6,
    "Vegas October has two seasons a day.",
    "Warm at three, cold by eight, sunset around six. Plan for the colder number, light the party before dark, and keep a plan B room in your pocket. Swipe for the math, then send this to whoever is planning a backyard party.",
    "#vegasweather #partytips #backyardparty #lasvegas #partyrentals"),
   (10, "BB_Caro_Sat_BeforeBreakfast", 5,
    "The party showed up before breakfast.",
    "Morning delivery means your Saturday starts finished: tables down, chairs set, truck gone. Delivery, setup and pickup are part of every order. Your only job is opening the door. Comment QUOTE and we will DM you a price today.",
    "#partyrentals #delivery #lasvegas #saturday #eventsetup"),
   (14, "BB_Caro_Sat_Tonight", 5,
    "Tonight at the party, listen close.",
    "Somebody will say it: we should do this for my birthday. That sentence is worth up to $100 when you send them our way and they drop your name. Paid after their event wraps, no limit on referrals. Send this to the friend who said it. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
    "#referral #saturdaynight #lasvegas #sidehustle #partyrentals"),
   (16, "BB_Caro_Sat_14Nights", 4,
    "Two weeks. Exactly.",
    "Fourteen nights from tonight it is Halloween night, a Saturday, the biggest party night of the fall. Lock tables, chairs and the room before the rush does it for you. Comment SPOOKY and we will DM you open October dates.",
    "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals")],
  ("BB_Venue_Sat_TwoSaturdays",
   "Two Saturdays left in October.",
   "The 24th and the 31st. One of them should be your party. Private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE and we will DM you which dates are still open. Questions? The chat on bigbusinesspartyrentals.com answers right away.",
   "#october #venue #lasvegas #halloweenparty #eventspace"),
  ("BB_PriceIt_KidsCartoon",
   "How much would you pay for this setup?",
   "Kids birthday at ballroom scale: rainbow tables, lanterns, a dessert spread and a dance floor with confetti already down. Be honest, wrong answers welcome, drop your number below. The decorations are the inspo. The tables, the chairs and the room underneath? That is us.",
   "#priceit #kidsparty #birthdayparty #lasvegas #partyrentals"),
  ("BB_Caro_Sat_Servicios", 5,
   "La comida está. ¿Dónde se sientan?",
   "La música está, los tamales están, y a última hora siempre faltan las mesas, las sillas y los manteles. Nosotros los entregamos, los instalamos y los recogemos en todo Las Vegas, con manteles del tamaño correcto para cada mesa. Envía esto a quien organiza la próxima fiesta. ¿Preguntas? Escríbenos al chat de bigbusinesspartyrentals.com.",
   "#fiestas #rentademesas #lasvegas #sillas #manteles")),
 ("2026-10-18",
  [(8, "BB_Caro_Sun_GoldenHour", 6,
    "Your party photos have a deadline.",
    "The hour before sunset is golden hour: cake, toasts and the group photo belong there. After dark, light the tables, not the fence. Swipe for the math, then send this to the friend with the good phone.",
    "#goldenhour #partyphotos #partytips #lasvegas #partyrentals"),
   (10, "BB_Caro_Sun_FootballSeats", 5,
    "Football Sunday needs more seats.",
    "The crew outgrew the couch three Sundays ago. Tables for the spread, chairs by the dozen, delivered and picked back up so the living room goes back to normal Monday. Skip the wait, chat with us at bigbusinesspartyrentals.com.",
    "#footballsunday #watchparty #lasvegas #partyrentals #gameday"),
   (14, "BB_Caro_Sun_ChatAdmin", 5,
    "Every group chat has an admin.",
    "Makes the plan, books the thing, collects the money, never gets paid. Fix that: point the chat's next party our way, have them drop your name, and collect up to $100 after the event wraps. Send this to the chat, the admin knows who they are. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
    "#groupchat #referral #lasvegas #sidehustle #partyrentals"),
   (16, "BB_Caro_Sun_13Nights", 4,
    "13 nights left. Fitting.",
    "The spookiest number on the calendar and the last comfortable week to book: the closer it gets, the fewer dates and chairs are left. Comment SPOOKY and we will DM you open October dates.",
    "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals")],
  ("BB_Venue_Sun_Friendsgiving",
   "Friendsgiving needs a bigger table.",
   "November weekends book first and they are already going. Private venue seats 40, holds 80 standing: 3 hours $625 or 4 hours $800 with tables, chairs and setup included. Comment VENUE for open November dates, or chat with us at bigbusinesspartyrentals.com.",
   "#friendsgiving #november #lasvegas #venue #eventspace"),
  ("BB_PriceIt_FallHarvest",
   "How much would you pay for this setup?",
   "Fall harvest dinner under the lights: three long tables, pumpkins and plaid down every runner, and a desert sunset doing the backdrop. Be honest, wrong answers welcome, drop your number below. The decor is the inspo. The tables, the chairs and the setup underneath? That is us.",
   "#priceit #falldinner #friendsgiving #lasvegas #partyrentals"),
  ("BB_Caro_Sun_ElVals", 5,
   "El vals necesita pista.",
   "La sala de la casa no alcanza para el vals, ni para la corte, ni para las quince mesas de la familia. Nuestro salón privado recibe 40 sentados y 80 de pie: 3 horas $625 o 4 horas $800 con mesas, sillas e instalación. También rentamos todo para tu jardín o salón. Envía esto a una familia que está planeando una quince.",
   "#quinceanera #quince #lasvegas #salondeeventos #fiestas")),
]

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for date, lanes, venue, priceit, espanol in DAYS:
        print("=== " + date)
        D = date + "T{:02d}:00:00-07:00"
        for hour, stem, n, opening, para, tags in lanes:
            due = D.format(hour)
            text = cap(opening, para, tags)
            run(f"FB  {stem}", create("fb", due, text, frames(stem, n), first_comment=True))
            run(f"IGp {stem}", create("ig", due, text, frames(stem, n), first_comment=True))

        vstem, vopen, vpara, vtags = venue
        due = D.format(12)
        vtext = cap(vopen, vpara, vtags)
        vassets = one(f"big-business-rentals/daily-posts/week7/{vstem}.png")
        run(f"FB  {vstem}", create("fb", due, vtext, vassets, first_comment=True))
        run(f"IGp {vstem}", create("ig", due, vtext, vassets, first_comment=True))

        pstem, popen, ppara, ptags = priceit
        due = D.format(13)
        ptext = cap(popen, ppara, ptags)
        run(f"FB  {pstem}", create("fb", due, ptext, one(f"big-business-rentals/inspo/{pstem}.png"), first_comment=True))
        run(f"IGp {pstem}", create("ig", due, ptext, one(f"big-business-rentals/inspo/{pstem}.png"), first_comment=True))
        run(f"TT  {pstem}", create("tt", due, ptext, one(f"big-business-rentals/story9/{pstem}.png")))

        estem, en, eopen, epara, etags = espanol
        due = D.format(15)
        etext = cap(eopen, epara, etags)
        run(f"FB  {estem}", create("fb", due, etext, frames(estem, en), first_comment=True, spanish=True))
        run(f"IGp {estem}", create("ig", due, etext, frames(estem, en), first_comment=True, spanish=True))
    print(f"done: {ok} OK, {fail} failed")
