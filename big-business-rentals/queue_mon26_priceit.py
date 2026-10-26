"""Monday Oct 26 2pm PRICE IT (weekly promotions, Flyer 2026 design) on Facebook + Instagram feed.
Owner approved: "queue it for 2pm"."""
import time
from queue_everywhere_oct24 import CH, RAW, FB_PIN, M, gql
IMG = RAW + "big-business-rentals/flyers2026/BB26_PriceIt_HalloweenGala.png"
DUE = "2026-10-26T14:00:00-07:00"
IG_PIN = "Follow for more Las Vegas party setups."
POSTS = [
 ("fb", "be honest: how much would you pay for this halloween dinner setup? 🎃 the tables, chairs and the room underneath it, that part is us.\n\n#lasvegas #halloweenparty #eventrentals #partysetup #setupinspo",
  {"facebook": {"type": "post", "firstComment": FB_PIN}}),
 ("ig", "How much would you pay for this Las Vegas Halloween dinner setup? Setup inspo: the tables, chairs and the room underneath it are the part we bring. 🎃\n\n#lasvegas #halloweenparty #partyrentals #eventdecor #setupinspo",
  {"instagram": {"type": "post", "shouldShareToFeed": True, "firstComment": IG_PIN}}),
]
for ch, text, md in POSTS:
    d = gql(M, {"input": {"channelId": CH[ch], "text": text, "mode": "customScheduled", "dueAt": DUE,
                          "schedulingType": "automatic", "assets": [{"image": {"url": IMG}}], "metadata": md}})
    res = (d.get("data") or {}).get("createPost") or {}
    print("OK  " if res.get("__typename") == "PostActionSuccess" else "FAIL", ch, res.get("post", {}).get("id") or str(d)[:300])
    time.sleep(3)
