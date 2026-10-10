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
 'navy': dict(bg="radial-gradient(circle at 46% 20%, #1d2c52 0%, #15203e 50%, #0a1024 100%)",
   ink="#f1edde", body="#ccd2e4", script="#9fb6e8", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#a9b6d4", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'blackgold': dict(bg="radial-gradient(circle at 48% 22%, #2e2a20 0%, #23201a 50%, #121009 100%)",
   ink="#f4eedb", body="#d8d0ba", script="#d8bd7e", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bdb294", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
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

# 1) TIP No.26 · CHAIR MATH · Daylight Cream · 6 slides · chat CTA
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Fri_ChairMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.26</div>'
       '<div class="h1">HOW MANY <em>CHAIRS</em> DO YOU ACTUALLY NEED?</div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Guest list says 30.<br><em>Thirty chairs, right?</em><br>Wrong.</div>'
       '<div class="sup">Two small rules save every host.</div></div>', p, 2, 6, ghost='26'),
 slide('<div class="mid"><div class="giant" style="font-size:240px">+10%</div>'
       '<div class="sup"><b>for the extras.</b> Plus-ones, neighbors and the friends your friends bring.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:220px">KIDS = 1</div>'
       '<div class="sup"><b>kids count as full seats.</b> Lap seating lasts about ten minutes.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">30 GUESTS =<br><em>33 CHAIRS. CALL IT 35.</em></div>'
       '<div class="sup">Round up. An empty chair is cheap, <b>a standing guest is not.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:56px">CHAT WITH US AT<br>'
       '<em style="font-size:46px">BIGBUSINESSPARTYRENTALS.COM</em><br>FOR AN INSTANT COUNT.</div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · FRIDAY SCRAMBLE · Midnight Navy · 5 slides
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Fri_Scramble'] = [
 slide('<div class="mid"><div class="script">It is Friday and</div>'
       '<div class="h1">THE PARTY IS TOMORROW. <em>NO TABLES YET.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">It happens every<br>Friday in Vegas.<br><em>Somebody counts chairs<br>and panics.</em></div>'
       '<div class="sup">Here is the unpanic button.</div></div>', p, 2, 5, ghost='!'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">1 CALL</div>'
       '<div class="sup"><b>tables, chairs and linens,</b> delivered and set up around your schedule.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">PANIC AT 9AM.<br><em>HANDLED BY NOON.</em></div>'
       '<div class="sup">You go back to the playlist, <b>we handle the heavy part.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) VENUE · TONIGHT NEEDS AN AFTERPARTY · Black&Gold · single card
p = palstyle(PAL['blackgold'])
venue_inner = (
 '<div class="mid"><div class="script">The whole city is out tonight</div>'
 '<div class="h1" style="font-size:112px">WHERE IS EVERYBODY GOING <em>AFTER?</em></div>'
 '<div class="sup" style="margin-top:34px"><b>Private venue · seats 40 · holds 80 standing.</b><br>'
 '3 hours $625 · up to 25 guests.<br>4 hours $800 · up to 40 guests.<br>Tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:30px;color:var(--gold1)"><b>Comment VENUE and we will DM you open dates this weekend.</b></div></div>')
CAROUSELS['BB_Venue_Fri_After'] = [slide(venue_inner, p, 1, 1, single=True)]

# 4) REFERRAL · FINDER'S FEE · Emerald · 5 slides
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Fri_FindersFee'] = [
 slide('<div class="mid"><div class="script">New hustle unlocked</div>'
       '<div class="h1">TALKING ABOUT PARTIES <em>PAYS</em> NOW.</div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Somebody out tonight<br>is already planning<br><em>their next event.</em></div>'
       '<div class="sup">You know exactly who. That is your finder\'s fee walking around.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book tables, chairs or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">MENTION US.<br><em>GET PAID.</em></div>'
       '<div class="sup">That is the whole job. <b>No limit on how many people you send.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE FRIEND WHO <em>KNOWS EVERYBODY.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 22 NIGHTS / 4 SATURDAYS · Halloween · 4 slides
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Fri_22Nights'] = [
 slide('<div class="mid"><div class="script">Do the math, Vegas</div>'
       '<div class="h1">4 SATURDAYS LEFT. ONE IS <em>HALLOWEEN.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">22 nights out.<br><em>The good dates<br>go first.</em></div>'
       '<div class="sup">And the biggest one lands on Saturday, October 31.</div></div>', p, 2, 4, ghost='22'),
 slide('<div class="mid"><div class="giant">22</div>'
       '<div class="sup"><b>nights to lock yours in:</b> tables, chairs and the party room before the calendar fills.</div></div>', p, 3, 4),
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
