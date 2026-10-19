"""Queue FRIDAY OCT 23 videos: trend 5pm, pink 6pm (story FB/IG), EP32 8pm. Run AFTER push."""
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

D = "2026-10-23T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_CatJudges.mp4", "reel", "23",
  cap("The toughest judge on the internet rated our setups. \U0001F408",
      "You know the black cat reaction format. Ours judged four exhibits: the budget chair got an instant no, the neighbor's dying table got personally insulted, a real setup earned a slow nod, and delivery day got actual applause. Even the harshest critic in the business approves. Book your own. Send this to somebody whose pet judges their life choices.",
      "#blackcat #catsoftiktok #funnyreels #lasvegas #partyrentals"),
  "The black cat judged our party setups \U0001F408 #Shorts",
  "Budget chair: no. Neighbor's table: insulted. Delivery day: applause. The toughest critic approves. Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #BlackCat #Funny #PartyRentals #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_OneMinute.mp4", "story", "22",
  cap("October is almost over. This takes one minute. \U0001F380",
      "Before the month ends, run the one-minute checklist: book or confirm your next screening, ask both sides of the family about history, and set a monthly self-check reminder. Then forward this to two people you love, because awareness only works when it travels. Source: American Cancer Society.",
      "#breastcancerawareness #pinkoctober #checklist #screening #lasvegas"),
  "The one-minute Pink October checklist \U0001F380 #Shorts",
  "Book the screening, ask both sides about family history, set a monthly reminder, tell two people. One minute. Source: American Cancer Society.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #Checklist #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep32_TheSupplyRun.mp4", "reel", "23",
  cap("He ordered party supplies. Every box was a chair. \U0001F4E6",
      "EP. 32: the finale supplies arrived, and box after box held one red folding chair. The suspect did a slow drive-by, the actual candy was one sad bag, Mrs. Never Wrong ordered returns, Tyler was inside box two the whole time, and the cat signed for everything. Record falls to 3 and 15. What should he order instead? Wrong answers only.",
      "#thebigbusinesschronicles #halloweenparty #comedy #lasvegas #funnyreels"),
  "EP. 32: The Supply Run \U0001F4E6 every box was a chair #Shorts",
  "THE BIG BUSINESS CHRONICLES: the finale order arrived and the villain filled it. One candy bag, three chairs, zero explanations. Record: 3 wins, 15 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
