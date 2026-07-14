import streamlit as st
import os

from ziko_st_toc import table_of_contents

# --------- IMAGE PATHS ---------
IMG_INTRO = "./resources/photo_intro.jpg"
IMG_TA = "./resources/photo_TA.jpg"
IMG_LRC = "./resources/photo_LRC.jpeg"
IMG_OR = "./resources/photo_OR.png"
# -------------------------------------

# -------- SIDEBAR -------------
with st.sidebar:
    st.caption("Table of contents")
    table_of_contents()


# --------- EDUCATION ------------- 
st.subheader("Education", divider="gray")
col1_ED, col2_ED = st.columns(2)
with col1_ED:
    st.markdown(
        """
        ##### **MS in Mathematics** (2024 - present)

        *University of the Philippines Los Baños*

        **Track**: Applied Mathematics

        **Research Focus**: Filipino sign language recognition 
        """
    ,
    text_alignment="center")
with col2_ED:
    st.markdown(
        """
        ##### **BS in Applied Mathematics** (2020 - 2024)

        *University of the Philippines Los Baños*

        **Awards**: :blue[Summa Cum Laude], DOST Undergraduate Scholar

        **Specialization**:
        Quantitative Management and Decision Science

        **Relevant Courses Taken**:
        Optimization, Numerical Analysis, Mathematical Modeling, Machine Learning, Complex Networks, Topological Data Analysis
        """
    ,
    text_alignment="center")

# --------- EXPERIENCE ------------- 
st.subheader("Experience", divider="gray")

# -- IHG
st.markdown("##### Business Intelligence Analyst/Specialist, :gray[IHG Hotels & Resorts]")
col1_IHG, col2_IHG, col3_IHG = st.columns(3)
with col1_IHG:
    pass
with col2_IHG:
    st.markdown(
        """
        **BI Analyst**   *(Apr 2025 - Jun 2026)*
        - Developed and maintained strategies to execute reporting needs, data gathering, trend analysis, and
        communicate business insights for various sites under the Reservations and Customer Care (RCC).
        - Developed automated solutions using Python API calls and Power Automate to streamline delivery of
        Tableau dashboards, Excel reports, and Powerpoint decks.
        - Collaborated with the BI-Sales team to streamline a Tableau data extract and distribution process
        dedicated to 250+ hotels.
        """
    )
with col3_IHG:
    st.markdown(
        """
        **BI Specialist**   *(Jun 2026 - present)*
        - Manages integrity of field marketing global participation data for accurate tracking and billing.
        - Oversees and develop key automation processes to enhance workflows that help drive scalability of field marketing services.
        """
    )

st.markdown('---')

# -- Teaching Associate
col1_TA, col2_TA = st.columns(2)
with col1_TA:
    if os.path.exists(IMG_TA):
        st.image(IMG_TA, width=480)
    else:
        st.warning("Image not found.")
with col2_TA:
    st.markdown("##### Teaching Associate, :gray[IMS UPLB]", text_alignment='left')
    st.markdown("""
                - Delivered instruction of an analytical geometry and calculus course to multiple undergraduate classes,
                ensuring consistent course coverage and assessment.
    """)

st.markdown('---')
# -- Teaching Associate
col1_LRC, col2_LRC = st.columns(2)
with col1_LRC:
    st.markdown("##### Math Peer Tutor, :gray[UPLB Learning Resource Center]", text_alignment='left')
    st.markdown("""
                - Conducted tutorial sessions in mathematics courses offered by UPLB e.g., *Fundamental Calculus,
                Theory of Interest*, and *Mathematical Analysis*.
                - Lectured as the resource speaker at a large class tutorial session of up to 100 students taking *Fundamental Calculus^.
                - Participated in pioneering a fully online self-enroll courses in Canvas for students taking Calculus by
                writing modules and recording supplementary video lectures.
    """)
with col2_LRC:
    if os.path.exists(IMG_LRC):
        st.image(IMG_LRC, width=480)
    else:
        st.warning("Image not found.")

st.markdown('---')
# -- OR Intern
col1_OR, col2_OR = st.columns(2)
with col1_OR:
    if os.path.exists(IMG_OR):
        st.image(IMG_OR, width=480)
    else:
        st.warning("Image not found.")
with col2_OR:
    st.markdown("##### Operations Research Intern, :gray[PASYENTE Project for Dengue]", text_alignment='left')
    st.markdown("""
                - Crafted dummy data backed up with related literature for queueing simulation models.
                - Organized a program for a queueing system using Python and SimPy. 
    """)

# --------- AFFILIATIONS -------------
st.subheader("Affiliations", divider="gray")
col1_aff, col2_aff = st.columns(2)
with col1_aff:
    st.markdown(
    """
    ##### [UP Hin-ay](https://www.facebook.com/UPHinay1991)

    Academics Comittee Head

    Pioneered the conduct of outreach activities that promote the development of education
    in Irosin, Sorsogon
    """,
    text_alignment="center"
    )

with col2_aff:
    st.markdown(
    """
    ##### [UPLB Actuarial Science Society](https://www.facebook.com/UPLBActSS)

    Asst. Head, Scholastics Committee

    Contributed in preparation for events that promote the actuarial science field internally
    and externally of the organization.
    """,
    text_alignment="center"
    )


