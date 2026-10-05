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
def caro(stem, n):
    return [img(f"big-business-rentals/daily-posts/week5/{stem}_{i:02d}.png") for i in range(1, n+1)]
def vid(p): return {"video": {"url": RAW + p}}

D = "2026-10-07T{:02d}:00:00-07:00"

POSTS = [
 ("1 TrashMath carousel", 8, ["fb","ig"], "post", "22",
  cap("Nobody plans for trash.",
      "Swipe for the one piece of party math everybody skips. Send this to whoever is on cleanup crew.",
      "#partytips #trashmath #partyplanning #vegas #lasvegas #partyrentals #eventplanning"),
  caro("BB_Caro_Wed_TrashMath", 6), None, None),

 ("2 WeekendBack carousel", 10, ["fb","ig"], "post", "22",
  cap("What does your party weekend actually look like?",
      "Swipe if it involves hauling, sweating and returns. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #vegas #eventrentals #partyplanning #weekend"),
  caro("BB_Caro_Wed_WeekendBack", 5), None, None),

 ("3 Venue OnePrice", 12, ["fb","ig"], "story", "22",
  cap("One price, the whole party.",
      "Our private room runs $625 for 3 hours up to 25 guests or $800 for 4 hours up to 40, rentals included, with space for 80 standing. Comment VENUE and we will DM you open dates.",
      "#venue #privateevent #lasvegas #vegas #partyvenue #oneprice"),
  [img("big-business-rentals/venue/BB_Venue_Wed_OnePrice.png")], None, None),

 ("4 GetPaid carousel", 14, ["fb","ig"], "post", "22",
  cap("Get paid to be popular.",
      "Swipe to see how introductions turn into money, then send this to the friend who knows everybody. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #getpaid #vegas #lasvegas #sidehustle #partyrentals"),
  caro("BB_Caro_Wed_GetPaid", 5), None, None),

 ("5 24Nights carousel", 16, ["fb","ig"], "post", "22",
  cap("Halloween lands on a SATURDAY this year.",
      "Swipe for why that changes everything: 24 nights out, four party Saturdays left. Comment SPOOKY and we will DM you open October dates.",
      "#halloween #halloweencountdown #24days #halloweensaturday #spookyseason #october #lasvegas #partyrentals"),
  caro("BB_Caro_Wed_24Nights", 4), None, None),

 ("6 Gag CandyHand", 17, ["fb","ig","tt","yt"], "reel", "23",
  cap("Who keeps eating the party candy? 💀",
      "The bowl kept shrinking, Unc kept turning around, and the hand under the tablecloth kept winning. The guest list had one extra body on it the whole time. Send this to the friend who raids the snack table.",
      "#candyhand #halloween #funnyreels #spookyseason #skeleton #lasvegas #partyrentals #comedy"),
  [vid("big-business-rentals/halloween/BB_Halloween_Reel_CandyHand.mp4")],
  "Who keeps eating the party candy? 💀",
  cap("The bowl kept shrinking.",
      "The hand under the tablecloth kept winning. Every guest gets a seat, and a snack. Tables and chairs delivered, set up and picked up in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #Skeleton #Halloween #FunnyShorts #SpookySeason #LasVegas #PartyRentals")),

 ("7 Pink MensEdition", 18, ["fb","ig","tt","yt"], "story", "22",
  cap("1 in 100 breast cancer cases in the U.S. is a man. 🎀",
      "Men have breast tissue too, the signs are the same, and because nobody is looking it often gets found later. A lump, a change in the skin or the nipple, anything new: get it checked. Say the awkward thing to the men you love. Send this to them. Source: CDC.",
      "#breastcancerawareness #pinkoctober #mensedition #menstoo #earlydetection #pinkribbon #lasvegas"),
  [vid("big-business-rentals/awareness/BB_PinkOctober_MensEdition.mp4")],
  "1 in 100 is a man 🎀 Men's edition",
  cap("Pink October, men's edition.",
      "Men have breast tissue too, the signs are the same, and late discovery is the danger. Say the awkward thing to the men you love. Source: CDC. Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #BreastCancerAwareness #PinkOctober #MensHealth #EarlyDetection #PinkRibbon")),

 ("8 EP17 Decoy", 20, ["fb","ig","tt","yt"], "reel", "23",
  cap("He put out the best chair for a big client.",
      "The cat found it first. EP. 17: the shoo, the bribe, the tilt, and the decoy chair that backfired spectacularly. Record: 0 wins, 3 losses. How do you beat the cat? Tell us below.",
      "#thebigbusinesschronicles #thecat #comedy #funnyreels #sitcom #catsofinstagram #lasvegas #partyrentals"),
  [vid("fb_safe/BB_Chronicles_Ep17_TheDecoy.mp4")],
  "EP. 17: The Decoy 😂 you cannot beat the cat",
  cap("THE BIG BUSINESS CHRONICLES: the decoy.",
      "The shoo, the bribe, the tilt, and the decoy chair that backfired. Record: 0 wins, 3 losses. How do you beat the cat? New episodes daily in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #Comedy #Sitcom #Cat #FunnyShorts #LasVegas #PartyRentals")),
]
for label, hour, channels, ptype, yt_cat, text, assets, yt_title, yt_text in POSTS:
    due = D.format(hour)
    for ch in channels:
        t = yt_text if (ch == "yt" and yt_text) else text
        res = create(ch, due, t, assets, yt_title if ch == "yt" else None,
                     ptype=ptype, yt_cat=yt_cat)
        print(f"{label} [{ch}] {due} -> {res}")
