"""Thursday Nov 5 1pm REFERRAL FLYER (weekly promotion, Flyer 2026): EVENT COORDINATORS (profession run continues:
Barber, NailTech, DJ, Bartender, Photographer, PartyPlanner, Teacher, HairStylist, EventCoordinator). Playbook framing:
lead with the client's problem the pro solves, the up-to-$100 is a thank-you after the event, fine print verbatim.
Services only (venue retired Nov 2): tables, chairs, tents, setup crews. Deep navy + gold. Feed 4:5 + story 9:16."""
import flyer2026 as F
args = dict(kicker='Event coordinators · Las Vegas',
            headline_html="Your clients ask you who does the <em>tables.</em>",
            steps=['Send them our way with their date and headcount', 'We deliver and pick up. Setup crews available', 'Your thank-you is paid after their event'],
            bg='radial-gradient(120% 80% at 0% 0%,#1d2f5c 0%,#121c38 50%,#090e1d 100%)',
            glow='radial-gradient(55% 40% at 100% 25%,rgba(229,184,75,.30),rgba(229,184,75,0))',
            sub='Point them to us for tables, chairs, tents and setup crews.',
            tags=['Tables + chairs', 'Tents', 'Setup + teardown crews'])
print(F.referral('BB26_Referral_Thu05', **args))
print(F.referral('BB26_Referral_Thu05_Story', size=(1080, 1920), **args))
