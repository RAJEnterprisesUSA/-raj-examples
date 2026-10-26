"""Tuesday Oct 27 1pm VENUE FLYER (weekly promotions, Flyer 2026 design): Facebook feed post + Instagram Story.
Owner approved: "queue it for 1pm"."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, M, gql
F = RAW + "big-business-rentals/flyers2026/"
DUE = "2026-10-27T13:00:00-07:00"
FB_TEXT = ("Skip the house this year. Book the room.\n\n"
           "Our private venue in Las Vegas seats 40 and holds 80 standing, with tables, chairs and setup included. "
           "Three hours is $625 for up to 25 guests, and four hours is $800 for up to 40. Birthdays, holiday dinners, "
           "baby showers, company parties: the room is ready when you are. Questions? The chat on our website answers right away.\n\n"
           "#LasVegasVenue #VegasEventSpace #LasVegasParty #VegasPartyRentals #HolidayPartyVegas")
POSTS = [
 ("fb", FB_TEXT, F + "BB26_Venue_Tue27.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_Venue_Tue27_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
for ch, text, img, md in POSTS:
    d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": DUE,
                          "schedulingType": "automatic", "assets": [{"image": {"url": img}}], "metadata": md}})
    res = (d.get("data") or {}).get("createPost") or {}
    print("OK  " if res.get("__typename") == "PostActionSuccess" else "FAIL", ch, res.get("post", {}).get("id") or str(d)[:300])
    time.sleep(3)
