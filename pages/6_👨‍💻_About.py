# ============================================================
# PROJECT LINKS
# ============================================================

st.subheader("Project Links")

st.write(
    "Explore the source code, project repository, and professional profile."
)

link_col1, link_col2, link_col3 = st.columns(3)


# ============================================================
# GITHUB PROFILE
# ============================================================

with link_col1:

    st.markdown("### 💻 GitHub Profile")

    st.caption(
        "Explore the complete source code, projects, "
        "and development work."
    )

    st.link_button(
        "View GitHub Profile",
        "https://github.com/GouravGC",
    )


# ============================================================
# PROJECT REPOSITORY
# ============================================================

with link_col2:

    st.markdown("### 📦 Project Repository")

    st.caption(
        "View the source code and architecture of "
        "this vehicle damage detection project."
    )

    st.link_button(
        "View Repository",
        "https://github.com/GouravGC/Vehicle_Damage_Detector_Computer_Vision",
    )


# ============================================================
# LINKEDIN
# ============================================================

with link_col3:

    st.markdown("### 🔵 LinkedIn")

    st.caption(
        "Connect with me and explore my professional "
        "background and experience."
    )

    st.link_button(
        "View LinkedIn",
        "https://www.linkedin.com/in/gourav-chhatwani-9a301134a/",
    )