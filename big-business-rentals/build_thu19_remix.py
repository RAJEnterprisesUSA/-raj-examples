"""Thursday Nov 19 TREND REMIX #30 "Push It 7 Inches" (reelH REELS[57], 24.2s, ~3 s caption holds, speech clouds, cast by story).
SOCIAL pool, checked Nov 18 (Google News, dated Nov 12-18 2026): crowds gather to "push" famous landmarks 7 inches to the left, a stunt
that began with a well known Chicago sculpture and spread to other cities and campuses. No landmark, city or person is named on screen:
a generic chrome dome on a stone base. The family pushes it (0 inches, Unc pushes from the other side), then one gentle push slides a
banquet table exactly 7 inches. Cast: Dad (STYLER2), Lil, Baby, Unc, the cat. No prices on screen.
UPGRADES: floor ruler + dashed ghost target for the 7 inches, live MOVED counter, a push chain (Baby pushes Lil, Lil pushes Dad)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_PushSevenInches.mp4'
def cues(add):
    add(bed(21.0, 100, 'groove'), 0.2, 0.40)
    add(kit('pop'), 3.0, 0.5)                                     # "3, 2, 1, PUSH!"
    for i in range(5): add(tone(180+i*6, 0.35, 0.10, 'saw'), 4.8+i*1.4)   # straining groans
    add(kit('sadtrom'), 6.2, 0.5)                                 # 0 inches
    add(kit('rimshot'), 9.4, 0.5)                                 # Unc, other side
    add(kit('whoosh'), 12.0, 0.6)
    add(kit('pop2'), 12.4, 0.6)
    for i in range(6): add(tone(500-i*20, 0.04, 0.10), 15.4+i*0.18)  # table sliding, 7 ticks
    add(kit('sneak'), 16.4, 0.4)
    add(kit('win'), 18.1, 0.7); add(kit('applause'), 18.3, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 57, 24.2, 23.7, OUT, cues)
