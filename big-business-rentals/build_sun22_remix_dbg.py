"""Debug bounding boxes for REELS[60]: renders each element alone (sky off) and prints its alpha bbox in 1080x1920 canvas px."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent/'audio'))
from render30 import CHROME, BASE
from playwright.sync_api import sync_playwright
T = [float(a) for a in sys.argv[1:]] or [18.0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=1)
    pg.goto('file://' + str(BASE/'halloween/reelH.html'))
    pg.wait_for_function("document.fonts.status==='loaded'")
    pg.wait_for_timeout(800)
    pg.evaluate("setReel(60)")
    res = pg.evaluate("""(T)=>{
      const out={}; const W0=W, H0=H;
      const bbox=()=>{ const d=ctx.getImageData(0,0,cv.width,cv.height); const sx=cv.width/W0; let x0=1e9,y0=1e9,x1=-1,y1=-1;
        for(let y=0;y<cv.height;y+=2){ for(let x=0;x<cv.width;x+=2){ if(d.data[(y*cv.width+x)*4+3]>40){ if(x<x0)x0=x; if(x>x1)x1=x; if(y<y0)y0=y; if(y>y1)y1=y; } } }
        return x1<0?null:[Math.round(x0/sx),Math.round(y0/sx),Math.round(x1/sx),Math.round(y1/sx)]; };
      const sky=skyT59, ch=chairT60, tb=tableT60, dg=drawGuestT60, kwp=kidWithProp, cat=drawCat, pl=placeCardT60, pills=pillsT60, tip=tipCardT60, sc=speakCloud, cp=captionPop, hp=headphonesK, ph=phoneK;
      const noop=()=>{};
      for(const t of T){
        const r={};
        const run=(name,cfg)=>{ window.skyT59=noop; window.chairT60=cfg.chair?ch:noop; window.tableT60=cfg.table?tb:noop; window.placeCardT60=noop; window.pillsT60=noop; window.tipCardT60=noop; window.speakCloud=noop; window.captionPop=noop;
          window.drawCat=cfg.cat?cat:noop; window.headphonesK=cfg.guest==="VAEH"?hp:noop; window.phoneK=cfg.guest==="VAEH"?ph:noop;
          window.drawGuestT60=(tt,g,P,e)=>{ if(cfg.guest===g.n) dg(tt,g,P,e); };
          window.kidWithProp=(pp,s)=>{ if(pp.style===STYLER2){ if(cfg.dad) kwp(pp,s); } else kwp(pp,s); };
          ctx.setTransform(1,0,0,1,0,0); ctx.clearRect(0,0,cv.width,cv.height); REELS[60](t); r[name]=bbox(); };
        run('chairs',{chair:true}); run('table',{table:true}); run('dad',{dad:true}); run('cat',{cat:true});
        ['LIL','BABY','UNC','VAEH'].forEach(n=>run(n,{guest:n}));
        out[t]=r;
      }
      window.skyT59=sky; window.chairT60=ch; window.tableT60=tb; window.drawGuestT60=dg; window.kidWithProp=kwp; window.drawCat=cat;
      return out; }""", T)
    for t, r in res.items():
        print('t=%s' % t)
        for k, v in r.items(): print('  %-6s %s' % (k, v))
    b.close()
