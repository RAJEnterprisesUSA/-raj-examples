"""Tuesday Oct 27 videos: TREND REMIX #9 Cat Handshake (reelH REELS[32], 17.2s) and EP. 36 The Wind
Check (reelsD REELS[36], 26s). Upgrades shipped: word-pop captions, 30 fps, instrument sound kit."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, remaster, kit, bed, tone, noise, BASE

def drums(add, start, end, bpm=110, gain=0.5):
    beat = 60/bpm; t = start; i = 0
    while t < end:
        add(kit('kick'), t, gain)
        if i % 2 == 1: add(noise(0.05, 0.12, lp=0.3), t)       # light snare tick
        t += beat; i += 1

def cues_t32(add):
    add(kit('theme'), 0.0)
    add(bed(13.6, 104, 'groove'), 0.6, 0.55)
    for d in (2.2, 6.4, 11.4):                                # clap clap clap, then the handshake
        for c in range(3): add(noise(0.06, 0.45, lp=0.6), d+0.2+c*0.4); add(kit('pop2'), d+0.2+c*0.4, 0.35)
        add(kit('win'), d+1.25, 0.7)
    add(kit('sneak'), 9.0, 0.8)                               # Wobbles slides in
    add(kit('rimshot'), 10.5)                                 # the swat
    add(kit('sadtrom'), 10.7, 0.5)
    add(kit('applause'), 12.8, 0.8)

def cues_ep36(add):
    add(kit('theme'), 0.0)
    add(bed(22.0, 96, 'sneak'), 0.6, 0.45)
    for a, b in ((2.4, 3.6), (8.3, 9.2), (10.5, 11.6), (18.4, 19.3), (19.9, 20.9)):   # gusts
        add(noise(b-a, 0.45, lp=0.02), a)
    add(kit('whoosh'), 3.0)                                   # linen flies off
    add(kit('pop'), 7.0); add(kit('pop2'), 7.4); add(kit('pop2'), 7.55)   # linen on, clips snap
    add(kit('win'), 8.6, 0.6)                                 # it holds
    add(kit('sneak'), 9.6, 0.8)                               # wobbles rolls in
    add(kit('boing'), 10.7)                                   # blown away
    add(kit('freeze'), 11.0)
    add(kit('win'), 12.0)                                     # one problem solved
    add(tone(1318.5, 0.22, 0.36, 'sine', bend=0.4), 13.2)     # tyler pop
    add(kit('pop'), 17.1)                                     # the cat lands
    add(kit('boing'), 20.0, 0.8)                              # wobbles blown BACK
    add(kit('freeze'), 20.8)
    add(kit('sadtrom'), 21.0)
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'remaster':
        import shutil
        for src, dur, fade, cues in ((BASE/'halloween/BB_Trend_CatHandshake.mp4', 17.2, 16.7, cues_t32),
                                     (BASE.parent/'fb_safe/BB_Chronicles_Ep36_TheWindCheck.mp4', 26.0, 25.2, cues_ep36)):
            tmp = src.with_suffix('.tmp.mp4'); remaster(src, dur, fade, cues, tmp); shutil.move(tmp, src)
        sys.exit(0)
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t32', 'both'):
        render_reel('halloween/reelH.html', 32, 17.2, 16.7, BASE/'halloween/BB_Trend_CatHandshake.mp4', cues_t32)
    if which in ('ep36', 'both'):
        render_reel('reelsD.html', 36, 26.0, 25.2, BASE.parent/'fb_safe/BB_Chronicles_Ep36_TheWindCheck.mp4', cues_ep36)
