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
def caro(stem, n):
    return [img(f"big-business-rentals/daily-posts/week5/{stem}_{i:02d}.png") for i in range(1, n+1)]

D = "2026-10-05T{:02d}:00:00-07:00"

POSTS = [
 ("1 IceMath carousel", 8, ["fb","ig"], "post", "22",
  cap("How much ice do you actually need?",
      "Swipe for the party math nobody does until it is too late. Send this to the friend who always forgets the ice.",
      "#partytips #icemath #partyplanning #vegas #lasvegas #partyrentals #eventplanning"),
  caro("BB_Caro_Mon_IceMath", 6), None, None),

 ("2 Handled carousel", 10, ["fb","ig"], "post", "22",
  cap("What if party day was already handled?",
      "Swipe to see how little you would be lifting. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #vegas #eventrentals #partyplanning #delivered"),
  caro("BB_Caro_Mon_Handled", 5), None, None),

 ("3 Venue lux carousel", 12, ["fb","ig"], "post", "22",
  cap("Your party deserves a home.",
      "Swipe through our private venue: seats 40, holds 80 standing, 3 hours for $625 or 4 hours for $800 with rentals included. Comment VENUE and we will DM you open dates.",
      "#venue #privateevent #lasvegas #vegas #partyvenue #eventspace #birthdayparty"),
  [img("big-business-rentals/examples/EX_Carousel_1.png"),
   img("big-business-rentals/examples/EX_Carousel_2.png"),
   img("big-business-rentals/examples/EX_Carousel_3.png")], None, None),

 ("4 Meet The Cast", 13, ["fb","ig"], "post", "22",
  cap("Vegas, meet the cast.",
      "THE BIG BUSINESS CHRONICLES premieres TONIGHT: Mr. Big Business, Mrs. Never Wrong, Unc, Tyler the Intern, Lil Wobbles the cheap chair, and The Cat. New episodes daily through the Halloween party finale. Which one are you? Tell us below.",
      "#newseries #comedy #meetthecast #lasvegas #vegas #partyrentals #chronicles"),
  [img("big-business-rentals/examples/EX_MeetTheCast.png")], None, None),

 ("5 Referral carousel", 14, ["fb","ig"], "post", "22",
  cap("The easiest $100 in Vegas is not on the casino floor.",
      "Swipe to see how the referral play works, then send this to the plug of your group chat. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #easiest100 #vegas #lasvegas #sidehustle #partyrentals"),
  caro("BB_Caro_Mon_Referral", 5), None, None),

 ("6 26Nights carousel", 16, ["fb","ig"], "post", "22",
  cap("26 nights till Halloween.",
      "Swipe before the good dates go, then send this to whoever is hosting Halloween.",
      "#halloween #halloweencountdown #26days #spookyseason #october #lasvegas #partyrentals"),
  caro("BB_Caro_Mon_26Nights", 4), None, None),

 ("7 Gag PumpkinHead", 17, ["fb","ig","tt","yt"], "reel", "23",
  cap("What do you do when the pumpkin will NOT come off? \U0001F383",
      "He wore it “for the pictures.” It stayed for everything else. One chair, one countdown, one POP, and the chair never moved an inch. Send this to whoever commits too hard to the costume.",
      "#pumpkinhead #halloween #funnyreels #spookyseason #costume #lasvegas #partyrentals #comedy"),
  [vid("big-business-rentals/halloween/BB_Halloween_Reel_PumpkinHead.mp4")],
  "The pumpkin would NOT come off \U0001F383",
  cap("He wore it for the pictures.",
      "It stayed for everything else. One chair, one POP, zero wobbles. Tables and chairs delivered, set up and picked up in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #PumpkinHead #Halloween #FunnyShorts #SpookySeason #LasVegas #PartyRentals")),

 ("8 Pink MythsBusted", 18, ["fb","ig","tt","yt"], "story", "22",
  cap("Most women diagnosed have NO family history. \U0001F380",
      "That fact busts the biggest myth out there. Myths busted today: “it runs in families, I’m safe”, “I’m too young”, and “it doesn’t hurt so it’s nothing.” Lumps are often painless. Know the facts and share them. Send this to someone you love. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #mythsbusted #knowthefacts #earlydetection #pinkribbon #lasvegas"),
  [vid("big-business-rentals/awareness/BB_PinkOctober_MythsBusted.mp4")],
  "Most diagnosed have NO family history \U0001F380",
  cap("Pink October, myths busted.",
      "No family history does not mean safe, young does not mean immune, painless does not mean harmless. Know the facts. Share them. Source: American Cancer Society. Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #BreastCancerAwareness #PinkOctober #MythsBusted #KnowTheFacts #PinkRibbon")),

 ("9 EP15 premiere", 20, ["fb","ig","tt","yt"], "reel", "23",
  cap("He hired an intern. He said four words: “stack the chairs.” \U0001F602",
      "EP. 15 premieres THE BIG BUSINESS CHRONICLES Season One. Tyler’s first day went exactly how you think it went. What should Tyler help with next? Best idea gets the next episode credit.",
      "#thebigbusinesschronicles #newintern #comedy #funnyreels #sitcom #lasvegas #vegas #partyrentals"),
  [vid("fb_safe/BB_Chronicles_Ep15_TheNewIntern.mp4")],
  "EP. 15: The New Intern \U0001F602 “stack the chairs”",
  cap("THE BIG BUSINESS CHRONICLES, Season One premiere.",
      "Tyler takes every instruction 100 percent literally. What should Tyler help with next? Comment below. New episodes daily in Las Vegas, NV. IG: @bigbusiness_rentals_events",
      "#Shorts #Comedy #Sitcom #NewIntern #FunnyShorts #LasVegas #PartyRentals")),
]

for label, hour, channels, ptype, yt_cat, text, assets, yt_title, yt_text in POSTS:
    due = D.format(hour)
    for ch in channels:
        t = yt_text if (ch == "yt" and yt_text) else text
        res = create(ch, due, t, assets, yt_title if ch == "yt" else None,
                     ptype=ptype, yt_cat=yt_cat)
        print(f"{label} [{ch}] {due} -> {res}")
