"""QA for Sun Nov 22 remix (reelH REELS[60], No Assigned Seats): console errors, frames at key times, contact sheet, caption/cloud widths,
plus a coarse text map of a few frames (no image viewer in unattended runs, so check layout numerically)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import CHROME, BASE, SCRATCH
from playwright.sync_api import sync_playwright
from PIL import Image
TIMES = [1.5, 4.0, 5.5, 7.5, 10.2, 11.6, 12.8, 13.8, 14.6, 15.4, 16.8, 18.0, 20.5, 22.9]
out = SCRATCH/'qa60'; out.mkdir(parents=True, exist_ok=True)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
    pg.on('console', lambda m: errs.append(m.text) if m.type in ('error', 'warning') else None)
    pg.on('pageerror', lambda e: errs.append('PAGEERROR ' + str(e)))
    pg.on('requestfailed', lambda r: errs.append('REQFAIL ' + r.url))
    pg.on('response', lambda r: errs.append('HTTP %d %s' % (r.status, r.url)) if r.status >= 400 else None)
    pg.goto('file://' + str(BASE/'halloween/reelH.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat']){try{await document.fonts.load(f)}catch(e){}}}""")
    pg.wait_for_timeout(600)
    pg.evaluate("setReel(60)"); pg.evaluate("drawFrame(0)")
    w = pg.evaluate("""()=>{const r={}; const m=(f,s)=>{ctx.font=f; return Math.round(ctx.measureText(s).width)};
      const A='px "Archivo Black"';
      r.cap1=Math.max(m('50'+A,'THE NEW HOSTING RULE:'),m('50'+A,'NO ASSIGNED SEATS.'));
      r.cap2=Math.max(m('54'+A,'EVERYONE PICKS'),m('54'+A,'THEIR OWN SEAT.'));
      r.cap3=Math.max(m('54'+A,'LIL AND BABY'),m('54'+A,'SIT TOGETHER.'));
      r.cap4=Math.max(m('46'+A,'UNC LEANS BACK.'),m('46'+A,'VAEH DOES NOT LOOK UP.'));
      r.cap5=Math.max(m('50'+A,'EVERYONE FOUND A SEAT.'),m('50'+A,'ALMOST.'));
      r.cap6=Math.max(m('46'+A,'YOU PICK THE SEATS.'),m('46'+A,'WE BRING THE CHAIRS.'));
      r.cloudDad1=Math.max(m('44'+A,'NO SEAT CARDS.'),m('44'+A,'SIT ANYWHERE.'))+70;
      r.cloudDad2=Math.max(m('44'+A,"I'LL TAKE THE"),m('44'+A,'LAST CHAIR.'))+70;
      r.cloudVaeh=Math.max(m('44'+A,'...this is SO'),m('44'+A,'embarrassing.'))+70;
      r.tip1=m('46'+A,'EVERY GUEST PICKS A CHAIR.'); r.tipFit=640; return r;}""")
    print('widths', w)
    for t in TIMES:
        pg.evaluate("drawFrame(%s)" % t)
        pg.locator('canvas').screenshot(path=str(out/('f_%05.2f.png' % t)))
    b.close()
print('errors:', errs if errs else 'none')
ims = [Image.open(out/('f_%05.2f.png' % t)).resize((270, 480)) for t in TIMES]
cols = 7; rows = (len(ims) + cols - 1)//cols
sheet = Image.new('RGB', (cols*270, rows*480), 'black')
for i, im in enumerate(ims): sheet.paste(im, ((i % cols)*270, (i//cols)*480))
dst = BASE/'daily-posts/qa_sun22_remix_contact.png'; sheet.save(dst); print('sheet', dst)
# coarse text map of the lower half (y 600..1500 of 1920), classes: # ink, s skin, w white chair/table, . background
def tmap(t):
    im = Image.open(out/('f_%05.2f.png' % t)).convert('RGB')
    W, H = im.size; rows = []
    for y in range(int(H*0.42), int(H*0.82), 8):
        row = ''
        for x in range(0, W, 5):
            r, g, bl = im.getpixel((x, y))
            if r < 60 and g < 50 and bl < 60: c = '#'
            elif r > 225 and g > 225 and bl > 215: c = 'w'
            elif abs(r-0xb9) < 28 and abs(g-0x84) < 28 and abs(bl-0x5a) < 28: c = 's'
            elif r > 200 and g < 120: c = 'p'
            elif r > 200 and g > 170 and bl < 120: c = 'g'
            else: c = '.'
            row += c
        rows.append(row)
    return '\n'.join(rows)
for t in (4.0, 11.6, 14.6, 18.0):
    print('--- t=%.1f' % t); print(tmap(t))
