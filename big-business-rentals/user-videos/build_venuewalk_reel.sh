set -e
cd /tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad
FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
GR="eq=contrast=1.07:saturation=1.2:brightness=0.004,vibrance=intensity=0.22,colorbalance=rs=-0.03:bs=0.05:rh=0.04:bh=-0.05,unsharp=5:5:0.5,vignette=PI/4.6,noise=alls=6:allf=t"
BARS="drawbox=x=0:y=0:w=1080:h=96:color=black@1:t=fill,drawbox=x=0:y=1824:w=1080:h=96:color=black@1:t=fill"
PUNCH="zoompan=z='1+0.05*on/(30*11.2)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"
$FF -y -i base.mp4 -loop 1 -t 3.4 -i flyer_venuewalk.png -loop 1 -t 2 -i wv1.png -loop 1 -t 2 -i wv2.png -i fx_venue.wav \
 -filter_complex "\
[0:v]$PUNCH,$GR,$BARS,setsar=1[s1];\
[1:v]fps=30,format=yuv420p,setsar=1[s2];\
[s1][s2]xfade=transition=fadeblack:duration=0.5:offset=10.9[xv];\
[xv][2:v]overlay=0:0:enable='between(t,0.2,3.2)'[va];\
[va][3:v]overlay=0:0:enable='between(t,3.7,10.3)',format=yuv420p[vout];\
[0:a]afade=t=out:st=10.6:d=0.9,apad=pad_dur=3.5[yr];\
[yr][4:a]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.891[aout]" \
 -map "[vout]" -map "[aout]" -t 13.9 \
 -c:v libx264 -pix_fmt yuv420p -crf 22 -preset medium -c:a aac -b:a 128k -movflags +faststart \
 /home/user/-raj-examples/big-business-rentals/user-videos/BB_Real_VenueWalk.mp4
