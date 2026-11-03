"""SERVICES ROTATION: LABOR CREW (setup + teardown for venues, banquet halls and planners) as a feed + story promo
(owner Nov 2: "i need those to be added into the rotation"). Same copy as the Nov 1 group flyer. No labor prices on file."""
import flyer2026 as F
args = ('Setup + teardown crew',
  'For venues, banquet halls and planners · Las Vegas',
  "Short on crew? We <em>set up</em> and tear down.",
  "Extra hands for your busy event days.",
  [('Setup', 'Tables, chairs and linens placed to your floor plan.'),
   ('Teardown', 'Folded, stacked and cleared out after the event.'),
   ('Tents', 'Raised before the party, taken down after.'),
   ('Extra hands', 'Add our crew to yours when the calendar stacks up.')],
  "Message us your <em>date,</em> hours and crew size.",
  "<b>Quoted by crew size, hours and date.</b> Need the rentals too? We deliver those.",
  'radial-gradient(120% 80% at 0% 0%,#1f3a52 0%,#13222f 50%,#0a1118 100%)',
  'radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.28),rgba(229,184,75,0))')
print(F.services('BB26_LaborCrew', *args))
print(F.services('BB26_LaborCrew_Story', *args, size=(1080, 1920)))
