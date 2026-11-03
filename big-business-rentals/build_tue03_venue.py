"""Tuesday Nov 3 VENUE FLYER (weekly promotions), holiday edition: FB feed (4:5) + IG Story (9:16). Real room photo,
owner-approved per-guest math ($800 / 40 = $20 a guest, $625 / 25 = $25 a guest), single ask. Emerald + gold."""
import flyer2026 as F
A = dict(photo='inspo/venue_real_room.png', kicker='Thanksgiving · Friendsgiving · December',
  headline_html="Host the <em>holidays.</em> Skip the cleanup.",
  tiles=[('4 hours · up to 40 guests', '$20', 'a guest · $800 total'), ('3 hours · up to 25 guests', '$25', 'a guest · $625 total')],
  chips=['Seats 40', 'Holds 80 standing', 'Tables, chairs + setup included'],
  ask_html="Message us your <em>date</em> and headcount.",
  bg='radial-gradient(120% 80% at 0% 0%,#0f4a3a 0%,#0c2a24 50%,#0b1512 100%)',
  glow='radial-gradient(55% 40% at 100% 45%,rgba(229,184,75,.30),rgba(229,184,75,0))')
if __name__ == '__main__':
    print(F.venue_holiday('BB26_Venue_Tue03', **A))
    print(F.venue_holiday('BB26_Venue_Tue03_Story', size=(1080, 1920), **A))
