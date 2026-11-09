"""Friday Nov 13 EP. 50 The Floor Plan (reelsD REELS[50], 26s, full ensemble; record 6 W · 4 L). Pairs with the 3-layouts
carousel: Dad draws the Dec 19 floor plan and flips rows, rounds and a U-shape. Mrs. Never Wrong moves one table one inch (it
blocked the door), Unc reads it upside down, Tyler pops out from behind the board, Princess draws a throne and Baby a bigger one,
somebody drew Lil Wobbles in (ERASED.), Vaeh is embarrassed, the cat approves it from the top of the board. Upgrade: live plan board."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep50_TheFloorPlan.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 102, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.2, 0.7)
    for i in range(6): add(tone(1200+i*80, 0.04, 0.12), 0.3+i*0.12)
    add(kit('pop'), 1.3, 0.5); add(kit('pop'), 1.9, 0.5); add(kit('pop'), 2.5, 0.5)
    add(kit('pop2'), 3.6, 0.6); add(kit('rimshot'), 4.4, 0.4)
    add(kit('whoosh'), 5.6, 0.6); add(kit('boing'), 6.0, 0.5)
    add(kit('pop'), 10.0, 0.5); add(kit('pop2'), 11.0, 0.7)
    add(kit('sneak'), 12.5, 0.5); add(kit('freeze'), 14.0); add(noise(0.6, 0.3, lp=0.3), 14.7)
    add(kit('sneak'), 17.0, 0.5)
    add(kit('pop2'), 7.6, 0.9); add(kit('rimshot'), 8.8, 0.5)
    add(kit('win'), 19.6, 0.7); add(kit('applause'), 19.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 50, 26.0, 25.2, OUT, cues)
