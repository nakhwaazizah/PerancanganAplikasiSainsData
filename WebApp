import streamlit as st 
import pandas as pd 
import numpy as np

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox(
      'primary_category',
      (Data.columns.values))
      
      Category2 = st.selectbox(
      'second_category',
      (Data.columns.values))
      
      Skin = st.selectbox(
      'skin_tone',
      (Data.columns.values))
      
      Type = st.selectbox(
      'skin_type',
      (Data.columns.values))
      
      Eye = st.selectbox(
      'eye_color',
      (Data.columns.values))

      st.write('Primary Category:', Category)
      st.write('Secondary Category:', Category2)
      st.write('Skin Tone:', Skin)
      st.write('Skin Type:', Type)
      st.write('Eye Color:', Eye)
