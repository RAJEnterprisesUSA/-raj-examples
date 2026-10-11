"""SUNDAY OCT 11 carousels. Palettes vs Sat: tip cream (weekly light card),
business emerald, venue velvet (masquerade = VIP burgundy), referral blackgold,
countdown purple. Raiders at New England 10am PT = brunch watch party day."""
import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'cream': dict(bg="radial-gradient(circle at 30% 18%, #faf3e3 0%, #f4ead6 45%, #e7d9bc 100%)",
   ink="#241a35", body="#4a3c28", script="#9a6f20", gold1="#c89a3c", gold2="#8a6a1c",
   frame="#a07c2c", soft="#5c4b2e", grainmode="multiply", vig="rgba(120,95,40,.16)",
   ghost="rgba(160,124,44,.25)", barbg="rgba(160,124,44,.25)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
 'velvet': dict(bg="radial-gradient(circle at 45% 22%, #5a1a26 0%, #40111b 50%, #230810 100%)",
   ink="#f6ecdd", body="#e4cdbb", script="#e0a9a9", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#cfa9a9", grainmode="overlay", vig="rgba(0,0,0,.52)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'blackgold': dict(bg="radial-gradient(circle at 48% 22%, #2e2a20 0%, #23201a 50%, #121009 100%)",
   ink="#f4eedb", body="#d8d0ba", script="#d8bd7e", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bdb294", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'purple': dict(bg="radial-gradient(circle at 50% 28%, #3a1a5e 0%, #2c1247 55%, #150826 100%)",
   ink="#f2ecdd", body="#d8ceb6", script="#cbb2e2", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bfa9d8", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.22)", barbg="rgba(229,184,75,.25)"),
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

def slide(inner, pal, i, n, hook=False, ghost=None, single=False):
    g = f'<div class="ghostn">{ghost}</div>' if ghost else ''
    kick = '<div class="kick">◆&nbsp; BIG BUSINESS · LAS VEGAS &nbsp;◆</div>'
    p = '' if (hook or single) else prog(i, n)
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

# 1) TIP No.28 · BRUNCH MATH · Daylight Cream · 6 slides
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Sun_BrunchMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.28</div>'
       '<div class="h1">HOW MUCH BRUNCH DOES A <em>WATCH PARTY</em> EAT?</div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Kickoff is at 10am.<br><em>Nobody ate breakfast.</em></div>'
       '<div class="sup">Morning guests arrive hungry. Three numbers keep the table ahead of them.</div></div>', p, 2, 6, ghost='28'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">1 GAL = 10</div>'
       '<div class="sup"><b>one gallon of juice pours about 10 glasses.</b> Twenty guests, two gallons, done.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:235px">6 FT</div>'
       '<div class="sup"><b>one 6 foot table runs a whole brunch line</b> when plates start at one end and food flows one direction.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">SEATS BEAT<br><em>SOFAS.</em></div>'
       '<div class="sup">Everyone eats at kickoff: <b>one real seat per guest,</b> not one couch per six. We deliver them.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS HOSTING THE <em>10AM GAME.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · GAME DAY HOST · Emerald · 5 slides · TikTok pick
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Sun_GameDay'] = [
 slide('<div class="mid"><div class="script">Vegas, it is game day</div>'
       '<div class="h1">YOUR CREW IS COMING AT <em>10AM.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">The group chat<br>picked your house.<br><em>Nobody asked your dining room.</em></div>'
       '<div class="sup">Six folding chairs and a prayer is not a seating plan.</div></div>', p, 2, 5, ghost='10'),
 slide('<div class="mid"><div class="giant" style="font-size:215px">20 SEATS</div>'
       '<div class="sup"><b>or forty, your call:</b> tables, chairs and linens delivered, set up and picked up around your schedule.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOU WATCH<br>THE GAME.<br><em>WE HANDLE THE ROOM.</em></div>'
       '<div class="sup">Host the win, <b>skip the warehouse shift.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:56px">COMMENT <em>"QUOTE"</em> OR CHAT WITH US AT<br>'
       '<em style="font-size:44px">BIGBUSINESSPARTYRENTALS.COM</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) VENUE · MIDNIGHT MASQUERADE · Velvet Rope · single card
p = palstyle(PAL['velvet'])
venue_inner = (
 '<div class="mid"><div class="script">For the grown folks</div>'
 '<div class="h1" style="font-size:102px">THIS HALLOWEEN, THROW A <em>MIDNIGHT MASQUERADE.</em></div>'
 '<div class="sup" style="margin-top:32px"><b>Masks on, kids at grandma\'s, Halloween on a Saturday.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:28px;color:var(--gold1)"><b>Comment VENUE for open October dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>')
CAROUSELS['BB_Venue_Sun_Masquerade'] = [slide(venue_inner, p, 1, 1, single=True)]

# 4) REFERRAL · SUNDAY DINNER · Black&Gold · 5 slides
p = palstyle(PAL['blackgold'])
CAROUSELS['BB_Caro_Sun_SundayDinner'] = [
 slide('<div class="mid"><div class="script">Look around the table today</div>'
       '<div class="h1">EVERY PARTY STARTS AT <em>SUNDAY DINNER.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody announces<br>a baby shower.<br><em>A birthday. A quince.</em></div>'
       '<div class="sup">The plans start before the plates are cleared. That is your moment.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book rentals or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">PASS THE PLATES.<br><em>DROP OUR NAME.</em></div>'
       '<div class="sup">No limit on referrals. <b>Paid after their event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE <em>FAMILY GROUP CHAT.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 20 NIGHTS · Purple/Gold · 4 slides
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Sun_20Nights'] = [
 slide('<div class="mid"><div class="script">Do the math tonight</div>'
       '<div class="h1">20 NIGHTS LEFT. <em>ZERO</em> EXCUSES.</div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Oct 17. Oct 24.<br><em>Then Halloween takes<br>Saturday night itself.</em></div>'
       '<div class="sup">Three Saturdays stand between you and the 31st.</div></div>', p, 2, 4, ghost='20'),
 slide('<div class="mid"><div class="giant">20</div>'
       '<div class="sup"><b>nights to claim your date:</b> tables, chairs and the party room go to whoever calls first.</div></div>', p, 3, 4),
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
            stem = name if n == 1 else f'{name}_{i+1:02d}'
            tmp = str(OUT/f'{stem}.2x.png')
            els.nth(i).screenshot(path=tmp)
            Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/f'{stem}.png')
            pathlib.Path(tmp).unlink()
        print('done', name, n, 'slides')
    b.close()
