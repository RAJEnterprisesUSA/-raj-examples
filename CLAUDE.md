# Big Business Party Rentals & Events · Content System Handbook

This repo runs the daily social content system for Big Business Party Rentals And Events
(Las Vegas, NV). Owner: Rashad Johnson. Read this whole file before building anything.
OPERATOR CHARTER (owner-issued Oct 6): big-business-rentals/OPERATOR.md defines the role, mission and
operating standards (growth mission, hooks-first, originality, research and growth-opportunity duties,
Sunday analytics loop, quality checklist, owner authority). It sits ON TOP of this file and changes
nothing in it; where the charter speaks generally (e.g. people in visuals) the specific rules below
still govern (no photos of real people on cards, no people in PRICE IT images) until the owner says
otherwise. Apply the charter in every session.
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

## The daily set (triggered when user names a weekday, e.g. "Monday")
8 pieces/day through October, each labeled with its ROUTING:
1. Morning tip card: "PARTY MATH · TIP No.X" series (next: No.22) [Story or feed]
2. Midday business card [feed or Story]
3. Venue space flyer, new design daily [feed ~2x/week, else Story]
4. Referral flyer, new design daily [Story]
5. Halloween countdown flyer until Oct 31 (live count: Oct N -> 31-N nights; VERIFY with python datetime) [Story]
6. Halloween gag reel, brand-new gag daily (reelH.html; next is REELS[11]; used: haunted chair, skeleton guest,
   pumpkin overload, witch setup, mummy unravel, frankenstein seat, zombie line dance, ghost guest,
   skeleton limbo, black cat) [feed]
7. Pink October awareness video daily until Oct 31 (pink*.html engine; made: 1-in-8 intro, Know the Signs,
   Monthly Check, Support Edition) [feed or Trial Reel]
8. Evening comedy reel: THE BIG BUSINESS CHRONICLES episode [feed]
FEED DISCIPLINE (owner-approved Oct 5; revised Oct 5 night "posts too, for ig and tiktok", "no videos";
REVISED AGAIN by owner Oct 8 night: "stop posting photo carousels to story"): every card-lane set
(tip, business, venue, referral, countdown) runs TWO ways daily: FB feed post + IG feed carousel
(4:5 originals, type post, firstComment attached, caption says "Swipe") AND TikTok PHOTO carousel
(9:16 story9 images, no metadata). NO IG STORY SEQUENCES for card sets anymore (the Mon-Thu story
lane is retired; story9 pads are still generated because TikTok uses them). Pink awareness VIDEO may
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
Card bank: inspo/BB_PriceIt_{GameDay,HockeyNight,BabyShower,KidsParty}.png (v2, owner-approved direction)
plus v1 {EmeraldGold,NavyChrome,Halloween}. Schedule GameDay near Raiders games, HockeyNight near VGK games.
QUOTA NOTE: the HF ZeroGPU image quota on the owner's free account is DAILY and small (~6-8 generations);
generate 1-2 new setups per day during the nightly build, not in batches. Outdoor seeds (pool party,
desert-sunset backyard) still owed as of Oct 5 night; generate them in the Thursday build for Friday's slot.

## THE BIG BUSINESS CHRONICLES (the show; full bible in big-business-rentals/CAST.md)
Star: MR. BIG BUSINESS (rig STYLER: slim, fade, green tee). Cast: MRS. NEVER WRONG (STYLEW),
UNC (default cap style), TYLER THE INTERN (STYLET; running gag: appears from nowhere,
someone asks "WHERE DID YOU EVEN COME FROM?", he always replies shy/irritated "...im the new intern."),
villain LIL WOBBLES the red cheap chair (col {a:'#e05252',b:'#c94444',c:'#ef6d6d'}), THE CAT (silent nemesis).
Episode numbering continues from Derrick era: next episode is EP. 15.
Season One rules: episode badge + "EP. N" on screen at open; hook text at second ZERO; episodes ~20s, NO VOICES
(owner decision Oct 5 evening: voices tested and CANCELLED, 45s format cancelled; EP15 final = 21.0s, 735 frames
@35fps, encode -t 21.0, afade out at 20.2; per-reel end card time via window.ENDTIMES[n] in reelsD.html);
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
  (all Vegas local): 1 tip 8am · 2 business card 10am · 3 venue 12pm · 4 PRICE IT 1pm (daily, feed) ·
  5 referral 2pm · 6 countdown 4pm · 7 gag reel 5pm · 8 pink video 6pm · 9 Chronicles episode 8pm.
  Owner can override per post.
  Default channels: cards -> FB + IG; videos -> FB + IG + YouTube + TikTok (YouTube gets the Shorts title/description).
  Required metadata or createPost FAILS: FB needs metadata.facebook.type (post/story/reel); IG needs
  metadata.instagram.type AND shouldShareToFeed (false for story); YouTube needs metadata.youtube.categoryId
  ("23" comedy reels, "22" pink/awareness) + title + privacy public + madeForKids false. TikTok needs none.
  Story routing: tip, business card, referral, countdown, pink = story; venue + cast = post; gag + episode = reel.
  Reference script: big-business-rentals/build_buffer_queue.py (Monday Oct 5 run queued 24/24 OK).
- PINNED FIRST COMMENT (owner directive Oct 5 night, applies to EVERY future FB + IG FEED post, type
  post or reel; stories carry none, TikTok/YouTube have no field): set metadata.facebook.firstComment /
  metadata.instagram.firstComment on createPost. Exact texts, verbatim:
  FB: "If you're planning anything this season, follow the page. We post real setups, open dates, and what's available before it books up.\nfacebook.com/profile.php?id=61589138907701"
  IG: "Follow @bigbusiness_rentals_events for real setups and open dates. Booking December now."
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
- EPISODE FORMAT (final, owner decisions Oct 5): ~20s, SFX only, NO voiceovers. A 52.5s ElevenLabs-voiced
  cut was built and then cancelled by the owner the same evening ("cancel the whole voices i dont like them
  and only make the video about 20 seconds"). Do not add TTS voices to episodes again unless he asks.
  build_ep15v3_render.py is the reference render script (735 frames, -t 21.0, afade 20.2).
  Per-reel end card time via window.ENDTIMES[n] in reelsD.html.
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
- Gag reels and awareness videos keep their short formats (only Chronicles episodes went long).
- Open offers never accepted: website work; re-render old reel end cards with new logo; referral tracking sheet.
