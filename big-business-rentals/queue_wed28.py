"""Wednesday Oct 28: TREND REMIX #10 Very Serious Opinions (5pm) and EP. 37 The Place Cards (8pm) on
all four platforms, now with designed covers (UPGRADE: video thumbnailUrl)."""
import time, json
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_EP, IG_PIN_TREND, M, gql

T = "big-business-rentals/halloween/BB_Trend_VerySeriousOpinions.mp4"
E = "fb_safe/BB_Chronicles_Ep37_ThePlaceCards.mp4"
TC = "big-business-rentals/covers/BB_Cover_Trend_VerySeriousOpinions.png"
EC = "big-business-rentals/covers/BB_Cover_Ep37_ThePlaceCards.png"
D5, D8 = "2026-10-28T17:00:00-07:00", "2026-10-28T20:00:00-07:00"
POSTS = [
 ("fb", D5, T, TC, "mrs. never wrong's very serious party opinions. she does not take questions. 🎤\n\n#twofishes #partyopinions #lasvegas #animation #comedy", None),
 ("ig", D5, T, TC, "Mrs. Never Wrong's very serious opinions on Las Vegas party seating. She does not take questions. 🎤\n\n#twofishes #partyplanning #lasvegas #partyrentals #comedy", IG_PIN_TREND),
 ("tt", D5, T, TC, "Very serious opinions. Zero follow-up questions. 🎤\n\n#twofishes #deadpan #partyrentals #lasvegas", None),
 ("yt", D5, T, TC, "A party without enough chairs is just a long meeting. Mrs. Never Wrong has spoken.\n\n#twofishes #deadpan #comedy",
  "Very serious party opinions (no questions) 🎤 #Shorts"),
 ("fb", D8, E, EC, "the big business chronicles ep. 37: 42 place cards, one swap war, and a surprise at the head table. 🪑\n\n#lasvegas #halloweenparty #animation #comedy", None),
 ("ig", D8, E, EC, "The Big Business Chronicles EP. 37: the Las Vegas Halloween party place cards were final, and the head table went to the cat. 🐈‍⬛\n\n#thebigbusinesschronicles #lasvegas #halloweenparty #seatingchart #comedy", IG_PIN_EP),
 ("tt", D8, E, EC, "The Big Business Chronicles EP. 37: the place card swap war. Nobody saw the winner coming. 🐈‍⬛\n\n#thebigbusinesschronicles #seatingchart #halloween #comedy", None),
 ("yt", D8, E, EC, "The Big Business Chronicles EP. 37: the place card swap war ended with a surprise at the head table. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
  "EP. 37: The Place Cards 🐈‍⬛ the swap war #Shorts"),
]
if __name__ == "__main__":
    ok = 0
    for ch, due, path, cover, text, extra in POSTS:
        def build(with_cover):
            v = {"url": RAW + path}
            if with_cover: v["thumbnailUrl"] = RAW + cover
            inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
                   "schedulingType": "automatic", "assets": [{"video": v}]}
            if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
            elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
            elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
            return inp
        d = gql(M, {"input": build(True)}); res = (d.get("data") or {}).get("createPost") or {}
        cov = "cover"
        if res.get("__typename") != "PostActionSuccess":
            print("  cover rejected on", ch, json.dumps(d)[:200]); cov = "no cover"
            d = gql(M, {"input": build(False)}); res = (d.get("data") or {}).get("createPost") or {}
        good = res.get("__typename") == "PostActionSuccess"; ok += good
        print("OK  " if good else "FAIL", ch, due, path.rsplit("/", 1)[-1], cov, res.get("post", {}).get("id") if good else str(d)[:300])
        time.sleep(3)
    print(f"{ok}/{len(POSTS)} queued")
