import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/gag16')
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
    pg.evaluate("setReel(16)")
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

def kick(vol=0.55):
    n = int(0.16*SR); t = np.arange(n)/SR
    f = 120*np.exp(-t*26)+44
    return vol*np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,0.001,0.06)

# two-note theme sting
add(tone(220.00,0.22,0.5,'square'), 0.00)
add(tone(329.63,0.34,0.5,'square'), 0.24)
# chair pop + entrance steps
add(noise(0.06,0.28,lp=0.05), 0.25); add(tone(110,0.08,0.3), 0.25)
for i in range(4):
    add(noise(0.035,0.16,lp=0.09), 0.2+i*0.2)
# bone rattle as the models walk in
for i in range(5):
    add(tone(1000+(i%3)*180,0.04,0.2), 0.95+i*0.1)
# camera flashes: charge whine + CLICK + flash poof
for f in (2.4, 4.6, 6.8):
    n = int(0.5*SR); tt = np.arange(n)/SR
    whine = np.sin(2*np.pi*np.cumsum(900+700*tt/0.5)/SR)*env(n,0.2,0.1)*0.1
    add(whine, f-0.5)
    add(tone(1800,0.04,0.45), f)               # click
    add(noise(0.12,0.3,lp=0.8), f+0.02)        # flash poof
# pose scramble rattles after each flash
for f in (2.7, 4.9, 7.1):
    for i in range(4):
        add(tone(950+(i%3)*200,0.045,0.22), f+i*0.09)
        add(noise(0.025,0.14,lp=0.15), f+i*0.09)
# head pop off (the keeper pose)
add(tone(500,0.2,0.35,'sine',bend=-0.5,vib=10), 7.15)
# sparkle: that is the one
add(tone(1567.98,0.35,0.3), 7.5)
add(tone(2093.0,0.3,0.2), 7.65)
# payoff two-note
add(tone(392.00,0.18,0.3), 8.3)
add(tone(587.33,0.3,0.3), 8.5)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'gag16.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = BASE/'halloween/BB_Halloween_Reel_PhotoBooth.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=11.7:d=0.5[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','12.2',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
