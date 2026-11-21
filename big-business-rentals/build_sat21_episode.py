"""Saturday Nov 21 EP. 55 The Load List (reelsD REELS[55], 26s, cast by story; Season Two record 9 W · 6 L).
Dec 19 truck load-out: 10 tables and their chairs fly onto a cutaway box truck while a HUD tallies TABLES, CHAIRS and EXTRA CHAIR.
The extra chair goes missing, Mrs. Never Wrong looks at Unc, who was sitting on it ("I WAS TESTING IT."); Dad saves face, the cat takes the
extra chair, Princess calls it her throne. Tyler gag, Vaeh sigh, Lil copies Dad. SFX only.
UPGRADE: cutaway box truck set with live tally HUD and a flying-in load animation, Unc leaning back on a chair as the plot device.
Usage: python3 build_sat21_episode.py qa   |   python3 build_sat21_episode.py   (full render)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE, CHROME, SCRATCH
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep55_TheLoadList.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(kit('whoosh'), 0.2, 0.6)                                                       # truck rolls in
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    for i in range(3): add(kit('pop' if i % 2 == 0 else 'pop2'), 0.4+i*0.15, 0.3)     # HUD pills
    add(tone(2200, 0.18, 0.12), 3.2)
    for i in range(10):
        a = 3.4+i*0.9
        add(kit('whoosh'), a, 0.35); add(kit('pop2' if i % 2 else 'pop'), a+0.33, 0.45)   # table flies in and lands
    add(kit('pop'), 5.6, 0.7)                                                          # Unc's chair appears
    add(kit('pop2'), 7.6, 0.9); add(kit('pop'), 8.8, 0.6)                              # Tyler gag
    add(kit('win'), 12.4, 0.5)                                                         # all loaded
    for i in range(5): add(tone(1500 if i % 2 == 0 else 1100, 0.14, 0.12, 'square'), 13.0+i*0.4)   # missing-chair alarm
    add(kit('whoosh'), 14.9, 0.6); add(kit('freeze'), 15.0); add(kit('kick'), 15.05, 0.9); add(kit('rimshot'), 15.7, 0.5)
    add(kit('pop2'), 17.1, 0.7)
    add(kit('whoosh'), 17.5, 0.8)                                                      # extra chair flies to the truck
    add(tone(2400, 0.4, 0.14), 17.9); add(kit('win'), 17.9, 0.7); add(kit('applause'), 17.9, 0.6)
    add(kit('sneak'), 18.1, 0.5)                                                       # cat trots in
    add(kit('pop'), 21.1, 0.6)
    add(kit('theme'), 22.5, 0.6)
def qa():
    from playwright.sync_api import sync_playwright
    d = SCRATCH/'qa55'; d.mkdir(parents=True, exist_ok=True)
    times = [0.5, 1.6, 3.6, 5.0, 6.2, 8.2, 9.4, 11.5, 12.8, 13.8, 15.3, 16.5, 17.7, 18.6, 20.0, 21.8, 22.6, 23.8]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.on('requestfailed', lambda r: errs.append('FAILED '+r.url))
        pg.goto('file://'+str(BASE/'reelsD.html')); pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(600); pg.evaluate("setReel(55)"); pg.evaluate("drawFrame(0)")
        for t in times:
            pg.evaluate(f"drawFrame({t})"); pg.locator('canvas').screenshot(path=str(d/f'f_{t:05.1f}.png'))
        # text widths (canvas px of 1080)
        w = pg.evaluate("""()=>{const c=document.createElement('canvas').getContext('2d'); const out={};
          const L=[['DAD HAS THE LIST.',46],['HAS THE CHECKLIST.',48],['IS ALWAYS ON THE TRUCK.',42],['CHAIRS DO YOU PLAN?',52],['ONE CHAIR MISSING.',46],['60 CHAIRS LOADED.',46],['BIG BUSINESS PARTY RENTALS',30],['SEASON TWO RECORD: 9 W · 6 L',30],['ON TRUCK',44],['EXTRA CHAIR',26]];
          for(const [s,z] of L){ c.font=(s==='EXTRA CHAIR'?'600 ':'')+z+'px "Archivo Black"'; out[s]=Math.round(c.measureText(s).width);} return out;}""")
        print('widths', w)
        b.close()
    print('console errors:', errs)
    from PIL import Image
    fs = sorted(d.glob('f_*.png')); w_, h_ = 240, 427
    sheet = Image.new('RGB', (w_*9, h_*2))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((w_, h_)), ((i % 9)*w_, (i//9)*h_))
    out = BASE/'daily-posts/qa_ep55_contact.png'; sheet.save(out); print('sheet', out)
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'qa': qa()
    else: render_reel('reelsD.html', 55, 26.0, 25.2, OUT, cues)
