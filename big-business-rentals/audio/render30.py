"""Shared renderer, UPGRADE Oct 27 (loudness: every mix normalized to -14 LUFS, the social standard): 30 fps (was a non-standard 35) and the instrument sound kit
(sfx_kit.py) for stingers. Usage from a build script:
    from render30 import render_reel, kit, tone, noise
    render_reel('reelsD.html', 36, 26.0, 25.2, OUT, cues)   # cues(add) places sounds
Timings stay in seconds, so the canvas timelines need no change."""
import glob, pathlib, subprocess, wave, sys
import numpy as np
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sfx_kit import render as kit, SR, bed

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
SCRATCH = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad')
FPS = 30

def _env(n, a=0.008, r=0.3):
    e = np.ones(n); na, nr = min(n, max(1, int(a*SR))), min(n, max(1, int(r*SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr); return e
def tone(f, dur, vol=0.5, shape='sine', bend=0.0, vib=0.0):
    n = int(dur*SR); t = np.arange(n)/SR; fr = f*(1+bend*t/dur)
    if vib: fr = fr*(1+0.02*np.sin(2*np.pi*vib*t))
    ph = 2*np.pi*np.cumsum(fr)/SR; s = np.sin(ph)
    if shape == 'square': s = np.sign(s)*0.6+0.4*s
    if shape == 'saw': s = 2*(ph/(2*np.pi) % 1)-1
    return s*_env(n, 0.008, dur*0.5)*vol
def noise(dur, vol=0.5, lp=1.0):
    n = int(dur*SR); s = np.random.randn(n)
    if lp < 1.0: k = max(1, int(1/lp)); s = np.convolve(s, np.ones(k)/k, 'same')
    return s*_env(n, 0.004, dur*0.6)*vol

def render_reel(html, reel, dur, fade_at, out, cues, work=None):
    work = SCRATCH/(work or f'r30_{pathlib.Path(html).stem}_{reel}')
    frames = work/'frames'; frames.mkdir(parents=True, exist_ok=True)
    n = int(round(dur*FPS))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.goto('file://'+str(BASE/html))
        pg.wait_for_function("document.fonts.status==='loaded'")
        pg.evaluate("""async()=>{for(const f of ['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat',
          '600 30px Montserrat','900 italic 40px Playfair']){try{await document.fonts.load(f)}catch(e){}}}""")
        pg.wait_for_timeout(600)
        pg.evaluate(f"setReel({reel})"); pg.evaluate("drawFrame(0)"); pg.evaluate("drawFrame(0)")
        cv = pg.locator('canvas')
        for i in range(n):
            pg.evaluate(f"drawFrame({i/FPS})")
            cv.screenshot(path=str(frames/f'{i:04d}.png'))
        b.close()
    print('frames done', n)
    A = np.zeros(int(SR*dur))
    def add(sig, at, gain=1.0):
        i0 = int(at*SR); i1 = min(len(A), i0+len(sig))
        if i1 > i0: A[i0:i1] += sig[:i1-i0]*gain
    cues(add)
    A = A/np.max(np.abs(A))*0.85
    wav = work/'mix.wav'
    with wave.open(str(wav), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((A*32767).astype(np.int16).tobytes())
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [FF, '-y', '-framerate', str(FPS), '-i', str(frames/'%04d.png'), '-i', str(wav),
           '-filter_complex', f'[0:v]scale=1080:1920:flags=lanczos[v];[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st={fade_at}:d={dur-fade_at:.2f}[a]',
           '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'medium',
           '-r', str(FPS), '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(dur), str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.returncode, r.stderr[-300:] if r.returncode else 'encoded', out)


def remaster(video_in, dur, fade_at, cues, out):
    """Rebuild only the audio of an already-rendered video (picture copied untouched)."""
    A = np.zeros(int(SR*dur))
    def add(sig, at, gain=1.0):
        i0 = int(at*SR); i1 = min(len(A), i0+len(sig))
        if i1 > i0: A[i0:i1] += sig[:i1-i0]*gain
    cues(add)
    A = A/np.max(np.abs(A))*0.85
    wav = SCRATCH/(pathlib.Path(out).stem+'_mix.wav')
    with wave.open(str(wav), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((A*32767).astype(np.int16).tobytes())
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [FF, '-y', '-i', str(video_in), '-i', str(wav), '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
           '-af', f'loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st={fade_at}:d={dur-fade_at:.2f}',
           '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(dur), str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.returncode, r.stderr[-300:] if r.returncode else 'remastered', out)
