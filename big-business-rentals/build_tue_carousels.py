import glob, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

# reuse the shared carousel CSS and helpers from the Monday generator
src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'navy': dict(bg="radial-gradient(circle at 34% 20%, #10224d 0%, #0b1736 50%, #070f26 100%)",
   ink="#eef0f6", body="#ccd6ea", script="#9db4e4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#c6cede", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'velvet': dict(bg="radial-gradient(circle at 40% 18%, #5e1223 0%, #420a17 50%, #2e0710 100%)",
   ink="#f6ecdf", body="#eddcc8", script="#e89aa8", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#d8a9b4", grainmode="overlay", vig="rgba(0,0,0,.52)",
   ghost="rgba(239,203,124,.16)", barbg="rgba(229,184,75,.25)"),
 'blackgold': dict(bg="radial-gradient(circle at 50% 26%, #2c2820 0%, #23201a 45%, #0e0c09 100%)",
   ink="#f2ecdd", body="#e2d8bd", script="#cfc4a4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#a99f85", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(229,184,75,.17)", barbg="rgba(229,184,75,.25)"),
 'halloween': dict(bg="radial-gradient(circle at 50% 36%, #241040 0%, #140823 50%, #060309 100%)",
   ink="#f6ecc9", body="#d9c9ef", script="#c9a9f0", gold1="#ffb13d", gold2="#ff8c2e",
   frame="#B08D3E", soft="#b9a8d4", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(255,140,46,.22)", barbg="rgba(255,140,46,.3)"),
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

def slide(inner, pal, i, n, hook=False, ghost=None):
    g = f'<div class="ghostn">{ghost}</div>' if ghost else ''
    kick = '<div class="kick">◆&nbsp; BIG BUSINESS · LAS VEGAS &nbsp;◆</div>'
    p = '' if hook else prog(i, n)
    sw = '<div class="swipe">SWIPE&nbsp;&nbsp;→</div>' if hook else ''
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

p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Tue_DrinkMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.23</div>'
       '<div class="h1">HOW MANY <em>DRINKS</em> DOES A PARTY NEED?</div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Guess wrong and<br>the bar dies<br><em>at hour two.</em></div>'
       '<div class="sup">There is a formula. Bartenders have used it forever.</div></div>', p, 2, 6, ghost='SIP'),
 slide('<div class="mid"><div class="giant">2</div>'
       '<div class="sup"><b>drinks per guest in the first hour,</b> every time. People arrive thirsty.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="h2"><em>+1</em> EVERY HOUR AFTER.</div>'
       '<div class="sup">The pace settles. One per guest, per hour, <b>till the lights come on.</b></div></div>', p, 4, 6),
 slide('<div class="mid"><div class="giant" style="font-size:240px">200</div>'
       '<div class="sup">drinks for <b>40 guests over 4 hours.</b> Yes, really. Stock that number and nobody goes thirsty.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS <em>STOCKING THE COOLER.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Tue_HiredATeam'] = [
 slide('<div class="mid"><div class="script">This weekend</div>'
       '<div class="h1">HOST LIKE YOU HIRED <em>A TEAM.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2"><em>Because you did.</em></div>'
       '<div class="sup">Every order comes with people whose whole job is your party day.</div></div>', p, 2, 5, ghost='VIP'),
 slide('<div class="mid"><div class="h2">DELIVERY.<br>SETUP.<br><em>PICKUP.</em></div>'
       '<div class="sup">Tables, chairs and linens that <b>match your theme,</b> on every single order.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOU GREET<br>THE GUESTS.<br><em>WE DO THE HEAVY LIFTING.</em></div>'
       '<div class="sup">Set before they arrive, <b>gone after they leave.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Tue_WordOfMouth'] = [
 slide('<div class="mid"><div class="script">In this economy,</div>'
       '<div class="h1">WORD OF MOUTH <em>PAYS.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody you know<br>is planning a party<br><em>right now.</em></div>'
       '<div class="sup">Group chat, job, family thread. Somebody.</div></div>', p, 2, 5, ghost='$$$'),
 slide('<div class="mid"><div class="h2">SAY <em>"I KNOW A GUY."</em></div>'
       '<div class="sup">Send them our way and have them <b>drop your name</b> when they book.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup">After their event wraps, <b>you collect.</b> Up to $100 per booking, no limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO YOUR <em>BEST CONNECTOR.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Tue_25Nights'] = [
 slide('<div class="mid"><div class="script">the jack-o-lanterns know</div>'
       '<div class="h1"><em>25 NIGHTS</em> TILL HALLOWEEN.</div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The pumpkins are<br>counting.<br><em>So are the bookings.</em></div>'
       '<div class="sup">October weekends in Vegas do not wait for anybody.</div></div>', p, 2, 4, ghost='25'),
 slide('<div class="mid"><div class="giant">25</div>'
       '<div class="sup"><b>Lock the date before the glow goes out:</b> tables, chairs and the party room in one call.</div></div>', p, 3, 4),
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
        for i in range(els.count()):
            tmp = str(OUT/f'{name}_{i+1:02d}.2x.png')
            els.nth(i).screenshot(path=tmp)
            img = Image.open(tmp)
            img.resize((1080,1350), Image.LANCZOS).save(OUT/f'{name}_{i+1:02d}.png')
            pathlib.Path(tmp).unlink()
        print('done', name, els.count(), 'slides')
    b.close()
