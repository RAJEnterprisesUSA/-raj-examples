"""GAME-COVER STYLE FLYER (owner Nov 20: "Create me. GTA 6 style flyer. Better than the last one using these two photos for
chairs and tables and a generated photo. For the tents but not with the gta format just a regular picture on the gta flyer").
Look only: black-gutter panel grid, sunset palette, bold slanted title. NO game logo, name, font or artwork (parody the look,
never the brand). Panels: the owner's REAL chairs + real setup photos in an illustrated treatment (gta/gta_art.py), the tent as a
regular AI photo (HF Z-Image seed 376925) with a "Setup inspo · AI" chip. Prices from the owner's card only; tents and crews quoted.
Outputs flyers2026/BB26_GameCover.png (1080x1350) and BB26_GameCover_Story.png (1080x1920). QR verified after render."""
import shutil
import flyer2026 as F

G = F.OUT/'gta'; G.mkdir(exist_ok=True)
for f in ['art_chairs.jpg', 'art_tables.jpg', 'tent_photo.png']: shutil.copy(F.BASE/'gta'/f, G/f)

CSS = """
.cv{position:absolute;inset:0;background:#07050c}
.pn{position:absolute;overflow:hidden;border-radius:6px;background:#1a1024}
.pn .im{position:absolute;inset:0;background-size:cover;background-position:center}
.pn .sun{position:absolute;inset:0;mix-blend-mode:soft-light;
 background:linear-gradient(170deg,rgba(255,60,150,.85) 0%,rgba(255,140,60,.55) 45%,rgba(70,20,140,.75) 100%)}
.pn .edge{position:absolute;inset:0;box-shadow:inset 0 0 0 3px rgba(255,255,255,.9),inset 0 0 60px rgba(10,0,30,.45);border-radius:6px}
.tag{position:absolute;left:18px;bottom:18px;background:#fff;color:#0b0712;font-family:'Brico';font-weight:800;font-size:28px;
 letter-spacing:-.01em;padding:8px 16px 6px;transform:skewX(-8deg);box-shadow:6px 6px 0 #ff3d8b}
.tag.r{left:auto;right:18px}
.ai{position:absolute;right:16px;top:16px;background:rgba(10,6,18,.72);color:#fff;font-family:'Inter';font-weight:600;font-size:17px;
 letter-spacing:.12em;text-transform:uppercase;padding:8px 14px;border-radius:999px;border:1px solid rgba(255,255,255,.35)}
.title{position:absolute;overflow:hidden;border-radius:6px;
 background:linear-gradient(180deg,#2a0b4d 0%,#9b1f7a 38%,#ff4f8b 62%,#ff9a3c 86%,#ffd36b 100%)}
.title .sunball{position:absolute;left:50%;width:420px;height:420px;margin-left:-210px;border-radius:50%;
 background:radial-gradient(circle,#ffe27a 0%,#ff9a3c 55%,rgba(255,79,139,0) 72%);opacity:.85}
.title .stripes{position:absolute;left:0;right:0;height:120px;background:repeating-linear-gradient(180deg,rgba(42,11,77,.55) 0 8px,transparent 8px 22px)}
.palm{position:absolute;bottom:-6px;width:150px;height:260px}
.big{position:absolute;left:0;right:0;text-align:center;font-family:'Brico';font-weight:800;color:#fff;letter-spacing:-.045em;line-height:.86;
 transform:skewX(-9deg);-webkit-text-stroke:5px #0b0712;paint-order:stroke fill;text-shadow:8px 8px 0 #0b0712,14px 14px 0 rgba(255,61,139,.85)}
.sub{position:absolute;left:0;right:0;text-align:center;font-family:'Inter';font-weight:800;color:#0b0712;letter-spacing:.28em;
 text-transform:uppercase}
.sub span{background:#fff;padding:8px 18px;box-shadow:6px 6px 0 #0b0712}
.price{position:absolute;border-radius:6px;background:#0f0a17;border:3px solid #fff;padding:16px 22px;overflow:hidden}
.price .n{font-family:'Brico';font-weight:800;letter-spacing:-.04em;line-height:.9;color:#ffd36b;transform:skewX(-8deg);display:inline-block;
 text-shadow:4px 4px 0 #ff3d8b}
.price .l{font-family:'Inter';font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:#fff;margin-top:6px}
.price.hot{background:linear-gradient(135deg,#ff3d8b,#ff9a3c)}
.price.hot .n{color:#fff;text-shadow:4px 4px 0 #0b0712}.price.hot .l{color:#0b0712}
.foot{position:absolute;left:0;right:0;bottom:0;background:#07050c;display:flex;align-items:center;gap:24px;padding:0 34px}
.foot .qr{background:#fff;border-radius:14px;padding:7px}.foot .qr img{display:block}
.foot .ph{font-family:'Brico';font-weight:800;color:#fff;letter-spacing:-.02em;line-height:1}
.foot .ln{font-family:'Inter';font-weight:600;color:#fff;opacity:.85;margin-top:6px}
.foot .lv{font-family:'Inter';font-weight:800;color:#ff9a3c;letter-spacing:.18em;text-transform:uppercase;margin-top:6px}
.foot .logo{margin-left:auto}
"""

PALM = ("<svg class='palm' viewBox='0 0 150 260' style='{pos}'><path d='M78 258 C 74 190 70 140 76 96' stroke='#1a0726' stroke-width='12' "
        "fill='none' stroke-linecap='round'/><g fill='#1a0726'><path d='M76 96 C 40 70 14 78 0 96 C 30 82 52 88 76 100Z'/>"
        "<path d='M76 96 C 112 64 136 70 150 88 C 120 76 100 84 76 100Z'/><path d='M76 96 C 60 54 34 40 14 44 C 40 52 58 70 72 100Z'/>"
        "<path d='M76 96 C 96 52 122 42 140 46 C 112 54 94 72 80 100Z'/><path d='M76 96 C 76 56 70 30 58 14 C 80 32 84 62 80 100Z'/></g></svg>")

def panel(x, y, w, h, img, tag='', sun=True, ai=False, right=False):
    return (f"<div class='pn' style='left:{x}px;top:{y}px;width:{w}px;height:{h}px'><div class='im' style=\"background-image:url('gta/{img}')\"></div>"
            + ("<div class='sun'></div>" if sun else "") + "<div class='edge'></div>"
            + ("<div class='ai'>Setup inspo · AI</div>" if ai else "")
            + (f"<div class='tag{' r' if right else ''}'>{tag}</div>" if tag else "") + "</div>")

def title(x, y, w, h, fs, subfs):
    return (f"<div class='title' style='left:{x}px;top:{y}px;width:{w}px;height:{h}px'>"
            f"<div class='sunball' style='top:{h*0.30:.0f}px'></div><div class='stripes' style='top:{h*0.58:.0f}px'></div>"
            + PALM.format(pos='left:10px') + PALM.format(pos='right:6px;transform:scaleX(-1)')
            + f"<div class='big' style='top:{h*0.07:.0f}px;font-size:{fs}px'>BIG<br>BUSINESS</div>"
            f"<div class='sub' style='bottom:{h*0.07:.0f}px;font-size:{subfs}px'><span>Party Rentals · Las Vegas</span></div></div>")

def price(x, y, w, h, n, l, nfs, lfs, hot=False):
    return (f"<div class='price{' hot' if hot else ''}' style='left:{x}px;top:{y}px;width:{w}px;height:{h}px'>"
            f"<div class='n' style='font-size:{nfs}px'>{n}</div><div class='l' style='font-size:{lfs}px'>{l}</div></div>")

def foot(h, phs, lns, qr, logo):
    return (f"<div class='foot' style='height:{h}px'><div class='qr'><img src='qr_site.png' style='width:{qr}px;height:{qr}px'></div>"
            f"<div><div class='ph' style='font-size:{phs}px'>702-706-8287</div>"
            f"<div class='ln' style='font-size:{lns}px'>bigbusinesspartyrentals.com · @bigbusiness_rentals_events</div>"
            f"<div class='lv' style='font-size:{lns-2}px'>Las Vegas, NV · Delivered + picked up</div></div>"
            f"<img class='logo' src='bb_logo.png' style='width:{qr}px;height:{qr}px'></div>")

def feed():
    g = 10; W = 1080
    b = "<div class='cv'></div>"
    b += panel(g, g, 640, 440, 'art_chairs.jpg', 'Chairs · $2 each')
    b += panel(g + 640 + g, g, W - 640 - 3*g, 440, 'art_tables.jpg', 'Tables + linens', right=True)
    b += title(g, 440 + 2*g, W - 2*g, 330, 118, 22)
    y3 = 440 + 330 + 3*g
    b += panel(g, y3, 640, 370, 'tent_photo.png', 'Tents + tent setup', sun=False, ai=True)
    px = g + 640 + g; pw = W - px - g; ph = (370 - 2*g) // 3
    b += price(px, y3, pw, ph, '$22', 'Table + 6 chairs', 66, 17, hot=True)
    b += price(px, y3 + ph + g, pw, ph, '$10', '6 ft table', 66, 17)
    b += price(px, y3 + 2*(ph + g), pw, ph, '$265+', 'Full-service setup', 66, 17)
    b += foot(1350 - (y3 + 370 + g), 46, 19, 104, 104)
    return b

def story():
    g = 12; W = 1080
    b = "<div class='cv'></div>"
    b += panel(g, g, W - 2*g, 560, 'art_chairs.jpg', 'Chairs · $2 each')
    y2 = 560 + 2*g
    b += title(g, y2, W - 2*g, 400, 146, 26)
    y3 = y2 + 400 + g
    b += panel(g, y3, 520, 470, 'art_tables.jpg', 'Tables + linens')
    b += panel(g + 520 + g, y3, W - 520 - 3*g, 470, 'tent_photo.png', 'Tents + setup', sun=False, ai=True, right=True)
    y4 = y3 + 470 + g; pw = (W - 4*g) // 3
    b += price(g, y4, pw, 200, '$22', 'Table + 6 chairs', 82, 18, hot=True)
    b += price(2*g + pw, y4, pw, 200, '$10', '6 ft table', 82, 18)
    b += price(3*g + 2*pw, y4, pw, 200, '$265+', 'Full-service setup', 82, 18)
    b += foot(1920 - (y4 + 200 + g), 54, 21, 130, 120)
    return b

if __name__ == '__main__':
    print(F.render('BB26_GameCover', feed(), (1080, 1350), CSS))
    print(F.render('BB26_GameCover_Story', story(), (1080, 1920), CSS))
