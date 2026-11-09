"""Sunday Nov 15 EP. 52 The Calendar (reelsD REELS[52], 26s, full ensemble; record 7 W · 5 L). Pairs with the holiday flyer
(Dec 5, 12, 19): Dad circles the 19th in one stroke, Mrs. Never Wrong circles the 5th and 12th (all Saturdays), Unc stands on
Lil Wobbles to hang it higher (NOPE.), Tyler peeks out of the advent window on the 25th, the kids mark the 19th, Vaeh is
embarrassed, the cat guards the calendar. WIN: Dec 19 locked in. Upgrade: advent-window reveal."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep52_TheCalendar.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.2, 0.7); add(noise(0.4, 0.25, lp=0.3), 1.0)
    add(noise(0.3, 0.2, lp=0.3), 3.4); add(noise(0.3, 0.2, lp=0.3), 3.9)
    for i in range(4): add(tone(300, 0.05, 0.12), 5.6+i*0.2)
    add(kit('kick'), 6.4, 0.8); add(kit('freeze'), 6.6); add(kit('rimshot'), 7.3, 0.4)
    add(kit('pop'), 10.0, 0.5); add(kit('pop'), 10.6, 0.5); add(kit('pop2'), 11.2, 0.7)
    add(kit('sneak'), 15.0, 0.5)
    add(kit('pop2'), 7.6, 0.9); add(kit('rimshot'), 8.8, 0.5)
    add(kit('win'), 19.6, 0.7); add(kit('applause'), 19.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 52, 26.0, 25.2, OUT, cues)
