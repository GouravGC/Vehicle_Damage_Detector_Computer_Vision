from pathlib import Path

from PIL import Image

from src.components.logger import logger
from src.exceptions import ImageValidationError, InferenceError
from src.model import YOLOModel
from src.schemas import Detection


class InferencePipeline:
    """Validate input and convert YOLO output into application results."""

    def __init__(self, model: YOLOModel) -> None:
        self.model = model

    @staticmethod
    def validate_image(image) -> Image.Image:
        """Validate and normalize an input image."""

        if isinstance(image, (str, Path)):
            image = Image.open(image)

        if not isinstance(image, Image.Image):
            raise ImageValidationError(
                "Input must be a PIL image or a valid image path."
            )

        if image.width <= 0 or image.height <= 0:
            raise ImageValidationError("Image dimensions are invalid.")

        return image.convert("RGB")

    def predict(self, image) -> list[Detection]:
        """Run inference and return structured detections."""

        image = self.validate_image(image)

        if not self.model.is_loaded():
            self.model.load()

        try:
            results = self.model.predict(image)

            detections = []

            if not results:
                return detections

            result = results[0]

            if result.boxes is None:
                return detections

            names = result.names

            for box in result.boxes:
                class_id = int(box.cls.item())
                confidence = float(box.conf.item())

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detections.append(
                    Detection(
                        class_id=class_id,
                        class_name=names[class_id],
                        confidence=confidence,
                        x1=float(x1),
                        y1=float(y1),
                        x2=float(x2),
                        y2=float(y2),
                    )
                )

            logger.info(
                "Inference completed successfully. Detections: %d",
                len(detections),
            )

            return detections

        except Exception as exc:
            if isinstance(exc, InferenceError):
                raise

            logger.exception("Inference pipeline failed.")
            raise InferenceError("Inference pipeline failed.") from exc