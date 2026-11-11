"""Wednesday Nov 11 TREND REMIX #25 "Answer in One Word" (reelH REELS[50], 25.2s, readable holds). Fresh build Tue Nov 10 night
(owner: "Build a fresh wed remix"). SOCIAL pool: TikTok's "Answer in One Word" format (questions that may only be answered with
one word; trend trackers, week of Nov 10 2026). Lil Big Business holds the mic and interviews the full cast under a spotlight:
CAT. / NO. (Mrs. Never Wrong) / SIDEWAYS. (Unc) / INTERN. (Tyler) / EMBARRASSING. (Vaeh) / ALL. (Baby, chair stack) / NOPE. (Lil
Wobbles folds) / THRONE. (Princess) / US. (Dad: who brings the tables and chairs?) and nine chairs pop in.
UPGRADES: spotlight on each answerer + speech-bubble answers that auto-fit the frame + "ANSWER IN ONE WORD" format chip."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_AnswerInOneWord.mp4'
BEATS = [0, 2.6, 5.0, 7.4, 9.8, 12.2, 14.6, 17.0, 19.4]
def cues(add):
    add(bed(21.6, 100, 'groove'), 0.2, 0.40)
    for b in BEATS: add(kit('whoosh'), b + 0.05, 0.35); add(kit('pop2'), b + 0.9, 0.75)   # question, then the one-word answer
    add(kit('pop2'), 7.4, 0.6)                                                             # Tyler pops up
    add(kit('kick'), 15.5, 0.8)                                                            # Lil Wobbles folds
    for i in range(9): add(kit('pop'), 20.5 + i * 0.1, 0.45)
    add(kit('win'), 20.3, 0.7); add(kit('applause'), 20.5, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 50, 25.2, 24.7, OUT, cues)
