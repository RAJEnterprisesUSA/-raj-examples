"""UPGRADE Oct 28: designed cover images for every video (1080x1920). A punchline frame from the video,
a dark gradient, a gold kicker, a big two-line title and the logo, kept inside the center 3:4 zone so
the Instagram grid crop never cuts the title. Usage: make_cover(video, sec, kicker, [line1, line2], out)"""
import pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

BASE = pathlib.Path(__file__).parent
FONTS = BASE/'assets/fonts'
FF = imageio_ffmpeg.get_ffmpeg_exe()
GOLD = (229, 184, 75); INK = (36, 26, 16)

def _font(name, size): return ImageFont.truetype(str(FONTS/name), size)

def make_cover(video, sec, kicker, lines, out):
    tmp = pathlib.Path(out).with_suffix('.frame.png')
    subprocess.run([FF, '-v', 'error', '-y', '-ss', str(sec), '-i', str(video), '-frames:v', '1', str(tmp)], check=True)
    im = Image.open(tmp).convert('RGB').resize((1080, 1920)); tmp.unlink()
    # gradient for legibility over the lower-middle band
    grad = Image.new('L', (1, 1920))
    for y in range(1920):
        grad.putpixel((0, y), int(max(0, min(230, (y-900)/700*230))) if y > 900 else 0)
    shade = Image.new('RGB', (1080, 1920), (14, 6, 24))
    im = Image.composite(shade, im, grad.resize((1080, 1920)))
    d = ImageDraw.Draw(im)
    # kicker pill
    kf = _font('Oswald600.ttf', 46); kw = d.textlength(kicker, font=kf)
    d.rounded_rectangle([540-kw/2-34, 1180, 540+kw/2+34, 1252], radius=26, fill=GOLD)
    d.text((540, 1216), kicker, font=kf, fill=INK, anchor='mm')
    # title, auto-sized to fit 960px
    size = 118
    while size > 60:
        tf = _font('ArchivoBlack.ttf', size)
        if max(d.textlength(l, font=tf) for l in lines) <= 960: break
        size -= 4
    y = 1300
    for l in lines:
        d.text((540, y), l, font=tf, fill='white', anchor='ma', stroke_width=10, stroke_fill=INK)
        y += int(size*1.12)
    # logo bottom-center, still inside the 3:4 zone
    logo = Image.open(BASE/'assets/bb_logo.png').convert('RGBA').resize((150, 150))
    im.paste(logo, (465, y+18), logo)
    im.save(out)
    return out

if __name__ == '__main__':
    v, s, k, l1, l2, o = sys.argv[1:7]
    print(make_cover(v, float(s), k, [l1, l2], o))


def make_cover_canvas(html, reel, sec, kicker, lines, out):
    """Same cover, but the background frame is rendered straight from the canvas with captions off."""
    import glob
    from playwright.sync_api import sync_playwright
    tmp = pathlib.Path(out).with_suffix('.frame.png')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0])
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.goto('file://'+str(BASE/html)); pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(400)
        pg.evaluate(f"window.NOCAP=true; setReel({reel}); drawFrame({sec}); drawFrame({sec})")
        pg.locator('canvas').screenshot(path=str(tmp)); b.close()
    tmpv = pathlib.Path(out).with_suffix('.frame.mp4')
    subprocess.run([FF, '-v', 'error', '-y', '-loop', '1', '-i', str(tmp), '-t', '0.2', '-pix_fmt', 'yuv420p', str(tmpv)], check=True)
    tmp.unlink()
    r = make_cover(tmpv, 0.0, kicker, lines, out); tmpv.unlink(); return r
