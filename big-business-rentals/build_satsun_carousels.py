"""SATURDAY OCT 17 + SUNDAY OCT 18 carousels and venue cards.
Palettes Sat: tip cream (light card), business purple, venue blackgold, referral velvet,
espanol emerald, countdown halloween. Sun: tip teal, business navy, venue cream,
referral emerald, espanol velvet, countdown purple. No lane repeats day to day.
"""
import glob, pathlib, shutil
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week7'
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

# ============ SATURDAY OCT 17 ============

# 1) TIP No.33 · WEATHER MATH · Daylight Cream · 6
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Sat_WeatherMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.33</div>'
       '<div class="h1" style="font-size:92px">VEGAS OCTOBER HAS TWO SEASONS <em>A DAY.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Warm at three.<br><em>Cold by eight.</em></div>'
       '<div class="sup">Outdoor parties plan for the first half and freeze in the second.</div></div>', p, 2, 6, ghost='33'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">20°</div>'
       '<div class="sup"><b>the desert drops fast after sunset,</b> often twenty degrees or more. Plan for the colder number, not the forecast high.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:220px">6 PM</div>'
       '<div class="sup"><b>sunset lands around six</b> in late October. Food, toasts and photos before dark, dancing after.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">PLAN B IS<br><em>A ROOM.</em></div>'
       '<div class="sup">If the cold wins, our private venue takes the whole party. <b>Seats 40, holds 80 standing.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS PLANNING A <em>BACKYARD PARTY.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · BEFORE BREAKFAST · Purple/Gold · 5
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Sat_BeforeBreakfast'] = [
 slide('<div class="mid"><div class="script">Saturday, early</div>'
       '<div class="h1">THE PARTY SHOWED UP BEFORE <em>BREAKFAST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Morning delivery means<br>your Saturday starts<br><em>finished.</em></div>'
       '<div class="sup">Tables down. Chairs set. Truck gone.</div></div>', p, 2, 5, ghost='AM'),
 slide('<div class="mid"><div class="h2">YOU SLEPT.<br><em>WE WORKED.</em></div>'
       '<div class="sup"><b>Delivery, setup and pickup</b> are all part of how we do it. Every order, every time.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOUR ONLY JOB:<br><em>OPEN THE DOOR.</em></div>'
       '<div class="sup">Point at the room. <b>We handle the rest,</b> then come back for it all tomorrow.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) VENUE · LAST TWO SATURDAYS · Black&Gold · single card
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Venue_Sat_TwoSaturdays'] = [slide(
 '<div class="mid"><div class="script">October 24 · October 31</div>'
 '<div class="h1" style="font-size:102px">TWO SATURDAYS LEFT IN <em>OCTOBER.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>The 24th and the 31st. One of them should be your party.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE and we will DM you which dates are still open.</b></div></div>',
 p, 1, 1, single=True)]

# 4) REFERRAL · TONIGHT · Velvet Rope · 5
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Sat_Tonight'] = [
 slide('<div class="mid"><div class="script">Saturday night assignment</div>'
       '<div class="h1">TONIGHT AT THE PARTY, <em>LISTEN CLOSE.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody will say it:<br><em>"we should do this<br>for my birthday."</em></div>'
       '<div class="sup">That sentence is worth money. To you.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book rentals or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOU HEARD IT<br><em>FIRST.</em></div>'
       '<div class="sup">Send them our way, have them drop your name, <b>collect after their event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE FRIEND WHO <em>SAID IT.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 5) EN ESPANOL · SERVICIOS · Emerald · 5
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Sat_Servicios'] = [
 slide('<div class="mid"><div class="script">Lo que siempre falta</div>'
       '<div class="h1">LA COMIDA ESTÁ. <em>¿DÓNDE SE SIENTAN?</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">La música está.<br>Los tamales están.<br><em>¿Y las mesas?</em></div>'
       '<div class="sup">Lo que siempre falta a última hora: mesas, sillas y manteles.</div></div>', p, 2, 5, ghost='?'),
 slide('<div class="mid"><div class="h2">MESAS Y<br><em>SILLAS.</em></div>'
       '<div class="sup"><b>Entregadas, instaladas y recogidas</b> por nosotros, en todo Las Vegas.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">MANTELES A LA<br><em>MEDIDA.</em></div>'
       '<div class="sup">Del tamaño correcto para cada mesa. <b>Tú no planchas nada.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A QUIEN ORGANIZA LA <em>PRÓXIMA FIESTA.</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 6) COUNTDOWN · 14 NIGHTS · Halloween · 4
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Sat_14Nights'] = [
 slide('<div class="mid"><div class="script">Halloween countdown</div>'
       '<div class="h1">TWO WEEKS. <em>EXACTLY.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Fourteen nights from<br>tonight, it is<br><em>Halloween night.</em></div>'
       '<div class="sup">A Saturday. The biggest party night of the fall.</div></div>', p, 2, 4, ghost='14'),
 slide('<div class="mid"><div class="giant">14</div>'
       '<div class="sup"><b>nights to lock tables, chairs and the room</b> before the rush locks them for you.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# ============ SUNDAY OCT 18 ============

# 7) TIP No.34 · GOLDEN HOUR MATH · Desert Teal · 6
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Sun_GoldenHour'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.34</div>'
       '<div class="h1" style="font-size:92px">YOUR PARTY PHOTOS HAVE A <em>DEADLINE.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Every phone comes out<br><em>at the party.</em></div>'
       '<div class="sup">The light decides whether those pictures are worth keeping.</div></div>', p, 2, 6, ghost='34'),
 slide('<div class="mid"><div class="giant" style="font-size:210px">1 HR</div>'
       '<div class="sup"><b>before sunset is golden hour:</b> warm light, soft shadows, everybody looks good in it.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="h2">CAKE BEFORE<br><em>DARK.</em></div>'
       '<div class="sup">Schedule the big moments, <b>cake, toasts, the group photo,</b> for that hour. Dancing can be dark.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">LIGHT THE TABLES,<br><em>NOT THE FENCE.</em></div>'
       '<div class="sup">After sunset, <b>warm bulbs over the seating</b> beat one porch floodlight every time.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE FRIEND WITH THE <em>GOOD PHONE.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 8) BUSINESS · FOOTBALL SUNDAY · Midnight Navy · 5
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Sun_FootballSeats'] = [
 slide('<div class="mid"><div class="script">Game day at the house</div>'
       '<div class="h1">FOOTBALL SUNDAY NEEDS MORE <em>SEATS.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">The crew outgrew the<br>couch about three<br><em>Sundays ago.</em></div>'
       '<div class="sup">Standing room by kickoff, plates balanced on knees by halftime.</div></div>', p, 2, 5, ghost='7'),
 slide('<div class="mid"><div class="h2">TABLES FOR<br><em>THE FOOD.</em></div>'
       '<div class="sup">A real spread needs a real table. <b>Not counter corners and a wobbly tray.</b></div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">CHAIRS FOR<br><em>THE CREW.</em></div>'
       '<div class="sup">By the dozen, <b>delivered and picked back up,</b> so the living room goes back to normal Monday.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:54px">CHAT WITH US AT<br><em style="font-size:46px">BIGBUSINESSPARTYRENTALS.COM</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 9) VENUE · FRIENDSGIVING · Daylight Cream · single card
p = palstyle(PAL['cream'])
CAROUSELS['BB_Venue_Sun_Friendsgiving'] = [slide(
 '<div class="mid"><div class="script">Before the family holidays</div>'
 '<div class="h1" style="font-size:100px">FRIENDSGIVING NEEDS A <em>BIGGER TABLE.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>November weekends book first, and they are already going.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open November dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 10) REFERRAL · GROUP CHAT ADMIN · Emerald · 5
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Sun_ChatAdmin'] = [
 slide('<div class="mid"><div class="script">You know the one</div>'
       '<div class="h1">EVERY GROUP CHAT HAS AN <em>ADMIN.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Makes the plan.<br>Books the thing.<br><em>Collects the money.</em></div>'
       '<div class="sup">That job has never paid. Until now.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when the chat books rentals or the venue and your name is on it.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">GET PAID LIKE<br><em>AN ADMIN.</em></div>'
       '<div class="sup">Point the next party our way. <b>Collect after the event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE CHAT. THE ADMIN KNOWS <em>WHO THEY ARE.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 11) EN ESPANOL · EL VALS · Velvet Rope · 5
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Sun_ElVals'] = [
 slide('<div class="mid"><div class="script">Para la quinceañera</div>'
       '<div class="h1">EL VALS NECESITA <em>PISTA.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">La sala de la casa<br>no alcanza para<br><em>el vals.</em></div>'
       '<div class="sup">Ni para la corte, ni para las quince mesas de la familia.</div></div>', p, 2, 5, ghost='XV'),
 slide('<div class="mid"><div class="h2">SALÓN<br><em>PRIVADO.</em></div>'
       '<div class="sup"><b>40 sentados, 80 de pie.</b> Espacio para el vals, la corte y la pista llena.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">3 HORAS $625.<br><em>4 HORAS $800.</em></div>'
       '<div class="sup">Con mesas, sillas e instalación incluidas. <b>También rentamos todo para tu jardín o salón.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A UNA FAMILIA QUE PLANEA UNA <em>QUINCE.</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 12) COUNTDOWN · 13 NIGHTS · Purple/Gold · 4
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Sun_13Nights'] = [
 slide('<div class="mid"><div class="script">Halloween countdown</div>'
       '<div class="h1">13 NIGHTS LEFT. <em>FITTING.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The spookiest number<br>on the <em>calendar.</em></div>'
       '<div class="sup">And the last comfortable week to book the room.</div></div>', p, 2, 4, ghost='13'),
 slide('<div class="mid"><div class="giant">13</div>'
       '<div class="sup"><b>nights out.</b> The closer it gets, the fewer dates and chairs are left. Book calm, not scrambling.</div></div>', p, 3, 4),
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
