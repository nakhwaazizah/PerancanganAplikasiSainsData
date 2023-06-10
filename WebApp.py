import streamlit as st 
import pandas as pd 
import numpy as np

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox(
      'Primary Category', Data['primary_category'].unique)
      
      Category2 = st.selectbox(
      'second_category', Data['second_category'].unique)
      
      Skin = st.selectbox(
      'skin_tone', Data['skin_tone'].unique)
      
      Type = st.selectbox(
      'skin_type', Data['skin_type'].unique)
      
      Eye = st.selectbox(
      'eye_color', Data['eye_color'].unique)

      st.write('Primary Category:', Category)
      st.write('Secondary Category:', Category2)
      st.write('Skin Tone:', Skin)
      st.write('Skin Type:', Type)
      st.write('Eye Color:', Eye)
