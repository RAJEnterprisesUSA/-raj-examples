"""Friday Nov 20 SAVE-WORTHY promo (weekly promotions, 1pm): Party Math "How much room does your guest count need?"
Single 1080x1350 image (the queue tool takes one image per post), Flyer 2026 design, Emerald Night palette + gold.
Math: square feet per guest, standing 6, seated 10, seated with a dance floor 15 (rule-of-thumb planning ranges, no prices, no inventory counts)."""
import flyer2026 as F

BG = ("<div class='bg' style='background:radial-gradient(120% 80% at 0% 0%,#14584a 0%,#0b3329 50%,#06201a 100%)'></div>"
      "<div class='bg' style='background:radial-gradient(55% 40% at 100% 30%,rgba(229,184,75,.24),rgba(229,184,75,0))'></div>")
CSS = """.blk{position:absolute;left:56px;right:56px;top:150px}
.kick{font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#E5B84B;margin-bottom:16px}
.sub{font-size:31px;line-height:1.35;font-weight:500;margin-top:22px;opacity:.95}.sub b{color:#E5B84B;font-weight:800}
table{width:100%;border-collapse:separate;border-spacing:0 10px;margin-top:22px}
th{font-family:'Inter';font-weight:800;font-size:18px;letter-spacing:.1em;text-transform:uppercase;color:#E5B84B;text-align:right;padding:0 20px;line-height:1.2}
th:first-child{text-align:left}
td{padding:14px 20px;font-size:30px;font-weight:600;background:rgba(255,255,255,.08);border-top:1px solid rgba(255,255,255,.16);border-bottom:1px solid rgba(255,255,255,.16);text-align:right}
td:first-child{border-radius:20px 0 0 20px;border-left:1px solid rgba(255,255,255,.16);text-align:left;font-family:'Brico';font-weight:800;font-size:40px;color:#E5B84B}
td:last-child{border-radius:0 20px 20px 0;border-right:1px solid rgba(255,255,255,.16)}
td.m{font-family:'Brico';font-weight:800;font-size:38px}
.note{font-size:24px;line-height:1.35;margin-top:14px;opacity:.85}
.ghost{position:absolute;right:10px;top:70px;font-family:'Brico';font-weight:800;font-size:420px;line-height:.8;color:transparent;-webkit-text-stroke:3px rgba(229,184,75,.14);letter-spacing:-.06em}"""

def rows():
    out = ""
    for g in (20, 40, 60, 100):
        out += (f"<tr><td>{g}</td><td class='m'>{g*6:,}</td><td class='m'>{g*10:,}</td><td class='m'>{g*15:,}</td></tr>")
    return out

body = (BG + F.top_bar("<div class='chip gold'>Party math · Save this</div>") + "<div class='ghost'>10</div>"
        "<div class='blk'><div class='kick'>Party math</div>"
        "<div class='h1' style='font-size:106px'>Will 40 people actually <em>fit?</em></div>"
        "<div class='sub'>Plan on about <b>10 sq ft</b> for every seated guest. Standing mingle needs about <b>6</b>. "
        "Add a dance floor and it jumps to <b>15</b>.</div>"
        "<table><tr><th>Guests</th><th>Standing<br>(6 sq ft)</th><th>Seated<br>(10 sq ft)</th><th>Seated + dance<br>(15 sq ft)</th></tr>"
        + rows() + "</table>"
        "<div class='note'>Square feet of floor you need. Tables, chairs and walkways all count. Measure the room, then do the math.</div>"
        "</div>" + F.contact_bar())
if __name__ == '__main__':
    print(F.render('BB26_PartyMath_Fri20', body, (1080, 1350), CSS))
