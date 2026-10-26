"""Sunday Nov 1 videos (Season Two begins): TREND REMIX #14 "POV: hosting Thanksgiving in 2026" (reelH REELS[37],
17.2s, Season Two look STYLER2) and EP. 41 Meet the Family, the Season Two premiere (reelsD REELS[41], 26s; record
0 W · 1 L). This build's upgrade: the Season Two rig (new Mr. Big Business look, four kid rigs with braids, locs,
tiara, headphones and phone) and the psychology playbook story rules (competence first, complete punchline, ask
only on the end card)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE

T37 = BASE/'halloween/BB_Trend_POVThanksgiving2026.mp4'
EP41 = BASE.parent/'fb_safe/BB_Chronicles_Ep41_MeetTheFamily.mp4'

def cues_t37(add):
    add(kit('pop'), 0.05)
    add(bed(14.0, 112, 'groove'), 0.3, 0.5)
    for at in (1.8, 4.2, 6.6, 9.0): add(kit('rimshot'), at, 0.55)
    for i in range(10): add(kit('pop2'), 1.9+i*0.2, 0.3)          # maybe bubbles + counter
    for i in range(4): add(kit('pop'), 4.25+i*0.6, 0.5)           # guest list jumps
    add(kit('sneak'), 6.7, 0.6)                                   # the cats
    add(kit('boing'), 9.1)                                        # turkey seat
    add(kit('win'), 11.4); add(kit('applause'), 12.0, 0.8)

def cues_ep41(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.45); add(kit('kick'), 0.8)                 # table snaps into place
    for at in (2.4, 4.8, 7.2): add(kit('pop2'), at, 0.8)             # kids pop in
    add(kit('whoosh'), 9.8, 0.6); add(kit('rimshot'), 11.2)          # vaeh + "so embarrassing"
    add(noise(0.12, 0.5, lp=0.3), 14.6); add(kit('freeze'), 14.6, 0.7)   # family photo flash
    add(kit('sneak'), 15.6, 0.6); add(kit('pop'), 17.2, 0.7)         # the cat obeys the princess
    add(kit('whoosh'), 18.8, 0.6); add(kit('sadtrom'), 20.2, 0.7)    # vaeh set the whole table
    add(kit('applause'), 21.4, 0.5)
    add(kit('theme'), 22.5, 0.6)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if which in ('t37', 'both'): render_reel('halloween/reelH.html', 37, 17.2, 16.7, T37, cues_t37)
    if which in ('ep41', 'both'): render_reel('reelsD.html', 41, 26.0, 25.2, EP41, cues_ep41)
