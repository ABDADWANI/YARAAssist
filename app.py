import streamlit as st
from components.sidebar import render_sidebar
from components.home_page import render_home
from components.generate_page import render_generate

# Page config
st.set_page_config(
    page_title="YARAAssist",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS from external file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# Render sidebar and get selected page
selected_page = render_sidebar()

# Render the appropriate page based on selection
if selected_page == "🏠 Home":
    render_home()
elif selected_page == "⚡ Generate":
    render_generate()