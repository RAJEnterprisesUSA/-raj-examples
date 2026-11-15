"""Sunday Nov 15 TREND REMIX #29 "The Turkey Floor Plan" (reelH REELS[56], 26.2s, ~3 s caption holds, speech clouds, cast by
story). Fresh nightly build Sat Nov 14, SOCIAL pool: turkey-shaped charcuterie/snack boards for Thanksgiving (NewEngen "TikTok
Trends: November 2026"). The snack board becomes a turkey-shaped floor plan: five 6 ft tables fanned as tail feathers (6 chairs
each) + a round body table (6 chairs) = seats 36. Cast: Mrs. Never Wrong, Dad ("CUTE. NOW WATCH THIS."), Princess ("IT NEEDS A
CROWN."), Lil Wobbles (wants to be the wattle; Mrs. Never Wrong: "ABSOLUTELY NOT."), the cat. No prices on screen.
UPGRADES: snack board morphs into a live overhead floor plan with a seat counter; ~3 s holds (owner pace rule)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_TurkeyFloorPlan.mp4'
def cues(add):
    add(bed(22.8, 100, 'groove'), 0.2, 0.40)
    add(kit('pop'), 3.0, 0.5)
    add(kit('whoosh'), 6.0, 0.6)
    for i in range(12): add(tone(1300+i*40, 0.03, 0.09), 6.1+i*0.2)      # chairs clicking in
    add(kit('pop2'), 10.0, 0.7)
    for i in range(3): add(tone(300, 0.05, 0.12), 12.2+i*0.3)
    add(kit('rimshot'), 13.9, 0.4); add(kit('whoosh'), 14.6, 0.5)
    add(kit('sneak'), 16.2, 0.5)
    add(kit('win'), 19.2, 0.7); add(kit('applause'), 19.4, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 56, 26.2, 25.7, OUT, cues)
