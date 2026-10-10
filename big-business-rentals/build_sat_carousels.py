import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0]

PAL = {
 'teal': dict(bg="radial-gradient(circle at 44% 20%, #10403e 0%, #0b2f2e 50%, #061d1c 100%)",
   ink="#f3eddc", body="#d8dcc6", script="#8fd0c4", gold1="#EFCB7C", gold2="#c07a3e",
   frame="#c07a3e", soft="#a8c4ba", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(214,138,74,.22)", barbg="rgba(214,138,74,.28)"),
 'velvet': dict(bg="radial-gradient(circle at 45% 22%, #5a1a26 0%, #40111b 50%, #230810 100%)",
   ink="#f6ecdd", body="#e4cdbb", script="#e0a9a9", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#cfa9a9", grainmode="overlay", vig="rgba(0,0,0,.52)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
 'purple': dict(bg="radial-gradient(circle at 50% 28%, #3a1a5e 0%, #2c1247 55%, #150826 100%)",
   ink="#f2ecdd", body="#d8ceb6", script="#cbb2e2", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#bfa9d8", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.22)", barbg="rgba(229,184,75,.25)"),
 'navy': dict(bg="radial-gradient(circle at 46% 20%, #1d2c52 0%, #15203e 50%, #0a1024 100%)",
   ink="#f1edde", body="#ccd2e4", script="#9fb6e8", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#a9b6d4", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.2)", barbg="rgba(229,184,75,.25)"),
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

# 1) TIP No.27 · SPACE MATH · Desert Teal · 6 slides
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Sat_SpaceMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.27</div>'
       '<div class="h1">WILL YOUR PARTY ACTUALLY <em>FIT?</em></div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Everything fits<br>in your head.<br><em>Then the tables arrive.</em></div>'
       '<div class="sup">Planners use one simple number.</div></div>', p, 2, 6, ghost='27'),
 slide('<div class="mid"><div class="giant" style="font-size:230px">10 FT²</div>'
       '<div class="sup"><b>per seated guest,</b> the planner rule of thumb. Tables, chairs and walking room included.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="giant" style="font-size:240px">+ DANCE</div>'
       '<div class="sup"><b>add a dance floor zone:</b> roughly 4 square feet per dancer, and not everyone dances at once.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="h2">40 GUESTS =<br><em>ABOUT A 20 BY 20 SPACE.</em></div>'
       '<div class="sup">Backyard, garage or our venue, <b>measure once and relax.</b></div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER SAYS <em>"IT WILL FIT."</em></div>'
       + cta_block() + '</div>', p, 6, 6),
]

# 2) BUSINESS · NO RECOVERY DAY · Velvet Rope · 5 slides · chat CTA
p = palstyle(PAL['velvet'])
CAROUSELS['BB_Caro_Sat_RecoveryDay'] = [
 slide('<div class="mid"><div class="script">Real question</div>'
       '<div class="h1">WHY DOES HOSTING NEED A <em>RECOVERY DAY?</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">You know the host<br>who never sits down<br><em>at their own party.</em></div>'
       '<div class="sup">Hauling, building, sweating, repeating. It does not have to be you.</div></div>', p, 2, 5, ghost='0'),
 slide('<div class="mid"><div class="giant" style="font-size:230px">0 LIFTING</div>'
       '<div class="sup"><b>for you.</b> Tables, chairs and linens delivered, set up and picked up by us.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOU STAY IN<br><em>THE PICTURES.</em></div>'
       '<div class="sup">Host the party, <b>not the warehouse shift.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain" style="font-size:56px">COMMENT <em>"QUOTE"</em> OR CHAT WITH US AT<br>'
       '<em style="font-size:44px">BIGBUSINESSPARTYRENTALS.COM</em></div>'
       + cta_block() + '</div>', p, 5, 5),
]

# 3) VENUE · DECEMBER BOOKS NOW · Purple/Gold · single card
p = palstyle(PAL['purple'])
venue_inner = (
 '<div class="mid"><div class="script">A word to the planners</div>'
 '<div class="h1" style="font-size:106px">DECEMBER PARTIES BOOK IN <em>OCTOBER.</em></div>'
 '<div class="sup" style="margin-top:34px"><b>Holiday dinners, friendsmas, company parties.</b><br>'
 'Private venue · seats 40 · holds 80 standing.<br>3 hours $625 · 4 hours $800 · setup included.</div>'
 '<div class="sup" style="margin-top:30px;color:var(--gold1)"><b>Comment VENUE for open December dates, or chat with us at bigbusinesspartyrentals.com.</b></div></div>')
CAROUSELS['BB_Venue_Sat_December'] = [slide(venue_inner, p, 1, 1, single=True)]

# 4) REFERRAL · WEEKEND EARS · Midnight Navy · 5 slides
p = palstyle(PAL['navy'])
CAROUSELS['BB_Caro_Sat_WeekendEars'] = [
 slide('<div class="mid"><div class="script">Listen closely tonight</div>'
       '<div class="h1">YOU WILL HEAR ABOUT <em>THREE PARTIES</em> THIS WEEKEND.</div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">A birthday. A baby<br>shower. Somebody\'s<br><em>holiday plans.</em></div>'
       '<div class="sup">Every single one needs tables and chairs. Get paid off one of them.</div></div>', p, 2, 5, ghost='3'),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup"><b>up to, per booking,</b> when they book rentals or the venue and drop your name.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">YOUR EARS.<br><em>YOUR MONEY.</em></div>'
       '<div class="sup">No limit on referrals. <b>Paid after their event wraps.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE ONE WHO <em>HEARS EVERYTHING FIRST.</em></div>'
       + cta_block('Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed') + '</div>', p, 5, 5),
]

# 5) COUNTDOWN · 21 NIGHTS · Halloween · 4 slides
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Sat_21Nights'] = [
 slide('<div class="mid"><div class="script">After tonight</div>'
       '<div class="h1">ONLY 3 SATURDAYS STAND BETWEEN YOU AND <em>HALLOWEEN.</em></div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">21 nights out.<br><em>Oct 17. Oct 24.<br>Then the big one.</em></div>'
       '<div class="sup">Halloween lands on the last Saturday itself.</div></div>', p, 2, 4, ghost='21'),
 slide('<div class="mid"><div class="giant">21</div>'
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
