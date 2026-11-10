"""TREND REMIX #23 "The Gavel Changed Hands" (reelH REELS[47], 17.2s). CONTROVERSY lane, owner Nov 9 evening picked ideas 1 + 2
combined ("Can you combine 1 and 2?"): the Congress flip told only through tells. 435 chairs in a chamber half-circle with a
center aisle and a gavel on the head table; "the head of the table is under new leadership"; everybody switches sides of the
aisle (Unc goes the wrong way); Mrs. Never Wrong reads the new seating chart; Vaeh is embarrassed; Tyler pops up; Baby finds the
gavel; the cat takes the big chair. Payoff: the seats didn't change, who sits in them did. Strictly nonpartisan: no parties,
red/blue, names, results or opinions; Lil Wobbles (red) left out. UPGRADE: a 435-chair chamber set with a live seat counter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_TheGavelChangedHands.mp4'
def cues(add):
    for i in range(8): add(tone(1300+i*60, 0.04, 0.1), 0.05+i*0.18)          # chairs clicking into place
    add(bed(13.6, 100, 'groove'), 0.3, 0.42)
    add(kit('whoosh'), 2.6, 0.7); add(kit('kick'), 3.6, 0.9)                     # gavel crosses, lands
    add(kit('whoosh'), 4.4, 0.6); add(kit('boing'), 5.6, 0.6)
    add(kit('pop'), 6.6, 0.5); add(kit('rimshot'), 7.8, 0.4)
    add(kit('pop2'), 8.6, 0.9); add(kit('rimshot'), 9.6, 0.5)
    for i in range(6): add(kit('kick'), 10.7+i*0.25, 0.6)                       # BANG BANG
    add(kit('sneak'), 12.2, 0.5); add(kit('win'), 12.3, 0.7); add(kit('applause'), 12.5, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 47, 17.2, 16.7, OUT, cues)
