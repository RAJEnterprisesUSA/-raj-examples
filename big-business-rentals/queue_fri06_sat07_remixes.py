"""Trend remixes: Fri Nov 6 5pm "Race week vs. locals" and Sat Nov 7 5pm "The Recount", all four platforms (PST -08:00).
Run ONLY after the owner approves. Pass 'fri' and/or 'sat' to queue only those days.
Nov 7: owner moved the race-week remix ("fri" key) to Sun Nov 8 5pm after the Friday slot went unapproved."""
import sys, time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, IG_PIN_TREND, M, gql
SETS = {
 "fri": ("2026-11-08T17:00:00-08:00", "big-business-rentals/halloween/BB_Trend_RaceWeekVsLocals.mp4", [
   ("fb", "race week is back in vegas. team love the race or team just get me home? 🏁\n\n#lasvegas #raceweek #vegaslocals #partyrentals #comedy", None),
   ("ig", "Race week is back in Las Vegas: road closures, detours and one very confident uncle with a shortcut. Skip the Strip and throw the party at home. 🏁\n\n#lasvegas #raceweek #vegaslocals #partyrentals #comedy", IG_PIN_TREND),
   ("tt", "Race week in Vegas. Whose side are you on? 🏁\n\n#lasvegas #raceweek #vegaslocals #comedy", None),
   ("yt", "Road closures, a shortcut that wasn't, and a party that moved home. Skip the Strip.\n\n#lasvegas #raceweek #comedy", "Race week in Vegas: whose side are you on? 🏁 #Shorts")]),
 "sat": ("2026-11-07T17:00:00-08:00", "big-business-rentals/halloween/BB_Trend_TheRecount.mp4", [
   ("fb", "the election's over. somebody still has to return the chairs. 36 and 36, every time. 🪑\n\n#lasvegas #recount #partyrentals #animation #comedy", None),
   ("ig", "The election's over, and somebody still has to return the chairs. The recount came out 36 and 36 once we found the chair Unc was sitting on. 🪑\n\n#recount #lasvegas #partyrentals #animation #comedy", IG_PIN_TREND),
   ("tt", "The recount. Unc was sitting on one. 🪑\n\n#recount #comedy #partyrentals #fyp", None),
   ("yt", "The red party and the blue party both returned their chairs. The recount is 36 and 36.\n\n#recount #comedy #partyrentals", "The recount: 36 and 36 🪑 #Shorts")]),
}
if __name__ == "__main__":
    days = [d for d in ("fri", "sat") if d in sys.argv] or ["fri", "sat"]
    for day in days:
        due, path, posts = SETS[day]; ok = 0
        for ch, text, extra in posts:
            inp = {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": due,
                   "schedulingType": "automatic", "assets": [{"video": {"url": RAW + path}}]}
            if ch == "fb": inp["metadata"] = {"facebook": {"type": "reel", "firstComment": FB_PIN}}
            elif ch == "ig": inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "firstComment": extra}}
            elif ch == "yt": inp["metadata"] = {"youtube": {"title": extra, "categoryId": "23", "privacy": "public", "madeForKids": False}}
            d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
            good = res.get("__typename") == "PostActionSuccess"; ok += good
            print("OK  " if good else "FAIL", day, ch, due, res.get("post", {}).get("id") if good else str(d)[:300]); time.sleep(3)
        print(f"{day}: {ok}/4 queued")
