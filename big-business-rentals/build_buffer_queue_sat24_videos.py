"""Queue SATURDAY OCT 24 videos: trend 5pm, pink 6pm (story FB/IG), EP33 8pm. Run AFTER push."""
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

D = "2026-10-24T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_PorchReveal.mp4", "reel", "23",
  cap("The porch reveal, but make it make money. \U0001F383",
      "You know the Halloween porch reveal format: the slow sweep, the classics, the skeleton greeter. Ours ends on the part everybody forgets, real seating. Decor gets the views, seating keeps the guests, and the tables and chairs come delivered and picked up anywhere in Las Vegas. Send this to the house that wins Halloween every year.",
      "#porchreveal #halloween #trending #lasvegas #partyrentals"),
  "The Halloween porch reveal with the real secret \U0001F383 #Shorts",
  "Pumpkins, skeleton, candy station, and the part everybody forgets: real seating. Delivered in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Halloween #PorchReveal #PartyRentals #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_AskThese.mp4", "story", "22",
  cap("Your next screening deserves questions. \U0001F380",
      "At the appointment, ask these three: is my breast tissue dense and what does that mean, when exactly is my next screening due, and what changes should I watch for at home. Then ask how results arrive and write the answers in your phone. Good questions save lives. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #askquestions #screening #lasvegas"),
  "Three questions to ask at your screening \U0001F380 #Shorts",
  "Dense tissue, next due date, changes to watch for. Write the answers down. Good questions save lives. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #AskQuestions #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep33_TheLightCheck.mp4", "reel", "23",
  cap("Every bulb worked. Then the cat found the outlet. \U0001F4A1",
      "EP. 33: finale lights. The tangle fought back, caught a red chair, and turned it into a chandelier with opinions. The inspector said higher, the intern pre-lit his corner, and for one shining moment every bulb worked on the first try. Then the cat found the outlet. One light survived, and it was the wrong one. Record: 3 and 16. Caption the cat's thoughts, best one gets credited.",
      "#thebigbusinesschronicles #halloweenparty #comedy #lasvegas #funnyreels"),
  "EP. 33: The Light Check \U0001F4A1 the cat found the outlet #Shorts",
  "THE BIG BUSINESS CHRONICLES: perfect lights, one outlet, one cat. One light survived and it was the wrong one. Record: 3 wins, 16 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
