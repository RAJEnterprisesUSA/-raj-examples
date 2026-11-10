"""TREND REMIX #23 "The Gavel Changed Hands", READABLE CUT (reelH REELS[48] = T47 re-timed, 25.6s). Owner Nov 9 5:30pm:
"That's moving to fast for anyone to read the captions". Every caption now holds 1.8 to 3.0 s (shortest was ~0.8 s);
action runs to 22.4 s, end card to 25.6 s; end-card tagline shortened so it fits the frame ("NEW LEADERSHIP. SAME TABLES.").
UPGRADE: per-beat readable caption timing (piecewise time map) + end-card tagline fit check."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_TheGavelChangedHands_Readable.mp4'
MAP = [(0,0),(2.6,2.4),(5.2,4.4),(7.4,5.6),(9.4,6.6),(11.8,7.8),(13.6,8.6),(15.4,9.6),(17.2,10.6),(19.4,12.2),(22.4,14.0)]
def R(s):
    for (a0,s0),(a1,s1) in zip(MAP, MAP[1:]):
        if s <= s1: return a0 + (a1-a0)*(s-s0)/(s1-s0)
    return 22.4
def cues(add):
    for i in range(8): add(tone(1300+i*60, 0.04, 0.1), R(0.05+i*0.18))
    add(bed(21.8, 100, 'groove'), 0.3, 0.42)
    add(kit('whoosh'), R(2.6), 0.7); add(kit('kick'), R(3.6), 0.9)
    add(kit('whoosh'), R(4.4), 0.6); add(kit('boing'), R(5.6), 0.6)
    add(kit('pop'), R(6.6), 0.5); add(kit('rimshot'), R(7.8), 0.4)
    add(kit('pop2'), R(8.6), 0.9); add(kit('rimshot'), R(9.6), 0.5)
    for i in range(6): add(kit('kick'), R(10.7+i*0.25), 0.6)
    add(kit('sneak'), R(12.2), 0.5); add(kit('win'), R(12.3), 0.7); add(kit('applause'), R(12.5), 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 48, 25.6, 25.1, OUT, cues)
