import streamlit as st

st.set_page_config(page_title="Welcome to YouTube Analytics Porta", 
                   page_icon=":youtube:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)




video = ('Video_main_page.mp4')
st.title("Hi, beautiful people, welcome to my final presentation 🤗 ")
st.video(video)

st.markdown("""As of 2022, YouTube has 51+ million active channels<style>.big-font {font-size:100px !important;}</style>
""",unsafe_allow_html=True)