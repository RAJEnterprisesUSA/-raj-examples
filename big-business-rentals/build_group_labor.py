"""Group flyer: LABOR CREW (owner Nov 1: "promotes my labor work setup and tear down for venues that need extra hands").
Flyer 2026, steel blue + gold. No labor prices on file, so it quotes by crew size, hours and date. No invented claims."""
import flyer2026 as F
print(F.services('BB26_Group_LaborCrew', 'Setup + teardown crew',
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
  'radial-gradient(55% 40% at 100% 40%,rgba(229,184,75,.28),rgba(229,184,75,0))'))
