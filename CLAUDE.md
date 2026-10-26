# Big Business Party Rentals & Events · Content System Handbook

This repo runs the daily social content system for Big Business Party Rentals And Events
(Las Vegas, NV). Owner: Rashad Johnson. Read this whole file before building anything.
OPERATOR CHARTER (owner-issued Oct 6): big-business-rentals/OPERATOR.md defines the role, mission and
operating standards (growth mission, hooks-first, originality, research and growth-opportunity duties,
Sunday analytics loop, quality checklist, owner authority). It sits ON TOP of this file and changes
nothing in it; where the charter speaks generally (e.g. people in visuals) the specific rules below
still govern (no photos of real people on cards, no people in PRICE IT images) until the owner says
otherwise. Apply the charter in every session.
TIKTOK CHARTER (owner-issued Oct 20, 2026): big-business-rentals/tiktok/CHARTER.md GOVERNS ALL
TIKTOK WORK and overrides every TikTok rule in this file (the 4-posts-a-day cap, the PRICE IT
TikTok pad, "videos -> TikTok" defaults, the phone/contact caption line on TikTok). Summary: the
TikTok posts are built as packages in big-business-rentals/tiktok/packages/ and published THROUGH
BUFFER (owner Oct 20 evening: "bypass the owner publishes . and stick with approve"), but ONLY
after the owner explicitly approves that specific post; never batch-queue TikTok from nightly
builds (the 19 old scheduled TikTok posts were deleted with owner approval Oct 20). AI LABELS
(owner Oct 20 night, "ok add for realistic ai videos", replaces the earlier no-labels rule): every
REALISTIC AI video gets the platform AI label on all four platforms (TikTok toggle + YouTube via
Buffer isAiGenerated; Meta label via the owner in Business Suite); on-screen stamps (AI CONCEPT
ART, AI SKIT) stay too. Drawn rig animation never gets a label.
AI SKIT RULE (owner Oct 20 night, all platforms): every AI skit revolves around the business
(setups, teardowns, tent setups, linens, loading, deliveries) and its main character is always
a Black man or woman, the competent pro; humor from the situation, never identity or stereotype.
UPGRADE RULE (owner Oct 25: "i want to always upgrade something when ever we can"): every build ships
at least one visible production upgrade over the last one (sound, captions, motion, covers, frame rate,
resolution). Log the upgrade with the captions. Upgrade backlog + research: big-business-rentals/UPGRADES.md.
SOUND KIT (free, Oct 25): big-business-rentals/audio/sfx_kit.py (FluidSynth + FluidR3 GM soundfont, MIT)
replaces synth beeps in new renders; install each session: apt-get install -y fluidsynth fluid-soundfont-gm; pip install mido.
EVERYWHERE RULE (owner Oct 24): every Chronicles episode and every trend remix video posts on ALL
FOUR platforms (FB, IG, TikTok, YouTube) with each platform's caption rules; this overrides the
per-platform caps for those two formats.
GUESS THE THEME (owner Oct 26, locked): weekly, clues Wed 1pm + answer Thu 1pm, TikTok + Instagram
only (never Facebook), AI label on, built as a package and queued only after owner approval.
FACEBOOK FEED (owner Oct 26): up to 3 feed posts a day.
WEEKLY PROMOTIONS (owner Oct 26, locked; one a day, built as packages, queued only after owner approval):
Mon PRICE IT (fresh AI setup image, FB feed + IG feed) · Tue VENUE FLYER (FB feed + IG Story) ·
Wed GUESS THE THEME clues (TikTok + IG, 1pm) · Thu REFERRAL FLYER (FB feed + IG Story) + GUESS THE THEME
answer (TikTok + IG, 1pm) · Fri SAVE-WORTHY CAROUSEL (IG feed carousel + FB album) · Sat PRICE LIST
(FB feed + IG Story) · Sun HOLIDAY BOOKING FLYER (FB feed + IG Story). Promo slot 1pm unless noted.
Captions follow each charter (no phone, links, "free" or bait on FB/IG; prices allowed on FB/IG, never TikTok). Max 1 TikTok post a day while median views
are under 100; first
frame = punchline, loops, no phone/prices/"free"/sales lines in TikTok captions.
INSTAGRAM CHARTER (owner-issued Oct 21, 2026): big-business-rentals/instagram/CHARTER.md GOVERNS ALL
INSTAGRAM WORK and overrides every Instagram rule in this file. Summary: 1 Reel a day (8pm, the Big
Business Chronicles are the signature series), new formats as trial reels first (owner posts
them, the API cannot), Stories 2 to 3 a day, max 1 save-worthy carousel a week; no phone, links,
"free" or bait in captions; one keyword line plus max 5 hashtags; pinned comment is a follow
prompt only; account needs the "AI-generated profile" label while it features AI people.
Nothing published, deleted or boosted without the owner's approval of that specific action
(Oct 20: 5 episode captions rewritten, 30 posts deleted with approval). Packages live in
big-business-rentals/instagram/packages/. Never batch-queue Instagram from the nightly build.
YOUTUBE CHARTER (owner-issued Oct 21, 2026): big-business-rentals/youtube/CHARTER.md GOVERNS ALL
YOUTUBE WORK and overrides every YouTube rule in this file. Summary: 1 to 2 Shorts a day, one-gag
skits ~50% (lead format), Chronicles ~35% (playlist "The Big Business Chronicles", end with "next
episode tomorrow"), real moments ~15%; NO health/awareness Shorts (4 pink Shorts deleted with
approval Oct 20); descriptions one line + max 3 hashtags, no phone, URL or "free"; "altered or
synthetic content" disclosure (Buffer isAiGenerated) on realistic AI only; playlist, Related video
and stickers are manual in Studio. Never delete and re-upload a Short. Nothing published, deleted
or changed without the owner's approval of that specific action. Packages live in
big-business-rentals/youtube/packages/. Never batch-queue YouTube from the nightly build.
With all four platforms under their own charters, the old 9-slot nightly build below is RETIRED
as a queueing plan; it stays as reference for rigs, specs and brand facts.
FACEBOOK CHARTER (owner-issued Oct 21, 2026): big-business-rentals/facebook/CHARTER.md GOVERNS ALL
FACEBOOK PAGE WORK and overrides every Facebook rule in this file. Summary: 1 to 2 feed posts a
day, mostly Reels (5pm), one people-centered post a week, Stories 2 to 3 a day max; no links, no
phone, no "free", no engagement bait ("send this to", "comment WORD", "tag", "wrong answers
only") and max 5 hashtags in Facebook captions; every Reel captioned; Meta AI label on
photorealistic AI (Buffer cannot set it, so those go through the owner in Business Suite).
Nothing is published, deleted or boosted on Facebook without the owner's approval of that
specific action (35 old scheduled FB posts deleted with approval Oct 20; 4 pink Stories kept).
Packages live in big-business-rentals/facebook/packages/. Never batch-queue Facebook from the
nightly build.
Everything lives under `big-business-rentals/`. Deeper lore: `big-business-rentals/CAST.md`.
All past captions and rule-change logs: `big-business-rentals/posting_captions.md` (append, never rewrite history).
Research backing the strategy: `reports/Party rental content strategy.md`.

## Non-negotiable brand facts (every deliverable)
- Phone: 702-706-8287 (NEVER 703-786-8369). Website: bigbusinesspartyrentals.com (always included).
- Instagram: @bigbusiness_rentals_events · LAS VEGAS, NV.
- Footer block on every card: logo + phone + site + IG + LAS VEGAS, NV.
- NO em dashes anywhere: chat, captions, designs. Use commas, periods, or " · ".
- STANDARD GRAMMAR ONLY in all copy (owner correction Oct 5): never use slang subject-verb constructions
  like "which one is you". Write "which one are you". Casual tone is fine, broken grammar is not.
- Captions end with: "📞 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com" + hashtags.
- Never remove or cover AI watermarks (e.g. Gemini/Veo) on user-supplied videos; BB badge may sit NEXT to one.
- Do not invent prices or services. Known prices: Venue Package 3-Hour $625 (up to 25 guests),
  4-Hour $800 (up to 40). Venue: seats 40, holds 80 standing. Referral: up to $100 per booking,
  fine print "Reward based on booking size, up to $100 · No limit on referrals · Paid after the referred event is completed".
  RENTAL PRICE LIST (owner-supplied price card, Oct 18 night; the pending price-list unlock is
  DONE): DROP-OFF prices: folding chair $2 · 6 ft rectangle table $10 · 6 ft round table $15 ·
  table + 6 chairs set $22. Drop-off = delivered and picked up, CUSTOMER sets up, delivery quoted
  with the order (not free, not included in item price). FULL-SERVICE (we set up and break down):
  packages FROM $265. COPY RULE from this point: for rentals say "delivered and picked up" plus
  "full-service setup available", never a blanket "setup included" (that applies to the VENUE
  package only, where it IS included). Owner's card saved at flyers/BB_PriceCard_Owner.png and
  posted; reuse these numbers freely, never others.

## The daily set (triggered when user names a weekday, e.g. "Monday")
8 pieces/day through October, each labeled with its ROUTING:
1. MORNING CARD, one per day at 9am (MERGED LANE, owner-approved Oct 18 after week-2 report
   showed tip + business cards each pulling single/low double digits: "yes make the merge",
   applies from the Monday Oct 19 build): ONE carousel that rotates the two old angles day by
   day, practical "PARTY MATH · TIP No.X" cards (numbering continues, next: No.35) and
   business/service cards. The old separate 8am tip + 10am business slots are RETIRED.
   Saved effort goes to real footage edits, profession-direct referral and the comedy lanes.
3. Venue space flyer, new design daily [feed ~2x/week, else Story]
4. Referral flyer, new design daily [Story]
5. Halloween countdown flyer until Oct 31 (live count: Oct N -> 31-N nights; VERIFY with python datetime) [Story]
6. GAG REEL LANE RETIRED (owner Oct 18 night: "this add on will replace the gag reel"): the daily
   TREND REMIX video (see TREND REMIX LANE below) takes the gag reel's 5pm slot and its TikTok
   reel slot from the Monday Oct 19 build. Gags #1-23 are history (last: Candy Tax, Sun Oct 18);
   gag #24 never runs. reelH.html stays on file (its rig, helpers and the GAGENDS per-reel
   end-card engine are reusable for trend videos). [feed]
7. Pink October awareness video daily until Oct 31 (pink*.html engine; made: 1-in-8 intro, Know the Signs,
   Monthly Check, Support Edition) [feed or Trial Reel]
8. Evening comedy reel: THE BIG BUSINESS CHRONICLES episode [feed]
9. EN ESPAÑOL (owner directive Oct 10, DAILY from Sunday Oct 11): one Spanish-language post per day
   at 3pm Vegas, FB + IG feed (card or 4-5 slide carousel, same design system). NATIVE Spanish copy
   written for the audience, never a literal translation of an English post. Theme rotation:
   quinceañeras, posadas/December holiday bookings, el venue, referidos (hasta $100), Halloween dates,
   services. CTA: phone + "Escríbenos al chat de bigbusinesspartyrentals.com" + "Envía esto a..."
   share lines; NO Spanish keyword-DM CTAs until the owner confirms he answers Spanish DMs.
   Hashtags Spanish + local, max 5. Spanish pinned comments for this lane's posts, verbatim:
   FB(ES): "¿Planeando una fiesta? Síguenos también en Instagram: montajes reales y fechas disponibles.\ninstagram.com/bigbusiness_rentals_events"
   IG(ES): "Sigue a @bigbusiness_rentals_events para ver montajes reales y fechas disponibles. También estamos en Facebook: facebook.com/profile.php?id=61589138907701" 
FEED DISCIPLINE (owner-approved Oct 5; revised Oct 5 night "posts too, for ig and tiktok", "no videos";
REVISED AGAIN by owner Oct 8 night: "stop posting photo carousels to story" and "only post one
carousel to tiktok a day"): every card-lane set (tip, business, venue, referral, countdown) runs as
FB feed post + IG feed carousel (4:5 originals, type post, firstComment attached, caption says
"Swipe"). TikTok gets exactly FOUR posts per day (owner confirmed Oct 9): ONE card carousel (9:16 story9
images) plus the THREE daily reels (gag, pink video, Chronicles episode). Nothing else goes to TikTok.
TIKTOK NON-REEL SLOT = PRICE IT (owner directive Oct 11 night, REPLACES the rotating carousel
pick): the one TikTok post besides the three reels is the day's PRICE IT image (9:16 story9 pad of
the card) at 1pm, same caption as FB/IG. The carousel-pick rotation is RETIRED (history: Fri Oct 9
countdown, Sat tip, Sun business, Mon tip, Tue countdown; Mon + Tue were swapped to PRICE IT in the
queue when the rule landed). story9 pads are still generated for every PRICE IT card.
NO IG STORY SEQUENCES for card sets anymore (the Mon-Thu story lane is
retired; story9 pads are still generated for the TikTok PRICE IT post). Pink awareness VIDEO may
still route as story (it is a video, not a photo carousel). Applied from the Friday Oct 9 queue onward.
NO slideshow videos for card sets (owner rejected them Oct 5 night; a music test was built in
slideshows/ then reverted, build_slideshow.py kept on file only). APIs cannot attach licensed music
to photo posts, so TikTok carousels run silent unless the owner adds a sound in-app.
STORY IMAGES MUST BE 9:16 (owner screenshot Oct 5: IG zoom-crops 4:5 cards posted as stories, cutting
the sides off). Every image queued as an IG story uses the 1080x1920 padded version from
big-business-rentals/story9/ (build_story_pad.py edge-smears the card's top/bottom rows onto a 1920
canvas; build_restory_ig.py re-points queued IG stories at story9/ URLs). Future daily builds: render
the 4:5 card for FB/feed AND generate the story9 pad in the same run; prefer dropping the "SWIPE →" cue
on frames that only run as stories. FB stories tolerate 4:5 but use the padded version there too when
routed as story. FB posts may stay as feed posts. Trial Reels cannot be
scheduled via API (manual only). All videos also go to YouTube Shorts and TikTok.
HASHTAGS: HARD MAX 5 per caption (Instagram caps meaning at 5 since 2026); prefer local + niche mix.
Captions: FB/IG version AND YouTube Shorts version (title + description + #Shorts) for every video.
Caption style: first line = question or bold claim; include a "send this to..." share line and/or ONE keyword CTA
("Comment VENUE and we will DM you..."); never engagement bait ("comment yes", "tag 3 friends").
Weekly: all-new flyer designs and all-new reel material every week, nothing reused.
WEEKLY ANALYTICS (Sundays): run big-business-rentals/build_weekly_report.py (pulls sent-post metrics from
Buffer GraphQL, groups by lane). After 2+ weeks of data, let winning lanes/hooks steer content and times.
REAL FOOTAGE STANDING ORDER (research priority 1): whenever the owner sends raw job footage (deliveries,
venue flips, teardowns, truck loading), DROP the illustrated piece in the nearest lane and cut the footage
instead: bold hook text ON FRAME ONE (no intros), 15-30s, end on the reveal, loop-edit short cuts, real
sound. Transformation content is the growth engine; illustrated content is the fallback.
CALENDAR HOOKS Oct 8-11 (from research + owner): RODEO WEEKEND (owner directive Oct 6: run it Thursday
AND Friday): Las Vegas Invitational Black Rodeo at Horseman's Park, Fri 10/9 7pm + Sat 10/10 1pm/7pm,
Saturday shows selling out. Thu: venue lane = "rodeo weekend afterparty headquarters", hook "The rodeo
sold out. Your afterparty should not."; generate western outdoor PRICE IT image Thu night (hay bales,
lanterns, desert sunset, denim+gold, no people, no event branding). Fri: 1pm PRICE IT = that western
outdoor setup (fills the owed outdoor slot); referral + other captions get rodeo-weekend flavor.
NEVER use the event's name or branding in posts, no implied affiliation; ride the weekend, not the brand.
Thu 10/8 VGK home opener (verify vs NHL.com): Thursday 1pm PRICE IT stays HockeyNight + watch-party angle;
Sat 10/10 World Mental Health Day (pair with pink lane); Sun 10/11 Raiders at New England 10am PT = brunch
watch party angle; pitch Pinterest-trend "midnight masquerade" venue package for adult Halloween;
F1 Vegas Nov 19-21 = corporate booking look-ahead.
CONVERSION NOTE: keyword CTAs (QUOTE/VENUE/SPOOKY) require the owner to answer comment DMs daily
(owner confirmed Oct 5 he sends the DMs; ready-made DM replies for each keyword are in chat history).
WEBSITE CHATBOT CTA (owner directive Oct 7 night, applies from the Friday Oct 9 build onward): the
chatbot on bigbusinesspartyrentals.com is a third conversion path alongside keyword DMs and calls.
Every day AT LEAST TWO captions direct people to it with a line like "Questions? The chat on
bigbusinesspartyrentals.com answers right away." or "Skip the wait, chat with us at
bigbusinesspartyrentals.com." Rotate the wording, never robotic-sounding, never replace the standing
contact line (that stays verbatim). CTA slides may use "CHAT WITH US AT BIGBUSINESSPARTYRENTALS.COM"
as the clear action in rotation with keyword CTAs and "send this to...". DM replies to keywords should
also point people to the site chat for instant answers after hours. (Site unreachable from this
environment through the proxy; copy stays tool-agnostic, just "the chat on our website".)
PRICE IT LANE (owner request Oct 5; made DAILY the same night): "How Much Would You Pay For This Setup?"
engagement post EVERY DAY in the 1pm FEED slot (FB + IG). ALTERNATE INDOOR AND OUTDOOR setups day by day
(owner directive): indoor = ballrooms, fan caves, living rooms, the venue look; outdoor = Vegas backyards,
pool decks, park pavilions, rooftop patios, desert-sunset yards. Rotate HIGH-VISUAL themes and never repeat
within 2 weeks: local sports colors (silver/black football, gold/steel hockey, NO team logos), cartoon-style
kids parties (generic characters only, NO licensed IP like Disney/Nick), baby showers, quinceañeras,
graduations, birthdays, holiday glam. Owner rejected subtle luxury-only looks ("make them more visual"):
go big, saturated, prop-heavy scenes. Images are AI-GENERATED via Hugging Face Z-Image
(mcp huggingface gr2_z_image_turbo_generate, 1104x1472 3:4, photoreal prompts, no people, "absolutely no
text or letters anywhere", no logos), NEVER photos scraped from Reddit or other sites (copyright +
passing-off risk). Card template: big-business-rentals/build_priceit.py ("SETUP INSPO" stamp stays so it
never reads as a client job photo). Caption rule: NEVER imply balloon decor is our service; angle is
"the tables, chairs and the room underneath it, that is us."
NEVER REPEAT SETUP INSPO (owner directive Oct 10, after Saturday's 1pm reused the Oct 5 BabyShower
card): EVERY PRICE IT image is FRESHLY GENERATED for its day. The card bank
(inspo/BB_PriceIt_{GameDay,HockeyNight,BabyShower,KidsParty,RodeoNight,PoolParty}.png + v1s) is RETIRED
from scheduling; already-posted ones are history only, and no banked or previously posted setup image may
ever be queued again. Generate the next day's setup during the nightly build (theme still matches the
calendar: football look near Raiders games, hockey look near VGK games, etc., always a new scene).
VENUE SCALE RULE (owner correction Oct 11 night, after the first HolidayGlam image read as a family
dinner at home): PRICE IT always promotes MEDIUM TO SEMI-LARGE SEATING ARRANGEMENTS IN VENUE SPACING:
banquet halls, ballrooms, event spaces, multiple round tables of 8-10 or long banquet runs, visible
floor space. A home setting is allowed ONLY as a very large dining room setup. No cozy family-dinner
scenes. Outdoor setups follow the same spirit: party scale, not patio-for-four.
QUOTA NOTE: the HF ZeroGPU image quota on the owner's free account is DAILY and small (~6-8 generations);
generate 1-2 new setups per day during the nightly build, not in batches. If the day's quota is exhausted
before the PRICE IT image is made, generate it first thing the next session, never fall back to the bank.

## MONETIZATION NORTH STAR (owner, Oct 18 night): "the main goal for all of this is to build
monetization, through social media while only posting things that will bring me leads."
Approved expansions ("ok"), live now:
- START HERE PINNED POST: flyers/BB_StartHere.png queued Wed Oct 21 10am FB+IG; owner pins both
  manually after they post. Refresh it when prices or services change.
- GOOGLE BUSINESS PROFILE PACK, WEEKLY: big-business-rentals/gbp/ holds a paste-ready pack
  (post text, image pointer, review-ask text). Produce a fresh pack every Sunday with the weekly
  report; owner pastes it into business.google.com. No hashtags on Google. Pinned-comment texts
  are allowed on Google posts per the firstComment rule.
- SUNDAY REPORT COUNTS LEADS: ask the owner each Sunday for rough call/DM/site-chat counts and
  fold them into the weekly report; steer lanes by leads, not reach.
PENDING OWNER INPUT (ask when relevant, never invent): weekly OPEN DATES list (unlocks scarcity posts; becomes the
countdown lane's replacement after Oct 31 as a December-dates countdown), SPANISH DM confirmation
(unlocks "Comenta COTIZA" keyword CTAs in the español lane), weekly $5-10 boost pick (report names
the candidate each Sunday).

## TREND REMIX LANE (owner directive Oct 18 night, DAILY from the Monday Oct 19 build)
One trending-topic comedy video per day that remixes the day's most talked-about topic toward the
business ("teslas new flying roadster" was the owner's example). Mechanics, every nightly build:
1. SEARCH: one extended WebSearch for the day's most talked-about topic (news + social trends).
   CURRENT ONLY (owner Oct 25: "i dont want to remix something thats old i want current trends thats
   going on right now, the remix is to only make the trend compatible with my business"): pick a
   trend that is live THIS WEEK (this week's TikTok/IG trend roundups, this week's news); never a
   revival or nostalgia format (the Mannequin Challenge remix was pulled for this). Keep the trend's
   format recognizable and only adapt it so the payoff lands on the business.
2. PICK with guardrails: fun topics only, product launches, viral formats, pop culture, sports
   moments, absurd stories. NEVER tragedies, deaths, disasters, politics, culture-war topics.
   Parody the IDEA, never the brand: no logos, trademarks, celebrity likenesses or implied
   affiliation (same spirit as the rodeo rule: ride the trend, not the brand). A "flying roadster"
   gag is fine, a Tesla logo is not. No licensed audio via API: remix the FORMAT with our own
   SFX bed; note in the caption log when the owner should add the trending sound in-app.
3. MAKE IT OURS: the punchline always lands on tables, chairs, linens, delivery or the venue.
   Use whatever medium fits: the canvas rig cast (Wobbles/cat/Chronicles characters reacting to
   or living the trend), recut real footage with the cinematic pipeline, or AI imagery (HF quota
   permitting). Comedy length rule applies (~17s+). Naming: BB_Trend_*.
4. SLOT (REVISED Oct 18 night, owner: the trend remix REPLACES the gag reel): 5pm Vegas daily,
   the old gag slot, on all four channels: FB reel + IG reel + TikTok + YouTube (cat 23). The
   TikTok 4-post cap holds: PRICE IT + trend + pink + episode through Oct 31.
5. LOG the day's topic, source and angle in posting_captions.md with the captions.

## THE BIG BUSINESS CHRONICLES (the show; full bible in big-business-rentals/CAST.md)
Star: MR. BIG BUSINESS (rig STYLER: slim, fade, green tee). Cast: MRS. NEVER WRONG (STYLEW),
UNC (default cap style), TYLER THE INTERN (STYLET; running gag: appears from nowhere,
someone asks "WHERE DID YOU EVEN COME FROM?", he always replies shy/irritated "...im the new intern."),
villain LIL WOBBLES the red cheap chair (col {a:'#e05252',b:'#c94444',c:'#ef6d6d'}), THE CAT (silent nemesis).
Episode numbering continues from Derrick era: next episode is EP. 15.
Season One rules: episode badge + "EP. N" on screen at open; hook text at second ZERO; episodes ~26s from
EP. 28 ON (owner directive Oct 14: "start making the comedy videos 5 seconds longer"; EP15-27 were ~21s),
NO VOICES (owner decision Oct 5 evening: voices tested and CANCELLED, 45s format cancelled).
26s SPEC: 910 frames @35fps, encode -t 26.0, afade out at 25.2, window.ENDTIMES[n]=23.5, end-card
question captions at t 22.4-23.45; use the extra ~5s for story beats, not a longer end card.
(Old 21s spec for reference: 735 frames, -t 21.0, afade 20.2, ENDTIMES 18.5, end card 17.4-18.45.);
zoom punches/instant replay/freeze frames; 2-note theme sting;
season arc "Road to the Halloween Party" (full-cast finale Oct 31); hidden pumpkin every episode;
end-card question + credit fan ideas by @name; W-L tracker for Mr. Big Business (he rarely wins).
Season One voices: NONE, SFX only (ElevenLabs VO tested Oct 5, owner cancelled it; keep IDs in CAST.md on file).
Season Two: owner's real voice recordings begin.

## DAILY CAROUSEL SYSTEM (owner directive Oct 5, REPLACES single static cards for tip, business,
## referral and countdown posts; videos and pre-built sets keep their formats)
Every daily card post is a swipeable carousel of 4 to 6 slides at 1080x1350, one idea per slide:
1. HOOK slide: huge headline only, question or bold claim, 8 words or fewer, NO body text,
   small "SWIPE →" cue bottom right. No progress marker on this slide.
2. SETUP slide: the problem or fact the hook promised, one or two short lines.
3. VALUE slides (1-3): ONE tip/number/step each; large gold number or keyword + max two sentences;
   ghost numeral or simple illustration behind.
4. PAYOFF slide: the surprising result or "here is what to do", set BIGGER than value slides.
5. CTA slide (last): one clear action (keyword comment CTA or "send this to..."), then logo LARGE,
   phone, site, IG, LAS VEGAS NV. Fine print here when required (referral).
Design rules: ONE palette + font set across the whole carousel, different palette each day; heavy display
type + italic serif accents + clean sans; gold accent, thin gold frame, film grain, soft vignette on EVERY
slide; "n/N" counter + slim gold progress bar on every slide after the first; slides 1 and last must work
standalone; small brand footer on every slide, large on CTA slide; no em dashes; no photos of real people.
Caption: question/bold claim first line, then a swipe line, then "send this to..." or ONE keyword CTA,
then contact line + hashtags.
Build: big-business-rentals/build_mon_carousels.py is the reference generator (one HTML per carousel,
.slide divs, Playwright element screenshots at dsf=2, LANCZOS downscale to 1080x1350).
Buffer: queue as type "post" (carousel = multiple image assets in order) on FB + IG.

## Design system (Flyer 2.0, since Oct 4)
- Feed cards 1080x1350 (4:5); carousels replace static flyers for feed (hook slide, value slide, CTA slide).
- Editorial/asymmetric layouts, mixed type (Playfair900 italic accents + Archivo Black), ghost outline numerals,
  illustrated hero objects (chair/table in rig style), film grain + vignette + drop shadows, rotated gold stamps.
- Color rotation is FREE across: Purple/Gold (#3a1a5e radial + #E5B84B), Black&Gold (#23201a), Emerald Night,
  Velvet Rope burgundy, Midnight Navy, Daylight Cream (light mode), Desert Teal/copper, Pink Hour (Oct),
  Halloween orange (#241040 bg, #ff8c2e). Gold appears in EVERY palette. No two consecutive days same palette;
  1+ light-mode card weekly. Palette matches message (green=money, burgundy=VIP, cream=daytime/family).
  Sampler: big-business-rentals/examples/EX_Palette_Roster.png.
- Luxury venue carousel lives in big-business-rentals/venue/lux/ (black/gold/#5b2a86 system, Playfair).

## Technical pipeline (proven, reuse exactly)
- Assets: big-business-rentals/assets/ (fonts/, bb_logo.png, BB_Logo_*.png, logo_master.html, card_land.html).
  Card HTML references fonts via relative "fonts/" and "bb_logo.png": copy assets into the working folder first.
  ("Great Vibes" font file does not exist; that look came from browser fallback.)
- Cards: Playwright chromium at glob /opt/pw-browsers/chromium-*/chrome-linux/chrome, viewport = card size,
  device_scale_factor=2, wait document.fonts.status==='loaded', screenshot, PIL LANCZOS downscale to target.
- Reels: canvas files expose setReel(n)/drawFrame(t); render 540x960 dsf=2 -> frames -> numpy-synth WAV
  (helpers in audio_w3 pattern inside repo build notes) -> imageio_ffmpeg encode libx264 yuv420p crf19
  scale 1080:1920 aac 128k faststart. Animation sources in repo: big-business-rentals/reelsB.html, reelsC.html,
  halloween/reelH.html (rig: drawMan with slim/fade/goatee flags, drawSkeleton noHead, drawGhost, drawCat,
  drawChair/drawTable, caption(), starburst(); STYLER/STYLET/STYLEW/STYLEM/STYLEF defined inside).
  QA EVERY new reel with an 8-frame contact sheet before full render. Long renders: run_in_background.
- Canvas text needs explicit await document.fonts.load(...) per family before drawing one-off frames.
- Awareness videos: big-business-rentals/awareness/pink*.html same drawFrame pattern (22-32s, stat-first cold open).
- Bash heredocs can trip the sandbox classifier; fall back to Write build_*.py then `python3 build_x.py`.

## Voice (TTS)
- `pip install piper-tts` works in this environment. huggingface.co downloads are PROXY-BLOCKED;
  get voices from GitHub releases instead: https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-{ryan-high,amy-low,danny-low}.tar.gz
  Demo mapping: Mr. Big Business=ryan-high, Mrs. Never Wrong=amy-low, Tyler=danny-low pitched up
  (ffmpeg asetrate=16000*1.22,aresample=48000,atempo=0.92). Unc: deep/slow (pitch down).
- ELEVENLABS_API_KEY should be available as an env var (user added it Oct 5). On session start, verify it exists
  and test it against the ElevenLabs API (never print the key). If valid, prefer ElevenLabs for character lines:
  pick consistent voices per character and keep IDs noted in CAST.md.

## Buffer scheduling (working since Oct 5; owner-approved workflow)
- API: GraphQL at https://api.buffer.com, auth via environment credential "Buffer" (Authorization: Bearer, injected).
  The legacy REST api.bufferapp.com does NOT accept this token; never use it.
- Organization ID: 6a8284ed71811e26a813241c. Channel IDs:
  facebook "Big Business Party Rentals & Events Specialist" = 6aabfb63ea19ca0bde696947
  instagram bigbusiness_rentals_events = 6aabfaf0ea19ca0bde6965d6
  tiktok rashad_abdulwali = 6ab81da7ea19ca0bdef9436e
  youtube "R.A Johnson" = 6ac2ff576a5c39ccb618d238
- createPost(input:{channelId, text, mode: customScheduled, dueAt: <ISO datetime>, schedulingType: automatic,
  assets:[{image:{url}} | {video:{url, thumbnailUrl?}}]}). Media = PUBLIC URLs; the repo is public, so use
  raw.githubusercontent.com/RAJEnterprisesUSA/-raj-examples/claude/photo-to-logo-editing-krxiu5/<path> for committed
  files (commit+push media BEFORE queueing). dueAt in Las Vegas local time with explicit offset (-07:00 PDT in October).
- DAILY WORKFLOW (owner-defined Oct 5): queue the WHOLE next day's set THE NIGHT BEFORE at the STANDING TIMES
  (all Vegas local; REVISED Oct 18, tip+business merged): 1 morning card 9am · 3 venue 12pm · 4 PRICE IT 1pm (daily, feed) ·
  5 referral 2pm · 6 countdown 4pm · 7 TREND REMIX video 5pm (replaced gag reel Oct 19) · 8 pink video 6pm · 9 Chronicles episode 8pm.
  Owner can override per post.
  Default channels: cards -> FB + IG; videos -> FB + IG + YouTube + TikTok (YouTube gets the Shorts title/description).
  Required metadata or createPost FAILS: FB needs metadata.facebook.type (post/story/reel); IG needs
  metadata.instagram.type AND shouldShareToFeed (false for story); YouTube needs metadata.youtube.categoryId
  ("23" comedy reels, "22" pink/awareness) + title + privacy public + madeForKids false. TikTok needs none.
  Story routing: tip, business card, referral, countdown, pink = story; venue + cast = post; gag + episode = reel.
  Reference script: big-business-rentals/build_buffer_queue.py (Monday Oct 5 run queued 24/24 OK).
- PINNED FIRST COMMENT (owner directive Oct 5 night, applies to EVERY future FB + IG FEED post, type
  post or reel; stories carry none, TikTok/YouTube have no field): set metadata.facebook.firstComment /
  metadata.instagram.firstComment on createPost. CROSS-LINKED (owner directive Oct 9: the FB comment
  carries the IG link, the IG comment carries the FB link). Exact texts, verbatim:
  FB: "If you're planning anything this season, follow us on Instagram too. Real setups, open dates, and what's available before it books up.\ninstagram.com/bigbusiness_rentals_events"
  IG: "Follow @bigbusiness_rentals_events for real setups and open dates. Booking December now. We are on Facebook too: facebook.com/profile.php?id=61589138907701"
  Buffer posts the comment automatically; PINNING it is manual (owner: open post, three dots on own
  comment, Pin). NEVER use these comments in Facebook groups, only on our own page, IG, and Google posts.
  Reference/backfill script: big-business-rentals/build_firstcomment.py (editPost note: video assets
  must be re-sent WITHOUT thumbnailUrl or the edit fails). Buffer rate-limits bursts of mutations
  (RATE_LIMIT_EXCEEDED): pace edits ~3s apart, back off 90s on a hit.
  Pending owner action: set a custom FB username so the FB comment link reads clean.
- BUFFER CAPTION FORMAT (owner spec, apply to 100% of Buffer captions, all platforms):
  opening line / blank line / ONE caption paragraph / blank line /
  "📞 702-706-8287 · Get your free quote at bigbusinesspartyrentals.com" / blank line / all hashtags on one line.
  No headings, labels or bullets. Never change caption content or meaning, only this visual structure.

## Git & delivery
- Branch: claude/photo-to-logo-editing-krxiu5 only. Commit+push after each day's set (retry 503s with backoff).
- NO PRs unless asked. No model names in repo artifacts. Commit footer: Co-Authored-By Claude + Claude-Session link per system reminder.
- Deliver files to the user via SendUserFile as they are produced (cards first, videos when encoded), captions in chat on request.
- The user's timezone is Las Vegas (UTC-7/8): the UTC date is often a day AHEAD of his. Confirm "today" from his words, not the clock.

## Current status (as of Monday Oct 5, end of day)
- MONDAY OCT 5 SET DELIVERED AND PUSHED: Tip No.22 ICE MATH (Daylight Cream), midday business card
  (Desert Teal "Party Day Handled"), referral casino chip (Emerald Night "easiest $100 in Vegas"),
  26-nights candy corn countdown, Halloween gag #11 Pumpkin Head (reelH REELS[11]),
  Pink October #5 Myths Busted (awareness/pink5.html, 28s), Meet The Cast post + six Cast File cards (from sibling session),
  and EP. 15 "The New Intern" FINAL at 21.0s, SFX only (fb_safe/BB_Chronicles_Ep15_TheNewIntern.mp4).
  All captions in posting_captions.md (use the Oct 5 corrected EP15 captions, no voice mentions).
- COMEDY LENGTH RULE (owner Oct 14: "start making the comedy videos 5 seconds longer", then
  "all funny videos not just the chronicles"): from the Monday Oct 19 builds, Chronicles episodes
  21s -> ~26s AND short comedy reels 12s -> ~17s (the gag lane retired Oct 18 night; the ~17s
  spec now applies to the TREND REMIX videos that replaced it). Pink videos are not comedy, 26s.
  17s SHORT-REEL SPEC: 595 frames @35fps, encode -t 17.2, afade out at 16.7, action to ~13.8s, set
  window.GAGENDS[n]=14.0 per new reel (reelH.html drawFrame now reads per-reel end-card start,
  default 9.0 keeps gags #1-23 correct). Use the extra 5s for one more gag turn or reaction.
  Episodes stay SFX only, NO voiceovers (owner Oct 5: "cancel the whole voices i dont like them").
  Do not add TTS voices to episodes again unless he asks. 26s render spec: 910 frames @35fps,
  -t 26.0, afade 25.2, ENDTIMES[n]=23.5, end-card captions 22.4-23.45 (see Season One rules above).
  EP15-27 shipped at 21.0s (build_ep15v3_render.py era: 735 frames, -t 21.0, afade 20.2).
- ElevenLabs is WORKING via environment credential (xi-api-key injected for api.elevenlabs.io; no env var).
  If 401 returns, the credential needs re-saving in environment settings; Piper stays the fallback.
- TUESDAY OCT 6 SET BUILT, DELIVERED AND PUSHED (awaiting owner go-ahead to queue in Buffer):
  Tip No.23 DRINK MATH (Midnight Navy), Hired A Team business card (Velvet Rope), Plan B venue flyer
  (Purple/Gold, Story), Word Of Mouth referral (Black&Gold), 25-nights jack-o-glow countdown,
  gag #12 Spider Guest (reelH REELS[12]), Pink #6 By The Numbers (pink6.html, 26s),
  EP. 16 The Demonstration (REELS[16] in reelsD, 21s: Mrs. Never Wrong debut, Lil Wobbles, W-L 0-2).
  Captions for all of it in posting_captions.md under TUESDAY OCT 6. DO NOT queue until owner says so;
  then use build_buffer_queue.py pattern at the standing times.
- WEDNESDAY OCT 7 SET BUILT, DELIVERED, PUSHED AND QUEUED IN BUFFER (22/22 OK at standing times):
  TRASH MATH Tip No.24 carousel (Emerald), YOUR WEEKEND BACK carousel (Cream), One Price venue card
  (Navy, Story), GET PAID TO BE POPULAR referral carousel (Purple/Gold), 24 NIGHTS carousel
  ("Halloween lands on a Saturday" hook), gag #13 Candy Hand (reelH REELS[13], boneArm+drawBowl added),
  Pink #7 Men's Edition (pink7.html, 26s, CDC), EP. 17 The Decoy (REELS[17] in reelsD, drawCatD ported,
  cat beats Mr. Big Business, W-L 0-3). Captions under WEDNESDAY OCT 7. Queue script: build_buffer_queue_wed.py.
- THURSDAY OCT 8 SET BUILT, DELIVERED AND PUSHED (queue the night before per workflow):
  Tip No.25 TABLE MATH carousel (Purple/Gold, 6), VEGAS THIS WEEKEND IS LOADED business carousel
  (Emerald, 5), rodeo venue card BB_Venue_Thu_SoldOut (Desert Teal, single, "The rodeo sold out. Your
  afterparty should not."), WEEKEND PLUG referral carousel (Velvet Rope, 5), 23 NIGHTS countdown
  (Halloween, 4), gag #14 DJ Bones (reelH REELS[14], drawSpeaker+drawSkullLoose; used now: ...candy hand,
  DJ Bones), Pink #8 The Screening Explained (pink8.html, 26s, ACS+USPSTF), EP. 18 The Flyer (REELS[18]
  in reelsD, drawFlyer helper, Tyler returns, W-L 0-4). PRICE IT Thu 1pm = HockeyNight (VGK opener).
  Captions under THURSDAY OCT 8. story9 pads generated for all Thursday cards.
  BANKED for Friday/Saturday: inspo/BB_PriceIt_RodeoNight.png (western outdoor, Fri 1pm) and
  BB_PriceIt_PoolParty.png (Sat); outdoor seeds debt CLEARED (setup_western.png, setup_pool.png).
- Friday Oct 9 needs: Tip No.26 carousel, business carousel, venue slot, referral carousel, 22-nights
  countdown (VERIFY with datetime), gag #15, Pink #9, EP. 19 (~21s SFX only; W-L 0-4 going in),
  PRICE IT = RodeoNight (banked). Rodeo-weekend caption flavor per calendar hooks.
- SUNDAY OCT 11 SET BUILT AND QUEUED MORNING-OF (owner said "Sunday" at 7:38am; tip slot ran 9am
  that day only; cards 15/15 queued, videos queued same day): Tip No.28 BRUNCH MATH carousel (Cream, 6),
  YOUR CREW IS COMING AT 10AM business carousel (Emerald, 5, TikTok pick; rotation Fri countdown,
  Sat tip, Sun business), MIDNIGHT MASQUERADE venue card (Velvet, single), SUNDAY DINNER referral
  carousel (Black&Gold, 5), 20 NIGHTS countdown (Purple, 4), PRICE IT = BB_PriceIt_SunBrunch
  (FRESH outdoor brunch watch party per never-repeat rule), EN ESPAÑOL debut Quince carousel 3pm,
  gag #17 Pinata (reelH REELS[17]; used now: ...DJ Bones, Tablecloth Ghost, Photo Booth, Pinata),
  Pink #11 Know Your History (pink11.html, 26s, ACS family-history facts),
  EP. 21 The Seating Chart (REELS[21] in reelsD; Mrs NW silent chair war, cat takes seat one,
  W-L 1-6). Captions under SUNDAY OCT 11. Next: Tip No.29, gag #18, Pink #12, EP. 22.
- MONDAY OCT 12 SET BUILT AND QUEUED SUNDAY NIGHT (29/29 OK): Tip No.29 LINEN MATH carousel (Teal,
  6, TikTok pick; rotation Sat tip / Sun business / Mon tip again, week-1 data logged), business 10am +
  venue 12pm = the two REAL FOOTAGE CINEMATIC reels (Party Day Flow 25s, Venue Walk 13.9s; each ends on
  its own fresh flyer per the new rules), PRICE IT = BB_PriceIt_DecemberBall (venue-scale ballroom; first HolidayGlam image rejected as home-scale, swapped in queue), CONTACTS referral carousel (Emerald, 5), EN ESPAÑOL #2 La Posada (Cream, 5, 3pm),
  19 NIGHTS countdown (Halloween, 4), gag #18 Ghost Waiter (reelH REELS[18]; used now:
  ...Photo Booth, Pinata, Ghost Waiter), Pink #12 Dense Facts (pink12.html, 26s, ACS+FDA),
  EP. 22 The Decoration Committee (REELS[22]; Tyler returns and wins, W-L 1-7).
  Captions under MONDAY OCT 12. Next: Tip No.30, gag #19, Pink #13, EP. 23, español #3 (theme: el
  venue or referidos), TikTok pick Tuesday ≠ tip. Banked for Tuesday: spiderman ballpit reveal clip
  (rotate last 5s +90 = vertical money shot), branded waterslide clip, backyard party photos.
- TUESDAY OCT 13 SET BUILT AND QUEUED SUNDAY (28/28 OK, two days ahead): Tip No.30 CAKE MATH
  carousel (Navy, 6), business 10am = BB_Real_FunStuff CINEMATIC reel (14.8s: ball pit, walk-out,
  rotated vertical reveal of the giant inflatable, fresh orange/purple flyer #3 "THE FUN STUFF TOO"),
  COMPANY PARTY venue card (Black&Gold, single, F1/December corporate angle), PRICE IT =
  BB_PriceIt_HalloweenYard (FRESH outdoor venue-scale Halloween night, three long tables of twelve),
  WORK PLUG referral carousel (Velvet, 5), EN ESPAÑOL #3 El Venue (Emerald, 5, 3pm),
  18 NIGHTS countdown (Purple, 4, TikTok pick; rotation Sun business / Mon tip / Tue countdown),
  gag #19 Candy Security (reelH REELS[19], ropePost+ropeLine+drawCandyBit helpers; used now:
  ...Ghost Waiter, Candy Security), Pink #13 Everyday Defense (pink13.html, 26s, ACS lifestyle),
  EP. 23 The Costume Check (REELS[23], witchHat helper; Wobbles busted at the door, W-L 2-7).
  Captions under TUESDAY OCT 13.
- WEDNESDAY OCT 14: NOTHING BUILT OR QUEUED (owner's Wed order was "create and queue Thursday-
  Sunday post now", explicitly skipping Wednesday; flagged to owner in chat).
- THU OCT 15 - SUN OCT 18 FOUR-DAY SET BUILT AND QUEUED WEDNESDAY (cards 60/60 OK; 12 videos
  rendered and queued the same session, 4 channels each, see chat for final counts; week7 folder): Tips No.31 TIMELINE MATH (Purple, 6) / No.32 RSVP MATH (Navy, 6) / No.33 WEATHER
  MATH (Cream, 6) / No.34 GOLDEN HOUR MATH (Teal, 6); business NOT A PROJECT (Cream) / 48 HOURS
  (Teal) / BEFORE BREAKFAST (Purple) / FOOTBALL SEATS (Navy, chat CTA); venue singles WINTER
  BIRTHDAYS (Velvet) / $625 SPLIT 25 WAYS (Emerald) / TWO SATURDAYS LEFT Oct 24+31 (Black&Gold) /
  FRIENDSGIVING (Cream); referral THE BARBER (Emerald) / PAYDAY (Black&Gold) / TONIGHT (Velvet) /
  CHAT ADMIN (Emerald); español #4 REFERIDOS (Black&Gold, Spanish fine print) / #5 FECHAS DE
  HALLOWEEN (Halloween) / #6 SERVICIOS (Emerald) / #7 EL VALS quince (Velvet); countdowns 16/15/14
  ("TWO WEEKS EXACTLY")/13 nights; PRICE IT fresh daily, venue scale, FB+IG+TT pad 1pm:
  QuinceBallroom (indoor) / RooftopGlow (outdoor) / KidsCartoon (indoor, generic characters) /
  FallHarvest (outdoor). Gags #20-23 FogMachine/DancingBroom (fogBank, drawBroom helpers) /
  SeanceTable / CandyTax (used now: ...Candy Security, Fog Machine, Dancing Broom, Seance Table,
  Candy Tax). Pink #14-17 Under40/BuddySystem/SurvivorSalute/GroupText (pink14-17.html).
  EP. 24 The Playlist War (drawPhoneD, sparkleD; cat runs the aux, W-L 2-8) / EP. 25 The Guest List
  (drawListD; Tyler "...im the new intern" plus two, 2-9) / EP. 26 The Dance Rehearsal (scoreCard
  helper; chair outscores him, cat gets a 10, 2-10) / EP. 27 The Walkthrough (WIN No.3: Wobbles
  denied, cat decoyed, approved, 3-10, sets up Halloween finale). Carousel generators
  build_thufri_carousels.py + build_satsun_carousels.py; queues build_buffer_queue_thusun.py +
  build_buffer_queue_thusun_videos.py. Captions under THURSDAY OCT 15 through SUNDAY OCT 18 +
  VIDEO CAPTIONS block. Next: Tip No.35, gag #24, Pink #18, EP. 28, español #8, Monday Oct 19 set;
  SUNDAY OCT 18 EVENING = weekly analytics report No.2 (build_weekly_report.py).
  Still banked: branded waterslide
  clip (owner-edited, ends on BB logo), backyard party photos, Blank Canvas venue concept (AI-dressed
  looks of the real room, CONCEPT stamp) when HF quota is fresh.
- MONDAY OCT 19 SET BUILT AND QUEUED SUNDAY NIGHT (25/25 OK: cards 13, videos 12; FIRST set on
  the merged format, the trend lane and the new comedy lengths): MORNING CARD debut SPACE MATH
  No.35 (Black&Gold, 6, 9am), HOLIDAY DATE venue single (Velvet), PRICE IT = BB_PriceIt_HoopLounge
  (fresh indoor NBA-tipoff watch-party ballroom, no logos, left-edge wall art cropped out),
  THE NAIL TECH referral (Purple, 5, profession-direct per week-2 data), EN ESPAÑOL #8
  DICIEMBRE (Cream, 5), 12 NIGHTS countdown (Halloween, 4), TREND REMIX DEBUT BB_Trend_CostumeWalk
  (17.2s, reelH REELS[24], GAGENDS[24]=14.0, witchHatH/capeH/spotOverlay helpers; topic: costume
  walk slow-reveal format, logged), Pink #18 THE CALLBACK (pink18.html, 26s, ACS), EP. 28 THE
  TASTE TEST (REELS[28], FIRST 26s EPISODE, 910 frames, ENDTIMES 23.5; his decoy used against
  him, W-L 3-11). Also queued separately: Bring To The Table sketch 10am (FB/IG/YT).
  Captions under MONDAY OCT 19. Next: morning card No.36 or business-angle day, trend search
  Tuesday, Pink #19, EP. 29, español #9, PRICE IT outdoor Tuesday.
- TUESDAY OCT 20 SET BUILT AND QUEUED SUNDAY NIGHT, TWO DAYS AHEAD (25/25 OK: cards 13,
  videos 12): MORNING CARD WE CARRY IT (Emerald, 6, business-angle day), CORPORATE NOVEMBER
  venue single (Navy, "big race weekends" phrasing, no event branding), PRICE IT =
  BB_PriceIt_MovieNight (fresh outdoor backyard cinema, background figures cropped out),
  THE DJ referral (Velvet, 5), EN ESPAÑOL #9 LA CORTE quince (Black&Gold, 5), 11 NIGHTS
  countdown (Purple, 4), TREND REMIX #2 BB_Trend_FaceRating (reelH REELS[25], "my reaction"
  face-only rating format, zoom-to-face zones), Pink #19 THE FAMILY TREE (pink19.html, both
  sides of the family, ACS), EP. 29 THE PUMPKIN CARVE (REELS[29], drawPumpkinC helper; Tyler's
  pumpkin carves itself, Wobbles headbutts his, W-L 3-12). Captions under TUESDAY
  OCT 20. Next: morning card tip-day No.36, trend search Wednesday, Pink #20, EP. 30,
  español #10, PRICE IT indoor Wednesday.
- WEDNESDAY OCT 21 SET BUILT AND QUEUED MONDAY NIGHT, TWO DAYS AHEAD (cards 13/13 OK; videos
  queued same session, see chat): MORNING CARD tip day BUDGET MATH No.36 (Teal, 6; FIRST
  price-list carousel: $2 chair / $22 set / $176 seats 48, QUOTE headcount CTA), THE 31ST IS A
  SATURDAY venue single (Purple), PRICE IT = BB_PriceIt_Masquerade (fresh indoor venue-scale
  midnight masquerade, Pinterest-trend angle), THE BARTENDER referral (Black&Gold, 5), EN
  ESPAÑOL #10 PRECIOS REALES (Cream, 5; first Spanish price card), 10 NIGHTS countdown
  (Halloween, 4), TREND REMIX #3 BB_Trend_GettingRobbed (reelH REELS[26], GAGENDS[26]=14.0;
  background-heist "robbed in broad daylight" format: cat/Wobbles/ghost strip the setup behind
  MBB, freeze HE HAS NO IDEA), Pink #20 THE 55 PLUS EDITION (pink20.html, ACS every-other-year
  choice at 55+), EP. 30 THE INVITATIONS (REELS[30]; invStack/invite helpers; Wobbles has an
  invite, decree everyone is invited, cat beds on the spare stack, finale setup, W-L 3-13).
  Wednesday ALSO carries START HERE pinned post 10am + owner price card 11am (queued earlier) =
  29 posts total. Captions under WEDNESDAY OCT 21. Next: morning card Thursday (business-angle
  day), Pink #21, EP. 31, español #11, PRICE IT outdoor Thursday,
  referral profession next: photographer or party planner.
- THURSDAY OCT 22 SET BUILT AND QUEUED MONDAY NIGHT, THREE DAYS AHEAD (cards 13/13 OK;
  videos queued same session, see chat): MORNING CARD business day DELIVERY DAY (Velvet, 6;
  chat CTA on the CTA slide), COSTUME PARTY HQ venue single (Emerald), PRICE IT =
  BB_PriceIt_GlowNight (fresh outdoor backyard glow party, three long banquet runs, neon
  centerpieces), THE PHOTOGRAPHER referral (Purple, 5; profession run: Barber, NailTech, DJ,
  Bartender, Photographer), EN ESPAÑOL #11 LAS POSADAS (Navy, 5; December bookings), 9 NIGHTS
  countdown (Black&Gold, 4), TREND REMIX #4 BB_Trend_RocketDelivery (reelH REELS[27],
  GAGENDS[27]=14.0; OWNER-LOCKED topic: the new Tesla roadster reveal; RESTAGED per owner Oct 19
  night to take place ON THE ROAD: scene A rush-hour traffic jam with skyline, liftoff and
  barrel-roll lane change over the cars; scene B pulls up at the CLIENT'S VENUE exterior
  (venueFrontT27 facade: awning, glowing windows, string lights) and delivers at the curb;
  drawVanH/drawCarH/roadSkyT27/roadStripT27 helpers; NO Tesla name/logo/design anywhere,
  "flying roadster news" phrasing only), Pink #21 THE NO-COST EDITION (pink21.html, CDC early detection program,
  dial 211), EP. 31 THE DRY RUN (REELS[31]; finale rehearsal, Wobbles crams into the row,
  inspection passed, cat knocks the centerpiece pumpkin, Tyler completes the row, W-L 3-14).
  Captions under THURSDAY OCT 22.
- FRIDAY OCT 23 + SATURDAY OCT 24 SETS BUILT AND QUEUED MONDAY NIGHT, FOUR AND FIVE DAYS
  AHEAD (cards 13/13 OK each; videos queued same session, see chat). FRIDAY: tip No.37
  PLAYLIST MATH (Cream, 6, weekly light card; chat line added to queued caption via
  editPost), TOMORROW OR NEXT SATURDAY venue (Halloween single, chat line via editPost),
  PRICE IT = BB_PriceIt_SpeakeasyJazz (fresh indoor 1920s speakeasy), THE PARTY PLANNER
  referral (Teal, 5), ESPAÑOL #12 HALLOWEEN CAE EN SÁBADO (Emerald, 5), 8 NIGHTS (Velvet,
  4), TREND #5 BB_Trend_CatJudges (REELS[28]; black-cat reaction format: the cat judges
  four exhibits from a podium, applause for delivery day), Pink #22 THE ONE-MINUTE
  CHECKLIST (pink22.html), EP. 32 THE SUPPLY RUN (REELS[32]; every box a red chair, one
  candy bag, Tyler in box two, W-L 3-15). SATURDAY: NOVEMBER IS THE NEW DECEMBER business
  card (Navy, 5), NEXT SATURDAY IS THE 31ST venue (Purple single, chat line), PRICE IT =
  BB_PriceIt_GridironYard (fresh outdoor backyard game day, no logos), THE TEACHER referral
  (Black&Gold, 5), ESPAÑOL #13 RECOMIENDA Y GANA (Teal, 5, Spanish fine print, chat line),
  7 NIGHTS ONE WEEK EXACTLY (Emerald, 4), TREND #6 BB_Trend_PorchReveal (REELS[29];
  porch-reveal format, payoff "decor gets the views, seating keeps the guests", Wobbles
  witch-hat cameo), Pink #23 ASK THESE THREE (pink23.html), EP. 33 THE LIGHT CHECK
  (REELS[33]; Wobbles becomes the chandelier, cat unplugs everything, one light survives,
  W-L 3-16). Trend picks from one Oct 19 extended search (socialpilot/newengen/later
  roundups), logged per day. Captions under FRIDAY OCT 23 and SATURDAY OCT 24. Next:
  SUNDAY OCT 25 = weekly analytics report No.3 + GBP pack + lead counts + boost pick;
  Sunday set: tip day No.38, trend search fresh, Pink #24, EP. 34, español #14, PRICE IT
  indoor Sunday, referral profession: event coordinator or hair stylist; countdown 6
  NIGHTS; arc note: EP. 34-37 run up to the Oct 31 full-cast finale.
- Awareness (pink) videos keep their 26s format. Comedy lengths from Oct 19: trend remixes ~17s,
  episodes ~26s (owner Oct 14 directive, see COMEDY LENGTH RULE above).
- Open offers never accepted: website work; re-render old reel end cards with new logo; referral tracking sheet.
