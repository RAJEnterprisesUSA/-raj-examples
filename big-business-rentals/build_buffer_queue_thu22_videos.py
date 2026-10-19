"""Queue THURSDAY OCT 22 videos: trend 5pm, pink 6pm (story FB/IG), EP31 8pm. Run AFTER push."""
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

D = "2026-10-22T{:02d}:00:00-07:00"

VIDEOS = [
 (17, "big-business-rentals/halloween/BB_Trend_RocketDelivery.mp4", "reel", "23",
  cap("Our delivery van saw the flying roadster news. \U0001F680",
      "Everybody is talking about a roadster that flies, so our delivery van decided traffic is optional: instant launch, mid-air parallel parking, soft landing, tables and chairs placed right on time. Delivered and picked up anywhere in Las Vegas, full-service setup available. The setup arrives, whatever it takes. Send this to somebody who is always stuck in traffic.",
      "#funnyreels #trending #delivery #lasvegas #partyrentals"),
  "The delivery van saw the flying roadster news \U0001F680 #Shorts",
  "Instant launch, mid-air parking, soft landing, party delivered. The setup arrives, whatever it takes. Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Funny #PartyRentals #Delivery #LasVegas"),
 (18, "big-business-rentals/awareness/BB_PinkOctober_NoCost.mp4", "story", "22",
  cap("A mammogram should not depend on a paycheck. \U0001F380",
      "Free and low-cost mammograms are real: the CDC early detection program runs in every state for people without insurance, and dialing 211 can point you to one nearby. Somebody you love is skipping a screening over the cost, so send them this. One call can book a free one. No cost, no excuses. Source: CDC.",
      "#breastcancerawareness #pinkoctober #freemammogram #earlydetection #lasvegas"),
  "Free mammograms exist. Pass it on. \U0001F380 #Shorts",
  "No insurance? The CDC early detection program offers free and low-cost screenings in every state. Dial 211 to find one. Source: CDC.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #PinkOctober #BreastCancerAwareness #EarlyDetection #LasVegas"),
 (20, "fb_safe/BB_Chronicles_Ep31_TheDryRun.mp4", "reel", "23",
  cap("The room was perfect for exactly two seconds. \U0001F383",
      "EP. 31: the finale dry run. Every chair had an assignment, the inspector approved, and the room was ready eight days early, until the cat jumped on the table and sent the centerpiece pumpkin flying. Lil Wobbles snuck into the seating row again, Tyler completed it somehow, and the record falls to 3 and 14. What goes wrong at the finale? Predictions below.",
      "#thebigbusinesschronicles #halloweenparty #comedy #lasvegas #funnyreels"),
  "EP. 31: The Dry Run \U0001F383 perfect for two seconds #Shorts",
  "THE BIG BUSINESS CHRONICLES: the finale rehearsal passed inspection, then the cat happened. Record: 3 wins, 14 losses. New episodes daily in Las Vegas, NV.\n\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\nIG: @bigbusiness_rentals_events\n#Shorts #Comedy #Sitcom #FunnyShorts #LasVegas #PartyRentals"),
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
