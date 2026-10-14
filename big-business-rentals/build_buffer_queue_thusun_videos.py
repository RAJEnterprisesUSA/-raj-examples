"""Queue THU OCT 15 - SUN OCT 18 videos: gag 5pm, pink 6pm (story FB/IG), episode 8pm.
Each goes FB + IG + TikTok + YouTube. Cross-linked firstComments on reels.
Run AFTER the mp4s are committed and pushed."""
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
           first_comment=False):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": due, "assets": assets}
    if channel == "fb":
        md = {"type": ptype}
        if first_comment and ptype in ("post", "reel"): md["firstComment"] = FC_FB
        inp["metadata"] = {"facebook": md}
    elif channel == "ig":
        md = {"type": ptype, "shouldShareToFeed": ptype != "story"}
        if first_comment and ptype in ("post", "reel"): md["firstComment"] = FC_IG
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

def vid(p): return [{"video": {"url": RAW + p}}]

# (date, hour, path, ptype, yt_cat, caption, yt_title, yt_text)
VIDEOS = [
 # ---------------- THURSDAY OCT 15 ----------------
 ("2026-10-15", 17, "big-business-rentals/halloween/BB_Halloween_Reel_FogMachine.mp4", "reel", "23",
  cap("A little fog for the vibes. Then a lot. \U0001F4A8",
      "The fog machine had one job and did it too well. When it cleared, the party had gained a guest nobody invited. Vibes: delivered. Send this to the friend who always overdoes the decorations.",
      "#halloween #fogmachine #funnyreels #lasvegas #partyrentals"),
  "The fog machine did its job TOO well \U0001F4A8 #Shorts",
  "A little fog for the vibes, then a lot, then a surprise guest. Vibes delivered. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #FogMachine #FunnyShorts #LasVegas #PartyRentals"),
 ("2026-10-15", 18, "big-business-rentals/awareness/BB_PinkOctober_Under40.mp4", "story", "22",
  cap("Under 40? This one is for you. \U0001F380",
      "Young does not mean immune. Know your normal, get changes checked, and if something feels off, speak up until somebody listens. Family history moves the timeline up, so ask your doctor when screening should start for you. Send this to a friend who keeps putting the call off.",
      "#breastcancerawareness #pinkoctober #under40 #knowyourbody #lasvegas"),
  "Under 40? Know your normal. \U0001F380 #Shorts",
  "Young does not mean immune. Know your normal, get changes checked, and ask your doctor when screening should start for you.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #Under40 #LasVegas"),
 ("2026-10-15", 20, "fb_safe/BB_Chronicles_Ep24_ThePlaylistWar.mp4", "reel", "23",
  cap("The cat is the DJ now. \U0001F3A7",
      "EP. 24: three hours of curated playlist versus one cat with a paw. Tap, tap back, tap again, and then the judge picked a side. DJ Cat runs the aux and the record falls to 2 and 8. What does the cat play first? Wrong answers only.",
      "#thebigbusinesschronicles #djcat #comedy #lasvegas #funnyreels"),
  "EP. 24: The Playlist War \U0001F3A7 DJ Cat wins #Shorts",
  "THE BIG BUSINESS CHRONICLES: one curated playlist, one cat with a paw, one judge who picked a side. Record: 2 wins, 8 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
 # ---------------- FRIDAY OCT 16 ----------------
 ("2026-10-16", 17, "big-business-rentals/halloween/BB_Halloween_Reel_DancingBroom.mp4", "reel", "23",
  cap("The broom is self-employed. \U0001F9F9",
      "Swept the whole floor, dodged a stakeout, and turned out to have a ghost on payroll the entire time. Cleanup crew never left. We pick up after parties too, send this to whoever always gets stuck sweeping.",
      "#halloween #hauntedhouse #funnyreels #lasvegas #partyrentals"),
  "The broom is self-employed \U0001F9F9 #Shorts",
  "It swept the floor, dodged a stakeout, and had a ghost on payroll the whole time. Cleanup crew never left. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Ghost #FunnyShorts #LasVegas #PartyRentals"),
 ("2026-10-16", 18, "big-business-rentals/awareness/BB_PinkOctober_BuddySystem.mp4", "story", "22",
  cap("Some things are easier with a friend. \U0001F380",
      "Screening is one of them. Book the same week, remind each other, celebrate after. Mammograms catch what hands cannot feel, and your doctor can tell you the schedule that fits your age and history. Send this to your screening buddy and make it a date. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #buddysystem #mammogram #lasvegas"),
  "Book your screening with a friend. \U0001F380 #Shorts",
  "The buddy system works: book the same week, remind each other, celebrate after. Mammograms catch what hands cannot feel. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #BuddySystem #LasVegas"),
 ("2026-10-16", 20, "fb_safe/BB_Chronicles_Ep25_TheGuestList.mp4", "reel", "23",
  cap("The guest list was final. Was. \U0001F4CB",
      "EP. 25: no crashers this year, until the cat and the chair showed up as somebody's plus two. Tyler appeared out of nowhere again, and the list is now decorative. Record drops to 2 and 9. Who else is on Tyler's list? Wrong answers only.",
      "#thebigbusinesschronicles #tylertheintern #comedy #lasvegas #funnyreels"),
  "EP. 25: The Guest List \U0001F4CB Tyler strikes again #Shorts",
  "THE BIG BUSINESS CHRONICLES: the list was final, laminated, and completely ignored. Tyler brought a plus two. Record: 2 wins, 9 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
 # ---------------- SATURDAY OCT 17 ----------------
 ("2026-10-17", 17, "big-business-rentals/halloween/BB_Halloween_Reel_SeanceTable.mp4", "reel", "23",
  cap("The table had other plans. \U0001F6F8",
      "One minute it is sturdy and normal, the next it is hovering like rent is due on the ceiling. He talked it down, it landed perfect, and the cat claimed it immediately. Our tables always come back down. Send this to somebody who believes in ghosts.",
      "#halloween #seance #funnyreels #lasvegas #partyrentals"),
  "The table had other plans \U0001F6F8 #Shorts",
  "Sturdy, normal, and suddenly airborne. He talked it down, it landed perfect, the cat claimed it. Our tables always come back down. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Seance #FunnyShorts #LasVegas #PartyRentals"),
 ("2026-10-17", 18, "big-business-rentals/awareness/BB_PinkOctober_SurvivorSalute.mp4", "story", "22",
  cap("This one is not a tip. It is a thank you. \U0001F380",
      "To everyone in the fight right now, to everyone who won it, and to everyone we carry with us. Pink looks good on Vegas all month. Wear it, share it, and ask somebody how they are really doing. Send this to a survivor you love.",
      "#breastcancerawareness #pinkoctober #survivor #stillhere #lasvegas"),
  "To the survivors: still here, still celebrated. \U0001F380 #Shorts",
  "To everyone in the fight, everyone who won it, and everyone we carry with us. Pink looks good on Vegas all October.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #Survivor #LasVegas"),
 ("2026-10-17", 20, "fb_safe/BB_Chronicles_Ep26_TheDanceRehearsal.mp4", "reel", "23",
  cap("The chair got a nine. He got a six. \U0001F483",
      "EP. 26: all week rehearsing the Halloween entrance, and the judge gave the routine a six. The red chair wobbled once and scored a nine. The cat did nothing and got a ten. Record: 2 and 10. Score his moves below, be honest.",
      "#thebigbusinesschronicles #dancebattle #comedy #lasvegas #funnyreels"),
  "EP. 26: The Dance Rehearsal \U0001F483 a six?! #Shorts",
  "THE BIG BUSINESS CHRONICLES: he rehearsed all week and scored a six. The chair got a nine. The cat did nothing and got a ten. Record: 2 wins, 10 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
 # ---------------- SUNDAY OCT 18 ----------------
 ("2026-10-18", 17, "big-business-rentals/halloween/BB_Halloween_Reel_CandyTax.mp4", "reel", "23",
  cap("Candy tax. Everybody pays. \U0001F36C",
      "One for the road from every bowl, no exceptions, until bowl number three turned out to have a cat on it. Full refund, interest included. The tax has exceptions. Send this to the friend who skims every candy bowl.",
      "#halloween #candytax #funnyreels #lasvegas #partyrentals"),
  "Candy tax. Everybody pays. Except one. \U0001F36C #Shorts",
  "One for the road from every bowl, until bowl three had a cat on it. Full refund, interest included. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #CandyTax #FunnyShorts #LasVegas #PartyRentals"),
 ("2026-10-18", 18, "big-business-rentals/awareness/BB_PinkOctober_GroupText.mp4", "story", "22",
  cap("Three names. One text. Today. \U0001F380",
      "Your mom, your sister, your best friend. Ask when their last screening was, no lecture, just love. The women in your life spend all year taking care of everybody else, so today somebody checks on them. That somebody is you. Send this to the group chat.",
      "#breastcancerawareness #pinkoctober #checkonyourpeople #grouptext #lasvegas"),
  "Three names. One text. Today. \U0001F380 #Shorts",
  "Ask the women you love when their last screening was. No lecture, just love. A thirty second text can start the appointment that matters.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #CheckOnYourPeople #LasVegas"),
 ("2026-10-18", 20, "fb_safe/BB_Chronicles_Ep27_TheWalkthrough.mp4", "reel", "23",
  cap("He finally had a perfect day. \U0001F3C6",
      "EP. 27: the final walkthrough before the big Halloween party. The chair tried the row, denied. The cat went for the bowl, decoyed. She said approved, and that is win number three. Can he keep the streak going at the Halloween party? Predictions below.",
      "#thebigbusinesschronicles #bigwin #comedy #lasvegas #funnyreels"),
  "EP. 27: The Walkthrough \U0001F3C6 win number three #Shorts",
  "THE BIG BUSINESS CHRONICLES: chair denied, cat decoyed, client approved. Win number three on the board. Record: 3 wins, 10 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
]

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for date, hour, path, ptype, yt_cat, text, yt_title, yt_text in VIDEOS:
        due = f"{date}T{hour:02d}:00:00-07:00"
        run(f"FB  {path.rsplit('/',1)[1]}", create("fb", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"IG  {path.rsplit('/',1)[1]}", create("ig", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"TT  {path.rsplit('/',1)[1]}", create("tt", due, text, vid(path)))
        run(f"YT  {path.rsplit('/',1)[1]}", create("yt", due, yt_text, vid(path),
                                                   yt_title=yt_title, yt_cat=yt_cat))
    print(f"done: {ok} OK, {fail} failed")
