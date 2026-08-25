import streamlit as st
from PIL import Image

from src.inference import InferencePipeline
from src.model import YOLOModel
from src.visualization import annotate_image

from src.ui.theme import apply_theme


st.set_page_config(
    page_title="Damage Detection",
    page_icon="🔍",
    layout="wide",
)

apply_theme()

@st.cache_resource
def load_pipeline():
    model = YOLOModel()
    model.load()
    return InferencePipeline(model)


st.title("🔍 Vehicle Damage Detection")

st.caption(
    "Upload an image and run the trained YOLO11n model."
)

uploaded_file = st.file_uploader(
    "Upload vehicle image",
    type=["jpg", "jpeg", "png", "webp"],
)


if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.markdown("### Input Image")

    st.image(
        image,
        width=700,
    )

    if st.button(
        "🚀 Detect Vehicle Damage",
        type="primary",
    ):

        pipeline = load_pipeline()

        with st.spinner("Running YOLO11n inference..."):

            detections = pipeline.predict(image)

            annotated = annotate_image(
                image,
                detections,
            )

        st.success("Inference completed.")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Original")

            st.image(
                image,
                width=700,
            )

        with col2:

            st.markdown("### Detection Result")

            st.image(
                annotated,
                width=700,
            )

        st.markdown("### Detection Summary")

        if not detections:

            st.info(
                "No vehicle damage was detected "
                "above the configured confidence threshold."
            )

        else:

            for detection in detections:

                st.markdown(
                    f"""
                    **{detection.class_name}**

                    Confidence: `{detection.confidence:.2%}`
                    """
                )

                st.progress(
                    min(detection.confidence, 1.0)
                )

else:

    st.info(
        "Upload a JPG, JPEG, PNG or WEBP vehicle image "
        "to begin detection."
    )