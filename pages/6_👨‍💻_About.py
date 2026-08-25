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

# ============================================================
# PROJECT LINKS
# ============================================================

st.subheader("Project Links")

st.markdown(
    """
    <style>

    /* ========================================================
       PROJECT LINKS
       ======================================================== */

    .project-links-card {
        background: #121c25;
        border: 1px solid #263541;
        border-radius: 16px;
        padding: 24px;
        margin-top: 10px;
    }

    .project-link-title {
        color: #f8fafc !important;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .project-link-description {
        color: #b8c6d3 !important;
        font-size: 0.9rem;
        line-height: 1.6;
        margin-bottom: 16px;
    }

    /* Streamlit link buttons */

    .project-links-card a {
        background-color: #1a2834 !important;
        color: #e8f0f7 !important;

        border: 1px solid #344655 !important;
        border-radius: 10px !important;

        text-decoration: none !important;

        font-weight: 600 !important;
    }

    .project-links-card a:hover {
        background-color: #223544 !important;
        color: #ffffff !important;

        border-color: #4a6173 !important;
    }

    .project-links-card a p,
    .project-links-card a span,
    .project-links-card a div {
        color: #e8f0f7 !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


link_col1, link_col2, link_col3 = st.columns(3)


with link_col1:

    st.markdown(
        """
        <div class="project-links-card">

            <div class="project-link-title">
                💻 GitHub Profile
            </div>

            <div class="project-link-description">
                Explore the complete source code, projects,
                and development work.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "View GitHub Profile",
        "https://github.com/GouravGC",
    )


with link_col2:

    st.markdown(
        """
        <div class="project-links-card">

            <div class="project-link-title">
                📦 Project Repository
            </div>

            <div class="project-link-description">
                View the source code and architecture of
                this vehicle damage detection project.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "View Repository",
        "https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision",
    )


with link_col3:

    st.markdown(
        """
        <div class="project-links-card">

            <div class="project-link-title">
                🔵 LinkedIn
            </div>

            <div class="project-link-description">
                Connect with me and explore my professional
                background and experience.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "View LinkedIn",
        "https://www.linkedin.com/in/gourav-chhatwani-9a301134a/",
    )