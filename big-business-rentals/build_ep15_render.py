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
N = 420

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

# NEW 2-note theme sting: G4 then D5
add(tone(392.00,0.20,0.55,'square'), 0.00)
add(tone(587.33,0.34,0.55,'square'), 0.22)
# poof (Tyler appears)
add(noise(0.28,0.5,lp=0.02), 1.55)
# ?! sting
add(tone(880,0.09,0.45), 1.95)
add(tone(1174.7,0.16,0.45), 2.05)
# sad catchphrase motif (same both times): E4 down to C4, drooping
for at in (3.1, 7.05):
    add(tone(329.63,0.22,0.42,'sine',bend=-0.06), at)
    add(tone(261.63,0.40,0.42,'sine',bend=-0.10), at+0.26)
# stack taps
for i in range(5):
    at = 4.4+i*0.16
    add(noise(0.05,0.35,lp=0.08), at)
    add(tone(180+i*22,0.07,0.3), at)
# record scratch at freeze
sc_n = int(0.28*SR); sc_t = np.arange(sc_n)/SR
scr = np.random.randn(sc_n)*np.sin(2*np.pi*9*sc_t)
scr = np.convolve(scr, np.ones(8)/8,'same')*env(sc_n,0.01,0.1)*0.55
add(scr, 5.10)
# wobble creak
cr_n = int(0.75*SR); cr_t = np.arange(cr_n)/SR
creak = (2*((np.cumsum(88*(1+0.25*np.sin(2*np.pi*5.5*cr_t)))/SR)%1)-1)
creak *= (0.5+0.5*np.sin(2*np.pi*6*cr_t))*env(cr_n,0.05,0.3)*0.22
add(creak, 5.78)
# CRASH
add(noise(0.5,0.9,lp=0.05), 6.50)
for j,at in enumerate((6.62,6.72,6.80,6.90)):
    add(noise(0.08,0.4-j*0.07,lp=0.1), at)
    add(tone(300-j*40,0.06,0.25), at)
# pop-out boing
add(tone(420,0.38,0.5,'sine',bend=-0.62,vib=11), 6.95)

A = A/np.max(np.abs(A))*0.8
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
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=11.7:d=0.5[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','12.2',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
