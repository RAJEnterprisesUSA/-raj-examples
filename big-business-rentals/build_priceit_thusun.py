"""Render the four Thu-Sun PRICE IT cards (fresh images, venue scale) + story9 pads."""
import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'inspo'
S9 = BASE/'story9'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_priceit.py').read_text()
TPL = src.split('TPL = """')[1].split('"""')[0]

JOBS = [
    ("setup_quinceballroom.png", "BB_PriceIt_QuinceBallroom.png"),
    ("setup_rooftopglow.png",    "BB_PriceIt_RooftopGlow.png"),
    ("setup_kidscartoon.png",    "BB_PriceIt_KidsCartoon.png"),
    ("setup_fallharvest.png",    "BB_PriceIt_FallHarvest.png"),
]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=2)
    for img, out in JOBS:
        f = OUT/f'priceit_{img.replace(".png","")}.html'
        f.write_text(TPL.format(img=img))
        pg.goto('file://'+str(f))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.wait_for_timeout(400)
        tmp = str(OUT/(out+'.2x.png'))
        pg.screenshot(path=tmp)
        Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/out)
        pathlib.Path(tmp).unlink()
        print('card', out)
    b.close()

# story9 pads (edge-smear 1080x1350 card onto 1080x1920)
for _, out in JOBS:
    card = Image.open(OUT/out)
    pad = Image.new('RGB', (1080, 1920))
    PT = 285
    top = card.crop((0, 0, 1080, 1)).resize((1080, PT))
    bot = card.crop((0, 1349, 1080, 1350)).resize((1080, 1920-PT-1350))
    pad.paste(top, (0, 0)); pad.paste(card, (0, PT)); pad.paste(bot, (0, PT+1350))
    stem = out.replace('.png','')
    pad.save(S9/f'{stem}_s9.png')
    print('pad ', f'{stem}_s9.png')
