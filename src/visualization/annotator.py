from PIL import Image, ImageDraw

from src.schemas import Detection


def annotate_image(
    image: Image.Image,
    detections: list[Detection],
) -> Image.Image:
    """Draw detection bounding boxes and labels on an image."""

    annotated = image.copy().convert("RGB")
    draw = ImageDraw.Draw(annotated)

    for detection in detections:
        box = (
            detection.x1,
            detection.y1,
            detection.x2,
            detection.y2,
        )

        label = (
            f"{detection.class_name} "
            f"{detection.confidence:.2f}"
        )

        draw.rectangle(box, outline="red", width=3)
        draw.text(
            (detection.x1, max(0, detection.y1 - 18)),
            label,
            fill="red",
        )

    return annotated