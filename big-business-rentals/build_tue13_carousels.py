"""TUESDAY OCT 13 carousels. Palettes vs Monday (teal/emerald/halloween/cream):
tip navy, venue blackgold (corporate), referral velvet, countdown purple, espanol emerald.
Business lane = the inflatable footage reel, no carousel."""
import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week6'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'navy': dict(bg="radial-gradient(circle at 46% 20%, #1d2c52 0%, #15203e 50%, #0a1024 100%)",
   ink="#f1edde", body="#ccd2e4", script="#9fb6e8", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#a9b6d4", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'blackgold': dict(bg="radial-gradient(circle at 48% 22%, #2e2a20 0%, #23201a 50%, #121009 100%)",
   ink="#f4eedb", body="#d8d0ba", script="#d8bd7e", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bdb294", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'velvet': dict(bg="radial-gradient(circle at 45% 22%, #5a1a26 0%, #40111b 50%, #230810 100%)",
   ink="#f6ecdd", body="#e4cdbb", script="#e0a9a9", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#cfa9a9", grainmode="overlay", vig="rgba(0,0,0,.52)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'purple': dict(bg="radial-gradient(circle at 50% 28%, #3a1a5e 0%, #2c1247 55%, #150826 100%)",
   ink="#f2ecdd", body="#d8ceb6", script="#cbb2e2", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bfa9d8", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.22)", barbg="rgba(229,184,75,.25)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
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

# 1) TIP No.30 · CAKE MATH · Midnight Navy · 6 slides
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Tue_CakeMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.30</div>'
       '<div class="h1">HOW MUCH CAKE DOES A PARTY <em>EAT?</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Everybody wants<br>a slice. Nobody wants<br><em>seven leftover pounds.</em></div>'
       '<div class="sup">Two numbers get the order right.</div></div>', p, 2, 6, ghost='30'),
 slide('<div class="mid"><div class="giant">24</div>'
       '<div class="sup"><b>party slices from one 8 inch round,</b> cut event style, one by two inches.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant">54</div>'
       '<div class="sup"><b>slices from a half sheet,</b> the workhorse of every birthday table.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">COUNT GUESTS.<br>ADD 10%.<br><em>STOP THERE.</em></div>'
       '<div class="sup">Cake handled. <b>The table it sits on, the chairs around it? That is us.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER ALWAYS <em>OVER-ORDERS.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) VENUE · COMPANY PARTY · Black&Gold · single card
p = palstyle(PAL['blackgold'])
venue_inner = (
 '<div class="mid"><div class="script">To every office planner</div>'
 '<div class="h1" style="font-size:98px">THE COMPANY PARTY DOES NOT NEED A <em>CASINO BUDGET.</em></div>'
 '<div class="sup" style="margin-top:30px"><b>December and F1 season are already filling.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:26px;color:var(--gold1)"><b>Comment VENUE for open dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>')
CAROUSELS['BB_Venue_Tue_Company'] = [slide(venue_inner, p, 1, 1, single=True)]

# 3) REFERRAL · THE WORK PLUG · Velvet Rope · 5 slides
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Tue_WorkPlug'] = [
 slide('<div class="mid"><div class="script">Check the break room</div>'
       '<div class="h1">EVERY JOB HAS A <em>PARTY PLANNER.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody at work is<br>about to get handed<br><em>the holiday party.</em></div>'
       '<div class="sup">They need tables, chairs and a room. You need their booking.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book rentals or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">BE THE PLUG.<br><em>NOT THE PLANNER.</em></div>'
       '<div class="sup">No limit on referrals. <b>Paid after their event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR <em>WORK BESTIE.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 4) COUNTDOWN · 18 NIGHTS · Purple/Gold · 4 slides
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Tue_18Nights'] = [
 slide('<div class="mid"><div class="script">Look at the calendar</div>'
       '<div class="h1">18 NIGHTS. TWO SATURDAYS. THEN <em>THE BIG ONE.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The 17th.<br>The 24th.<br><em>Then Halloween itself.</em></div>'
       '<div class="sup">Every party between now and then needs chairs. Most of them call this week.</div></div>', p, 2, 4, ghost='18'),
 slide('<div class="mid"><div class="giant">18</div>'
       '<div class="sup"><b>nights to lock your date:</b> tables, chairs and the party room go to whoever calls first.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# 5) EN ESPANOL · EL VENUE · Emerald · 5 slides
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Tue_ElVenue'] = [
 slide('<div class="mid"><div class="script">La pregunta de siempre</div>'
       '<div class="h1">¿DÓNDE VA A SER <em>LA FIESTA?</em></div></div>', p, 1, 5, hook=True,
       swipetext='DESLIZA&nbsp;&nbsp;→'),
 slide('<div class="mid"><div class="h2">En tu sala no caben<br><em>60 personas.</em></div>'
       '<div class="sup">Lo sabemos. Para eso está nuestro salón privado.</div></div>', p, 2, 5, ghost='60'),
 slide('<div class="mid"><div class="h2">SALÓN PRIVADO<br><em>EN LAS VEGAS.</em></div>'
       '<div class="sup"><b>40 personas sentadas, 80 de pie.</b> Perfecto para cumpleaños, bautizos y posadas.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">3 HORAS · $625<br><em>4 HORAS · $800</em></div>'
       '<div class="sup">Con mesas, sillas e instalación <b>incluidas.</b></div></div>', p, 4, 5),
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
            stem = name if n == 1 else f'{name}_{i+1:02d}'
            tmp = str(OUT/f'{stem}.2x.png')
            els.nth(i).screenshot(path=tmp)
            Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/f'{stem}.png')
            pathlib.Path(tmp).unlink()
        print('done', name, n, 'slides')
    b.close()
