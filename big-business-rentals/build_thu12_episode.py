"""Thursday Nov 12 EP. 49 The Buffet Line (reelsD REELS[49], 26s, full ensemble; record 5 W · 4 L). Pairs with the caterer
referral: the caterer brings the food, Dad builds the buffet line. Mrs. Never Wrong labels every dish, Unc puts a chair in the
line, Tyler crawls out from under the tablecloth, Baby cuts Lil, Lil Wobbles folds under a tray ("NOPE."), Vaeh is embarrassed,
the cat is first in line (it eats cat food). LOSS: Dad built the line and is last in it. Upgrade: tablecloth skirt + chafers."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep49_TheBuffetLine.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 98, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.7); add(kit('kick'), 0.7, 0.7)
    for i in range(3): add(tone(900+i*150, 0.08, 0.2), 0.9+i*0.15)
    for i in range(3): add(kit('pop'), 3.4+i*0.3, 0.5)
    add(kit('kick'), 5.8, 0.6)
    add(kit('whoosh'), 10.0, 0.6); add(kit('boing'), 10.6, 0.5)
    for i in range(3): add(tone(300, 0.05, 0.12), 12.8+i*0.5)
    add(kit('kick'), 14.2, 0.8); add(kit('freeze'), 14.6); add(kit('rimshot'), 15.3, 0.4)
    add(kit('sneak'), 17.0, 0.5)
    add(kit('pop2'), 7.6, 0.9); add(kit('rimshot'), 8.8, 0.5)
    add(kit('boing'), 19.6, 0.7); add(kit('applause'), 19.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 49, 26.0, 25.2, OUT, cues)
