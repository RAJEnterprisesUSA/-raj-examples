"""Saturday Nov 14 EP. 51 The Kids' Table (reelsD REELS[51], 26s, full ensemble; record 6 W · 5 L). Pairs with the Thanksgiving
headcount price list: Dad sets the big table and the kids' table. Mrs. Never Wrong counts every seat, Unc sits at the kids' table
on Lil Wobbles (NOPE.), Tyler is under the kids' table, Vaeh will not sit at the kids' table, Baby moves himself to the big table,
the cat takes the head seat. LOSS: everybody has a seat, Dad got the kids' table. Upgrade: two-table Thanksgiving set."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep51_TheKidsTable.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 96, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.7); add(kit('kick'), 0.7, 0.7)
    for i in range(4): add(tone(1000+i*120, 0.06, 0.15), 3.3+i*0.35)
    for i in range(3): add(tone(300, 0.05, 0.12), 5.7+i*0.25)
    add(kit('kick'), 6.4, 0.8); add(kit('freeze'), 6.6); add(kit('rimshot'), 7.3, 0.4)
    add(kit('boing'), 10.0, 0.5)
    add(kit('whoosh'), 13.0, 0.5); add(kit('pop'), 13.5, 0.5)
    add(kit('sneak'), 16.0, 0.5)
    add(kit('pop2'), 7.6, 0.9); add(kit('rimshot'), 8.8, 0.5)
    add(kit('boing'), 19.6, 0.7); add(kit('applause'), 19.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 51, 26.0, 25.2, OUT, cues)
