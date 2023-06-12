import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns
import numpy as np
import plotly.express as px
import pandas_bokeh
import requests
import json
import bokeh.plotting as bpl
from bokeh.palettes import Spectral11
from bokeh.models import NumeralTickFormatter, Legend

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/Results%20dataset%20Sephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
# Dashboard
def main():
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")
    
    filtered_data = Data[(Data['secondary_category'] == Category) & (Data['skin_tone'] == Skin) & (Data['skin_type'] == Type)]
    if len(filtered_data) > 0:
        st.write("Hasil Pencarian:")
        st.table(filtered_data[['product_name', 'brand_name', 'review_title', 'loves_count', 'price_usd', 'review_text']])
    else:
        st.write("Maaf, tidak ada produk yang cocok dengan pilihan Anda.")
            

if __name__ == "__main__":
    main()
