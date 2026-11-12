"""TREND REMIX #28 "The Spy, Part 2: Target Big Business" (reelH REELS[53], 23.0s, speech clouds, cast by story). Owner Thu Nov 12:
"then we will do a part two of this video, of a spy trying to infiltrate big business. But is not successful. And that'll be a win
for Mr. Big Business." THE SPY returns (original character, face hidden, no nationality/ethnicity cues): mustache disguise (Mrs.
Never Wrong: "NORMAL GUESTS DON'T WEAR A SPY HAT."), chair disguise (the cat sits on her, ACHOO!), the TOP SECRET plans are a seating
chart (Dad: "NO SECRETS. EVERYTHING'S ON OUR PRICE CARD."), she asks Tyler where he came from, Baby blocks the door, she books a
table. Payoff: SPY 0 · BIG BUSINESS 1 (a WIN). UPGRADES: disguise gags + live scoreboard; series continuity (Part 1 -> Part 2)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_SpyPart2_TargetBigBusiness.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.6); add(bed(19.6, 100, 'groove'), 0.3, 0.38)
    add(kit('pop'), 2.6, 0.5); add(kit('rimshot'), 3.6, 0.4)
    add(kit('whoosh'), 5.0, 0.5); add(kit('sneak'), 5.6, 0.4); add(noise(0.25, 0.4, lp=0.4), 6.6); add(kit('boing'), 6.7, 0.6)
    add(kit('whoosh'), 7.4, 0.5); add(kit('pop'), 8.4, 0.5); add(kit('rimshot'), 8.6, 0.4)
    add(kit('pop2'), 9.8, 0.9); add(kit('rimshot'), 10.9, 0.5)
    add(kit('kick'), 12.3, 0.7); add(kit('boing'), 13.4, 0.5)
    add(tone(1500, 0.1, 0.2), 14.7); add(kit('pop'), 15.0, 0.5)
    add(kit('win'), 17.0, 0.8); add(kit('applause'), 17.2, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 53, 23.0, 22.5, OUT, cues)
