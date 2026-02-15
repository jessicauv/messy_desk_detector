import cv2
from datetime import datetime
from ultralytics import YOLO
#import requests #for notifications

model = YOLO("yolov8n.pt")

# Open MacBook camera - need to change to ESP32S3 Sense camera instead!
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Test classes - need to refine and add more!
MESSY_CLASSES = ["book", "bottle", "cup", "cell phone", "remote", "keyboard", "laptop", "chair", "shoe"]
MESSY_THRESHOLD = 5

COCO_CLASSES = model.names

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # YOLOv8 detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Check if messiness is too much
    detected_classes = [COCO_CLASSES[int(box.cls)] for box in results[0].boxes]
    clutter_count = sum(1 for cls in detected_classes if cls in MESSY_CLASSES)

    if clutter_count >= MESSY_THRESHOLD:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"messy_desk_{timestamp}.jpg"
        cv2.imwrite(filename, annotated_frame)
        print(f"Messy Desk Detected! {clutter_count} clutter items. Screenshot saved: {filename}")
        
        # Send Push Notification to iPhone (and group chat?)

    # Display annotated frame
    cv2.imshow("Messy Desk Detector", annotated_frame)

    #'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
