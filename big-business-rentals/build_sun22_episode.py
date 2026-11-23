"""Sunday Nov 22 EP. 56 The Headcount (reelsD REELS[56], 26s, cast by story; Season Two record 10 W · 6 L).
Dec 19 guest list: RSVP bubbles fly from Vaeh's phone to a GUEST LIST board, a floor-plan strip adds one table icon per six guests.
Mrs. Never Wrong throws a sticky note that says 73 before the count starts, Lil and Baby add friends, the group chat bursts, the last RSVP is the cat.
Count lands on exactly 73. SFX only.
UPGRADE: live GUEST LIST board with a flipping counter and a self-building top-down floor-plan strip, flying RSVP chat bubbles with a cat-face avatar bubble.
Usage: python3 build_sun22_episode.py qa   |   python3 build_sun22_episode.py   (full render)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE, CHROME, SCRATCH
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep56_TheHeadcount.mp4'
BUBS = [4.8, 5.5, 6.2, 9.9, 10.7, 12.0, 12.4, 12.8, 13.9]
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 100, 'groove'), 0.5, 0.34)
    add(kit('pop'), 0.3, 0.4)                                                          # board pops in
    for i in range(6): add(kit('pop2' if i % 2 else 'pop'), 0.3+i*0.15, 0.25)           # first six table icons
    add(kit('whoosh'), 3.0, 0.6); add(kit('pop'), 3.65, 0.6)                           # note flies and sticks
    for i, b in enumerate(BUBS):
        add(tone(1900 if i % 2 == 0 else 2300, 0.14, 0.12), b)                         # phone ding
        add(kit('whoosh'), b+0.05, 0.25); add(kit('pop2' if i % 2 else 'pop'), b+0.55, 0.45)   # lands on the board
    add(kit('pop2'), 7.4, 0.9); add(kit('pop'), 9.2, 0.6)                              # Tyler gag
    add(kit('win'), 13.75, 0.35)                                                       # 72
    add(kit('whoosh'), 14.45, 0.6); add(kit('freeze'), 14.55); add(kit('kick'), 14.6, 0.9); add(kit('rimshot'), 15.25, 0.5)   # 73, exact
    add(kit('pop'), 16.4, 0.7)                                                         # chair
    add(kit('sneak'), 16.6, 0.5)                                                       # cat trots in
    add(tone(2400, 0.4, 0.14), 18.5); add(kit('win'), 18.5, 0.7); add(kit('applause'), 18.5, 0.6)
    add(kit('pop'), 21.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
def qa():
    from playwright.sync_api import sync_playwright
    d = SCRATCH/'qa56'; d.mkdir(parents=True, exist_ok=True)
    times = [0.5, 1.6, 3.4, 5.2, 6.8, 8.2, 9.5, 10.4, 11.3, 12.8, 14.2, 14.7, 15.4, 16.9, 17.8, 19.0, 20.5, 22.0, 22.8, 24.5]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.on('requestfailed', lambda r: errs.append('FAILED '+r.url))
        pg.goto('file://'+str(BASE/'reelsD.html')); pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(600); pg.evaluate("setReel(56)"); pg.evaluate("drawFrame(0)")
        for t in times:
            pg.evaluate(f"drawFrame({t})"); pg.locator('canvas').screenshot(path=str(d/f'f_{t:05.1f}.png'))
        w = pg.evaluate("""()=>{const c=document.createElement('canvas').getContext('2d'); const out={};
          const L=[['36 GUESTS. TABLES SET.',46,0],['MRS. NEVER WRONG',48,0],['KEEP COMING.',52,0],['LIL INVITED A FRIEND.',46,0],['BABY INVITED TWO.',46,0],['THE GROUP CHAT',52,0],
            ['CALLED 73.',50,0],['TOOK',52,0],['THE CAT TOOK',52,0],['MORE CHAIR.',40,1],['EVERY RSVP',54,0],['GOT A CHAIR.',54,0],['HOW MUCH DID YOUR',52,0],['GUEST LIST GROW?',52,0],
            ['SEASON TWO RECORD: 10 W · 6 L',30,0],['...im the new intern.',40,1],['EVEN COME FROM?',40,1],['DEC 19 GUEST LIST',34,0],['+2 FRIENDS',38,0],['73',190,0],['EXACT.',66,0]];
          for(const [s,z,cl] of L){ c.font=z+'px "Archivo Black"'; out[s]=Math.round(c.measureText(s).width)+(cl?70:0);} return out;}""")
        print('widths', w)
        b.close()
    print('console errors:', errs)
    from PIL import Image
    fs = sorted(d.glob('f_*.png')); w_, h_ = 216, 384
    sheet = Image.new('RGB', (w_*10, h_*2))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((w_, h_)), ((i % 10)*w_, (i//10)*h_))
    out = BASE/'daily-posts/qa_ep56_contact.png'; sheet.save(out); print('sheet', out)
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'qa': qa()
    else: render_reel('reelsD.html', 56, 26.0, 25.2, OUT, cues)
