"""Thursday Nov 19 EP. 53 The Walkthrough (reelsD REELS[53], 26s, cast by story; Season Two record 8 W · 5 L).
Dad walks the Dec 19 room with a tape measure and marks 10 table spots in seconds (live FT tag on the tape, numbered dashed
floor plan that fills with real tables and chairs at the payoff). Mrs. Never Wrong: "DON'T LET GO." Unc lets go, the tape whips
back and folds Lil Wobbles. Tyler gag, Lil and Baby carry a chair each, Vaeh sighs, the cat claims table 7.
UPGRADE: floor-plan marks on the stage floor + a live tape reading, no Christmas imagery (owner Nov 8). SFX only.
Usage: python3 build_thu19_episode.py qa   (8-frame contact sheet)  |  python3 build_thu19_episode.py   (full render)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import render_reel, kit, bed, tone, noise, BASE, CHROME, SCRATCH
OUT = BASE.parent/'fb_safe/BB_Chronicles_Ep53_TheWalkthrough.mp4'
def cues(add):
    add(kit('theme'), 0.0)
    add(bed(21.5, 104, 'groove'), 0.5, 0.36)
    add(kit('whoosh'), 0.3, 0.6)
    for i in range(14): add(tone(900+i*30, 0.03, 0.08), 0.35+i*0.075)      # tape ticking out
    for i in range(10): add(kit('pop' if i % 2 == 0 else 'pop2'), 1.4+i*0.12, 0.35)   # ten spots marked
    add(kit('pop2'), 2.9, 0.5)
    add(tone(1500, 0.16, 0.10, 'square', bend=-0.5), 5.0)                    # Lil Wobbles squeak
    add(kit('whoosh'), 6.3, 0.7); add(kit('kick'), 6.5, 0.8); add(kit('freeze'), 6.6); add(kit('rimshot'), 7.3, 0.4)
    add(kit('pop2'), 7.6, 0.9); add(kit('pop'), 8.8, 0.6)
    add(kit('pop'), 10.0, 0.5); add(kit('pop'), 10.6, 0.5)
    add(kit('sneak'), 15.0, 0.5)
    add(kit('win'), 19.6, 0.7); add(kit('applause'), 19.6, 0.6)
    add(kit('theme'), 22.5, 0.6)
def qa():
    from playwright.sync_api import sync_playwright
    d = SCRATCH/'qa53'; d.mkdir(parents=True, exist_ok=True)
    times = [0.8, 2.2, 4.0, 5.8, 6.9, 9.2, 11.5, 14.0, 17.0, 20.5, 22.6, 24.5]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
        pg.goto('file://'+str(BASE/'reelsD.html')); pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(600); pg.evaluate("setReel(53)"); pg.evaluate("drawFrame(0)")
        for t in times:
            pg.evaluate(f"drawFrame({t})"); pg.locator('canvas').screenshot(path=str(d/f'f_{t:05.1f}.png'))
        b.close()
    from PIL import Image
    fs = sorted(d.glob('f_*.png')); w, h = 270, 480
    sheet = Image.new('RGB', (w*6, h*2))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((w, h)), ((i % 6)*w, (i//6)*h))
    out = BASE/'daily-posts/qa_ep53_contact.png'; sheet.save(out); print('sheet', out)
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'qa': qa()
    else: render_reel('reelsD.html', 53, 26.0, 25.2, OUT, cues)
