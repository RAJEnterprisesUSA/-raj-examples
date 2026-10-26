"""Saturday Oct 31 videos: TREND REMIX #13 The Merger (reelH REELS[36], 17.2s), the first NEWS remix (owner Oct 26:
news trends too, no advice, only remixed for the business), and EP. 40 The Halloween Party (reelsD REELS[40], 26s),
the Season One finale: full cast, WIN No. 5, final record 5 W · 21 L. This build's upgrade: a wide-shot camera for
the full cast and a group-photo freeze frame with a printed photo border."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T36 = BASE/'halloween/BB_Trend_TheMerger.mp4'
EP40 = BASE.parent/'fb_safe/BB_Chronicles_Ep40_TheHalloweenParty.mp4'

def cues_t36(add):
    add(kit('theme'), 0.0)
    add(bed(14.0, 104, 'groove'), 0.4, 0.5)
    for i in range(4): add(kit('pop' if i % 2 else 'pop2'), 2.1+i*0.25)     # chairs pop in
    add(noise(0.4, 0.2, lp=0.1), 4.8); add(noise(0.4, 0.2, lp=0.1), 5.4)    # pen scribbles
    add(kit('whoosh'), 5.2); add(tone(220, 1.4, 0.3, 'saw', bend=0.6), 5.2)  # tables slide together
    add(kit('freeze'), 6.6)                                    # MERGED
    add(kit('whoosh'), 7.2, 0.6)                               # long cloth
    add(kit('sneak'), 9.6, 0.8)                                # hostile takeover
    add(kit('rimshot'), 10.6)                                  # DENIED
    add(kit('boing'), 11.9)                                    # cat hops up
    add(kit('win'), 12.2); add(kit('applause'), 12.3, 0.8)

def cues_ep40(add):
    add(kit('theme'), 0.0)
    add(bed(22.0, 108, 'groove'), 0.5, 0.36)
    add(tone(659.3, 0.5, 0.45), 2.3); add(tone(523.3, 0.8, 0.45), 2.75)     # doorbell
    add(kit('pop2'), 3.4, 0.7)
    add(tone(1318.5, 0.22, 0.36, 'sine', bend=0.4), 4.4)      # tyler pop
    add(kit('rimshot'), 5.2)                                   # ...im the new intern.
    add(kit('whoosh'), 6.0, 0.6)                               # cut to the table
    for i in range(4): add(kit('pop'), 6.2+i*0.25, 0.6)        # four chairs, four guests
    add(kit('sadtrom'), 7.6, 0.7)                              # where does the host sit
    add(kit('freeze'), 8.8)                                    # NO SEAT
    add(kit('sneak'), 9.6, 0.7)                                # lil wobbles slides in
    add(kit('rimshot'), 10.8, 0.7)                             # no thank you
    add(kit('whoosh'), 12.4); add(kit('kick'), 12.75); add(kit('boing'), 12.8, 0.6)   # extra chair lands
    add(kit('win'), 15.4); add(kit('applause'), 15.5)          # WIN No. 5
    add(kit('pop2'), 16.6, 0.7); add(kit('boing'), 17.0, 0.5)   # the cat hops onto wobbles
    add(noise(0.12, 0.5, lp=0.3), 19.0); add(kit('freeze'), 19.0, 0.6)   # camera flash
    add(kit('theme'), 21.0, 0.8); add(kit('applause'), 21.2, 0.5)
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t36', 'both'): render_reel('halloween/reelH.html', 36, 17.2, 16.7, T36, cues_t36)
    if which in ('ep40', 'both'): render_reel('reelsD.html', 40, 26.0, 25.2, EP40, cues_ep40)
