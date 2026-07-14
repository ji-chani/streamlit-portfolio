import streamlit as st
import os

from ziko_st_toc import table_of_contents

# --------- IMAGE PATHS ---------
IMG_FSL = './resources/photo_live_fsl.png'
IMG_BC = './resources/photo_breastcancer.png'
IMG_SP = './resources/photo_sp.png'
IMG_HVG = './resources/photo_hvg.png'
IMG_DSS = './resources/photo_dss.png'
IMG_TOP = './resources/photo_topopy.png'

st.set_page_config(
    page_title="CBJ Portfolio",
    layout="wide"
)

# -------- SIDEBAR
with st.sidebar:
    st.caption("Table of contents")
    table_of_contents()


# -------- RESEARCH ---------
st.subheader("Research", divider="gray")
st.caption(':red[Click "Read More" in each item to learn more about them!]')

if "title" not in st.session_state:
    st.session_state.title = None
if "content" not in st.session_state:
    st.session_state.content = None

@st.dialog(" ", width="medium")
def show_more_details():
    if st.session_state.title == "FSL":
        st.markdown("""## Filipino Sign Language Alphabet Recognition Using Persistent Homology Classification Algorithm""",
                    text_alignment="center")

        if os.path.exists(IMG_FSL):
            st.image(IMG_FSL, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    This paper explores Topological Data Analysis (TDA), an emerging field of study that harnesses techniques 
                    from computational topology, for Filipino sign language (FSL) recognition. A TDA-inspired classifier called 
                    Persistent Homology Classification Algorithm (PHCA) is used to classify static alphabet signed using FSL and
                    compare its result with classical classifiers. Results show that PHCA and Support Vector Machine (SVM) performed
                    better than the other classifiers, having mean Accuracy of 99.31% and 99.45%, respectively. Further analysis shows
                    that PHCA's performance is not significantly different from SVM, indicating that PHCA performed at par with the
                    best performing classifier.
                    """)
        st.markdown("---")
        st.markdown("Full paper can be accessed [here](https://peerj.com/articles/cs-2720/).")

    if st.session_state.title == "BC":
        st.markdown("""## Topological Insights and Hybrid Feature Extraction for Mass Breast Cancer Classification""",
                    text_alignment="center")

        if os.path.exists(IMG_BC):
            st.image(IMG_BC, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    This paper harnesses the computational flexibility of Persistent Homology in classification of mammogram scans. 
                    These scans are used in medicine wherein breast tissues are exposed to small amounts of X-ray radiation to obtain 
                    an inside picture of the breast details for the purpose of abnormality/mass detection and classification. Particularly, 
                    it aims to differentiate benign breast tumors from their malignant counterparts using the breast mammogram. 
                    Classification between benign and malignant images is done using Persistent Homology Classification Algorithm (PHCA).
                    """)
        st.markdown("---")
        st.markdown("Full paper can be accessed [here](https://peerj.com/articles/cs-3374/).")

    if st.session_state.title == "HVG":
        st.markdown("""## Classification of Time Series Electrocardiogram (ECG) signals using Horizontal Visibility Graphs""",
                    text_alignment="center")

        if os.path.exists(IMG_HVG):
            st.image(IMG_HVG, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    Electrocardiogram (ECG) signals are used in medicine to identify signs of cardiovascular diseases of a patient. 
                    This is done by observing and identifying possible abnormalities in the time series signal. Machine learning tools 
                    has been utilized to aid this classification problem, that is classifying normal and abnormal ECG signals. 
                    But with the introduction of Visibility Algorithm which converts time series data into a complex network, 
                    different approaches were developed to solve the classification problem. This paper presents a simple approach 
                    to perform ECG signal classification by utilizing graph properties obtained from visibility graphs corresponding 
                    to the signals. The classification is done using Logistic Regression which resulted with a promising overall 
                    accuracy of 96.9%.
                    """)
        st.markdown("---")
        st.markdown("Code repository is available [here](https://github.com/ji-chani/ClassificationECGwithHVG).")

    if st.session_state.title == "SP":
        st.markdown("""## Comparing Persistent Homology-based classifiers for FSL recognition""",
                    text_alignment="center")

        if os.path.exists(IMG_SP):
            st.image(IMG_SP, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    This paper aims to utilize the Persistent Homology Classification Algorithm (PHCA) in classifying or interpreting dynamic FSL gestures. 
                    Due to many distinct classes considered in this problem, this paper also aims to develop the multi-level PHCA in which this approach divides
                    the classification task. It does so by defining categories consisting of classes and performing two-part classification, first on the 
                    categories, and second on the classes within the selected category. The performance of PHCA and multi-level PHCA using different
                    classification metrics is evaluated. The predicting and training time of the models are also compared. Results show that both PHCA and 
                    multi-level PHCA produced satisfactory performance for SLR. It is shown further that multi-level PHCA outperformed PHCA in all setups considered, 
                    producing an accuracy of 85% for 10 classes and 60.99% on 105 classes, indicating a potential for further research.
                    """)
        st.markdown("---")
        st.markdown("Full paper can be accessed [here](https://doi.org/10.23939/mmc2025.02.512).")

    if st.session_state.title == "DSS":
        st.markdown("""## Decision Support System for Selecting UPLB BS AMAT/MATH Major Courses using Analytic Hierarchy Process""",
                    text_alignment="center")

        if os.path.exists(IMG_DSS):
            st.image(IMG_DSS, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    Before becoming a 3rd-year student, every student pursuing a degree in BS Applied Mathematics or BS Mathematics must submit their Plan of Study (POS). 
                    This process involves determining their specialization, opting for either a thesis or a special problem, selecting their thesis/SP adviser, choosing major 
                    and free electives, and scheduling when to take them. While an orientation covers these aspects, many students struggle in selecting their electives. 
                    Hence, this project aims to be an aid in selecting major courses that are based on the student’s preference, the courses’ perceived difficulty, 
                    availability of slots, and peer pressure. Specifically, this project aims to create a decision support system for students in selecting major courses. 
                    The development of the decision support system (DSS) was successfully implemented using the Analytic Hierarchy Process (AHP) framework. 
                    Upon inputting the necessary data into the system, the DSS generates ranked courses based on all the criteria stated and provides a list of major courses, 
                    ordered according to their overall importance determined by the AHP process.
                    """)
        st.markdown("---")
        st.markdown("Code repository is available [here](https://github.com/ji-chani/DSS-AHP).")

    if st.session_state.title == "TOP":
        st.markdown("""## TopoPy: Topological Data Analysis in Python""",
                    text_alignment="center")

        if os.path.exists(IMG_TOP):
            st.image(IMG_TOP, width='stretch')
        else:
            st.warning("Image not found.")

        st.markdown("""
                    Aside from learning the various fields of study, it is also my passion to impart my knowledge to other people in the hopes that they may share the same 
                    interest in the field. This applies also to TDA. To facilitate these sharing, I usually prepare discussion materials in the form of Jupyter notebook 
                    to include implementation examples.
                    """)
        st.markdown("---")
        st.markdown("One of such notebooks is available [here](https://colab.research.google.com/drive/1TKwzVuKEIQNBbyKYLn9ejHX_RyY_MJPk#scrollTo=AMMqzNwLo4QQ).")
    
    if st.button("Close"):
        st.rerun()


row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)

container_FSL = row1[0].container(border=True)
container_BC = row1[1].container(border=True)
container_HVG = row2[0].container(border=True)
container_SP = row2[1].container(border=True)
container_DSS = row3[0].container(border=True)
container_TOP = row3[1].container(border=True)

with container_FSL:
    st.markdown("""
                #### Filipino Sign Language Alphabet Recognition Using Persistent Homology Classification Algorithm
            
                Exploring the potential of :red[*topological data analysis (TDA)*] to recognize the alphabet signed using the
                Filipino sign language. 
            """,
            )
    if st.button("Read More", key="FSL"):
        st.session_state.title = "FSL"
        show_more_details()
    
    if os.path.exists(IMG_FSL):
        st.image(IMG_FSL, width='stretch')
    else:
        st.warning("Image not found.")
    st.space(123)  # to match height of container_BC
    
with container_BC:
    st.markdown("""
                #### Topological Insights and Hybrid Feature Extraction for Mass Breast Cancer Classification
            
                Harnessing the robustness and computational flexibility of :red[*Persistent Homology*] to classify breast image scans into having
                benign or malignant tumors.
            """,
            )
    if st.button("Read More", key="BC"):
        st.session_state.title = "BC"
        show_more_details()

    if os.path.exists(IMG_BC):
        st.image(IMG_BC, width='stretch')
    else:
        st.warning("Image not found.")

with container_HVG:
    st.markdown("""
                #### Classification of Time Series Electrocardiogram (ECG) signals using Horizontal Visibility Graphs
            
                Fusing two fields, :red[*Complex Networks and Machine Learning*], to detect heart abnormalities in ECG signals of a patient.
            """,
            )
    
    if st.button("Read More", key="HVG"):
        st.session_state.title = "HVG"
        show_more_details()

    if os.path.exists(IMG_HVG):
        st.image(IMG_HVG, width='stretch')
    else:
        st.warning("Image not found.")
    st.space(67)

with container_SP:
    st.markdown("""
                #### Comparing Persistent Homology-based classifiers for FSL recognition
            
                Improving on a topological data analysis-based algorithm to classify many distinct classes of dynamic FSL gestures.
            """,
            )
    
    if st.button("Read More", key="SP"):
        st.session_state.title = "SP"
        show_more_details()

    if os.path.exists(IMG_SP):
        st.image(IMG_SP, width='stretch')
    else:
        st.warning("Image not found.")

with container_DSS:
    st.markdown("""
                #### Decision Support System for Selecting UPLB BS AMAT/MATH Major Courses using Analytic Hierarchy Process
            
                Crafted a decision support system that incorporates a multi-criteria decision technique to select major courses
                for BS Math and Applied Students from UPLB.
            """,
            )
    if st.button("Read More", key="DSS"):
        st.session_state.title = "DSS"
        show_more_details()

    if os.path.exists(IMG_DSS):
        st.image(IMG_DSS, width='stretch')
    else:
        st.warning("Image not found.")

with container_TOP:
    st.markdown("""
                #### TopoPy: Topological Data Analysis in Python
            
                Developed a Colab notebook to discuss TDA use-cases and surface-level theory with Python.
            """,
            )
    
    if st.button("Read More", key="TOP"):
        st.session_state.title = "TOP"
        show_more_details()

    if os.path.exists(IMG_TOP):
        st.image(IMG_TOP, width='stretch')
    else:
        st.warning("Image not found.")
    st.space(64)