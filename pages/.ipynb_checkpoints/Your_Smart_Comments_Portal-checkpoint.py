import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import altair as alt


st.set_page_config(page_title = "Comment Analysis", page_icon='▶️')


st.title("One click and you get an overall opinion about how your audience feel about your video")

comments = pd.read_csv('comments_analysis_per_video.csv')
positive_comments = pd.read_csv("positive_comments.csv")
negative_comments = pd.read_csv("negative_comments.csv")
neutral_comments = pd.read_csv("neutral_comments.csv")


df = comments[["video_id", "positive_comments", "negative_comments", "Neutral_comments"]]#.reset_index(inplace= True)

#st.dataframe(df.head())
#input the video we want to analyse

video = st.text_input('Here put your VideoID to get the comments analysis.', 'lLN1FwiqGwc')

st.write('comments analytic of the video', video)

videoid = str(video)



def ploting_viewer_sent_per_video(videoid):
    
    video = df.loc[df["video_id"] == videoid, :]
    #st.write(video.info())
    y1 = video["positive_comments"]
    y2 = video["negative_comments"]
    y3 = video["Neutral_comments"]
    
    x = ["positive_comments", "negative_comments", "Neutral_comments"]
    y = [video.positive_comments.values, video.negative_comments.values, video.Neutral_comments.values]
    data = pd.DataFrame({
    'comments_an': y,
    'values':x
    })

   
    
    #fig, ax = plt.subplots(figsize=(8,8))
    
    #channel = sns.barplot(x='values', y="comments_an", data=data,palette=('flare'), ax=ax)
    #channel = ax.set(xlabel="number of videos base on the size of the channel", 
      #               ylabel="top20 Channels with most trending videos", title = "n Channels with more trending videos")
    
    #st.pyplot(fig)
    
    
    with st.expander("COMMENTS ANALYSIS"):
         ###  Bar Chart using Altair
            
        st.subheader('Display Bar chart')
        st.bar_chart(video[["positive_comments", "negative_comments", "Neutral_comments"]])
        
        st.write("""
    # Positive Words Mostly used
    Positive words that are mostly used by viewers that wrote a comment!
    ***
    """)
    
        p = positive_comments.loc[positive_comments["video_id"] == videoid, :]
        st.dataframe(p[["video_id", "clean_comment"]].head())
        
        # Create some sample text
        text = str(p["clean_comment"])
        
        # Create and generate a word cloud image:
        wordcloud = WordCloud(background_color="white").generate(text)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write("""
    # Negative Words mostly used
    Negative words that are mostly used by viewers that wrote a comment!
    ***
    """)
        
        n = negative_comments.loc[negative_comments["video_id"] == videoid, :]
        st.dataframe(n[["video_id", "clean_comment"]].head())
        
        # Create some sample text
        text1 = str(n["clean_comment"])
        
        #Create and generate a word cloud image:
        wordcloud = WordCloud(background_color="white").generate(text1)
        
        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        
        st.write("""
    # Neutral Words mostly used
    Neutral words that are mostly used by viewers that wrote a comment!
    ***
    """)
        neu = neutral_comments.loc[neutral_comments["video_id"] == videoid, :]
        st.dataframe(p[["video_id", "clean_comment"]].head())
        
        # Create some sample text
        text2 = str(neu["clean_comment"])
        
        # Create and generate a word cloud image:
        wordcloud = WordCloud(background_color="white").generate(text2)
        
        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    
    return video

#channel_with_more_trending_videos(n)

#st.set_page_config(layout="wide") 

 
#st.write("""
#### How the viewer feel about your videos
#""")

viewer_sentiments = ploting_viewer_sent_per_video(videoid)
#st.text(channel_choise)
st.table(viewer_sentiments)


   