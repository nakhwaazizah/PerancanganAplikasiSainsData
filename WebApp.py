import streamlit as st 
import pandas as pd 
import numpy as np

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)

def main():
    # Halaman Utama (Home)
    st.title("Beauty Things")
    st.write("Hello Beauty!")
    st.write("Silakan ke halaman dasbor untuk melihat lebih banyak informasi.")

    # Halaman Dasbor (Dashboard)
    if st.button("Halaman Dasbor"):
        st.title("Dasbor")
        st.write("Ini adalah halaman dasbor.")
        # Tambahkan kode tambahan untuk menampilkan informasi lebih lanjut di dasbor

if __name__ == "__main__":
    main()

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
      Eye = st.selectbox('Eye Color', Data['eye_color'].unique())

