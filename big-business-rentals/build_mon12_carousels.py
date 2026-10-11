"""MONDAY OCT 12 carousels. Palettes vs Sunday (cream/emerald/velvet/blackgold/purple):
tip teal, referral emerald (green = money), countdown halloween, espanol cream (weekly light card,
family daytime). Business + venue lanes are the two real-footage reels today, no carousels."""
import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week6'
OUT.mkdir(parents=True, exist_ok=True)
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

import shutil
if not (OUT/'fonts').exists(): shutil.copytree(BASE/'assets/fonts', OUT/'fonts')
shutil.copy(BASE/'assets/bb_logo.png', OUT/'bb_logo.png')

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'teal': dict(bg="radial-gradient(circle at 44% 20%, #10403e 0%, #0b2f2e 50%, #061d1c 100%)",
   ink="#f3eddc", body="#d8dcc6", script="#8fd0c4", gold1="#EFCB7C", gold2="#c07a3e",
   frame="#c07a3e", soft="#a8c4ba", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(214,138,74,.22)", barbg="rgba(214,138,74,.28)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
 'halloween': dict(bg="radial-gradient(circle at 50% 36%, #241040 0%, #140823 50%, #060309 100%)",
   ink="#f6ecc9", body="#d9c9ef", script="#c9a9f0", gold1="#ffb13d", gold2="#ff8c2e",
   frame="#B08D3E", soft="#b9a8d4", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(255,140,46,.22)", barbg="rgba(255,140,46,.3)"),
 'cream': dict(bg="radial-gradient(circle at 30% 18%, #faf3e3 0%, #f4ead6 45%, #e7d9bc 100%)",
   ink="#241a35", body="#4a3c28", script="#9a6f20", gold1="#c89a3c", gold2="#8a6a1c",
   frame="#a07c2c", soft="#5c4b2e", grainmode="multiply", vig="rgba(120,95,40,.16)",
   ghost="rgba(160,124,44,.25)", barbg="rgba(160,124,44,.25)"),
}

def frame_bits():
    return """<div class="grain"></div><div class="vig"></div><div class="frame"></div>
<div class="dia" style="left:29px;top:29px"></div><div class="dia" style="right:29px;top:29px"></div>
<div class="dia" style="left:29px;bottom:29px"></div><div class="dia" style="right:29px;bottom:29px"></div>"""

def foot_small():
    return """<div class="footS"><img src="bb_logo.png">
<div class="t"><b>702-706-8287</b> · bigbusinesspartyrentals.com<br>@bigbusiness_rentals_events · LAS VEGAS, NV</div></div>"""

def prog(i, n):
    pct = int(i/n*100)
    return f'<div class="prog">{i}/{n}</div><div class="bar"><i style="width:{pct}%"></i></div>'

def slide(inner, pal, i, n, hook=False, ghost=None, single=False, swipetext='SWIPE&nbsp;&nbsp;→'):
    g = f'<div class="ghostn">{ghost}</div>' if ghost else ''
    kick = '<div class="kick">◆&nbsp; BIG BUSINESS · LAS VEGAS &nbsp;◆</div>'
    p = '' if (hook or single) else prog(i, n)
    sw = f'<div class="swipe">{swipetext}</div>' if hook else ''
    return f'<div class="slide" style="{pal}">{g}{frame_bits()}{kick}{p}{inner}{sw}{foot_small()}</div>'

def palstyle(p):
    return (f"--bg:{p['bg']};--ink:{p['ink']};--body:{p['body']};--script:{p['script']};"
            f"--gold1:{p['gold1']};--gold2:{p['gold2']};--frame:{p['frame']};--soft:{p['soft']};"
            f"--grainmode:{p['grainmode']};--vig:{p['vig']};--ghost:{p['ghost']};--barbg:{p['barbg']}")

def cta_block(fine=None):
    f = f'<div class="fine">{fine}</div>' if fine else ''
    return ('<div class="ctaBlock"><img src="bb_logo.png"><div class="ph">702-706-8287</div>'
            '<div class="site">bigbusinesspartyrentals.com</div>'
            '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div>'+f)

CAROUSELS = {}

# 1) TIP No.29 · LINEN MATH · Desert Teal · 6 slides
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Mon_LinenMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.29</div>'
       '<div class="h1" style="font-size:94px">WHY DO TABLECLOTHS NEVER <em>FIT?</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">You bought a cloth.<br><em>It floats at half-mast.</em></div>'
       '<div class="sup">Linens have math. Two numbers fix every table.</div></div>', p, 2, 6, ghost='29'),
 slide('<div class="mid"><div class="giant" style="font-size:200px">90x132</div>'
       '<div class="sup"><b>the linen that takes an 8 foot banquet table</b> all the way to the floor.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:230px">120"</div>'
       '<div class="sup"><b>one 120 inch round cloth</b> drops a 60 inch round table floor length, no ankles showing.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">RENTED LINENS<br><em>COME SIZED.</em></div>'
       '<div class="sup">Tell us the table, <b>we bring the cloth that fits.</b> Pressed, dropped and picked back up.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS STILL USING <em>BED SHEETS.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) REFERRAL · CONTACTS LIST · Emerald · 5 slides
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Mon_Contacts'] = [
 slide('<div class="mid"><div class="script">Open your phone</div>'
       '<div class="h1">YOUR CONTACTS LIST IS WORTH <em>MONEY.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody saved in<br>your phone is planning<br><em>a party right now.</em></div>'
       '<div class="sup">A birthday. A baby shower. A December dinner. You know exactly who.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book rentals or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">SCROLL.<br>SEND.<br><em>GET PAID.</em></div>'
       '<div class="sup">No limit on referrals. <b>Paid after their event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE ONE WHO IS <em>ALWAYS PLANNING SOMETHING.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 3) COUNTDOWN · 19 NIGHTS · Halloween · 4 slides
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Mon_19Nights'] = [
 slide('<div class="mid"><div class="script">Check the calendar</div>'
       '<div class="h1">19 NIGHTS. THE COSTUME IS NOT <em>THE HARD PART.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The costume takes<br>an hour.<br><em>The room takes a call.</em></div>'
       '<div class="sup">If you make that call before the rush does.</div></div>', p, 2, 4, ghost='19'),
 slide('<div class="mid"><div class="giant">19</div>'
       '<div class="sup"><b>nights out, and the good Saturdays are already going:</b> tables, chairs and the party room book first.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# 4) EN ESPANOL · LA POSADA · Daylight Cream · 5 slides
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Mon_Posada'] = [
 slide('<div class="mid"><div class="script">Diciembre viene rápido</div>'
       '<div class="h1">¿LA POSADA ES EN <em>TU CASA</em> ESTE AÑO?</div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Diciembre se llena<br><em>primero.</em></div>'
       '<div class="sup">Las fechas buenas se apartan desde octubre, no desde diciembre.</div></div>', p, 2, 5, ghost='12'),
 slide('<div class="mid"><div class="h2">MESAS, SILLAS<br>Y MANTELES<br><em>LISTOS.</em></div>'
       '<div class="sup">Entregados, instalados y recogidos por nosotros, en todo Las Vegas. <b>Tú pones los tamales.</b></div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿MUCHA GENTE?<br><em>TENEMOS SALÓN.</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:54px">ESCRÍBENOS AL CHAT DE<br><em style="font-size:44px">BIGBUSINESSPARTYRENTALS.COM</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':1080,'height':1400}, device_scale_factor=2)
    for name, slides in CAROUSELS.items():
        html = ("<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"
                + "\n".join(slides) + "</body></html>")
        f = OUT/f'{name}.html'
        f.write_text(html)
        pg.goto('file://'+str(f))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.wait_for_timeout(300)
        els = pg.locator('.slide')
        n = els.count()
        for i in range(n):
            stem = f'{name}_{i+1:02d}'
            tmp = str(OUT/f'{stem}.2x.png')
            els.nth(i).screenshot(path=tmp)
            Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/f'{stem}.png')
            pathlib.Path(tmp).unlink()
        print('done', name, n, 'slides')
    b.close()
