"""Tuesday Nov 3 EP. 43 The Tablecloth (reelsD REELS[43], 26s, Season Two; record 2 W · 1 L). Competence first: Dad sets
a table in 3 seconds and nails the tablecloth trick (freeze, NAILED.). Lil tries it and the plates fly; Vaeh catches
every one without looking up. Baby does it clean, then spins three times on purpose (TUFF.). Princess wears the cloth
as a cape, the cat takes the last plate, Dad resets it all: practice round for the Dec 19 family party.
Upgrade: first multi-object physics gag in the series (staggered plate arcs that stack into a catch)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP43 = BASE.parent/'fb_safe/BB_Chronicles_Ep43_TheTablecloth.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 108, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.5)                                          # cloth on
    for i in range(4): add(kit('pop'), 0.6+i*0.3, 0.55)                   # four plates set
    add(kit('pop2'), 2.6, 0.8); add(kit('pop'), 3.8, 0.7)                  # Lil, Baby
    add(kit('sneak'), 5.0, 0.6)                                           # watch this
    add(kit('whoosh'), 6.2); add(kit('freeze'), 6.6); add(kit('win'), 7.4, 0.6)
    add(kit('sneak'), 8.4, 0.5)                                           # Lil tries it
    add(kit('whoosh'), 9.4); add(kit('kick'), 9.4, 0.8)
    for i in range(4): add(kit('pop'), 9.9+i*0.18, 0.6)                   # plates land in Vaeh's hand
    add(kit('rimshot'), 10.4, 0.7)
    add(kit('pop2'), 11.9, 0.7); add(kit('whoosh'), 12.6)
    for i in range(3): add(kit('whoosh'), 12.7+i*0.4, 0.35)               # three spins
    add(kit('kick'), 13.85); add(kit('applause'), 13.9, 0.5)
    add(kit('pop2'), 15.1, 0.7)                                           # princess cape
    add(kit('sneak'), 17.9, 0.5); add(kit('pop'), 18.9, 0.6)               # cat hops on the plate
    add(kit('whoosh'), 19.9, 0.6); add(kit('applause'), 20.1, 0.6)         # reset + confetti
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 43, 26.0, 25.2, EP43, cues)
