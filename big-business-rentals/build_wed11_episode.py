"""Wednesday Nov 11 EP. 48 The Cocoa Bar (reelsD REELS[48], 26s, full ensemble; record 5 W · 3 L). Pairs with Wednesday's
Guess the Theme No. 4 (Hot Cocoa Party). Competence first: Dad sets the Dec 19 cocoa bar in seconds. Mrs. Never Wrong gives it a
10, Unc fills the marshmallow jar with mini chairs, Tyler pops up from behind the bar ("...im the new intern."), Lil gets a
whipped cream beard and Baby a bigger one, the pot sits on Lil Wobbles until he folds and Dad catches it ("SAVED."), Princess
crowns the mug, the cat sleeps in the empty marshmallow box. Upgrade: a mid-air catch with a freeze-zoom on the save."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP48 = BASE.parent/'fb_safe/BB_Chronicles_Ep48_TheCocoaBar.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 100, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.7); add(kit('kick'), 0.7, 0.7)
    for i in range(3): add(tone(1400+i*200, 0.06, 0.18), 1.2+i*0.15)         # mugs clink down
    add(kit('pop2'), 3.6, 0.8)
    add(kit('boing'), 5.4, 0.6)
    add(kit('pop2'), 7.6, 0.9); add(kit('rimshot'), 8.8, 0.5)
    add(noise(0.35, 0.3, lp=0.2), 10.0); add(noise(0.5, 0.35, lp=0.2), 11.0)    # whipped cream sprays
    for i in range(4): add(tone(300, 0.05, 0.12), 12.6+i*0.6)                 # Wobbles creaks
    add(kit('kick'), 15.0, 0.8); add(kit('whoosh'), 15.4, 0.6)
    add(kit('freeze'), 16.0); add(kit('win'), 16.1, 0.5)
    add(tone(2200, 0.15, 0.2), 17.2); add(kit('sneak'), 18.0, 0.5)
    add(kit('win'), 19.6, 0.7); add(kit('applause'), 19.6, 0.7)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 48, 26.0, 25.2, EP48, cues)
