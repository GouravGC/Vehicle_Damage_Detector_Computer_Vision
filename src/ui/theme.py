import streamlit as st


def apply_theme():
    """
    Apply one consistent dark theme across the entire application.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           GLOBAL APPLICATION
        ========================================================= */

        .stApp {
            background-color: #0b1117 !important;
            color: #d8e1e8 !important;
        }

        .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }


        /* =========================================================
           GLOBAL TEXT
        ========================================================= */

        p,
        li,
        span,
        label {
            color: #d8e1e8 !important;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            color: #f8fafc !important;
        }

        strong,
        b {
            color: #ffffff !important;
        }

        [data-testid="stMarkdownContainer"] {
            color: #d8e1e8 !important;
        }

        [data-testid="stMarkdownContainer"] p {
            color: #d8e1e8 !important;
        }

        [data-testid="stMarkdownContainer"] li {
            color: #d8e1e8 !important;
        }

        [data-testid="stMarkdownContainer"] strong,
        [data-testid="stMarkdownContainer"] b {
            color: #ffffff !important;
        }


        /* =========================================================
           SIDEBAR
        ========================================================= */

        [data-testid="stSidebar"] {
            background-color: #0d151d !important;
            border-right: 1px solid #263541 !important;
        }

        [data-testid="stSidebar"] * {
            color: #e5edf5 !important;
        }

        [data-testid="stSidebar"] p {
            color: #b8c6d3 !important;
        }


        /* =========================================================
           PAGE HEADERS
        ========================================================= */

        .page-title {
            color: #ffffff !important;
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 0.25rem;
        }

        .page-subtitle {
            color: #aebdca !important;
            font-size: 1rem;
            margin-bottom: 2rem;
        }


        /* =========================================================
           CARDS
        ========================================================= */

        .info-card {
            background: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.18);
        }

        .info-card-title {
            color: #f8fafc !important;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .info-card-text {
            color: #b8c6d3 !important;
            font-size: 0.95rem;
            line-height: 1.65;
        }


        /* =========================================================
           METRICS
        ========================================================= */

        [data-testid="stMetric"] {
            background: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 14px;
            padding: 16px;
        }

        [data-testid="stMetricLabel"] {
            color: #aebdca !important;
        }

        [data-testid="stMetricLabel"] * {
            color: #aebdca !important;
        }

        [data-testid="stMetricValue"] {
            color: #ffffff !important;
        }

        [data-testid="stMetricValue"] * {
            color: #ffffff !important;
        }


        /* =========================================================
           BUTTONS
        ========================================================= */

        .stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }

        .stButton > button * {
            color: inherit !important;
        }


        /* =========================================================
           FILE UPLOADER
        ========================================================= */

        [data-testid="stFileUploader"] {
            background-color: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 14px !important;
            padding: 10px !important;
        }

        [data-testid="stFileUploader"] section {
            background-color: #121c25 !important;
        }

        [data-testid="stFileUploader"] section > div {
            background-color: #121c25 !important;
        }

        [data-testid="stFileUploader"] * {
            color: #d8e1e8 !important;
        }

        [data-testid="stFileUploader"] span {
            color: #d8e1e8 !important;
        }

        [data-testid="stFileUploader"] small {
            color: #aebdca !important;
        }

        [data-testid="stFileUploader"] button {
            background-color: #1b2a36 !important;
            color: #f8fafc !important;
            border: 1px solid #344454 !important;
        }

        [data-testid="stFileUploader"] button * {
            color: #f8fafc !important;
        }

        [data-testid="stFileUploader"] button span {
            color: #f8fafc !important;
        }


        /* =========================================================
           INPUTS
        ========================================================= */

        input,
        textarea {
            color: #f8fafc !important;
            background-color: #121c25 !important;
        }

        input::placeholder,
        textarea::placeholder {
            color: #7f8d99 !important;
        }


        /* =========================================================
           SELECTBOX / DROPDOWN
        ========================================================= */

        [data-baseweb="select"] > div {
            background-color: #121c25 !important;
            color: #f8fafc !important;
            border-color: #344454 !important;
        }

        [data-baseweb="select"] * {
            color: #f8fafc !important;
        }


        /* =========================================================
           EXPANDERS
        ========================================================= */

        [data-testid="stExpander"] {
            background: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 12px !important;
        }

        [data-testid="stExpander"] * {
            color: #d8e1e8 !important;
        }

        [data-testid="stExpander"] summary {
            color: #f1f5f9 !important;
        }

        [data-testid="stExpander"] summary span {
            color: #f1f5f9 !important;
        }


        /* =========================================================
           ALERTS
        ========================================================= */

        [data-testid="stAlert"] {
            border-radius: 12px !important;
        }

        [data-testid="stAlert"] * {
            color: #d8e1e8 !important;
        }


        /* =========================================================
           INLINE CODE
        ========================================================= */

        [data-testid="stMarkdownContainer"] code {
            color: #c7e3ff !important;
            background-color: #121c25 !important;
            border: 1px solid #263541 !important;
        }

        code {
            color: #c7e3ff !important;
        }


        /* =========================================================
           CODE BLOCKS
        ========================================================= */

        [data-testid="stCodeBlock"] {
            background-color: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 12px !important;
        }

        [data-testid="stCodeBlock"] pre {
            background-color: #121c25 !important;
        }

        [data-testid="stCodeBlock"] code {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
        }

        pre {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
            border: 1px solid #263541 !important;
            border-radius: 12px !important;
        }

        pre code {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
        }


        /* =========================================================
           RAW JSON / RAW METRICS
        ========================================================= */

        [data-testid="stJson"] {
            background-color: #121c25 !important;
            border: 1px solid #263541 !important;
            border-radius: 12px !important;
            padding: 16px !important;
            color: #d8e1e8 !important;
        }

        [data-testid="stJson"] * {
            color: #d8e1e8 !important;
        }

        [data-testid="stJson"] pre {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
        }

        [data-testid="stJson"] code {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
        }

        [data-testid="stJson"] span {
            color: #d8e1e8 !important;
        }

        .stJson {
            background-color: #121c25 !important;
            color: #d8e1e8 !important;
        }

        .stJson * {
            color: #d8e1e8 !important;
        }


        /* =========================================================
           CAPTIONS
        ========================================================= */

        [data-testid="stCaptionContainer"] {
            color: #9eabb7 !important;
        }

        [data-testid="stCaptionContainer"] * {
            color: #9eabb7 !important;
        }


        /* =========================================================
           DIVIDERS
        ========================================================= */

        hr {
            border-color: #263541 !important;
        }


        /* =========================================================
           FOOTER
        ========================================================= */

        .app-footer {
            text-align: center;
            padding: 35px 0 10px 0;
            color: #7d8a96 !important;
            font-size: 0.85rem;
        }
        
                /* =========================================================
        HOME PAGE - PROJECT HIGHLIGHTS
        ========================================================= */

        /* Section headings */
        .project-highlights,
        .project-highlights h2,
        .project-highlights h3,
        .project-highlights h4 {
            color: #f8fafc !important;
        }

        /* Project highlight text */
        .project-highlights p,
        .project-highlights li {
            color: #e2e8f0 !important;
        }

        /* Bold highlight titles */
        .project-highlights strong,
        .project-highlights b {
            color: #ffffff !important;
        }


        /* =========================================================
        RAW METRICS - FORCE READABLE TEXT
        ========================================================= */

        [data-testid="stJson"] {
            background-color: #121c25 !important;
            color: #f1f5f9 !important;
            border: 1px solid #263541 !important;
        }

        [data-testid="stJson"] * {
            color: #f1f5f9 !important;
        }

        [data-testid="stJson"] span {
            color: #f1f5f9 !important;
        }

        [data-testid="stJson"] code {
            color: #f1f5f9 !important;
            background-color: transparent !important;
        }

        [data-testid="stJson"] pre {
            color: #f1f5f9 !important;
            background-color: #121c25 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )