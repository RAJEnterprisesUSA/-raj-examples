"""SLOW CUTS of the Spy two-parter (owner Thu Nov 12: "The first video still moves to fast."). reelH REELS[54] = T52 Part 1 and
REELS[55] = T53 Part 2, both played 35% slower so every caption and speech cloud holds ~3 s. Sound cues scale with the picture.
Outputs: halloween/BB_Trend_NoIdeaSheWasASpy_Slow.mp4 (31.55s), halloween/BB_Trend_SpyPart2_TargetBigBusiness_Slow.mp4 (29.93s)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio')); sys.path.insert(0, str(pathlib.Path(__file__).parent))
import render30
import build_remix_spy as p1, build_remix_spy2 as p2
S = 1.35
def scaled(mod):
    def cues(add):
        ob = mod.bed; mod.bed = lambda d, *a: ob(d * S, *a)
        try: mod.cues(lambda clip, t, *a: add(clip, t * S, *a))
        finally: mod.bed = ob
    return cues
B = render30.BASE
if __name__ == '__main__':
    which = sys.argv[1:] or ['1', '2']
    if '1' in which: render30.render_reel('halloween/reelH.html', 54, 21.0*S + 3.2, 21.0*S + 2.7, B/'halloween/BB_Trend_NoIdeaSheWasASpy_Slow.mp4', scaled(p1))
    if '2' in which: render30.render_reel('halloween/reelH.html', 55, 19.8*S + 3.2, 19.8*S + 2.7, B/'halloween/BB_Trend_SpyPart2_TargetBigBusiness_Slow.mp4', scaled(p2))
