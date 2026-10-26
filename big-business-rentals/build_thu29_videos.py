"""Thursday Oct 29 videos: TREND REMIX #11 Pumpkin Head Illusion (reelH REELS[34], 17.2s) and EP. 38
The Delivery (reelsD REELS[38], 26s, WIN No. 4). This build's upgrades: confetti bursts and the
cinematic finish (contrast/color lift, vignette, film grain) in audio/render30.py."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T34 = BASE/'halloween/BB_Trend_PumpkinHeadIllusion.mp4'
EP38 = BASE.parent/'fb_safe/BB_Chronicles_Ep38_TheDelivery.mp4'

def cues_t34(add):
    add(kit('theme'), 0.0)
    add(bed(7.4, 112, 'groove'), 0.5, 0.55)                    # the dance
    add(kit('rimshot'), 6.2)                                   # he steps out, the pumpkin stays
    add(kit('whoosh'), 8.0); add(tone(180, 1.4, 0.3, 'saw', bend=1.0), 8.0)   # the pull-back reveal
    add(kit('win'), 9.4, 0.7)
    add(kit('sneak'), 10.6, 0.8)                               # the cat
    add(kit('boing'), 11.7); add(kit('freeze'), 12.3, 0.8)     # pumpkin falls
    add(kit('win'), 12.9); add(kit('applause'), 13.0, 0.8)     # payoff + confetti

def cues_ep38(add):
    add(kit('theme'), 0.0)
    add(bed(22.0, 100, 'groove'), 0.6, 0.38)
    for i in range(6): add(noise(0.05, 0.15, lp=0.07), 2.4+i*0.25)   # dolly rattle
    add(tone(1318.5, 0.22, 0.36, 'sine', bend=0.4), 2.5)       # tyler pop
    for i in range(4): add(kit('pop' if i % 2 else 'pop2'), 5.8+i*0.5)   # chairs land
    for i in range(5): add(kit('pop2'), 9.0+i*0.5, 0.6)        # counting
    add(kit('sneak'), 11.0, 0.8)                               # the fifth chair
    add(kit('whoosh'), 13.0); add(kit('freeze'), 13.6)          # sheet off: SNEAKY
    add(kit('rimshot'), 14.6)                                  # OUT
    for i in range(8): add(noise(0.05, 0.15, lp=0.07), 15.9+i*0.25)  # wheeled out
    add(kit('win'), 18.2); add(kit('applause'), 18.3)          # WIN No. 4 + confetti
    add(kit('freeze'), 19.0, 0.6)
    add(kit('sneak'), 20.6, 0.6)                               # the empty sheet floats off
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t34', 'both'): render_reel('halloween/reelH.html', 34, 17.2, 16.7, T34, cues_t34)
    if which in ('ep38', 'both'): render_reel('reelsD.html', 38, 26.0, 25.2, EP38, cues_ep38)
