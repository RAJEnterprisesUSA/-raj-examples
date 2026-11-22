"""Sunday Nov 22 HOLIDAY BOOKING FLYER (weekly promotion, 1pm): FB feed (4:5) + IG Story (9:16), Flyer 2026, deep wine + gold.
New angle vs Nov 1 (November starts today, copper) and Nov 15 (only three Saturdays, pine green, set price tiles):
a day COUNT from today to each pre-Christmas Saturday. Counts computed with python from 2026-11-22 (13, 20, 27).
Prices only from the owner's card ($2 chair, $10 6 ft table, $22 table + 6 chairs, full-service from $265). No scarcity claims.
Includes an overflow QA pass because there is no image viewer in unattended runs."""
import json
import datetime as dt
import flyer2026 as F
from playwright.sync_api import sync_playwright
from PIL import Image

QA = {}
today = dt.date(2026, 11, 22)
days = [(dt.date(2026, 12, d) - today).days for d in (5, 12, 19)]
assert days == [13, 20, 27], days
assert all(dt.date(2026, 12, d).weekday() == 5 for d in (5, 12, 19))


def render_qa(name, body, size=(1080, 1350), extra_css=''):
    w, h = size
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{F.CSS}{extra_css}</style></head>"
            f"<body style='--w:{w}px;--h:{h}px'><div class='card'>{body}<div class='grain'></div></div></body></html>")
    f = F.OUT / f'{name}.html'
    f.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=F.CHROME)
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
        errs = []
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.goto('file://' + str(f))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.wait_for_timeout(500)
        QA[name] = pg.evaluate("""() => {
          const r = s => [...document.querySelectorAll(s)].map(e => {const b = e.getBoundingClientRect(); return [s, Math.round(b.left), Math.round(b.top), Math.round(b.right), Math.round(b.bottom), e.scrollWidth > e.clientWidth + 1 ? 'OVERFLOW_X' : '']});
          const col = document.querySelector('.col').getBoundingClientRect();
          return {col: [col.left, col.top, col.right, col.bottom],
                  colScroll: [document.querySelector('.col').scrollHeight, document.querySelector('.col').clientHeight],
                  items: [].concat(r('.kick'), r('.h1'), r('.dates .chip'), r('.tile'), r('.num'), r('.ask'), r('.note'), r('.contact'))}
        }""")
        QA[name]['console_errors'] = errs
        tmp = F.OUT / f'{name}.2x.png'
        pg.screenshot(path=str(tmp))
        b.close()
    Image.open(tmp).resize((w, h), Image.LANCZOS).save(F.OUT / f'{name}.png')
    tmp.unlink()
    f.unlink()
    return F.OUT / f'{name}.png'


F.render = render_qa

A = dict(kicker='Days until each pre-Christmas Saturday',
         headline_html="Your holiday party is <em>13, 20 or 27</em> days away.",
         date_chips=['Chair $2', '6 ft table $10', 'Table + 6 chairs $22'],
         tiles=[('Sat · Dec 5', '13', 'days from today'), ('Sat · Dec 12', '20', 'days from today'),
                ('Sat · Dec 19', '27', 'last one before Christmas')],
         ask_html="Pick your <em>Saturday.</em> Message us the date and headcount.",
         note_html="<b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order. Want us to set up too? Full-service starts at $265.",
         bg='radial-gradient(120% 80% at 0% 0%,#6a1f33 0%,#3a0f1d 50%,#14060b 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.30),rgba(229,184,75,0))',
         chip='Holiday bookings')

if __name__ == '__main__':
    print(F.holiday('BB26_Holiday_Sun22', **A))
    print(F.holiday('BB26_Holiday_Sun22_Story', size=(1080, 1920), **A))
    print(json.dumps(QA, indent=1))
