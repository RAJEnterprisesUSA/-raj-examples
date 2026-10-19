"""Queue MONDAY OCT 19 videos: TREND REMIX 5pm (all 4 channels, debut), pink 6pm
(story FB/IG + TT + YT), EP28 8pm (all 4). Run AFTER mp4s are committed and pushed."""
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

D = "2026-10-19T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_CostumeWalk.mp4", "reel", "23",
  cap("The costume walk. Everybody is doing it. \U0001F383",
      "Even the chair understood the assignment: full dramatic slow walk, cape, hat, overtaken by the cat halfway down the runway. The real reveal is the setup behind it. We deliver the whole scene, tables, chairs and all. Send this to the most dramatic person you know.",
      "#costumewalk #halloween #trending #lasvegas #partyrentals"),
  "The costume walk, but make it furniture \U0001F383 #Shorts",
  "The dramatic slow walk, the cape, the reveal. Even the chair is doing the trend, and the real reveal is the party setup behind it. Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #CostumeWalk #Halloween #FunnyShorts #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_TheCallback.mp4", "story", "22",
  cap("Got called back after a screening? Breathe. \U0001F380",
      "A callback is not a diagnosis. Often they just need a clearer image, and most callbacks are not cancer. The only wrong move is skipping the follow-up: take somebody with you, ask questions, write the answers down. Send this to somebody waiting on that letter. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #mammogram #thecallback #lasvegas"),
  "A callback is not a diagnosis. \U0001F380 #Shorts",
  "Most screening callbacks are not cancer, often they just need a clearer image. The only wrong move is skipping the follow-up. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #TheCallback #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep28_TheTasteTest.mp4", "reel", "23",
  cap("He invented the decoy. They learned it. \U0001F63C",
      "EP. 28, now in extended cut: three secret menu samples, one very loud red distraction at the door, and one cat already on the table. The student became the teacher and the record falls to 3 and 11. What snack would you guard with your life?",
      "#thebigbusinesschronicles #comedy #lasvegas #funnyreels #decoy"),
  "EP. 28: The Taste Test \U0001F63C his own decoy #Shorts",
  "THE BIG BUSINESS CHRONICLES, extended cut: three menu samples, one loud distraction, one cat already eating. Record: 3 wins, 11 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
