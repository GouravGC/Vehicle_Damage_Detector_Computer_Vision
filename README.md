# 🚗 Vehicle Damage Detection — Computer Vision

### End-to-End Vehicle Damage Detection using YOLO11n

<p align="center">

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge)](https://vehicledamagedetectorcomputervision.streamlit.app/)

[![GitHub](https://img.shields.io/badge/💻%20GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gourav%20Chhatwani-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/gourav-chhatwani-9a301134a/)

</p>

---

## 🔗 Project Links

| Resource | Link |
|---|---|
| 🚀 **Live Demo** | [Vehicle Damage Detection — Streamlit](https://vehicledamagedetectorcomputervision.streamlit.app/) |
| 💻 **GitHub Repository** | [Vehicle Damage Detector — GitHub](https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision) |
| 👤 **LinkedIn** | [Gourav Chhatwani — LinkedIn](https://www.linkedin.com/in/gourav-chhatwani-9a301134a/) |

> **Try the application:** The live Streamlit demo provides an interactive interface for uploading vehicle images and running YOLO11n inference.

---

## 📌 Overview

Vehicle Damage Detection is an end-to-end computer vision application designed to detect and localize visible vehicle damage from images.

The project uses a trained **YOLO11n object detection model** and integrates the model into a modular inference pipeline with image validation, structured prediction handling, visualization, evaluation metrics, and an interactive Streamlit web application.

The goal of this project is not only to train an object detection model, but also to demonstrate how a trained computer vision model can be organized into a maintainable, reusable, and deployable application.

---

## 🎯 Project Objectives

The project focuses on:

- Detecting visible vehicle damage from images
- Localizing damage using bounding boxes
- Classifying different types of vehicle damage
- Filtering predictions using confidence thresholds
- Converting raw model predictions into structured results
- Visualizing detection results
- Evaluating model performance on test data
- Building a reusable inference pipeline
- Providing an interactive Streamlit interface
- Organizing the application using modular software architecture

---

## 🧠 Model

The project uses **YOLO11n** for object detection.

YOLO (You Only Look Once) is a one-stage object detection architecture capable of performing object localization and classification within a single inference pipeline.

### Model Configuration

| Property | Value |
|---|---|
| Architecture | YOLO11n |
| Task | Object Detection |
| Input Size | 640 × 640 |
| Confidence Threshold | 0.50 |
| IoU Threshold | 0.50 |
| Number of Classes | 6 |
| Framework | Ultralytics / PyTorch |

---

## 🚘 Damage Classes

The trained model detects six vehicle damage categories:

| ID | Damage Class |
|---:|---|
| 0 | Dent |
| 1 | Scratch |
| 2 | Crack |
| 3 | Glass Shatter |
| 4 | Lamp Broken |
| 5 | Tire Flat |

---

## 📊 Model Evaluation

The model was evaluated on a held-out test set.

| Metric | Score |
|---|---:|
| Precision | 0.7136 |
| Recall | 0.6769 |
| mAP@50 | 0.7135 |
| mAP@50–95 | 0.5653 |

### Interpretation

The evaluation demonstrates that the model is capable of detecting multiple types of visible vehicle damage while maintaining a reasonable balance between precision and recall.

The evaluation metrics are also exposed through the application's **Model Analytics** page.

---

## 🔄 End-to-End Pipeline

```text
                    Vehicle Image
                         │
                         ▼
                   Image Upload
                         │
                         ▼
                  Image Validation
                         │
                         ▼
                     YOLO11n
                  Object Detection
                         │
                         ▼
                   Bounding Boxes
                         │
                         ▼
                Confidence Filtering
                         │
                         ▼
                Structured Detections
                         │
                         ▼
                   Visualization
                         │
                         ▼
                  Streamlit Output