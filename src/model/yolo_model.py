from pathlib import Path

from ultralytics import YOLO

from src.components.logger import logger
from src.config import MODEL_PATH, IMAGE_SIZE, CONFIDENCE_THRESHOLD, IOU_THRESHOLD
from src.exceptions import ModelLoadingError, InferenceError


class YOLOModel:
    """Production wrapper around the YOLO model."""

    def __init__(self, model_path: Path = MODEL_PATH) -> None:
        self.model_path = Path(model_path)
        self.model = None

    def load(self) -> None:
        """Load the YOLO model into memory."""

        if not self.model_path.exists():
            raise ModelLoadingError(
                f"Model file not found: {self.model_path}"
            )

        try:
            logger.info("Loading YOLO model from: %s", self.model_path)

            self.model = YOLO(str(self.model_path))

            logger.info("YOLO model loaded successfully.")

        except Exception as exc:
            logger.exception("Failed to load YOLO model.")

            raise ModelLoadingError(
                f"Failed to load YOLO model from {self.model_path}"
            ) from exc

    def is_loaded(self) -> bool:
        """Return whether the model is currently loaded."""

        return self.model is not None

    def predict(self, image):
        """Run YOLO inference on an image."""

        if not self.is_loaded():
            raise InferenceError("YOLO model has not been loaded.")

        try:
            return self.model.predict(
                source=image,
                imgsz=IMAGE_SIZE,
                conf=CONFIDENCE_THRESHOLD,
                iou=IOU_THRESHOLD,
                verbose=False,
            )

        except Exception as exc:
            logger.exception("YOLO inference failed.")
            raise InferenceError("YOLO inference failed.") from exc