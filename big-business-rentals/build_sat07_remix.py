"""Saturday Nov 7 TREND REMIX #20 "The Recount" (reelH REELS[43], 17.2s, full Season Two cast). OWNER-PICKED (Nov 5:
"and then politics one"), sequel to the Red Party Blue Party remix (owner-approved politics override). Strictly
nonpartisan: party THEMES only; no candidates, real party names, races, results, lawsuits or voting info; both sides
identical (36 and 36); no character placed on a side; Lil Wobbles is "not from either party" and is turned away from our
truck. Gag: Unc's recount comes up 35-35 because he sits on a chair each time; Tyler points it out.
UPGRADES: counters that drop and recover mid-video, a drop-in entrance for Lil Wobbles, one-van pickup with the full cast."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T43 = BASE/'halloween/BB_Trend_TheRecount.mp4'
def cues(add):
    add(kit('pop'), 0.05)
    add(bed(14.0, 100, 'sneak'), 0.2, 0.45)
    for i in range(12): add(tone(1100+(i%6)*90, 0.04, 0.15), 2.9+i*0.17)        # counting ticks, both sides
    add(kit('sneak'), 5.6, 0.5); add(kit('freeze'), 6.62); add(kit('sadtrom'), 6.8, 0.5)
    add(kit('pop2'), 7.4, 0.8); add(kit('rimshot'), 8.0, 0.5); add(kit('win'), 8.6, 0.6)
    add(kit('whoosh'), 9.6, 0.6); add(kit('kick'), 10.8, 0.7)                     # Wobbles drops, folds
    add(kit('whoosh'), 11.2, 0.6); add(kit('applause'), 11.6, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 43, 17.2, 16.7, T43, cues)
