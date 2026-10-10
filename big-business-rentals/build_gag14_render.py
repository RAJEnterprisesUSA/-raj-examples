import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/gag14')
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
    pg.evaluate("setReel(14)")
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
# house groove until the drop (126 bpm), muted after beat cuts at 4.9
STEP = 0.476
t = 0.6
while t < 4.9:
    add(kick(), t)
    add(noise(0.03,0.12,lp=0.4), t+STEP/2)           # hat
    add(tone(55,0.3,0.22,'sine'), t)                  # sub
    t += STEP
# bass riff blips
for i, f in enumerate([220,262,220,196,220,262,294,330]):
    add(tone(f,0.12,0.14,'saw'), 0.84+i*STEP)
# riser into the drop
n = int(1.0*SR); tt = np.arange(n)/SR
ris = np.sin(2*np.pi*np.cumsum(300+900*tt/1.0)/SR)*env(n,0.3,0.2)*0.22
add(ris, 4.2)
# beat CUTS at 4.9 (silence), then THE DROP at 5.2
add(kick(0.9), 5.2)
add(tone(48,0.5,0.5), 5.2)
add(noise(0.4,0.4,lp=0.9), 5.2)                       # crash-ish
# slide whistle: skull flies (up then down)
n = int(0.5*SR); tt = np.arange(n)/SR
up = np.sin(2*np.pi*np.cumsum(600+700*tt/0.5)/SR)*env(n,0.02,0.1)*0.3
add(up, 5.25)
n = int(0.45*SR); tt = np.arange(n)/SR
dn = np.sin(2*np.pi*np.cumsum(1300-800*tt/0.45)/SR)*env(n,0.02,0.1)*0.3
add(dn, 5.78)
# skull bounces (boing + blip)
add(tone(500,0.22,0.4,'sine',bend=-0.5,vib=12), 6.2)
add(tone(640,0.14,0.3,'sine',bend=-0.4,vib=12), 6.55)
# bone rattle
for i in range(5):
    add(tone(1000+(i%3)*180,0.045,0.26), 6.6+i*0.1)
    add(noise(0.03,0.16,lp=0.15), 6.6+i*0.1)
# ?! sting for the reaction
add(tone(880,0.09,0.4), 6.0)
add(tone(1174.7,0.16,0.4), 6.1)
# groove resumes lighter, headless and unbothered
t = 7.0
while t < 11.4:
    add(kick(0.4), t)
    add(noise(0.03,0.09,lp=0.4), t+STEP/2)
    add(tone(55,0.3,0.16,'sine'), t)
    t += STEP
# payoff sparkle
add(tone(1567.98,0.35,0.28), 8.0)

A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'gag14.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = BASE/'halloween/BB_Halloween_Reel_DJBones.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=11.7:d=0.5[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','12.2',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
