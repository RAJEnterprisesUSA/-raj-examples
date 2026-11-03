"""SERVICES ROTATION: CREW ONLY flyer as a feed + story promo (owner Nov 2: "i dont need one for groups i need those to be
added into the rotation"). Feed 4:5 (Facebook feed) + 9:16 story (Instagram Story), Flyer 2026, deep teal + gold.
No crew prices on file: quoted by crew size, hours and date. No invented claims."""
import flyer2026 as F
args = ('Setup + teardown crew',
  'Already have the tables, chairs or tent? · Las Vegas',
  "Got the gear? We bring the <em>crew.</em>",
  "Setup and teardown hands for the equipment you already have.",
  [('Setup', 'Tables and chairs placed to your layout before guests arrive.'),
   ('Teardown', 'Folded, stacked and cleared after the party.'),
   ('Tents', 'Your tent raised before the party and taken down after.'),
   ('Your place', 'Backyard, hall or community center.')],
  "Message us your <em>date,</em> hours and what you have.",
  "<b>Quoted by crew size, hours and date.</b> Need rentals too? We deliver those.",
  'radial-gradient(120% 80% at 0% 0%,#0f4a4a 0%,#0b2b2e 50%,#061517 100%)',
  'radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.28),rgba(229,184,75,0))')
print(F.services('BB26_CrewOnly', *args))
print(F.services('BB26_CrewOnly_Story', *args, size=(1080, 1920)))
