"""Saturday Nov 21 TREND REMIX #32 "The Day-Off Pitch" (reelH REELS[59], 25.2s, ~3 s caption holds, speech clouds, cast by story).
GTA6 VIBE WEEK day 1 of 8 (THEME_GTA6_REMIX_WEEK.md): sunset + neon look, "NEW MISSION" card, loading bar chip, HUD mini-map, "MISSION COMPLETE".
SOCIAL pool, checked Nov 21 (Google News, dated Nov 15 to Nov 19 2026): workers are pitching their bosses for the day off to play the big new game
and bosses are saying yes in viral posts. No game name, logo, brand, company or person on screen or in captions. Drawn with the canvas rig, original lettering.
Cast: Dad (STYLER2), Unc, Lil Big Business, Mrs. Never Wrong, the cat (Soup Swap was Dad/MNW/Vaeh/Princess/cat, Push It was Dad/Lil/Baby/Unc/cat).
UPGRADES: first full sunset/neon world set (striped sun, skyline, palms, perspective plaza), objective chip that doubles as a loading bar,
mini-map HUD that fills with tables, mission cards, chair flip gag (Unc carries it wrong way, Mrs. Never Wrong fixes it without a word)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_DayOffPitch.mp4'
def cues(add):
    add(bed(23.0, 104, 'groove'), 0.2, 0.40)
    add(kit('pop'), 3.0, 0.5)                                                  # Unc pitches the boss
    add(kit('pop2'), 6.0, 0.5)                                                 # Dad: deal, setup first
    add(kit('whoosh'), 8.9, 0.5)                                               # mission card slides in
    add(tone(660, 0.10, 0.22), 9.35); add(tone(880, 0.14, 0.24), 9.5)          # mission ping
    add(kit('whoosh'), 11.8, 0.4)                                              # card slides out
    for i in range(10): add(tone(420+i*38, 0.05, 0.12), 12.3+i*0.3)            # loading bar ticks, rising
    for t0 in (12.5, 13.0, 13.6): add(kit('pop'), t0, 0.35)                    # tables pop in
    for t0 in (12.9, 13.9, 14.2, 14.6, 14.8, 15.1): add(tone(300, 0.06, 0.2), t0)   # chairs pop in
    add(kit('rimshot'), 13.7, 0.45)                                            # the chair gets flipped right side up
    add(kit('win'), 15.4, 0.7); add(kit('applause'), 15.6, 0.6)                # mission complete
    add(kit('sneak'), 16.3, 0.4)                                               # the cat is already playing
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 59, 25.2, 24.7, OUT, cues)
