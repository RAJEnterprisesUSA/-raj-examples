"""Friday Nov 6 TREND REMIX #19 "Race week vs. locals" (reelH REELS[42], 17.2s, full Season Two cast). OWNER-PICKED
(Nov 5: "community one") from a 3-lane menu (politics / finance / community). News: the big race returns Nov 19 to 21,
lane closures on the Strip now, full road closures and bus detours on race nights, locals frustrated again (FOX5, KTNV,
LVSportsBiz). No race name, logos or branding. Two teams, both shown; payoff "Skip the Strip. Party at home."
UPGRADES: full ensemble back in a remix (Season One crew + Season Two family together), road-closure props
(barricade with sign, cones, traffic wands), adults scaled so ten characters fit one frame."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
T42 = BASE/'halloween/BB_Trend_RaceWeekVsLocals.mp4'
def cues(add):
    add(kit('pop'), 0.05)
    add(bed(14.0, 112, 'groove'), 0.2, 0.42)
    for i in range(3): add(noise(0.4, 0.18, lp=0.15), 0.3+i*0.6)                 # race engines far off
    add(kit('whoosh'), 2.6, 0.5); add(kit('kick'), 3.9, 0.6)                    # van brakes at the closure
    add(kit('sneak'), 5.4, 0.6); add(kit('whoosh'), 6.0, 0.7); add(kit('boing'), 7.4, 0.6)   # the shortcut loop
    add(kit('pop2'), 7.8, 0.8); add(kit('rimshot'), 9.0, 0.5)                    # Tyler
    add(kit('kick'), 9.4, 0.7); add(kit('whoosh'), 9.8, 0.6)                    # Wobbles folds, van through
    add(kit('win'), 10.5); add(kit('applause'), 10.6, 0.8)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 42, 17.2, 16.7, T42, cues)
