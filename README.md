# American Sign Language detector - NVIDIA Jetson Nano
American Sign Language detection with Jetson Nano and YOLOv8

# Citations
This is a project for the Jetson Community and couldn't be possible without the effort of other developers:
  - https://developer.nvidia.com/embedded/community
  - https://forums.developer.nvidia.com/
    
All the YoloV8 code and documentation can be found here:
  - https://docs.ultralytics.com/

# Index
0.  [Project Description](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#project-description)
1.  [Dataset](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#dataset)
2.  [Network Connection](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#network-connection)
3.  [Neural Network](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#neural-network)
4.  [Test](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#test)
5.  [Conclusions](https://github.com/gerardiandre79/asljetsonyolov8/blob/main/README.md#conclusions)

# Project Description
The aims of this project is to show how it is possible to detect all the signs belonging to the American Sign Language automatically thanks to the capabilities of Nvidia Jetson Nano and YOLOv8.

With OpenCV and a public dataset on Roboflow I trained a customized version of the YOLOv8 model for real-time ASL letters detection.

At the end, AI will permits you to recognize Sign Language, with real-time detection and a line written in terminal.

# Dataset

The dataset is freely available [here](https://public.roboflow.com/object-detection/american-sign-language-letters/1). It has a lot of images: 1512 for training, 144 for validation and 72 for testing. The problem is the type of images. They are very accurate and very clear, yet they look very similar to each other and do not fit new contexts.

Each letter represent exactly one class :
- [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

# Network Connection

# Neural Network

# Test
   
# Conclusions
