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

st.write(
    "Explore the source code, project repository, "
    "and professional profile."
)

link_col1, link_col2, link_col3 = st.columns(3)


# ============================================================
# GITHUB PROFILE
# ============================================================

with link_col1:

    st.markdown("### 💻 GitHub Profile")

    st.caption(
        "Explore the complete source code, projects, "
        "and development work."
    )

    st.link_button(
        "View GitHub Profile",
        "https://github.com/GouravGC",
    )


# ============================================================
# PROJECT REPOSITORY
# ============================================================

with link_col2:

    st.markdown("### 📦 Project Repository")

    st.caption(
        "View the source code and architecture of "
        "this vehicle damage detection project."
    )

    st.link_button(
        "View Repository",
        "https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision",
    )


# ============================================================
# LINKEDIN
# ============================================================

with link_col3:

    st.markdown("### 🔵 LinkedIn")

    st.caption(
        "Connect with me and explore my professional "
        "background and experience."
    )

    st.link_button(
        "View LinkedIn",
        "https://www.linkedin.com/in/gourav-chhatwani-9a301134a/",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Built as an end-to-end Computer Vision portfolio project."
)