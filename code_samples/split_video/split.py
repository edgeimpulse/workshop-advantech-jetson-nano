#!/usr/bin/env python
import argparse
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def split(input, output, times):
  if not os.path.exists(output):
        os.makedirs(output)

  with open(times) as f:
    times = f.readlines()

  times = [x.strip() for x in times] 

  for time in times:
    starttime = int(time.split("-")[0])
    endtime = int(time.split("-")[1])
    ffmpeg_extract_subclip(input, starttime, endtime, targetname=output+"/"+str(times.index(time)+1)+".mp4")

if __name__=="__main__":
    print("splitting video into smaller videos") 
    a = argparse.ArgumentParser()
    a.add_argument("--input", help="path to video input")
    a.add_argument("--output", help="path to output")
    a.add_argument("--times", help="path to times txt file")
    args = a.parse_args()
    print(args)
    split(args.input, args.output, args.times)

#exemple: python3 split.py --input ../../dataset/dataset.mp4 --output output --times times.txt