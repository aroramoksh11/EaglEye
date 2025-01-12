import cv2
import numpy as np
import time

# Load Object Detector
detector = cv2.dnn.readNet("weights/custom_model_weights.weights", "config_files/custom_model_config.cfg")

# Define Classes
categories = ['Road Damage Type 1', 'Road Damage Type 2', 'Road Damage Type 3', 'Road Damage Type 4']

# Load Video
video_source = cv2.VideoCapture("test_data/sample_video.mp4")

# Define Visualization Attributes
font_style = cv2.FONT_HERSHEY_PLAIN
color_palette = np.random.uniform(0, 255, size=(100, 3))

frame_counter = 0
start_time = time.time()

# Process Frames
while True:
    success, frame = video_source.read()
    if not success:
        print("End of video or error loading frame.")
        break
    
    height, width, channels = frame.shape
    frame_counter += 1

    # Preprocess Frame
    input_blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    detector.setInput(input_blob)
    output_names = detector.getUnconnectedOutLayersNames()
    detections = detector.forward(output_names)

    bounding_boxes = []
    detection_scores = []
    category_ids = []

    for output in detections:
        for item in output:
            probabilities = item[5:]
            category_id = np.argmax(probabilities)
            score = probabilities[category_id]
            if score > 0.1:  # Detection Threshold
                center_x = int(item[0] * width)
                center_y = int(item[1] * height)
                box_width = int(item[2] * width)
                box_height = int(item[3] * height)
                top_left_x = int(center_x - box_width / 2)
                top_left_y = int(center_y - box_height / 2)

                bounding_boxes.append([top_left_x, top_left_y, box_width, box_height])
                detection_scores.append(float(score))
                category_ids.append(category_id)

    indices = cv2.dnn.NMSBoxes(bounding_boxes, detection_scores, 0.4, 0.3)

    # Draw Detections
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = bounding_boxes[i]
            label = str(categories[category_ids[i]])
            confidence = str(round(detection_scores[i], 2))
            color = color_palette[i % len(color_palette)]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence}", (x, y - 10), font_style, 1, (255, 255, 255), 2)

    # Display FPS
    elapsed_time = time.time() - start_time
    fps = frame_counter / elapsed_time
    cv2.putText(frame, f"FPS: {round(fps, 2)}", (10, 50), font_style, 2, (0, 0, 0), 3)

    # Show Frame
    cv2.imshow('Detection Frame', frame)
    if cv2.waitKey(1) == 27:  # Exit on 'Esc'
        break

# Release Resources
video_source.release()
cv2.destroyAllWindows()
