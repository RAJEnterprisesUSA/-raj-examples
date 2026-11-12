"""TREND REMIX #27 "He Had No Idea She Was a Spy" (reelH REELS[52], 24.2s, speech clouds). OWNER-PICKED topic, Thu Nov 12:
"It has to be some type of relationship cheating ... people have to know who we are talking about without naming them."
News (AP, Nov 10 2026): a chip-company CEO's affair with an alleged foreign agent; officials said he "had absolutely no idea" she
was a spy; the stock fell ~4% that Monday. Parody of the headline only: no names, company, logo, real face or new claims; two
original characters (THE TECH BOSS, THE SPY: face hidden, no nationality/ethnicity cues). Payoff: some people cheat, we won't
cheat on you, every chair we quote shows up. Cast by story (owner Nov 12): Dad, Mrs. Never Wrong, Unc, Tyler, Lil Wobbles, the cat; the kids sit this one out.
UPGRADES: two new characters with on-screen name chips + camera-flash gag."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_NoIdeaSheWasASpy.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.6); add(bed(20.8, 96, 'groove'), 0.3, 0.38)
    for i in range(4): add(noise(0.08, 0.3, lp=0.6), 0.3+i*1.25)      # camera flashes
    add(kit('pop'), 2.6, 0.5); add(kit('sneak'), 5.0, 0.5); add(kit('whoosh'), 6.6, 0.5)
    for i in range(3): add(tone(300, 0.05, 0.12), 7.5+i*0.2)
    add(kit('kick'), 8.2, 0.8); add(kit('whoosh'), 9.0, 0.6)
    add(kit('rimshot'), 9.8, 0.4)
    add(kit('pop2'), 11.8, 0.9); add(kit('rimshot'), 12.9, 0.5)
    add(kit('rimshot'), 14.7, 0.4); add(kit('boing'), 16.5, 0.5)
    for i in range(9): add(kit('pop'), 18.8+i*0.1, 0.45)
    add(kit('win'), 18.5, 0.7); add(kit('applause'), 18.9, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 52, 24.2, 23.7, OUT, cues)
