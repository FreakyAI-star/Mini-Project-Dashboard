import streamlit as st
import awesome_streamlit as ast

import src.home
import src.research
import src.prediction

# List of pages available for display
PAGES = {
    "Home": src.home,
    "Research": src.research,
    "Prediction": src.prediction,
}

def main():
    """Core of the app - switches between 'tabs' thanks to the sidebar"""

    # Add the hamburger menu

    # Use CSS to style the sidebar and move it to the left side of the screen
    st.markdown(
        '<style>' + open('style.css').read()+
        '.sidebar .sidebar-content .block-container {border: none;}' +
        '.sidebar .sidebar-content button {border: none;}' +
        '</style>',
        unsafe_allow_html=True,
    )
    
    # Initialize a variable to keep track of which tab is currently active
    active_tab = "Home"
    
    # Create buttons in the sidebar for each page
    if st.sidebar.button("Home", key="home"):
        active_tab = "Home"
    if st.sidebar.button("Research", key="research"):
        active_tab = "Research"
    if st.sidebar.button("Prediction", key="prediction"):
        active_tab = "Prediction"
    
    # Only show the "Home" button if it's the currently active tab
    if active_tab == "Home":
        ast.shared.components.write_page(PAGES["Home"])
    elif active_tab == "Research":
        ast.shared.components.write_page(PAGES["Research"])
    elif active_tab == "Prediction":
        ast.shared.components.write_page(PAGES["Prediction"])

if __name__ == "__main__":
    main()
