"""Friday Nov 20 TREND REMIX #31 "The Soup Swap" (reelH REELS[58], 24.2s, ~3 s caption holds, speech clouds, cast by story).
SOCIAL pool, checked Nov 20 (Google News, dated Nov 14 to Nov 19 2026): Food & Wine, Nov 14, "The Soup Swap Is TikTok's Coziest Hosting Trend"
(each guest brings a pot of soup and everyone swaps), plus a local soup swap event story dated Nov 19. No brand, app, person or place is named on screen.
Remix: four pots, one card table. Mrs. Never Wrong sets her pot on the floor and says nothing, Vaeh tosses her pot without looking up, Princess
tosses hers on top, the card table taps out, a real table with a chair for every pot fixes it, the cat takes the best seat.
Cast: Dad (STYLER2), Mrs. Never Wrong, Vaeh, Princess, the cat (new mix: not the Push It cast of Lil, Baby and Unc). No prices on screen.
UPGRADES: live POTS counter that flips to ON THE TABLE, pot pile that sags before it collapses, thrown pots with arcs, steaming pots."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_SoupSwap.mp4'
def cues(add):
    add(bed(21.0, 100, 'groove'), 0.2, 0.40)
    add(kit('pop'), 3.0, 0.5)                                            # Dad's cloud
    for i in range(7): add(tone(110+(i%2)*14, 0.06, 0.12), 3.2+i*0.2)    # footsteps
    add(tone(170, 0.10, 0.22), 4.6)                                      # Mrs. Never Wrong sets her pot down
    add(tone(520, 0.08, 0.2), 4.85); add(tone(210, 0.12, 0.26), 5.3)     # Vaeh toss and landing
    add(tone(520, 0.08, 0.2), 7.05); add(tone(230, 0.12, 0.28), 7.5)     # Princess toss and landing
    for i in range(5): add(tone(150-i*8, 0.45, 0.10, 'saw', bend=0.12), 7.55+i*0.17)   # the table creaks
    add(kit('freeze'), 8.4, 0.5)                                         # the card table taps out
    add(noise(0.5, 0.35, 0.2), 8.4)
    for t0 in (8.95, 9.05, 9.15): add(tone(900-int((t0-8.95)*1200), 0.12, 0.2), t0)   # pots clang
    add(kit('sadtrom'), 9.6, 0.5)
    add(kit('rimshot'), 11.6, 0.5)
    add(kit('whoosh'), 12.1, 0.6)
    add(kit('pop2'), 12.5, 0.6)                                          # the real table arrives
    for t0 in (13.4, 13.85, 14.3, 14.75): add(tone(620, 0.08, 0.22), t0+0.5)   # each pot lands on the table
    add(kit('sneak'), 16.4, 0.4)                                         # the cat
    add(kit('win'), 18.1, 0.7); add(kit('applause'), 18.3, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 58, 24.2, 23.7, OUT, cues)
