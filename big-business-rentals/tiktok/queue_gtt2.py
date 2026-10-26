"""Guess the Theme No. 2 (Dia de los Muertos) on TikTok: Pt. 1 Wed Oct 28 1pm, Pt. 2 Thu Oct 29 1pm.
Owner approved: "queue both for 1pm". AI label ON (photoreal AI concept art). Instagram = Trial Reels the owner posts."""
import sys, time, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from queue_everywhere_oct24 import CH, RAW, M, gql
V = RAW + "big-business-rentals/tiktok/"
POSTS = [
 ("2026-10-28T13:00:00-07:00", "TT_GuessTheTheme_DiaDeMuertos_Pt1.mp4",
  "Three clues, one party theme. Can you get it before clue 3?\n\n#guessthetheme #partytheme #partyinspo #lasvegas"),
 ("2026-10-29T13:00:00-07:00", "TT_GuessTheTheme_DiaDeMuertos_Pt2.mp4",
  "Día de los Muertos, the celebration that honors the people we love. Marigold runners, papel picado and sugar skulls, all in one room. Who got it on clue 1?\n\n#guessthetheme #diadelosmuertos #partyinspo #lasvegas"),
]
for due, f, text in POSTS:
    d = gql(M, {"input": {"channelId": CH["tt"], "text": text, "mode": "customScheduled", "dueAt": due,
                          "schedulingType": "automatic", "assets": [{"video": {"url": V + f}}],
                          "metadata": {"tiktok": {"isAiGenerated": True}}}})
    res = (d.get("data") or {}).get("createPost") or {}
    print("OK  " if res.get("__typename") == "PostActionSuccess" else "FAIL", f, res.get("post", {}).get("id") or str(d)[:300])
    time.sleep(3)
