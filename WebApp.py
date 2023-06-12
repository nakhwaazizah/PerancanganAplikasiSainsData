import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt
import re 
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

clean_spcl = re.compile('[/(){}\[\]\|@,;]')
clean_symbol = re.compile('[^0-9a-z #+_]')
stopworda = set(stopwords.words('english'))

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/Results%20dataset%20Sephora.csv'
Data = pd.read_csv(url)

title = "Beauty Things"
subtitle = "Let's find skincare for you!"

st.set_page_config(page_title = title,
                   page_icon = None,
                   layout = "wide")
      
st.sidebar.header("Select the options :")

with st.sidebar:          
      Category = st.selectbox('Category', Data['secondary_category'].unique())
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
def clean_text(text):
    text = text.lower() # lowercase text
    text = clean_spcl.sub(' ', text)
    text = clean_symbol.sub('', text)
    text = ' '.join(word for word in text.split() if word not in stopworda) # hapus stopword dari kolom deskripsi
    return text
  
def recommendations(name, cos_sim = cos_sim):
    recommendedProducts = []
    idx =indices[indices == name].index[0]
    score = pd.Series(cos_sim[idx]).sort_values(ascending = False)
    top_10 = list(score.iloc[1:11].index)
    for i in top_10:
        recommendedProducts.append(list(data.index)[i])
    return recommendedProducts
  
def main():
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")
    st.write("Dataset Visualization :")
    
    # Bubble Chart
    category_counts = Data['primary_category'].value_counts()
    colors = plt.cm.get_cmap('tab20c', len(category_counts))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(category_counts.index, category_counts.values, s=category_counts.values*10, c=colors(range(len(category_counts))), alpha=0.7)
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title('Number of Products in Each Category (Bubble Chart)')
    ax.set_xticks(category_counts.index)
    ax.set_xticklabels(category_counts.index, rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    filtered_data = Data.loc[Data.secondary_category == Category]
    filtered_data = filtered_data.loc[filtered_data.skin_tone == Skin]
    filtered_data = filtered_data.loc[filtered_data.skin_type == Type]
    
    Product = st.selectbox('Product Name', filtered_data['product_name'].unique())
    st.write(Product)
    
    Data['review_clean'] = Data['review_text'].apply(clean_text)

    Data.set_index('product_name', inplace=True)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(Data['review_clean'])
    cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    cos_sim
    
    indices = pd.Series(Data.index)
    
    recommendations(Product)
    
#      filtered_data = (Data[(Data['secondary_category'] == Category) & (Data['skin_tone'] == Skin) & (Data['skin_type'] == Type)])
#     if len(filtered_data) > 0:
#         st.write("Hasil Pencarian:")
#         st.write(filtered_data.iloc[0]['product_name'])
#         st.table(filtered_data[['product_name', 'brand_name', 'loves_count', 'price_usd', 'review_title', 'review_text'][0]])
#     else:
#         st.write("Maaf, tidak ada produk yang cocok dengan pilihan Anda.")   
            

if __name__ == "__main__":
    main()
