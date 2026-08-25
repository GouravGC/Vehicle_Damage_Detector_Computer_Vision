import streamlit as st

from src.ui.theme import apply_theme


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About | Vehicle Damage Detection",
    page_icon="👨‍💻",
    layout="wide",
)

apply_theme()


# ============================================================
# PAGE HEADER
# ============================================================

st.title("👨‍💻 About the Project")

st.markdown(
    """
    This project demonstrates an end-to-end computer vision
    workflow for detecting visible vehicle damage from images.

    The application combines a trained **YOLO11n object detection
    model** with a modular inference architecture, image
    validation, detection visualization, and an interactive
    Streamlit interface.
    """
)


st.divider()


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.subheader("Technology Stack")

technologies = [
    ("🐍", "Python", "Application development"),
    ("🔥", "PyTorch", "Deep learning framework"),
    ("🎯", "YOLO11n", "Object detection model"),
    ("⚡", "Ultralytics", "YOLO inference framework"),
    ("🖼️", "Pillow", "Image handling"),
    ("👁️", "OpenCV", "Computer vision"),
    ("📊", "Streamlit", "Interactive web application"),
]

columns = st.columns(3)

for index, (icon, name, description) in enumerate(technologies):

    with columns[index % 3]:

        st.markdown(f"### {icon} {name}")

        st.caption(description)

        st.divider()


# ============================================================
# ENGINEERING FOCUS
# ============================================================

st.subheader("Engineering Focus")

engineering_focus = [
    "Modular project architecture",
    "Centralized configuration",
    "Structured exception handling",
    "Application logging",
    "Reusable model interface",
    "Image validation",
    "Structured inference results",
    "Detection visualization",
    "Automated testing",
    "Interactive Streamlit application",
]

for item in engineering_focus:
    st.markdown(f"- {item}")


# ============================================================
# PROJECT SCOPE
# ============================================================

st.subheader("Project Scope")

st.markdown(
    """
    The goal of this project is not only to demonstrate object
    detection, but also to show how a trained computer vision
    model can be organized into a maintainable application.

    The trained model artifact is loaded directly during
    inference, meaning the deployed application does not perform
    model training.
    """
)


# ============================================================
# PROJECT LINKS
# ============================================================

st.subheader("Project Links")

st.info(
    "GitHub, LinkedIn and portfolio links can be added here."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Built as an end-to-end Computer Vision portfolio project."
)