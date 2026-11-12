"""Thursday Nov 12 TREND REMIX #26 PARTY PHYSICS #3 "Once in 10 Billion" (reelH REELS[51], 24.2s). Fresh nightly build Wed Nov 11,
NEWS pool (last remix was the social pool): ScienceDaily, Nov 9 2026, physicists at the world's biggest particle lab found evidence
of a particle decay that happens about once in 10 billion decays. No lab, logo or names on screen. The family runs its own rare-event
experiment with a live ODDS meter; payoff: the rarest event, every guest has a chair. With us: every time.
UPGRADES: live odds meter on every beat + speech clouds for Vaeh/Dad/Tyler + space-to-room flash open (Party Physics series look)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_OnceInTenBillion.mp4'
def cues(add):
    add(noise(1.2, 0.35, lp=0.15), 0.0); add(kit('whoosh'), 0.1, 0.6)          # the collision
    add(kit('kick'), 2.6, 0.8); add(bed(20.8, 104, 'groove'), 2.6, 0.42)
    for b in [5.0, 7.4, 9.8, 12.2, 14.6, 17.0]: add(tone(1700, 0.08, 0.18), b + 0.6)   # odds meter blip
    add(kit('boing'), 6.8, 0.6)
    add(kit('rimshot'), 8.5, 0.4)
    add(kit('pop2'), 9.8, 0.9); add(kit('rimshot'), 10.9, 0.5)
    for i in range(3): add(tone(300, 0.05, 0.12), 12.4+i*0.25)
    add(kit('kick'), 13.2, 0.8)
    add(kit('pop'), 15.2, 0.5)
    for i in range(9): add(kit('pop'), 17.2+i*0.1, 0.45)
    add(kit('win'), 17.1, 0.7); add(kit('applause'), 17.4, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 51, 24.2, 23.7, OUT, cues)
