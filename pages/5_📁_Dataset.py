import streamlit as st

from src.ui.theme import apply_theme

st.set_page_config(
    page_title="Dataset",
    page_icon="📁",
    layout="wide",
)

apply_theme()

st.title("📁 Dataset")

st.caption(
    "Training data and object-detection configuration."
)


st.markdown(
    """
    ### Dataset Overview

    The model was developed using a **Kaggle-sourced vehicle
    damage detection dataset** containing annotated vehicle
    images for object detection.

    The dataset provides labeled examples of visible vehicle
    damage that can be used to train an object detection model.
    """
)


st.info(
    "The exact dataset metadata can be added here once the "
    "original dataset information is verified."
)


st.subheader("Detection Categories")

st.markdown(
    """
    The trained model is configured to identify vehicle damage
    categories represented in the project's model configuration.
    """
)


st.subheader("Dataset Configuration")

st.write(
    "The project's dataset configuration is maintained in:"
)

st.code(
    "configs/Vehicle Damage Collab.yaml",
    language="text",
)


st.subheader("Data → Model Pipeline")

st.markdown(
    """
    ```text
    Annotated Vehicle Images
              ↓
        Dataset Configuration
              ↓
          Model Training
              ↓
           YOLO11n
              ↓
       Trained Model Artifact
              ↓
         Production Inference
    ```
    """
)