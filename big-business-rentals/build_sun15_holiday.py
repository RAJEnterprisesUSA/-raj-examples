"""Sunday Nov 15 HOLIDAY BOOKING FLYER (weekly promotions, 1pm): FB feed (4:5) + IG Story (9:16), Flyer 2026, pine green.
TRUE calendar facts only: the three Saturdays before Christmas are Dec 5, 12, 19 (checked with python). Owner-approved
price math (6 sets $132 seats 36; 10 sets $220 seats 60; full-service from $265). No scarcity claims beyond the calendar."""
import flyer2026 as F
A = dict(kicker='December holiday parties · Las Vegas',
         headline_html="Only three Saturdays before <em>Christmas.</em>",
         date_chips=['Sat · Dec 5', 'Sat · Dec 12', 'Sat · Dec 19'],
         tiles=[('36 guests', '$132', '6 tables + 36 chairs'), ('60 guests', '$220', '10 tables + 60 chairs'), ('Full-service', '$265', 'from · we set up')],
         ask_html="Message us your <em>date</em> and headcount.",
         note_html="<b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order.",
         bg='radial-gradient(120% 80% at 0% 0%,#1d5a3a 0%,#0f3322 50%,#06140d 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.32),rgba(229,184,75,0))',
         chip='Holiday bookings')
if __name__ == '__main__':
    print(F.holiday('BB26_Holiday_Sun15', **A))
    print(F.holiday('BB26_Holiday_Sun15_Story', size=(1080, 1920), **A))
