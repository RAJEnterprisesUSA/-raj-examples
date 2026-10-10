import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
 'cream': dict(bg="radial-gradient(circle at 30% 18%, #faf3e3 0%, #f4ead6 45%, #e7d9bc 100%)",
   ink="#241a35", body="#4a3c28", script="#9a6f20", gold1="#c89a3c", gold2="#8a6a1c",
   frame="#a07c2c", soft="#5c4b2e", grainmode="multiply", vig="rgba(120,95,40,.16)",
   ghost="rgba(160,124,44,.25)", barbg="rgba(160,124,44,.25)"),
 'purple': dict(bg="radial-gradient(circle at 50% 28%, #3a1a5e 0%, #2c1247 55%, #150826 100%)",
   ink="#f2ecdd", body="#d8ceb6", script="#cbb2e2", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bfa9d8", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.22)", barbg="rgba(229,184,75,.25)"),
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

p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Wed_TrashMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.24</div>'
       '<div class="h1">NOBODY PLANS FOR <em>TRASH.</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">The party is great<br>until hour three.<br><em>Then the cups pile up.</em></div>'
       '<div class="sup">One overflowing bin can wreck a whole setup. The math is easy.</div></div>', p, 2, 6, ghost='24'),
 slide('<div class="mid"><div class="giant">1 BIN</div>'
       '<div class="sup"><b>per 25 guests.</b> Two bins minimum for any party, one near the food, one near the drinks.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:220px">2 BAGS</div>'
       '<div class="sup"><b>per bin, minimum.</b> Doubled up so nothing leaks when you carry it out.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">THE PRO MOVE:<br><em>SWAP AT 2/3 FULL.</em></div>'
       '<div class="sup">Never let a bin overflow. Pull the bag early, <b>and the party never looks messy.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS ON <em>CLEANUP CREW.</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Wed_WeekendBack'] = [
 slide('<div class="mid"><div class="script">Be honest</div>'
       '<div class="h1">WHAT DOES YOUR PARTY <em>WEEKEND</em> LOOK LIKE?</div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Friday: hauling.<br>Saturday: sweating.<br><em>Sunday: returns.</em></div>'
       '<div class="sup">That is three days spent on one afternoon.</div></div>', p, 2, 5, ghost='3'),
 slide('<div class="mid"><div class="giant">0</div>'
       '<div class="sup"><b>trips to pick anything up.</b> Tables, chairs and linens are delivered, set up and collected by us.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOUR ONLY JOB:<br><em>HOST.</em></div>'
       '<div class="sup">You get the whole weekend back, <b>minus the two hours you spend enjoying your own party.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       + cta_block() + '</div>', p, 5, 5),
]

p = palstyle(PAL['purple'])
CAROUSELS['BB_Caro_Wed_GetPaid'] = [
 slide('<div class="mid"><div class="script">Your new side gig</div>'
       '<div class="h1">GET PAID TO BE <em>POPULAR.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">You already know<br>everybody.<br><em>Make it official.</em></div>'
       '<div class="sup">Our referral program pays you for introductions.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="h2">THEY BOOK,<br><em>THEY DROP YOUR NAME.</em></div>'
       '<div class="sup">Tables, chairs or the venue, <b>any booking counts.</b></div></div>', p, 3, 5),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> paid after their event wraps. No limit on how many people you send.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE FRIEND WHO <em>KNOWS EVERYBODY.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Wed_24Nights'] = [
 slide('<div class="mid"><div class="script">check the calendar</div>'
       '<div class="h1">HALLOWEEN LANDS ON A <em>SATURDAY.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">24 nights out.<br><em>Four party Saturdays</em><br>left in October.</div>'
       '<div class="sup">And the last one IS the party. Biggest Halloween weekend in years.</div></div>', p, 2, 4, ghost='24'),
 slide('<div class="mid"><div class="giant">24</div>'
       '<div class="sup"><b>nights to lock it in:</b> tables, chairs and the party room, one call before the Saturdays sell out.</div></div>', p, 3, 4),
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
