import json
from pathlib import Path

import streamlit as st

from src.ui.theme import apply_theme

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide",
)

apply_theme()

st.title("📊 Model Analytics")

st.caption(
    "Evaluation information available from the project artifacts."
)


metrics_path = Path("metrics/test_metrics.json")


if metrics_path.exists():

    with metrics_path.open("r", encoding="utf-8") as file:
        metrics = json.load(file)

    st.subheader("Test Evaluation")

    if isinstance(metrics, dict):

        columns = st.columns(
            min(len(metrics), 4)
        )

        for index, (key, value) in enumerate(metrics.items()):

            with columns[index % len(columns)]:

                st.metric(
                    label=str(key).replace("_", " ").title(),
                    value=str(value),
                )

        st.markdown("### Evaluation Artifact")

        with st.expander("View raw metrics"):

            st.code(
                json.dumps(metrics, indent=2),
                language="json",
            )

else:

    st.warning(
        "Test metrics artifact was not found."
    )