"""Friday Oct 30 SAVE-WORTHY CAROUSEL (weekly promotions): the Holiday Seating Cheat Sheet, 6 slides, Flyer 2026.
IG feed carousel + FB album. Real planning guide built only from the owner's price card: table + 6 chairs $22
(seats 6), folding chair $2, full-service from $265. Midnight navy + gold."""
import flyer2026 as F

N = 6
BG = ("<div class='bg' style='background:radial-gradient(120% 80% at 0% 0%,#1d2f5e 0%,#121a36 50%,#0b0f1f 100%)'></div>"
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
th:last-child{text-align:right}"""

def chrome(i):
    if i == 1: return ""
    return f"<div class='prog'><i style='width:{i/N*100:.1f}%'></i></div><div class='cnt'>{i}/{N}</div>"

def mini():
    return ("<div class='mini'><img src='bb_logo.png'>bigbusinesspartyrentals.com · "
            "@bigbusiness_rentals_events · Las Vegas, NV</div>")

def slide(i, inner, cta=False):
    body = BG + F.top_bar("<div class='chip gold'>Save this</div>") + chrome(i) + inner + (F.contact_bar() if cta else mini())
    return F.render(f'BB26_Carousel_Fri30_{i}', body, (1080, 1350), CSS)

S = []
S.append(slide(1, "<div class='ghost'>?</div><div class='blk' style='top:300px'><div class='kick'>Holiday seating cheat sheet</div>"
                  "<div class='h1' style='font-size:136px'>How many tables do you <em>actually</em> need?</div></div>"
                  "<div class='sw'>SWIPE →</div>"))
S.append(slide(2, "<div class='ghost'>6</div><div class='blk mid'><div class='kick'>Start here</div>"
                  "<div class='h1' style='font-size:124px'>One table. Six chairs. <em>Six</em> guests.</div>"
                  "<div class='body'>Take your guest count, divide by six and <b>round up</b>. That is how many table sets you need.</div></div>"))
rows = [(12, 2), (18, 3), (24, 4), (30, 5), (36, 6), (48, 8), (60, 10)]
tr = ''.join(f"<tr><td class='g'>{g}</td><td>{s} tables + {s*6} chairs</td><td class='c'>${s*22}</td></tr>" for g, s in rows)
S.append(slide(3, "<div class='blk'><div class='kick'>The cheat sheet</div>"
                  "<div class='h1' style='font-size:80px'>Guests to <em>tables</em> to total.</div>"
                  f"<table><tr><th>Guests</th><th>You need</th><th>Sets at $22</th></tr>{tr}</table></div>"))
S.append(slide(4, "<div class='ghost'>+</div><div class='blk mid'><div class='kick'>Tip 1</div>"
                  "<div class='h1' style='font-size:124px'>Add a few <em>spare</em> chairs.</div>"
                  "<div class='body'>Somebody always brings a plus-one. Extra folding chairs are <b>$2 each</b>, cheaper than a guest standing all night.</div></div>"))
S.append(slide(5, "<div class='ghost'>3</div><div class='blk mid'><div class='kick'>Tip 2</div>"
                  "<div class='h1' style='font-size:124px'>Leave room to <em>walk.</em></div>"
                  "<div class='body'>Plan about <b>3 feet</b> behind every chair so people can get up, pass plates and squeeze by without a fight.</div></div>"))
S.append(slide(6, "<div class='blk' style='top:200px'><div class='kick'>Save this for the holidays</div>"
                  "<div class='h1' style='font-size:104px'>We bring the <em>seats.</em> You host.</div>"
                  "<div class='body'><b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order. "
                  "Full&#8209;service setup and breakdown starts at $265.</div></div><img class='biglogo' src='bb_logo.png'>", cta=True))

if __name__ == '__main__':
    for p in S: print(p)
