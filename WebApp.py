import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/Results%20dataset%20Sephora.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
# Function to get top 5 similar products
def get_top_similar_products(product_name):
        index = indices[product_name]
        similarity_scores = list(enumerate(cosine_similarities[index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similarity_scores = similarity_scores[1:6]  # Exclude the same product
        product_indices = [score[0] for score in similarity_scores]
        return product_names.iloc[product_indices]
      
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
            
    product_name = get_top_similar_products(product_name)
            

if __name__ == "__main__":
    main()
