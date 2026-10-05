import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')

JOBS = [
    (BASE/'daily-posts/week5/tip22.html',      BASE/'daily-posts/week5/BB_Post_Tip22_IceMath.png',      (1080,1350)),
    (BASE/'daily-posts/week5/biz_mon_w5.html', BASE/'daily-posts/week5/BB_Post_Mon_Handled.png',        (1080,1350)),
    (BASE/'daily-posts/week5/ref_mon_w5.html', BASE/'daily-posts/week5/BB_Referral_Mon_CasinoChip.png', (1080,1350)),
    (BASE/'halloween/hallow_flyer11.html',     BASE/'halloween/BB_Halloween_26Nights.png',              (1080,1080)),
]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    for src, out, (w,h) in JOBS:
        pg = b.new_page(viewport={'width':w,'height':h}, device_scale_factor=2)
        pg.goto('file://'+str(src))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.wait_for_timeout(300)
        tmp = str(out)+'.2x.png'
        pg.screenshot(path=tmp)
        pg.close()
        img = Image.open(tmp)
        img.resize((w,h), Image.LANCZOS).save(out)
        pathlib.Path(tmp).unlink()
        print('done', out.name)
    b.close()
