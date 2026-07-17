import streamlit as st
import os


# --------- IMAGE/ICON PATHS ---------
IMG_INTRO = "./resources/photo_intro.jpg"
ICON_LINKEDIN = './resources/icons/logo_linkedin.png'
ICON_RG = './resources/icons/logo_rg.png'
ICON_GH = './resources/icons/logo_github.png'
ICON_GM = './resources/icons/logo_gmail.png'
# -------------------------------------

st.set_page_config(
    page_title="CBJ Portfolio",
    layout="wide"
)
st.title("🚀Cristian Jetomo")

# -------- SIDEBAR
with st.sidebar:
    st.markdown("*If you wish to contact me, kindly use the icons!* 😊")

# --------- ABOUT ME -------------

col1_intro, col2_intro = st.columns(2)
with col1_intro:
    st.markdown(
    """
    Hi! I'm Cristian, an :rainbow[applied math enthusiast].
    
    I'm a graduate student in Mathematics at UPLB with a degree in Applied Mathematics.
    My interest is doing research on **Optimization**, **Data Science**, **Machine Learning**,
    and its fuse with **Topological Data Analysis**.

    Aside from research, I served as a Teaching Associate at UPLB, sharing my expertise and knowledge in my domain of study.
    I've worked with on numerous projects that uses techniques I learned from class and independent studies.
    These projects mainly focus on Filipino sign language recognition, breast cancer classification, heart disase diagnosis,
    and decision support systems.
    
    Currently, my time is being spent as a **Business Intelligence Specialist** at 
    *IHG Hotels & Resorts*. My role is focused on managing the integrity of data for the field marketing team,
    making sure that the billing and tracking of hotels and services are accurate. I also develop automated
    solutions to streamline workflows and processes that drives the operations of the team more effectively.

    If you're also passionate to use applied math tools for impactful projects, :red[***I'm interested to collaborate!***]

    Kindly reach out by clicking any of the respective platforms below.
    """
    )

    _, col1, col2, col3, col4, _ = st.columns([10,1,1,1,1, 10])
    with col1:
        st.image(ICON_LINKEDIN, 
                width=30,
                link="https://www.linkedin.com/in/cristian-jetomo/",
                )
    with col2:
        st.image(ICON_RG, 
                width=20,
                link="https://www.researchgate.net/profile/Cristian-Jetomo?ev=hdr_xprf",
                )
        
    with col3:
        st.image(ICON_GH, 
                width=25,
                link="https://github.com/ji-chani",
                )

    with col4:
        st.image(ICON_GM, 
                width=35,
                link="mailto:chanjetomo@gmail.com",
                )
        

with col2_intro:
    if os.path.exists(IMG_INTRO):
        st.image(IMG_INTRO, width=480)
    else:
        st.warning("Intro image not found.")
