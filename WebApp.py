import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/Results%20dataset%20Sephora.csv'
Data = pd.read_csv(url)


with st.sidebar:
      st.set_page_config(page_title='Main.py', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
                   
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
            
    # Count the number of products in each category
    category_counts = data['primary_category'].value_counts()

      # Create a color map for each category
    colors = plt.cm.get_cmap('tab20c', len(category_counts))

      # Create the bubble chart
    plt.figure(figsize=(10, 6))
    plt.scatter(category_counts.index, category_counts.values, s=category_counts.values*10, c=colors(range(len(category_counts))), alpha=0.7)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Number of Products in Each Category (Bubble Chart)')
    plt.xticks(rotation=45)
    plt.tight_layout()

# Display the plot
plt.show()
            

if __name__ == "__main__":
    main()
