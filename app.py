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
        '<style>' +open('style.css').read()+'<style>'
       ,
        unsafe_allow_html=True,
    )

    # Create tabs in the sidebar for each page
    active_tab = st.sidebar.button("Home")
    if active_tab:
        ast.shared.components.write_page(PAGES["Home"])
    active_tab = st.sidebar.button("Research")
    if active_tab:
        ast.shared.components.write_page(PAGES["Research"])
    active_tab = st.sidebar.button("Prediction")
    if active_tab:
        ast.shared.components.write_page(PAGES["Prediction"])

if __name__ == "__main__":
    main()
