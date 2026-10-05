import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/gag11')
FRAMES = WORK/'frames'
FRAMES.mkdir(parents=True, exist_ok=True)
OUT = BASE.parent/'fb_safe'
OUT.mkdir(exist_ok=True)

FPS = 35
N = 420

# ---------- frames ----------
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':540,'height':960}, device_scale_factor=2)
    pg.goto('file://'+str(BASE/'halloween/reelH.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.evaluate("""async()=>{
      const F=['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat','600 30px Montserrat','900 italic 40px Playfair'];
      for(const f of F){ try{ await document.fonts.load(f);}catch(e){} }
    }""")
    pg.wait_for_timeout(600)
    pg.evaluate("setReel(11)")
    pg.evaluate("drawFrame(0)"); pg.evaluate("drawFrame(0)")  # warmup
    cv = pg.locator('canvas')
    for i in range(N):
        t = i/FPS
        pg.evaluate(f"drawFrame({t})")
        cv.screenshot(path=str(FRAMES/f'{i:04d}.png'))
    b.close()
print('frames done')

# ---------- audio ----------
SR = 48000
DUR = 12.2
A = np.zeros(int(SR*DUR))

def add(sig, at):
    i0 = int(at*SR)
    i1 = min(len(A), i0+len(sig))
    if i1 > i0: A[i0:i1] += sig[:i1-i0]

def env(n, a=0.01, r=0.3):
    e = np.ones(n)
    na, nr = max(1,int(a*SR)), max(1,int(r*SR))
    e[:na] = np.linspace(0,1,na)
    e[-nr:] *= np.linspace(1,0,nr)
    return e

def tone(f, dur, vol=0.5, shape='sine', bend=0.0, vib=0.0):
    n = int(dur*SR); t = np.arange(n)/SR
    fr = f*(1+bend*t/dur)
    if vib: fr = fr*(1+0.02*np.sin(2*np.pi*vib*t))
    ph = 2*np.pi*np.cumsum(fr)/SR
    s = np.sin(ph)
    if shape=='square': s = np.sign(s)*0.6+0.4*s
    if shape=='saw': s = 2*(ph/(2*np.pi)%1)-1
    return s*env(n,0.008,dur*0.5)*vol

def noise(dur, vol=0.5, lp=1.0):
    n = int(dur*SR)
    s = np.random.randn(n)
    if lp < 1.0:
        k = max(1,int(1/lp))
        s = np.convolve(s, np.ones(k)/k, 'same')
    return s*env(n,0.004,dur*0.6)*vol

# spooky intro two-note
add(tone(220.00,0.22,0.5,'square'), 0.00)
add(tone(329.63,0.34,0.5,'square'), 0.24)
# pumpkin-on-head thunk
add(noise(0.1,0.5,lp=0.04), 1.92)
add(tone(120,0.12,0.5), 1.92)
# ta-da
add(tone(523.25,0.1,0.4), 2.12)
add(tone(783.99,0.22,0.4), 2.24)
# stuck struggle creaks
for at in (3.15, 3.65):
    n=int(0.4*48000); tt=np.arange(n)/48000
    cr=(2*((np.cumsum(95*(1+0.3*np.sin(2*np.pi*5*tt)))/48000)%1)-1)
    cr*=(0.5+0.5*np.sin(2*np.pi*7*tt))*env(n,0.04,0.2)*0.2
    add(cr, at)
# sit thump
add(noise(0.08,0.4,lp=0.05), 4.98)
add(tone(100,0.1,0.45), 4.98)
# three heave swooshes
for at in (5.15, 5.5, 5.85):
    n=int(0.18*48000)
    sw=np.random.randn(n)
    sw=np.convolve(sw,np.ones(24)/24,'same')*env(n,0.02,0.08)*0.4
    add(sw, at)
# POP (cork)
add(tone(640,0.07,0.6,'sine',bend=0.5), 5.92)
add(noise(0.05,0.5,lp=0.2), 5.92)
# Mr BB floor thump
add(noise(0.1,0.5,lp=0.05), 6.45)
add(tone(90,0.12,0.5), 6.45)
# chair sparkle ding
add(tone(1567.98,0.3,0.3), 6.75)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'gag11.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

# ---------- encode ----------
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = BASE/'halloween/BB_Halloween_Reel_PumpkinHead.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=11.7:d=0.5[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','12.2',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
