import argparse
import cv2
import os

def extractImages(input, output, frameRate):
    if not os.path.exists(output):
        os.makedirs(output)

    count=1
    vidcap = cv2.VideoCapture(input)

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite(output+"/"+str(count)+".jpg", image) # Save frame as JPG file
        return hasFrames

    sec = 0
    frameRate = int(frameRate) # Change this number to 1 for each 1 second, 0.5 for 500ms etc...
    # frameRate = 0.5 # Use this line if you want to take 2 images per second
        
    success = getFrame(sec)
    while success:
        print ('Read a new frame: ', success, '; at ', sec, 's ; frame number: ', count)
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
        

if __name__=="__main__":
    print("Extracting Frames from video")
    a = argparse.ArgumentParser()
    a.add_argument("--input", help="path to video input")
    a.add_argument("--output", help="path to images")
    a.add_argument("--frameRate", help="frame rates, set 1 for 1 image per second, 2 for 1 images every 2 seconds, etc...")
    args = a.parse_args()
    print(args)
    extractImages(args.input, args.output, args.frameRate)

# example: python3 extract_frames.py --input ../../dataset/dataset.mp4 --output output --frameRate 2 