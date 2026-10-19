"""WEDNESDAY OCT 21 cards. Morning card = tip day No.36 BUDGET MATH, the first card built on
the official price list. Palettes vs Tuesday (morning emerald / venue navy / referral velvet /
espanol blackgold / countdown purple): morning teal, venue purple single, referral blackgold,
espanol cream (weekly light, PRECIOS theme), countdown halloween."""
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

# 1) MORNING CARD · TIP No.36 BUDGET MATH (first price-list card) · Desert Teal · 6
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Wed21_BudgetMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.36</div>'
       '<div class="h1" style="font-size:88px">SEATING 48 PEOPLE COSTS LESS THAN <em>DINNER.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Everybody guesses high.<br><em>Here is the real math.</em></div>'
       '<div class="sup">Actual drop-off prices, no mystery, no quote games.</div></div>', p, 2, 6, ghost='36'),
 slide('<div class="mid"><div class="giant" style="font-size:240px">$2</div>'
       '<div class="sup"><b>one folding chair.</b> Two dollars. That is the whole price.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:230px">$22</div>'
       '<div class="sup"><b>a 6 ft table with six chairs.</b> One set, one family, twenty two dollars.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="giant" style="font-size:210px">$176</div>'
       '<div class="sup"><b>eight sets seats 48 guests,</b> delivered and picked up. You set up, or full-service setup and breakdown starts at $265.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> WITH YOUR HEADCOUNT FOR YOUR TOTAL.</div>'
       + cta_block('Drop-off pricing · delivery quoted with your order') + '</div>', p, 6, 6),
]

# 2) VENUE · HALLOWEEN SATURDAY · Purple/Gold · single card
p = palstyle(PAL['purple'])
CAROUSELS['BB_Venue_Wed21_HalloweenSat'] = [slide(
 '<div class="mid"><div class="script">Ten nights out</div>'
 '<div class="h1" style="font-size:98px">THE 31ST IS A SATURDAY. <em>BOOK THE ROOM.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>A private room beats a crowded bar on the biggest party night of fall.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for Halloween availability, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 3) REFERRAL · THE BARTENDER · Black&Gold · 5
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Wed21_Bartender'] = [
 slide('<div class="mid"><div class="script">Behind the bar</div>'
       '<div class="h1">BARTENDERS HEAR THE PARTY PLANS <em>FIRST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Every round comes with<br>a story about<br><em>a party.</em></div>'
       '<div class="sup">Birthdays being planned, showers being argued about, venues being hunted.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">POUR THE DRINK.<br><em>DROP OUR NAME.</em></div>'
       '<div class="sup">They book, you collect <b>after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR FAVORITE <em>BARTENDER.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 4) EN ESPANOL #10 · PRECIOS REALES · Daylight Cream · 5
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Wed21_Precios'] = [
 slide('<div class="mid"><div class="script">Sin misterio</div>'
       '<div class="h1">¿CUÁNTO CUESTA? <em>PRECIOS REALES.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="giant" style="font-size:230px">$2</div>'
       '<div class="sup"><b>una silla plegable.</b> Mesas de 6 pies desde $10.</div></div>', p, 2, 5),
 slide('<div class="mid"><div class="giant" style="font-size:220px">$22</div>'
       '<div class="sup"><b>mesa con seis sillas.</b> Entregadas y recogidas en todo Las Vegas, tú instalas. ¿Quieres que instalemos y recojamos todo? Servicio completo desde $265.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿Y EL<br><em>SALÓN?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación incluidas.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A QUIEN ANDA COTIZANDO <em>SU FIESTA.</em></div>'
       + cta_block('Precios de entrega · el costo de envío se cotiza con tu orden') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 10 NIGHTS · Halloween · 4
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Wed21_10Nights'] = [
 slide('<div class="mid"><div class="script">Single digits soon</div>'
       '<div class="h1">10 NIGHTS. THE RUSH IS <em>HERE.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">This is the week<br>everybody calls<br><em>at once.</em></div>'
       '<div class="sup">The ones who called early are not stressing right now.</div></div>', p, 2, 4, ghost='10'),
 slide('<div class="mid"><div class="giant">10</div>'
       '<div class="sup"><b>nights out.</b> Halloween is a Saturday, and tables, chairs and the room go to whoever calls first.</div></div>', p, 3, 4),
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
