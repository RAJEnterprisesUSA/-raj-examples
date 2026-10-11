import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep22')
FRAMES = WORK/'frames'
FRAMES.mkdir(parents=True, exist_ok=True)
OUT = BASE.parent/'fb_safe'
OUT.mkdir(exist_ok=True)

FPS = 35
N = 735  # 21.0s @ 35fps

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
    pg.evaluate("setReel(22)")
    pg.evaluate("drawFrame(0)"); pg.evaluate("drawFrame(0)")
    cv = pg.locator('canvas')
    for i in range(N):
        pg.evaluate(f"drawFrame({i/FPS})")
        cv.screenshot(path=str(FRAMES/f'{i:04d}.png'))
    b.close()
print('frames done')

SR = 48000
DUR = 21.0
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

def slide(at, dur, vol=0.3, rate=9):
    # furniture drag: pulsed low rumble
    n = int(dur*SR); t = np.arange(n)/SR
    s = np.convolve(np.random.randn(n), np.ones(60)/60, 'same')
    s *= (0.6+0.4*np.sin(2*np.pi*rate*t))*env(n,0.08,0.25)*vol
    add(s, at)
    add(tone(130,dur,0.12,'saw',vib=6), at)

# theme sting
add(tone(392.00,0.20,0.55,'square'), 0.00)
add(tone(587.33,0.34,0.55,'square'), 0.22)
# entrance steps
for i in range(5):
    add(noise(0.035,0.16,lp=0.09), 0.3+i*0.24)
# the one pumpkin: soft pop + proud chime
add(noise(0.05,0.24,lp=0.05), 1.55); add(tone(110,0.07,0.25), 1.55)
add(tone(783.99,0.3,0.22), 2.7); add(tone(987.77,0.3,0.18), 2.85)
# TYLER APPEARS: record scratch + ?! sting at the freeze
n=int(0.3*SR); t=np.arange(n)/SR
scr=np.sin(2*np.pi*np.cumsum(1200-900*t/0.3)/SR)*env(n,0.01,0.1)*0.3
add(scr, 4.5)
add(tone(880,0.09,0.42), 4.55); add(tone(1174.7,0.16,0.42), 4.65)
add(tone(60,0.12,0.4,bend=-0.3), 4.5)
# shy intern mumble beat (soft low two-note)
add(tone(220,0.14,0.18), 5.6); add(tone(196,0.2,0.16), 5.8)
# decorating frenzy: pop-pop-pop for each pumpkin + busy steps
for i in range(10):
    at=6.6+i*0.5
    add(noise(0.04,0.2,lp=0.05), at); add(tone(130+(i%3)*30,0.06,0.22), at)
for i in range(16):
    add(noise(0.028,0.12,lp=0.09), 6.8+i*0.33)
# garland whoosh
n=int(0.6*SR)
add(np.convolve(np.random.randn(n),np.ones(26)/26,'same')*env(n,0.3,0.2)*0.26, 11.5)
# committee entrance heels
for i in range(5):
    add(noise(0.03,0.18,lp=0.06), 12.5+i*0.2)
# verdict: APPROVED sting + gavel knock
add(tone(90,0.12,0.4), 14.9)
add(tone(523.25,0.16,0.3), 15.0); add(tone(659.25,0.16,0.3), 15.16); add(tone(783.99,0.3,0.32), 15.32)
# sad descend for MBB
for i,f in enumerate((440,392,349,294)):
    add(tone(f,0.22,0.2), 16.5+i*0.24)
# end-card question sting
add(tone(392.00,0.18,0.3), 17.5)
add(tone(587.33,0.3,0.3), 17.7)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'ep22.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = OUT/'BB_Chronicles_Ep22_TheDecorationCommittee.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=20.2:d=0.8[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','21.0',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
