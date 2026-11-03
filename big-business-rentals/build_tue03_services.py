"""Tuesday Nov 3 1pm SERVICES FLYER (owner Nov 2: "we are not promoting the venue anymore, only our services" and
"generate pictures to replace the venue photo"). Flyer 2026 photo-card layout. Fresh HF Z-Image setups (no people, no
text): feed = holiday dinner under a frame tent (seed 928822), story = December backyard party (seed 689750).
Real prices only: $22 table + 6 chairs ($3.67 a seated guest, owner-approved), full-service from $265, delivery quoted."""
import flyer2026 as F
ARGS = dict(kicker='Thanksgiving · Friendsgiving · December',
            headline_html="Host the <em>holidays.</em> We bring the seating.",
            tiles=[('Table + 6 chairs', '$22', '$3.67 a seated guest'),
                   ('Full-service setup', 'from $265', 'we set up and break down')],
            chips=['Delivered + picked up', 'Tents + tent setup', 'Delivery quoted with your order'],
            ask_html="Message us your <em>date</em> and headcount.",
            bg='radial-gradient(120% 80% at 0% 0%,#5a1f2e 0%,#2e1019 50%,#14070b 100%)',
            glow='radial-gradient(55% 40% at 100% 30%,rgba(229,184,75,.30),rgba(229,184,75,0))',
            top_chip='Holiday rentals', photo_chip='Setup inspo')
print(F.venue_holiday('BB26_Services_Tue03', 'inspo/setup_holiday_tent.png', pos='center 50%', **ARGS))
print(F.venue_holiday('BB26_Services_Tue03_Story', 'inspo/setup_december_yard.png', size=(1080, 1920), pos='center 60%', **ARGS))
