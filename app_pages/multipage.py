import streamlit as st


class MultiPage:
    """
    Generates multiple pages on the Streamlit dahsborad through object orientation.
    """
    def __init__(self, app_name) -> None:
        """
        Creates array containing all dashboard pages and 
        displays title and favicon
        """
        self.pages = []
        self.app_name = "Cherry Leaf Powdery Mildew Detector"

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🍒")
    
        def add_page(self, title, func) -> None:
            """
            Add pages to app
            """
            self.pages.append({"title": title, "function": func})