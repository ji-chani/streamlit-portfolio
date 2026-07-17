import os

import streamlit as st
import numpy as np
from ziko_st_toc import table_of_contents

# --------- IMAGE PATHS ---------
act_folder_path = "./resources/activities"
spk_folder_path = "./resources/speaker"
act_img_fnames = np.array([os.path.join(act_folder_path,f) 
                           for f in os.listdir(act_folder_path) if f.endswith(".jpg")]).reshape((2,3))
spk_img_fnames = np.array([os.path.join(spk_folder_path,f) 
                           for f in os.listdir(spk_folder_path) if f.endswith(".jpg")]).reshape((2,3))

act_captions = np.load(os.path.join(act_folder_path, 'captions.npy'), allow_pickle=True).item()
spk_captions = np.load(os.path.join(spk_folder_path, 'captions.npy'), allow_pickle=True).item()


st.set_page_config(
    page_title="CBJ Portfolio",
    layout="wide"
)

# -------- SIDEBAR
with st.sidebar:
    st.caption("Table of contents")
    table_of_contents()

# ----- ACTIVITIES
st.subheader("Activities", divider='gray')

for i in range(2):
    row = st.columns(3)

    for j in range(len(row)):
        with row[j].container(border=True, height=500):
            filename = os.path.basename(act_img_fnames[i,j])
            st.markdown(act_captions[filename[:-4]],
                        text_alignment="center") # remove .jpg and get corresponding caption
            if os.path.exists(act_img_fnames[i,j]):
                st.image(act_img_fnames[i,j], width='content')
            else:
                st.warning("Image not found.")


# ----- SPEAKERSHIPS
st.subheader("Speakerships", divider='gray')
for i in range(2):
    row = st.columns(3)

    for j in range(len(row)):
        with row[j].container(border=True, height=500):
            filename = os.path.basename(spk_img_fnames[i,j])
            st.markdown(spk_captions[filename[:-4]],
                        text_alignment="center") # remove .jpg and get corresponding caption
            if os.path.exists(spk_img_fnames[i,j]):
                st.image(spk_img_fnames[i,j], width='content')
            else:
                st.warning("Image not found.")