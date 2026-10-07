import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad')

TIMES = [0.5, 2.0, 3.4, 4.8, 5.5, 6.3, 7.0, 8.3]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':540,'height':960}, device_scale_factor=1)
    pg.goto('file://'+str(BASE/'halloween/reelH.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.evaluate("""async()=>{
      const F=['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat','900 italic 40px Playfair'];
      for(const f of F){ try{ await document.fonts.load(f);}catch(e){} }
    }""")
    pg.wait_for_timeout(500)
    pg.evaluate("setReel(14)")
    pg.evaluate("drawFrame(0)")
    cv = pg.locator('canvas')
    tiles = []
    for i, t in enumerate(TIMES):
        pg.evaluate(f"drawFrame({t})")
        f = OUT/f'g14_{i}.png'
        cv.screenshot(path=str(f))
        tiles.append(Image.open(f))
    b.close()
w, h = tiles[0].size
sheet = Image.new('RGB', (w*4, h*2))
for i, im in enumerate(tiles):
    sheet.paste(im, ((i%4)*w, (i//4)*h))
sheet.save(OUT/'g14_sheet.png')
print('sheet saved')
