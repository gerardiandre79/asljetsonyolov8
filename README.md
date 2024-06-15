# American Sign Language detector - NVIDIA Jetson Nano
American Sign Language detection with Jetson Nano and YOLOv8

Hello World! I am using GIT.

This is my second commit.

# Citations
This is a project for the Jetson Community and couldn't be possible without the effort of other developers:
  - https://developer.nvidia.com/embedded/community
  - https://forums.developer.nvidia.com/
    
All the YOLOV8 code and documentation can be found here:
  - https://docs.ultralytics.com/

Literature related to American Sign Language (ASL):
- https://en.wikipedia.org/wiki/American_Sign_Language

# Index
0.  [Project Description](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#project-description)
1.  [Dataset](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#dataset)
2.  [YOLOv8](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#yolov8)
3.  [Test](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#test)

# Project Description
The aims of this project is to show how it is possible to detect all the signs belonging to the American Sign Language automatically thanks to the capabilities of Nvidia Jetson Nano and YOLOv8.

With OpenCV and a public dataset on Roboflow I trained a customized version of the YOLOv8 model for real-time ASL letters detection.

All the operations are intended to be executed through a Remote Desktop Connection between my own MacBook Pro and Jetsono Nano.

At the end, AI will permits you to recognize Sign Language, with real-time detection and a line written in terminal.

# Dataset

The dataset is freely available [here](https://public.roboflow.com/object-detection/american-sign-language-letters/1). It has a lot of images: 1512 for training, 144 for validation and 72 for testing. The problem is the type of images. They are very accurate and very clear, yet they look very similar to each other and do not fit new contexts.

Each letter represent exactly one class :
- [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

# YOLOv8
- Checking whether YOLOv8 is intalled and it is working fine
- Importing the American Sign Language Alphabets Dataset from Roboflow
- Train the YOLOv8 Model on the Custom Dataset
- Now, you can inference with Custom Model

# Test
Finally we can observe the result of the inference on the trained dataset (Letter A, prob : 0.76):
![American Sign Language - Sign of Letter A](/images/A22_jpg.rf.f02ad8558ce1c88213b4f83c0bc66bc8.jpg)
![American Sign Language - Sign of Letter A Detected](/images/A22_jpg.rf.f02ad8558ce1c88213b4f83c0bc66bc8p.jpg)



