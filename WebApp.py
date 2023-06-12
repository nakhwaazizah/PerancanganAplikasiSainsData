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
      
filtered_data = Data[(Data['secondary_category'] == category) & (Data['skin_tone'] == skin_tone) & (Data['skin_type'] == skin_type)]

# Dashboard
def main():
    # Halaman Utama (Home)
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")

    if len(filtered_data) > 0:
            st.write("Hasil Pencarian:")
            st.table(filtered_data[['product_name', 'brand', 'description']])
      else:
            st.write("Maaf, tidak ada produk yang cocok dengan pilihan Anda.")

if __name__ == "__main__":
    main()


