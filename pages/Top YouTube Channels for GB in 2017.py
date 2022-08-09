import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Top_n_Channels",page_icon='▶️')

st.write("""
# Here you can see top YouTube channels for GB in 2017
""") # pour faire une ligne

#input the number of channels we want to see
number = st.number_input('you can view top 10 YouTube channels just type in the text box 10. or type any numbers to show the list you would like to see. Max. number is 20.')

st.write('The number of top channels you want to see is ', number)

n = int(number)


df = pd.read_csv('GBchannels_with_more_the_most_trending_videos.csv')  

def channel_with_more_trending_videos(n):
    
    chanelsbysize = df.head(n)
   
    top_recommendations = chanelsbysize[['channel_title', 'video_count']]#.reset_index()
    
    fig, ax = plt.subplots(figsize=(8,8))
    
    channel = sns.barplot(x="video_count", y="channel_title", data=top_recommendations,palette=('flare'), ax=ax)
    channel = ax.set(xlabel="number of videos base on the size of the channel", 
                     ylabel="top20 Channels with most trending videos", title = "n Channels with more trending videos")
    
    st.pyplot(fig)
    
    return top_recommendations

#channel_with_more_trending_videos(n)

#st.set_page_config(layout="wide") 
st.header("Display the list of the Top trending Channels")
 
if st.button('Top Channel on Trending'):
    
    popul_channels = channel_with_more_trending_videos(n)
    #st.text(channel_choise)
    st.table(popul_channels)
else:
     st.write('Show the the Top trending channels!')
