import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/Results%20dataset%20Sephora.csv'
Data = pd.read_csv(url)

title = "Beauty Things"
subtitle = "Let's find skincare for you!"

st.set_page_config(page_title = title,
                   page_icon = None,
                   layout = "wide")

# st.title(title)
# st.caption(subtitle)

# Bar Chart
category_counts = Data['primary_category'].value_counts()

colors = plt.cm.get_cmap('tab20c', len(category_counts))

# Create the bubble chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(category_counts.index, category_counts.values, s=category_counts.values*10, c=colors(range(len(category_counts))), alpha=0.7)
ax.set_xlabel('Category')
ax.set_ylabel('Count')
ax.set_title('Number of Products in Each Category (Bubble Chart)')
ax.set_xticks(category_counts.index)
ax.set_xticklabels(category_counts.index, rotation=45)
plt.tight_layout()
bubblechart = st.pyplot(fig)
      
st.sidebar.header("Select the option :")

with st.sidebar:          
      Category = st.selectbox('Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
# Dashboard
def main():
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")
    bubblechart
    
    filtered_data = Data[(Data['secondary_category'] == Category) & (Data['skin_tone'] == Skin) & (Data['skin_type'] == Type)]
    if len(filtered_data) > 0:
        st.write("Hasil Pencarian:")
        st.table(filtered_data[['product_name', 'brand_name', 'review_title', 'loves_count', 'price_usd', 'review_text']])
    else:
        st.write("Maaf, tidak ada produk yang cocok dengan pilihan Anda.")
    
            

if __name__ == "__main__":
    main()
