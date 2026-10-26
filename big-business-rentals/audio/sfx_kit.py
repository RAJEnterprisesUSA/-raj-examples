"""Free sound upgrade (owner Oct 25: no ElevenLabs budget). Real instrument stingers and beds from
the FluidR3 General MIDI soundfont (MIT license) via FluidSynth, replacing pure synth beeps.
Setup each session: apt-get install -y fluidsynth fluid-soundfont-gm ; pip install mido
Usage: render(name) -> numpy float array at 48 kHz mono; render_events([...]) for custom phrases."""
import subprocess, tempfile, pathlib, wave
import numpy as np
import mido

SF2 = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
SR = 48000
PROG = {"brass": 61, "trombone": 57, "trumpet": 56, "xylo": 13, "pizz": 45, "strings": 48,
        "orchhit": 55, "timpani": 47, "piano": 0, "glock": 9, "marimba": 12, "tuba": 58,
        "applause": 126, "bass": 32, "whistle": 78, "clarinet": 71, "harp": 46}

def render_events(events, length=None):
    """events: list of (time_sec, channel, program_or_None, note, velocity, dur_sec[, bend])
    channel 9 = drums (note = GM drum key). bend: -1..1 pitch-bend glide over the note."""
    mid = mido.MidiFile(ticks_per_beat=480); tr = mido.MidiTrack(); mid.tracks.append(tr)
    tr.append(mido.MetaMessage("set_tempo", tempo=500000))   # 120 bpm: 1 beat = 0.5 s
    msgs = []
    for ev in events:
        t, ch, prog, note, vel, dur = ev[:6]
        bend = ev[6] if len(ev) > 6 else 0
        if prog is not None and ch != 9:
            msgs.append((t, 0, mido.Message("program_change", channel=ch, program=PROG.get(prog, prog))))
        msgs.append((t, 2, mido.Message("note_on", channel=ch, note=note, velocity=vel)))
        if bend:
            for i in range(1, 9):
                msgs.append((t + dur * i / 9, 1, mido.Message("pitchwheel", channel=ch, pitch=int(8191 * bend * i / 8))))
        msgs.append((t + dur, 3, mido.Message("note_off", channel=ch, note=note, velocity=0)))
        if bend:
            msgs.append((t + dur + 0.01, 1, mido.Message("pitchwheel", channel=ch, pitch=0)))
    msgs.sort(key=lambda m: (m[0], m[1]))
    last = 0.0
    for t, _, m in msgs:
        dt = int(round((t - last) * 960)); last = t
        tr.append(m.copy(time=max(0, dt)))
    with tempfile.TemporaryDirectory() as d:
        mp, wp = pathlib.Path(d) / "x.mid", pathlib.Path(d) / "x.wav"
        mid.save(mp)
        subprocess.run(["fluidsynth", "-ni", "-g", "0.8", "-r", str(SR), "-F", str(wp), SF2, str(mp)],
                       capture_output=True, check=True)
        with wave.open(str(wp)) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
            if w.getnchannels() == 2: a = a.reshape(-1, 2).mean(1)
    if length: a = np.pad(a, (0, max(0, int(length * SR) - len(a))))[:int(length * SR)] if length else a
    return a

KIT = {
 # the Chronicles 2-note theme, now brass + snare + crash
 "theme":   [(0, 0, "brass", 67, 110, 0.2), (0.22, 0, None, 74, 120, 0.4), (0.22, 9, None, 38, 110, 0.1), (0.22, 9, None, 49, 90, 0.8)],
 "freeze":  [(0, 1, "orchhit", 60, 127, 0.4), (0, 2, "timpani", 41, 127, 0.6)],
 "pop":     [(0, 3, "xylo", 84, 115, 0.12)],
 "pop2":    [(0, 3, "xylo", 91, 115, 0.12)],
 "sadtrom": [(0, 4, "trombone", 58, 105, 0.45), (0.5, 4, None, 57, 105, 0.45), (1.0, 4, None, 56, 105, 0.45), (1.5, 4, None, 55, 110, 1.1, -0.35)],
 "sneak":   [(i * 0.25, 5, "pizz" if i == 0 else None, n, 95, 0.18) for i, n in enumerate([48, 51, 55, 51, 48, 51, 56, 55])] +
            [(i * 0.5, 9, None, 76, 70, 0.1) for i in range(4)],
 "win":     [(0, 0, "brass", 60, 115, 0.15), (0.16, 0, None, 64, 115, 0.15), (0.32, 0, None, 67, 115, 0.15), (0.48, 0, None, 72, 125, 0.7), (0.48, 9, None, 49, 110, 1.0)],
 "applause":[(0, 6, "applause", 60, 110, 2.2)],
 "boing":   [(0, 7, "bass", 40, 120, 0.4, 0.9)],
 "whoosh":  [(0, 9, None, 55, 110, 0.6)],          # splash cymbal swell
 "rimshot": [(0, 9, None, 38, 120, 0.1), (0.12, 9, None, 49, 100, 0.8)],
 "kick":    [(0, 9, None, 36, 120, 0.1)],
}
_cache = {}
def render(name):
    if name not in _cache: _cache[name] = render_events(KIT[name])
    return _cache[name]

if __name__ == "__main__":   # demo reel of the new palette
    seq = [("theme", 0.0), ("pop", 1.4), ("pop2", 1.7), ("sneak", 2.3), ("freeze", 4.6), ("boing", 5.6),
           ("rimshot", 6.4), ("sadtrom", 7.4), ("win", 10.4), ("applause", 11.4)]
    A = np.zeros(SR * 14)
    for n, at in seq:
        s = render(n); i0 = int(at * SR); A[i0:i0 + len(s)] += s[:len(A) - i0]
    A = A / np.max(np.abs(A)) * 0.85
    out = pathlib.Path(__file__).parent / "BB_SoundKit_Demo.wav"
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((A * 32767).astype(np.int16).tobytes())
    print("wrote", out)
