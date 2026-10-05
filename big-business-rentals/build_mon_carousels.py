import glob, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'daily-posts/week5'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]

# palette tokens per carousel
PAL = {
 'cream': dict(bg="radial-gradient(circle at 30% 18%, #faf3e3 0%, #f4ead6 45%, #e7d9bc 100%)",
   ink="#241a35", body="#4a3c28", script="#9a6f20", gold1="#c89a3c", gold2="#8a6a1c",
   frame="#a07c2c", soft="#5c4b2e", grainmode="multiply", vig="rgba(120,95,40,.16)",
   ghost="rgba(160,124,44,.25)", barbg="rgba(160,124,44,.25)"),
 'teal': dict(bg="radial-gradient(circle at 40% 20%, #0d4a4f 0%, #073036 50%, #04272b 100%)",
   ink="#f0ece0", body="#dfe8d9", script="#8fd0c8", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9ec4bd", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(240,164,97,.2)", barbg="rgba(229,184,75,.25)"),
 'emerald': dict(bg="radial-gradient(circle at 42% 18%, #0f3d2e 0%, #0a2e22 48%, #072218 100%)",
   ink="#eef3e4", body="#d9e6c8", script="#9fd4b4", gold1="#EFCB7C", gold2="#B08D3E",
   frame="#B08D3E", soft="#9fb894", grainmode="overlay", vig="rgba(0,0,0,.5)",
   ghost="rgba(229,184,75,.18)", barbg="rgba(229,184,75,.25)"),
 'halloween': dict(bg="radial-gradient(circle at 50% 36%, #241040 0%, #140823 50%, #060309 100%)",
   ink="#f6ecc9", body="#d9c9ef", script="#c9a9f0", gold1="#ffb13d", gold2="#ff8c2e",
   frame="#B08D3E", soft="#b9a8d4", grainmode="overlay", vig="rgba(0,0,0,.55)",
   ghost="rgba(255,140,46,.22)", barbg="rgba(255,140,46,.3)"),
}

CSS = """
@font-face{font-family:'Archivo Black';src:url('fonts/ArchivoBlack.ttf')}
@font-face{font-family:'Playfair';src:url('fonts/Playfair900.ttf');font-weight:900}
@font-face{font-family:'Oswald';src:url('fonts/Oswald600.ttf');font-weight:600}
@font-face{font-family:'Montserrat';src:url('fonts/Mont600.ttf');font-weight:600}
@font-face{font-family:'Montserrat';src:url('fonts/Mont700.ttf');font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#111}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Montserrat';
  color:var(--ink);background:var(--bg)}
.grain{position:absolute;inset:0;opacity:.10;mix-blend-mode:var(--grainmode);
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='300' height='300' filter='url(%23n)' opacity='1'/></svg>")}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%, transparent 55%, var(--vig) 100%)}
.frame{position:absolute;inset:34px;border:2px solid var(--frame)}
.dia{position:absolute;width:12px;height:12px;background:var(--frame);transform:rotate(45deg)}
.ghostn{position:absolute;right:-70px;top:230px;font-family:'Archivo Black';font-size:620px;line-height:1;
  color:transparent;-webkit-text-stroke:3px var(--ghost);letter-spacing:-22px}
.kick{position:absolute;top:84px;left:0;right:0;text-align:center;
  font-family:'Oswald';font-weight:600;font-size:23px;letter-spacing:9px;color:var(--gold2)}
.prog{position:absolute;top:84px;right:92px;font-family:'Oswald';font-weight:600;font-size:24px;
  letter-spacing:3px;color:var(--gold2)}
.bar{position:absolute;top:130px;left:92px;right:92px;height:5px;background:var(--barbg);border-radius:3px}
.bar i{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,var(--gold1),var(--gold2));border-radius:3px}
.mid{position:absolute;left:92px;right:92px;top:0;bottom:0;display:flex;flex-direction:column;
  justify-content:center;align-items:flex-start;text-align:left}
.mid.center{align-items:center;text-align:center}
.script{font-family:'Playfair';font-weight:900;font-style:italic;font-size:64px;color:var(--script);line-height:1.05}
.h1{font-family:'Archivo Black';font-size:124px;line-height:1.02;color:var(--ink);margin-top:14px}
.h1 em{font-style:normal;background:linear-gradient(180deg,var(--gold1),var(--gold2) 80%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.h2{font-family:'Archivo Black';font-size:78px;line-height:1.1;color:var(--ink)}
.h2 em{font-style:normal;background:linear-gradient(180deg,var(--gold1),var(--gold2) 80%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.giant{font-family:'Archivo Black';font-size:300px;line-height:.95;
  background:linear-gradient(180deg,var(--gold1),var(--gold2) 85%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 16px 30px rgba(0,0,0,.25))}
.sup{font-weight:600;font-size:34px;color:var(--body);line-height:1.5;margin-top:34px;max-width:860px}
.sup b{color:var(--gold2)}
.swipe{position:absolute;right:92px;bottom:150px;font-family:'Oswald';font-weight:600;font-size:30px;
  letter-spacing:6px;color:var(--gold2)}
.footS{position:absolute;left:92px;bottom:76px;display:flex;align-items:center;gap:16px;opacity:.92}
.footS img{width:54px;height:54px}
.footS .t{font-weight:600;font-size:17px;color:var(--soft);line-height:1.5}
.footS .t b{color:var(--gold2);font-weight:700}
.ctaMain{font-family:'Archivo Black';font-size:72px;line-height:1.12;color:var(--ink)}
.ctaMain em{font-style:normal;background:linear-gradient(180deg,var(--gold1),var(--gold2) 80%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.ctaBlock{margin-top:70px;display:flex;flex-direction:column;align-items:center;gap:10px}
.ctaBlock img{width:170px;height:170px;margin-bottom:8px}
.ctaBlock .ph{font-family:'Archivo Black';font-size:64px;color:var(--gold2)}
.ctaBlock .site{font-weight:700;font-size:32px;color:var(--ink)}
.ctaBlock .ig{font-weight:600;font-size:24px;color:var(--soft)}
.fine{margin-top:26px;font-weight:600;font-size:17px;color:var(--soft);line-height:1.5;max-width:700px;text-align:center}
"""

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
    bits = frame_bits()
    g = f'<div class="ghostn">{ghost}</div>' if ghost else ''
    kick = '<div class="kick">◆&nbsp; BIG BUSINESS · LAS VEGAS &nbsp;◆</div>'
    p = '' if hook else prog(i, n)
    sw = '<div class="swipe">SWIPE&nbsp;&nbsp;→</div>' if hook else ''
    return f'<div class="slide" style="{pal}">{g}{bits}{kick}{p}{inner}{sw}{foot_small()}</div>'

def palstyle(p):
    return (f"--bg:{p['bg']};--ink:{p['ink']};--body:{p['body']};--script:{p['script']};"
            f"--gold1:{p['gold1']};--gold2:{p['gold2']};--frame:{p['frame']};--soft:{p['soft']};"
            f"--grainmode:{p['grainmode']};--vig:{p['vig']};--ghost:{p['ghost']};--barbg:{p['barbg']}")

CAROUSELS = {}

# ---------- 1 · TIP 22 ICE MATH (cream, 6 slides) ----------
p = palstyle(PAL['cream'])
CAROUSELS['BB_Caro_Mon_IceMath'] = [
 slide('<div class="mid"><div class="script">Party math, tip No.22</div>'
       '<div class="h1">HOW MUCH <em>ICE</em> DO YOU ACTUALLY NEED?</div></div>', p, 1, 6, hook=True),
 slide('<div class="mid"><div class="h2">Most hosts guess.<br><em>Most hosts run out</em><br>by 9pm.</div>'
       '<div class="sup">Ice is the one thing you cannot set up early. Here is the math.</div></div>', p, 2, 6, ghost='ICE'),
 slide('<div class="mid"><div class="giant">2 LBS</div>'
       '<div class="sup"><b>per guest</b> if cans and bottles are riding in a cooler. Cups only? 1 lb each, minimum.</div></div>', p, 3, 6),
 slide('<div class="mid"><div class="h2">HOT NIGHT?<br><em>MAKE IT 3.</em></div>'
       '<div class="sup">This is Vegas. <b>The sun drinks first,</b> and outdoor parties melt a bag before the music starts.</div></div>', p, 4, 6),
 slide('<div class="mid"><div class="script">The cooler count</div>'
       '<div class="h2"><em>100 LBS</em> FOR 50 GUESTS.</div>'
       '<div class="sup">Five 20-lb bags, two big coolers, <b>bought last and kept shaded.</b> That is the whole trick.</div></div>', p, 5, 6),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE FRIEND WHO <em>ALWAYS FORGETS THE ICE.</em></div>'
       '<div class="ctaBlock"><img src="bb_logo.png"><div class="ph">702-706-8287</div>'
       '<div class="site">bigbusinesspartyrentals.com</div>'
       '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div></div>', p, 6, 6),
]

# ---------- 2 · BUSINESS (teal, 5 slides) ----------
p = palstyle(PAL['teal'])
CAROUSELS['BB_Caro_Mon_Handled'] = [
 slide('<div class="mid"><div class="script">Imagine this</div>'
       '<div class="h1">PARTY DAY, <em>ALREADY HANDLED.</em></div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">Hosting usually means<br><em>hauling, unfolding,</em><br>sweating, repeat.</div>'
       '<div class="sup">There is a better division of labor.</div></div>', p, 2, 5, ghost='GO'),
 slide('<div class="mid"><div class="giant" style="font-size:128px">DELIVERED.</div>'
       '<div class="sup">Tables, chairs and linens <b>arrive at your door,</b> matched to your theme and guest count.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="h2">WE SET UP.<br>WE PICK UP.<br><em>YOU NEVER LIFT A THING.</em></div>'
       '<div class="sup">Set while you get dressed, <b>gone when the party ends.</b></div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">COMMENT <em>"QUOTE"</em> AND WE WILL DM YOU A PRICE TODAY.</div>'
       '<div class="ctaBlock"><img src="bb_logo.png"><div class="ph">702-706-8287</div>'
       '<div class="site">bigbusinesspartyrentals.com</div>'
       '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div></div>', p, 5, 5),
]

# ---------- 3 · REFERRAL (emerald, 5 slides) ----------
p = palstyle(PAL['emerald'])
CAROUSELS['BB_Caro_Mon_Referral'] = [
 slide('<div class="mid"><div class="script">No slots, no dice</div>'
       '<div class="h1">THE EASIEST <em>$100</em> IN VEGAS?</div></div>', p, 1, 5, hook=True),
 slide('<div class="mid"><div class="h2">It is not on the<br>casino floor.<br><em>It is in your group chat.</em></div>'
       '<div class="sup">Somebody you know is planning a party right now.</div></div>', p, 2, 5, ghost='$'),
 slide('<div class="mid"><div class="h2">SAY <em>"I KNOW A GUY."</em></div>'
       '<div class="sup">Send them our way and have them <b>drop your name</b> when they book their tables, chairs or the venue.</div></div>', p, 3, 5),
 slide('<div class="mid"><div class="giant">$100</div>'
       '<div class="sup">After their event wraps, <b>you collect.</b> Up to $100 per booking, no limit on referrals.</div></div>', p, 4, 5),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO THE <em>PLUG</em> OF YOUR GROUP CHAT.</div>'
       '<div class="ctaBlock"><img src="bb_logo.png"><div class="ph">702-706-8287</div>'
       '<div class="site">bigbusinesspartyrentals.com</div>'
       '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div>'
       '<div class="fine">Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed</div></div>', p, 5, 5),
]

# ---------- 4 · COUNTDOWN (halloween, 4 slides) ----------
p = palstyle(PAL['halloween'])
CAROUSELS['BB_Caro_Mon_26Nights'] = [
 slide('<div class="mid"><div class="script">candy corn says</div>'
       '<div class="h1"><em>26 NIGHTS</em> TILL HALLOWEEN.</div></div>', p, 1, 4, hook=True),
 slide('<div class="mid"><div class="h2">The good dates and<br>the good chairs<br><em>disappear first.</em></div>'
       '<div class="sup">Spooky season books itself out faster every year.</div></div>', p, 2, 4, ghost='26'),
 slide('<div class="mid"><div class="giant">26</div>'
       '<div class="sup"><b>Lock the date before the glow goes out:</b> tables, chairs and the party room in one call.</div></div>', p, 3, 4),
 slide('<div class="mid center"><div class="ctaMain">SEND THIS TO WHOEVER IS <em>HOSTING HALLOWEEN.</em></div>'
       '<div class="ctaBlock"><img src="bb_logo.png"><div class="ph">702-706-8287</div>'
       '<div class="site">bigbusinesspartyrentals.com</div>'
       '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div></div>', p, 4, 4),
]

# ---------- build + render ----------
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
