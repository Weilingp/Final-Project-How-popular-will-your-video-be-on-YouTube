import pandas as pd
import streamlit as st




path = ''

df = pd.read_csv('GBvideos_col_centiment_analysis.csv')  


def channel_with_more_videos(n):
    
    chanelsbysize =df.groupby("channel_title").size().reset_index(name="video_count")
    chanelsbysize = chanelsbysize.sort_values("video_count", ascending=False).head(n)
    top_recommendations = chanelsbysize['channel_title'].reset_index()
    top_recommendations.rename(columns =
    {'index':'Total_Videos','channel_title':'Channel_Title'},inplace =True)
    top_recommendations= top_recommendations.sort_values("Total_Videos", ascending=False).head(n)
    return top_recommendations

channel_with_more_videos(20)

st.set_page_config(layout="wide") 
st.title("Top Trending Videos per Channel")
 
st.write("""
### Top Trending Videos per Channel
""")
channel_choise = st.selectbox(
                      'channel_title',
                      (df.channel_title)
                      )
popul_channels = channel_with_more_videos(20)
st.text(channel_choise)
st.table(popul_channels)
