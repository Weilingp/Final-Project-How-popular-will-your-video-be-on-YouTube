import pandas as pd
import streamlit as st
#import altair as alt
from PIL import Image
import seaborn as sns

######################
# Youtube views analyser
#####################



st.write("""
# Trending Youtube Videos
This app will help you analyse your youtube videos to help your videos appeat on the trending list!
***
""") # pour faire une ligne


df = pd.read_csv("channel_sort_by_video_asc.csv")
st.dataframe(df.head())

######################
# Input Text Box
######################

#st.s



number = st.number_input('Choose the number of channels with the most videoson trending list')

st.write('The current number is ', number)



def channel_with_more_videos(number):
    
    chanelsbysize = st.dataframe(df.head(number))
    
    fig, ax = plt.subplots(figsize=(8,8))
    channel = sns.barplot(x="video_count", y="channel_title", data=chanelsbysize ,palette=('flare'), ax=ax)
    channel = ax.set(xlabel="number of videos base on the size of the channel", 
                     ylabel="