"""Sunset-poster flyer (owner request in CRM chat, GTA 6 style homage): 1080x1350.
Hot pink / orange / purple sunset sky, palms, skyline, three lit event tents with round tables and gold chairs,
a 4-panel cast collage along the bottom, own lettering only. No game name, no studio name, no marks.
Hand-built vector scene (not AI imagery) so no AI chip is needed. No prices, no counts.
Output: flyers2026/BB26_SunsetSetup_Flyer.png (1080) and _2160.png. Phone 702-706-8287."""
import glob, math, pathlib, shutil, json
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path(__file__).parent
OUT = BASE/'flyers2026'
CHROME = (glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') + glob.glob('/opt/pw-browsers/chromium-*/chrome-linux64/chrome')
          + glob.glob(str(pathlib.Path.home()/'.cache/ms-playwright/chromium-*/chrome-linux*/chrome'))
          + glob.glob(str(pathlib.Path.home()/'.cache/ms-playwright/chromium_headless_shell-*/chrome-linux*/headless_shell')))[0]
FONTS = OUT/'sunset_fonts'
if not FONTS.exists(): shutil.copytree(BASE/'assets/fonts', FONTS)
for n in ['sp_mbb','sp_mnw','sp_unc','sp_tyler']:
    shutil.copy(BASE/'examples'/(n+'.png'), OUT/(n+'.png'))
shutil.copy(BASE/'brand/BB_Logo_Purple_512.png', OUT/'sunset_logo.png')

# ---------- scene pieces ----------
def chair(x, flip=False):
    s = -1 if flip else 1
    return f'''<g transform="translate({x},0) scale({s},1)">
<rect x="-17" y="-80" width="6" height="52" rx="2" fill="#e9b73c" stroke="#5a3a00" stroke-width="1.5"/>
<rect x="-17" y="-80" width="6" height="8" rx="2" fill="#ffd978"/>
<rect x="-11" y="-74" width="4" height="22" fill="#c8922a"/>
<rect x="-18" y="-35" width="38" height="7" rx="2" fill="#f4c855" stroke="#5a3a00" stroke-width="1.5"/>
<rect x="-14" y="-28" width="4" height="28" fill="#c8922a"/><rect x="13" y="-28" width="4" height="28" fill="#c8922a"/>
</g>'''

def table(x, cloth, trim):
    return f'''<g transform="translate({x},0)">
<ellipse cx="0" cy="1" rx="78" ry="12" fill="rgba(0,0,0,.35)"/>
<path d="M-60,-66 L-80,-2 Q0,14 80,-2 L60,-66 Z" fill="{cloth}"/>
<path d="M-60,-66 L-80,-2 Q-40,6 -20,8 L-14,-66 Z" fill="rgba(0,0,0,.14)"/>
<path d="M-80,-2 Q0,14 80,-2" fill="none" stroke="{trim}" stroke-width="3"/>
<ellipse cx="0" cy="-66" rx="64" ry="13" fill="{cloth}"/>
<ellipse cx="0" cy="-67" rx="64" ry="13" fill="none" stroke="{trim}" stroke-width="2.5"/>
<rect x="-2" y="-94" width="4" height="28" fill="#2a6b4a"/>
<circle cx="0" cy="-100" r="11" fill="#ff5fa8"/><circle cx="-9" cy="-94" r="8" fill="#ffb347"/><circle cx="9" cy="-94" r="8" fill="#ff8ad0"/>
<circle cx="0" cy="-99" r="4" fill="#ffe27a"/>
</g>'''

def tent(cx, base, s, tables, uid, roof='#fff6ea'):
    """Gable-end event tent, local units: 620 wide, eaves at -210, peak at -318."""
    scal = ''.join(
        f'<path d="M{-310+i*41.33:.1f},-210 Q{-310+i*41.33+20.66:.1f},-170 {-310+(i+1)*41.33:.1f},-210 Z" fill="#fff" stroke="#ff4fa3" stroke-width="2"/>'
        for i in range(15))
    # string lights along a sagging curve
    lights = ''
    for k in range(0, 17):
        t = k/16; x = -300 + 600*t; y = -176 + 38*math.sin(math.pi*t)
        c = ['#ffe27a', '#ff9ad0', '#ffb347'][k % 3]
        lights += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{c}" filter="url(#glow{uid})"/>'
    inner = ''
    for kind, x in tables:
        if kind == 'T': inner += table(x, '#ff4fa3' if x < 0 else '#7a3cff', '#ffd978')
    for kind, x in tables:
        if kind == 'C': inner += chair(x, False)
        if kind == 'c': inner += chair(x, True)
    return f'''<g transform="translate({cx},{base}) scale({s})">
<defs>
<filter id="glow{uid}" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="in{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a0c55"/><stop offset=".55" stop-color="#8a2a8f"/><stop offset="1" stop-color="#ff9a4a"/></linearGradient>
<linearGradient id="fl{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb06a"/><stop offset="1" stop-color="#7a2a6a"/></linearGradient>
</defs>
<ellipse cx="0" cy="6" rx="360" ry="22" fill="rgba(20,4,40,.55)"/>
<rect x="-310" y="-210" width="620" height="210" fill="url(#in{uid})"/>
<rect x="-310" y="-14" width="620" height="14" fill="url(#fl{uid})"/>
<g>{inner}</g>
<rect x="-316" y="-210" width="10" height="212" fill="#f6ecdc"/><rect x="306" y="-210" width="10" height="212" fill="#f6ecdc"/>
<rect x="-316" y="-210" width="4" height="212" fill="rgba(0,0,0,.12)"/><rect x="306" y="-210" width="4" height="212" fill="rgba(0,0,0,.12)"/>
<polygon points="-336,-210 0,-326 336,-210" fill="{roof}"/>
<polygon points="-336,-210 0,-326 0,-210" fill="rgba(255,120,190,.30)"/>
<polygon points="0,-326 336,-210 0,-210" fill="rgba(255,255,255,.35)"/>
<polygon points="-336,-210 0,-326 336,-210" fill="none" stroke="#ff4fa3" stroke-width="6" stroke-linejoin="round" filter="url(#glow{uid})"/>
<g>{scal}</g>
<g>{lights}</g>
<path d="M-300,-176 Q0,-100 300,-176" fill="none" stroke="rgba(255,226,122,.45)" stroke-width="1.5" transform="translate(0,0)"/>
</g>'''

def palm(x, base, h, lean, scale=1.0, col='#12032b'):
    topx, topy = x+lean, base-h
    trunk = f'<path d="M{x-9*scale},{base} Q{x+lean*0.2},{base-h*0.55} {topx-4},{topy} L{topx+4},{topy} Q{x+lean*0.2+16},{base-h*0.55} {x+9*scale},{base} Z" fill="{col}"/>'
    fr = ''
    for ang, ln in [(-170, 150), (-145, 175), (-118, 160), (-90, 120), (-62, 160), (-35, 175), (-10, 150), (20, 120), (160, 120), (95, 70), (80, 70)]:
        a = math.radians(ang); L = ln*scale
        ex, ey = topx+L*math.cos(a), topy+L*math.sin(a)+L*0.38
        mx, my = topx+L*0.55*math.cos(a), topy+L*0.55*math.sin(a)-L*0.22
        nx, ny = -math.sin(a)*14*scale, math.cos(a)*14*scale
        fr += f'<path d="M{topx},{topy} Q{mx+nx:.1f},{my+ny:.1f} {ex:.1f},{ey:.1f} Q{mx-nx:.1f},{my-ny-8:.1f} {topx},{topy} Z" fill="{col}"/>'
    return trunk+fr+f'<circle cx="{topx}" cy="{topy+4}" r="9" fill="{col}"/>'

def skyline():
    import random
    random.seed(7)
    out = ''; x = -10
    while x < 1090:
        w = random.randint(38, 84); h = random.randint(50, 170)
        out += f'<rect x="{x}" y="{470-h}" width="{w}" height="{h+40}" fill="#2a0b57"/>'
        for wy in range(470-h+10, 462, 18):
            for wx in range(x+8, x+w-10, 14):
                if random.random() < .28:
                    out += f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="{random.choice(["#ff7ac0","#ffc46b","#ff9a4a"])}" opacity=".85"/>'
        x += w + random.randint(0, 6)
    return out

def sun():
    bars = ''.join(f'<rect x="380" y="{150+i*22}" width="320" height="{3+i*1.6:.1f}" fill="black"/>' for i in range(8))
    return f'''<defs><linearGradient id="sung" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe27a"/><stop offset=".5" stop-color="#ff8a3d"/><stop offset="1" stop-color="#ff2f92"/></linearGradient>
<mask id="sunm"><rect width="1080" height="600" fill="white"/>{bars}</mask>
<radialGradient id="halo"><stop offset="0" stop-color="rgba(255,120,190,.65)"/><stop offset="1" stop-color="rgba(255,120,190,0)"/></radialGradient></defs>
<circle cx="540" cy="190" r="330" fill="url(#halo)"/>
<circle cx="540" cy="190" r="160" fill="url(#sung)" mask="url(#sunm)"/>'''

SCENE = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="600" viewBox="0 0 1080 600" style="position:absolute;left:0;top:360px">
{sun()}
{skyline()}
<rect x="0" y="470" width="1080" height="130" fill="#14042c"/>
<rect x="0" y="470" width="1080" height="3" fill="#ff4fa3"/>
{tent(120, 520, 0.50, [('T', 0), ('C', -95), ('c', 95)], 'a')}
{tent(960, 520, 0.50, [('T', 0), ('C', -95), ('c', 95)], 'b')}
{tent(540, 575, 0.90, [('T', -150), ('C', -245), ('c', -55), ('T', 150), ('C', 55), ('c', 245)], 'c')}
{palm(40, 600, 330, 45, 1.25)}
{palm(1045, 600, 360, -50, 1.3)}
{palm(150, 600, 190, 25, 0.8)}
</svg>'''

# ---------- cast collage ----------
PANELS = [
    ('sp_mbb.png', 'MR. BIG BUSINESS', 'linear-gradient(160deg,#ff4fa3,#7a1fa2)', 665),
    ('sp_mnw.png', 'MRS. NEVER WRONG', 'linear-gradient(160deg,#ffb347,#ff2f92)', 709),
    ('sp_unc.png', 'UNC', 'linear-gradient(160deg,#7a3cff,#ff4fa3)', 656),
    ('sp_tyler.png', 'TYLER THE INTERN', 'linear-gradient(160deg,#ff8a3d,#6a1fb0)', 667),
]
panels = ''
for i, (img, name, grad, h) in enumerate(PANELS):
    ih = round(380*h/665)
    panels += f'''<div class="pn" style="background:{grad}"><div class="sunb"></div>
<img src="{img}" style="height:{ih}px"><div class="nm">{name}</div></div>'''

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo Black';src:url('sunset_fonts/ArchivoBlack.ttf')}}
@font-face{{font-family:'Oswald';src:url('sunset_fonts/Oswald600.ttf');font-weight:600}}
@font-face{{font-family:'Montserrat';src:url('sunset_fonts/Mont600.ttf');font-weight:600}}
@font-face{{font-family:'Montserrat';src:url('sunset_fonts/Mont700.ttf');font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#14042c}}
body{{position:relative;font-family:'Montserrat';color:#fff;
 background:linear-gradient(180deg,#1b0647 0%,#4a0f82 18%,#a21fa0 34%,#ff3d9a 50%,#ff8a3d 64%,#ffc46b 72%,#14042c 72.1%)}}
.grain{{position:absolute;inset:0;opacity:.12;mix-blend-mode:overlay;pointer-events:none;z-index:9;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}}
.top{{position:absolute;left:44px;right:44px;top:36px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.top .brand{{font-family:'Oswald';font-weight:600;font-size:24px;letter-spacing:5px;color:#ffe9f6}}
.top .chip{{font-family:'Oswald';font-weight:600;font-size:22px;letter-spacing:4px;color:#2a0c55;background:linear-gradient(180deg,#ffe27a,#ffb347);padding:8px 20px;border-radius:6px}}
.title{{position:absolute;left:0;right:0;top:84px;text-align:center;z-index:5;transform:skewX(-6deg)}}
.title .l{{display:block;width:max-content;margin:0 auto;font-family:'Archivo Black';font-size:118px;line-height:.98;letter-spacing:1px;white-space:nowrap;
 background:linear-gradient(180deg,#ffffff 0%,#ffd3ec 38%,#ff6fb5 62%,#ffa24a 100%);-webkit-background-clip:text;background-clip:text;color:transparent;
 -webkit-text-stroke:3px #2a0c55;paint-order:stroke fill;filter:drop-shadow(0 6px 0 #2a0c55) drop-shadow(0 0 22px rgba(255,79,163,.75))}}
.sub{{position:absolute;left:0;right:0;top:322px;text-align:center;z-index:5;font-family:'Oswald';font-weight:600;font-size:26px;letter-spacing:9px;color:#fff3d0;text-shadow:0 2px 10px rgba(42,12,85,.9)}}
.panels{{position:absolute;left:36px;right:36px;top:950px;height:196px;display:flex;gap:10px;z-index:6}}
.pn{{position:relative;flex:1;border:3px solid #fff;border-radius:6px;overflow:hidden;box-shadow:0 10px 24px rgba(0,0,0,.5)}}
.pn .sunb{{position:absolute;left:50%;top:18px;width:150px;height:150px;margin-left:-75px;border-radius:50%;background:radial-gradient(circle,rgba(255,226,122,.75),rgba(255,226,122,0) 70%)}}
.pn img{{position:absolute;left:50%;transform:translateX(-50%);top:6px}}
.pn .nm{{position:absolute;left:0;right:0;bottom:0;padding:6px 4px 7px;text-align:center;font-family:'Oswald';font-weight:600;font-size:17px;letter-spacing:2px;color:#fff;background:linear-gradient(180deg,rgba(20,4,44,0),rgba(20,4,44,.92) 55%)}}
.info{{position:absolute;left:0;right:0;top:1156px;text-align:center;z-index:6}}
.info .a{{font-family:'Archivo Black';font-size:46px;letter-spacing:2px;background:linear-gradient(180deg,#fff2b8,#ffb347);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 3px 0 #2a0c55)}}
.info .b{{margin-top:4px;font-weight:700;font-size:27px;color:#fff;letter-spacing:.5px}}
.cta{{position:absolute;left:36px;right:36px;top:1262px;height:72px;z-index:6;display:flex;align-items:center;gap:18px;padding:0 22px 0 12px;border-radius:10px;
 background:linear-gradient(90deg,#ff2f92,#ff8a3d);box-shadow:0 10px 26px rgba(0,0,0,.45);border:2px solid #fff3d0}}
.cta img{{width:56px;height:56px}}
.cta .ph{{font-family:'Archivo Black';font-size:40px;color:#fff;text-shadow:0 3px 0 #2a0c55;white-space:nowrap}}
.cta .web{{margin-left:auto;font-weight:700;font-size:25px;color:#2a0c55;background:#fff3d0;padding:9px 16px;border-radius:6px;white-space:nowrap}}
</style></head><body>
<div class="top"><div class="brand">BIG BUSINESS PARTY RENTALS</div><div class="chip">LAS VEGAS · NOW BOOKING</div></div>
<div class="title"><span class="l" id="t1">YOUR PARTY.</span><span class="l" id="t2">OUR SETUP.</span></div>
<div class="sub">TENTS &nbsp;·&nbsp; TABLES &nbsp;·&nbsp; CHAIRS</div>
{SCENE}
<div class="panels">{panels}</div>
<div class="info"><div class="a" id="ia">THE WHOLE CREW SHOWS UP</div><div class="b" id="ib">Setup and teardown by our crew</div></div>
<div class="cta"><img src="sunset_logo.png"><div class="ph" id="cph">702-706-8287</div><div class="web" id="cweb">bigbusinesspartyrentals.com</div></div>
<div class="grain"></div>
</body></html>'''

(OUT/'BB26_SunsetSetup_Flyer.html').write_text(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto('file://'+str(OUT/'BB26_SunsetSetup_Flyer.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.wait_for_timeout(600)
    boxes = pg.evaluate("""()=>{const o={};for(const id of ['t1','t2','ia','ib','cph','cweb']){const r=document.getElementById(id).getBoundingClientRect();o[id]=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]}
      for(const sel of ['.top','.sub','.panels','.info','.cta']){const r=document.querySelector(sel).getBoundingClientRect();o[sel]=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]}
      const c=document.querySelector('.cta');o.ctaOverflow=c.scrollWidth-c.clientWidth;
      o.imgs=[...document.images].map(i=>i.naturalWidth>0);return o}""")
    print(json.dumps(boxes))
    tmp = str(OUT/'sunset.2x.png')
    pg.screenshot(path=tmp)
    im = Image.open(tmp).convert('RGB')
    im.save(OUT/'BB26_SunsetSetup_Flyer_2160.png')
    im.resize((1080, 1350), Image.LANCZOS).save(OUT/'BB26_SunsetSetup_Flyer.png')
    pathlib.Path(tmp).unlink()
    b.close()
print('done')
