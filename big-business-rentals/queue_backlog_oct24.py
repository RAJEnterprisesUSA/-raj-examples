"""Owner Oct 24, "Post them all now": catch up every episode and remix from this week on the
platforms that missed them. Episodes go today on Facebook and TikTok in story order, ahead of EP. 33
at 8pm; remixes go Sunday, ahead of EP. 34 at 8pm. Same caption rules and pinned comments as
queue_everywhere_oct24.py (imported from there)."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql

EP = "fb_safe/BB_Chronicles_Ep{}.mp4"
TR = "big-business-rentals/halloween/BB_Trend_{}.mp4"
SAT, SUN = "2026-10-24T{}:00-07:00", "2026-10-25T{}:00-07:00"
POSTS = [
 ("fb", SAT.format("13:30"), EP.format("29_ThePumpkinCarve"),
  "the big business chronicles ep. 29: halloween party prep means a pumpkin carve, and the intern wins without touching a knife. 🎃\n\n#lasvegas #halloweenparty #animation #comedy"),
 ("tt", SAT.format("13:30"), EP.format("29_ThePumpkinCarve"),
  "The Big Business Chronicles EP. 29: the intern won the pumpkin carve without touching a knife. 🎃\n\n#thebigbusinesschronicles #pumpkincarving #halloween #comedy"),
 ("fb", SAT.format("14:30"), EP.format("30_TheInvitations"),
  "the big business chronicles ep. 30: the halloween party invitations went out, and somehow the cheap chair got one. 🎃\n\n#lasvegas #halloweenparty #animation #comedy"),
 ("tt", SAT.format("14:30"), EP.format("30_TheInvitations"),
  "The Big Business Chronicles EP. 30: the invitations went out. Somehow the cheap chair got one. 🎃\n\n#thebigbusinesschronicles #halloweenparty #animation #comedy"),
 ("fb", SAT.format("15:30"), EP.format("31_TheDryRun"),
  "the big business chronicles ep. 31: the halloween party dry run was perfect for exactly two seconds. 🎃\n\n#lasvegas #halloweenparty #animation #comedy"),
 ("tt", SAT.format("15:30"), EP.format("31_TheDryRun"),
  "The Big Business Chronicles EP. 31: the dry run was perfect for exactly two seconds. 🎃\n\n#thebigbusinesschronicles #halloween #animation #comedy"),
 ("fb", SAT.format("18:30"), EP.format("32_TheSupplyRun"),
  "the big business chronicles ep. 32: he ordered the halloween party supplies, and every single box was a chair. 📦\n\n#lasvegas #halloweenparty #animation #comedy"),
 ("tt", SAT.format("18:30"), EP.format("32_TheSupplyRun"),
  "The Big Business Chronicles EP. 32: he ordered party supplies. Every box was a chair. 📦\n\n#thebigbusinesschronicles #halloween #animation #comedy"),
 # Sunday remixes
 ("tt", SUN.format("09:00"), TR.format("FaceRating"),
  "Rating party setups with my face only. 😐\n\n#partysetup #reaction #lasvegas #animation"),
 ("fb", SUN.format("11:00"), TR.format("GettingRobbed"),
  "robbed in broad daylight and he never looked up. 👀\n\n#lasvegas #halloween #animation #comedy"),
 ("ig", SUN.format("11:00"), TR.format("GettingRobbed"),
  "Robbed in broad daylight at a Las Vegas Halloween setup, and he never looked up. 👀\n\n#lasvegas #halloweenparty #animation #comedy #partyrentals"),
 ("tt", SUN.format("11:00"), TR.format("GettingRobbed"),
  "Robbed in broad daylight. He never looked up. 👀\n\n#robbedinbroaddaylight #halloween #animation #lasvegas"),
 ("fb", SUN.format("15:00"), TR.format("RocketDelivery"),
  "the delivery van saw the flying roadster news and took it personally. 🚀\n\n#lasvegas #delivery #animation #comedy"),
 ("ig", SUN.format("15:00"), TR.format("RocketDelivery"),
  "The party delivery van saw the flying roadster news, and Las Vegas rush hour never stood a chance. 🚀\n\n#lasvegas #flyingcar #animation #comedy #partyrentals"),
 ("tt", SUN.format("15:00"), TR.format("RocketDelivery"),
  "The delivery van saw the flying roadster news. 🚀\n\n#flyingcar #lasvegas #animation #comedy"),
 ("fb", SUN.format("17:00"), TR.format("CatJudges"),
  "the toughest critic in las vegas judged our party setups. only one got applause. 🐈‍⬛\n\n#lasvegas #blackcat #animation #comedy"),
 ("ig", SUN.format("17:00"), TR.format("CatJudges"),
  "The black cat judged four Las Vegas party setups, and only one got applause. 🐈‍⬛\n\n#lasvegas #blackcat #halloween #animation #comedy"),
 ("tt", SUN.format("17:00"), TR.format("CatJudges"),
  "The black cat judges party setups. 🐈‍⬛\n\n#blackcat #halloween #animation #lasvegas"),
]

if __name__ == "__main__":
    ok = 0
    for ch, due, path, text in POSTS:
        inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
               "schedulingType": "automatic", "assets": [{"video": {"url": RAW + path}}]}
        if ch == "fb":
            inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
        elif ch == "ig":
            inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": IG_PIN_TREND}}
        d = gql(M, {"input": inp})
        res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"
        ok += good
        print("OK  " if good else "FAIL", ch, due, path.rsplit("/", 1)[-1],
              res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{len(POSTS)} queued")
