"""Monday Nov 9 TREND REMIX #21 "It's time." (reelH REELS[44], 17.2s, full cast). Fresh nightly build Sun Nov 8, SOCIAL
pool: the "It's time" moment creators use to declare the holiday season open (NewEngen November 2026 roundup). Format only:
no celebrity likeness, no licensed audio (owner may add the trending sound in-app). Dad flips the switch, Unc brings the
tree, Mrs. Never Wrong says not until after Thanksgiving, Tyler appears wrapped in lights, the cat knocks the tree onto
Lil Wobbles; payoff: it's time to book December tables (Dec 5, 12, 19 = the real pre-Christmas Saturdays).
UPGRADES: lights-on reveal (dark first frame to color with a flash), a real December 2026 calendar prop with circled dates."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T44 = BASE/'halloween/BB_Trend_ItsTime.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.6)
    add(kit('kick'), 2.6, 0.9); add(kit('win'), 2.65, 0.7)                         # the switch: lights on
    add(bed(11.4, 112, 'groove'), 2.6, 0.45)
    for i in range(6): add(tone(1800+i*120, 0.05, 0.12), 2.7+i*0.08)              # sparkle
    add(kit('whoosh'), 3.0, 0.6); add(kit('pop2'), 5.0, 0.7)
    add(kit('pop2'), 7.6, 0.8); add(kit('rimshot'), 8.8, 0.5)
    add(kit('whoosh'), 10.0, 0.6); add(kit('kick'), 10.4, 0.8)
    add(kit('pop'), 12.0, 0.8); add(kit('applause'), 12.6, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 44, 17.2, 16.7, T44, cues)
