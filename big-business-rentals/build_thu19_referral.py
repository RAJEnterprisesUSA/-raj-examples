"""Thursday Nov 19 1pm REFERRAL FLYER (weekly promotion, Flyer 2026): FLORISTS (profession run: Barber, NailTech, DJ,
Bartender, Photographer, PartyPlanner, Teacher, HairStylist, EventCoordinator, Caterer, Florist). Lead with the client's
problem the pro already sees; the up-to-$100 is a thank-you after the event; fine print verbatim. Services only.
Deep rose-wine + gold. Feed 4:5 + story 9:16."""
import flyer2026 as F
args = dict(kicker='Florists · Las Vegas',
            headline_html="Every centerpiece needs a <em>table.</em>",
            steps=['Send your clients our way with their date and headcount', 'We deliver and pick up. Setup crews available', 'Your thank-you is paid after their event'],
            bg='radial-gradient(120% 80% at 0% 0%,#5a1d3a 0%,#33102a 50%,#150510 100%)',
            glow='radial-gradient(55% 40% at 100% 25%,rgba(229,184,75,.30),rgba(229,184,75,0))',
            sub='You style the flowers. We bring the tables, chairs, tents and crews.',
            tags=['Tables + chairs', 'Tents', 'Setup + teardown crews'])
print(F.referral('BB26_Referral_Thu19', **args))
print(F.referral('BB26_Referral_Thu19_Story', size=(1080, 1920), **args))
