import streamlit as st
import awesome_streamlit as ast


import streamlit.components.v1 as components
st.set_page_config(page_title="Dashboard", page_icon="")


import streamlit as st

# Set page title
st.title("Stock Market Dashboard")

# Create a header for the page
st.header("Welcome to our stock market analysis tool")

# Create a subheader with bold and left-aligned text
st.subheader("**Research**")

# Add some descriptive text for the Research section
st.write("Our research section provides in-depth analysis of key stocks and market sectors, helping you stay informed and make informed investment decisions.")

# Create another subheader for the Prediction section
st.subheader("**Prediction**")

# Add some descriptive text for the Prediction section
st.write("Our prediction section uses advanced modeling techniques to forecast stock prices and identify emerging trends, giving you a competitive edge in the market.")

# Align all text to the left side of the page
st.set_option('deprecation.showfileUploaderEncoding', False)

# Hide Streamlit menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
