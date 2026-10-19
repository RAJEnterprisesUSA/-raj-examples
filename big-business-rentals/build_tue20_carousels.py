"""TUESDAY OCT 20 cards. Merged morning card = business-angle day. Palettes vs Monday
(morning blackgold / venue velvet / referral purple / espanol cream / countdown halloween):
morning emerald, venue navy single, referral velvet, espanol blackgold, countdown purple."""
import glob, pathlib, shutil
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week8'
OUT.mkdir(parents=True, exist_ok=True)
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
if not (OUT/'fonts').exists(): shutil.copytree(BASE/'assets/fonts', OUT/'fonts')
shutil.copy(BASE/'assets/bb_logo.png', OUT/'bb_logo.png')

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]
t13 = (BASE/'build_tue13_carousels.py').read_text()
m12 = (BASE/'build_mon12_carousels.py').read_text()
ns = {}
exec(t13.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns)
PAL = ns['PAL']
ns2 = {}
exec(m12.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns2)
for k in ('teal', 'halloween', 'cream'): PAL[k] = ns2['PAL'][k]

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

FINE = ('Reward based on booking size, up to $100 · No limit on referrals · '
        'Paid after the referred event is completed')

CAROUSELS = {}

# 1) MORNING CARD (business-angle day) · WE CARRY IT · Emerald · 6
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Tue20_WeCarryIt'] = [
 slide('<div class="mid"><div class="script">The part nobody posts</div>'
       '<div class="h1">YOU PLAN THE PARTY. <em>WE CARRY IT.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Every rental includes<br>the invisible<br><em>half.</em></div>'
       '<div class="sup">The truck. The setup. The teardown. The part that ruins backs and Saturdays.</div></div>', p, 2, 6, ghost='3'),
 slide('<div class="mid"><div class="h2">1.<br><em>DELIVERED.</em></div>'
       '<div class="sup"><b>Tables, chairs, linens and chair covers,</b> dropped at your door anywhere in Las Vegas.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="h2">2.<br><em>BUILT.</em></div>'
       '<div class="sup"><b>We set every table and chair before we leave.</b> You point, we place.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">3. GONE BY<br><em>MONDAY.</em></div>'
       '<div class="sup"><b>Pickup is part of the job.</b> Your garage never meets a folding chair.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) VENUE · CORPORATE NOVEMBER · Midnight Navy · single card
p = palstyle(PAL['navy'])
CAROUSELS['BB_Venue_Tue20_Corporate'] = [slide(
 '<div class="mid"><div class="script">Corporate season is coming</div>'
 '<div class="h1" style="font-size:96px">BOOK THE COMPANY PARTY BEFORE <em>NOVEMBER DOES.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>Big race weekends and holiday dinners stack November and December fast.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 3) REFERRAL · THE DJ · Velvet Rope · 5
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Tue20_TheDJ'] = [
 slide('<div class="mid"><div class="script">Check the booth</div>'
       '<div class="h1">THE DJ KNOWS WHERE EVERY PARTY <em>IS.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Booked every weekend.<br>Talking to<br><em>every host.</em></div>'
       '<div class="sup">That contact list is a second paycheck waiting to happen.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">PLAY THE SONG.<br><em>DROP OUR NAME.</em></div>'
       '<div class="sup">They book, you collect <b>after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE <em>DJ.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 4) EN ESPANOL #9 · LA CORTE · Black&Gold · 5
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Tue20_LaCorte'] = [
 slide('<div class="mid"><div class="script">Para la quince</div>'
       '<div class="h1">LA CORTE SON 14. <em>¿Y LAS SILLAS?</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Damas, chambelanes,<br>la quinceañera y<br><em>toda la familia.</em></div>'
       '<div class="sup">Las sillas se acaban antes que los tamales. Siempre.</div></div>', p, 2, 5, ghost='XV'),
 slide('<div class="mid"><div class="h2">MESAS Y SILLAS<br><em>PARA TODOS.</em></div>'
       '<div class="sup"><b>Entregadas, instaladas y recogidas</b> en todo Las Vegas, del vals a la cena.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿LA FIESTA ES<br><em>GRANDE?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A UNA FAMILIA CON QUINCE <em>EN CAMINO.</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 11 NIGHTS · Purple/Gold · 4
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Tue20_11Nights'] = [
 slide('<div class="mid"><div class="script">Halloween countdown</div>'
       '<div class="h1">11 NIGHTS. WHERE IS THE COSTUME <em>GOING?</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">A costume with no party<br>is just<br><em>an outfit.</em></div>'
       '<div class="sup">Somebody has to host. It might as well be you.</div></div>', p, 2, 4, ghost='11'),
 slide('<div class="mid"><div class="giant">11</div>'
       '<div class="sup"><b>nights out.</b> Tables, chairs and the room book faster every day now. Halloween is a Saturday.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
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
            stem = f'{name}_{i+1:02d}' if n > 1 else name
            tmp = str(OUT/f'{stem}.2x.png')
            els.nth(i).screenshot(path=tmp)
            Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/f'{stem}.png')
            pathlib.Path(tmp).unlink()
        print('done', name, n, 'slides')
    b.close()
