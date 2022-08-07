import pandas as pd
import streamlit as st


df = pd.read_csv("GBvideos_col_centiment_analysis.csv")
def video_rec_per_channel(channel):
    
    videos = []
    
    for i in (df['channel_title']):
        
        if i == channel:
            
            videos = df.loc[df['channel_title'] == i, :]
            
            channel_withmoreviews = videos.groupby('title')[['views']].sum()#.reset_index()
            channel_withmoreviews.sort_values(by='views',inplace=True,ascending=False)
            channel_withmoreviews.head(1)
    
    return channel_withmoreviews.head(1)


st.write(video_rec_per_channel('John Lewis'))