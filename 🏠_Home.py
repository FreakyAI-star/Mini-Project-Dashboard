import streamlit as st
import awesome_streamlit as ast

import streamlit.components.v1 as components
st.set_page_config(page_title="Dashboard", page_icon="📈", initial_sidebar_state="expanded")

# Set background color and image
# page_bg = """
# <style>
# body {
# background-image: "https://blog.paperspace.com/content/images/size/w1050/2021/05/0_JhQln53nvsJNM7-c.jpg";
# background-size: cover;
# }
# </style>
# """
st.markdown("https://blog.paperspace.com/content/images/size/w1050/2021/05/0_JhQln53nvsJNM7-c.jpg", unsafe_allow_html=True)
# Replace "your_code" with your actual font awesome code

# List of pages available for display
st.title('Financial Dashboard')
with st.spinner("Loading About ..."):
    st.markdown(
        """
        A Financial data dashbord that could be used
        for data visualization, exploration and predicting behavior of
        Financial quantities.""", unsafe_allow_html=True,
       
    )
st.markdown(
'<style>'+open('style.css').read()+'</style>'
       ,
        unsafe_allow_html=True,
 )
from streamlit_card import card
cols=st.columns(2)
with cols[0]:
    card(
        title="Research",
        text="View companies and check stats",
        image="https://tradebrains.in/features/wp-content/uploads/2021/07/stock-market-news-trade-brains.jpg",
        url="http://localhost:8501/Research"
    )
with cols[1]:
    card(
        title="Prediction",
        text="Predict the future of stocks",
        image="https://miro.medium.com/v2/resize:fit:1400/1*NpT5pyemQQsGEHXbfS51Zw.png",
        url="http://localhost:8501/Prediction"
    )