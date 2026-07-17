import streamlit as st

st.set_page_config(
    page_title="CBJ Portfolio",
    layout="wide"
)

pages = {   
    "About Me": [
        st.Page("./pages/1.1_Intro.py", title="Intro"),
        st.Page("./pages/1.2_Education_Experience.py", title="Education and Experiences"),
        st.Page("./pages/1.3_Recognition_Awards.py", title="Recognition and Awards"),
    ],
    "Things I Do": [
        st.Page("./pages/2.1_Research.py", title="Research"),
        st.Page("./pages/2.2_Activities.py", title="Activities")
    ]
}

pg = st.navigation(pages, position='top')
pg.run()
