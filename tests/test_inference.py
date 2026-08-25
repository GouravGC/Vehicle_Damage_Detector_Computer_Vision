from pathlib import Path

from src.inference import InferencePipeline
from src.model import YOLOModel


def test_inference_on_real_image():
    image_files = [
        path
        for path in Path("inference").rglob("*")
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]

    assert image_files

    pipeline = InferencePipeline(YOLOModel())

    detections = pipeline.predict(image_files[0])

    assert isinstance(detections, list)