import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep15')
FRAMES = WORK/'frames'
FRAMES.mkdir(parents=True, exist_ok=True)
OUT = BASE.parent/'fb_safe'
OUT.mkdir(exist_ok=True)

FPS = 35
N = 1838  # 52.5s @ 35fps

# ---------- frames ----------
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width':540,'height':960}, device_scale_factor=2)
    pg.goto('file://'+str(BASE/'reelsD.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.evaluate("""async()=>{
      const F=['900 48px "Archivo Black"','600 30px Oswald','700 30px Montserrat','600 30px Montserrat','900 italic 40px Playfair'];
      for(const f of F){ try{ await document.fonts.load(f);}catch(e){} }
    }""")
    pg.wait_for_timeout(600)
    pg.evaluate("setReel(15)")
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
DUR = 52.5
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

import pathlib as _pl, wave as _wv
VO = _pl.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/vo')
def vo(name, at, vol=1.0):
    with _wv.open(str(VO/(name+'.wav'))) as w:
        d = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64)/32768.0
    add(d*vol, at)

# theme sting
add(tone(392.00,0.20,0.5,'square'), 0.00)
add(tone(587.33,0.34,0.5,'square'), 0.22)
# VO
vo('01_narr_intro',   0.60)
vo('02_mbb_bigday',   5.60)
vo('03_mbb_where',   11.60)
vo('04_ty_intern1',  14.30)
vo('05_mbb_stack',   17.00)
vo('06_ty_sayless',  21.60)
vo('07_narr_literal',25.00)
vo('08_mbb_ladder',  33.00)
vo('09_ty_intern2',  39.20)
vo('10_narr_outro',  41.80)
# chair place thuds
for at in (2.0, 3.6):
    add(noise(0.07,0.3,lp=0.05), at); add(tone(110,0.1,0.35), at)
# poof
add(noise(0.28,0.45,lp=0.02), 10.6)
# ?! sting
add(tone(880,0.09,0.4), 11.30); add(tone(1174.7,0.16,0.4), 11.40)
# sad catchphrase motif both times
for at in (14.3, 39.2):
    add(tone(329.63,0.22,0.3,'sine',bend=-0.06), at)
    add(tone(261.63,0.40,0.3,'sine',bend=-0.10), at+0.26)
# stack taps
for i in range(5):
    at = 24.8+i*0.55
    add(noise(0.05,0.3,lp=0.08), at); add(tone(180+i*22,0.07,0.25), at)
# record scratch at freeze
sc_n=int(0.28*SR); sc_t=np.arange(sc_n)/SR
scr=np.random.randn(sc_n)*np.sin(2*np.pi*9*sc_t)
scr=np.convolve(scr,np.ones(8)/8,'same')*env(sc_n,0.01,0.1)*0.5
add(scr, 32.0)
# wobble creak
cr_n=int(0.8*SR); cr_t=np.arange(cr_n)/SR
creak=(2*((np.cumsum(88*(1+0.25*np.sin(2*np.pi*5.5*cr_t)))/SR)%1)-1)
creak*=(0.5+0.5*np.sin(2*np.pi*6*cr_t))*env(cr_n,0.05,0.3)*0.2
add(creak, 36.6)
# CRASH
add(noise(0.5,0.85,lp=0.05), 37.5)
for j,at in enumerate((37.62,37.72,37.80,37.90)):
    add(noise(0.08,0.38-j*0.07,lp=0.1), at); add(tone(300-j*40,0.06,0.22), at)
# pop-out boing
add(tone(420,0.38,0.45,'sine',bend=-0.62,vib=11), 38.3)
# theme reprise over end card
add(tone(392.00,0.20,0.45,'square'), 46.20)
add(tone(587.33,0.40,0.45,'square'), 46.42)
A = A/np.max(np.abs(A))*0.87
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'ep15.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

# ---------- encode ----------
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = OUT/'BB_Chronicles_Ep15_TheNewIntern.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=51.5:d=1.0[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','52.5',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
