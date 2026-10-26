"""Monday Oct 26 PRICE IT (weekly promotions: Mon = Price It). Fresh indoor venue-scale Halloween
dinner gala (HF Z-Image, seed 992092). Sub-line changed for the FB/IG charters: no "drop your number",
no "wrong answers" bait; the question stays because people genuinely want to answer it."""
import re, pathlib
src = (pathlib.Path(__file__).parent/'build_priceit.py').read_text()
src = src.replace("Drop your number below. Wrong answers welcome. 👇",
                  "The tables, the chairs and the room underneath it: that part is us.")
src = re.sub(r"JOBS = \[.*?\]\n", 'JOBS = [("setup_halloweengala.png", "BB_PriceIt_HalloweenGala.png")]\n', src, flags=re.S)
exec(compile(src, 'build_priceit_mon26', 'exec'))
