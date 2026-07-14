import streamlit as st
import os

from ziko_st_toc import table_of_contents

st.set_page_config(
    page_title="CBJ Portfolio",
    layout="wide"
)

# --------- IMAGE PATHS ---------
IMG_BOP = "./resources/photo_bop.png"
IMG_OSP = "./resources/photo_osp.png"
IMG_FN = "./resources/photo_finalist.png"
# -------------------------------------

# -------- SIDEBAR -------------
with st.sidebar:
    st.caption("Table of contents")
    table_of_contents()

st.subheader("Recognition and Awards", divider="gray")

col1, col2, col3 = st.columns(3)
with col1:
    if os.path.exists(IMG_BOP):
        st.image(IMG_BOP, width="stretch")
    else:
        st.warning("Image not found.")

    st.space(11)    
    st.markdown(
        """
        ##### Best in Oral Presentation in the Mathematical Sciences

        *16th UPLB-CAS Student-Faculty Conference*
        """,
    text_alignment="center")
with col2:
    if os.path.exists(IMG_OSP):
        st.image(IMG_OSP, width="stretch")
    else:
        st.warning("Image not found.")
        
    st.markdown(
        """
        ##### Outstanding Special Problem in Applied Mathematics

        *2024 Institute of Mathematical Sciences and Physics Awards*
        """,
    text_alignment="center")
with col3:
    if os.path.exists(IMG_FN):
        st.image(IMG_FN, width="stretch")
    else:
        st.warning("Image not found.")

    st.space(4)
    st.markdown(
        """
        ##### Finalist

        *UPLB MASS 47th Annual Search for Math Wizard 2023*
        """,
    text_alignment="center")
