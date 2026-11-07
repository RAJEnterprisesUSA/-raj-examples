"""Saturday Nov 7 EP. 46 The Crew Is Back (reelsD REELS[46], 26s; FIRST full-ensemble Season Two episode per the owner's
Nov 5 rule; record 3 W · 3 L). Competence first: Dad sets the Dec 19 table in 2 seconds, but 101 guests needs the crew.
Mrs. Never Wrong straightens the crooked place cards, Unc (the kids' uncle now) carries a table the wrong way and hugs
Vaeh ("...this is SO embarrassing."), Tyler appears ("...im the new intern." "(STILL.)"), Lil Wobbles sneaks in and Baby
stands tuff, the cat takes Dad's seat. Upgrade: ten characters on screen with staged entrances and a place-card prop."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP46 = BASE.parent/'fb_safe/BB_Chronicles_Ep46_TheCrewIsBack.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 108, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.4, 0.6); add(kit('kick'), 0.75, 0.6)
    for i in range(4): add(kit('pop'), 1.0+i*0.15, 0.5)
    add(kit('sneak'), 2.8, 0.5)
    add(kit("pop2"), 5.6, 0.8)
    for i in range(4): add(tone(1300+i*100, 0.05, 0.18), 6.4+i*0.25)   # cards straightened
    add(kit('whoosh'), 8.3, 0.7); add(kit('boing'), 9.2, 0.6); add(kit('rimshot'), 10.0, 0.5)
    add(kit('pop2'), 11.2, 0.9); add(kit('rimshot'), 12.4, 0.5)
    add(kit('sneak'), 14.2, 0.6); add(kit('kick'), 16.4, 0.7)
    add(kit('sneak'), 17.2, 0.5); add(kit('freeze'), 18.4); add(kit('sadtrom'), 18.6, 0.5)
    add(kit('win'), 20.0, 0.7); add(kit('applause'), 20.0, 0.7)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 46, 26.0, 25.2, EP46, cues)
