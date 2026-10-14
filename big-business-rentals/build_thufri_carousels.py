"""THURSDAY OCT 15 + FRIDAY OCT 16 carousels and venue cards.
Palettes Thu: tip purple, business cream (light card), venue velvet, referral emerald,
espanol blackgold, countdown halloween. Fri: tip navy, business teal, venue emerald,
referral blackgold, espanol halloween (theme match), countdown purple.
No lane repeats vs Tue (tip navy, venue blackgold, referral velvet, countdown purple, espanol emerald).
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
exec(t13.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns)   # navy blackgold velvet purple emerald
PAL = ns['PAL']
ns2 = {}
exec(m12.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns2)  # teal emerald halloween cream
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

# ============ THURSDAY OCT 15 ============

# 1) TIP No.31 · TIMELINE MATH · Purple/Gold · 6
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Thu_TimelineMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.31</div>'
       '<div class="h1" style="font-size:96px">YOUR PARTY HAS A SECRET <em>DEADLINE.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Three dates decide<br><em>everything.</em></div>'
       '<div class="sup">Most people miss all three, then call it bad luck.</div></div>', p, 2, 6, ghost='31'),
 slide('<div class="mid"><div class="giant" style="font-size:210px">3 WKS</div>'
       '<div class="sup"><b>invites go out three weeks ahead.</b> People lock their weekends fast, especially in the holiday stretch.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:210px">72 HRS</div>'
       '<div class="sup"><b>final headcount 72 hours out.</b> That is when the table, chair and food numbers get real.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">MORNING OF:<br><em>NOTHING.</em></div>'
       '<div class="sup">If setup is still on your list that morning, the math failed. <b>We deliver, set up and pick up,</b> so it never is.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO SOMEBODY PLANNING A <em>NOVEMBER PARTY.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · NOT A PROJECT · Daylight Cream · 5
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Thu_NotAProject'] = [
 slide('<div class="mid"><div class="script">The whole process</div>'
       '<div class="h1">RENTING TABLES IS NOT A <em>PROJECT.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="giant" style="font-size:230px">1</div>'
       '<div class="sup"><b>Tell us the date, the guest count and the address.</b> That is the entire form.</div></div>', p, 2, 5),
 slide('<div class="mid"><div class="giant" style="font-size:230px">2</div>'
       '<div class="sup"><b>We price it fast.</b> By call, by DM, or the chat on bigbusinesspartyrentals.com answers right away.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="giant" style="font-size:230px">3</div>'
       '<div class="sup"><b>It shows up. We set up. We pick up.</b> You never touch a folding chair.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) VENUE · WINTER BIRTHDAYS · Velvet Rope · single card
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Venue_Thu_WinterBday'] = [slide(
 '<div class="mid"><div class="script">To every November and December baby</div>'
 '<div class="h1" style="font-size:98px">WINTER BIRTHDAYS DESERVE A <em>REAL ROOM.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>Too cold for the backyard. Too many people for the living room.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 4) REFERRAL · THE BARBER · Emerald · 5
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Thu_Barber'] = [
 slide('<div class="mid"><div class="script">Fresh cut, fresh intel</div>'
       '<div class="h1">YOUR BARBER HEARS ABOUT EVERY PARTY <em>FIRST.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">The chair is where<br>every event gets<br><em>announced.</em></div>'
       '<div class="sup">Birthdays, baby showers, graduations, reunions. All of it gets said out loud in that chair.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">CUT HAIR? DO NAILS?<br><em>HEAR EVERYTHING?</em></div>'
       '<div class="sup">Mention us, have them drop your name, <b>collect after their event wraps.</b> No limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE CHAIR THAT <em>HEARS EVERYTHING.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 5) EN ESPANOL · REFERIDOS · Black&Gold · 5
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Thu_Referidos'] = [
 slide('<div class="mid"><div class="script">Gana con nosotros</div>'
       '<div class="h1">¿CONOCES A ALGUIEN QUE HACE <em>FIESTAS?</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">En cada familia hay<br>alguien que organiza<br><em>todo.</em></div>'
       '<div class="sup">Esa persona vale dinero. Literalmente.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>hasta $100 por reserva,</b> cuando reservan mesas, sillas o el salón y dan tu nombre.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">SIN LÍMITE DE<br><em>REFERIDOS.</em></div>'
       '<div class="sup">Recomienda a toda la familia. <b>Se paga cuando termina el evento referido.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">ENVÍA ESTO A LA TÍA QUE <em>ORGANIZA TODO.</em></div>'
       + cta_block(FINE_ES) + '</div>', p, 5, 5),
]

# 6) COUNTDOWN · 16 NIGHTS · Halloween · 4
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Thu_16Nights'] = [
 slide('<div class="mid"><div class="script">Check the group chat</div>'
       '<div class="h1">16 NIGHTS. THE GROUP CHAT IS STILL <em>DECIDING.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Somebody has to<br>pick the <em>house.</em></div>'
       '<div class="sup">And the one who picks the house needs tables, chairs and a plan.</div></div>', p, 2, 4, ghost='16'),
 slide('<div class="mid"><div class="giant">16</div>'
       '<div class="sup"><b>nights out.</b> Tables, chairs and the party room book first. The costume can wait a week.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# ============ FRIDAY OCT 16 ============

# 7) TIP No.32 · RSVP MATH · Midnight Navy · 6
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Fri_RsvpMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.32</div>'
       '<div class="h1" style="font-size:94px">EVERY GUEST LIST TELLS A LITTLE <em>LIE.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">People say yes in<br>October and go quiet<br><em>in November.</em></div>'
       '<div class="sup">You cannot seat a party on a guess. Here is the fix.</div></div>', p, 2, 6, ghost='32'),
 slide('<div class="mid"><div class="h2">SET FOR EVERY<br><em>YES.</em></div>'
       '<div class="sup">An empty chair costs nothing. <b>A missing chair is a scramble</b> in front of everybody.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:240px">+2</div>'
       '<div class="sup"><b>add two seats past your count:</b> the plus-one you forgot and the cousin nobody invited.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">RENTALS<br><em>FLEX.</em></div>'
       '<div class="sup">Tell us the range and we size the order. <b>Adjust the final count 72 hours out.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS STILL WAITING ON <em>RSVPS.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 8) BUSINESS · 48 HOURS · Desert Teal · 5
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Fri_48Hours'] = [
 slide('<div class="mid"><div class="script">It is Friday</div>'
       '<div class="h1">THE WEEKEND IS 48 HOURS <em>AWAY.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Saturday party,<br><em>Friday panic.</em></div>'
       '<div class="sup">It does not have to go like that. Not this week.</div></div>', p, 2, 5, ghost='48'),
 slide('<div class="mid"><div class="h2">ONE CALL<br><em>TODAY.</em></div>'
       '<div class="sup"><b>Tables, chairs and linens locked for the weekend</b> before you finish lunch.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">DELIVERED.<br>SET.<br><em>GONE.</em></div>'
       '<div class="sup">We drop it, set it and pick it up after. <b>You never load a truck.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A WEEKEND PRICE.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 9) VENUE · $25 EACH · Emerald · single card
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Venue_Fri_SplitMath'] = [slide(
 '<div class="mid"><div class="script">Do the math with us</div>'
 '<div class="h1" style="font-size:102px">$625 SPLIT 25 WAYS IS <em>$25 EACH.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>Three hours. Private venue. Tables, chairs and setup included.</b><br>'
 'Less than one round of drinks on the Strip, and the room is all yours.<br>'
 'Seats 40 · holds 80 standing · 4 hours $800.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>',
 p, 1, 1, single=True)]

# 10) REFERRAL · PAYDAY · Black&Gold · 5
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Fri_Payday'] = [
 slide('<div class="mid"><div class="script">Check your account</div>'
       '<div class="h1">TODAY IS PAYDAY. HERE IS A <em>SECOND ONE.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">The first check came<br>from work. The second<br>comes from <em>knowing people.</em></div>'
       '<div class="sup">No shifts, no applications, no clocking in.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when somebody you send books rentals or the venue and drops your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">REFER FRIDAY.<br><em>COLLECT AFTER.</em></div>'
       '<div class="sup">No limit on referrals. <b>Paid after the referred event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO SOMEBODY WHO KNOWS <em>EVERYBODY.</em></div>'
       + cta_block(FINE) + '</div>', p, 5, 5),
]

# 11) EN ESPANOL · FECHAS DE HALLOWEEN · Halloween · 5
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Fri_HalloweenES'] = [
 slide('<div class="mid"><div class="script">Mira el calendario</div>'
       '<div class="h1">HALLOWEEN CAE EN <em>SÁBADO</em> ESTE AÑO.</div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">Fiesta grande<br><em>garantizada.</em></div>'
       '<div class="sup">Y las fechas buenas de octubre ya se están apartando.</div></div>', p, 2, 5, ghost='31'),
 slide('<div class="mid"><div class="h2">MESAS, SILLAS<br>Y <em>MANTELES.</em></div>'
       '<div class="sup"><b>Entregados, instalados y recogidos</b> en todo Las Vegas. También el 31.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">¿Y EL<br><em>LUGAR?</em></div>'
       '<div class="sup">Salón privado: <b>40 sentados, 80 de pie.</b> 3 horas $625 · 4 horas $800, con mesas, sillas e instalación.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:54px">ESCRÍBENOS AL CHAT DE<br><em style="font-size:44px">BIGBUSINESSPARTYRENTALS.COM</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 12) COUNTDOWN · 15 NIGHTS · Purple/Gold · 4
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Fri_15Nights'] = [
 slide('<div class="mid"><div class="script">Halloween countdown</div>'
       '<div class="h1">15 NIGHTS. CANDY IS NOT <em>THE PLAN.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Candy is for the kids<br>at the door.<br><em>The party is for after.</em></div>'
       '<div class="sup">And the party needs tables, chairs and a room.</div></div>', p, 2, 4, ghost='15'),
 slide('<div class="mid"><div class="giant">15</div>'
       '<div class="sup"><b>nights out.</b> Halloween is a Saturday this year, the busiest kind. The setup books before the costume does.</div></div>', p, 3, 4),
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
