"""Queue WEDNESDAY OCT 21 videos: trend 5pm, pink 6pm (story FB/IG), EP30 8pm. Run AFTER push."""
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

D = "2026-10-21T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_GettingRobbed.mp4", "reel", "23",
  cap("He got robbed in broad daylight and never noticed. \U0001F440",
      "He was busy showing off the setup while the cat took the candy, Lil Wobbles bulldozed a chair clean off the scene, and the ghost floated away with the whole bowl. That is what happens when the setup is this good, everybody wants it. Book your own, we deliver anywhere in Las Vegas. Send this to somebody who never notices anything.",
      "#funnyreels #halloween #trending #lasvegas #partyrentals"),
  "Robbed in broad daylight and he never noticed \U0001F440 #Shorts",
  "The cat took the candy, the chair took a chair, the ghost took the bowl. Everybody wants the setup. Book your own in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Funny #Halloween #PartyRentals #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_55Plus.mp4", "story", "22",
  cap("At 55, your screening plan gets a choice. \U0001F380",
      "At 55 and up there are two good options: switch to a mammogram every other year, or keep going every single year. Either way, stay on a schedule for as long as you are in good health. Then pass it on to the women you love, moms, aunties, grandmothers, neighbors. One phone call can put a screening back on the calendar. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #mammogram #over55 #lasvegas"),
  "At 55, the screening plan gets a choice. \U0001F380 #Shorts",
  "Every other year or every year, your call, just stay on a schedule. Tell the 55 plus women you love. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #Over55 #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep30_TheInvitations.mp4", "reel", "23",
  cap("The chair got invited before you did. \U0001F383",
      "EP. 30: the official party invitations went out. Mrs. Never Wrong got hers, the intern appeared out of nowhere already holding his, and somehow Lil Wobbles had one propped against his leg. Nobody confessed. The decree came down, everyone is invited, and the cat claimed the spare stack as a bed. Oct 31, everybody is coming. Who else gets an invite? Wrong answers only.",
      "#thebigbusinesschronicles #halloweenparty #comedy #lasvegas #funnyreels"),
  "EP. 30: The Invitations \U0001F383 even the chair is coming #Shorts",
  "THE BIG BUSINESS CHRONICLES: the invites went out and somehow the villain chair got one. Everyone is invited, Oct 31. Record: 3 wins, 13 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
