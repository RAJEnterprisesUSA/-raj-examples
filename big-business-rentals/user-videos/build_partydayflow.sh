set -e
FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
B=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237/7e42504f-IMG_2274.mov
A=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237/24e2d437-IMG_1539.mov
P=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237/14f8aac4-image.jpg
TM="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=1080:1920,setsar=1"
$FF -y -i "$B" -i "$P" -i "$A" -loop 1 -t 2 -i ov1.png -loop 1 -t 2 -i ov2.png -loop 1 -t 2 -i ov3.png -loop 1 -t 2 -i ov4.png \
 -filter_complex "\
[0:v]trim=0.5:8.5,setpts=PTS-STARTPTS,$TM[v0];\
[1:v]crop=850:1512:583:0,scale=1080:1920,format=yuv420p,setsar=1,loop=loop=60:size=1:start=0,setpts=N/30/TB,fps=30[v1];\
[2:v]trim=1.0:9.5,setpts=PTS-STARTPTS,$TM[v2];\
[v0][v1][v2]concat=n=3:v=1:a=0[vc];\
[vc][3:v]overlay=0:0:enable='between(t,0,3.2)'[va];\
[va][4:v]overlay=0:0:enable='between(t,8.2,10.0)'[vb];\
[vb][5:v]overlay=0:0:enable='between(t,10.3,13.3)'[vd];\
[vd][6:v]overlay=0:0:enable='between(t,15.0,18.4)',fps=30,format=yuv420p[vout];\
[0:a]atrim=0.5:10.5,asetpts=PTS-STARTPTS[a0];\
[2:a]atrim=1.0:9.5,asetpts=PTS-STARTPTS[a2];\
[a0][a2]concat=n=2:v=0:a=1,afade=t=out:st=18.0:d=0.5[aout]" \
 -map "[vout]" -map "[aout]" -t 18.5 \
 -c:v libx264 -pix_fmt yuv420p -crf 23 -preset medium -c:a aac -b:a 160k -movflags +faststart \
 /home/user/-raj-examples/big-business-rentals/user-videos/BB_Real_PartyDayFlow.mp4
