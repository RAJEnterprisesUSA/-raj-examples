import json, subprocess

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CONTACT = "\U0001F4DE 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com"

def cap(opening, para, tags):
    return f"{opening}\n\n{para}\n\n{CONTACT}\n\n{tags}"

def caro(stem, n):
    return [{"image": {"url": RAW + f"big-business-rentals/daily-posts/week5/{stem}_{i:02d}.png"}} for i in range(1, n+1)]

def img(p): return [{"image": {"url": RAW + p}}]
def vid(p): return [{"video": {"url": RAW + p}}]

STORY = {"instagram": {"type": "story", "shouldShareToFeed": False}}
POST  = {"instagram": {"type": "post",  "shouldShareToFeed": True}}
REEL  = {"instagram": {"type": "reel",  "shouldShareToFeed": True}}

# (post_id, text, assets, metadata)
EDITS = [
 # ---------- MONDAY (feed: IceMath carousel, Cast, gag reel, EP15 reel) ----------
 ("6ac3136169a169193a57b4a7",  # IceMath IG stays FEED, trim tags
  cap("How much ice do you actually need?",
      "Swipe for the party math nobody does until it is too late. Send this to the friend who always forgets the ice.",
      "#partytips #partyplanning #lasvegas #partyrentals #vegas"),
  caro("BB_Caro_Mon_IceMath", 6), POST),
 ("6ac3136369a169193a57b503",  # Venue lux IG -> STORY sequence
  cap("Your party deserves a home.",
      "Tap through our private venue: seats 40, holds 80 standing, 3 hours for $625 or 4 hours for $800 with rentals included. Comment VENUE and we will DM you open dates.",
      "#venue #privateevent #lasvegas #partyvenue #vegas"),
  img("big-business-rentals/examples/EX_Carousel_1.png") +
  img("big-business-rentals/examples/EX_Carousel_2.png")[0:1] +
  img("big-business-rentals/examples/EX_Carousel_3.png")[0:1], STORY),
 ("6ac3136463761da98b67d96d",  # Cast IG stays FEED, trim tags
  cap("Vegas, meet the cast.",
      "THE BIG BUSINESS CHRONICLES premieres TONIGHT: Mr. Big Business, Mrs. Never Wrong, Unc, Tyler the Intern, Lil Wobbles the cheap chair, and The Cat. New episodes daily through the Halloween party finale. Which one are you? Tell us below.",
      "#newseries #comedy #meetthecast #lasvegas #partyrentals"),
  img("big-business-rentals/examples/EX_MeetTheCast.png"), POST),
 ("6ac3136563761da98b67d9df",  # Referral IG -> STORY sequence
  cap("The easiest $100 in Vegas is not on the casino floor.",
      "Tap through to see how the referral play works, then send this to the plug of your group chat. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #easiest100 #lasvegas #sidehustle #partyrentals"),
  caro("BB_Caro_Mon_Referral", 5), STORY),
 ("6ac313665de5ee424c22bf02",  # 26Nights IG -> STORY sequence
  cap("26 nights till Halloween.",
      "Tap through before the good dates go, then send this to whoever is hosting Halloween.",
      "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
  caro("BB_Caro_Mon_26Nights", 4), STORY),
 ("6ac3136769a169193a57b59b",  # gag IG reel, trim tags
  cap("What do you do when the pumpkin will NOT come off? \U0001F383",
      "He wore it “for the pictures.” It stayed for everything else. One chair, one countdown, one POP, and the chair never moved an inch. Send this to whoever commits too hard to the costume.",
      "#pumpkinhead #halloween #funnyreels #lasvegas #partyrentals"),
  vid("big-business-rentals/halloween/BB_Halloween_Reel_PumpkinHead.mp4"), REEL),
 ("6ac313695de5ee424c22c14a",  # pink IG story, trim tags
  cap("Most women diagnosed have NO family history. \U0001F380",
      "That fact busts the biggest myth out there. Myths busted today: “it runs in families, I’m safe”, “I’m too young”, and “it doesn’t hurt so it’s nothing.” Lumps are often painless. Know the facts and share them. Send this to someone you love. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #mythsbusted #earlydetection #lasvegas"),
  vid("big-business-rentals/awareness/BB_PinkOctober_MythsBusted.mp4"), STORY),
 ("6ac3136c5de5ee424c22c18c",  # EP15 IG reel, trim tags
  cap("He hired an intern. He said four words: “stack the chairs.” \U0001F602",
      "EP. 15 premieres THE BIG BUSINESS CHRONICLES Season One. Tyler’s first day went exactly how you think it went. What should Tyler help with next? Best idea gets the next episode credit.",
      "#thebigbusinesschronicles #comedy #funnyreels #lasvegas #partyrentals"),
  vid("fb_safe/BB_Chronicles_Ep15_TheNewIntern.mp4"), REEL),

 # ---------- TUESDAY (feed: WordOfMouth carousel, gag reel, EP16 reel) ----------
 ("6ac314fc69a169193a57ef06",  # DrinkMath IG -> STORY
  cap("How many drinks does a party actually need?",
      "Tap through for the bartender math, then send this to whoever is stocking the cooler.",
      "#partytips #drinkmath #partyplanning #lasvegas #partyrentals"),
  caro("BB_Caro_Tue_DrinkMath", 6), STORY),
 ("6ac314fd5de5ee424c22f0f1",  # HiredATeam IG -> STORY
  cap("What if you could host like you hired a team?",
      "Tap through to meet your party day crew. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #eventrentals #fullservice #vegas"),
  caro("BB_Caro_Tue_HiredATeam", 5), STORY),
 ("6ac314ffca1380ada843439d",  # WordOfMouth IG stays FEED, trim tags
  cap("In this economy, word of mouth pays.",
      "Swipe to see the referral play, then send this to your best connector. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #wordofmouth #lasvegas #sidehustle #partyrentals"),
  caro("BB_Caro_Tue_WordOfMouth", 5), POST),
 ("6ac314ff5de5ee424c22f14b",  # 25Nights IG -> STORY
  cap("25 nights till Halloween.",
      "Tap through before the glow goes out. Comment SPOOKY and we will DM you open October dates.",
      "#halloween #halloweencountdown #spookyseason #lasvegas #partyrentals"),
  caro("BB_Caro_Tue_25Nights", 4), STORY),
 ("6ac3150163761da98b681fe3",  # gag12 IG reel, trim
  cap("What would YOU do if the plus-one had eight legs? \U0001F577️",
      "Unc screamed, dropped every plate and left the building. The spider? It just wanted a good seat, and honestly it picked the best one. Send this to whoever RSVPs without asking.",
      "#spider #halloween #funnyreels #lasvegas #partyrentals"),
  vid("big-business-rentals/halloween/BB_Halloween_Reel_SpiderGuest.mp4"), REEL),
 ("6ac31503fe1389e4134cfa82",  # pink6 IG story, trim
  cap("99%. That is the five-year survival rate when breast cancer is caught at the localized stage. \U0001F380",
      "Found small means beaten big: screening can find it before you can feel it, sometimes years earlier. Book the screening, put it on the calendar, take a friend. Send this to someone who keeps putting it off. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #earlydetection #screening #lasvegas"),
  vid("big-business-rentals/awareness/BB_PinkOctober_ByTheNumbers.mp4"), STORY),
 ("6ac315055de5ee424c22f20c",  # EP16 IG reel, trim
  cap("He tried to save $5 on one chair.",
      "EP. 16: Mr. Big Business sneaks Lil Wobbles into the setup, Mrs. Never Wrong says absolutely nothing, and the demonstration goes exactly how she knew it would. Record: 0 wins, 2 losses. Should anyone warn Lil Wobbles’ next victim? Tell us below.",
      "#thebigbusinesschronicles #comedy #funnyreels #lasvegas #partyrentals"),
  vid("fb_safe/BB_Chronicles_Ep16_TheDemonstration.mp4"), REEL),

 # ---------- WEDNESDAY (feed: 24Nights carousel, gag reel, EP17 reel) ----------
 ("6ac31aa5ca1380ada844113d",  # TrashMath IG -> STORY
  cap("Nobody plans for trash.",
      "Tap through for the one piece of party math everybody skips. Send this to whoever is on cleanup crew.",
      "#partytips #partyplanning #lasvegas #partyrentals #vegas"),
  caro("BB_Caro_Wed_TrashMath", 6), STORY),
 ("6ac31aa65de5ee424c23d2a7",  # WeekendBack IG -> STORY
  cap("What does your party weekend actually look like?",
      "Tap through if it involves hauling, sweating and returns. Comment QUOTE and we will DM you a price today.",
      "#partyrentals #lasvegas #eventrentals #partyplanning #weekend"),
  caro("BB_Caro_Wed_WeekendBack", 5), STORY),
 ("6ac31aa869a169193a58ab74",  # GetPaid IG -> STORY
  cap("Get paid to be popular.",
      "Tap through to see how introductions turn into money, then send this to the friend who knows everybody. Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed.",
      "#referral #getpaid #lasvegas #sidehustle #partyrentals"),
  caro("BB_Caro_Wed_GetPaid", 5), STORY),
 ("6ac31aa969a169193a58abc9",  # 24Nights IG stays FEED, trim tags
  cap("Halloween lands on a SATURDAY this year.",
      "Swipe for why that changes everything: 24 nights out, four party Saturdays left. Comment SPOOKY and we will DM you open October dates.",
      "#halloween #halloweencountdown #halloweensaturday #lasvegas #partyrentals"),
  caro("BB_Caro_Wed_24Nights", 4), POST),
 ("6ac31aaad467abe8cfd452f1",  # gag13 IG reel, trim
  cap("Who keeps eating the party candy? \U0001F480",
      "The bowl kept shrinking, Unc kept turning around, and the hand under the tablecloth kept winning. The guest list had one extra body on it the whole time. Send this to the friend who raids the snack table.",
      "#candyhand #halloween #funnyreels #lasvegas #partyrentals"),
  vid("big-business-rentals/halloween/BB_Halloween_Reel_CandyHand.mp4"), REEL),
 ("6ac31aac5de5ee424c23d67e",  # pink7 IG story, trim
  cap("1 in 100 breast cancer cases in the U.S. is a man. \U0001F380",
      "Men have breast tissue too, the signs are the same, and because nobody is looking it often gets found later. A lump, a change in the skin or the nipple, anything new: get it checked. Say the awkward thing to the men you love. Send this to them. Source: CDC.",
      "#breastcancerawareness #pinkoctober #mensedition #earlydetection #lasvegas"),
  vid("big-business-rentals/awareness/BB_PinkOctober_MensEdition.mp4"), STORY),
 ("6ac31aae69a169193a58ac84",  # EP17 IG reel, trim
  cap("He put out the best chair for a big client.",
      "The cat found it first. EP. 17: the shoo, the bribe, the tilt, and the decoy chair that backfired spectacularly. Record: 0 wins, 3 losses. How do you beat the cat? Tell us below.",
      "#thebigbusinesschronicles #thecat #comedy #lasvegas #partyrentals"),
  vid("fb_safe/BB_Chronicles_Ep17_TheDecoy.mp4"), REEL),
]

MUT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""
ok = fail = 0
for pid, text, assets, meta in EDITS:
    inp = {"id": pid, "text": text, "assets": assets, "metadata": meta}
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": MUT, "variables": {"input": inp}})],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        tn = d["data"]["editPost"]["__typename"]
        if tn == "PostActionSuccess": ok += 1; print("OK  ", pid)
        else: fail += 1; print("FAIL", pid, r.stdout[:200])
    except Exception:
        fail += 1; print("FAIL", pid, r.stdout[:200])
print(f"done: {ok} OK, {fail} failed")
