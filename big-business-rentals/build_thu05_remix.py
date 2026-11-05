"""Thursday Nov 5 TREND REMIX #18 PARTY PHYSICS #2 (fresh nightly build, NEWS pool): "a third kind of magnetism"
(reelH REELS[41], 17.2s, Season Two look + the whole family). News: researchers confirmed altermagnetism, a third kind of
magnetism after nearly 90 years of two (ScienceDaily / SLAC listing, early Nov 2026). The back-burnered nuclear clock story
turned out to date from Oct 8, so it failed the current-only rule and was dropped. Series format copied from the best
remix so far (Big Bang extra chair): real science headline as the hook, big visual, payoff on chairs in the last seconds.
UPGRADES: Party Physics series title chip, animated magnetic field lines with flowing charge dots, Season Two kid rigs
ported into reelH (first remix with the whole family)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T41 = BASE/'halloween/BB_Trend_PartyPhysics2_Magnetism.mp4'
def cues(add):
    add(kit('pop'), 0.05)
    for i in range(10): add(tone(220+i*20, 0.25, 0.10), 0.1+i*0.25)               # lab hum
    add(bed(14.0, 100, 'groove'), 2.5, 0.42)
    add(kit('whoosh'), 2.6, 0.6); add(kit('sneak'), 3.0, 0.5)                    # type 1
    add(kit('whoosh'), 5.2, 0.6); add(kit('pop2'), 5.5, 0.6)                     # type 2
    add(kit('whoosh'), 7.8, 0.7)                                                 # type 3
    for i in range(6): add(noise(0.08, 0.2, lp=0.2), 8.2+i*0.2)                  # everybody slides in
    add(kit('freeze'), 9.6); add(kit('rimshot'), 10.3, 0.5)
    for i in range(4): add(kit('pop'), 11.0+i*0.18, 0.6)                         # chairs pop in
    add(kit('win'), 11.5); add(kit('applause'), 11.6, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 41, 17.2, 16.7, T41, cues)
