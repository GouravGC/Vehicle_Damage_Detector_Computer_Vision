from pathlib import Path


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "model"
CONFIG_DIR = PROJECT_ROOT / "configs"
METRICS_DIR = PROJECT_ROOT / "metrics"
INFERENCE_DIR = PROJECT_ROOT / "inference"

MODEL_PATH = MODEL_DIR / "vehicle_damage_yolo11n_best.pt"
ONNX_MODEL_PATH = MODEL_DIR / "vehicle_damage_yolo11n_best.onnx"

CONFIG_PATH = CONFIG_DIR / "Vehicle Damage Collab.yaml"
METRICS_PATH = METRICS_DIR / "test_metrics.json"
INFERENCE_PATH = INFERENCE_DIR


# ---------------------------------------------------------------------------
# Inference configuration
# ---------------------------------------------------------------------------

IMAGE_SIZE = 640

CONFIDENCE_THRESHOLD = 0.50
IOU_THRESHOLD = 0.50