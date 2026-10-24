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

> **Try the application:** Upload vehicle images to the interactive Streamlit application and run YOLO11n inference to detect and localize visible vehicle damage.

---

## 📌 Overview

Vehicle Damage Detection is an end-to-end computer vision application designed to detect and localize visible vehicle damage from images.

The project uses a trained **YOLO11n object detection model** and integrates it into a modular inference pipeline with image validation, structured prediction handling, visualization, evaluation metrics, and an interactive Streamlit web application.

Beyond model training, the project explores **inference optimization and deployment performance** by comparing PyTorch inference with ONNX Runtime. The optimized inference workflow demonstrates lower measured latency and higher throughput while retaining a computer vision evaluation pipeline.

The goal is to demonstrate how a trained object detection model can be developed, evaluated, optimized, and integrated into a maintainable, reusable application.

---

## 🎯 Project Objectives

- Detect visible vehicle damage from images.
- Localize damage using bounding boxes.
- Classify six types of vehicle damage.
- Filter predictions using confidence thresholds.
- Convert raw model predictions into structured results.
- Visualize detection results.
- Evaluate model performance on held-out test data.
- Build a reusable inference pipeline.
- Compare inference latency and throughput across runtimes.
- Integrate optimized inference into a deployable application.
- Provide an interactive Streamlit interface.
- Organize the application using modular software architecture.

---

## 🧠 Model

The project uses **YOLO11n** for object detection.

YOLO is a one-stage object detection architecture that performs object localization and classification within a single inference pipeline.

### Model Configuration

| Property | Value |
|---|---|
| Architecture | YOLO11n |
| Task | Object Detection |
| Input Size | 640 × 640 |
| Confidence Threshold | 0.50 |
| IoU Threshold | 0.50 |
| Number of Classes | 6 |
| Training / Reference Framework | Ultralytics / PyTorch |
| Optimized Inference Runtime | ONNX Runtime |

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

The evaluation measures the model's ability to identify damage categories and localize them using bounding boxes. Precision and recall capture different aspects of detection performance, while mAP evaluates detection quality across confidence and, for mAP@50–95, multiple IoU thresholds.

The evaluation metrics are also exposed through the application's **Model Analytics** page.

---

## ⚡ Inference Optimization & Throughput

A key engineering component of this project is comparing model inference performance between **PyTorch and ONNX Runtime**.

ONNX Runtime provides an alternative execution path for deploying the trained model. The comparison examines two practical performance metrics: latency per image and inference throughput.

### PyTorch vs. ONNX Runtime

| Performance Metric | PyTorch | ONNX Runtime |
|---|---:|---:|
| Inference latency per image | 14.31 ms | 10.94 ms |
| Throughput | 69.87 FPS | 91.41 FPS |

### Measured Performance Improvements

- **23.56% lower inference latency**, reducing the measured time per image from 14.31 ms to 10.94 ms.
- **30.82% higher throughput**, increasing the measured processing rate from 69.87 FPS to 91.41 FPS.
- Integrated model inference into a reusable application workflow rather than limiting the project to offline model evaluation.

These results highlight the potential deployment-performance benefits of the ONNX Runtime inference path for this project.

*Benchmark note: These figures represent the previously recorded comparison. Hardware, warm-up procedure, batch size, and timing methodology should be documented alongside the results for a fully reproducible benchmark. Runtime comparisons should use equivalent input conditions and the same measurement methodology.*

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
                 Model Inference
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
         PyTorch Path          ONNX Runtime Path
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                  Raw Predictions
                         │
                         ▼
                 Confidence Filtering
                         │
                         ▼
                Structured Detections
                         │
                         ▼
                    Bounding Boxes
                         │
                         ▼
                    Visualization
                         │
                         ▼
                 Streamlit Output
```

---

## 🏗️ Application Design

The application is organized around a reusable inference workflow:

- **Input handling:** Accepts uploaded vehicle images.
- **Image validation:** Checks input images before inference.
- **Model inference:** Generates object-detection predictions.
- **Post-processing:** Applies confidence filtering and structures predictions.
- **Visualization:** Displays localized damage with bounding boxes.
- **Evaluation:** Presents model performance metrics.
- **User interface:** Provides an interactive Streamlit application.

This structure separates inference and result processing from the user interface, making the application easier to maintain and extend.

---

## 🛠️ Technology Stack

- **Computer Vision:** YOLO11n, object detection
- **Model Framework:** Ultralytics, PyTorch
- **Optimized Inference:** ONNX Runtime
- **Programming Language:** Python
- **Application:** Streamlit
- **Model Evaluation:** Precision, recall, mAP@50, mAP@50–95
- **Performance Analysis:** Inference latency, throughput (FPS)

---

## 💡 Key Engineering Takeaways

- Evaluating an object detector requires both model-quality metrics and deployment-performance measurements.
- Model inference can be integrated into a reusable application pipeline with input validation, post-processing, and visualization.
- Runtime optimization can improve inference efficiency without replacing the overall application architecture.
- Measuring latency and throughput helps assess the practical performance of a deployed computer vision model.

---

## 🚀 Live Application

Explore the deployed application:

**[Open Vehicle Damage Detection Demo](https://vehicledamagedetectorcomputervision.streamlit.app/)**

Source code:

**[View the GitHub Repository](https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision)**

---

## 👨‍💻 Author

**Gourav Chhatwani**

- [GitHub](https://github.com/GouravGC)
- [LinkedIn](https://www.linkedin.com/in/gourav-chhatwani-9a301134a/)
- [Portfolio](https://gcsportfolio.streamlit.app/)
