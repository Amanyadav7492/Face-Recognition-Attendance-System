# Face-Recognition-Attendance-System
# 🔥 Fire Detection Model (YOLOv8 + OpenCV)

A **real-time Fire Detection System** built using **YOLOv8**, **OpenCV**, and **Python**, capable of detecting fire from video streams or webcams.  
This project can trigger **sound alarms** and send **email notifications** when fire is detected, making it useful for **smart surveillance and safety monitoring**.

---

## 🚀 Features

✅ Real-time fire detection using YOLOv8  
✅ Works with webcam or video files  
✅ Automatic **sound alert** when fire is detected  
✅ Sends **email alerts** with timestamp  
✅ Lightweight and easy to deploy  
✅ Configurable for custom datasets  

---

## 🧠 Model Overview

This project uses the **Ultralytics YOLOv8** model trained on a **custom fire dataset** (e.g., from Kaggle).  

**Model Configuration:**
- Model: `yolov8n.pt` (nano version for faster performance)
- Task: Fire detection
- Epochs: 15  
- Image size: 640×640  

Example training command:
```bash
yolo task=detect mode=train model=yolov8n.pt data="/path/to/data.yaml" epochs=15 imgsz=640
