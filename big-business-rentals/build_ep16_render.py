import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep16')
FRAMES = WORK/'frames'
FRAMES.mkdir(parents=True, exist_ok=True)
OUT = BASE.parent/'fb_safe'
OUT.mkdir(exist_ok=True)

FPS = 35
N = 735  # 21.0s @ 35fps

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
    pg.evaluate("setReel(16)")
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
DUR = 21.0
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

# theme sting
add(tone(392.00,0.20,0.55,'square'), 0.00)
add(tone(587.33,0.34,0.55,'square'), 0.22)
# sneak tiptoe steps
for i in range(6):
    add(noise(0.035,0.18,lp=0.09), 0.2+i*0.2)
# Wobbles placed: thud + evil squeak (two descending saw notes)
add(noise(0.07,0.3,lp=0.05), 1.5); add(tone(110,0.1,0.35), 1.5)
add(tone(660,0.16,0.3,'saw',bend=-0.2), 1.75)
add(tone(520,0.22,0.3,'saw',bend=-0.25), 1.95)
# her entrance steps
for i in range(4):
    add(noise(0.04,0.2,lp=0.09), 3.5+i*0.3)
# the silent look
add(tone(523.25,0.18,0.22), 5.25)
# his walk to the chair
for i in range(3):
    add(noise(0.04,0.2,lp=0.09), 8.6+i*0.28)
# sit creak
add(tone(130,0.15,0.3,'saw'), 9.65)
# wobble creak build
cr_n = int(2.6*SR); cr_t = np.arange(cr_n)/SR
creak = (2*((np.cumsum(82*(1+0.3*np.sin(2*np.pi*(4+cr_t*2)*cr_t)))/SR)%1)-1)
creak *= (0.4+0.6*cr_t/2.6)*env(cr_n,0.2,0.4)*0.2
add(creak, 11.5)
# record scratch at freeze
sc_n = int(0.28*SR); sc_t = np.arange(sc_n)/SR
scr = np.random.randn(sc_n)*np.sin(2*np.pi*9*sc_t)
scr = np.convolve(scr, np.ones(8)/8,'same')*env(sc_n,0.01,0.1)*0.55
add(scr, 13.40)
# CRASH
add(noise(0.5,0.9,lp=0.05), 14.30)
for j,at in enumerate((14.42,14.52,14.60,14.70)):
    add(noise(0.08,0.4-j*0.07,lp=0.1), at)
    add(tone(300-j*40,0.06,0.25), at)
# sad two-note (his L)
add(tone(329.63,0.22,0.4,'sine',bend=-0.06), 15.3)
add(tone(261.63,0.40,0.4,'sine',bend=-0.10), 15.56)
# her calm steps past him
for i in range(4):
    add(noise(0.04,0.18,lp=0.09), 15.1+i*0.32)
# elegant chime as she sits
for i,f in enumerate((783.99,987.77,1174.66)):
    add(tone(f,0.3,0.22), 16.5+i*0.1)
# theme reprise over end card
add(tone(392.00,0.20,0.45,'square'), 19.20)
add(tone(587.33,0.40,0.45,'square'), 19.42)
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
out = OUT/'BB_Chronicles_Ep16_TheDemonstration.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=20.2:d=0.8[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','21.0',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
