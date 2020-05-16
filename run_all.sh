#!/usr/bin/env bash


make_rule_video () {
source activate nkos
echo "Creating rule $1"

python rule.py $1 960 540 539
cd $1

ffmpeg -framerate 30 -pattern_type glob -i 'frame*.png' -filter_complex "
[0:v]
drawtext='font=sans-serif:fontsize=60:x=20:y=20:
fontcolor=#96A8C0:
text=$1'
" ../$1.webm
rm frame*.png
cd ..
rmdir $1
}

export -f make_rule_video

seq 1 255|parallel make_rule_video {}
