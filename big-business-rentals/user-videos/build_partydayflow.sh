set -e
cd /tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad
FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
U=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237
B=$U/7e42504f-IMG_2274.mov
C=$U/f449182f-IMG_2269.mov
D=$U/0faae95b-IMG_2270.mov
P=$U/14f8aac4-image.jpg
A=$U/24e2d437-IMG_1539.mov
TM="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=1080:1920"
GR="eq=contrast=1.07:saturation=1.2:brightness=0.004,vibrance=intensity=0.22,colorbalance=rs=-0.03:bs=0.05:rh=0.04:bh=-0.05,unsharp=5:5:0.5,vignette=PI/4.6,noise=alls=6:allf=t"
BARS="drawbox=x=0:y=0:w=1080:h=96:color=black@1:t=fill,drawbox=x=0:y=1824:w=1080:h=96:color=black@1:t=fill"
PUNCH1="zoompan=z='1+0.06*on/(30*4.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"
PUNCH2="zoompan=z='1+0.06*on/(30*4.0)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"
PUNCH3="zoompan=z='1+0.06*on/(30*5.0)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"
PUNCH5="zoompan=z='1+0.05*on/(30*8.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"

$FF -y -i "$D" -i "$C" -i "$B" -i "$P" -i "$A" \
 -loop 1 -t 3 -i flyer_pdflow.png \
 -loop 1 -t 2 -i ov1.png -loop 1 -t 2 -i ov2.png -loop 1 -t 2 -i ov3.png \
 -i fx_bed.wav \
 -filter_complex "\
[0:v]trim=1:5.5,setpts=PTS-STARTPTS,$TM,$PUNCH1,$GR,$BARS,setsar=1[s1];\
[1:v]trim=2:6,setpts=PTS-STARTPTS,$TM,$PUNCH2,$GR,$BARS,setsar=1[s2];\
[2:v]trim=0.5:5.5,setpts=PTS-STARTPTS,$TM,$PUNCH3,$GR,$BARS,setsar=1[s3];\
[3:v]split[p1][p2];\
[p1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.12[pbg];\
[p2]scale=1080:810[pfg];\
[pbg][pfg]overlay=(W-w)/2:(H-h)/2,format=yuv420p,loop=loop=60:size=1:start=0,setpts=N/30/TB,fps=30,$GR,$BARS,setsar=1[s4];\
[4:v]trim=1.0:9.5,setpts=PTS-STARTPTS,$TM,$PUNCH5,$GR,$BARS,setsar=1[s5];\
[5:v]fps=30,format=yuv420p,setsar=1[s6];\
[s1][s2]xfade=transition=slideleft:duration=0.3:offset=4.2[x1];\
[x1][s3]xfade=transition=slideleft:duration=0.3:offset=7.9[x2];\
[x2][s4]xfade=transition=fade:duration=0.3:offset=12.6[x3];\
[x3][s5]xfade=transition=fadeblack:duration=0.3:offset=14.3[x4];\
[x4][s6]xfade=transition=fadeblack:duration=0.5:offset=22.5[xv];\
[xv][6:v]overlay=0:0:enable='between(t,0.2,3.4)'[va];\
[va][7:v]overlay=0:0:enable='between(t,12.8,14.2)'[vb];\
[vb][8:v]overlay=0:0:enable='between(t,14.7,17.7)',format=yuv420p[vout];\
[0:a]atrim=1:5.5,asetpts=PTS-STARTPTS[a1];\
[1:a]atrim=2:6,asetpts=PTS-STARTPTS[a2];\
[2:a]atrim=0.5:7.5,asetpts=PTS-STARTPTS[a3];\
[4:a]atrim=1.0:9.5,asetpts=PTS-STARTPTS[a5];\
[a1][a2]acrossfade=d=0.3[y1];\
[y1][a3]acrossfade=d=0.3[y2];\
[y2][a5]acrossfade=d=0.3[y3];\
[y3]afade=t=out:st=22.2:d=0.9,apad=pad_dur=3,volume=1.0[yreal];\
[yreal][9:a]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.891[aout]" \
 -map "[vout]" -map "[aout]" -t 25.0 \
 -c:v libx264 -pix_fmt yuv420p -crf 22 -preset medium -c:a aac -b:a 160k -movflags +faststart \
 /home/user/-raj-examples/big-business-rentals/user-videos/BB_Real_PartyDayFlow.mp4
