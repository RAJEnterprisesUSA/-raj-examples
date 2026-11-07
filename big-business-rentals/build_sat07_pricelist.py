"""Saturday Nov 7 PRICE LIST (weekly promotion, 1pm, FB feed 4:5 + IG Story 9:16), Flyer 2026, autumn copper + gold.
New angle this week: Thanksgiving seating priced by headcount, using the owner-approved derived figures only
($22 set = table + 6 chairs = $3.67 a seated guest; 2 sets $44 / 4 sets $88 / 6 sets $132 / 8 sets $176). Never called a discount."""
import flyer2026 as F
A = dict(kicker='Real prices · Thanksgiving · Las Vegas',
         headline_html="Thanksgiving seating, <em>priced</em> by headcount.",
         tiles=[('12 guests', '$44', '2 sets'), ('24 guests', '$88', '4 sets'), ('36 guests', '$132', '6 sets'), ('48 guests', '$176', '8 sets')],
         note_html="<b>One set = a 6 ft table + 6 chairs, $22 ($3.67 a seated guest).</b> Chairs are $2 each, round tables $15. Delivered and picked up; delivery is quoted with your order. Full&#8209;service setup from $265.",
         bg='radial-gradient(120% 80% at 0% 0%,#7a3a12 0%,#3d1c0a 50%,#170b05 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.32),rgba(229,184,75,0))',
         chip='Real prices')
if __name__ == '__main__':
    print(F.price_card('BB26_PriceList_Sat07', **A))
    print(F.price_card('BB26_PriceList_Sat07_Story', size=(1080, 1920), **A))
