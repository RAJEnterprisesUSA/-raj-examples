# Video Upgrade Backlog (owner Oct 25: "always upgrade something when ever we can")

One visible upgrade per build. Ordered by impact per effort. Status updated as each ships.

## I can do these myself (no cost)
1. **Real-sounding audio** · ElevenLabs sound-effects + music generation would replace the synth
   beeps. BLOCKED Oct 25: the ElevenLabs account returns "payment_required: failed or incomplete
   payment" (owner must complete the latest invoice).
   FREE REPLACEMENT BUILT Oct 25: big-business-rentals/audio/sfx_kit.py renders real instrument
   stingers and beds (brass theme, orchestra-hit freeze, xylophone pops, sad trombone, pizzicato
   sneak, rimshot, applause, boing) from the FluidR3 General MIDI soundfont (MIT license) via
   FluidSynth. Demo: audio/BB_SoundKit_Demo.m4a. Setup each session (container resets):
   apt-get update && apt-get install -y fluidsynth fluid-soundfont-gm ; pip install mido.
   Free sound sites (Freesound, Pixabay, Mixkit, Kenney, OpenGameArt, Sonniss) are unreachable
   from this environment; the owner can download CC0 or Pixabay-license effects and upload them.
2. **Animated captions** (SHIPPED Oct 27) · word-by-word pop/highlight captions (the native TikTok/Reels look)
   instead of whole-line pops.
3. **30 fps renders** (SHIPPED Oct 27) · the rig renders at 35 fps, a non-standard rate the apps convert; render at
   30 (or 60 for smoother motion).
4. **Custom covers** (BUILT Oct 28, but Buffer rejects video thumbnailUrl on every platform: "social networks do not accept custom video thumbnail images". Covers are made and saved in covers/ for the owner to set by hand in the Instagram app) · a designed cover frame for every video (Buffer createPost thumbnailUrl), so
   the Instagram grid and YouTube Shorts shelf look like one show.
5. **Motion polish** (confetti bursts SHIPPED Oct 29) · motion blur on fast moves, squash and stretch, camera push-ins, parallax
   backgrounds, particle bursts (confetti, dust, sparkles).
6. **Sharper AI skits** · Veo clips arrive at 720x1280; upscale to 1080x1920 with sharpening
   (ffmpeg) or an AI upscaler space on Hugging Face (small daily quota).
7. **Lottie effects** · licensed free Lottie animations (confetti, emoji reactions) layered on the
   canvas; npm is reachable from this environment.

## Owner-side tools (outside this session)
- **Veo 3.1 in Google Flow** (in use) for realistic AI skits.
- **CapCut** for trending templates, effects and auto-captions on the owner's own edits (check the
  commercial-use terms on templates and music for a business account).
- **In-app trending sounds** on TikTok and Instagram (Buffer can't attach licensed music).

## Shipped
- Oct 27 (Tue build: Cat Handshake remix + EP. 36): word-by-word pop captions (captionPop in reelH
  and reelsD), 30 fps renders (audio/render30.py), instrument sound kit stingers, music beds under
  the SFX (sfx_kit.bed), and loudness normalized to -14 LUFS (was peak-normalized, often ~-30 dB).
- Oct 28 (Wed build: Very Serious Opinions remix + EP. 37): designed covers for every video
  (build_covers.py make_cover_canvas, captions-off canvas frame, grid-safe title). Buffer refused the
  thumbnail on all four platforms, so posts went out with the default frame; covers stay in covers/ for manual use.
- Oct 29 (Thu build: Pumpkin Head Illusion remix + EP. 38): confetti bursts and the cinematic finish
  (slight contrast/color lift, soft vignette, fine moving grain) on every render (render30 FINISH).
