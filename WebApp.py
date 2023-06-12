import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
      Eye = st.selectbox('Eye Color', Data['eye_color'].unique())
        
filtered_data = [data(data[primary_category] == selected_primary_category) & data(data['secondary_category'] == selected_secondary_category) & data(data['skin_type'] == selected_skin_type) & (data['skin_tone'] == selected_skin_tone)]

# Dashboard
def main():
    # Halaman Utama (Home)
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")

if __name__ == "__main__":
    main()


