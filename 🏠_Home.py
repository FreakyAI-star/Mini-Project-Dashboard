import streamlit as st
import awesome_streamlit as ast


import streamlit.components.v1 as components
st.set_page_config(page_title="Dashboard", page_icon="")


# Replace "your_code" with your actual font awesome code

# List of pages available for display
st.title('Alfred - Home')
with st.spinner("Loading About ..."):
    st.markdown(
        """
        This Streamlit app is a Financial data dashbord that could be used
        for data visualization, exploration and predicting behavior of
        Financial quantities.""", unsafe_allow_html=True,
       
    )
st.markdown(
'<style>'+open('style.css').read()+'</style>'
       ,
        unsafe_allow_html=True,
 )

    
    # Initialize a variable to keep track of which tab is currently active
    # active_tab = "Home"
    
    # # Create buttons in the sidebar for each page
    # if st.sidebar.button("Home", key="home") and active_tab != "Home":
    #     active_tab = "Home"
    # if st.sidebar.button("Research", key="research") and active_tab != "Research":
    #     active_tab = "Research"
    # if st.sidebar.button("Prediction", key="prediction") and active_tab != "Prediction":
    #     active_tab = "Prediction"
    
    # # Show the active tab content
    # if active_tab == "Home":
    #     ast.shared.components.write_page(PAGES["Home"])
    # elif active_tab == "Research":
    #     ast.shared.components.write_page(PAGES["Research"])
    # elif active_tab == "Prediction":
    #     ast.shared.components.write_page(PAGES["Prediction"])

