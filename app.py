import streamlit as st
import awesome_streamlit as ast

import src.home
import src.research
import src.prediction


ast.core.services.other.set_logging_format()

# List of pages available for display
PAGES = {
    # "Home": src.home,
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
        unsafe_allow_html=True,  # Fix the typo here
    )

    # Use a beta_expander to create the sidebar content
    selection = st.sidebar.radio("", list(PAGES.keys()),key="radio")

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()
