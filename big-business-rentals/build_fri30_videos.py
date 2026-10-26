"""Friday Oct 30 videos: TREND REMIX #12 Be OK (reelH REELS[35], 17.2s) and EP. 39 The Night Before
(reelsD REELS[39], 26s, loss: he screams at the intern, 4 W · 21 L). This build's upgrade: a real lighting
effect, a flashlight cone cut out of a dark room (nightD), and lights snapping on at the switch."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T35 = BASE/'halloween/BB_Trend_BeOK.mp4'
EP39 = BASE.parent/'fb_safe/BB_Chronicles_Ep39_TheNightBefore.mp4'

def cues_t35(add):
    add(bed(14.0, 124, 'groove'), 0.0, 0.7)                    # the cheerful dance never stops
    add(kit('pop'), 0.05)
    for at in (1.6, 4.2, 6.8, 9.4): add(kit('rimshot'), at, 0.6)   # each "not ok" line lands
    for i in range(8): add(kit('pop2'), 1.9+i*0.2, 0.35)          # the guest counter ticks
    add(kit('sneak'), 4.3, 0.5)                                # the cat
    add(kit('boing'), 6.9)                                     # cake chair
    add(noise(2.4, 0.25, lp=0.05), 9.4)                        # wind
    add(kit('win'), 12.0); add(kit('applause'), 12.6, 0.8)     # the truck + confetti

def cues_ep39(add):
    add(kit('sneak'), 0.2, 0.7); add(kit('sneak'), 2.3, 0.6)   # tiptoe flashlight check
    add(tone(1200, 0.06, 0.25), 2.5)                           # click
    for i in range(3): add(tone(70+i*6, 0.9, 0.35, 'sine', vib=5), 5.6+i*0.9)   # low creep as the sheet glides in
    add(kit('freeze'), 8.0)                                    # BOO freeze
    add(kit('whoosh'), 8.9); add(tone(900, 1.6, 0.4, 'saw', bend=0.8, vib=9), 9.0)   # the scream
    add(kit('boing'), 9.3)
    add(kit('whoosh'), 11.6, 0.6)                              # sheet pulled off
    add(tone(1318.5, 0.22, 0.36, 'sine', bend=0.4), 11.8)      # tyler pop
    add(kit('rimshot'), 13.6)                                  # ...im the new intern.
    add(tone(1500, 0.05, 0.4), 14.6); add(kit('pop2'), 14.62)  # light switch
    add(bed(5.0, 100, 'groove'), 14.8, 0.35)
    add(tone(659.3, 0.5, 0.5), 17.4); add(tone(523.3, 0.8, 0.5), 17.9)   # ding dong
    add(kit('sneak'), 17.9, 0.6)
    add(kit('freeze'), 19.4)                                   # INVITED.
    add(kit('sadtrom'), 20.3, 0.7)                             # facepalm
    add(kit('applause'), 20.7, 0.4)
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t35', 'both'): render_reel('halloween/reelH.html', 35, 17.2, 16.7, T35, cues_t35)
    if which in ('ep39', 'both'): render_reel('reelsD.html', 39, 26.0, 25.2, EP39, cues_ep39)
