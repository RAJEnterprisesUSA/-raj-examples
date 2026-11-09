"""Guess the Theme No. 4: Hot Cocoa Party. Pt. 1 (3 clues, Wed Nov 11 1pm) + Pt. 2 (answer, Thu Nov 12 1pm).
TikTok + Instagram only. Photoreal AI concept art (HF Z-Image 9:16, seeds 101130 / 14936 / 829772 / 643959), AI label on,
AI CONCEPT ART chip on every frame. UPGRADE over No. 3: the theme motion layer is now rising cocoa steam instead of snow.
Same engine as build_gtt2/3."""
import pathlib, subprocess, sys, wave
import numpy as np
from playwright.sync_api import sync_playwright
from PIL import Image
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent/'audio'))
from sfx_kit import render as kit, render_events, SR
from render30 import CHROME, FPS, FINISH
import imageio_ffmpeg
G = HERE/'gtt4'
SCR = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/gtt4')
PARTS = {1: (10.4, [2.6, 5.2], 7.8), 2: (10.4, [2.8, 4.4, 6.0], 7.6)}   # dur, clue cuts, end cut

def frames(part, times, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.goto('file://'+str(G/'gtt4.html')); pg.evaluate('ready()'); pg.evaluate(f'window.PART={part}')
        out = []
        for i, t in enumerate(times):
            pg.evaluate(f'drawFrame({t})')
            pg.evaluate("Promise.all([...document.images].map(i=>i.decode().catch(()=>0)))")
            f = outdir/f'{i:04d}.png'; pg.locator('#c').screenshot(path=str(f)); out.append(f)
        b.close()
    return out

def music(dur):
    """Original winter bed: harp chords (I-IV-V-I in C) + a celesta arpeggio, 104 bpm."""
    beat = 60/104; ev = []; chords = [[48, 52, 55, 60], [53, 57, 60, 65], [55, 59, 62, 67], [48, 52, 55, 60]]
    t = 0.0; i = 0
    while t < dur:
        ch = chords[(i//4) % 4]
        for j, n in enumerate(ch):
            ev.append((t + j*0.018, 1, 46 if (i == 0 and j == 0) else None, n, 62 if i % 2 else 78, beat*0.9))
        arp = [ch[0]+12, ch[1]+12, ch[2]+12, ch[1]+12]
        ev.append((t, 2, 8 if i == 0 else None, arp[i % 4], 70, beat*0.45))
        ev.append((t+beat/2, 2, None, arp[(i+2) % 4], 55, beat*0.4))
        t += beat; i += 1
    return render_events(ev)

def audio(part, out):
    dur, cuts, endc = PARTS[part]
    A = np.zeros(int(SR*dur))
    def add(s, at, g=1.0):
        i0 = int(at*SR); i1 = min(len(A), i0+len(s))
        if i1 > i0: A[i0:i1] += s[:i1-i0]*g
    add(music(dur), 0, 0.55)
    if part == 1:
        add(kit('pop'), 0.02, 0.9)
        for c in cuts: add(kit('whoosh'), c-0.05, 0.6); add(kit('pop2'), c+0.05, 0.9)
        add(kit('freeze'), endc, 0.7)
    else:
        add(kit('win'), 0.0, 0.9)
        for c in cuts: add(kit('whoosh'), c-0.05, 0.5); add(kit('pop'), c+0.1, 0.8)
        add(kit('applause'), endc+0.2, 0.5)
    A = A/np.max(np.abs(A))*0.85
    with wave.open(str(out), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((A*32767).astype(np.int16).tobytes())

def contact(part):
    dur = PARTS[part][0]
    ts = [0, 1.3, 2.75, 4.0, 5.4, 6.8, 8.3, 9.8]
    fs = frames(part, ts, SCR/f'cs{part}')
    sheet = Image.new('RGB', (4*270, 2*480))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((270, 480)), ((i % 4)*270, (i//4)*480))
    p = SCR/f'contact_pt{part}.png'; sheet.save(p); print(p)

def build(part, name):
    dur = PARTS[part][0]; n = int(round(dur*FPS)); d = SCR/f'f{part}'
    frames(part, [i/FPS for i in range(n)], d)
    wav = SCR/f'pt{part}.wav'; audio(part, wav)
    FF = imageio_ffmpeg.get_ffmpeg_exe(); out = HERE/name
    cmd = [FF, '-y', '-framerate', str(FPS), '-i', str(d/'%04d.png'), '-i', str(wav), '-filter_complex',
           f'[0:v]scale=1080:1920:flags=lanczos{FINISH}[v];[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st={dur-0.5}:d=0.5[a]',
           '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-maxrate', '6M', '-bufsize', '12M',
           '-r', str(FPS), '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(dur), str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True); print(r.returncode, r.stderr[-300:] if r.returncode else 'encoded', out)

if __name__ == '__main__':
    if sys.argv[1:] == ['contact']: contact(1); contact(2)
    else:
        build(1, 'TT_GuessTheTheme_HotCocoa_Pt1.mp4'); build(2, 'TT_GuessTheTheme_HotCocoa_Pt2.mp4')
