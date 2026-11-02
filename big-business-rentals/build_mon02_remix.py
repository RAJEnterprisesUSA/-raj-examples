"""Monday Nov 2 TREND REMIX #15 (first FRESH NIGHTLY BUILD, news pool): "why matter survived the Big Bang" (reelH
REELS[38], 17.2s, Season Two look). News: Nov 1 2026 ScienceDaily, an overlooked particle may explain why a tiny bit of
matter was left over after the Big Bang. Remixed only: one leftover spark = the one extra chair on the truck.
Upgrade: the first non-Halloween remix room (roomS2: plum wall, gold string lights, Vegas skyline window) and a
space-to-party zoom transition."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T38 = BASE/'halloween/BB_Trend_BigBangExtraChair.mp4'

def cues(add):
    add(noise(1.2, 0.8, lp=0.04), 0.0); add(kit('freeze'), 0.0, 0.8); add(tone(55, 1.6, 0.6, 'sine', bend=-0.4), 0.0)   # the bang
    for i in range(12): add(kit('pop' if i % 2 else 'pop2'), 2.5+i*0.13, 0.35)       # annihilations
    add(tone(880, 1.2, 0.3, 'sine', vib=6), 3.9)                                     # the survivor glows
    add(kit('whoosh'), 5.0); add(tone(220, 2.2, 0.3, 'saw', bend=1.2), 5.0)           # zoom in
    add(bed(10.0, 108, 'groove'), 7.4, 0.5)
    add(kit('sadtrom'), 8.6, 0.6)                                                    # 13 guests, 12 chairs
    add(kit('sneak'), 11.0, 0.6)                                                     # unless...
    add(kit('kick'), 12.2); add(kit('win'), 12.3); add(kit('applause'), 12.4, 0.8)    # the extra chair lands

if __name__ == '__main__':
    render_reel('halloween/reelH.html', 38, 17.2, 16.7, T38, cues)
