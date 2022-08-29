import streamlit as st
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

img=Image.open('youtube.png')
st.set_page_config(page_title="Welcome to YouTube Analytics Porta", 
                   page_icon= img,
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

st.sidebar.header('YouTuber,you want to :crystal_ball:')

#CONTACT
########
expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn](https://www.linkedin.com/in/weilingp), and [Twitter](https://twitter.com/mspengde)")


video = ('Video_main_page.mp4')
st.title("Hi, beautiful people, welcome to my final presentation 🤗 ")
st.video(video)

st.markdown("""As of 2022, YouTube has 51+ million active channels<style>.big-font {font-size:100px !important;}</style>
""",unsafe_allow_html=True)

