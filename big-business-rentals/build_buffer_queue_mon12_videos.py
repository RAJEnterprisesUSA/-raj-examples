"""Queue MONDAY OCT 12 videos: gag 5pm, pink 6pm (story FB/IG), EP21 8pm.
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

D = "2026-10-12T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Halloween_Reel_GhostWaiter.mp4", "reel", "23",
  cap("The drinks started serving themselves. \U0001F47B",
      "New record: the tray did three laps before anybody asked who was carrying it. Turns out he works here, great attitude, never spills. Send this to whoever never gets up to refill anything.",
      "#halloween #ghost #funnyreels #lasvegas #partyrentals"),
  "The drinks are serving themselves \U0001F47B #Shorts",
  "The tray did three laps before anybody asked who was carrying it. He works here now. New Halloween gags daily from Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #Ghost #FunnyShorts #LasVegas #PartyRentals"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_DenseFacts.mp4", "story", "22",
  cap("About half of women over 40 have dense breasts. \U0001F380",
      "Totally normal, and worth knowing about: dense tissue can hide changes on a mammogram and your report now has to tell you if you have it. So read the report, then ask your doctor one question: does extra screening make sense for me? Send this to a woman who had a mammogram this year. Source: American Cancer Society and FDA.",
      "#breastcancerawareness #pinkoctober #densebreasts #earlydetection #lasvegas"),
  "Dense breasts: read the report, ask the question. \U0001F380 #Shorts",
  "About half of women over 40 have dense breast tissue. It can hide changes on a mammogram, and your report now has to tell you. Ask your doctor if extra screening makes sense. Source: American Cancer Society and FDA.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #DenseBreasts #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep22_TheDecorationCommittee.mp4", "reel", "23",
  cap("He hung one pumpkin. Tyler hung fifty. \U0001F602",
      "EP. 22: one tasteful pumpkin versus the intern's entire wall of Halloween, and the committee did not hesitate. WHERE DID HE EVEN COME FROM? What should Tyler decorate next? Best answer gets the next episode credit.",
      "#thebigbusinesschronicles #comedy #lasvegas #funnyreels #halloweenparty"),
  "EP. 22: The Decoration Committee \U0001F602 Tyler strikes again #Shorts",
  "THE BIG BUSINESS CHRONICLES: one tasteful pumpkin versus the intern's entire wall of Halloween. The committee has spoken. Record: 1 win, 7 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
]

if __name__ == "__main__":
    ok = fail = 0
    def run(label, res):
        global ok, fail
        if res.startswith("OK"): ok += 1
        else: fail += 1
        print(res, label)

    for hour, path, ptype, yt_cat, text, yt_title, yt_text in VIDEOS:
        due = D.format(hour)
        run(f"FB  {path.rsplit('/',1)[1]}", create("fb", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"IG  {path.rsplit('/',1)[1]}", create("ig", due, text, vid(path), ptype,
                                                   first_comment=(ptype == "reel")))
        run(f"TT  {path.rsplit('/',1)[1]}", create("tt", due, text, vid(path)))
        run(f"YT  {path.rsplit('/',1)[1]}", create("yt", due, yt_text, vid(path),
                                                   yt_title=yt_title, yt_cat=yt_cat))
    print(f"done: {ok} OK, {fail} failed")
