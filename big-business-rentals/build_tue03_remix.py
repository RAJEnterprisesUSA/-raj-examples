"""Tuesday Nov 3 TREND REMIX #16 (fresh nightly build, SOCIAL pool): "Reasons you don't need to rent tables and chairs for
Thanksgiving" (reelH REELS[39], 17.2s, Season Two look). Trend: reverse-psychology "reasons why you don't need to..." text
overlays (early Nov 2026 roundups: startups.co.uk). Upgrade: numbered glass reason cards that slide in + a recap list that
gets struck through at the payoff."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T39 = BASE/'halloween/BB_Trend_ReasonsYouDontNeed.mp4'
def cues(add):
    add(kit('pop'), 0.05)
    add(bed(14.0, 96, 'sneak'), 0.2, 0.5)                                   # deadpan bed
    for at in (1.9, 4.3, 6.7, 9.1): add(kit('whoosh'), at, 0.4); add(kit('pop2'), at+0.3, 0.6)   # reason cards slide in
    for i in range(10): add(tone(1600, 0.03, 0.2), 2.0+i*0.2)               # clock ticking
    add(kit('boing'), 5.6, 0.6)                                             # ironing board wobble
    add(kit('freeze'), 8.2, 0.7); add(kit('sadtrom'), 8.3, 0.6)             # Lil Wobbles collapses
    add(kit('sneak'), 9.2, 0.5)                                             # the cat
    for i in range(4): add(noise(0.12, 0.25, lp=0.3), 11.9+i*0.18)          # strike-throughs
    add(kit('win'), 12.4); add(kit('applause'), 12.9, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 39, 17.2, 16.7, T39, cues)
