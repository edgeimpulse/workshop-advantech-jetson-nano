# Workshop Advantech Jetson Nano

This tutorial has been designed for the [PERFECTING FACTORY 5.0 WITH EDGE-POWERED AI](https://www.sparkfun.com/perfecting_factory_5_with_edge) workshop in collaboration with Advantech and Sparkfun.

## Overview


**Context**

Edge Impulse has been provided two videos by Advantech. **Both videos are real cases for a production line and an operation station in a factory respectively.**:

- Production line video dataset:
![production-line](assets/production-line.png)

- Operation station video dataset: 
![protective-equipment-advantech](assets/protective-equipment-advantech.png)

**Objectives:**

Advantech wants to provide an efficient way to manage operation time and productivity calculation in manufacturing assembly. At the current state, there is an administrator looking around to make sure normal productivity:

- **Use case 1:**
For the first use case, the goal is to improve productivity and make human resources more effective through this AI solution for smart factory management.
Administrators can be informed immediately once productivity has something wrong (bottleneck, operator not present, etc...) even though administrators are not at the scene.

![advantech-manufacturing-image](assets/advantech-manufacturing-image.jpeg)

- **Use case 2:**
For the second use case, the video shows a limited-access operation where it is accessible only for specific staff to keep production quality and operational safety.
The allowable staff would be dressed in specified a hat and vest.
With such an AI solution, administrators can be informed immediately once unusual personnel would like to manipulate crucial equipment.

![protective-equipment-advantech-2](assets/protective-equipment-advantech-2.png)


**Tools and Softwares:**

- [Edge Impulse Studio](https://studio.edgeimpulse.com) 
- [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/cli-installation) (optional)
- [Balena Etcher](https://www.balena.io/etcher) to flash the SD card
- [Python 3](https://www.python.org/downloads/) to extract frames from a video

**Hardware:**


- [Advantech AIR-020](https://www.advantech.com/products/65f20c25-f6ef-4ab5-be3c-b7dfa7a833b3/air-020/mod_fcf216c8-3495-4809-b815-61dc008d53a4) or
[NVIDIA Jetson Nano 2GB Developer Kit](https://www.sparkfun.com/products/17244) or [NVIDIA Jetson Nano Developer Kit](https://www.sparkfun.com/products/16271)

![AIR-020-vs-Jetson](assets/air-jetson.png)

- An SD Card (recommended 32 GB UHS-1 card according to Nvidia)
- An ethernet cable
- An external camera (optional)
- Depending on how you want to setup your Jetson Nano you'll need either:
	- an extra computer to communicate with the Jetson Nano directly from the host computer 
	- or a monitor, keyboard and mouse to interact directly with the Jetson Nano.

Please see [Getting Started with Jetson Nano 2GB Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#setup) for more indications.

For this workshop I will use the first option to ease the screen sharing during the screencast.


## Agenda 

- [Introduction](#overview)
- [Installing the dependencies](#installing-the-dependencies)
- [Prepare your dataset](#prepare-your-dataset)
- [Train your Machine Learning Model](#train-your-machine-learning-model)
- [Run your inference on the target](#run-your-inference-on-the-target)

## Installing the dependencies

Although this step should have been done before the workshop, we'll go through it quickly.

*Note that this step can take up to one hour depending on your internet speed.*

Make sure to follow this documentation page to setup your Jetson Nano with Edge Impulse:

[https://docs.edgeimpulse.com/docs/nvidia-jetson-nano](https://docs.edgeimpulse.com/docs/nvidia-jetson-nano)

![setup-hardware-ei-doc](assets/setup-hardware-ei-doc.png)

On the documentation page, go to the `Setting up your Jetson Nano` section and click on the NVIDIA's setup instructions link according to which Jetson Nano you have. You will arrive on Nvidia's getting started page and then download the `Jetson Nano Developer Kit SD Card Image` (about 6.1 GB). Once downloaded, open [Balena Etcher](https://www.balena.io/etcher) to flash the SD card (about 10 to 15 min):

![Balena](assets/Balena.png)

Insert your SD card, connect the ethernet cable, connect the Micro-USB port to your computer and connect the USB-C power source:

![jetson-nano-dev-kit-dli-animation_v002_lores](assets/jetson-nano-dev-kit-dli-animation_v002_lores.mp4)

On your primary computer, open a serial console (`PuTTY` on Windows or `screen` on MacOS and Linux), see the full instruction [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#setup).

Example on MacOS:

```
sudo screen /dev/cu.usbmodem14241201137883 115200
```

Follow the command prompt and once finished, you will be able to log in your Jetson Nano 2GB Developer Kit:

![jetson-welcome-screen](assets/jetson-welcome-screen.png)

All you need to do now is to make sure your device is connected to the internet and run the following command to install Edge Impulse Linux CLI:

```
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/jetson.sh | bash
```


## Prepare your dataset

In most of machine learning projects, collecting data and preparing your dataset is a long and repetitive task. During this workshop, you will be taught how to use a video as the datasource, how to extract sequences of the video (optional but convenient) and finally how to extract frames from the video sequences.

*Edge Impulse core engineering team is currently working on adding video support directly from the studio to ease this process but as of December 2021 it is not yet publicly available.*

To obtain an extract of one of the dataset we will be seeing together, download it from here: [dataset](https://edgeimpulse-public.s3.fr-par.scw.cloud/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/dataset.mp4)


### Extract frames from a video source

I created two python script to help you do that. They can be found under this Github repository. 

*The following actions has been tested on the Jetson Nano 2GB Developer Kit. It should also work on your laptop as long as you have python3 installed properly, Edge Impulse CLI installed (you need Node v14 or higher installed) and a few python packages. All the needed dependencies are already installed on the Jetson Nano.*

First clone this repository:

```
git clone https://github.com/edgeimpulse/workshop-advantech-jetson-nano.git
```

The structure looks like that:

```
├── LICENSE
├── README.md
├── assets
├── code_samples
│   ├── extract_frames
│   │   └── extract_frames.py
│   └── split_video
│       ├── split.py
│       └── times.txt
└── dataset
```

Navigate to the `dataset/` repository and get the video source:

```
cd dataset/
```
```
wget https://edgeimpulse-public.s3.fr-par.scw.cloud/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/Advantech-Workshop/dataset.mp4
```

We won't be focusing on the split_video script during this workshop but it is present because it can help you to extract a video sequence an exact event if needed.

Now, navigate to the `extract_frames` repository:

```
cd ../code_samples/extract_frames
```

and run the following command to execute the script:

```
python3 extract_frames.py --input ../../dataset/dataset.mp4 --output output --frameRate 1 
```

*Explanation: The script takes as an input the video dataset, stores in an output folder each frame, taken once every second*

Here is the full script if you want to have a look:

```
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
```

Now that we have our individual frames, it is time to go to Edge Impulse Studio and create a project. If you do not have an Edge Impulse account yet, start by creating an account on [Edge Impulse Studio](https://studio.edgeimpulse.com) and create a project by selecting an `Image` project and an `Object Detection` model:

![studio-image-project](assets/studio-image-project.png)

![studio-object-detection-project](assets/studio-object-detection-project.png)

![studio-get-started](assets/studio-get-started.png)

Go to the `Data Acquisition` view while we will upload the frames.

Back on your Jetson Nano, make sure you are still under the `code-samples/extract_frames/` folder and run the following command:

```
edge-impulse-uploader output/* 
```

You should see the following output:

```
Edge Impulse uploader v1.14.0
? What is your user name or e-mail address (edgeimpulse.com)? louis-demo
? What is your password? [hidden]
Endpoints:
    API:         https://studio.edgeimpulse.com/v1
    Ingestion:   https://ingestion.edgeimpulse.com

Upload configuration:
    Label:       Not set, will be infered from file name
    Category:    training

? To which project do you want to upload the data? Louis (Demo) / Workshop Advan
tech Sparkfun
[  1/180] Uploading output/101.jpg OK (1929 ms)
[  2/180] Uploading output/109.jpg OK (1945 ms)
[  3/180] Uploading output/116.jpg OK (2551 ms)
...
[179/180] Uploading output/90.jpg OK (2706 ms)
[180/180] Uploading output/93.jpg OK (2335 ms)

Done. Files uploaded successful: 180. Files that failed to upload: 0.
```



*Hint: If you have an external camera connected to your Jetson Nano, you can use the following command to connect your Jetson Nano to the studio and collect images directly from your Jetson Nano: `edge-impulse-linux`*

![studio-custom-data-collection](assets/studio-custom-data-collection.png)

Some users reported a permission issue. To bypass it do:

```
$> whoami
your-username

$> chown -R your-username:your-username ~/.config
```


### Create bounding boxes on your images


## Train your Machine Learning Model

## Run your inference on the target
