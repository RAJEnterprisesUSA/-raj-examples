import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep20')
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
    pg.evaluate("setReel(20)")
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

def flutter(at, dur=0.7, vol=0.22):
    # paper flutter: pulsed filtered noise
    n = int(dur*SR); t = np.arange(n)/SR
    s = np.random.randn(n)
    s = np.convolve(s, np.ones(30)/30, 'same')
    s *= (0.5+0.5*np.sin(2*np.pi*13*t))*env(n,0.02,0.2)*vol
    add(s, at)

# theme sting
add(tone(392.00,0.20,0.55,'square'), 0.00)
add(tone(587.33,0.34,0.55,'square'), 0.22)
# bowl set down + entrance steps
add(noise(0.06,0.25,lp=0.05), 0.4); add(tone(120,0.08,0.3), 0.4)
for i in range(6):
    add(noise(0.035,0.16,lp=0.09), 0.3+i*0.22)
# innocent whistle (Unc)
for i,f in enumerate((880, 1046, 988, 880)):
    add(tone(f,0.16,0.12,'sine',vib=5), 1.9+i*0.22)
# sneaky grabs: slide + candy clink
for at in (2.8, 4.2):
    n=int(0.3*SR)
    sw=np.convolve(np.random.randn(n),np.ones(30)/30,'same')*env(n,0.04,0.1)*0.28
    add(sw, at)
    add(tone(1400,0.05,0.2), at+0.2)
# ?! sting + record scratch at freeze
add(tone(880,0.09,0.42), 4.5); add(tone(1174.7,0.16,0.42), 4.6)
sc_n=int(0.28*SR); sc_t=np.arange(sc_n)/SR
scr=np.random.randn(sc_n)*np.sin(2*np.pi*9*sc_t)
scr=np.convolve(scr,np.ones(8)/8,'same')*env(sc_n,0.01,0.1)*0.55
add(scr, 5.2)
# sheepish sad note
add(tone(246.94,0.3,0.3,'sine',bend=-0.08), 6.6)
# idea ding + refill pours
add(tone(1046.5,0.3,0.3), 8.6)
for i in range(4):
    add(tone(1300+i*120,0.05,0.2), 9.6+i*0.1)
add(tone(1567.98,0.3,0.26), 10.0)
# chair pop + mini bowl set
add(noise(0.06,0.28,lp=0.05), 10.85); add(tone(110,0.08,0.3), 10.85)
add(noise(0.04,0.2,lp=0.06), 11.3)
# sit + happy munching clicks
add(noise(0.06,0.25,lp=0.05), 12.8)
for i in range(4):
    add(tone(1500,0.03,0.12), 13.2+i*0.3)
# THE FIRST W: triumphant little fanfare
for i,f in enumerate((523.25, 659.25, 783.99, 1046.5)):
    add(tone(f,0.22,0.4,'square'), 14.7+i*0.15)
add(tone(1318.5,0.5,0.3), 15.35)
# theme reprise over end card
add(tone(392.00,0.20,0.45,'square'), 19.20)
add(tone(587.33,0.40,0.45,'square'), 19.42)
A = A/np.max(np.abs(A))*0.8
pcm = (A*32767).astype(np.int16)
wav_path = WORK/'ep20.wav'
with wave.open(str(wav_path),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio done')

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
out = OUT/'BB_Chronicles_Ep20_TheFirstW.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=20.2:d=0.8[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','21.0',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
