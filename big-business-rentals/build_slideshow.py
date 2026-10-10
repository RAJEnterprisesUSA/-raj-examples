"""Card set -> TikTok slideshow video with daily original music.

Owner directive Oct 5 night: tap-through sets run as posts on IG and TikTok
"with music, you can pick it daily". APIs cannot attach licensed music to
photo posts, so the TikTok copy becomes a slideshow VIDEO: each story9 frame
~2.8s with a slow push-in, plus an original synth track per day (different
vibe daily, my pick). 1080x1920, 30fps, libx264+aac.

Usage: python3 build_slideshow.py  (renders Tue+Wed sets into slideshows/)
"""
import pathlib, subprocess
import numpy as np
import imageio_ffmpeg

BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
S9 = BASE / 'story9'
OUT = BASE / 'slideshows'
OUT.mkdir(exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 44100
PER = 2.8          # seconds per slide
SINGLE = 8.0       # single-card sets

SETS = {
    # day: [(output stem, [frame names...])]
    "tue": [
        ("TT_Tue_DrinkMath",   [f"BB_Caro_Tue_DrinkMath_{i:02d}.png" for i in range(1, 7)]),
        ("TT_Tue_HiredATeam",  [f"BB_Caro_Tue_HiredATeam_{i:02d}.png" for i in range(1, 6)]),
        ("TT_Tue_PlanB",       ["BB_Venue_Tue_PlanB.png"]),
        ("TT_Tue_WordOfMouth", [f"BB_Caro_Tue_WordOfMouth_{i:02d}.png" for i in range(1, 6)]),
        ("TT_Tue_25Nights",    [f"BB_Caro_Tue_25Nights_{i:02d}.png" for i in range(1, 5)]),
    ],
    "wed": [
        ("TT_Wed_TrashMath",   [f"BB_Caro_Wed_TrashMath_{i:02d}.png" for i in range(1, 7)]),
        ("TT_Wed_WeekendBack", [f"BB_Caro_Wed_WeekendBack_{i:02d}.png" for i in range(1, 6)]),
        ("TT_Wed_OnePrice",    ["BB_Venue_Wed_OnePrice.png"]),
        ("TT_Wed_GetPaid",     [f"BB_Caro_Wed_GetPaid_{i:02d}.png" for i in range(1, 6)]),
        ("TT_Wed_24Nights",    [f"BB_Caro_Wed_24Nights_{i:02d}.png" for i in range(1, 5)]),
    ],
}

# ---- tiny synth -------------------------------------------------------------
def env(n, a=0.005, r=0.08):
    e = np.ones(n)
    na, nr = max(1, int(a * SR)), max(1, int(r * SR))
    na, nr = min(na, n), min(nr, n)
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e

def tone(f, dur, amp=0.3, shape="sine", a=0.005, r=0.08):
    n = int(dur * SR)
    t = np.arange(n) / SR
    if shape == "saw":
        w = 2 * ((f * t) % 1) - 1
    elif shape == "square":
        w = np.sign(np.sin(2 * np.pi * f * t))
    elif shape == "tri":
        w = 2 * np.abs(2 * ((f * t) % 1) - 1) - 1
    else:
        w = np.sin(2 * np.pi * f * t)
    return amp * w * env(n, a, r)

def kick(dur=0.22, amp=0.9):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 110 * np.exp(-t * 22) + 42
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.05)

def snare(dur=0.16, amp=0.5):
    n = int(dur * SR)
    return amp * (np.random.randn(n) * 0.6 + tone(190, dur, 0.5)[:n]) * env(n, 0.001, 0.1) * np.exp(-np.arange(n)/SR*18)

def hat(dur=0.05, amp=0.18):
    n = int(dur * SR)
    return amp * np.random.randn(n) * np.exp(-np.arange(n)/SR*60)

def place(buf, snd, at):
    i = int(at * SR)
    j = min(len(buf), i + len(snd))
    if i < len(buf):
        buf[i:j] += snd[:j - i]

NOTE = {k: 440 * 2 ** ((v - 9) / 12) for v, k in enumerate(
    ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"])}
def nf(name, octv):
    return NOTE[name] * 2 ** (octv - 4)

def track_tue(dur):
    """Vegas funk strut: 104bpm, walking bass, clav stabs."""
    buf = np.zeros(int(dur * SR) + SR)
    spb = 60 / 104
    bass = [("G", 1), ("G", 1), ("As", 1), ("C", 2), ("G", 1), ("F", 1), ("Ds", 1), ("D", 1)]
    chords = [[("G", 3), ("As", 3), ("D", 4)], [("F", 3), ("A", 3), ("C", 4)]]
    t, bi = 0.0, 0
    while t < dur:
        beat = bi % 8
        place(buf, kick(), t)
        if beat % 4 == 2: place(buf, snare(), t + spb)
        for h in range(2): place(buf, hat(), t + h * spb / 2)
        n, o = bass[beat]
        place(buf, tone(nf(n, o + 1), spb * 0.9, 0.34, "saw", 0.004, 0.06), t)
        if beat in (1, 5):
            ch = chords[(bi // 8) % 2]
            for cn, co in ch:
                place(buf, tone(nf(cn, co), spb * 0.45, 0.10, "square", 0.002, 0.05), t + spb * 0.5)
        t += spb; bi += 1
    return buf[:int(dur * SR)]

def track_wed(dur):
    """Midnight groove: 88bpm lo-fi, minor, airy pad."""
    buf = np.zeros(int(dur * SR) + SR)
    spb = 60 / 88
    bass = [("A", 1), ("A", 1), ("F", 1), ("G", 1)]
    pads = [[("A", 3), ("C", 4), ("E", 4)], [("F", 3), ("A", 3), ("C", 4)],
            [("G", 3), ("B", 3), ("D", 4)], [("E", 3), ("G", 3), ("B", 3)]]
    t, bi = 0.0, 0
    while t < dur:
        beat = bi % 4
        place(buf, kick(0.25, 0.7), t)
        if beat == 2: place(buf, snare(0.18, 0.35), t)
        place(buf, hat(0.04, 0.10), t + spb * 0.5)
        place(buf, tone(nf(*bass[beat]) * 2, spb * 1.7, 0.28, "tri", 0.01, 0.3), t)
        if beat == 0:
            for cn, co in pads[(bi // 4) % 4]:
                place(buf, tone(nf(cn, co), spb * 3.6, 0.07, "sine", 0.4, 1.0), t)
        t += spb; bi += 1
    return buf[:int(dur * SR)]

TRACKS = {"tue": track_tue, "wed": track_wed}

# ---- render -----------------------------------------------------------------
def render(day, stem, frames):
    dur = SINGLE if len(frames) == 1 else round(len(frames) * PER, 2)
    wav = OUT / f"{stem}.wav"
    audio = TRACKS[day](dur)
    audio = np.clip(audio * 0.8, -1, 1)
    fade = int(0.8 * SR)
    audio[-fade:] *= np.linspace(1, 0, fade)
    pcm = (audio * 32767).astype(np.int16)
    import wave
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())

    per = dur if len(frames) == 1 else PER
    d_frames = int(per * 30)
    inputs, filt = [], []
    for i, name in enumerate(frames):
        inputs += ["-loop", "1", "-t", str(per), "-i", str(S9 / name)]
        filt.append(
            f"[{i}:v]scale=2160:3840,zoompan=z='1+0.045*on/{d_frames}':d={d_frames}"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,setsar=1[v{i}]")
    concat = "".join(f"[v{i}]" for i in range(len(frames)))
    filt.append(f"{concat}concat=n={len(frames)}:v=1:a=0[v]")
    out = OUT / f"{stem}.mp4"
    cmd = [FF, "-y"] + inputs + ["-i", str(wav),
           "-filter_complex", ";".join(filt), "-map", "[v]",
           "-map", f"{len(frames)}:a",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
           "-c:a", "aac", "-b:a", "128k", "-t", str(dur),
           "-movflags", "+faststart", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG FAIL", stem, r.stderr[-400:]); return False
    wav.unlink()
    print("rendered", out.name, f"{dur}s")
    return True

if __name__ == "__main__":
    for day, sets in SETS.items():
        for stem, frames in sets:
            render(day, stem, frames)
