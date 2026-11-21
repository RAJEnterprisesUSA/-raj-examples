"""QA for Sat Nov 21 remix (reelH REELS[59]): console errors, frames at key times, contact sheet, caption/cloud width measurement."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import CHROME, BASE, SCRATCH
from playwright.sync_api import sync_playwright
from PIL import Image
TIMES = [1.5, 4.5, 7.5, 10.5, 12.9, 13.8, 14.6, 15.2, 16.0, 17.6, 19.5, 21.0, 22.8, 24.5]
out = SCRATCH/'qa59'; out.mkdir(parents=True, exist_ok=True)
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
    pg.evaluate("setReel(59)"); pg.evaluate("drawFrame(0)")
    # text widths of the captions / clouds (canvas px, frame is 1080 wide)
    w = pg.evaluate("""()=>{const r={}; const m=(f,s)=>{ctx.font=f; return Math.round(ctx.measureText(s).width)};
      r.cap1=Math.max(m('46px "Archivo Black"','EVERYONE IS PITCHING THE'),m('46px "Archivo Black"','BOSS FOR A DAY OFF.'));
      r.cap2=Math.max(m('54px "Archivo Black"','THE BOSS ADDED'),m('54px "Archivo Black"','A MISSION.'));
      r.cap3=Math.max(m('54px "Archivo Black"','THE CREW SET UP'),m('54px "Archivo Black"','THE WHOLE PARTY.'));
      r.cap4=Math.max(m('46px "Archivo Black"','SETUP FIRST.'),m('46px "Archivo Black"','THEN THE CONTROLLERS.'));
      r.cap5=Math.max(m('42px "Archivo Black"','YOUR PARTY IS THE MISSION.'),m('42px "Archivo Black"','WE DO SETUP AND TEARDOWN.'));
      r.cloudUnc=Math.max(m('40px "Archivo Black"','BOSS. THE DAY OFF'),m('40px "Archivo Black"','FOR THE BIG GAME?'))+70;
      r.cloudDad=Math.max(m('44px "Archivo Black"','DEAL. BUT'),m('44px "Archivo Black"','SETUP FIRST.'))+70;
      r.tag=0; return r;}""")
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
dst = BASE/'daily-posts/qa_sat21_remix_contact.png'; sheet.save(dst); print('sheet', dst)
