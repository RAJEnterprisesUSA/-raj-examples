"""Saturday Nov 21 PRICE LIST (weekly promotion, 1pm, FB feed 4:5 + IG Story 9:16), Flyer 2026, deep teal + gold.
New angle this week: drop-off vs full-service, who sets up the tables. Prices from the owner's price card only
($2 chair, $10 6 ft table, $22 table + 6 chairs, full-service from $265). Earlier price lists: Oct 31 (plain list), Nov 7/14 (Thanksgiving by headcount).
Includes an overflow QA pass (element boxes vs. the card) because there is no image viewer in unattended runs."""
import json
import flyer2026 as F
from playwright.sync_api import sync_playwright
from PIL import Image

QA = {}


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
                  items: [].concat(r('.kick'), r('.h1'), r('.tile'), r('.lbl'), r('.num'), r('.tag'), r('.note'), r('.contact'))}
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

A = dict(kicker='Real prices · Las Vegas',
         headline_html="Who sets up the tables, <em>you or us?</em>",
         tiles=[('Folding chair', '$2', ''), ('6 ft rectangle table', '$10', ''),
                ('Table + 6 chairs', '$22', 'you set up'), ('Full-service from', '$265', 'we set up')],
         note_html=("<b>Drop-off:</b> delivered and picked up, you set up. Delivery is quoted with your order. "
                    "<b>Full&#8209;service:</b> we set up and break down."),
         bg='radial-gradient(120% 80% at 0% 0%,#0f4f52 0%,#0a2c33 50%,#071318 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.30),rgba(229,184,75,0))',
         chip='Real prices')

if __name__ == '__main__':
    print(F.price_card('BB26_PriceList_Sat21', **A))
    print(F.price_card('BB26_PriceList_Sat21_Story', size=(1080, 1920), **A))
    print(json.dumps(QA, indent=1))
