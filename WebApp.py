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
      

# Dashboard
def main():
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")
    
    filtered_data = Data[(Data['secondary_category'] == Category) & (Data['skin_tone'] == Skin) & (Data['skin_type'] == Type)]
    if len(filtered_data) > 0:
        st.write("Hasil Pencarian:")
        st.table(filtered_data[['product_name', 'brand_name', 'review_text']])
    else:
        st.write("Maaf, tidak ada produk yang cocok dengan pilihan Anda.")
            
    # Jika ada produk yang cocok dengan pilihan pengguna
    if not filtered_data.empty:
    # Define TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Apply TF-IDF vectorizer to review text
    tfidf_matrix = vectorizer.fit_transform(filtered_data['review_text'])

    # Calculate cosine similarity matrix
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Get product names and indices
    product_names = filtered_data['product_name']
    indices = pd.Series(filtered_data.index, index=filtered_data['product_name'])

if __name__ == "__main__":
    main()
