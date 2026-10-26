"""FLYER 2026 design system (owner Oct 26: "upgrade the looks of the promotion flyers ... I need them to
look like it's the year 2026 and an average person did not do them").
Replaces the Flyer 2.0 gold-frame/diamond look for promotions. Principles:
- Full-bleed image or rich gradient, fine grain, no borders or corner ornaments.
- Type: Bricolage Grotesque 800 (tight tracking) for headlines, Instrument Serif italic for one accent
  word, Inter Tight for UI text. Brand gold #E5B84B stays the accent.
- Frosted-glass panels (backdrop blur), pill chips, 32px radii, bento grids for prices.
- Contact bar with a scannable QR code to the website. No em dashes.
Usage: render(name, html_body, size=(1080,1350)) or the ready templates below."""
import glob, pathlib, shutil
from playwright.sync_api import sync_playwright
from PIL import Image
import qrcode

BASE = pathlib.Path(__file__).parent
OUT = BASE/'flyers2026'
OUT.mkdir(exist_ok=True)
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
if not (OUT/'fonts2026').exists(): shutil.copytree(BASE/'assets/fonts2026', OUT/'fonts2026')
shutil.copy(BASE/'assets/bb_logo.png', OUT/'bb_logo.png')
if not (OUT/'qr_site.png').exists():
    q = qrcode.QRCode(border=1, box_size=12); q.add_data('https://bigbusinesspartyrentals.com'); q.make(fit=True)
    q.make_image(fill_color='#120a1c', back_color='white').save(OUT/'qr_site.png')

CSS = """
@font-face{font-family:'Brico';src:url('fonts2026/bricolage-grotesque-latin-800-normal.woff2');font-weight:800}
@font-face{font-family:'Brico';src:url('fonts2026/bricolage-grotesque-latin-700-normal.woff2');font-weight:700}
@font-face{font-family:'Brico';src:url('fonts2026/bricolage-grotesque-latin-500-normal.woff2');font-weight:500}
@font-face{font-family:'Serif';src:url('fonts2026/instrument-serif-latin-400-italic.woff2');font-style:italic}
@font-face{font-family:'Inter';src:url('fonts2026/inter-tight-latin-500-normal.woff2');font-weight:500}
@font-face{font-family:'Inter';src:url('fonts2026/inter-tight-latin-600-normal.woff2');font-weight:600}
@font-face{font-family:'Inter';src:url('fonts2026/inter-tight-latin-800-normal.woff2');font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
:root{--gold:#E5B84B;--ink:#0f0a17;--cream:#fbf6ea}
html,body{width:var(--w);height:var(--h);overflow:hidden;background:var(--ink)}
.card{position:relative;width:var(--w);height:var(--h);overflow:hidden;color:var(--cream);font-family:'Inter';font-weight:500}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,10,23,.55) 0%,rgba(15,10,23,0) 22%,rgba(15,10,23,0) 42%,rgba(15,10,23,.78) 72%,rgba(15,10,23,.96) 100%)}
.grain{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;pointer-events:none;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.1' numOctaves='2' stitchTiles='stitch'/></filter><rect width='240' height='240' filter='url(%23n)'/></svg>")}
.top{position:absolute;left:56px;right:56px;top:52px;display:flex;justify-content:space-between;align-items:center}
.chip{display:inline-flex;align-items:center;gap:12px;height:58px;padding:0 24px;border-radius:999px;
 background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
 font-family:'Inter';font-weight:600;font-size:22px;letter-spacing:.06em;text-transform:uppercase}
.chip img{width:38px;height:38px;border-radius:50%}
.chip.gold{background:var(--gold);color:var(--ink);border:none}
.h1{font-family:'Brico';font-weight:800;letter-spacing:-.035em;line-height:.92}
.h1 em{font-family:'Serif';font-style:italic;font-weight:400;letter-spacing:-.01em;color:var(--gold)}
.glass{border-radius:34px;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.24);
 backdrop-filter:blur(26px) saturate(140%);-webkit-backdrop-filter:blur(26px) saturate(140%)}
.contact{position:absolute;left:56px;right:56px;bottom:52px;height:150px;display:flex;align-items:center;gap:26px;padding:0 26px}
.contact .qr{width:108px;height:108px;border-radius:20px;background:#fff;padding:8px}
.contact .qr img{width:100%;height:100%}
.contact .ph{font-family:'Inter';font-weight:800;font-size:44px;letter-spacing:-.01em}
.contact .ln{font-family:'Inter';font-weight:500;font-size:21px;opacity:.85;margin-top:4px}
.contact .logo{margin-left:auto;width:96px;height:96px}
.scan{font-family:'Inter';font-weight:600;font-size:15px;letter-spacing:.12em;text-transform:uppercase;opacity:.7;margin-top:6px}
"""

def contact_bar():
    return ("<div class='contact glass'><div class='qr'><img src='qr_site.png'></div>"
            "<div><div class='ph'>702-706-8287</div><div class='ln'>bigbusinesspartyrentals.com · @bigbusiness_rentals_events</div>"
            "<div class='scan'>Scan for a quote · Las Vegas, NV</div></div><img class='logo' src='bb_logo.png'></div>")

def top_bar(right_chip):
    return (f"<div class='top'><div class='chip'><img src='bb_logo.png'>Big Business · Las Vegas</div>{right_chip}</div>")

def render(name, body, size=(1080, 1350), extra_css=''):
    w, h = size
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head>"
            f"<body style='--w:{w}px;--h:{h}px'><div class='card'>{body}<div class='grain'></div></div></body></html>")
    f = OUT/f'{name}.html'; f.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
        pg.goto('file://'+str(f)); pg.wait_for_function("document.fonts.status==='loaded'"); pg.wait_for_timeout(500)
        tmp = OUT/f'{name}.2x.png'; pg.screenshot(path=str(tmp)); b.close()
    Image.open(tmp).resize((w, h), Image.LANCZOS).save(OUT/f'{name}.png'); tmp.unlink(); f.unlink()
    return OUT/f'{name}.png'

# ---------- templates ----------
def price_it(name, img, size=(1080, 1350)):
    """Mon PRICE IT: full-bleed AI setup photo, question headline, glass sub-panel, contact bar."""
    shutil.copy(img, OUT/pathlib.Path(img).name)
    tall = size[1] > 1500
    body = (f"<div class='bg' style=\"background-image:url('{pathlib.Path(img).name}')\"></div><div class='shade'></div>"
            + top_bar("<div class='chip gold'>Setup inspo</div>")
            + f"<div style='position:absolute;left:56px;right:56px;bottom:{'440' if tall else '232'}px'>"
              "<div class='h1' style='font-size:118px'>How much would you <em>pay</em> for this setup?</div>"
              "<div class='glass' style='margin-top:30px;padding:24px 30px;font-size:29px;line-height:1.35;display:inline-block'>"
              "The tables, the chairs and the room underneath it: <b style=\"font-weight:800;color:#E5B84B\">that part is us.</b></div></div>"
            + contact_bar())
    return render(name, body, size)

def price_list(name, size=(1080, 1350)):
    """Sat PRICE LIST: bento grid of real prices on a rich gradient."""
    tiles = [('Folding chair', '$2', ''), ('6 ft rectangle table', '$10', ''), ('6 ft round table', '$15', ''),
             ('Table + 6 chairs', '$22', 'seats 6')]
    cells = ''.join(f"<div class='tile glass'><div class='lbl'>{l}</div><div class='num'>{n}</div>"
                    + (f"<div class='tag'>{tg}</div>" if tg else '') + "</div>" for l, n, tg in tiles)
    css = """.bento{position:absolute;left:56px;right:56px;top:470px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
    .tile{position:relative;height:250px;padding:30px 30px}.lbl{font-size:28px;font-weight:600;opacity:.9}
    .num{font-family:'Brico';font-weight:800;font-size:120px;letter-spacing:-.04em;line-height:1;margin-top:18px;color:#fff}
    .tag{position:absolute;top:26px;right:24px;background:#E5B84B;color:#0f0a17;font-weight:800;font-size:17px;letter-spacing:.08em;
    text-transform:uppercase;border-radius:999px;padding:8px 14px}
    .note{position:absolute;left:56px;right:56px;top:1010px;font-size:25px;line-height:1.4;opacity:.92}
    .note b{color:#E5B84B;font-weight:800}"""
    body = ("<div class='bg' style='background:radial-gradient(120% 80% at 15% 0%,#5b2a86 0%,#2a1240 45%,#0f0a17 100%)'></div>"
            "<div class='bg' style='background:radial-gradient(60% 40% at 95% 30%,rgba(229,184,75,.35),rgba(229,184,75,0))'></div>"
            + top_bar("<div class='chip'>Real prices</div>")
            + "<div style='position:absolute;left:56px;right:56px;top:170px'><div class='h1' style='font-size:112px'>Party rentals, <em>priced</em> plainly.</div></div>"
            + f"<div class='bento'>{cells}</div>"
            + "<div class='note'><b>Delivered and picked up.</b> Delivery is quoted with your order. Full-service setup and breakdown from $265.</div>"
            + contact_bar())
    return render(name, body, size, css)

def venue(name, photo, headline_html, size=(1080, 1350)):
    """Tue VENUE FLYER: the REAL room as a rounded photo card, headline, two price tiles, fact chips."""
    shutil.copy(photo, OUT/pathlib.Path(photo).name)
    w, h = size; tall = h > 1500
    ph_h = 560 if tall else 470
    css = f""".photo{{position:absolute;left:56px;right:56px;top:140px;height:{ph_h}px;border-radius:36px;overflow:hidden;
    box-shadow:0 30px 70px rgba(0,0,0,.55);background:url('{pathlib.Path(photo).name}') center 60%/cover}}
    .photo .chip{{position:absolute;left:22px;bottom:22px;background:rgba(15,10,23,.78);border:1px solid rgba(229,184,75,.7);color:#fbf6ea}}
    .photo .chip::before{{content:'';width:12px;height:12px;border-radius:50%;background:#E5B84B}}
    .vh{{position:absolute;left:56px;right:56px;top:{140+ph_h+46}px}}
    .tiles{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:{38 if tall else 30}px}}
    .tile{{padding:24px 28px}}.tile .k{{font-size:24px;font-weight:600;opacity:.9}}
    .tile .v{{font-family:'Brico';font-weight:800;font-size:{100 if tall else 88}px;letter-spacing:-.04em;line-height:1;margin-top:8px}}
    .tile .s{{font-size:21px;opacity:.8;margin-top:6px}}
    .facts{{display:flex;gap:12px;flex-wrap:wrap;margin-top:{28 if tall else 22}px}}
    .facts .chip{{height:50px;font-size:19px}}"""
    if tall:
        css += """/* story safe zone: IG covers ~250px top (profile row) and bottom (reply bar) */
        .top{top:200px}.contact{bottom:240px}
        .stack{position:absolute;left:56px;right:56px;top:290px;bottom:440px;display:flex;flex-direction:column;gap:44px}
        .stack .photo{position:relative;left:auto;right:auto;top:auto;height:auto;flex:1}
        .stack .vh{position:relative;left:auto;right:auto;top:auto}
        .tile{padding:30px 32px}.tile .k{font-size:28px}.tile .s{font-size:24px}
        .facts .chip{height:58px;font-size:22px}"""
    body = ("<div class='bg' style='background:radial-gradient(110% 70% at 0% 0%,#4a1530 0%,#22101f 50%,#0f0a17 100%)'></div>"
            "<div class='bg' style='background:radial-gradient(50% 35% at 100% 55%,rgba(229,184,75,.28),rgba(229,184,75,0))'></div>"
            + top_bar("<div class='chip gold'>Private venue</div>")
            + ("<div class='stack'>" if tall else '')
            + "<div class='photo'><div class='chip'>The real room</div></div>"
            + f"<div class='vh'><div class='h1' style='font-size:{104 if tall else 92}px'>{headline_html}</div>"
              "<div class='tiles'><div class='tile glass'><div class='k'>3 hours</div><div class='v'>$625</div><div class='s'>up to 25 guests</div></div>"
              "<div class='tile glass'><div class='k'>4 hours</div><div class='v'>$800</div><div class='s'>up to 40 guests</div></div></div>"
              "<div class='facts'><div class='chip'>Seats 40</div><div class='chip'>Holds 80 standing</div>"
              "<div class='chip'>Tables, chairs + setup included</div></div></div>"
            + ('</div>' if tall else '')
            + contact_bar())
    return render(name, body, size, css)

def bento_promo(name, chip, headline_html, tiles, note_html, bg, glow, size=(1080, 1350), kicker='', uses=(), extra_css=''):
    """Generic promo: chip, big headline, 2x2 bento of real prices, one note line, contact bar.
    tiles = [(label, number, tag_or_empty)], bg/glow = CSS colors for the gradient."""
    cells = ''.join(f"<div class='tile glass'><div class='lbl'>{l}</div><div class='num'>{n}</div>"
                    + (f"<div class='tag'>{tg}</div>" if tg else '') + "</div>" for l, n, tg in tiles)
    css = """.bento{position:absolute;left:56px;right:56px;top:560px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
    .tile{position:relative;height:206px;padding:26px 30px}.lbl{font-size:27px;font-weight:600;opacity:.92}
    .num{font-family:'Brico';font-weight:800;font-size:100px;letter-spacing:-.04em;line-height:1;margin-top:14px;color:#fff}
    .tag{position:absolute;top:24px;right:22px;background:#E5B84B;color:#0f0a17;font-weight:800;font-size:16px;letter-spacing:.08em;
    text-transform:uppercase;border-radius:999px;padding:8px 14px}
    .kick{font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#E5B84B;margin-bottom:16px}
    .note{position:absolute;left:56px;right:56px;top:1030px;font-size:25px;line-height:1.4;opacity:.94}
    .note b{color:#E5B84B;font-weight:800}
    .uses{position:absolute;left:56px;right:56px;top:440px;display:flex;flex-wrap:wrap;gap:12px}.uses .chip{height:52px;font-size:20px}"""
    body = (f"<div class='bg' style='background:{bg}'></div><div class='bg' style='background:{glow}'></div>"
            + top_bar(f"<div class='chip gold'>{chip}</div>")
            + f"<div style='position:absolute;left:56px;right:56px;top:165px'>{f'<div class=kick>{kicker}</div>' if kicker else ''}"
              f"<div class='h1' style='font-size:98px'>{headline_html}</div></div>"
            + ("<div class='uses'>" + ''.join(f"<div class='chip'>{u}</div>" for u in uses) + "</div>" if uses else '')
            + f"<div class='bento'>{cells}</div><div class='note'>{note_html}</div>" + contact_bar())
    return render(name, body, size, css + extra_css)

def venue_full(name, photo, headline_html, size=(1080, 1350), sub=''):
    """Group VENUE flyer: the REAL room full-bleed, headline over a dark fade, glass price strip, contact bar."""
    shutil.copy(photo, OUT/pathlib.Path(photo).name)
    css = """.vtiles{position:absolute;left:56px;right:56px;bottom:232px;display:grid;grid-template-columns:1fr 1fr;gap:18px}
    .vt{padding:22px 26px}.vt .k{font-size:23px;font-weight:600;opacity:.92}
    .vt .v{font-family:'Brico';font-weight:800;font-size:84px;letter-spacing:-.04em;line-height:1;margin-top:6px}
    .vt .s{font-size:20px;opacity:.85;margin-top:4px}
    .vfacts{position:absolute;left:56px;right:56px;bottom:452px;display:flex;gap:12px;flex-wrap:wrap}.vfacts .chip{height:50px;font-size:19px;background:rgba(15,10,23,.6)}
    .shade2{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,10,23,.9) 0%,rgba(15,10,23,.6) 30%,rgba(15,10,23,.12) 48%,rgba(15,10,23,.8) 66%,rgba(15,10,23,.97) 100%)}"""
    body = (f"<div class='bg' style=\"background-image:url('{pathlib.Path(photo).name}');background-position:40% 60%\"></div><div class='shade2'></div>"
            + top_bar("<div class='chip gold'>Private party room</div>")
            + f"<div style='position:absolute;left:56px;right:56px;top:165px'><div class='h1' style='font-size:120px'>{headline_html}</div>"
              + (f"<div style='margin-top:18px;font-size:34px;font-weight:600'>{sub}</div>" if sub else '') + "</div>"
            + "<div class='vfacts'><div class='chip'>Seats 40</div><div class='chip'>Holds 80 standing</div><div class='chip'>Tables, chairs + setup included</div></div>"
            + "<div class='vtiles'><div class='vt glass'><div class='k'>3 hours</div><div class='v'>$625</div><div class='s'>up to 25 guests</div></div>"
              "<div class='vt glass'><div class='k'>4 hours</div><div class='v'>$800</div><div class='s'>up to 40 guests</div></div></div>"
            + contact_bar())
    return render(name, body, size, css)

def tent(name, img, headline_html, sub, points, note_html, size=(1080, 1350)):
    """Group TENT flyer: AI setup-inspo tent photo full-bleed, ink headline on the sky, glass service points, contact bar.
    No tent prices until the owner supplies them (never invent)."""
    shutil.copy(img, OUT/pathlib.Path(img).name)
    pts = ''.join(f"<div class='pt glass'><div class='n'>{i+1}</div><div class='t'>{a}</div><div class='d'>{b}</div></div>" for i, (a, b) in enumerate(points))
    css = """.tshade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(251,246,234,.55) 0%,rgba(251,246,234,0) 34%,rgba(15,10,23,0) 52%,rgba(15,10,23,.72) 70%,rgba(15,10,23,.96) 100%)}
    .th{position:absolute;left:56px;right:56px;top:150px;color:#1d1424}.th .h1 em{color:#a8741c}
    .th .sb{margin-top:16px;font-size:30px;font-weight:600;color:#3a2a44}
    .top .chip{background:rgba(255,255,255,.72);color:#1d1424;border:1px solid rgba(29,20,36,.14)}.top .chip.gold{background:#1d1424;color:#E5B84B}
    .insp{position:absolute;right:56px;top:560px;background:rgba(15,10,23,.72);border:1px solid rgba(229,184,75,.7)}
    .pts{position:absolute;left:56px;right:56px;bottom:330px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
    .pt{padding:20px 22px;background:rgba(15,10,23,.45)}.pt .n{font-family:'Brico';font-weight:800;font-size:44px;color:#E5B84B;line-height:1}
    .pt .t{font-family:'Brico';font-weight:800;font-size:30px;letter-spacing:-.02em;margin-top:8px}.pt .d{font-size:19px;opacity:.85;margin-top:6px;line-height:1.3}
    .tnote{position:absolute;left:56px;right:56px;bottom:226px;font-size:24px;line-height:1.4}.tnote b{color:#E5B84B;font-weight:800}"""
    body = (f"<div class='bg' style=\"background-image:url('{pathlib.Path(img).name}');background-position:center 70%\"></div><div class='tshade'></div>"
            + top_bar("<div class='chip gold'>Tents + setup</div>")
            + f"<div class='th'><div class='h1' style='font-size:112px'>{headline_html}</div><div class='sb'>{sub}</div></div>"
            + "<div class='chip insp'>Setup inspo</div>"
            + f"<div class='pts'>{pts}</div><div class='tnote'>{note_html}</div>" + contact_bar())
    return render(name, body, size, css)

REFERRAL_FINE = "Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed"

def referral(name, kicker, headline_html, steps, bg, glow, size=(1080, 1350), sub='', tags=()):
    """Thu REFERRAL FLYER: kicker + headline, giant 'up to $100' glass panel, 3 steps, verbatim fine print, contact bar.
    Works at 1080x1350 (feed) and 1080x1920 (story, inside the IG safe zone)."""
    w, h = size; tall = h > 1500
    st = ''.join(f"<div class='st glass'><div class='n'>{i+1}</div><div class='t'>{a}</div></div>" for i, a in enumerate(steps))
    css = f""".col{{position:absolute;left:56px;right:56px;top:{290 if tall else 150}px;bottom:{440 if tall else 232}px;display:flex;flex-direction:column;justify-content:space-between}}
    {'.top{top:200px}.contact{bottom:240px}' if tall else ''}
    .kick{{font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#E5B84B;margin-bottom:14px}}
    .money{{position:relative;padding:{'34px 40px' if tall else '26px 36px'};overflow:hidden}}
    .money .u{{font-size:30px;font-weight:600;opacity:.9}}
    .money .v{{font-family:'Brico';font-weight:800;font-size:{230 if tall else 190}px;letter-spacing:-.05em;line-height:.9;color:#E5B84B}}
    .money .p{{font-size:28px;font-weight:600;margin-top:6px}}
    .money .ghost{{position:absolute;right:-30px;bottom:-70px;font-family:'Brico';font-weight:800;font-size:330px;color:transparent;
      -webkit-text-stroke:2px rgba(229,184,75,.22);letter-spacing:-.06em}}
    .steps{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}}
    .st{{padding:{'22px' if tall else '18px'} 20px}}.st .n{{font-family:'Brico';font-weight:800;font-size:40px;color:#E5B84B;line-height:1}}
    .st .t{{font-size:{24 if tall else 22}px;font-weight:600;line-height:1.25;margin-top:8px}}
    .fine{{font-size:{19 if tall else 17}px;opacity:.75;line-height:1.4;margin-top:14px}}
    .rsub{{font-size:{32 if tall else 28}px;font-weight:600;margin-top:{22 if tall else 16}px;opacity:.92}}
    .rtags{{display:flex;flex-wrap:wrap;gap:10px;margin-top:{26 if tall else 18}px}}.rtags .chip{{height:{54 if tall else 48}px;font-size:{20 if tall else 18}px}}"""
    body = (f"<div class='bg' style='background:{bg}'></div><div class='bg' style='background:{glow}'></div>"
            + top_bar("<div class='chip gold'>Referral reward</div>")
            + f"<div class='col'><div><div class='kick'>{kicker}</div><div class='h1' style='font-size:{104 if tall else 92}px'>{headline_html}</div>"
              + (f"<div class='rsub'>{sub}</div>" if sub else '')
              + ("<div class='rtags'>" + ''.join(f"<div class='chip'>{t}</div>" for t in tags) + "</div>" if tags else '') + "</div>"
              "<div class='money glass'><div class='ghost'>$</div><div class='u'>Up to</div><div class='v'>$100</div>"
              "<div class='p'>for every booking you send our way.</div></div>"
              f"<div><div class='steps'>{st}</div><div class='fine'>{REFERRAL_FINE}</div></div></div>"
            + contact_bar())
    return render(name, body, size, css)

LIGHT_CSS = """.card{color:#1d1424}.chip{background:rgba(255,255,255,.7);border:1px solid rgba(29,20,36,.14);color:#1d1424}
.chip.gold{background:#1d1424;color:#E5B84B}.h1 em{color:#b8862a}.glass{background:rgba(255,255,255,.62);border:1px solid rgba(29,20,36,.12);
box-shadow:0 18px 40px rgba(90,60,20,.12)}.num{color:#1d1424!important}.tag{background:#1d1424!important;color:#E5B84B!important}
.kick{color:#b8862a!important}.note b{color:#9a6b17!important}.grain{opacity:.07}.contact .ln,.scan{opacity:.8}"""

if __name__ == '__main__':
    print(price_it('BB26_PriceIt_HalloweenGala', BASE/'inspo/setup_halloweengala.png'))
    print(price_list('BB26_PriceList_Sample'))
