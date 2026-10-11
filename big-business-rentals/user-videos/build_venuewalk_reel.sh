set -e
cd /tmp/claude-0/-home-user--raj-examples/f1b174bd-2cbb-57de-a5ad-e48edd214237/scratchpad
FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
V=/root/.claude/uploads/f1b174bd-2cbb-57de-a5ad-e48edd214237/649d0fb7-d2246e80ba944fba857398161aadc257.mov
TM="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
# step 1: trimmed, tonemapped, blur-padded vertical base (11.2s)
$FF -y -i "$V" -filter_complex "\
[0:v]trim=0.3:11.5,setpts=PTS-STARTPTS,$TM,split[main][forbg];\
[forbg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.12[bg];\
[main]scale=1080:810[fg];\
[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,fps=30,format=yuv420p[v];\
[0:a]atrim=0.3:11.5,asetpts=PTS-STARTPTS[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset fast -c:a aac -b:a 160k base.mp4
# step 2: last frame for the freeze tail
$FF -y -sseof -0.1 -i base.mp4 -frames:v 1 last.png
# step 3: concat base + 2.3s freeze, add text overlays
$FF -y -i base.mp4 -loop 1 -t 2.3 -i last.png -loop 1 -t 2 -i wv1.png -loop 1 -t 2 -i wv2.png -loop 1 -t 2 -i wv3.png \
 -filter_complex "\
[1:v]fps=30,format=yuv420p,setsar=1[fr];\
[0:v][fr]concat=n=2:v=1:a=0[vc];\
[vc][2:v]overlay=0:0:enable='between(t,0,3.2)'[va];\
[va][3:v]overlay=0:0:enable='between(t,3.6,9.0)'[vb];\
[vb][4:v]overlay=0:0:enable='between(t,9.4,13.5)',format=yuv420p[vout];\
[0:a]apad=pad_dur=2.3,afade=t=out:st=13.0:d=0.5[aout]" \
 -map "[vout]" -map "[aout]" -t 13.5 \
 -c:v libx264 -pix_fmt yuv420p -crf 22 -preset medium -c:a aac -b:a 128k -movflags +faststart \
 /home/user/-raj-examples/big-business-rentals/user-videos/BB_Real_VenueWalk.mp4
