import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'purple': dict(bg="radial-gradient(circle at 50% 28%, #3a1a5e 0%, #2c1247 55%, #150826 100%)",
   ink="#f2ecdd", body="#d8ceb6", script="#cbb2e2", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bfa9d8", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.22)", barbg="rgba(229,184,75,.25)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
 'velvet': dict(bg="radial-gradient(circle at 45% 22%, #5a1a26 0%, #40111b 50%, #230810 100%)",
   ink="#f6ecdd", body="#e4cdbb", script="#e0a9a9", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#cfa9a9", grainmode="overlay", vig="rgba(0,0,0,.52)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'teal': dict(bg="radial-gradient(circle at 44% 20%, #10403e 0%, #0b2f2e 50%, #061d1c 100%)",
   ink="#f3eddc", body="#d8dcc6", script="#8fd0c4", gold1="#EFCB7C", gold2="#c07a3e",
   frame="#c07a3e", soft="#a8c4ba", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(214,138,74,.22)", barbg="rgba(214,138,74,.28)"),
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

# 1) TIP No.25 · TABLE MATH · Purple/Gold · 6 slides
p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Thu_TableMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.25</div>'
       '<div class="h1">HOW MANY <em>TABLES</em> DOES YOUR PARTY NEED?</div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Most hosts guess.<br><em>Then half the room<br>stands all night.</em></div>'
       '<div class="sup">There is a number. It takes ten seconds.</div></div>', p, 2, 6, ghost='25'),
 slide('<div class="mid"><div class="giant">8</div>'
       '<div class="sup"><b>guests per 60 inch round table.</b> Guest count divided by 8 equals your tables. 40 guests, 5 tables.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:240px">+2</div>'
       '<div class="sup"><b>the two everyone forgets:</b> one table for the food, one for the gifts. They never make the first count.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">40 GUESTS =<br><em>5 ROUNDS + 2 BANQUETS.</em></div>'
       '<div class="sup">Chairs, linens and delivery included, <b>counted for you in one call.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · LOADED WEEKEND · Emerald · 5 slides
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Thu_Loaded'] = [
 slide('<div class="mid"><div class="script">Check the schedule</div>'
       '<div class="h1">VEGAS, THIS WEEKEND IS <em>LOADED.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Hockey is back tonight.<br>The rodeo is in town.<br><em>Football brunch Sunday.</em></div>'
       '<div class="sup">Somebody in your circle is hosting all three.</div></div>', p, 2, 5, ghost='3'),
 slide('<div class="mid"><div class="giant" style="font-size:220px">1 CALL</div>'
       '<div class="sup"><b>covers the whole weekend:</b> tables, chairs and linens delivered, set up and picked up around your schedule.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOU HOST.<br><em>WE HAUL.</em></div>'
       '<div class="sup">Booked in minutes, <b>done before warmups end.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) REFERRAL · WEEKEND PLUG · Velvet Rope · 5 slides
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Thu_WeekendPlug'] = [
 slide('<div class="mid"><div class="script">Look at your group chat</div>'
       '<div class="h1">EVERYBODY IS PLANNING <em>SOMETHING</em> THIS WEEKEND.</div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Rodeo crews.<br>Watch parties.<br><em>Birthday dinners.</em></div>'
       '<div class="sup">Every single one of them needs tables and chairs.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="h2">SEND THEM OUR WAY.<br><em>THEY DROP YOUR NAME.</em></div>'
       '<div class="sup">Any booking counts, <b>rentals or the venue.</b></div></div>', p, 3, 5),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> paid after their event wraps. Their party. Your payday.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE <em>PLANNER</em> OF YOUR CREW.</div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 4) COUNTDOWN · 23 NIGHTS · Halloween · 4 slides
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Thu_23Nights'] = [
 slide('<div class="mid"><div class="script">tick tock, Vegas</div>'
       '<div class="h1">23 NIGHTS TILL <em>HALLOWEEN.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">Three weekends left.<br><em>The Saturday parties<br>claim dates first.</em></div>'
       '<div class="sup">And the last Saturday IS Halloween night.</div></div>', p, 2, 4, ghost='23'),
 slide('<div class="mid"><div class="giant">23</div>'
       '<div class="sup"><b>nights to lock yours in:</b> tables, chairs and the party room, before the calendar fills.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"SPOOKY"</em> AND WE WILL DM YOU OPEN OCTOBER DATES.</div>'
       + cta_block() + '</div>', p, 4, 4),
]

# 5) VENUE · RODEO WEEKEND · Desert Teal/copper · single card
p = palstyle(PAL['teal'])
venue_inner = (
 '<div class="mid"><div class="script">Rodeo weekend plans?</div>'
 '<div class="h1" style="font-size:108px">THE RODEO <em>SOLD OUT.</em><br>YOUR AFTERPARTY<br>SHOULD NOT.</div>'
 '<div class="sup" style="margin-top:34px"><b>Private venue · seats 40 · holds 80 standing.</b><br>'
 '3 hours $625 · up to 25 guests.<br>4 hours $800 · up to 40 guests.<br>Tables, chairs and setup included.</div>'
 '<div class="sup" style="margin-top:30px;color:var(--gold1)"><b>Comment VENUE and we will DM you open dates this weekend.</b></div></div>')
CAROUSELS['BB_Venue_Thu_SoldOut'] = [slide(venue_inner, p, 1, 1, single=True)]

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
