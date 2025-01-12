Eagle Eye: Road Defects Detection

Eagle Eye, designed to detect and localize road surface defects like potholes and cracks in real-time. By using advanced object detection models, I aim to make manual onsite inspections a thing of the past. I used TensorFlow Lite and YOLOv3 models, implementing the system on a Raspberry Pi equipped with a camera and GPS module. The detected defects and their precise locations are uploaded to a cloud database for further analysis and record-keeping.

Table of Contents

Features

Proposed Architectures

TensorFlow Lite

YOLOv3

System Requirements

Installation Guide

For macOS

For Windows

Running the System

Code Features

Results and Observations

Contributing

Features

Real-Time Detection: The system uses a camera and GPS module integrated with a Raspberry Pi to detect road defects.

Cloud Integration: Detected defects and their GPS-tagged locations are uploaded to a cloud database.

Transfer Learning: I leveraged pre-trained models to make detection efficient and accurate.

Proposed Architectures

TensorFlow Lite

Model: EfficientDet-Lite[0-4], designed for mobile and IoT applications.

Dataset Split:

90% for training

10% for validation/testing

Training Configuration:

Epochs: 300

Batch Size: 32

Image Size: 320×320 pixels

YOLOv3

Model: Customized YOLOv3 architecture with Darknet-53 backbone.

Dataset Split:

85% for training

15% for testing

Training Configuration:

Epochs: 8000

Batch Size: 64

Image Size: 418×418 pixels

System Requirements

Raspberry Pi (with a camera module and GPS integration)

Python 3.7 or later

TensorFlow Lite

YOLOv3 with Darknet

Cloud database access

Installation Guide

For macOS

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

For Windows

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

Running the System

Prepare the Raspberry Pi:

Install Raspbian OS and set up the camera and GPS modules.

Start the Program:

python3 main.py

View Outputs:

The system displays detected defects on the console along with their GPS locations.

Annotated images are uploaded to the cloud database.

Code Features

The detection and annotation process is built using OpenCV and YOLOv3. Here are some highlights:

Object Detection: Identifies road defects like potholes and cracks (longitudinal, transverse, alligator).

Real-Time Video Processing: Processes video streams frame-by-frame for defect detection.

Bounding Boxes: Draws bounding boxes around detected defects with confidence scores.

FPS Calculation: Displays real-time Frames Per Second (FPS) on the output.

Non-Maximum Suppression: Filters overlapping bounding boxes for accurate detection.

Custom Thresholds: Allows for confidence thresholds to classify defects.

How to Use the Code

Load your YOLO model weights and configuration files.

Define the list of classes for detection (e.g., potholes, cracks).

Provide a video or image as input to the program.

Run the script to see real-time detection and annotations.

Results and Observations

TensorFlow Lite was faster, making it ideal for IoT devices.

YOLOv3 delivered higher accuracy but required more computational power.

Real-time defect detection and localization were successfully achieved.

Contributing

I’d love for others to contribute! Feel free to fork the repository, make improvements, and submit pull requests. Contributions can include:

Improving model accuracy

Enhancing processing speed

Adding support for more defect types

If you have any questions or ideas, reach out to me directly. Let’s make our project more accurate and efficient.

