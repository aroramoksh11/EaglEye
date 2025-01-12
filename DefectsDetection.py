import cv2
import numpy as np
import glob
import random
import darknet as dnet

# So we load up the Yolo model with the custom weights and cfg file
net = cv2.dnn.readNet("weights/yolov3_custom_final.weights", "cfg_files/yolov3_custom.cfg")

# These are the objects Yolo is looking for
classes = ['Pothole', 'Longitudinal Crack', 'Transverse Crack', 'Alligator Crack']

# Here we get the paths of the test images
images_path = glob.glob(r"test_data/*.jpg")

# Get layer names and figure out the output layers for YOLO
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Pick random colors for the boxes we'll draw around detected objects
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Shuffle images so we dont always do them in the same order
random.shuffle(images_path)

# Loop through each image in the test dataset
for img_path in images_path:
    # Read the image and resize it (although here it ain't really being resized)
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=1, fy=1)
    height, width, channels = img.shape

    # Now we turn the image into a blob that YOLO can work with
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Set the blob as input and run the forward pass
    net.setInput(blob)
    outs = net.forward(output_layers)

    # We will store our results here: class IDs, confidence scores, and box coordinates
    class_ids = []
    confidences = []
    boxes = []

    # Go through all the detections YOLO makes
    for out in outs:
        for detection in out:
            # Get the scores for each class (the part after the first 5 values)
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            # We only care about detections that are above 30% confidence
            if confidence > 0.3:
                # Calculate the box's center (x, y) and its width & height
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Convert to top-left corner (x, y) for drawing the rectangle
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Add the box, confidence and class_id to the list
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maximum suppression (NMS) to get rid of overlapping boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Print out which boxes passed NMS (Just for debugging)
    print(indexes)

    # Font for the text labels we'll put on the boxes
    font = cv2.FONT_HERSHEY_PLAIN

    # Loop through all the boxes and draw them if they're in the final list
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])  # Get the label from the class ID
            color = colors[class_ids[i]]  # Get a random color for the box

            # Draw the rectangle for the bounding box
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # Put the label just above the box
            cv2.putText(img, label, (x, y - 10), font, 1.5, color, 2)

    # Show the image with the detected boxes
    cv2.imshow("Detected Image", img)

    # Wait for a key press before moving to the next image
    key = cv2.waitKey(0)

# Close all windows after we're done
cv2.destroyAllWindows()
