set -e
cd /tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad
FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
U=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237
B=$U/7e42504f-IMG_2274.mov
C=$U/f449182f-IMG_2269.mov
D=$U/0faae95b-IMG_2270.mov
P=$U/14f8aac4-image.jpg
A=$U/24e2d437-IMG_1539.mov
TM="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=1080:1920,setsar=1"
$FF -y -i "$B" -i "$C" -i "$D" -i "$P" -i "$A" \
 -loop 1 -t 2 -i ov1.png -loop 1 -t 2 -i ov2.png -loop 1 -t 2 -i ov3.png -loop 1 -t 2 -i ov4.png \
 -filter_complex "\
[0:v]trim=0.5:5.5,setpts=PTS-STARTPTS,$TM[v0];\
[1:v]trim=2:6,setpts=PTS-STARTPTS,$TM[v1];\
[2:v]trim=1:5.5,setpts=PTS-STARTPTS,$TM[v2];\
[3:v]split[p1][p2];\
[p1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.12[pbg];\
[p2]scale=1080:810[pfg];\
[pbg][pfg]overlay=(W-w)/2:(H-h)/2,format=yuv420p,setsar=1,loop=loop=60:size=1:start=0,setpts=N/30/TB,fps=30[v3];\
[4:v]trim=1.0:9.5,setpts=PTS-STARTPTS,$TM[v4];\
[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[vc];\
[vc][5:v]overlay=0:0:enable='between(t,0,3.2)'[va];\
[va][6:v]overlay=0:0:enable='between(t,13.6,15.5)'[vb];\
[vb][7:v]overlay=0:0:enable='between(t,15.8,18.8)'[vd];\
[vd][8:v]overlay=0:0:enable='between(t,20.8,24.0)',fps=30,format=yuv420p[vout];\
[0:a]atrim=0.5:5.5,asetpts=PTS-STARTPTS[a0];\
[1:a]atrim=2:6,asetpts=PTS-STARTPTS[a1];\
[2:a]atrim=1:7.5,asetpts=PTS-STARTPTS[a2];\
[4:a]atrim=1.0:9.5,asetpts=PTS-STARTPTS[a4];\
[a0][a1][a2][a4]concat=n=4:v=0:a=1,afade=t=out:st=23.5:d=0.5[aout]" \
 -map "[vout]" -map "[aout]" -t 24.0 \
 -c:v libx264 -pix_fmt yuv420p -crf 23 -preset medium -c:a aac -b:a 160k -movflags +faststart \
 /home/user/-raj-examples/big-business-rentals/user-videos/BB_Real_PartyDayFlow.mp4
