"""THURSDAY OCT 22 cards. Morning card = business-angle day DELIVERY DAY. Palettes vs
Wednesday (morning teal / venue purple / referral blackgold / espanol cream / countdown
halloween): morning velvet, venue emerald single, referral purple, espanol navy (POSADAS),
countdown blackgold."""
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

# 1) MORNING CARD · DELIVERY DAY (business angle) · Velvet Rope · 6
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Thu22_DeliveryDay'] = [
 slide('<div class="mid"><div class="script">Delivery day</div>'
       '<div class="h1" style="font-size:94px">YOUR PARTY SHOWS UP <em>ON A TRUCK.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">No borrowed pickups.<br>No favors.<br><em>No lifting.</em></div>'
       '<div class="sup">Here is what delivery day actually looks like.</div></div>', p, 2, 6, ghost='BB'),
 slide('<div class="mid"><div class="giant" style="font-size:200px">DROP</div>'
       '<div class="sup"><b>we pull up, unload, and go.</b> Tables and chairs delivered and picked up anywhere in Las Vegas, delivery quoted with your order.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:210px">$265</div>'
       '<div class="sup"><b>want it fully handled?</b> Full-service setup and breakdown starts here. You point, we build.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">AFTER THE PARTY,<br><em>WE HAUL IT BACK.</em></div>'
       '<div class="sup">You enjoy the night and skip the teardown. <b>You never load a single table.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:54px">QUESTIONS? THE CHAT AT <em>BIGBUSINESSPARTYRENTALS.COM</em> ANSWERS RIGHT AWAY.</div>'
       + cta_block('Drop-off pricing · delivery quoted with your order') + '</div>', p, 6, 6),
]

# 2) VENUE · COSTUME PARTY HQ · Emerald Night · single card
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Venue_Thu22_CostumeHQ'] = [slide(
 '<div class="mid"><div class="script">Nine nights out</div>'
 '<div class="h1" style="font-size:96px">HOST THE COSTUME PARTY. <em>SKIP THE CLEANUP.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>Your place stays spotless, the party still happens.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for October dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 3) REFERRAL · THE PHOTOGRAPHER · Purple/Gold · 5
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Thu22_Photographer'] = [
 slide('<div class="mid"><div class="script">Behind the lens</div>'
       '<div class="h1" style="font-size:82px">PHOTOGRAPHERS SEE THE PARTY <em>FIRST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Every shoot ends with<br>somebody planning<br><em>the next one.</em></div>'
       '<div class="sup">Quinceañeras, baby showers, birthdays, the clients keep talking.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">SHOOT THE PARTY.<br><em>DROP OUR NAME.</em></div>'
       '<div class="sup">They book, you collect <b>after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR FAVORITE <em>PHOTOGRAPHER.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 4) EN ESPANOL #11 · LAS POSADAS · Midnight Navy · 5
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Thu22_Posadas'] = [
 slide('<div class="mid"><div class="script">Diciembre se llena</div>'
       '<div class="h1">LA POSADA SE PLANEA <em>DESDE OCTUBRE.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Diciembre<br><em>vuela.</em></div>'
       '<div class="sup">Las fechas de posadas y cenas navideñas se apartan primero, cada año pasa igual.</div></div>', p, 2, 5, ghost='12'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">$22</div>'
       '<div class="sup"><b>mesa con seis sillas,</b> entregada y recogida en todo Las Vegas. Tú instalas, o servicio completo desde $265.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿LA POSADA<br><em>GRANDE?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación incluidas.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO AL GRUPO FAMILIAR ANTES DE QUE <em>DICIEMBRE SE LLENE.</em></div>'
       + cta_block('Precios de entrega · el costo de envío se cotiza con tu orden') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 9 NIGHTS · Black&Gold · 4
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Thu22_9Nights'] = [
 slide('<div class="mid"><div class="script">The final stretch</div>'
       '<div class="h1">9 NIGHTS. <em>SINGLE DIGITS.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The calendar<br>just got<br><em>serious.</em></div>'
       '<div class="sup">Nine nights, two Saturdays, one monster weekend.</div></div>', p, 2, 4, ghost='9'),
 slide('<div class="mid"><div class="giant">9</div>'
       '<div class="sup"><b>nights out.</b> The parties on the 24th and the finale on the 31st are booking at the same time.</div></div>', p, 3, 4),
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
