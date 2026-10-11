"""Combine two job photos + one raw clip into a vertical 1080x1920 reel (branded + clean versions).

Usage:  python3 -I build_combine.py <workdir>
  <workdir>/in_combine/clip.mov, portrait.jpg, landscape.jpg   (copy the uploads here first)
  outputs: <workdir>/fb_safe/BB_SuperheroParty_Combined.mp4 (hook text + phone/site strip)
           <workdir>/fb_safe/BB_SuperheroParty_Combined_Clean.mp4 (no text)

Edit for the job: CLIP_A / CLIP_B, the photo crops, and the hook text. Written for the Oct 10 superhero-party job:
 - clip is 1920x1080 HLG HDR (tone-mapped to SDR here), 16.4 s, upright until ~12.2 s, then the phone rolls
   sideways; the plan skips the roll (12.0 -> 13.7) and shows the sideways reveal shot rotated upright (transpose=1).
 - landscape.jpg has people in the top of the frame, so its crop starts below them.
 - order = attachment order: portrait, landscape, clip. ~19.9 s total. crf 22 keeps the files ~10 MB.
"""
import os, sys, shutil, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import imageio_ffmpeg

S = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
IN = f'{S}/in_combine'
OUT = f'{S}/out_combine'
FONTS = '/home/user/-raj-examples/big-business-rentals/assets/fonts'
os.makedirs(OUT, exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
PHOTO_S = 2.6
CLIP_A = (0.0, 12.0)
CLIP_B = (13.7, 16.4)
T_PHOTOS = 2 * PHOTO_S
T_CLIP_A = CLIP_A[1] - CLIP_A[0]
T_CLIP_B = CLIP_B[1] - CLIP_B[0]
TOTAL = T_PHOTOS + T_CLIP_A + T_CLIP_B
GOLD = (229, 184, 75)

def ease(k):
    k = max(0.0, min(1.0, k)); return k * k * (3 - 2 * k)

def blurred_bg(img):
    small = ImageOps.fit(img, (270, 480), Image.LANCZOS).filter(ImageFilter.GaussianBlur(14))
    return Image.eval(small.resize((W, H), Image.LANCZOS), lambda v: int(v * 0.42))

def render_photo(name, crop0, crop1, aspect, folder):
    img = ImageOps.exif_transpose(Image.open(f'{IN}/{name}.jpg')).convert('RGB')
    bg = blurred_bg(img)
    bh = int(round(W / aspect))
    y_off = (H - bh) // 2 - 40
    shutil.rmtree(folder, ignore_errors=True); os.makedirs(folder)
    n = int(PHOTO_S * FPS)
    for i in range(n):
        k = ease(i / (n - 1))
        cx = crop0[0] + (crop1[0] - crop0[0]) * k
        cy = crop0[1] + (crop1[1] - crop0[1]) * k
        cw = crop0[2] + (crop1[2] - crop0[2]) * k
        ch = cw / aspect
        box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
        fg = img.resize((W, bh), Image.LANCZOS, box=box)
        frame = bg.copy()
        sh = Image.new('RGBA', (W, bh + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle([0, 30, W, bh + 30], fill=(0, 0, 0, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        frame.paste(sh, (0, y_off - 30), sh)
        frame.paste(fg, (0, y_off))
        frame.save(f'{folder}/f{i:04d}.png')

# portrait.jpg = 1932x2576 empty tables (3:4); landscape.jpg = 2576x1932 with people in the top ~600 px, so its crop starts below them
render_photo('portrait', (966, 1288, 1932), (966, 1400, 1650), 3 / 4, f'{S}/frC1')
render_photo('landscape', (1450, 1266, 1776), (1450, 1202, 1500), 4 / 3, f'{S}/frC2')

f_h = ImageFont.truetype(f'{FONTS}/ArchivoBlack.ttf', 92)
f_s = ImageFont.truetype(f'{FONTS}/Mont700.ttf', 40)
f_p = ImageFont.truetype(f'{FONTS}/ArchivoBlack.ttf', 54)

def centered(draw, y, text, font, fill, stroke=0):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill, stroke_width=stroke, stroke_fill=(15, 8, 30))

hook = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(hook)
centered(d, 235, 'SUPERHERO PARTY.', f_h, (255, 255, 255, 255), 6)
centered(d, 345, 'TABLES SET.', f_h, GOLD + (255,), 6)
centered(d, 470, 'Tables & chairs by Big Business', f_s, (255, 255, 255, 235), 3)
hook.save(f'{OUT}/hook.png')

strip = Image.new('RGBA', (W, H), (0, 0, 0, 0))
g = Image.new('RGBA', (W, 330), (0, 0, 0, 0)); gp = g.load()
for yy in range(330):
    a = int(200 * (yy / 330) ** 1.6)
    for xx in range(W): gp[xx, yy] = (8, 6, 16, a)
strip.paste(g, (0, H - 330), g)
d = ImageDraw.Draw(strip)
centered(d, H - 215, '702-706-8287', f_p, GOLD + (255,), 4)
centered(d, H - 140, 'bigbusinesspartyrentals.com', f_s, (255, 255, 255, 240), 3)
strip.save(f'{OUT}/strip.png')

SR = 48000
NA = int(SR * TOTAL)
buf = np.zeros(NA)
rng = np.random.RandomState(7)
def add(at, sig, gain=1.0):
    i0 = int(at * SR); i1 = min(NA, i0 + len(sig))
    if 0 <= i0 < NA: buf[i0:i1] += sig[:i1 - i0] * gain
def decay(s, k): return s * np.exp(-k * np.arange(len(s)) / SR)
def tone(f, dur): return np.sin(2 * np.pi * f * np.arange(int(dur * SR)) / SR)
def gliss(f0, f1, dur): return np.sin(2 * np.pi * np.cumsum(np.linspace(f0, f1, int(dur * SR))) / SR)
def lowpass(s, a):
    o = np.zeros_like(s); acc = 0.0
    for i, v in enumerate(s): acc += a * (v - acc); o[i] = acc
    return o
def whoosh(at, dur=0.5, gain=0.5):
    n = lowpass(rng.randn(int(dur * SR)), 0.22)
    add(at, n * np.sin(np.pi * np.arange(len(n)) / len(n)) ** 2, gain)
BT = 60 / 112.0
t = 0.0
while t < T_PHOTOS - 0.2:
    fade = 1.0 if t < T_PHOTOS - 0.8 else max(0.0, (T_PHOTOS - 0.1 - t) / 0.7)
    add(t, decay(gliss(110, 38, 0.14), 22), 0.30 * fade)
    h = rng.randn(int(0.03 * SR)); add(t + BT / 2, decay(h - np.concatenate([[0], h[:-1]]), 60), 0.05 * fade)
    t += BT
whoosh(PHOTO_S - 0.32, 0.5, 0.45)
whoosh(T_PHOTOS - 0.35, 0.5, 0.5)
whoosh(T_PHOTOS + T_CLIP_A - 0.3, 0.5, 0.55)
for i, f in enumerate([880, 1320, 1760]):
    add(T_PHOTOS + T_CLIP_A + 0.05 + i * 0.09, decay(tone(f, 0.7), 5), 0.16)
m = np.max(np.abs(buf)); buf = buf / m * 0.7 if m > 0 else buf
st = np.stack([buf, buf], axis=1)
w = wave.open(f'{OUT}/sfx.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st * 32767).astype('<i2').tobytes()); w.close()

TM = ("zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,"
      "zscale=t=bt709:m=bt709:r=tv,format=yuv420p")

def build(branded, out):
    vf = (
        f"[0:v]format=yuv420p,setsar=1,fps={FPS}[a];"
        f"[1:v]format=yuv420p,setsar=1,fps={FPS}[b];"
        f"[2:v]trim={CLIP_A[0]}:{CLIP_A[1]},setpts=PTS-STARTPTS,{TM},fps={FPS},setsar=1,split[c0a][c0b];"
        f"[c0a]scale=-2:{H},crop={W}:{H},boxblur=30:3,eq=brightness=-0.22[cbg];"
        f"[c0b]scale={W}:608[cfg];[cbg][cfg]overlay=0:(H-h)/2-40,format=yuv420p,setsar=1[c];"
        f"[3:v]trim={CLIP_B[0]}:{CLIP_B[1]},setpts=PTS-STARTPTS,{TM},transpose=1,scale={W}:{H},fps={FPS},setsar=1[d];"
        f"[a][b][c][d]concat=n=4:v=1:a=0[vc]"
    )
    inputs = ['-framerate', str(FPS), '-i', f'{S}/frC1/f%04d.png',
              '-framerate', str(FPS), '-i', f'{S}/frC2/f%04d.png',
              '-i', f'{IN}/clip.mov', '-i', f'{IN}/clip.mov', '-i', f'{OUT}/sfx.wav']
    if branded:
        inputs += ['-loop', '1', '-t', f'{TOTAL:.2f}', '-i', f'{OUT}/hook.png',
                   '-loop', '1', '-t', f'{TOTAL:.2f}', '-i', f'{OUT}/strip.png']
        vf += (f";[vc][5:v]overlay=0:0:enable='between(t,0,{PHOTO_S - 0.05})'[vh];"
               f"[vh][6:v]overlay=0:0,format=yuv420p[vout]")
    else:
        vf += ";[vc]format=yuv420p[vout]"
    af = (f";[2:a]atrim={CLIP_A[0]}:{CLIP_A[1]},asetpts=PTS-STARTPTS,afade=t=in:d=0.12,afade=t=out:st={T_CLIP_A - 0.08}:d=0.08[a1];"
          f"[3:a]atrim={CLIP_B[0]}:{CLIP_B[1]},asetpts=PTS-STARTPTS,afade=t=in:d=0.08[a2];"
          f"[a1][a2]concat=n=2:v=0:a=1,adelay={int(T_PHOTOS * 1000)}|{int(T_PHOTOS * 1000)},aresample=48000[cad];"
          f"[4:a]aresample=48000[sfx];[sfx][cad]amix=inputs=2:duration=longest:normalize=0[aout]")
    cmd = [FF, '-y'] + inputs + ['-filter_complex', vf + af, '-map', '[vout]', '-map', '[aout]',
           '-t', f'{TOTAL:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '22', '-r', str(FPS),
           '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-movflags', '+faststart', out, '-loglevel', 'error']
    subprocess.run(cmd, check=True)
    print('ENCODED', out)

os.makedirs(f'{S}/fb_safe', exist_ok=True)
build(True, f'{S}/fb_safe/BB_SuperheroParty_Combined.mp4')
build(False, f'{S}/fb_safe/BB_SuperheroParty_Combined_Clean.mp4')
print('total seconds', TOTAL)
