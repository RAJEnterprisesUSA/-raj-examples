"""TREND REMIX #22 "The New Majority" (reelH REELS[46], 17.2s, full cast minus Lil Wobbles). CONTROVERSY lane, owner Nov 9
5:20pm: "I want one based of controversy". Topic: control of Congress changed hands in the Nov 3 2026 midterms. Strictly
nonpartisan (no parties, colors, names, results or opinions): the kids win the table vote, pass "kids get the big table",
Dad lands on the tiny chair, Mrs. Never Wrong objects, Tyler ties it, the cat breaks the tie. Payoff: whoever has the
majority, everybody gets a seat. Lil Wobbles (red) left out so red never reads as a side.
UPGRADE: live on-screen vote tally board that updates with each beat."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_TheNewMajority.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.5)
    add(bed(13.6, 108, 'groove'), 0.3, 0.42)
    add(kit('pop2'), 2.4, 0.8); add(kit('applause'), 2.5, 0.4)
    add(kit('rimshot'), 3.9, 0.4)
    add(kit('whoosh'), 4.6, 0.6); add(kit('boing'), 5.0, 0.6)
    add(kit('kick'), 6.8, 0.7)
    add(kit('pop2'), 8.8, 0.9); add(kit('rimshot'), 9.8, 0.5)
    add(kit('freeze'), 10.8); add(kit('sneak'), 11.0, 0.5)
    for i in range(4): add(kit('pop'), 12.5+i*0.12, 0.5)
    add(kit('win'), 12.45, 0.7); add(kit('applause'), 12.7, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 46, 17.2, 16.7, OUT, cues)
