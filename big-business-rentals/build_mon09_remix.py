"""Monday Nov 9 TREND REMIX #21 "One table, five parties" (reelH REELS[45], 17.2s, full cast). Fresh nightly build Sun Nov 8,
SOCIAL pool: fashion's "one hero piece, many outfits fast" format (tryvolume.app tracker measured Nov 8 2026, ~7x usual views).
Replaces the pulled "It's time" tree remix (owner Nov 8: "i dont want a video of a christmas celebration"). The hero piece is one
6 ft table styled five ways fast: birthday, Friendsgiving, game day, baby shower, office party. Tyler pops up from under the office
party table, Lil Wobbles wants a look too (NOPE.), the cat takes the table. Payoff: one table, every party, we deliver it.
UPGRADES: spin-change transitions with a flash on every look + a LOOK n/5 counter (the fashion format's own grammar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T45 = BASE/'halloween/BB_Trend_OneTableFiveParties.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.5)
    add(bed(13.6, 118, 'groove'), 0.3, 0.42)
    for i in range(5): add(kit('whoosh'), 2.3+i*1.8, 0.6); add(kit('pop'), 2.45+i*1.8, 0.55)   # each look change
    add(kit('applause'), 3.0, 0.3)
    add(kit('pop2'), 9.8, 0.8); add(kit('rimshot'), 10.8, 0.5)
    for i in range(3): add(tone(300, 0.05, 0.12), 11.9+i*0.15)
    add(kit('kick'), 12.4, 0.8); add(kit('win'), 12.95, 0.7); add(kit('applause'), 13.2, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 45, 17.2, 16.7, T45, cues)
