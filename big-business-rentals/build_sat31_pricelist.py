"""Saturday Oct 31 PRICE LIST (weekly promotions): FB feed (4:5) + IG Story (9:16), Flyer 2026, Velvet Rope burgundy.
Prices from the owner's price card only."""
import flyer2026 as F
A = dict(kicker='Real prices · Las Vegas',
         headline_html="Party rentals, <em>priced</em> plainly.",
         tiles=[('Folding chair', '$2', ''), ('6 ft rectangle table', '$10', ''), ('6 ft round table', '$15', ''), ('Table + 6 chairs', '$22', 'seats 6')],
         note_html="<b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order. Full&#8209;service setup and breakdown starts at $265.",
         bg='radial-gradient(120% 80% at 0% 0%,#6b1d34 0%,#3a0f1f 50%,#170910 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.30),rgba(229,184,75,0))')
if __name__ == '__main__':
    print(F.price_card('BB26_PriceList_Sat31', **A))
    print(F.price_card('BB26_PriceList_Sat31_Story', size=(1080, 1920), **A))
