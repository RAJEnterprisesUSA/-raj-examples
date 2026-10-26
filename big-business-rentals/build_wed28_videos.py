"""Wednesday Oct 28 videos: TREND REMIX #10 Very Serious Opinions ("Two Fishes" deadpan format, reelH
REELS[33], 17.2s) and EP. 37 The Place Cards (reelsD REELS[37], 26s). This build's upgrade: designed
cover images for every video (covers/), passed to Buffer as the video thumbnail."""
import sys, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T33 = BASE/'halloween/BB_Trend_VerySeriousOpinions.mp4'
EP37 = BASE.parent/'fb_safe/BB_Chronicles_Ep37_ThePlaceCards.mp4'

def cues_t33(add):
    add(kit('theme'), 0.0)
    add(bed(13.4, 84, 'sneak'), 0.6, 0.35)                     # a dry, deadpan bed
    for at in (2.0, 4.9, 7.8, 11.0):                           # each opinion: a gavel-like knock
        add(kit('kick'), at, 0.9); add(noise(0.05, 0.3, lp=0.2), at)
    for at in (4.4, 7.3, 10.5):                                # the tiny nod
        add(kit('pop'), at, 0.4)
    add(kit('sneak'), 8.2, 0.7)                                # wobbles trembles in
    add(kit('sadtrom'), 9.9, 0.6)                              # and slides away
    add(kit('freeze'), 13.25)                                  # mic drop
    add(kit('applause'), 13.4, 0.7)

def cues_ep37(add):
    add(kit('theme'), 0.0)
    add(bed(22.0, 100, 'groove'), 0.6, 0.4)
    for i in range(6): add(kit('pop' if i % 2 else 'pop2'), 2.4+i*0.38, 0.8)   # cards land
    add(kit('sneak'), 5.6, 0.8)                                # wobbles rolls in
    add(kit('freeze'), 7.6)
    for i in range(6): add(noise(0.12, 0.3, lp=0.05), 8.6+i*0.4); add(kit('pop2'), 8.6+i*0.4, 0.5)  # swap war
    add(kit('rimshot'), 11.05)                                 # decree
    add(tone(1318.5, 0.22, 0.36, 'sine', bend=0.4), 13.0)      # tyler pop
    add(kit('pop'), 15.4)
    add(kit('pop'), 16.6)                                      # the cat lands
    add(kit('freeze'), 20.6)
    add(kit('sadtrom'), 20.9)
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t33', 'both'): render_reel('halloween/reelH.html', 33, 17.2, 16.7, T33, cues_t33)
    if which in ('ep37', 'both'): render_reel('reelsD.html', 37, 26.0, 25.2, EP37, cues_ep37)
