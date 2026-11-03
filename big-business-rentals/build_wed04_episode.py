"""Wednesday Nov 4 EP. 44 The Teardown (reelsD REELS[44], 26s, Season Two; record 2 W · 2 L). Competence first: Dad folds
a table in 2 seconds and steadies Baby's wobbling six-chair tower with one hand. Lil stacks four perfectly, Baby stacks
six, Princess finds the one they missed (the cat is in it), Dad loses three rounds to the cat, Vaeh lifts the cat
without looking up, teardown done: Dec 19 is ready. Ties into the setup and teardown crew service (owner Nov 2).
Upgrade: a physics stack that wobbles from the base up (each chair sways more the higher it sits) and settles."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP44 = BASE.parent/'fb_safe/BB_Chronicles_Ep44_TheTeardown.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 112, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.6); add(kit('kick'), 1.1, 0.8); add(kit('win'), 1.3, 0.5)     # table folds
    add(kit('pop2'), 2.5, 0.8)
    for i in range(4): add(kit('pop'), 3.1+i*0.45, 0.6)                                      # Lil's four
    add(kit('pop'), 5.1, 0.8)
    for i in range(2): add(kit('pop'), 5.7+i*0.5, 0.7)                                       # Baby's two
    add(kit('sneak'), 6.5, 0.6); add(kit('freeze'), 7.6)                                     # wobble, TIMBER?
    add(kit('kick'), 8.5, 0.7); add(kit('win'), 8.6, 0.5)                                    # one hand
    add(kit('pop2'), 9.6, 0.7)                                                               # princess
    for a in (13.25, 14.35, 15.45): add(kit('rimshot'), a, 0.5)                              # HSSS x3
    add(kit('whoosh'), 16.0, 0.6); add(kit('pop'), 16.6, 0.7)                                # Vaeh lifts the cat
    add(kit('kick'), 19.0, 0.7); add(kit('applause'), 19.5, 0.6)                             # last chair, done
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 44, 26.0, 25.2, EP44, cues)
