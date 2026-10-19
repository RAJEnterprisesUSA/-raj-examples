"""MONDAY OCT 19 cards, first set on the merged format. Palettes vs Sunday
(tip teal / business navy / venue cream / referral emerald / espanol velvet / countdown purple):
morning blackgold, venue velvet single, referral purple, espanol cream (weekly light card),
countdown halloween."""
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

# 1) MORNING CARD (merged lane debut) · TIP No.35 SPACE MATH · Black&Gold · 6
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Mon19_SpaceMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.35</div>'
       '<div class="h1" style="font-size:90px">YOUR LIVING ROOM IS SMALLER THAN YOU <em>THINK.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Twenty yeses in the<br>group chat.<br><em>One couch.</em></div>'
       '<div class="sup">Every party has this moment. Here is the math that prevents it.</div></div>', p, 2, 6, ghost='35'),
 slide('<div class="mid"><div class="giant" style="font-size:200px">10 SQFT</div>'
       '<div class="sup"><b>about ten square feet per seated guest.</b> That is the number nobody measures.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:230px">x 20</div>'
       '<div class="sup"><b>twenty guests need around 200 clear square feet.</b> Count it after you move the sectional, not before.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">CHAIRS STACK.<br><em>WALLS DO NOT.</em></div>'
       '<div class="sup"><b>We size the table and chair order to your space.</b> And if the math says no, our private venue seats 40.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) VENUE · HOLIDAY DATE · Velvet Rope · single card
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Venue_Mon19_HolidayDate'] = [slide(
 '<div class="mid"><div class="script">December books first</div>'
 '<div class="h1" style="font-size:96px">YOUR HOLIDAY PARTY HAS A DATE. <em>CLAIM IT.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>The December Saturdays are already moving.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open December dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 3) REFERRAL · THE NAIL TECH · Purple/Gold · 5
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Mon19_NailTech'] = [
 slide('<div class="mid"><div class="script">Fresh set, fresh intel</div>'
       '<div class="h1">YOUR NAIL TECH HEARS EVERY PARTY PLAN <em>FIRST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Baby showers. Birthdays.<br>Quinces. Weddings.<br><em>All planned in that chair.</em></div>'
       '<div class="sup">Two hours of acrylic is two hours of party intel.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">DO NAILS?<br><em>HEAR EVERYTHING?</em></div>'
       '<div class="sup">Mention us, have them drop your name, <b>collect after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR <em>NAIL TECH.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 4) EN ESPANOL #8 · DICIEMBRE · Daylight Cream · 5
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Mon19_Diciembre'] = [
 slide('<div class="mid"><div class="script">Las fechas vuelan</div>'
       '<div class="h1">DICIEMBRE SE RESERVA EN <em>OCTUBRE.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Posadas. Cenas de<br>empresa. <em>Año nuevo.</em></div>'
       '<div class="sup">Los sábados de diciembre se apartan primero, y se apartan desde ahora.</div></div>', p, 2, 5, ghost='12'),
 slide('<div class="mid"><div class="h2">MESAS, SILLAS<br>Y <em>MANTELES.</em></div>'
       '<div class="sup"><b>Entregados, instalados y recogidos</b> por nosotros, en todo Las Vegas.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿Y EL<br><em>LUGAR?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">APARTA TU FECHA <em>HOY.</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 12 NIGHTS · Halloween · 4
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Mon19_12Nights'] = [
 slide('<div class="mid"><div class="script">Halloween countdown</div>'
       '<div class="h1">12 NIGHTS. YOUR HOUSE OR <em>THEIRS?</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Somebody in your circle<br>is hosting<br><em>Halloween.</em></div>'
       '<div class="sup">The one with the tables and chairs wins the argument.</div></div>', p, 2, 4, ghost='12'),
 slide('<div class="mid"><div class="giant">12</div>'
       '<div class="sup"><b>nights out.</b> The setup books before the candy aisle empties. Halloween is a Saturday this year.</div></div>', p, 3, 4),
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
