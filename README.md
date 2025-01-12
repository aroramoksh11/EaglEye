# EaglEye: Road Defects Detector

Eagleye is designed to detect and localize road surface defects like potholes and cracks in real-time. By using advanced object detection models, this project aims to make manual onsite inspections a thing of the past. It utilizes TensorFlow Lite and YOLOv3 models, implementing the system on a Raspberry Pi equipped with a camera and GPS module. The detected defects and their precise locations are uploaded to a cloud database for further analysis and record-keeping.

## Table of Contents

1. Features
2. Proposed Architectures
   - TensorFlow Lite
   - YOLOv3
3. System Requirements
4. Installation Guide
   - For macOS
   - For Windows
5. Running the System
6. Code Features
7. Results and Observations
8. Contributing

## Features

- **Real-Time Detection:** The system uses a camera and GPS module integrated with a Raspberry Pi to detect road defects.
- **Cloud Integration:** Detected defects and their GPS-tagged locations are uploaded to a cloud database.
- **Transfer Learning:** Pre-trained models are leveraged to make detection efficient and accurate.

## Proposed Architectures

### TensorFlow Lite

- **Model:** EfficientDet-Lite[0-4], designed for mobile and IoT applications.
- **Dataset Split:**
  - 90% for training
  - 10% for validation/testing
- **Training Configuration:**
  - Epochs: 300
  - Batch Size: 32
  - Image Size: 320×320 pixels

### YOLOv3

- **Model:** Customized YOLOv3 architecture with Darknet-53 backbone.
- **Dataset Split:**
  - 85% for training
  - 15% for testing
- **Training Configuration:**
  - Epochs: 8000
  - Batch Size: 64
  - Image Size: 418×418 pixels

## System Requirements

- Raspberry Pi (with a camera module and GPS integration)
- Python 3.7 or later
- TensorFlow Lite
- YOLOv3 with Darknet
- Cloud database access

## Installation Guide

### For macOS

1. Install Python:
   ```bash
   brew install python3
   ```
2. Install Required Libraries:
   ```bash
   pip3 install tensorflow tensorflow-lite numpy opencv-python matplotlib
   ```
3. Clone the Repository:
   ```bash
   git clone https://github.com/aroramoksh11/eagle-eye.git
   cd eagle-eye
   ```
4. Download Pre-trained Models:
   - Place the TensorFlow Lite and YOLOv3 model files in the `models/` directory.
5. Set Up Cloud Database:
   - Configure your database credentials in `config.json`.

### For Windows

1. Install Python:
   - Download and install Python from [python.org](https://www.python.org/).
2. Install Required Libraries:
   ```bash
   pip install tensorflow tensorflow-lite numpy opencv-python matplotlib
   ```
3. Clone the Repository:
   ```bash
   git clone https://github.com/aroramoksh11/eagle-eye.git
   cd eagle-eye
   ```
4. Download Pre-trained Models:
   - Place the TensorFlow Lite and YOLOv3 model files in the `models/` directory.
5. Set Up Cloud Database:
   - Configure your database credentials in `config.json`.

## Running the System

1. **Prepare the Raspberry Pi:**
   - Install Raspbian OS and set up the camera and GPS modules.
2. **Start the Program:**
   ```bash
   python3 main.py
   ```
3. **View Outputs:**
   - The system displays detected defects on the console along with their GPS locations.
   - Annotated images are uploaded to the cloud database.

## Code Features

- **Object Detection:** Identifies road defects like potholes and cracks (longitudinal, transverse, alligator).
- **Real-Time Video Processing:** Processes video streams frame-by-frame for defect detection.
- **Bounding Boxes:** Draws bounding boxes around detected defects with confidence scores.
- **FPS Calculation:** Displays real-time Frames Per Second (FPS) on the output.
- **Non-Maximum Suppression:** Filters overlapping bounding boxes for accurate detection.
- **Custom Thresholds:** Allows for confidence thresholds to classify defects.

## How to Use the Code

1. Load your YOLO model weights and configuration files.
2. Define the list of classes for detection (e.g., potholes, cracks).
3. Provide a video or image as input to the program.
4. Run the script to see real-time detection and annotations.

## Results and Observations

- TensorFlow Lite was faster, making it ideal for IoT devices.
- YOLOv3 delivered higher accuracy but required more computational power.
- Real-time defect detection and localization were successfully achieved.

## Contributing
If you have any questions or ideas, reach out directly. Let’s make this project more accurate and efficient!
