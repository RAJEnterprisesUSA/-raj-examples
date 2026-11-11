"""TREND REMIX #24 "We Let the AI Plan the Party" (reelH REELS[49], 24.2s, readable caption holds). CONTROVERSY lane, owner Tue
Nov 10 6:40pm: "Let's post a remix for tonight. Whats controversial right now today". Topic: Nov 10 2026 backlash over a new AI
app that reads your camera roll to help "run your family" (critics: outsourcing parenting to AI). No app, company or founder
named. The AI scans the family photos, orders ONE chair for nine (Lil Wobbles, NOPE.), Mrs. Never Wrong does the math (9), Tyler,
the AI seats the cat at the head; the crew carries in nine chairs. Payoff: AI can plan the party, it can't carry the chairs.
UPGRADES: on-screen AI planner panel with a live scan bar + every caption held >= 1.8 s (owner Nov 9 feedback)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE
OUT = BASE/'halloween/BB_Trend_AIPlansTheParty.mp4'
def cues(add):
    add(kit('sneak'), 0.05, 0.5)
    add(bed(20.6, 104, 'groove'), 0.3, 0.42)
    for i in range(10): add(tone(1800+i*90, 0.04, 0.1), 2.7+i*0.2)       # scanning beeps
    add(kit('rimshot'), 4.9, 0.4)
    add(tone(600, 0.12, 0.25), 6.6); add(kit('pop2'), 6.7, 0.7)
    for i in range(4): add(tone(300, 0.05, 0.12), 8.9+i*0.12)
    add(kit('kick'), 9.4, 0.8)
    add(kit('pop'), 10.7, 0.6); add(tone(1500, 0.1, 0.2), 11.0)
    add(kit('pop2'), 12.8, 0.9); add(kit('rimshot'), 14.6, 0.5)
    add(kit('sneak'), 16.4, 0.5)
    for i in range(9): add(kit('pop'), 18.6+i*0.1, 0.45)
    add(kit('win'), 18.5, 0.7); add(kit('applause'), 18.8, 0.7)
if __name__ == '__main__':
    render_reel('halloween/reelH.html', 49, 24.2, 23.7, OUT, cues)
