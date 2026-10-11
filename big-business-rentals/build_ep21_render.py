import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep21')
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
    pg.evaluate("setReel(21)")
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
for i in range(6):
    add(noise(0.035,0.16,lp=0.09), 0.3+i*0.24)
# tape rip + paper rustle
add(noise(0.18,0.3,lp=0.5), 1.7)
add(noise(0.3,0.16,lp=0.2), 1.95)
# chair pop + proud chime
add(noise(0.06,0.26,lp=0.05), 2.2); add(tone(110,0.08,0.3), 2.2)
add(tone(783.99,0.3,0.25), 2.6); add(tone(987.77,0.35,0.2), 2.75)
# her entrance steps (brisk)
for i in range(5):
    add(noise(0.03,0.15,lp=0.09), 3.6+i*0.19)
# DRAG ONE (hers, 4.6-6.0)
slide(4.6, 1.4, 0.3, 9)
# approval sparkle
add(tone(1318.5,0.25,0.18), 6.3)
# her exit steps
for i in range(5):
    add(noise(0.03,0.13,lp=0.09), 7.3+i*0.22)
# DRAG TWO (his, 8.8-10.0)
slide(8.8, 1.2, 0.3, 8)
# dust-off pats
add(noise(0.05,0.2,lp=0.07), 10.15); add(noise(0.05,0.2,lp=0.07), 10.35)
# dash-in whoosh + LIGHTNING DRAG (10.8-11.6, faster pulse)
n=int(0.25*SR); add(np.convolve(np.random.randn(n),np.ones(20)/20,'same')*env(n,0.15,0.08)*0.3, 10.55)
slide(10.8, 0.8, 0.36, 14)
# ?! sting
add(tone(880,0.09,0.42), 11.72); add(tone(1174.7,0.16,0.42), 11.82)
# cat trot pitter-pat
for i in range(8):
    add(noise(0.02,0.1,lp=0.12), 12.0+i*0.12)
# freeze: record scratch + zoom punch
n=int(0.3*SR); t=np.arange(n)/SR
scr=np.sin(2*np.pi*np.cumsum(1200-900*t/0.3)/SR)*env(n,0.01,0.1)*0.3
add(scr, 13.2)
add(tone(60,0.12,0.5,bend=-0.3), 13.2)
# sassy cat two-tone (not a voice, a sting)
add(tone(660,0.12,0.3), 13.4); add(tone(495,0.22,0.3,bend=-0.15), 13.55)
# tense stare drone
add(tone(98,1.2,0.1,'saw',vib=3), 14.1)
# defeat descend
for i,f in enumerate((440,392,349,294)):
    add(tone(f,0.22,0.22), 16.4+i*0.24)
# end-card question sting
add(tone(392.00,0.18,0.3), 17.5)
add(tone(587.33,0.3,0.3), 17.7)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'ep21.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = OUT/'BB_Chronicles_Ep21_TheSeatingChart.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=20.2:d=0.8[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','21.0',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
