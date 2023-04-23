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

st.markdown("<link rel='stylesheet' href='style.css'>", unsafe_allow_html=True)


def main():
    """Core of the app - switches between 'tabs' thanks to the sidebar"""

    # Add the hamburger menu

    # Use CSS to style the sidebar and move it to the left side of the screen
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            margin-left: -20px;
            padding: 0;
            background-color: #f5f5f5;
            position: fixed;
            top: 0;
            bottom: 0;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
            z-index: 99;
        }
        .sidebar .sidebar-content li {
            margin-bottom: 10px;
        }
       
        .st-bo {
            padding-right: 2px;
            padding-bottom: 10px!important;
        }

  .css-1aumxhk {
            visibility: hidden;
        }
        .css-3qjal9 {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,  # Fix the typo here
    )

    # Use a beta_expander to create the sidebar content
    selection = st.sidebar.radio("", list(PAGES.keys()), key="sidebar")

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()
