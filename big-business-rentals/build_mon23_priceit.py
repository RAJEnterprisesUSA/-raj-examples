"""Monday Nov 23 PRICE IT (weekly promotion, 1pm, FB feed + IG feed). Fresh HF Z-Image (fal provider) indoor corporate
holiday dinner in an industrial loft, ten round tables, white folding chairs, seed 417263, 1104x1472
(inspo/setup_corporate_loft.png). No people, no text. Chip carries AI concept art disclosure on screen."""
import pathlib, shutil
import flyer2026 as F
img = F.BASE/'inspo/setup_corporate_loft.png'
shutil.copy(img, F.OUT/img.name)
body = (f"<div class='bg' style=\"background-image:url('{img.name}');background-position:center 55%\"></div><div class='shade'></div>"
        + F.top_bar("<div class='chip gold'>Setup inspo · AI concept art</div>")
        + "<div style='position:absolute;left:56px;right:56px;bottom:232px'>"
          "<div class='h1' style='font-size:118px'>How much would you <em>pay</em> for this setup?</div>"
          "<div class='glass' style='margin-top:30px;padding:24px 30px;font-size:29px;line-height:1.35;display:inline-block'>"
          "A company holiday dinner, round tables and all. The tables and chairs underneath it: <b style=\"font-weight:800;color:#E5B84B\">that part is us.</b></div></div>"
        + F.contact_bar())
print(F.render('BB26_PriceIt_CorporateLoft', body, (1080, 1350)))
