"""Queue the Bring To The Table sketch: Monday Oct 19, 10am Vegas, business slot.
FB reel + IG reel (cross-linked firstComments) + YouTube (cat 23). NOT TikTok:
the 4-post TikTok cap belongs to Monday's gag, pink, episode and PRICE IT."""
import json, subprocess, time

API = "https://api.buffer.com"
RAW = "https://raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/"
CH = {"fb": "6aabfb63ea19ca0bde696947", "ig": "6aabfaf0ea19ca0bde6965d6",
      "yt": "6ac2ff576a5c39ccb618d238"}
CONTACT = "\U0001F4DE 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com"
FC_FB = ("If you're planning anything this season, follow us on Instagram too. "
         "Real setups, open dates, and what's available before it books up.\n"
         "instagram.com/bigbusiness_rentals_events")
FC_IG = ("Follow @bigbusiness_rentals_events for real setups and open dates. "
         "Booking December now. We are on Facebook too: "
         "facebook.com/profile.php?id=61589138907701")

TEXT = ("So what do you bring to the table?\n\n"
        "The tables. He understood the assignment: white folding tables, white folding chairs "
        "and white round tables, delivered, set up and picked up all over Las Vegas. Send this "
        "to somebody whose answer would be the same, or comment QUOTE and we will DM you a price today.\n\n"
        + CONTACT + "\n\n"
        "#datenight #partyrentals #funnyreels #lasvegas #tablesandchairs")
YT_TITLE = "What do you bring to the table? \U0001F602 #Shorts"
YT_TEXT = ("She asked what he brings to the table. He brought the actual tables. White folding "
           "tables, folding chairs and round tables, delivered and set up all over Las Vegas, NV.\n"
           "\U0001F4DE 702-706-8287 · Free quotes at bigbusinesspartyrentals.com\n"
           "IG: @bigbusiness_rentals_events\n"
           "#Shorts #FunnyShorts #DateNight #PartyRentals #LasVegas")

MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
 ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""

def gql(inp):
    body = json.dumps({"query": MUT, "variables": {"input": inp}})
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API,
                        "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

def create(channel, text, yt_title=None):
    inp = {"channelId": CH[channel], "text": text, "mode": "customScheduled",
           "schedulingType": "automatic", "dueAt": "2026-10-19T10:00:00-07:00",
           "assets": [{"video": {"url": RAW + "big-business-rentals/user-videos/BB_BringToTable_V.mp4"}}]}
    if channel == "fb":
        inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FC_FB}}
    elif channel == "ig":
        inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True,
                                         "firstComment": FC_IG}}
    elif channel == "yt":
        inp["metadata"] = {"youtube": {"title": yt_title, "madeForKids": False,
                                       "privacy": "public", "categoryId": "23"}}
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

if __name__ == "__main__":
    print(create("fb", TEXT), "FB  BB_BringToTable")
    print(create("ig", TEXT), "IG  BB_BringToTable")
    print(create("yt", YT_TEXT, YT_TITLE), "YT  BB_BringToTable")
