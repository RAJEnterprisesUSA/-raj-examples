"""Sunday Nov 1 HOLIDAY BOOKING FLYER (weekly promotions): FB feed (4:5) + IG Story (9:16), Flyer 2026, autumn copper.
Psychology playbook: fresh-start framing (Nov 1), TRUE calendar facts only (Thanksgiving Thu Nov 26; pre-Christmas
Saturdays Dec 5, 12, 19, checked with python calendar), owner-approved price math, the single ask. No scarcity claims."""
import flyer2026 as F
A = dict(kicker='November starts today · Las Vegas',
         headline_html="The holidays are for <em>family.</em> We bring the seats.",
         date_chips=['Thanksgiving · Thu Nov 26', 'Friendsgiving weekends', 'Pre-Christmas Saturdays · Dec 5 · 12 · 19'],
         tiles=[('24 guests', '$88', '4 tables + 24 chairs'), ('48 guests', '$176', '8 tables + 48 chairs'), ('Full-service', '$265', 'from · we set up')],
         ask_html="Message us your <em>date</em> and headcount.",
         note_html="<b>Delivered and picked up across Las Vegas.</b> Delivery is quoted with your order.",
         bg='radial-gradient(120% 80% at 0% 0%,#7a3a14 0%,#3b1a0b 50%,#160a05 100%)',
         glow='radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.32),rgba(229,184,75,0))')
if __name__ == '__main__':
    print(F.holiday('BB26_Holiday_Sun01', **A))
    print(F.holiday('BB26_Holiday_Sun01_Story', size=(1080, 1920), **A))
