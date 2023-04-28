import streamlit as st
import awesome_streamlit as ast


import streamlit.components.v1 as components
st.set_page_config(page_title="Dashboard", page_icon="")


import streamlit as st

import streamlit as st

# Define some CSS styles for the title and content
import streamlit as st
page_bg_img = '''
<style>

</style>
'''
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('back.png')
# Use the st.markdown function to display the styled CSS
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define some CSS styles for the title and content
title_style = """
    <style>
    /* Align title to the left */
   .css-uf99v8 {
   
    align-items: baseline !important;
    margin-top: 7rem;
}
h1 {

    color: springgreen !important;
    padding: 0 !important;
    font-size: 86px;
  
}
.css-1n76uvr {

    padding-left: 4rem !important;
}
.css-1we6k59 {
    
    margin-bottom: 20px !important;
   
}
    </style>
"""
content_style = "<div style='font-size: 36px;'>Data Analysis Tool</div>"

# Use the st.markdown function to display the styled title and content
st.markdown(title_style, unsafe_allow_html=True)
st.title("StockPilot")
st.markdown(content_style, unsafe_allow_html=True)



# Create a subheader with bold and left-aligned text
