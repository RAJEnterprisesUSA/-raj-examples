"""Final Hosting Chaos #1 cut: cleaned frames 1-168 (7.0s), then a 1.0s push-in hold on the
host's deadpan stare, 1080x1920, hook text in the first seconds, AI SKIT tag throughout,
the clip's own audio (8.0s). The end frame cuts back to frame one for the loop."""
import pathlib, subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

HERE = pathlib.Path(__file__).parent
FONTS = pathlib.Path("/home/user/-raj-examples/big-business-rentals/assets/fonts")
OUT_MP4 = pathlib.Path("/home/user/-raj-examples/big-business-rentals/tiktok/TT_HostingChaos_ACouplePeople.mp4")
FPS, W, H = 24, 1080, 1920
CUT, HOLD = 168, 24
F_HOOK = ImageFont.truetype(str(FONTS/"ArchivoBlack.ttf"), 68)
F_TAG = ImageFont.truetype(str(FONTS/"Oswald600.ttf"), 34)
INK, GOLD = (20, 12, 30), (229, 184, 75)
FACE = (190, 380)            # host's face in the 720x1280 source, for the push-in

def hook(d, alpha_frames):
    lines = ["HE SAID", '"A COUPLE PEOPLE."']
    for i, ln in enumerate(lines):
        w = d.textlength(ln, font=F_HOOK)
        d.text(((W-w)/2, 185+i*84), ln, font=F_HOOK, fill=(255, 255, 255),
               stroke_width=11, stroke_fill=INK)

def tag(d):
    t = "AI SKIT"
    w = d.textlength(t, font=F_TAG)
    x1 = W-40; x0 = x1-int(w)-40
    d.rounded_rectangle((x0, 392, x1, 448), 18, fill=(36, 18, 67), outline=GOLD, width=3)
    d.text((x0+20, 397), t, font=F_TAG, fill=GOLD)

def frame(i):
    if i < CUT:
        src = Image.open(HERE/f"clean/{i+1:04d}.png").convert("RGB")
    else:
        k = (i-CUT+1)/HOLD
        z = 1+0.28*(k*k*(3-2*k))
        src = Image.open(HERE/f"clean/{CUT:04d}.png").convert("RGB")
        sw, sh = 720/z, 1280/z
        cx = min(max(FACE[0], sw/2), 720-sw/2); cy = min(max(FACE[1], sh/2), 1280-sh/2)
        src = src.crop((int(cx-sw/2), int(cy-sh/2), int(cx+sw/2), int(cy+sh/2)))
    f = src.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(f)
    if i < int(2.6*FPS):
        hook(d, i)
    tag(d)
    return f

def main():
    tmp = HERE/"out"; tmp.mkdir(exist_ok=True)
    n = CUT+HOLD
    for i in range(n):
        frame(i).save(tmp/f"{i:04d}.png")
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, "-y", "-framerate", str(FPS), "-i", str(tmp/"%04d.png"), "-i", str(HERE/"src.mp4"),
           "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
           "-preset", "medium", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
           "-t", f"{n/FPS:.3f}", str(OUT_MP4)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.returncode, r.stderr[-200:] if r.returncode else "encoded", OUT_MP4.name, n, "frames")

if __name__ == "__main__":
    main()
