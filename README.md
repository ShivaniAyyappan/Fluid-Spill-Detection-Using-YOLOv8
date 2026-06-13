# Fluid Spill Detection Using YOLOv8

## Overview
This project uses YOLOv8 to detect fluid spills in real time through webcam input.

## Features
- Real-time spill detection
- YOLOv8 object detection
- Webcam deployment
- Custom trained dataset
- Bounding box visualization

## Technologies Used
- Python
- YOLOv8
- OpenCV
- Ultralytics

## Project Structure

```
Fluid-Spill-Detection-Using-YOLOv8
│
├── train/
│   └── weights/
│       └── best.pt
│
├── webcam.py
├── results.png
├── confusion_matrix.png
└── README.md
```

## Installation

```bash
pip install ultralytics opencv-python
```

## Run

```bash
python webcam.py
```

## Future Improvements

- Improve detection accuracy
- Email alert system
- Automatic screenshot capture
- Mobile deployment
