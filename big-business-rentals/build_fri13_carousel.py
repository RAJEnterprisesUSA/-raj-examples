"""Friday Nov 13 SAVE-WORTHY CAROUSEL (weekly promotions, 1pm): "3 ways to seat 24 for Thanksgiving", 6 slides, Flyer 2026.
IG feed carousel + FB album. Built only from the owner's price card: table + 6 chairs $22 (seats 6: 3 per long side),
4 sets $88 seats 24, full-service from $265. Deep burgundy + gold. UPGRADE: drawn floor-plan diagrams on the layout slides."""
import flyer2026 as F

N = 6
BG = ("<div class='bg' style='background:radial-gradient(120% 80% at 0% 0%,#5e1d2f 0%,#36121c 50%,#1a0a0f 100%)'></div>"
      "<div class='bg' style='background:radial-gradient(55% 40% at 100% 35%,rgba(229,184,75,.26),rgba(229,184,75,0))'></div>")
CSS = """.prog{position:absolute;left:56px;right:56px;top:128px;height:6px;border-radius:3px;background:rgba(255,255,255,.18)}
.prog i{display:block;height:100%;border-radius:3px;background:#E5B84B}
.cnt{position:absolute;right:56px;top:146px;font-family:'Inter';font-weight:800;font-size:22px;letter-spacing:.1em;color:#E5B84B}
.sw{position:absolute;right:56px;bottom:232px;font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.14em;color:#E5B84B}
.blk{position:absolute;left:56px;right:56px;top:210px}
.kick{font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#E5B84B;margin-bottom:18px}
.body{font-size:40px;line-height:1.4;font-weight:500;margin-top:34px;opacity:.95}
.mid{top:380px}
.biglogo{position:absolute;left:50%;top:790px;width:300px;height:300px;margin-left:-150px;filter:drop-shadow(0 20px 40px rgba(0,0,0,.5))}.body b{color:#E5B84B;font-weight:800}
.ghost{position:absolute;right:20px;bottom:180px;font-family:'Brico';font-weight:800;font-size:520px;line-height:.8;color:transparent;
 -webkit-text-stroke:3px rgba(229,184,75,.16);letter-spacing:-.06em}
.mini{position:absolute;left:56px;right:56px;bottom:56px;display:flex;align-items:center;gap:14px;font-size:20px;font-weight:600;opacity:.8}
.mini img{width:44px;height:44px}
table{width:100%;border-collapse:separate;border-spacing:0 12px;margin-top:26px}
td{padding:16px 24px;font-size:32px;font-weight:600;background:rgba(255,255,255,.08);border-top:1px solid rgba(255,255,255,.16);border-bottom:1px solid rgba(255,255,255,.16)}
td:first-child{border-radius:20px 0 0 20px;border-left:1px solid rgba(255,255,255,.16)}td:last-child{border-radius:0 20px 20px 0;border-right:1px solid rgba(255,255,255,.16);text-align:right}
td.g{font-family:'Brico';font-weight:800;font-size:44px;letter-spacing:-.02em}td.c{font-family:'Brico';font-weight:800;font-size:44px;color:#E5B84B}
th{font-family:'Inter';font-weight:800;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#E5B84B;text-align:left;padding:0 24px}
th:last-child{text-align:right}
.plan{position:relative;margin:30px auto 0;width:860px;height:420px;border-radius:28px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16)}
.tb{position:absolute;background:#fbf6ea;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.35)}
.ch{position:absolute;width:26px;height:26px;border-radius:7px;background:#E5B84B}
.kid{background:#7fd3ff}"""

def chrome(i):
    if i == 1: return ""
    return f"<div class='prog'><i style='width:{i/N*100:.1f}%'></i></div><div class='cnt'>{i}/{N}</div>"

def mini():
    return ("<div class='mini'><img src='bb_logo.png'>bigbusinesspartyrentals.com · "
            "@bigbusiness_rentals_events · Las Vegas, NV</div>")

def slide(i, inner, cta=False):
    body = BG + F.top_bar("<div class='chip gold'>Save this</div>") + chrome(i) + inner + (F.contact_bar() if cta else mini())
    return F.render(f'BB26_Carousel_Fri13_{i}', body, (1080, 1350), CSS)


def plan(tables, kids=()):
    """tables: list of (x, y, w, h, horizontal) in plan px; chairs placed 3 per long side of every 6 ft table."""
    h = "<div class='plan'>"
    for (x, y, w, hh, hor) in list(tables) + list(kids):
        kc = " kid" if (x, y, w, hh, hor) in kids else ""
        h += f"<div class='tb' style='left:{x}px;top:{y}px;width:{w}px;height:{hh}px'></div>"
        if hor:
            n = round(w / 180) * 3
            for i in range(n):
                cx = x + (i + 0.5) * w / n - 13
                h += f"<div class='ch{kc}' style='left:{cx:.0f}px;top:{y-34}px'></div><div class='ch{kc}' style='left:{cx:.0f}px;top:{y+hh+8}px'></div>"
        else:
            n = round(hh / 180) * 3
            for i in range(n):
                cy = y + (i + 0.5) * hh / n - 13
                h += f"<div class='ch{kc}' style='left:{x-34}px;top:{cy:.0f}px'></div><div class='ch{kc}' style='left:{x+w+8}px;top:{cy:.0f}px'></div>"
    return h + "</div>"

S = []
S.append(slide(1, "<div class='ghost'>24</div><div class='blk' style='top:300px'><div class='kick'>Thanksgiving seating</div>"
                  "<div class='h1' style='font-size:136px'>3 ways to seat <em>24</em> for Thanksgiving.</div></div>"
                  "<div class='sw'>SWIPE →</div>"))
S.append(slide(2, "<div class='ghost'>4</div><div class='blk mid'><div class='kick'>Start here</div>"
                  "<div class='h1' style='font-size:118px'>24 guests = <em>4</em> table sets.</div>"
                  "<div class='body'>Each set is a 6 ft table and 6 chairs, <b>$22</b>. Four sets is <b>$88</b>. Now pick how you want the room to feel.</div></div>"))
S.append(slide(3, "<div class='blk'><div class='kick'>Layout 1 · One long table</div>"
                  "<div class='h1' style='font-size:84px'>Everybody <em>together.</em></div>"
                  + plan([(70, 190, 720, 46, True)]) +
                  "<div class='body' style='font-size:34px'>Four tables end to end. Best for a family that wants <b>one conversation</b>.</div></div>"))
S.append(slide(4, "<div class='blk'><div class='kick'>Layout 2 · Two long rows</div>"
                  "<div class='h1' style='font-size:84px'>Room to <em>walk.</em></div>"
                  + plan([(250, 90, 360, 46, True), (250, 290, 360, 46, True)]) +
                  "<div class='body' style='font-size:34px'>Two tables end to end, twice. Leaves a lane for <b>plates and the dessert run</b>.</div></div>"))
S.append(slide(5, "<div class='blk'><div class='kick'>Layout 3 · Grown-ups + kids' table</div>"
                  "<div class='h1' style='font-size:84px'>Peace and <em>quiet.</em></div>"
                  + plan([(70, 140, 540, 46, True)], kids=((660, 300, 180, 46, True),)) +
                  "<div class='body' style='font-size:34px'>Three tables long for the grown-ups, one <b>kids' table</b> close enough to keep an eye on.</div></div>"))
S.append(slide(6, "<div class='blk' style='top:200px'><div class='kick'>Save this for Thanksgiving</div>"
                  "<div class='h1' style='font-size:104px'>Pick the layout. We bring the <em>seats.</em></div>"
                  "<div class='body'><b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order. "
                  "Full&#8209;service setup and breakdown starts at $265.</div></div><img class='biglogo' src='bb_logo.png'>", cta=True))

if __name__ == '__main__':
    for p in S: print(p)
