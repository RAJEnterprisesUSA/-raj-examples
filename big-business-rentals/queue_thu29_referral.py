"""Thursday Oct 29 1pm REFERRAL FLYER (weekly promotions, Flyer 2026, hair stylists): Facebook feed post + Instagram Story.
Owner approved: "queue it for 1pm"."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, M, gql
F = RAW + "big-business-rentals/flyers2026/"
DUE = "2026-10-29T13:00:00-07:00"
FB_TEXT = ("Hair stylists in Las Vegas: your clients tell you about every party before anyone else hears about it.\n\n"
           "Point them to Big Business for their tables, chairs and setup, and you can earn up to $100 for every booking. "
           "The reward is based on booking size, there is no limit on referrals, and you get paid after their event is completed. "
           "Questions? The chat on our website answers right away.\n\n"
           "#LasVegasHairStylist #VegasStylist #LasVegasSalon #VegasPartyRentals #LasVegasEvents")
POSTS = [
 ("fb", FB_TEXT, F + "BB26_Referral_Thu29.png", {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "", F + "BB26_Referral_Thu29_Story.png", {"instagram": {"type": "story", "shouldShareToFeed": False}}),
]
for ch, text, img, md in POSTS:
    d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": DUE,
                          "schedulingType": "automatic", "assets": [{"image": {"url": img}}], "metadata": md}})
    res = (d.get("data") or {}).get("createPost") or {}
    print("OK  " if res.get("__typename") == "PostActionSuccess" else "FAIL", ch, res.get("post", {}).get("id") or str(d)[:300])
    time.sleep(3)
