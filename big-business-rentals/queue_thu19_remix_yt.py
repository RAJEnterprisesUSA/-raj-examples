"""Thu Nov 19 5pm TREND REMIX #30 "Push It 7 Inches", YouTube Short ONLY. The buffer_queue_post tool has no categoryId field and Buffer
rejects YouTube posts without one ("YouTube posts require a category"), so this was NOT queued by Hail. FB, IG and TikTok are queued.
Run by the owner or an agent that has direct Buffer API access:  python3 queue_thu19_remix_yt.py 2026-11-19T17:00:00-08:00"""
import sys
from queue_everywhere_oct24 import CH, RAW, M, gql
T = "big-business-rentals/halloween/BB_Trend_PushSevenInches.mp4"
TITLE = "Everyone is pushing landmarks 7 inches. We tried a table 😄 #Shorts"
TEXT = "The landmark moved 0 inches. Our table moved 7. Setup and teardown crews move things on request all day.\n\n#comedy #partyrentals #lasvegas"
if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].startswith("2026-"): sys.exit("pass dueAt, e.g. 2026-11-19T17:00:00-08:00")
    inp = {"channelId": CH["yt"], "text": TEXT, "mode": "customScheduled", "dueAt": sys.argv[1], "schedulingType": "automatic",
           "assets": [{"video": {"url": RAW + T}}],
           "metadata": {"youtube": {"title": TITLE, "categoryId": "23", "privacy": "public", "madeForKids": False}}}
    d = gql(M, {"input": inp}); res = (d.get("data") or {}).get("createPost") or {}
    print("OK" if res.get("__typename") == "PostActionSuccess" else "FAIL", res.get("post", {}).get("id") or str(d)[:300])
