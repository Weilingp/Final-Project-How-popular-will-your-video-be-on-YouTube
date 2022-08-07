import streamlit as st
from PIL import Image
import numpy as np

st.title('why we analyze Youtube Videos')
image_1 = Image.open('why_we_analyz_youtubevideos.png')
st.image(image_1, caption='why_we_analyz_youtubevideos.png')

    
st.title('Machin Learning methods we used to predict popular videos and spam commentsß')
image_2= Image.open('methods_on_project_machinelearing.png')
st.image(image_2, caption='methods_on_project_machinelearing.png')


st.title('Machin Learning methods:Nutral Language Processing NLTK to categorize the comments in : Neg,Pos & Neu.')
image_3= Image.open('methods_we_use_toanalyz-nltk.png')
st.image(image_3, caption='wmethods_we_use_toanalyz-nltk.png')

st.title('Here we can see what are the trending videos are there in GB 2017')
image_4 = Image.open('what_are_the_trending_videos.png')
st.image(image_4, caption='what_are_the_trending_videos.png')

st.title('Let us take a further look at what features in the titles and descriptions of trending videos.')
image_5 = Image.open('mostly_apear_key_words_in_title.png')
st.image(image_5, caption='mostly_apear_key_words_in_title.png')

st.title('These are words that repeated 100+ times.')
image_6 = Image.open('mostly_repeated_words_intitel_100time.png')
st.image(image_6, caption='mostly_repeated_words_intitel_100time.png')

st.title('Now let us see what are the features of words in tags.')
image_7 = Image.open('mostly_apear_key_words_in_tags.png')
st.image(image_7, caption='mostly_apear_key_words_in_tags.png')

st.title('These are words that repeated 100+ times.')
image_8 = Image.open('words_apears_100moretimes_details.png')
st.image(image_8, caption='words_apears_100moretimes_details.png')

st.title('How long will it take a video to be trended ?')
image_9 = Image.open('how_long_takeavideotobetrended.png')
st.image(image_9, caption='how_long_takeavideotobetrended.png')


st.title('YouTube comments in overview')
image_9 = Image.open('YouTube Comments.png')
st.image(image_9, caption='YouTube Comments.png')