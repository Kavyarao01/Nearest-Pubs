import streamlit as st
import pydeck as pdk
import pandas as pd
from matplotlib import image
import os
import pandas as pd
import plotly.express as px
import numpy as np

st.markdown("<h1 style='text-align: center; color: Red;'>Nearest Pubs </h1>", unsafe_allow_html=True)


st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.wallpapersafari.com/55/7/9ia4UK.jpg");
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

#Take input -latitude and longitude
col1,col2=st.columns(2)
with col1:
    lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)
with col2:
    lon=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)

#Entered location
search_location=np.array((lat,lon))
#Original/available Location
original_location=np.array([df['latitude'],df['longitude']]).T

#Finding Euclidean distance
dist=np.sum((original_location-search_location)**2, axis=1)
#Adding Distance column to dataframe

df['Distance']=dist



#Asking user that how many nearest Pub they want to see
nearest=st.number_input(label="How Many Nearest Pub You Want to See",
                   min_value=1, max_value=50, value=5)
data=df.sort_values(by='Distance', ascending=True)[:nearest]

#List of Bar Names
st.subheader(f"{nearest} Nearest Pubs:")
st.table(data[['name','address','local_authority']])





#Show Nearest Pubs on Map
st.map(data=data, zoom=None, use_container_width=True)

