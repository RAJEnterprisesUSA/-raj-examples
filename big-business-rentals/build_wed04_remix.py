"""Wednesday Nov 4 TREND REMIX #17 (fresh nightly build): "The red party and the blue party" (reelH REELS[40], 17.2s,
Season Two look). OWNER-PICKED topic (Nov 3, Election Day: "remix one about the elections the red party and the blue
party"), a one-time owner override of the no-politics guardrail, built strictly nonpartisan: red and blue are party
THEMES, no candidates, real party names, logos, results or voting info; both sides identical. The clock remix
(nuclear clock news) moved to Thursday. Upgrade: live seat counters that tick up as each table lands + a split-screen
color grade that merges into one room."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T40 = BASE/'halloween/BB_Trend_RedPartyBlueParty.mp4'
def cues(add):
    add(kit('pop'), 0.05)
    add(bed(14.0, 104, 'groove'), 0.2, 0.45)
    add(kit('whoosh'), 2.4, 0.5)
    for i in range(6): add(kit('pop'), 2.7+i*0.42, 0.55); add(tone(1200+i*80, 0.05, 0.18), 2.75+i*0.42)   # red tables + counter ticks
    add(kit('whoosh'), 5.4, 0.5)
    for i in range(6): add(kit('pop'), 5.7+i*0.42, 0.55); add(tone(1200+i*80, 0.05, 0.18), 5.75+i*0.42)   # blue tables, same
    add(kit('sneak'), 8.4, 0.5); add(kit('freeze'), 9.4, 0.7)                                               # the seat count. TIE.
    add(kit('whoosh'), 10.8); add(kit('win'), 11.2); add(kit('applause'), 11.4, 0.8)                         # one long table
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 40, 17.2, 16.7, T40, cues)
