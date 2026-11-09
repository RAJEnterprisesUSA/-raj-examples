"""Tuesday Nov 10 EP. 47 The Tent (reelsD REELS[47], 26s, full ensemble; record 4 W · 3 L). Competence first: Dad raises the
Dec 19 party tent in seconds. Unc holds a pole sideways, Mrs. Never Wrong adds weights (she was right), the gust blows Lil
Wobbles away ("BYE."), Tyler appears on top of the tent, the kids hang lights (Baby higher), Vaeh is embarrassed, the cat takes
the middle seat. Ties to Tuesday's Labor Crew flyer and the tents service. Upgrade: wind gust streaks + a tent that rises."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP47 = BASE.parent/'fb_safe/BB_Chronicles_Ep47_TheTent.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.7); add(kit('kick'), 0.9, 0.7); add(kit('win'), 1.0, 0.5)
    add(kit('boing'), 3.2, 0.6)
    add(kit('pop2'), 5.5, 0.7); add(kit('kick'), 6.2, 0.5); add(kit('kick'), 6.6, 0.5)
    for i in range(5): add(noise(0.5, 0.25, lp=0.12), 8.1+i*0.4)               # wind
    add(kit('freeze'), 9.4); add(kit('rimshot'), 10.1, 0.5)
    add(kit('pop2'), 10.7, 0.9); add(kit('rimshot'), 11.9, 0.5)
    for i in range(6): add(tone(1600+i*110, 0.05, 0.15), 13.6+i*0.3)          # lights on, one by one
    add(kit('pop'), 16.3, 0.6); add(kit('pop'), 16.6, 0.6); add(kit('sneak'), 17.4, 0.5)
    add(kit('win'), 19.6, 0.7); add(kit('applause'), 19.6, 0.7)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 47, 26.0, 25.2, EP47, cues)
