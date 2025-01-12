# EaglEye: Road Defects Detector

EaglEye is designed to detect and localize road surface defects like potholes and cracks in real-time. By using advanced object detection models, this project aims to replace manual onsite inspections. Implemented with TensorFlow Lite and YOLOv3 models on a Raspberry Pi equipped with a camera and GPS module, the system uploads detected defects and their precise locations to a cloud database for analysis and record-keeping.

## Table of Contents
- [Features](#features)
- [Proposed Architectures](#proposed-architectures)
  - [TensorFlow Lite](#tensorflow-lite)
  - [YOLOv3](#yolov3)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
  - [For macOS](#for-macos)
  - [For Windows](#for-windows)
- [Running the System](#running-the-system)
- [Code Features](#code-features)
- [Results and Observations](#results-and-observations)
- [Contributing](#contributing)

## Features
- **Real-Time Detection**: Utilizes a camera and GPS module integrated with a Raspberry Pi to detect road defects.
- **Cloud Integration**: Uploads detected defects and their GPS-tagged locations to a cloud database.
- **Transfer Learning**: Leverages pre-trained models for efficient and accurate detection.

## Proposed Architectures

### TensorFlow Lite
- **Model**: EfficientDet-Lite[0-4], optimized for mobile and IoT applications.
- **Dataset Split**:
  - 90% for training
  - 10% for validation/testing
- **Training Configuration**:
  - Epochs: 300
  - Batch Size: 32
  - Image Size: 320×320 pixels

### YOLOv3
- **Model**: Customized YOLOv3 architecture with Darknet-53 backbone.
- **Dataset Split**:
  - 85% for training
  - 15% for testing
- **Training Configuration**:
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
```bash
# Install Python
brew install python3

# Install Required Libraries
pip3 install tensorflow tensorflow-lite numpy opencv-python matplotlib

# Clone the Repository
git clone https://github.com/aroramoksh11/eagle-eye.git
cd eagle-eye

# Download Pre-trained Models
# Place the TensorFlow Lite and YOLOv3 model files in the `models/` directory

# Set Up Cloud Database
# Configure your database credentials in `config.json`
```

### For Windows
```bash
# Install Python
# Download and install Python from https://www.python.org/

# Install Required Libraries
pip install tensorflow tensorflow-lite numpy opencv-python matplotlib

# Clone the Repository
git clone https://github.com/aroramoksh11/eagle-eye.git
cd eagle-eye

# Download Pre-trained Models
# Place the TensorFlow Lite and YOLOv3 model files in the `models/` directory

# Set Up Cloud Database
# Configure your database credentials in `config.json`
```

## Running the System

1. **Prepare the Raspberry Pi**:
   - Install Raspbian OS and set up the camera and GPS modules.
2. **Start the Program**:
   ```bash
   python3 main.py
   ```
3. **View Outputs**:
   - The system displays detected defects on the console along with their GPS locations.
   - Annotated images are uploaded to the cloud database.

## Code Features
- **Object Detection**: Identifies road defects like potholes and cracks (longitudinal, transverse, alligator).
- **Real-Time Video Processing**: Processes video streams frame-by-frame for defect detection.
- **Bounding Boxes**: Draws bounding boxes around detected defects with confidence scores.
- **FPS Calculation**: Displays real-time Frames Per Second (FPS) on the output.
- **Non-Maximum Suppression**: Filters overlapping bounding boxes for accurate detection.
- **Custom Thresholds**: Allows for confidence thresholds to classify defects.

## Results and Observations
- TensorFlow Lite was faster, making it ideal for IoT devices.
- YOLOv3 delivered higher accuracy but required more computational power.
- Real-time defect detection and localization were successfully achieved.

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. Potential contributions include:
- Improving model accuracy
- Enhancing processing speed
- Adding support for more defect types

For any questions or ideas, reach out directly. Let’s make this project more accurate and efficient!
