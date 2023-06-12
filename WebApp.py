import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

url = 'https://raw.githubusercontent.com/nakhwaazizah/Sephora/main/PreprocessingDatasetSephora.csv'
Data = pd.read_csv(url)
        
# def Category(Data,n):
#       col1,col2,col3,col4 = st.columns(4)
    
#     with col1:
#             kategori = st.selectbox('Product Category', Data['secondary_category'].unique())
    
#     with col2:
#             skin = st.selectbox('Your Skin Tone', Data['skin_tone'].unique())
      
#     with col3:
#             type = st.selectbox('Your Skin Type', Data['skin_type'].unique())
    
#     with col4:
#             eye = st.selectbox('Your Eye Color', Data['eye_color'].unique())
#     return Data,n
    
#     if item != 'all':
#         df = df.loc[df.item == int(item)]
        
#     if store != 'all':
#         df = df.loc[df.store == int(store)]
    
#     df = df.drop(['store','item'], axis=1)
   
#     return df, n

with st.sidebar:
      Category = st.selectbox('Skincare Category', Data['secondary_category'].unique())
      
      Skin = st.selectbox('Skin Tone', Data['skin_tone'].unique())
      
      Type = st.selectbox('Skin Type', Data['skin_type'].unique())
      
      Eye = st.selectbox('Eye Color', Data['eye_color'].unique())
        
        
# fig = px.scatter(data_frame=Data,x=Category, y=Skin, size =Type,Eye=Color,log_x=True,log_y=True,size_max=Circle_area)
# st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# Dashboard
def main():
    # Halaman Utama (Home)
    st.title("Beauty Things")
    st.write("Let's find skincare for you!")

if __name__ == "__main__":
    main()


