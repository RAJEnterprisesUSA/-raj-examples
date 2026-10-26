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
2. **Animated captions** · word-by-word pop/highlight captions (the native TikTok/Reels look)
   instead of whole-line pops.
3. **30 fps renders** · the rig renders at 35 fps, a non-standard rate the apps convert; render at
   30 (or 60 for smoother motion).
4. **Custom covers** · a designed cover frame for every video (Buffer createPost thumbnailUrl), so
   the Instagram grid and YouTube Shorts shelf look like one show.
5. **Motion polish** · motion blur on fast moves, squash and stretch, camera push-ins, parallax
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
- (none yet)
