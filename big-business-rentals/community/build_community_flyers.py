"""Community flyers for Facebook groups and Nextdoor (owner Oct 21: "i need flyers and captions to
post in fb groups, marketplace and next door"). Single standalone 4:5 cards: every one carries the
full price or package info plus a large contact block, because group posts get screenshotted and
shared on their own. Prices are the owner's price card only."""
import glob, pathlib, shutil
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE/'community'
CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
if not (OUT/'fonts').exists(): shutil.copytree(BASE/'assets/fonts', OUT/'fonts')
shutil.copy(BASE/'assets/bb_logo.png', OUT/'bb_logo.png')

src = (BASE/'build_mon_carousels.py').read_text()
CSS = src.split('CSS = """')[1].split('"""')[0] + """
.mid{top:130px;bottom:300px}
.script{font-size:52px}
.row{padding:13px 0}
.plist{margin-top:38px;width:100%}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:24px;
  border-bottom:2px dashed var(--frame);padding:16px 0}
.row .n{font-weight:700;font-size:36px;color:var(--ink)}
.row .n small{display:block;font-weight:600;font-size:22px;color:var(--soft);margin-top:4px}
.row .p{font-family:'Archivo Black';font-size:64px;line-height:1;
  background:linear-gradient(180deg,var(--gold1),var(--gold2) 85%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.note{font-weight:600;font-size:28px;color:var(--body);line-height:1.5;margin-top:28px;max-width:900px}
.note b{color:var(--gold2)}
.bigfoot{position:absolute;left:92px;right:92px;bottom:78px;display:flex;align-items:center;gap:26px;
  border-top:2px solid var(--frame);padding-top:26px}
.bigfoot img{width:120px;height:120px}
.bigfoot .ph{font-family:'Archivo Black';font-size:58px;line-height:1;color:var(--gold2)}
.bigfoot .site{font-weight:700;font-size:28px;color:var(--ink);margin-top:8px}
.bigfoot .ig{font-weight:600;font-size:20px;color:var(--soft);margin-top:4px}
"""
t13 = (BASE/'build_tue13_carousels.py').read_text()
m12 = (BASE/'build_mon12_carousels.py').read_text()
ns = {}
exec(t13.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns)
PAL = ns['PAL']
ns2 = {}
exec(m12.split('PAL = ')[1].split('\n\n')[0].join(['PAL = ', '']), ns2)
for k in ('teal', 'halloween', 'cream'): PAL[k] = ns2['PAL'][k]

def palstyle(p):
    return (f"--bg:{p['bg']};--ink:{p['ink']};--body:{p['body']};--script:{p['script']};"
            f"--gold1:{p['gold1']};--gold2:{p['gold2']};--frame:{p['frame']};--soft:{p['soft']};"
            f"--grainmode:{p['grainmode']};--vig:{p['vig']};--ghost:{p['ghost']};--barbg:{p['barbg']}")

def flyer(inner, pal, kick='BIG BUSINESS · LAS VEGAS'):
    return (f'<div class="slide" style="{palstyle(PAL[pal])}">'
            '<div class="grain"></div><div class="vig"></div><div class="frame"></div>'
            '<div class="dia" style="left:29px;top:29px"></div><div class="dia" style="right:29px;top:29px"></div>'
            '<div class="dia" style="left:29px;bottom:29px"></div><div class="dia" style="right:29px;bottom:29px"></div>'
            f'<div class="kick">◆&nbsp; {kick} &nbsp;◆</div>'
            f'<div class="mid">{inner}</div>'
            '<div class="bigfoot"><img src="bb_logo.png"><div><div class="ph">702-706-8287</div>'
            '<div class="site">bigbusinesspartyrentals.com</div>'
            '<div class="ig">@bigbusiness_rentals_events · LAS VEGAS, NV</div></div></div></div>')

def rows(items):
    return '<div class="plist">' + ''.join(
        f'<div class="row"><div class="n">{n}</div><div class="p">{p}</div></div>' for n, p in items) + '</div>'

FLYERS = {
 'BB_Community_PriceList': flyer(
   '<div class="script">Las Vegas party rentals</div>'
   '<div class="h1" style="font-size:84px">TABLES &amp; CHAIRS, <em>DELIVERED.</em></div>'
   + rows([('Folding chair', '$2'), ('6 ft rectangle table', '$10'),
           ('6 ft round table', '$15'), ('Table + 6 chairs set', '$22')]) +
   '<div class="note"><b>Delivered and picked up.</b> Delivery is quoted with your order. '
   'Full-service setup and breakdown available, packages from $265.</div>', 'blackgold'),

 'BB_Community_Venue': flyer(
   '<div class="script">Private party room</div>'
   '<div class="h1" style="font-size:96px">NEED A PLACE FOR THE <em>PARTY?</em></div>'
   + rows([('3 hours<small>up to 25 guests</small>', '$625'),
           ('4 hours<small>up to 40 guests</small>', '$800')]) +
   '<div class="note"><b>Seats 40 · holds 80 standing.</b> Tables, chairs and setup included. '
   'Birthdays, showers, holiday parties and team nights.</div>', 'velvet'),

 'BB_Community_Halloween': flyer(
   '<div class="script">Halloween is a Saturday</div>'
   '<div class="h1" style="font-size:92px">TABLES &amp; CHAIRS FOR THE <em>31ST.</em></div>'
   + rows([('Folding chair', '$2'), ('Table + 6 chairs set', '$22'),
           ('8 sets · seats 48 guests', '$176')]) +
   '<div class="note"><b>Delivered and picked up across Las Vegas.</b> '
   'Call to check your date before the weekend fills up.</div>', 'halloween',
   kick='HALLOWEEN WEEKEND · LAS VEGAS'),

 'BB_Community_Holidays': flyer(
   '<div class="script">Friendsgiving to December</div>'
   '<div class="h1" style="font-size:84px">THE HOLIDAY TABLE FOR <em>48 GUESTS.</em></div>'
   '<div class="giant" style="font-size:230px;margin-top:20px">$176</div>'
   '<div class="note" style="margin-top:10px"><b>8 tables and 48 chairs, delivered and picked up.</b> '
   'Booking November and December now. Full-service setup available, packages from $265.</div>',
   'cream', kick='HOLIDAY SEASON · LAS VEGAS'),

 'BB_Community_MesasSillas': flyer(
   '<div class="script">Renta para fiestas</div>'
   '<div class="h1" style="font-size:84px">MESAS Y SILLAS, <em>A DOMICILIO.</em></div>'
   + rows([('Silla plegable', '$2'), ('Mesa rectangular de 6 ft', '$10'),
           ('Mesa redonda de 6 ft', '$15'), ('Mesa + 6 sillas', '$22')]) +
   '<div class="note"><b>Entregamos y recogemos.</b> El envío se cotiza con tu pedido. '
   'Montaje completo disponible desde $265. Quinceañeras, bautizos, cumpleaños y posadas.</div>',
   'emerald', kick='SE HABLA FIESTA · LAS VEGAS'),
}

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':1080,'height':1400}, device_scale_factor=2)
    for name, html_slide in FLYERS.items():
        f = OUT/f'{name}.html'
        f.write_text("<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"
                     + html_slide + "</body></html>")
        pg.goto('file://'+str(f))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.wait_for_timeout(300)
        tmp = str(OUT/f'{name}.2x.png')
        pg.locator('.slide').first.screenshot(path=tmp)
        Image.open(tmp).resize((1080,1350), Image.LANCZOS).save(OUT/f'{name}.png')
        pathlib.Path(tmp).unlink()
        print('done', name)
    b.close()
