"""Pad 1080x1350 cards onto a 1080x1920 story canvas.

Instagram zoom-crops any non-9:16 image posted as a story, cutting off the
card's left and right edges. This renders a true 9:16 version: the card sits
centered at full width and the top/bottom pads are edge-smeared from the
card's first and last pixel rows, so gradients continue seamlessly. The
1350px card lands inside the story safe zone (IG UI covers ~150px top,
~250px bottom).

Output: big-business-rentals/story9/<same basename>.png
Queued IG story posts are re-pointed at these via build_restory_ig.py.
"""
import pathlib
from PIL import Image

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
OUT = BASE / 'story9'
OUT.mkdir(exist_ok=True)

W, H, CH = 1080, 1920, 1350
PAD_TOP = (H - CH) // 2          # 285
PAD_BOT = H - CH - PAD_TOP       # 285

SOURCES = (
    sorted((BASE / 'daily-posts/week5').glob('BB_Caro_*.png')) +
    [BASE / 'examples/EX_Carousel_1.png', BASE / 'examples/EX_Carousel_2.png',
     BASE / 'examples/EX_Carousel_3.png',
     BASE / 'venue/BB_Venue_Tue_PlanB.png', BASE / 'venue/BB_Venue_Wed_OnePrice.png']
)

for src in SOURCES:
    if not src.exists():
        print('missing', src); continue
    im = Image.open(src).convert('RGB')
    if im.size != (W, CH):
        im = im.resize((W, CH), Image.LANCZOS)
    canvas = Image.new('RGB', (W, H))
    top = im.crop((0, 0, W, 1)).resize((W, PAD_TOP))
    bot = im.crop((0, CH - 1, W, CH)).resize((W, PAD_BOT))
    canvas.paste(top, (0, 0))
    canvas.paste(im, (0, PAD_TOP))
    canvas.paste(bot, (0, PAD_TOP + CH))
    canvas.save(OUT / src.name)
    print('padded', src.name)
print('done ->', OUT)
