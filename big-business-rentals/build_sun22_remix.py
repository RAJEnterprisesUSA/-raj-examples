"""Sunday Nov 22 TREND REMIX #33 "No Assigned Seats" (reelH REELS[60], 25.6s, ~3 s caption holds, speech clouds, cast by story).
GTA6 VIBE WEEK day 2 of 8 (THEME_GTA6_REMIX_WEEK.md): sunset + neon world (skyT59 from day 1), LOADING TIP card with a filling bar, lobby-style
player pills (PICKING to LOCKED IN). No game name, logo or wordmark anywhere, original lettering, no weapons, crime or cars.
SOCIAL/lifestyle pool, checked Nov 22 2026 (Good Housekeeping, published Nov 19 2026: Gen Z hosts are dropping assigned seating and matching place settings;
etiquette-debate roundup Nov 22). No outlet, brand or person on screen or in captions.
Cast: Dad (STYLER2), Lil, Baby, Unc, Vaeh, the cat (Day-Off Pitch was Dad/Unc/Lil/Mrs. Never Wrong/cat; Mrs. Never Wrong, Princess, Tyler rotate out).
UPGRADES: first seated rigs in a remix (kid-scaled hips solved onto a shared chair scale, dangling legs), chair tip-back with pivot on the rear legs,
Vaeh with headphones and a lit phone fixing it with her back arm, place cards swept off the table."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_NoAssignedSeats.mp4'
def cues(add):
    add(bed(24.0, 104, 'groove'), 0.2, 0.40)
    add(kit('pop2'), 3.2, 0.5)                                                 # Dad: no seat cards
    add(kit('whoosh'), 3.45, 0.4)                                              # cards swept off
    for t0 in (4.0, 4.2, 4.4, 4.6, 4.8): add(kit('pop'), t0, 0.35)             # chairs pop in
    add(kit('whoosh'), 6.2, 0.5)                                               # tip card slides in
    add(tone(660, 0.10, 0.22), 6.6); add(tone(880, 0.14, 0.24), 6.75)          # tip ping
    for i in range(9): add(tone(420+i*38, 0.05, 0.12), 6.9+i*0.25)             # loading bar ticks, rising
    add(kit('whoosh'), 8.9, 0.4)                                               # card slides out
    for t0 in (11.45, 11.85, 13.85, 14.15):                                    # LOCKED IN pings
        add(tone(784, 0.08, 0.22), t0); add(tone(1047, 0.12, 0.22), t0+0.09)
    for t0 in (11.27, 11.67, 13.67, 13.97): add(tone(180, 0.07, 0.25), t0)     # sit thumps
    add(kit('pop'), 13.9, 0.4)                                                 # Vaeh cloud
    add(kit('boing'), 14.35, 0.4)                                              # Unc leans back
    add(kit('pop2'), 15.1, 0.45)                                               # Vaeh taps the chair
    add(kit('pop'), 15.45, 0.35)                                               # chair upright
    add(kit('pop2'), 16.4, 0.5)                                                # Dad: last chair
    add(kit('sneak'), 17.2, 0.4)                                               # the cat arrives
    add(kit('rimshot'), 17.65, 0.45)                                           # the cat is already in it
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 60, 25.6, 25.1, OUT, cues)
