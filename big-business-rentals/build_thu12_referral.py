"""Thursday Nov 12 1pm REFERRAL FLYER (weekly promotion, Flyer 2026): CATERERS (profession run: ..., HairStylist,
EventCoordinator, Caterer). Playbook framing: lead with the client's problem the pro solves; the up-to-$100 is a thank-you
after the event; fine print verbatim. Services only. Deep plum + gold. Feed 4:5 + story 9:16."""
import flyer2026 as F
args = dict(kicker='Caterers · Las Vegas',
            headline_html="You bring the food. Who brings the <em>tables?</em>",
            steps=['Send them our way with their date and headcount', 'We deliver and pick up. Setup crews available', 'Your thank-you is paid after their event'],
            bg='radial-gradient(120% 80% at 0% 0%,#4a1d5e 0%,#2a1038 50%,#12061a 100%)',
            glow='radial-gradient(55% 40% at 100% 25%,rgba(229,184,75,.30),rgba(229,184,75,0))',
            sub='Point your clients to us for tables, chairs, tents and setup crews.',
            tags=['Tables + chairs', 'Tents', 'Setup + teardown crews'])
print(F.referral('BB26_Referral_Thu12', **args))
print(F.referral('BB26_Referral_Thu12_Story', size=(1080, 1920), **args))
