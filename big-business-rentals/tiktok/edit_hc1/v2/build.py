"""Hosting Chaos #1, take 2 (owner's avatar as the cousin).

Shot 1 (files 1-96): track the chip bag and paint out its red "CHOP" label every frame.
Shot 2: the reaction plays files 97-145 (smile fading), then a 2s push-in hold on file 145,
the flattest expression. 192 frames, 8.0s, hook text 0-2.6s, AI SKIT tag throughout,
the clip's own audio."""
import pathlib, subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

HERE = pathlib.Path(__file__).parent
FR, CLEAN, OUT = HERE/"fr", HERE/"clean", HERE/"out"
for p in (CLEAN, OUT): p.mkdir(exist_ok=True)
FONTS = pathlib.Path("/home/user/-raj-examples/big-business-rentals/assets/fonts")
OUT_MP4 = pathlib.Path("/home/user/-raj-examples/big-business-rentals/tiktok/TT_HostingChaos_ACouplePeople_v2.mp4")
SHOT1_END, REACT_END, TOTAL, FPS, W, H = 96, 145, 192, 24, 1080, 1920
FACE = (360, 520)            # host's face centre in the 720x1280 close-up

def clean_shot1():
    first = cv2.imread(str(FR/"0001.png"))
    box = [412, 565, 68, 72]                       # x, y, w, h around the bag in frame 1
    tmpl = first[box[1]:box[1]+box[3], box[0]:box[0]+box[2]].copy()
    for n in range(1, SHOT1_END+1):
        img = cv2.imread(str(FR/f"{n:04d}.png"))
        x, y, w, h = box
        sx, sy = max(0, x-50), max(0, y-50)
        search = img[sy:y+h+50, sx:x+w+50]
        res = cv2.matchTemplate(search, tmpl, cv2.TM_CCOEFF_NORMED)
        _, score, _, loc = cv2.minMaxLoc(res)
        if score > 0.4:
            box = [sx+loc[0], sy+loc[1], w, h]
            x, y = box[0], box[1]
            tmpl = img[y:y+h, x:x+w].copy()
        roi = img[y:y+h, x:x+w].astype(int)
        b, g, r = roi[..., 0], roi[..., 1], roi[..., 2]
        red = ((r > 75) & (g < 60) & (b < 60) & (r-g > 55)).astype(np.uint8)*255
        red = cv2.morphologyEx(red, cv2.MORPH_CLOSE, np.ones((11, 11), np.uint8))
        red = cv2.dilate(red, np.ones((5, 5), np.uint8))
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[y:y+h, x:x+w] = red
        if mask.any():
            img = cv2.inpaint(img, mask, 6, cv2.INPAINT_TELEA)
        cv2.imwrite(str(CLEAN/f"{n:04d}.png"), img)

F_HOOK = ImageFont.truetype(str(FONTS/"ArchivoBlack.ttf"), 68)
F_TAG = ImageFont.truetype(str(FONTS/"Oswald600.ttf"), 34)
INK, GOLD = (20, 12, 30), (229, 184, 75)

def overlay(f, i):
    d = ImageDraw.Draw(f)
    if i < int(2.6*FPS):
        for k, ln in enumerate(["HE SAID", '"A COUPLE PEOPLE."']):
            w = d.textlength(ln, font=F_HOOK)
            d.text(((W-w)/2, 185+k*84), ln, font=F_HOOK, fill=(255, 255, 255),
                   stroke_width=11, stroke_fill=INK)
    t = "AI SKIT"; w = d.textlength(t, font=F_TAG); x1 = W-40; x0 = x1-int(w)-40
    d.rounded_rectangle((x0, 392, x1, 448), 18, fill=(36, 18, 67), outline=GOLD, width=3)
    d.text((x0+20, 397), t, font=F_TAG, fill=GOLD)

def frame(i):
    if i < SHOT1_END:
        src = Image.open(CLEAN/f"{i+1:04d}.png").convert("RGB")
    elif i < REACT_END:
        src = Image.open(FR/f"{i+1:04d}.png").convert("RGB")
    else:
        k = (i-REACT_END+1)/(TOTAL-REACT_END)
        z = 1+0.22*(k*k*(3-2*k))
        src = Image.open(FR/f"{REACT_END:04d}.png").convert("RGB")
        sw, sh = 720/z, 1280/z
        cx = min(max(FACE[0], sw/2), 720-sw/2); cy = min(max(FACE[1], sh/2), 1280-sh/2)
        src = src.crop((int(cx-sw/2), int(cy-sh/2), int(cx+sw/2), int(cy+sh/2)))
    f = src.resize((W, H), Image.LANCZOS)
    overlay(f, i)
    return f

def main():
    clean_shot1()
    for i in range(TOTAL):
        frame(i).save(OUT/f"{i:04d}.png")
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, "-y", "-framerate", str(FPS), "-i", str(OUT/"%04d.png"), "-i", str(HERE/"src.mp4"),
           "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
           "-preset", "medium", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
           "-t", f"{TOTAL/FPS:.3f}", str(OUT_MP4)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.returncode, r.stderr[-200:] if r.returncode else "encoded", OUT_MP4.name)

if __name__ == "__main__":
    main()
