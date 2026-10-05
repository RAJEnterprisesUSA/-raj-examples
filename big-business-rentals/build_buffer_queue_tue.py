import json, subprocess

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "tt": "6ab81da7ea19ca0bdef9436e", "yt": "6ac2ff576a5c39ccb618d238"}
CONTACT = "\U0001F4DE 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com"

def cap(opening, para, tags):
    return f"{opening}\n\n{para}\n\n{CONTACT}\n\n{tags}"

MUT = """
mutation($input: CreatePostInput!){
  createPost(input:$input){
    __typename
    ... on PostActionSuccess { post { id dueAt status } }
    ... on MutationError { message }
  }
}"""

def create(channel, due, text, assets=None, yt_title=None, ptype="post", yt_cat="22"):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": due}
    if assets: inp["assets"] = assets
    if channel == "fb":
        inp["metadata"] = {"facebook": {"type": ptype}}
    elif channel == "ig":
        inp["metadata"] = {"instagram": {"type": ptype, "shouldShareToFeed": ptype != "story"}}
    elif channel == "yt":
        inp["metadata"] = {"youtube": {"title": yt_title, "madeForKids": False,
                                       "privacy": "public", "categoryId": yt_cat}}
    body = json.dumps({"query": MUT, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        cp = d.get("data", {}).get("createPost") or {}
        if cp.get("__typename") == "PostActionSuccess":
            return "OK " + cp["post"]["id"]
        return "FAIL " + json.dumps(d)[:300]
    except Exception:
        return "FAIL raw:" + r.stdout[:200]

def img(p): return {"image": {"url": RAW + p}}
def vid(p): return {"video": {"url": RAW + p}}

D = "2026-10-06T{:02d}:00:00-07:00"

POSTS = [
 ("1 Tip23 DrinkMath", 8, ["fb","ig"], "story", "22",
  cap("How many drinks does a party actually need?",
      "2 per guest in the first hour, 1 more every hour after, and that adds up to 200 drinks for 40 guests over 4 hours. Stock the bar with that number and nobody goes thirsty. You pour, we handle every table, chair and linen under it. Send this to whoever is stocking the cooler.",
      "#partytips #drinkmath #partyplanning #vegas #lasvegas #partyrentals #eventplanning"),
  [img("big-business-rentals/daily-posts/week5/BB_Post_Tip23_DrinkMath.png")], None, None),

 ("2 HiredATeam", 10, ["fb","ig"], "story", "22",
  cap("What if you could host like you hired a team?",
      "Because you did. Delivery, setup and pickup on every order, tables, chairs and linens that match your theme. You greet the guests, we do the heavy lifting. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #vegas #eventrentals #fullservice #hosting"),
  [img("big-business-rentals/daily-posts/week5/BB_Post_Tue_HiredATeam.png")], None, None),

 ("3 Venue PlanB", 12, ["fb","ig"], "story", "22",
  cap("Plan B is prettier than Plan A.",
      "October wind in Vegas is undefeated, and our private room does not care. 80 guests standing, 40 seated, 3 hours for $625 with rentals included. Comment VENUE and we will DM you open dates.",
      "#venue #privateevent #lasvegas #vegas #partyvenue #indoorvenue #planb"),
  [img("big-business-rentals/venue/BB_Venue_Tue_PlanB.png")], None, None),

 ("4 Referral WordOfMouth", 14, ["fb","ig"], "story", "22",
  cap("In this economy, word of mouth pays.",
      "Somebody mentions a party coming up, you say “I know a guy,” they drop your name, and after their event you collect up to $100. That is the whole hustle. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #wordofmouth #vegas #lasvegas #sidehustle #partyrentals"),
  [img("big-business-rentals/daily-posts/week5/BB_Referral_Tue_WordOfMouth.png")], None, None),

 ("5 Countdown 25", 16, ["fb","ig"], "story", "22",
  cap("The jack-o-lanterns know: 25 nights left.",
      "Every carved pumpkin on the block is counting with us, and the good dates go first. Tables, chairs and the party room, booked before the glow goes out.",
      "#halloween #halloweencountdown #25days #jackolantern #spookyseason #october #lasvegas #partyrentals"),
  [img("big-business-rentals/halloween/BB_Halloween_25Nights.png")], None, None),

 ("6 Gag SpiderGuest", 17, ["fb","ig","tt","yt"], "reel", "23",
  cap("What would YOU do if the plus-one had eight legs? \U0001F577️",
      "Unc screamed, dropped every plate and left the building. The spider? It just wanted a good seat, and honestly it picked the best one. Send this to whoever RSVPs without asking.",
      "#spider #halloween #funnyreels #spookyseason #plusone #lasvegas #partyrentals #comedy"),
  [vid("big-business-rentals/halloween/BB_Halloween_Reel_SpiderGuest.mp4")],
  "The plus-one had eight legs \U0001F577️",
  cap("Unc dropped every plate and left.",
      "The spider just wanted a good seat. Tables and chairs delivered, set up and picked up in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #Spider #Halloween #FunnyShorts #SpookySeason #LasVegas #PartyRentals")),

 ("7 Pink ByTheNumbers", 18, ["fb","ig","tt","yt"], "story", "22",
  cap("99%. That is the five-year survival rate when breast cancer is caught at the localized stage. \U0001F380",
      "Found small means beaten big: screening can find it before you can feel it, sometimes years earlier. Book the screening, put it on the calendar, take a friend. Send this to someone who keeps putting it off. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #earlydetection #bythenumbers #screening #pinkribbon #lasvegas"),
  [vid("big-business-rentals/awareness/BB_PinkOctober_ByTheNumbers.mp4")],
  "99% when caught early \U0001F380",
  cap("Pink October, by the numbers.",
      "Caught at the localized stage, the five-year survival rate is 99%. Screening finds it before you can feel it. Book the screening. Source: American Cancer Society. Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #BreastCancerAwareness #PinkOctober #EarlyDetection #Screening #PinkRibbon")),

 ("8 EP16 Demonstration", 20, ["fb","ig","tt","yt"], "reel", "23",
  cap("He tried to save $5 on one chair.",
      "EP. 16: Mr. Big Business sneaks Lil Wobbles into the setup, Mrs. Never Wrong says absolutely nothing, and the demonstration goes exactly how she knew it would. Record: 0 wins, 2 losses. Should anyone warn Lil Wobbles’ next victim? Tell us below.",
      "#thebigbusinesschronicles #lilwobbles #mrsneverwrong #comedy #funnyreels #sitcom #lasvegas #partyrentals"),
  [vid("fb_safe/BB_Chronicles_Ep16_TheDemonstration.mp4")],
  "EP. 16: The Demonstration \U0001F602 she said nothing",
  cap("THE BIG BUSINESS CHRONICLES: he tried to save $5.",
      "Mrs. Never Wrong said nothing, and the cheap chair did what cheap chairs do. Record: 0 wins, 2 losses. New episodes daily in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #Comedy #Sitcom #CheapChair #FunnyShorts #LasVegas #PartyRentals")),
]

for label, hour, channels, ptype, yt_cat, text, assets, yt_title, yt_text in POSTS:
    due = D.format(hour)
    for ch in channels:
        t = yt_text if (ch == "yt" and yt_text) else text
        res = create(ch, due, t, assets, yt_title if ch == "yt" else None,
                     ptype=ptype, yt_cat=yt_cat)
        print(f"{label} [{ch}] {due} -> {res}")
