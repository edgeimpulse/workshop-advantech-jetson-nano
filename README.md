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

### Create bounding boxes on your images


## Train your Machine Learning Model

## Run your inference on the target
