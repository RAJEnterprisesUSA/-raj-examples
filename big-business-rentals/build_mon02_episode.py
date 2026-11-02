"""Monday Nov 2 EP. 42 The Carry (reelsD REELS[42], 26s, Season Two; record 1 W · 1 L). Competence first: Dad moves 8
chairs in one trip; Lil copies Dad, Baby copies Lil but more, Dad's dolly saves the wobble, Princess rides the dolly,
Vaeh posts it anyway, the family holiday party (Sat Dec 19, in-story) is announced. Upgrade: in-story invitation card
reveal that sets the dated December arc."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP42 = BASE.parent/'fb_safe/BB_Chronicles_Ep42_TheCarry.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 106, 'groove'), 0.5, 0.36)
    for i in range(8): add(noise(0.05, 0.15, lp=0.07), 0.3+i*0.25)       # dolly rattle
    add(kit('pop2'), 2.4, 0.8); add(kit('pop'), 5.2, 0.8)                  # kids pop in
    add(kit('sneak'), 8.4, 0.6)                                           # third chair
    add(kit('freeze'), 9.6)                                               # NOPE.
    add(kit('whoosh'), 10.4); add(kit('kick'), 10.9)                       # chairs land on the dolly
    add(kit('win'), 11.0, 0.6)
    add(kit('pop2'), 11.4, 0.7)                                           # princess climbs aboard
    add(kit('rimshot'), 15.0, 0.7); add(kit('pop'), 16.6, 0.6)             # so embarrassing / posted it
    add(kit('whoosh'), 18.0, 0.6); add(kit('applause'), 18.4, 0.6)         # the invitation
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 42, 26.0, 25.2, EP42, cues)
