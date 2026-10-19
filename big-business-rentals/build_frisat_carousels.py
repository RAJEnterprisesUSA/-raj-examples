"""FRIDAY OCT 23 + SATURDAY OCT 24 cards. Fri = tip day No.37 (weekly light-mode card),
Sat = business-angle day. Palettes per lane vs prior day:
Thu (velvet/emerald/purple/navy/blackgold) -> Fri morning cream, venue halloween, referral
teal, espanol emerald, countdown velvet -> Sat morning navy, venue purple, referral
blackgold, espanol teal, countdown emerald."""
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
FINE_ES = ('Recompensa según el tamaño de la reserva, hasta $100 · Sin límite de referidos · '
           'Se paga al completarse el evento referido')

CAROUSELS = {}

# ============ FRIDAY OCT 23 ============
# 1) MORNING CARD · TIP No.37 PLAYLIST MATH · Daylight Cream (weekly light card) · 6
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Fri23_PlaylistMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.37</div>'
       '<div class="h1" style="font-size:86px">68 SONGS. THAT IS THE WHOLE <em>PARTY.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Everybody fights<br>about the aux.<br><em>Nobody does the math.</em></div>'
       '<div class="sup">Here is what a four hour party actually plays.</div></div>', p, 2, 6, ghost='37'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">68</div>'
       '<div class="sup"><b>songs fill four hours</b> at three and a half minutes each. That is the entire night.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:220px">20</div>'
       '<div class="sup"><b>must-plays is all you pick.</b> That covers the first hour, and the room carries the rest.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">ONE AUX RULE:<br><em>THE HOST HOLDS IT.</em></div>'
       '<div class="sup">Guests request, the host decides. <b>No fifteen minute genre debates.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">ARGUE ABOUT THE PLAYLIST. <em>THE ROOM IS OUR JOB.</em></div>'
       + cta_block('Tables, chairs and the venue · comment "QUOTE" and we will DM you') + '</div>', p, 6, 6),
]

# 2) VENUE · TOMORROW OR NEXT SATURDAY · Halloween · single
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Venue_Fri23_TwoNights'] = [slide(
 '<div class="mid"><div class="script">Decision time</div>'
 '<div class="h1" style="font-size:94px">TOMORROW NIGHT OR <em>NEXT SATURDAY?</em></div>'
 '<div class="sup" style="margin-top:30px"><b>The 24th and the 31st are both party Saturdays, and the room works for either.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE and we will DM you what is open.</b></div></div>',
 p, 1, 1, single=True)]

# 3) REFERRAL · THE PARTY PLANNER · Desert Teal · 5
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Fri23_PartyPlanner'] = [
 slide('<div class="mid"><div class="script">To the pros</div>'
       '<div class="h1" style="font-size:84px">PARTY PLANNERS, THIS ONE PAYS <em>YOU.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">You already send<br>people to vendors<br><em>for free.</em></div>'
       '<div class="sup">Tables, chairs, linens, a venue. Your clients need all of it.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> every time a client you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">ADD US TO YOUR<br><em>VENDOR LIST.</em></div>'
       '<div class="sup">They book, you collect <b>after their event wraps.</b> No limit, every single referral pays.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE PLANNER WHO DOES <em>EVERYTHING.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 4) EN ESPANOL #12 · HALLOWEEN CAE EN SABADO · Emerald Night · 5
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Fri23_SabadoES'] = [
 slide('<div class="mid"><div class="script">Última semana</div>'
       '<div class="h1">HALLOWEEN CAE EN <em>SÁBADO.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Dos sábados<br>de fiesta<br><em>seguidos.</em></div>'
       '<div class="sup">El 24 y el 31. Las mesas y las sillas se van con quien llama primero.</div></div>', p, 2, 5, ghost='31'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">$22</div>'
       '<div class="sup"><b>mesa con seis sillas,</b> entregada y recogida en todo Las Vegas. Tú instalas, o servicio completo desde $265.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿FIESTA<br><em>GRANDE?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800 con instalación incluida.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO AL GRUPO QUE TODAVÍA NO DECIDE <em>DÓNDE.</em></div>'
       + cta_block('Precios de entrega · el costo de envío se cotiza con tu orden') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 8 NIGHTS · Velvet Rope · 4
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Fri23_8Nights'] = [
 slide('<div class="mid"><div class="script">Loaded weekend</div>'
       '<div class="h1">8 NIGHTS. THE WEEKEND IS <em>LOADED.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Costume parties<br>tomorrow.<br><em>The finale next week.</em></div>'
       '<div class="sup">Two party Saturdays back to back, one pile of phone calls.</div></div>', p, 2, 4, ghost='8'),
 slide('<div class="mid"><div class="giant">8</div>'
       '<div class="sup"><b>nights to Halloween.</b> Whoever locks their tables this weekend skips next week completely.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# ============ SATURDAY OCT 24 ============
# 6) MORNING CARD · NOVEMBER IS THE NEW DECEMBER (business day) · Midnight Navy · 5
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Sat24_November'] = [
 slide('<div class="mid"><div class="script">Think one month ahead</div>'
       '<div class="h1" style="font-size:88px">NOVEMBER IS THE NEW <em>DECEMBER.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Friendsgiving, work<br>parties, big race weekend<br><em>guests.</em></div>'
       '<div class="sup">November fills quietly while everybody stares at December.</div></div>', p, 2, 5, ghost='11'),
 slide('<div class="mid"><div class="giant" style="font-size:200px">$22</div>'
       '<div class="sup"><b>a table and six chairs,</b> delivered and picked up. Full-service setup and breakdown from $265.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">BOOK NOVEMBER<br><em>IN OCTOBER.</em></div>'
       '<div class="sup">The easy dates go first. <b>Lock yours before the holiday rush starts.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> WITH YOUR NOVEMBER DATE.</div>'
       + cta_block('Drop-off pricing · delivery quoted with your order') + '</div>', p, 5, 5),
]

# 7) VENUE · NEXT SATURDAY IS THE 31ST · Purple/Gold · single
p = palstyle(PAL['purple'])
CAROUSELS['BB_Venue_Sat24_The31st'] = [slide(
 '<div class="mid"><div class="script">One week out</div>'
 '<div class="h1" style="font-size:96px">NEXT SATURDAY IS <em>THE 31ST.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>One week from tonight, the biggest party night of fall.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for Halloween night, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 8) REFERRAL · THE TEACHER · Black&Gold · 5
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Sat24_Teacher'] = [
 slide('<div class="mid"><div class="script">Class is in session</div>'
       '<div class="h1" style="font-size:84px">TEACHERS KNOW EVERY PARTY <em>FIRST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Birthday invites in<br>the backpacks, quinces<br><em>in the group chat.</em></div>'
       '<div class="sup">Thirty families per classroom, and somebody is always planning something.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when a family you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">TEACH THE LESSON:<br><em>DROP OUR NAME.</em></div>'
       '<div class="sup">They book, you collect <b>after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR FAVORITE <em>TEACHER.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 9) EN ESPANOL #13 · RECOMIENDA Y GANA · Desert Teal · 5
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Sat24_RecomiendaES'] = [
 slide('<div class="mid"><div class="script">Corre la voz</div>'
       '<div class="h1" style="font-size:84px">RECOMIENDA Y GANA HASTA <em>$100.</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">En tu familia<br>siempre hay<br><em>una fiesta.</em></div>'
       '<div class="sup">Quinceañeras, bautizos, posadas, cumpleaños. Alguien siempre anda organizando.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>hasta, por reserva,</b> cuando alguien que tú mandas reserva mesas, sillas o el salón y da tu nombre.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">TÚ RECOMIENDAS.<br><em>NOSOTROS PAGAMOS.</em></div>'
       '<div class="sup">Ellos reservan y tú cobras <b>cuando termina su evento.</b> Sin límite de referidos.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A QUIEN CONOCE A <em>TODO EL MUNDO.</em></div>'
       + cta_block(FINE_ES) + '</div>', p, 5, 5),
]

# 10) COUNTDOWN · 7 NIGHTS ONE WEEK · Emerald Night · 4
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Sat24_7Nights'] = [
 slide('<div class="mid"><div class="script">Mark the calendar</div>'
       '<div class="h1">7 NIGHTS. ONE WEEK <em>EXACTLY.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Next Saturday,<br>this exact hour,<br><em>it is Halloween.</em></div>'
       '<div class="sup">The people partying tonight are booking next week before they go home.</div></div>', p, 2, 4, ghost='7'),
 slide('<div class="mid"><div class="giant">7</div>'
       '<div class="sup"><b>nights left.</b> One week to lock tables, chairs and the room for the finale.</div></div>', p, 3, 4),
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
