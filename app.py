import streamlit as st
from components.sidebar import render_sidebar
from components.home_page import render_home
from components.generate_page import render_generate

st.set_page_config(
    page_title="YARAAssist",
    page_icon="/images/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

selected_page = render_sidebar()

if selected_page == "🏠 Home":
    render_home()
elif selected_page == "⚡ Generate":
    render_generate()