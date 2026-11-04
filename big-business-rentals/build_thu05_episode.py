"""Thursday Nov 5 EP. 45 The Headcount (reelsD REELS[45], 26s, Season Two; record 3 W · 2 L). Competence first: Dad does
the seating math in his head every time the Dec 19 guest list grows (6 seats a table). Lil invites his team, Baby invites
his team (he has no team), Princess invites her dolls, Vaeh posts it: 40 RSVPs. 100 guests, 17 tables, 102 seats; the
cat RSVPs (101) and there are still enough seats. End card: "What's your headcount this year?" (the one ask).
Upgrade: a live guest-list whiteboard whose numbers roll up in real time as the list grows."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
EP45 = BASE.parent/'fb_safe/BB_Chronicles_Ep45_TheHeadcount.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 110, 'groove'), 0.5, 0.36)
    for a in (1.2, 4.3, 7.3, 10.3, 19.0):
        add(kit('pop'), a, 0.6)
        for i in range(4): add(tone(1400+i*120, 0.04, 0.15), a+0.05+i*0.07)        # number roll
    add(kit('pop2'), 2.7, 0.8); add(kit('pop2'), 5.7, 0.8); add(kit('pop2'), 8.7, 0.8)
    for i in range(6): add(kit('pop'), 9.0+i*0.15, 0.4)                               # dolls
    add(kit('whoosh'), 11.7, 0.5); add(kit('pop'), 12.8, 0.9)                          # Vaeh, RSVP ping
    for i in range(8): add(tone(1400+i*90, 0.04, 0.15), 12.9+i*0.05)
    add(kit('freeze'), 13.25); add(kit('rimshot'), 14.0, 0.6)
    for i in range(6): add(kit('pop'), 14.8+i*0.24, 0.45)                              # seats roll out
    add(kit('sneak'), 18.1, 0.5)
    add(kit('win'), 20.0, 0.7); add(kit('applause'), 20.0, 0.6)
    add(kit('theme'), 22.5, 0.6)
if __name__ == '__main__':
    render_reel('reelsD.html', 45, 26.0, 25.2, EP45, cues)
