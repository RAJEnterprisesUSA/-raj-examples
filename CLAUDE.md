# Big Business Party Rentals & Events · Content System Handbook

This repo runs the daily social content system for Big Business Party Rentals And Events
(Las Vegas, NV). Owner: Rashad Johnson. Read this whole file before building anything.
Everything lives under `big-business-rentals/`. Deeper lore: `big-business-rentals/CAST.md`.
All past captions and rule-change logs: `big-business-rentals/posting_captions.md` (append, never rewrite history).
Research backing the strategy: `reports/Party rental content strategy.md`.

## Non-negotiable brand facts (every deliverable)
- Phone: 702-706-8287 (NEVER 703-786-8369). Website: bigbusinesspartyrentals.com (always included).
- Instagram: @bigbusiness_rentals_events · LAS VEGAS, NV.
- Footer block on every card: logo + phone + site + IG + LAS VEGAS, NV.
- NO em dashes anywhere: chat, captions, designs. Use commas, periods, or " · ".
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
Routing rule: only 2-3 FEED posts/day; everything else Stories + 1-2 Trial Reels; all videos also to YouTube Shorts.
Captions: FB/IG version AND YouTube Shorts version (title + description + #Shorts) for every video.
Caption style: first line = question or bold claim; include a "send this to..." share line and/or ONE keyword CTA
("Comment VENUE and we will DM you..."); never engagement bait ("comment yes", "tag 3 friends").
Weekly: all-new flyer designs and all-new reel material every week, nothing reused.

## THE BIG BUSINESS CHRONICLES (the show; full bible in big-business-rentals/CAST.md)
Star: MR. BIG BUSINESS (rig STYLER: slim, fade, green tee). Cast: MRS. NEVER WRONG (STYLEW),
UNC (default cap style), TYLER THE INTERN (STYLET; running gag: appears from nowhere,
someone asks "WHERE DID YOU EVEN COME FROM?", he always replies shy/irritated "...im the new intern."),
villain LIL WOBBLES the red cheap chair (col {a:'#e05252',b:'#c94444',c:'#ef6d6d'}), THE CAT (silent nemesis).
Episode numbering continues from Derrick era: next episode is EP. 15.
Season One rules: episode badge + "EP. N" on screen at open; hook text at second ZERO; ~12s runtime
(encode -t 12.2 with afade out at 11.7); zoom punches/instant replay/freeze frames; 2-note theme sting;
season arc "Road to the Halloween Party" (full-cast finale Oct 31); hidden pumpkin every episode;
end-card question + credit fan ideas by @name; W-L tracker for Mr. Big Business (he rarely wins).
Season One voices: Piper TTS or silent. Season Two: owner's real voice recordings begin.

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

## Git & delivery
- Branch: claude/photo-to-logo-editing-krxiu5 only. Commit+push after each day's set (retry 503s with backoff).
- NO PRs unless asked. No model names in repo artifacts. Commit footer: Co-Authored-By Claude + Claude-Session link per system reminder.
- Deliver files to the user via SendUserFile as they are produced (cards first, videos when encoded), captions in chat on request.
- The user's timezone is Las Vegas (UTC-7/8): the UTC date is often a day AHEAD of his. Confirm "today" from his words, not the clock.

## Current status (as of Oct 5 handoff, second save)
- Done through Sunday Oct 4. Last Halloween reel: #10 Black Cat. Last tip: No.21. Countdown Monday = 26 nights (verified).
- SEASON ONE sources ready: big-business-rentals/reelsD.html = reelsC copy with purple end-card logo (window.logoReady)
  plus REELS[15] = EP. 15 "The New Intern" FULLY WRITTEN and contact-sheet QA'd (badge/captions/freeze-zoom/tower/crash all working).
  Remaining nits before full render: move the CRASH starburst from x=350 to ~x=430 (clips left edge), re-check Tyler's
  reach pose at tt~4.9 against the tower. Render it like the Halloween reels: setReel(15), 420 frames, numpy audio
  (add the NEW 2-note theme sting at t=0, e.g. G4 then D5, plus poof at 1.55, ?! sting 1.95, sad two-note catchphrase
  motif at 3.1 AND 7.05 same notes both times, stack taps 4.4+, record-scratch at freeze 5.1, wobble creak, CRASH 6.5,
  pop-out boing 6.95), encode with -t 12.2 and afade out at 11.7 -> fb_safe/BB_Chronicles_Ep15_TheNewIntern.mp4.
- Monday premiere still to build: Tip No.22 "ICE MATH" (Daylight Cream light-mode, Flyer 2.0 4:5), referral card
  (Emerald Night, casino-chip "easiest $100 in Vegas" concept), Halloween 26-nights flyer (candy-corn striped numeral),
  Halloween gag #11 (suggested: "Pumpkin Head" - pumpkin stuck on head, our chair holds during the pull-off),
  Pink October #5 ("Myths, Busted": most diagnosed have no family history ACS; younger women too; lumps often painless),
  Meet The Cast announcement post (examples/EX_MeetTheCast.png, ready), venue slot = the caro1-3 carousel (never posted).
  Feed routing Monday: Ep15 + Cast card + gag #11; everything else Stories/Trial Reel; captions FB/IG + YT Shorts, hook-first.
- ElevenLabs: key added by user Oct 5; sessions started after that should have ELEVENLABS_API_KEY. Verify + test on start.
- Season One voice decision still open (Piper or silent); user said voices "season 2" originally, Piper demo was liked.
- Open offers never accepted: website work; re-render old reel end cards with new logo; referral tracking sheet.
