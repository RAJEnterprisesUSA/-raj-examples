"""Guess the Theme: Old Vegas Lounge. Pt. 1 (3 clues) and Pt. 2 (reveal), 1080x1920 video.

Images are AI concept art (HF Z-Image) and carry an "AI CONCEPT ART" stamp on every frame.
Frame one of each part is its most interesting frame: Pt. 1 opens on the first clue with the
question already on screen, Pt. 2 opens on the finished reveal and ends on it again (loop).
"""
import math, pathlib, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import imageio_ffmpeg

HERE = pathlib.Path(__file__).parent
G = HERE/"gtt"
FONTS = HERE.parent/"assets/fonts"
W, H, FPS, SR = 1080, 1920, 35, 48000
GOLD, INK, CREAM = (229, 184, 75), (20, 12, 30), (246, 241, 228)
F_BIG = ImageFont.truetype(str(FONTS/"ArchivoBlack.ttf"), 76)
F_MID = ImageFont.truetype(str(FONTS/"ArchivoBlack.ttf"), 58)
F_TAG = ImageFont.truetype(str(FONTS/"Oswald600.ttf"), 34)
F_STAMP = ImageFont.truetype(str(FONTS/"Oswald600.ttf"), 30)
IMG_Y, IMG_S = 420, 1080

def load(name):
    return Image.open(G/f"{name}.png").convert("RGB")

def backdrop(img):
    bg = img.resize((H, H), Image.LANCZOS).crop(((H-W)//2, 0, (H-W)//2+W, H))
    bg = bg.filter(ImageFilter.GaussianBlur(38))
    return Image.eval(bg, lambda v: int(v*0.42))

def kenburns(img, k, zoom=0.08):
    z = 1+zoom*k
    s = int(1024/z); o = (1024-s)//2
    return img.crop((o, o, o+s, o+s)).resize((IMG_S, IMG_S), Image.LANCZOS)

def text_c(d, y, lines, font, fill=CREAM, stroke=10):
    for i, ln in enumerate(lines):
        w = d.textlength(ln, font=font)
        d.text(((W-w)/2, y+i*int(font.size*1.18)), ln, font=font, fill=fill,
               stroke_width=stroke, stroke_fill=INK)

def chrome(frame, tag):
    d = ImageDraw.Draw(frame)
    d.rounded_rectangle((40, 150, 40+int(d.textlength(tag, font=F_TAG))+48, 214), 20,
                        fill=(36, 18, 67), outline=GOLD, width=4)
    d.text((64, 158), tag, font=F_TAG, fill=GOLD)
    # the concept-art stamp, rotated, on the image corner
    st = Image.new("RGBA", (330, 70), (0, 0, 0, 0))
    sd = ImageDraw.Draw(st)
    sd.rounded_rectangle((0, 0, 329, 69), 12, fill=GOLD+(240,))
    sd.text((24, 14), "AI CONCEPT ART", font=F_STAMP, fill=INK)
    st = st.rotate(6, expand=True, resample=Image.BICUBIC)
    frame.paste(st, (W-st.width-36, IMG_Y+36), st)
    return d

def compose(img, k, bg):
    f = bg.copy()
    f.paste(kenburns(img, k), (0, IMG_Y))
    return f

def triptych(imgs, bg):
    f = bg.copy()
    s = 340
    for i, im in enumerate(imgs):
        f.paste(im.resize((s, s), Image.LANCZOS), (15+i*(s+15), IMG_Y+370))
    return f

def write(frames_fn, n, out, audio):
    tmp = HERE/"_frames"; tmp.mkdir(exist_ok=True)
    for i in range(n):
        frames_fn(i/FPS).save(tmp/f"{i:04d}.png")
    wav = tmp/"a.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((audio*32767).astype(np.int16).tobytes())
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, "-y", "-framerate", str(FPS), "-i", str(tmp/"%04d.png"), "-i", str(wav),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-preset", "medium",
           "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "-t", f"{n/FPS:.2f}", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    for p in tmp.glob("*"): p.unlink()
    tmp.rmdir()
    print(r.returncode, r.stderr[-200:] if r.returncode else "encoded", out.name)

def lounge_bed(dur, hits):
    """Original sound: a walking upright-bass line, brushed hats on 2 and 4, a ding per clue."""
    n = int(SR*dur); a = np.zeros(n); t = np.arange(n)/SR
    bpm = 120; beat = 60/bpm
    walk = [55.0, 61.74, 65.41, 73.42, 82.41, 73.42, 65.41, 61.74]
    for b in range(int(dur/beat)+1):
        i0 = int(b*beat*SR); L = int(beat*SR*0.9)
        if i0 >= n: break
        L = min(L, n-i0); tt = np.arange(L)/SR
        f = walk[b % len(walk)]
        a[i0:i0+L] += 0.5*np.sin(2*np.pi*f*tt)*np.exp(-tt*5)
        if b % 2 == 1:
            hl = min(int(0.09*SR), n-i0)
            a[i0:i0+hl] += 0.08*np.random.randn(hl)*np.exp(-np.arange(hl)/SR*40)
    for at in hits:
        i0 = int(at*SR); L = min(int(0.5*SR), n-i0); tt = np.arange(L)/SR
        a[i0:i0+L] += 0.28*(np.sin(2*np.pi*1046.5*tt)+0.5*np.sin(2*np.pi*1568*tt))*np.exp(-tt*6)
    return a/np.max(np.abs(a))*0.75

def part1():
    clues = [load("clue1_dice"), load("clue2_chandelier"), load("clue3_martini")]
    bgs = [backdrop(c) for c in clues]
    SEG, TRI = 2.6, 2.4
    total = SEG*3+TRI
    def fr(t):
        if t < SEG*3:
            i = min(2, int(t//SEG)); k = (t-i*SEG)/SEG
            f = compose(clues[i], k, bgs[i])
            d = chrome(f, "GUESS THE THEME · Pt. 1")
            text_c(d, 250, ["GUESS THE PARTY THEME", "FROM 3 CLUES."] if i == 0 else [f"CLUE {i+1} OF 3."],
                   F_MID if i == 0 else F_BIG)
            return f
        f = triptych(clues, bgs[0])
        d = chrome(f, "GUESS THE THEME · Pt. 1")
        text_c(d, 245, ["SO WHAT IS", "THE THEME?"], F_BIG)
        text_c(d, IMG_Y+800, ["REVEAL IN Pt. 2."], F_MID, fill=GOLD)
        return f
    n = int(total*FPS)
    write(fr, n, HERE/"TT_GuessTheTheme_OldVegas_Pt1.mp4", lounge_bed(n/FPS, [0.05, SEG, SEG*2, SEG*3]))

def part2():
    rev = load("reveal_lounge"); clues = [load("clue1_dice"), load("clue2_chandelier"), load("clue3_martini")]
    bg = backdrop(rev); cbgs = [backdrop(c) for c in clues]
    total = 9.4
    def fr(t):
        if t < 2.6 or t >= 7.6:
            k = (t/2.6) if t < 2.6 else 1-(t-7.6)/1.8
            f = compose(rev, max(0.0, min(1.0, k)), bg)
            d = chrome(f, "GUESS THE THEME · Pt. 2")
            text_c(d, 250, ["THE THEME:", "OLD VEGAS LOUNGE."], F_MID)
            return f
        i = min(2, int((t-2.6)//(5.0/3))); k = ((t-2.6)-i*(5.0/3))/(5.0/3)
        f = compose(clues[i], k, cbgs[i])
        d = chrome(f, "GUESS THE THEME · Pt. 2")
        text_c(d, 250, [["THE DICE: CENTERPIECES."], ["THE STARBURST LIGHTS."], ["THE MARTINI STAGE."]][i], F_MID)
        return f
    n = int(total*FPS)
    write(fr, n, HERE/"TT_GuessTheTheme_OldVegas_Pt2.mp4", lounge_bed(n/FPS, [0.05, 2.6, 2.6+5/3, 2.6+10/3, 7.6]))

if __name__ == "__main__":
    part1(); part2()
