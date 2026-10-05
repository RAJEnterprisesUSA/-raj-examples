import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad')
OUT.mkdir(parents=True, exist_ok=True)

TIMES = [0.4, 1.2, 2.0, 2.8, 4.2, 5.6, 7.2, 9.0, 9.8, 12.0, 13.8, 14.6, 15.6, 16.7, 17.8, 19.5]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':540,'height':960}, device_scale_factor=1)
    pg.goto('file://'+str(BASE/'reelsD.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.wait_for_timeout(800)
    pg.evaluate("setReel(16)")
    frames=[]
    for t in TIMES:
        pg.evaluate(f"drawFrame({t})")
        fp = OUT/f'ep16_{t:.2f}.png'
        pg.locator('canvas').screenshot(path=str(fp))
        frames.append(fp)
    b.close()

imgs=[Image.open(f) for f in frames]
w,h=imgs[0].size
sheet=Image.new('RGB',(w*4,h*4),'black')
for i,im in enumerate(imgs):
    sheet.paste(im,((i%4)*w,(i//4)*h))
sheet.save(OUT/'ep16_contactsheet.png')
print('sheet saved', w*4, h*3)
