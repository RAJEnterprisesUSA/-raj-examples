import os, sys, subprocess, shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pymupdf
import imageio_ffmpeg

S = '/tmp/claude-0/-home-user--raj-examples/3d009e7e-4e78-50bc-a373-5a916eff7e8c/scratchpad'
IN = f'{S}/in_rate'
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1440, 1080, 30
MODE = sys.argv[1] if len(sys.argv) > 1 else 'full'   # 'sheet' = contact sheet only

BG = (12, 10, 22)
GOLD = (229, 184, 75)

# ---------------- rate sheet page on a dark canvas ----------------
doc = pymupdf.open(f'{IN}/ratesheet.pdf')
pix = doc[0].get_pixmap(dpi=300)
page = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
PW, PH = page.size                    # 2550 x 3300
CW, CH = 4800, 3600
canvas = Image.new('RGB', (CW, CH), BG)
x0, y0 = (CW - PW) // 2, (CH - PH) // 2
shadow = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rectangle([x0 + 30, y0 + 40, x0 + PW + 30, y0 + PH + 40], fill=(0, 0, 0, 170))
shadow = shadow.filter(ImageFilter.GaussianBlur(40))
canvas.paste(shadow, (0, 0), shadow)
canvas.paste(page, (x0, y0))

# camera = (left, top, width) in canvas coords, 4:3 aspect
def cam(px, py, w):
    return (x0 + px, y0 + py, w)
K0 = (0, 0, CW)                              # full view
K1 = cam(88, 346, 2377)                      # title + packages + included/add-ons
K2 = cam(88, 1477, 2377)                     # add-ons, area, drop-off, footer
KEYS = [
    (0.0, K0), (1.1, K0),
    (1.9, K1), (5.0, K1),
    (5.9, K2), (9.0, K2),
]
SHEET_T = KEYS[-1][0]

def ease(k):
    k = max(0.0, min(1.0, k))
    return k * k * (3 - 2 * k)

def camera_at(t):
    for (ta, ca), (tb, cb) in zip(KEYS, KEYS[1:]):
        if ta <= t <= tb:
            if ca == cb:
                return ca
            k = ease((t - ta) / (tb - ta))
            return tuple(ca[i] + (cb[i] - ca[i]) * k for i in range(3))
    return KEYS[-1][1]

def sheet_frame(t):
    l, tp, w = camera_at(t)
    h = w * H / W
    l = max(0, min(CW - w, l)); tp = max(0, min(CH - h, tp))
    box = (int(l), int(tp), int(l + w), int(tp + h))
    return canvas.crop(box).resize((W, H), Image.LANCZOS)

# ---------------- logo card ----------------
logo = Image.open(f'{IN}/logo.png').convert('RGBA')
LOGO_T = 3.6
f_url = ImageFont.truetype(f'{S}/fonts/Mont600.ttf', 34)

def logo_frame(t):
    bgc = Image.new('RGB', (W, H), (8, 7, 15))
    # soft gold glow behind the logo
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([W // 2 - 470, 40, W // 2 + 470, 980], fill=(229, 184, 75, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    bgc.paste(glow, (0, 0), glow)
    zoom = 0.94 + 0.06 * ease(t / LOGO_T)
    d = int(880 * zoom)
    lg = logo.resize((d, d), Image.LANCZOS)
    bgc.paste(lg, ((W - d) // 2, 48 + (880 - d) // 2), lg)
    a = ease((t - 0.8) / 0.6)
    if a > 0:
        txt = Image.new('RGBA', (W, 90), (0, 0, 0, 0))
        dr = ImageDraw.Draw(txt)
        s = 'bigbusinesspartyrentals.com   ·   @bigbusiness_rentals_events'
        tw = dr.textlength(s, font=f_url)
        dr.text(((W - tw) / 2, 20), s, font=f_url, fill=(229, 184, 75, int(255 * a)))
        bgc.paste(txt, (0, 972), txt)
    return bgc

def fade_in(img, t, dur):
    k = ease(t / dur)
    if k >= 1:
        return img
    return Image.eval(img, lambda v: int(v * k))

if MODE == 'sheet':
    ts = [0.2, 1.0, 1.9, 3.5, 5.0, 5.9, 7.4, 8.9]
    ims = [sheet_frame(t).resize((480, 360)) for t in ts] + [logo_frame(t).resize((480, 360)) for t in (0.2, 3.5)]
    sh = Image.new('RGB', (480 * 5, 360 * 2))
    for i, im in enumerate(ims):
        sh.paste(im, ((i % 5) * 480, (i // 5) * 360))
    sh.save(f'{S}/out_rate/cards_sheet.png')
    print('contact sheet written')
    sys.exit(0)

# ---------------- render card frames ----------------
fr = f'{S}/frRATE'
shutil.rmtree(fr, ignore_errors=True)
os.makedirs(fr)
n = 0
for i in range(int(SHEET_T * FPS)):
    t = i / FPS
    img = fade_in(sheet_frame(t), t, 0.35)
    img.save(f'{fr}/f{n:05d}.jpg', quality=95); n += 1
for i in range(int(LOGO_T * FPS)):
    t = i / FPS
    img = fade_in(logo_frame(t), t, 0.45)
    img.save(f'{fr}/f{n:05d}.jpg', quality=95); n += 1
total_card_s = n / FPS
print('card frames', n, 'seconds', total_card_s)

# ---------------- cards -> silent video segment ----------------
subprocess.run([FF, '-y', '-framerate', str(FPS), '-i', f'{fr}/f%05d.jpg', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                '-crf', '16', '-vf', 'setsar=1', f'{S}/out_rate/cards_seg.mp4', '-loglevel', 'error'], check=True)

# ---------------- original clip -> SDR (tone-mapped), then join; audio kept as recorded ----------------
vf_src = ("zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,"
          "zscale=t=bt709:m=bt709:r=tv,format=yuv420p,fps=30,setsar=1")
out = f'{S}/fb_safe/BB_VenueWalkthrough_RateSheet.mp4'
os.makedirs(f'{S}/fb_safe', exist_ok=True)
fc = (f"[0:v]{vf_src}[v0];[1:v]fps=30,setsar=1[v1];[v0][v1]concat=n=2:v=1:a=0[v];"
      f"anullsrc=r=44100:cl=stereo,atrim=0:{total_card_s:.3f}[sil];[0:a][sil]concat=n=2:v=0:a=1[a]")
subprocess.run([FF, '-y', '-i', f'{IN}/video.mov', '-i', f'{S}/out_rate/cards_seg.mp4', '-filter_complex', fc,
                '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                '-c:a', 'aac', '-b:a', '160k', '-ar', '44100', '-movflags', '+faststart', out, '-loglevel', 'error'], check=True)
print('ENCODED', out)
