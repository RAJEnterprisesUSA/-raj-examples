import json, statistics as st, collections
rows=json.load(open('reports/week3_posts.json'))
VIEW={'tt':'Video Views','ig':'Views','yt':'Video Views','fb':'Impressions'}
def fmt(r):
    s=(r['assets'][0]['source'] if r['assets'] else '').rsplit('/',1)[-1]
    if 'Chronicles' in s: return 'episode'
    if 'BB_Trend_' in s: return 'remix'
    if 'PinkOctober' in s: return 'pink'
    if 'HostingChaos' in s: return 'ai_skit'
    if 'GuessTheTheme' in s: return 'guess_theme'
    if 'FB_People' in s: return 'people'
    if s.endswith('.mp4') or not s: return 'video_other' if s else 'tt_video'
    return 'card'
def m(r,name):
    for x in r['metrics'] or []:
        if x['name']==name: return x['value']
    return None
def week(r):
    d=r['dueAt']
    if d>='2026-10-19T07:00': return 'W3'
    if d>='2026-10-12T07:00': return 'W2'
    return None
# tiktok assets are re-hosted by buffer: map by caption keywords
def tt_fmt(r):
    t=r['text'].lower()
    if 'chronicles' in t or 'ep. ' in t or 'cheap chair' in t or 'worst seat' in t: return 'episode'
    if 'clue' in t or 'guessed it' in t: return 'guess_theme'
    if 'couple people' in t: return 'ai_skit'
    if any(k in t for k in ('porch','face only','broad daylight','roadster','judges')): return 'remix'
    if 'how much would you pay' in t: return 'card'
    if any(k in t for k in ('screening','mammogram','pink','checklist','55')): return 'pink'
    return 'other'
agg=collections.defaultdict(list)
for r in rows:
    w=week(r)
    if not w: continue
    f=tt_fmt(r) if r['ch']=='tt' else fmt(r)
    agg[(r['ch'],w,f)].append(r)
for ch in ('tt','ig','fb','yt'):
    print('=====',ch, VIEW[ch])
    for w in ('W2','W3'):
        tot=[r for k,v in agg.items() if k[0]==ch and k[1]==w for r in v]
        vs=[m(r,VIEW[ch]) for r in tot if m(r,VIEW[ch]) is not None]
        print(f' {w} all: n={len(tot)} median={st.median(vs) if vs else "-"} total={sum(vs) if vs else 0}')
        for (c,ww,f),v in sorted(agg.items()):
            if c!=ch or ww!=w: continue
            vs=[m(r,VIEW[ch]) for r in v if m(r,VIEW[ch]) is not None]
            aw=[m(r,'Avg. Watch Time (sec)') for r in v if m(r,'Avg. Watch Time (sec)') is not None]
            ex=''
            if aw: ex+=f' avgwatch_med={st.median(aw):.1f}s'
            for nm in ('Shares','Comments','Follows','Saves'):
                s=[m(r,nm) for r in v if m(r,nm) is not None]
                if s and sum(s): ex+=f' {nm.lower()}={sum(s):g}'
            print(f'   {f:12s} n={len(v):2d} withdata={len(vs):2d} median={st.median(vs) if vs else "-"} max={max(vs) if vs else "-"}{ex}')
# top posts W3
print('===== TOP W3 by views')
w3=[r for r in rows if week(r)=='W3' and m(r,VIEW[r['ch']]) is not None]
for r in sorted(w3,key=lambda r:-m(r,VIEW[r['ch']]))[:12]:
    print(r['ch'], r['dueAt'][:10], m(r,VIEW[r['ch']]), m(r,'Avg. Watch Time (sec)'), '|', r['text'][:60].replace('\n',' '))
print('pending (no metrics) W3:', sum(1 for r in rows if week(r)=='W3' and not r['metrics']))
