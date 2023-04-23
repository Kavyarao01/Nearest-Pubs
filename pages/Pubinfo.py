from codecs import latin_1_decode
import streamlit as st
from matplotlib import image
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.markdown("<h1 style='text-align: center; color: Red;'>Pub Info </h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: Red;'>About Us </h2>", unsafe_allow_html=True)

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.lsst.ac/wp-content/uploads/hd_party_wallpaper.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "clean_open_pubs.csv")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.subheader(f"Total Pubs: :green[{df['name'].nunique()}]")
st.subheader(f"Total Post Codes: :green[{df['postcode'].nunique()}]")
st.subheader(f"Total Local Authorities:  :green[{df['local_authority'].nunique()}]")


Country = st.selectbox("Select the Option:", df['local_authority'].unique())

col1, col2= st.columns(2)


fig_1 = px.histogram(df[df['local_authority'] == Country], x="local_authority")
col1.plotly_chart(fig_1, use_container_width=True)











