import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


st.set_page_config(page_title = "Comment Analysis", page_icon='▶️')


st.title("Sentiments Analysis on Comments Per video")

comments = pd.read_csv('spam_perc_by_videoid.csv')
non_spam_comments = pd.read_csv("non_spam_comments.csv")

df = comments[["video_id", "total_videos", "total_spam_comments", "perc"]]#.reset_index(inplace= True)

good_comment = non_spam_comments.loc[non_spam_comments["true_values"]==0, :]

#st.dataframe(df.head())
#input the video we want to analyse

video = st.text_input('Type The VideoID to view the percentage of spam comments', 'VideoID')

#st.write('This is the classifications of the comments of the video', video)

videoid = str(video)



def ploting_spam_comments_per_video(videoid):
    
    video = df.loc[df["video_id"] == videoid, :]
    st.dataframe(video)
    
    good_comments = good_comment.loc[good_comment["video_id"]==videoid, :]
    st.dataframe(good_comments[["predictions", "true_values", "clean_comment"]].head())
  
    fig = video.plot.bar()
    st.pyplot()
   
    return video

st.write("""
#### Percentage of spam comments
***
""")


if st.button('Comments'):
    viewer_sentiments = ploting_spam_comments_per_video(videoid)
    #st.text(channel_choise)
    st.table(viewer_sentiments)

else:
    st.write('predict the percentage of Spam comments!')


