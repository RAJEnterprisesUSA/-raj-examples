"""Queue TUESDAY OCT 20 videos: trend 5pm, pink 6pm (story FB/IG), EP29 8pm. Run AFTER push."""
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

D = "2026-10-20T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_FaceRating.mp4", "reel", "23",
  cap("Rating party setups with my face only. \U0001F610",
      "The fresh setup got the good face. The budget chair got concern. The uninvited guest got the long stare, and delivery day got the face that says book it. No words needed, the setup speaks. Send this to somebody whose face hides nothing.",
      "#myreaction #trending #funnyreels #lasvegas #partyrentals"),
  "Rating party setups with my face only \U0001F610 #Shorts",
  "The fresh setup, the budget chair, the uninvited guest, and delivery day. No words needed. Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #MyReaction #FunnyShorts #PartyRentals #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_FamilyTree.mp4", "story", "22",
  cap("Your family history has two sides. \U0001F380",
      "Breast cancer history can pass through either parent, so ask about aunts and grandmothers on both sides, and the men in your tree count too. Write it down and bring the list to your doctor: one honest family conversation can change your screening timeline. Send this to the family historian. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #familyhistory #knowyourrisk #lasvegas"),
  "Dad's side counts too. \U0001F380 #Shorts",
  "Family history of breast cancer can pass through either parent. Ask both sides, write it down, bring it to your doctor. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #FamilyHistory #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep29_ThePumpkinCarve.mp4", "reel", "23",
  cap("The intern won without touching a knife. \U0001F383",
      "EP. 29: the annual pumpkin carve. He had a vision, Wobbles used his head, literally, and Tyler's pumpkin showed up perfect without anybody seeing him carve it. The intern wins again and the record falls to 3 and 12. What should he carve next? Wrong answers only.",
      "#thebigbusinesschronicles #pumpkincarving #comedy #lasvegas #funnyreels"),
  "EP. 29: The Pumpkin Carve \U0001F383 the intern strikes again #Shorts",
  "THE BIG BUSINESS CHRONICLES: one masterpiece, one headbutt, one pumpkin that carved itself. Record: 3 wins, 12 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
