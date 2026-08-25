import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background-color: #0b1117;
        color: #e5edf5 !important;
    }

    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4 {
        color: #f8fafc !important;
    }

    p,
    li {
        color: #d8e1e8 !important;
    }

    .stMarkdown p,
    .stMarkdown li {
        color: #d8e1e8 !important;
    }

    strong,
    b {
        color: #ffffff !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background-color: #0d151d;
        border-right: 1px solid #263541;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #e8f0f7 !important;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        background: linear-gradient(
            135deg,
            #162633,
            #101a23
        );

        border: 1px solid #2a3c4b;
        border-radius: 22px;

        padding: 45px;

        margin-bottom: 35px;

        box-shadow:
            0 15px 40px rgba(0, 0, 0, 0.25);
    }

    .hero-badge {
        color: #9ed7ff !important;

        font-size: 0.78rem;

        font-weight: 700;

        letter-spacing: 0.12em;

        margin-bottom: 15px;
    }

    .hero-description {
        color: #d0dce6 !important;

        font-size: 1.08rem;

        line-height: 1.7;

        max-width: 800px;
    }


    /* ========================================================
       CARDS
       ======================================================== */

    .card {
        background-color: #121d27;

        border: 1px solid #293b49;

        border-radius: 16px;

        padding: 25px;

        min-height: 170px;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.18);
    }

    .card-icon {
        font-size: 2rem;

        margin-bottom: 10px;
    }

    .card-title {
        color: #f1f5f9 !important;

        font-size: 1.15rem;

        font-weight: 700;

        margin-bottom: 8px;
    }

    .card-description {
        color: #c7d3dd !important;

        line-height: 1.6;

        font-size: 0.92rem;
    }


    /* ========================================================
       PIPELINE
       ======================================================== */

    .pipeline-number {
        color: #9ed7ff !important;

        font-size: 0.85rem;

        font-weight: 700;
    }

    .pipeline-title {
        color: #f1f5f9 !important;

        font-weight: 650;
    }

    .pipeline-description {
        color: #b4c2ce !important;

        font-size: 0.9rem;
    }


    /* ========================================================
       PROJECT HIGHLIGHTS
       ======================================================== */

    .highlight-card {
        background-color: #121d27;

        border: 1px solid #293b49;

        border-radius: 16px;

        padding: 25px;

        min-height: 230px;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.18);
    }

    .highlight-card h3 {
        color: #f8fafc !important;
    }

    .highlight-card p,
    .highlight-card li {
        color: #d8e1e8 !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;

        color: #8b9aa7 !important;

        padding-top: 35px;

        margin-top: 50px;

        border-top: 1px solid #263541;

        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🚗 Vehicle Damage AI")

    st.caption(
        "Computer Vision Portfolio Project"
    )

    st.divider()

    st.subheader("Navigation")

    st.page_link(
        "app.py",
        label="Home",
        icon="🏠",
    )

    st.page_link(
        "pages/2_🔍_Damage_Detection.py",
        label="Damage Detection",
        icon="🔍",
    )

    st.page_link(
        "pages/3_📊_Analytics.py",
        label="Analytics",
        icon="📊",
    )

    st.page_link(
        "pages/4_🧠_Model.py",
        label="Model",
        icon="🧠",
    )

    st.page_link(
        "pages/5_📁_Dataset.py",
        label="Dataset",
        icon="📁",
    )

    st.page_link(
        "pages/6_👨‍💻_About.py",
        label="About",
        icon="👨‍💻",
    )

    st.divider()

    st.caption("YOLO11n")
    st.caption("PyTorch")
    st.caption("OpenCV")
    st.caption("Streamlit")


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="hero">',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-badge">'
    'COMPUTER VISION • OBJECT DETECTION'
    '</div>',
    unsafe_allow_html=True,
)

st.title("Vehicle Damage Detection")

st.markdown(
    """
    <div class="hero-description">
    An end-to-end computer vision application powered by
    YOLO11n to detect and localize visible vehicle damage
    from images.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.header("Project Overview")

st.write(
    """
    A production-oriented computer vision application that
    combines a trained YOLO11n object detection model with
    a modular inference pipeline and an interactive web
    interface.
    """
)

st.write("")


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="card">

        <div class="card-icon">🔍</div>

        <div class="card-title">
        Detect
        </div>

        <div class="card-description">
        Upload a vehicle image and run inference using
        the trained YOLO11n object detection model.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="card">

        <div class="card-icon">🎯</div>

        <div class="card-title">
        Localize
        </div>

        <div class="card-description">
        Identify damage categories and localize them
        using object-detection bounding boxes.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="card">

        <div class="card-icon">📊</div>

        <div class="card-title">
        Analyze
        </div>

        <div class="card-description">
        Explore detection confidence, damage categories
        and model information.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# END-TO-END PIPELINE
# ============================================================

st.header("End-to-End Pipeline")

pipeline_steps = [
    (
        "01",
        "Image Upload",
        "Provide a vehicle image.",
    ),
    (
        "02",
        "Image Validation",
        "Validate the uploaded image.",
    ),
    (
        "03",
        "YOLO11n",
        "Run object detection.",
    ),
    (
        "04",
        "Post-processing",
        "Convert predictions into structured results.",
    ),
    (
        "05",
        "Visualization",
        "Display annotated detections.",
    ),
]


for number, title, description in pipeline_steps:

    col_number, col_content = st.columns([1, 8])

    with col_number:

        st.markdown(
            f"""
            <div class="pipeline-number">
                {number}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_content:

        st.markdown(
            f"""
            <div class="pipeline-title">
                {title}
            </div>

            <div class="pipeline-description">
                {description}
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================

st.header("Project Highlights")

left, right = st.columns(2)


# ============================================================
# PRODUCTION ARCHITECTURE
# ============================================================

with left:

    st.markdown(
        """
        <div class="highlight-card">

        <h3>⚙️ Production Architecture</h3>

        <p>✓ Centralized configuration</p>
        <p>✓ Application logging</p>
        <p>✓ Custom exception handling</p>
        <p>✓ Modular model interface</p>
        <p>✓ Reusable inference pipeline</p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# COMPUTER VISION WORKFLOW
# ============================================================

with right:

    st.markdown(
        """
        <div class="highlight-card">

        <h3>👁️ Computer Vision Workflow</h3>

        <p>✓ Image validation</p>
        <p>✓ YOLO11n inference</p>
        <p>✓ Bounding-box detection</p>
        <p>✓ Confidence filtering</p>
        <p>✓ Detection visualization</p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Vehicle Damage Detection · YOLO11n · Computer Vision
    </div>
    """,
    unsafe_allow_html=True,
)