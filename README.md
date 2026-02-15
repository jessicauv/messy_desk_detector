# messy_desk_detector

This project uses NVIDIA YOLOv8 to detect objects on my desk and determine when clutter crosses a defined threshold. If the desk is “too messy,” the system saves an image and sends a notification as a reminder to clean up.

### Current Version (Prototype)
- MacBook camera captures live video.
- YOLOv8 detects objects in real time.
- If clutter objects ≥ defined threshold:
  - Screenshot is saved
  - Notification is triggered (console or push service).

### Planned Final Architecture
ESP32-S3 Sense camera → sends image via WiFi → server runs YOLOv8 → clutter threshold check → phone notification with image.
