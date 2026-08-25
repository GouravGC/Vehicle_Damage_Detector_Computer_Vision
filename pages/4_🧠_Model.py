import streamlit as st

from src.ui.theme import apply_theme

from src.config import (
    MODEL_PATH,
    ONNX_MODEL_PATH,
    IMAGE_SIZE,
    CONFIDENCE_THRESHOLD,
    IOU_THRESHOLD,
)


st.set_page_config(
    page_title="Model",
    page_icon="🧠",
    layout="wide",
)

apply_theme()

st.title("🧠 Model Architecture")

st.caption(
    "YOLO11n-based vehicle damage object detection."
)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Architecture", "YOLO11n")

with col2:
    st.metric("Input Size", f"{IMAGE_SIZE} × {IMAGE_SIZE}")

with col3:
    st.metric(
        "Confidence Threshold",
        f"{CONFIDENCE_THRESHOLD:.2f}",
    )


st.markdown("---")

st.subheader("Model Overview")

st.write(
    """
    The application uses a trained YOLO11n object detection model
    to identify and localize visible vehicle damage.

    YOLO is a one-stage object detection architecture that performs
    object localization and classification in a single inference
    pipeline, making it suitable for real-time and interactive
    computer vision applications.
    """
)


st.subheader("Inference Configuration")

config_col1, config_col2 = st.columns(2)

with config_col1:

    st.markdown(
        f"""
        **Image Size**

        `{IMAGE_SIZE} × {IMAGE_SIZE}`

        **Confidence Threshold**

        `{CONFIDENCE_THRESHOLD}`
        """
    )

with config_col2:

    st.markdown(
        f"""
        **IoU Threshold**

        `{IOU_THRESHOLD}`

        **Framework**

        `Ultralytics`
        """
    )


st.subheader("Model Artifacts")

st.code(
    f"""
PyTorch model:
{MODEL_PATH}

ONNX model:
{ONNX_MODEL_PATH}
""",
    language="text",
)


st.subheader("Production Inference Flow")

st.markdown(
    """
    ```text
    Input Image
         ↓
    Image Validation
         ↓
    YOLO11n Model
         ↓
    Bounding Boxes
         ↓
    Confidence Filtering
         ↓
    Structured Detections
         ↓
    Visualization
    ```
    """
)