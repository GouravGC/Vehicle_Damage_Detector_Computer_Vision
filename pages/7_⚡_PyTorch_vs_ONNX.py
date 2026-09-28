# pages/7_⚡_PyTorch_vs_ONNX.py

import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
import psutil
import streamlit as st
from PIL import Image
from ultralytics import YOLO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PyTorch vs ONNX Benchmark",
    page_icon="⚡",
    layout="wide",
)


# ============================================================
# DARK THEME — PAGE 7
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL PAGE
       ====================================================== */

    .stApp {
        background-color: #0e1117;
        color: #f5f5f5;
    }

    .main {
        background-color: #0e1117;
    }


    /* ======================================================
       MAIN CONTENT
       ====================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* ======================================================
       HEADINGS
       ====================================================== */

    h1 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    h2 {
        color: #ffffff !important;
        font-weight: 650 !important;
    }

    h3 {
        color: #f0f0f0 !important;
        font-weight: 600 !important;
    }


    /* ======================================================
       NORMAL TEXT
       ====================================================== */

    p,
    label,
    .stMarkdown,
    .stText,
    span {
        color: #e6e6e6;
    }


    /* ======================================================
       INPUT / SELECTBOX / RADIO / SLIDER
       ====================================================== */

    div[data-baseweb="select"] > div {
        background-color: #161b22 !important;
        border-color: #30363d !important;
        color: #ffffff !important;
    }

    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    div[data-baseweb="popover"] {
        background-color: #161b22 !important;
    }

    div[role="radiogroup"] label {
        color: #e6e6e6 !important;
    }

    div[data-testid="stSlider"] {
        color: #ffffff !important;
    }


    /* ======================================================
       FILE UPLOADER
       ====================================================== */

    section[data-testid="stFileUploader"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 10px;
    }

    section[data-testid="stFileUploader"] * {
        color: #e6e6e6 !important;
    }


    /* ======================================================
       BUTTONS
       ====================================================== */

    .stButton > button {
        background-color: #21262d;
        color: #ffffff;
        border: 1px solid #30363d;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.55rem 1.2rem;
    }

    .stButton > button:hover {
        background-color: #30363d;
        border-color: #8b949e;
        color: #ffffff;
    }

    .stButton > button:focus {
        color: #ffffff;
        border-color: #58a6ff;
        box-shadow: 0 0 0 1px #58a6ff;
    }


    /* ======================================================
       PRIMARY BUTTON
       ====================================================== */

    .stButton > button[kind="primary"] {
        background-color: #238636;
        color: #ffffff;
        border: 1px solid #2ea043;
        font-weight: 700;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #2ea043;
        color: #ffffff;
    }


    /* ======================================================
       INFO / SUCCESS / WARNING / ERROR BOXES
       ====================================================== */

    div[data-testid="stAlert"] {
        background-color: #161b22;
        border-radius: 8px;
        border: 1px solid #30363d;
    }


    /* ======================================================
       METRIC CARDS
       ====================================================== */

    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
    }

    div[data-testid="stMetricLabel"] {
        color: #8b949e !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    div[data-testid="stMetricDelta"] {
        color: #58a6ff !important;
    }


    /* ======================================================
       DATAFRAME / TABLE
       ====================================================== */

    div[data-testid="stDataFrame"] {
        border: 1px solid #30363d;
        border-radius: 8px;
        overflow: hidden;
    }


    /* ======================================================
       CODE / MONOSPACE
       ====================================================== */

    code {
        background-color: #161b22 !important;
        color: #79c0ff !important;
    }


    /* ======================================================
       DIVIDERS
       ====================================================== */

    hr {
        border-color: #30363d !important;
    }


    /* ======================================================
       CAPTIONS
       ====================================================== */

    .stCaption {
        color: #8b949e !important;
    }


    /* ======================================================
       SPINNER
       ====================================================== */

    div[data-testid="stSpinner"] {
        color: #58a6ff !important;
    }


    /* ======================================================
       IMAGE CONTAINERS
       ====================================================== */

    img {
        border-radius: 8px;
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid #30363d;
    }

    section[data-testid="stSidebar"] * {
        color: #e6e6e6;
    }


    /* ======================================================
       SCROLLBAR
       ====================================================== */

    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #0e1117;
    }

    ::-webkit-scrollbar-thumb {
        background: #30363d;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #484f58;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.title("⚡ PyTorch Native vs ONNX Runtime")

st.markdown(
    """
    Compare the same YOLO11n vehicle-damage detector using
    **PyTorch Native** and **ONNX Runtime** inference.

    The benchmark measures inference performance, CPU/RAM usage,
    GPU usage where available, model size, and resource efficiency.
    """
)

st.info(
    "Benchmark results are measured on the current machine. "
    "No performance or cost figures are hard-coded."
)


# ============================================================
# PATH CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PYTORCH_MODEL_PATH = PROJECT_ROOT / "model" / "vehicle_damage_yolo11n_best.pt"
ONNX_MODEL_PATH = PROJECT_ROOT / "model" / "vehicle_damage_yolo11n_best.onnx"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_file_size_mb(path: Path):
    """Return model file size in MB."""

    if path.exists():
        return path.stat().st_size / (1024 * 1024)

    return None


def get_cpu_percent():
    """Return current CPU utilization."""

    return psutil.cpu_percent(interval=0.1)


def get_memory_mb():
    """Return current system RAM usage in MB."""

    memory = psutil.virtual_memory()

    return memory.used / (1024 * 1024)


def get_process_memory_mb():
    """Return current Python process memory usage in MB."""

    process = psutil.Process(os.getpid())

    return process.memory_info().rss / (1024 * 1024)


def get_gpu_metrics():
    """
    Attempt to collect NVIDIA GPU information.

    Returns:
        Dictionary containing GPU availability and
        allocated GPU memory.
    """

    try:

        import torch

        if not torch.cuda.is_available():

            return {
                "gpu_available": False,
                "gpu_utilization": None,
                "gpu_memory_mb": None,
            }

        device_index = torch.cuda.current_device()

        torch.cuda.synchronize()

        allocated_mb = (
            torch.cuda.memory_allocated(device_index)
            / (1024 * 1024)
        )

        return {
            "gpu_available": True,
            "gpu_utilization": None,
            "gpu_memory_mb": allocated_mb,
        }

    except Exception:

        return {
            "gpu_available": False,
            "gpu_utilization": None,
            "gpu_memory_mb": None,
        }


def calculate_fps(latency_seconds):
    """Calculate FPS from inference latency."""

    if latency_seconds <= 0:
        return 0.0

    return 1.0 / latency_seconds


def calculate_percentage_reduction(before, after):
    """Calculate percentage reduction from before to after."""

    if before is None or after is None or before == 0:
        return None

    return ((before - after) / before) * 100


def calculate_percentage_change(before, after):
    """Calculate percentage change from before to after."""

    if before is None or after is None or before == 0:
        return None

    return ((after - before) / before) * 100


# ============================================================
# MODEL LOADING
# ============================================================

@st.cache_resource
def load_pytorch_model():
    """Load the existing PyTorch YOLO model."""

    if not PYTORCH_MODEL_PATH.exists():

        raise FileNotFoundError(
            f"PyTorch model not found:\n"
            f"{PYTORCH_MODEL_PATH}"
        )

    return YOLO(str(PYTORCH_MODEL_PATH))


@st.cache_resource
def load_onnx_model():
    """Load the ONNX YOLO model through Ultralytics."""

    if not ONNX_MODEL_PATH.exists():

        raise FileNotFoundError(
            f"ONNX model not found:\n"
            f"{ONNX_MODEL_PATH}"
        )

    return YOLO(str(ONNX_MODEL_PATH))


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def run_prediction(model, image, confidence=0.50):
    """
    Run one YOLO inference and return the first result.
    """

    results = model.predict(
        source=image,
        conf=confidence,
        imgsz=640,
        verbose=False,
    )

    return results[0]


# ============================================================
# BENCHMARK FUNCTION
# ============================================================

def benchmark_model(
    model,
    image,
    benchmark_runs=10,
    warmup_runs=3,
):
    """
    Benchmark a YOLO model.

    Warm-up runs are performed before collecting timing results.
    Multiple benchmark runs are used for more stable statistics.
    """

    # --------------------------------------------------------
    # Warm-up
    # --------------------------------------------------------

    for _ in range(warmup_runs):

        run_prediction(
            model,
            image,
        )


    # --------------------------------------------------------
    # Resource state before benchmark
    # --------------------------------------------------------

    cpu_before = get_cpu_percent()

    ram_before = get_memory_mb()

    process_ram_before = get_process_memory_mb()

    gpu_before = get_gpu_metrics()


    # --------------------------------------------------------
    # Benchmark
    # --------------------------------------------------------

    latencies = []

    first_result = None

    for _ in range(benchmark_runs):

        start_time = time.perf_counter()

        result = run_prediction(
            model,
            image,
        )

        end_time = time.perf_counter()

        latency = end_time - start_time

        latencies.append(latency)

        if first_result is None:

            first_result = result


    # --------------------------------------------------------
    # Resource state after benchmark
    # --------------------------------------------------------

    cpu_after = get_cpu_percent()

    ram_after = get_memory_mb()

    process_ram_after = get_process_memory_mb()

    gpu_after = get_gpu_metrics()


    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    latency_array = np.array(
        latencies
    )

    mean_latency = float(
        np.mean(latency_array)
    )

    median_latency = float(
        np.median(latency_array)
    )

    p95_latency = float(
        np.percentile(
            latency_array,
            95,
        )
    )

    min_latency = float(
        np.min(latency_array)
    )

    max_latency = float(
        np.max(latency_array)
    )

    fps = calculate_fps(
        mean_latency
    )


    # --------------------------------------------------------
    # Detection information
    # --------------------------------------------------------

    detection_count = 0

    classes = []

    confidences = []

    boxes = []


    if (
        first_result is not None
        and first_result.boxes is not None
    ):

        detection_count = len(
            first_result.boxes
        )

        if detection_count > 0:

            classes = (
                first_result
                .boxes
                .cls
                .cpu()
                .numpy()
                .astype(int)
                .tolist()
            )

            confidences = (
                first_result
                .boxes
                .conf
                .cpu()
                .numpy()
                .tolist()
            )

            boxes = (
                first_result
                .boxes
                .xyxy
                .cpu()
                .numpy()
                .tolist()
            )


    # --------------------------------------------------------
    # Return benchmark results
    # --------------------------------------------------------

    return {

        "result": first_result,

        "mean_latency_ms": (
            mean_latency * 1000
        ),

        "median_latency_ms": (
            median_latency * 1000
        ),

        "p95_latency_ms": (
            p95_latency * 1000
        ),

        "min_latency_ms": (
            min_latency * 1000
        ),

        "max_latency_ms": (
            max_latency * 1000
        ),

        "fps": fps,

        "cpu_before": cpu_before,

        "cpu_after": cpu_after,

        "ram_before_mb": ram_before,

        "ram_after_mb": ram_after,

        "process_ram_before_mb": (
            process_ram_before
        ),

        "process_ram_after_mb": (
            process_ram_after
        ),

        "gpu_before": gpu_before,

        "gpu_after": gpu_after,

        "detection_count": detection_count,

        "classes": classes,

        "confidences": confidences,

        "boxes": boxes,

        "latencies": latencies,
    }


# ============================================================
# IMAGE RENDERING
# ============================================================

def render_detection(result):
    """
    Render YOLO detection result as a PIL image.
    """

    if result is None:

        return None

    plotted = result.plot()

    # Ultralytics returns BGR numpy image.
    plotted = plotted[:, :, ::-1]

    return Image.fromarray(
        plotted
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.header("📦 Model Information")

model_info_col1, model_info_col2 = st.columns(2)


# ------------------------------------------------------------
# PyTorch information
# ------------------------------------------------------------

with model_info_col1:

    st.subheader(
        "🔥 PyTorch Native"
    )

    pytorch_size = get_file_size_mb(
        PYTORCH_MODEL_PATH
    )

    st.write(
        f"**Model:** "
        f"`{PYTORCH_MODEL_PATH.name}`"
    )

    st.write(
        "**Format:** PyTorch / `.pt`"
    )

    if pytorch_size is not None:

        st.write(
            f"**Model Size:** "
            f"{pytorch_size:.2f} MB"
        )

    else:

        st.write(
            "**Model Size:** Not found"
        )


# ------------------------------------------------------------
# ONNX information
# ------------------------------------------------------------

with model_info_col2:

    st.subheader(
        "⚡ ONNX Runtime"
    )

    onnx_size = get_file_size_mb(
        ONNX_MODEL_PATH
    )

    st.write(
        f"**Model:** "
        f"`{ONNX_MODEL_PATH.name}`"
    )

    st.write(
        "**Format:** ONNX / `.onnx`"
    )

    if onnx_size is not None:

        st.write(
            f"**Model Size:** "
            f"{onnx_size:.2f} MB"
        )

    else:

        st.write(
            "**Model Size:** Not found"
        )


# ============================================================
# INPUT
# ============================================================

st.header("📤 Benchmark Input")

uploaded_file = st.file_uploader(
    "Upload a vehicle damage image",
    type=[
        "jpg",
        "jpeg",
        "png",
    ],
)


benchmark_mode = st.radio(
    "Inference Mode",
    [
        "PyTorch Native",
        "ONNX Runtime",
        "Compare Both",
    ],
    horizontal=True,
)


benchmark_runs = st.slider(
    "Benchmark iterations",
    min_value=3,
    max_value=30,
    value=10,
    step=1,
)


warmup_runs = st.slider(
    "Warm-up iterations",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
)


# ============================================================
# RUN BENCHMARK
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")


    # --------------------------------------------------------
    # Input image
    # --------------------------------------------------------

    st.subheader(
        "Input Image"
    )

    st.image(
        image,
        caption="Uploaded vehicle image",
        use_column_width=True,
    )


    # --------------------------------------------------------
    # Benchmark button
    # --------------------------------------------------------

    if st.button(
        "🚀 Run Benchmark",
        type="primary",
    ):

        pytorch_metrics = None

        onnx_metrics = None


        # ====================================================
        # PYTORCH
        # ====================================================

        if benchmark_mode in [
            "PyTorch Native",
            "Compare Both",
        ]:

            with st.spinner(
                "Running PyTorch Native benchmark..."
            ):

                try:

                    pytorch_model = (
                        load_pytorch_model()
                    )

                    pytorch_metrics = (
                        benchmark_model(
                            pytorch_model,
                            image,
                            benchmark_runs=(
                                benchmark_runs
                            ),
                            warmup_runs=(
                                warmup_runs
                            ),
                        )
                    )

                except Exception as e:

                    st.error(
                        f"PyTorch benchmark failed: "
                        f"{e}"
                    )


        # ====================================================
        # ONNX
        # ====================================================

        if benchmark_mode in [
            "ONNX Runtime",
            "Compare Both",
        ]:

            with st.spinner(
                "Running ONNX Runtime benchmark..."
            ):

                try:

                    onnx_model = (
                        load_onnx_model()
                    )

                    onnx_metrics = (
                        benchmark_model(
                            onnx_model,
                            image,
                            benchmark_runs=(
                                benchmark_runs
                            ),
                            warmup_runs=(
                                warmup_runs
                            ),
                        )
                    )

                except Exception as e:

                    st.error(
                        f"ONNX benchmark failed: "
                        f"{e}"
                    )


        # ====================================================
        # RESULTS
        # ====================================================

        st.divider()

        st.header(
            "⏱️ Inference Performance"
        )

        performance_rows = []


        if pytorch_metrics:

            performance_rows.append(
                {
                    "Metric": (
                        "PyTorch Native"
                    ),

                    "Mean Latency (ms)": round(
                        pytorch_metrics[
                            "mean_latency_ms"
                        ],
                        3,
                    ),

                    "P50 Latency (ms)": round(
                        pytorch_metrics[
                            "median_latency_ms"
                        ],
                        3,
                    ),

                    "P95 Latency (ms)": round(
                        pytorch_metrics[
                            "p95_latency_ms"
                        ],
                        3,
                    ),

                    "FPS": round(
                        pytorch_metrics[
                            "fps"
                        ],
                        2,
                    ),
                }
            )


        if onnx_metrics:

            performance_rows.append(
                {
                    "Metric": (
                        "ONNX Runtime"
                    ),

                    "Mean Latency (ms)": round(
                        onnx_metrics[
                            "mean_latency_ms"
                        ],
                        3,
                    ),

                    "P50 Latency (ms)": round(
                        onnx_metrics[
                            "median_latency_ms"
                        ],
                        3,
                    ),

                    "P95 Latency (ms)": round(
                        onnx_metrics[
                            "p95_latency_ms"
                        ],
                        3,
                    ),

                    "FPS": round(
                        onnx_metrics[
                            "fps"
                        ],
                        2,
                    ),
                }
            )


        if performance_rows:

            st.dataframe(
                pd.DataFrame(
                    performance_rows
                ),
                use_container_width=True,
                hide_index=True,
            )


        # ====================================================
        # RESOURCE UTILIZATION
        # ====================================================

        st.header(
            "🖥️ Resource Utilization"
        )

        resource_rows = []


        if pytorch_metrics:

            resource_rows.append(
                {
                    "Backend": (
                        "PyTorch Native"
                    ),

                    "CPU Before (%)": round(
                        pytorch_metrics[
                            "cpu_before"
                        ],
                        2,
                    ),

                    "CPU After (%)": round(
                        pytorch_metrics[
                            "cpu_after"
                        ],
                        2,
                    ),

                    "RAM Before (MB)": round(
                        pytorch_metrics[
                            "ram_before_mb"
                        ],
                        2,
                    ),

                    "RAM After (MB)": round(
                        pytorch_metrics[
                            "ram_after_mb"
                        ],
                        2,
                    ),

                    "Process RAM Before (MB)": round(
                        pytorch_metrics[
                            "process_ram_before_mb"
                        ],
                        2,
                    ),

                    "Process RAM After (MB)": round(
                        pytorch_metrics[
                            "process_ram_after_mb"
                        ],
                        2,
                    ),
                }
            )


        if onnx_metrics:

            resource_rows.append(
                {
                    "Backend": (
                        "ONNX Runtime"
                    ),

                    "CPU Before (%)": round(
                        onnx_metrics[
                            "cpu_before"
                        ],
                        2,
                    ),

                    "CPU After (%)": round(
                        onnx_metrics[
                            "cpu_after"
                        ],
                        2,
                    ),

                    "RAM Before (MB)": round(
                        onnx_metrics[
                            "ram_before_mb"
                        ],
                        2,
                    ),

                    "RAM After (MB)": round(
                        onnx_metrics[
                            "ram_after_mb"
                        ],
                        2,
                    ),

                    "Process RAM Before (MB)": round(
                        onnx_metrics[
                            "process_ram_before_mb"
                        ],
                        2,
                    ),

                    "Process RAM After (MB)": round(
                        onnx_metrics[
                            "process_ram_after_mb"
                        ],
                        2,
                    ),
                }
            )


        if resource_rows:

            st.dataframe(
                pd.DataFrame(
                    resource_rows
                ),
                use_container_width=True,
                hide_index=True,
            )


        # ====================================================
        # GPU INFORMATION
        # ====================================================

        st.header(
            "🎮 GPU Resource Utilization"
        )

        gpu_rows = []


        if pytorch_metrics:

            gpu_rows.append(
                {
                    "Backend": (
                        "PyTorch Native"
                    ),

                    "GPU Available": (
                        pytorch_metrics[
                            "gpu_after"
                        ]["gpu_available"]
                    ),

                    "GPU Memory (MB)": (

                        round(
                            pytorch_metrics[
                                "gpu_after"
                            ]["gpu_memory_mb"],
                            2,
                        )

                        if pytorch_metrics[
                            "gpu_after"
                        ]["gpu_memory_mb"]
                        is not None

                        else "N/A"
                    ),
                }
            )


        if onnx_metrics:

            gpu_rows.append(
                {
                    "Backend": (
                        "ONNX Runtime"
                    ),

                    "GPU Available": (
                        onnx_metrics[
                            "gpu_after"
                        ]["gpu_available"]
                    ),

                    "GPU Memory (MB)": (

                        round(
                            onnx_metrics[
                                "gpu_after"
                            ]["gpu_memory_mb"],
                            2,
                        )

                        if onnx_metrics[
                            "gpu_after"
                        ]["gpu_memory_mb"]
                        is not None

                        else "N/A"
                    ),
                }
            )


        if gpu_rows:

            st.dataframe(
                pd.DataFrame(
                    gpu_rows
                ),
                use_container_width=True,
                hide_index=True,
            )


        # ====================================================
        # DETECTION RESULTS
        # ====================================================

        st.header(
            "🎯 Detection Results"
        )

        detection_col1, detection_col2 = (
            st.columns(2)
        )


        # ----------------------------------------------------
        # PyTorch result
        # ----------------------------------------------------

        if pytorch_metrics:

            with detection_col1:

                st.subheader(
                    "🔥 PyTorch Native"
                )

                pytorch_result_image = (
                    render_detection(
                        pytorch_metrics[
                            "result"
                        ]
                    )
                )

                if pytorch_result_image:

                    st.image(
                        pytorch_result_image,
                        use_column_width=True,
                    )

                st.metric(
                    "Detections",
                    pytorch_metrics[
                        "detection_count"
                    ],
                )


        # ----------------------------------------------------
        # ONNX result
        # ----------------------------------------------------

        if onnx_metrics:

            with detection_col2:

                st.subheader(
                    "⚡ ONNX Runtime"
                )

                onnx_result_image = (
                    render_detection(
                        onnx_metrics[
                            "result"
                        ]
                    )
                )

                if onnx_result_image:

                    st.image(
                        onnx_result_image,
                        use_column_width=True,
                    )

                st.metric(
                    "Detections",
                    onnx_metrics[
                        "detection_count"
                    ],
                )


        # ====================================================
        # COMPARISON
        # ====================================================

        if (
            pytorch_metrics
            and onnx_metrics
        ):

            st.divider()

            st.header(
                "📊 PyTorch vs ONNX Comparison"
            )


            # ------------------------------------------------
            # Calculations
            # ------------------------------------------------

            latency_reduction = (
                calculate_percentage_reduction(
                    pytorch_metrics[
                        "mean_latency_ms"
                    ],
                    onnx_metrics[
                        "mean_latency_ms"
                    ],
                )
            )


            ram_reduction = (
                calculate_percentage_reduction(
                    pytorch_metrics[
                        "process_ram_after_mb"
                    ],
                    onnx_metrics[
                        "process_ram_after_mb"
                    ],
                )
            )


            gpu_memory_reduction = (
                calculate_percentage_reduction(
                    pytorch_metrics[
                        "gpu_after"
                    ]["gpu_memory_mb"],
                    onnx_metrics[
                        "gpu_after"
                    ]["gpu_memory_mb"],
                )
            )


            fps_change = (
                calculate_percentage_change(
                    pytorch_metrics[
                        "fps"
                    ],
                    onnx_metrics[
                        "fps"
                    ],
                )
            )


            # ------------------------------------------------
            # Comparison table
            # ------------------------------------------------

            comparison_rows = [

                {
                    "Metric": (
                        "Mean Latency"
                    ),

                    "PyTorch": round(
                        pytorch_metrics[
                            "mean_latency_ms"
                        ],
                        3,
                    ),

                    "ONNX": round(
                        onnx_metrics[
                            "mean_latency_ms"
                        ],
                        3,
                    ),

                    "Change / Reduction": (

                        f"{latency_reduction:.2f}%"

                        if latency_reduction
                        is not None

                        else "N/A"
                    ),
                },


                {
                    "Metric": "FPS",

                    "PyTorch": round(
                        pytorch_metrics[
                            "fps"
                        ],
                        2,
                    ),

                    "ONNX": round(
                        onnx_metrics[
                            "fps"
                        ],
                        2,
                    ),

                    "Change": (

                        f"{fps_change:.2f}%"

                        if fps_change
                        is not None

                        else "N/A"
                    ),
                },


                {
                    "Metric": (
                        "Process RAM"
                    ),

                    "PyTorch": round(
                        pytorch_metrics[
                            "process_ram_after_mb"
                        ],
                        2,
                    ),

                    "ONNX": round(
                        onnx_metrics[
                            "process_ram_after_mb"
                        ],
                        2,
                    ),

                    "Reduction": (

                        f"{ram_reduction:.2f}%"

                        if ram_reduction
                        is not None

                        else "N/A"
                    ),
                },
            ]


            # ------------------------------------------------
            # GPU memory comparison
            # ------------------------------------------------

            pytorch_gpu_memory = (
                pytorch_metrics[
                    "gpu_after"
                ]["gpu_memory_mb"]
            )

            onnx_gpu_memory = (
                onnx_metrics[
                    "gpu_after"
                ]["gpu_memory_mb"]
            )


            if (
                pytorch_gpu_memory
                is not None

                and onnx_gpu_memory
                is not None
            ):

                comparison_rows.append(
                    {
                        "Metric": (
                            "GPU Memory"
                        ),

                        "PyTorch": round(
                            pytorch_gpu_memory,
                            2,
                        ),

                        "ONNX": round(
                            onnx_gpu_memory,
                            2,
                        ),

                        "Reduction": (

                            f"{gpu_memory_reduction:.2f}%"

                            if gpu_memory_reduction
                            is not None

                            else "N/A"
                        ),
                    }
                )


            st.dataframe(
                pd.DataFrame(
                    comparison_rows
                ),
                use_container_width=True,
                hide_index=True,
            )


            # =================================================
            # RESOURCE EFFICIENCY
            # =================================================

            st.header(
                "💰 Resource Utilization & Cost Efficiency"
            )

            st.caption(
                "These values represent measured resource "
                "differences on the current machine. "
                "They are not direct cloud billing estimates."
            )


            efficiency_col1, efficiency_col2 = (
                st.columns(2)
            )


            with efficiency_col1:

                st.subheader(
                    "Latency Efficiency"
                )

                if latency_reduction is not None:

                    st.metric(
                        "Latency Reduction",
                        f"{latency_reduction:.2f}%",
                    )


                if fps_change is not None:

                    st.metric(
                        "Throughput Change",
                        f"{fps_change:.2f}%",
                    )


            with efficiency_col2:

                st.subheader(
                    "Memory Efficiency"
                )

                if ram_reduction is not None:

                    st.metric(
                        "Process RAM Reduction",
                        f"{ram_reduction:.2f}%",
                    )


                if gpu_memory_reduction is not None:

                    st.metric(
                        "GPU Memory Reduction",
                        f"{gpu_memory_reduction:.2f}%",
                    )


            # =================================================
            # SUMMARY
            # =================================================

            st.header(
                "🏁 Benchmark Summary"
            )


            if (
                latency_reduction is not None
                and latency_reduction > 0
            ):

                st.success(
                    f"ONNX Runtime reduced measured mean "
                    f"inference latency by "
                    f"{latency_reduction:.2f}% "
                    f"under this benchmark configuration."
                )

            elif latency_reduction is not None:

                st.info(
                    "ONNX Runtime did not reduce mean "
                    "latency under this benchmark configuration."
                )


            st.warning(
                "Benchmark results depend on hardware, "
                "execution provider, model configuration, "
                "warm-up strategy, and workload. "
                "Use repeated benchmark runs when reporting "
                "results publicly."
            )