import streamlit as st 
import pandas as pd 
import numpy as np

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox('Primary Category', Data['primary_category'].unique())
      
      Category2 = st.selectbox('Secondary Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
      Eye = st.selectbox('Eye Color', Data['eye_color'].unique())

      st.write('Primary Category:', Category)
      st.write('Secondary Category:', Category2)
      st.write('Skin Tone:', Skin)
      st.write('Skin Type:', Type)
      st.write('Eye Color:', Eye)
