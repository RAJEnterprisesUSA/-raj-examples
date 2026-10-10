import glob, pathlib, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

CHROME = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
BASE = pathlib.Path('/home/user/-raj-examples/big-business-rentals')
WORK = pathlib.Path('/tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad/ep17')
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
    pg.evaluate("setReel(17)")
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
# entrance steps
for i in range(6):
    add(noise(0.035,0.18,lp=0.09), 0.2+i*0.2)
# chair pop + polish squeaks + sparkle ding
add(noise(0.07,0.3,lp=0.05), 1.6); add(tone(110,0.1,0.35), 1.6)
add(tone(760,0.1,0.22,'saw'), 2.45); add(tone(820,0.1,0.22,'saw'), 2.75)
add(tone(1567.98,0.3,0.28), 3.35)
# cat pitter-patter
for i in range(6):
    add(noise(0.025,0.14,lp=0.12), 3.85+i*0.12)
# hop boing + ?! sting
add(tone(500,0.3,0.45,'sine',bend=-0.5,vib=10), 4.62)
add(tone(880,0.09,0.4), 5.15); add(tone(1174.7,0.16,0.4), 5.25)
# shoo whooshes
import numpy as _np
for at in (6.6, 7.0, 7.4):
    n=int(0.16*48000)
    sw=_np.convolve(_np.random.randn(n),_np.ones(22)/22,'same')*env(n,0.02,0.06)*0.35
    add(sw, at)
# bribe ding
add(tone(1046.5,0.25,0.3), 8.85)
# tilt creak
cr_n=int(1.0*48000); cr_t=_np.arange(cr_n)/48000
creak=(2*((_np.cumsum(86*(1+0.25*_np.sin(2*_np.pi*5*cr_t)))/48000)%1)-1)
creak*=(0.5+0.5*_np.sin(2*_np.pi*6*cr_t))*env(cr_n,0.06,0.3)*0.2
add(creak, 10.8)
# walk off and back
for i in range(4):
    add(noise(0.035,0.16,lp=0.09), 12.0+i*0.2)
for i in range(4):
    add(noise(0.035,0.16,lp=0.09), 12.7+i*0.2)
# decoy chair pop
add(noise(0.07,0.3,lp=0.05), 13.0); add(tone(110,0.1,0.35), 13.0)
# record scratch at freeze
sc_n=int(0.28*48000); sc_t=_np.arange(sc_n)/48000
scr=_np.random.randn(sc_n)*_np.sin(2*_np.pi*9*sc_t)
scr=_np.convolve(scr,_np.ones(8)/8,'same')*env(sc_n,0.01,0.1)*0.55
add(scr, 13.40)
# sit
add(noise(0.06,0.3,lp=0.05), 14.85); add(tone(120,0.1,0.3), 14.85)
# cat hop boing + lap land
add(tone(520,0.26,0.4,'sine',bend=-0.45,vib=9), 15.5)
add(noise(0.05,0.25,lp=0.04), 15.85)
# sad two-note
add(tone(329.63,0.22,0.42,'sine',bend=-0.06), 16.3)
add(tone(261.63,0.40,0.42,'sine',bend=-0.10), 16.56)
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
out = OUT/'BB_Chronicles_Ep17_TheDecoy.mp4'
cmd = [FF,'-y','-framerate',str(FPS),'-i',str(FRAMES/'%04d.png'),
 '-i',str(wav_path),
 '-filter_complex','[0:v]scale=1080:1920:flags=lanczos[v];[1:a]afade=t=out:st=20.2:d=0.8[a]',
 '-map','[v]','-map','[a]',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium',
 '-c:a','aac','-b:a','128k','-movflags','+faststart','-t','21.0',str(out)]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.returncode, r.stderr[-400:] if r.returncode else 'encoded', out)
