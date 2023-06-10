import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
      Eye = st.selectbox('Eye Color', Data['eye_color'].unique())
        
        
fig = px.scatter(data_frame=Data,x=Category, y=Skin, size =Type,Eye=Color,log_x=True,log_y=True,size_max=Circle_area)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

