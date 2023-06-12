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
    # Halaman Utama (Home)
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")
#     filtered_data = [data(data[primary_category] == selected_primary_category) & data(data['secondary_category'] == selected_secondary_category) & data(data['skin_type'] == selected_skin_type) & (data['skin_tone'] == selected_skin_tone)]

# # Jika ada produk yang cocok dengan pilihan pengguna
# if not filtered_data.empty:
#     # Define TF-IDF vectorizer
#     vectorizer = TfidfVectorizer()

#     # Apply TF-IDF vectorizer to review text
#     tfidf_matrix = vectorizer.fit_transform(filtered_data['review_text'])

#     # Calculate cosine similarity matrix
#     cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

#     # Get product names and indices
#     product_names = filtered_data['product_name']
#     indices = pd.Series(filtered_data.index, index=filtered_data['product_name'])

    product_name = get_top_similar_product(product_name)

if __name__ == "__main__":
    main()


