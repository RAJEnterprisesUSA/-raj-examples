"""Friday Nov 20 EP. 54 The Setup Clock (reelsD REELS[54], 26s, cast by story; Season Two record 9 W · 5 L).
Dad promises the Dec 19 room (10 tables, 60 chairs) in 20 minutes; Mrs. Never Wrong starts a giant stopwatch with a live mm:ss readout and a
10-cell floor plan strip that fills as the crew sets tables. A red chair (Lil Wobbles) joins the row and Baby punts it out (PUNT. freeze frame).
Tyler gag, Vaeh sighs, then Vaeh quietly sets the last table without looking up; the clock stops at 17:52, Dad says I DID THAT, the cat takes the best seat.
UPGRADE: giant stopwatch HUD with a sweeping hand and live clock, new cause for the Wobbles exit (punt, not fold). SFX only.
Usage: python3 build_fri20_episode.py qa   (contact sheet + numeric checks)  |  python3 build_fri20_episode.py   (full render)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE, CHROME, SCRATCH
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep54_TheSetupClock.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.6)
    for i in range(10): add(kit('pop' if i % 2 == 0 else 'pop2'), 0.6+i*0.1, 0.25)   # floor plan cells appear
    add(kit('whoosh'), 2.8, 0.5); add(tone(2200, 0.18, 0.12), 3.2)                    # stopwatch start click
    for i in range(int((17.0-3.4)/0.5)): add(tone(1300 if i % 2 == 0 else 1000, 0.025, 0.07), 3.4+i*0.5)   # clock ticking
    for i in range(9):
        a = 3.4+i*1.4
        if not (6.6 <= a < 7.3): add(kit('pop2' if i % 2 else 'pop'), a, 0.4)           # tables set
    add(tone(1500, 0.16, 0.10, 'square', bend=-0.5), 5.0)                                # Lil Wobbles squeak
    add(kit('whoosh'), 6.0, 0.6); add(kit('kick'), 6.5, 0.9); add(kit('freeze'), 6.6); add(kit('rimshot'), 7.3, 0.4)
    add(kit('whoosh'), 7.4, 0.8)                                                         # punted out of the room
    add(kit('pop2'), 7.6, 0.9); add(kit('pop'), 8.8, 0.6)
    add(kit('pop'), 13.0, 0.5)
    for i in range(6): add(tone(1400, 0.02, 0.08), 15.0+i*0.33)                          # panic ticks
    add(kit('sneak'), 17.3, 0.5)
    add(tone(2400, 0.4, 0.14), 17.0); add(kit('win'), 17.0, 0.7); add(kit('applause'), 17.0, 0.6)
    add(tone(1500, 0.16, 0.10, 'square', bend=-0.5), 19.2)                               # Wobbles is back
    add(kit('theme'), 22.5, 0.6)
def qa():
    from playwright.sync_api import sync_playwright
    d = SCRATCH/'qa54'; d.mkdir(parents=True, exist_ok=True)
    times = [0.8, 2.2, 3.6, 5.8, 6.9, 7.8, 9.2, 11.5, 14.0, 16.2, 17.6, 18.6, 20.5, 22.6]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.goto('file://'+str(BASE/'reelsD.html')); pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(600); pg.evaluate("setReel(54)"); pg.evaluate("drawFrame(0)")
        for t in times:
            pg.evaluate(f"drawFrame({t})"); pg.locator('canvas').screenshot(path=str(d/f'f_{t:05.1f}.png'))
        b.close()
    print('console errors:', errs)
    from PIL import Image
    fs = sorted(d.glob('f_*.png')); w, h = 270, 480
    sheet = Image.new('RGB', (w*7, h*2))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((w, h)), ((i % 7)*w, (i//7)*h))
    out = BASE/'daily-posts/qa_ep54_contact.png'; sheet.save(out); print('sheet', out)
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'qa': qa()
    else: render_reel('reelsD.html', 54, 26.0, 25.2, OUT, cues)
