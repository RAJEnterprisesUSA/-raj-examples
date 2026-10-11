import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/gag18')
FRAMES = WORK/'frames'
FRAMES.mkdir(parents=True, exist_ok=True)

FPS = 35
N = 420

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
    pg.evaluate("setReel(18)")
    pg.evaluate("drawFrame(0)"); pg.evaluate("drawFrame(0)")
    cv = pg.locator('canvas')
    for i in range(N):
        pg.evaluate(f"drawFrame({i/FPS})")
        cv.screenshot(path=str(FRAMES/f'{i:04d}.png'))
    b.close()
print('frames done')

SR = 48000
DUR = 12.2
A = np.zeros(int(SR*DUR))

def add(sig, at):
    i0 = int(at*SR); i1 = min(len(A), i0+len(sig))
    if i1 > i0: A[i0:i1] += sig[:i1-i0]

def env(n, a=0.01, r=0.3):
    e = np.ones(n)
    na, nr = max(1,int(a*SR)), max(1,int(r*SR))
    na, nr = min(na,n), min(nr,n)
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

# two-note theme sting
add(tone(220.00,0.22,0.5,'square'), 0.00)
add(tone(329.63,0.34,0.5,'square'), 0.24)
# entrance steps + tray set-down
for i in range(4):
    add(noise(0.035,0.16,lp=0.09), 0.2+i*0.2)
add(noise(0.06,0.3,lp=0.05), 1.0); add(tone(1500,0.05,0.2), 1.05)
# the lift: eerie shimmer gliss up
n = int(1.2*SR); t = np.arange(n)/SR
gl = np.sin(2*np.pi*np.cumsum(500+700*t/1.2)/SR)*env(n,0.3,0.4)*0.14
add(gl, 1.8)
add(tone(1760,0.5,0.1,vib=6), 2.2)
# ?! sting
add(tone(880,0.09,0.4), 2.05); add(tone(1174.7,0.16,0.4), 2.15)
# chase steps (quick)
for i in range(10):
    add(noise(0.03,0.15,lp=0.09), 2.9+i*0.24)
# ghostly theremin wobble while the tray glides
n = int(2.6*SR); t = np.arange(n)/SR
add(np.sin(2*np.pi*(620+40*np.sin(2*np.pi*1.6*t))*t)*env(n,0.5,0.6)*0.07, 2.6)
# BOO reveal: whoosh + low thud + sparkle
add(noise(0.3,0.3,lp=0.03), 5.4)
add(tone(80,0.14,0.5,bend=-0.3), 5.55)
add(tone(1567.98,0.3,0.25), 5.75); add(tone(2093.0,0.25,0.18), 5.9)
# polite service clinks
for i,f in enumerate((1400,1600,1500)):
    add(tone(f,0.05,0.16), 6.6+i*0.3)
# cup grab + happy sip
add(tone(1500,0.05,0.2), 7.8)
add(tone(523.25,0.2,0.2), 8.2); add(tone(659.25,0.3,0.2), 8.4)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'gag18.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = BASE/'halloween/BB_Halloween_Reel_GhostWaiter.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=11.7:d=0.5[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','12.2',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
