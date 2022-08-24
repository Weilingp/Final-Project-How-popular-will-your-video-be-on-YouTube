import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import altair as alt


st.set_page_config(page_title = "Comment Analysis", page_icon='▶️')


st.title("Sentiments Analysis on Comments")

comments = pd.read_csv('comments_analysis_per_video.csv')
positive_comments = pd.read_csv("positive_comments.csv")
negative_comments = pd.read_csv("negative_comments.csv")
neutral_comments = pd.read_csv("neutral_comments.csv")


df = comments[["video_id", "positive_comments", "negative_comments", "Neutral_comments"]]#.reset_index(inplace= True)

#st.dataframe(df.head())
#input the video we want to analyse

video = st.text_input('Type The VideoID to see the viewer sentiments', 'jt2OHQh0HoQ') 
#st.write('comments analytic of', video)

videoid = str(video)


def ploting_viewer_sent_per_video(videoid):
    
    video = df.loc[df["video_id"] == videoid, :]
   
    if st.button('click to plot the comments'):
        fig = video.plot.bar()
        st.pyplot() 
    else:
        
        st.write("do you want to know how your audience feel about your video?")
    
    
   



 #   st.table(penguins[penguins.species == option])
    
    
    with st.expander("COMMENTS ANALYSIS"):
        
        option = st.selectbox('which type of message do you want?', ('Positive', 'Negative', 'Neutral'))
         ###  Bar Chart using Altair
        
        
            
        if(option == 'Positive'):
            
            st.write("""
            #### Positive Words Mostly used
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
        
        elif(option == 'Negative'):
            
            st.write("""
            #### Negative Words mostly used
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
          
        elif(option == 'Neutral'):
            
            st.write("""
            #### Neutral Words mostly used
            Neutral words that are mostly used by viewers that wrote a comment!
            ***
            """)
            neu = neutral_comments.loc[neutral_comments["video_id"] == videoid, :]
            st.dataframe(neu[["video_id", "clean_comment"]].head())
            
            # Create some sample text
            text2 = str(neu["clean_comment"])
            
            # Create and generate a word cloud image:
            wordcloud = WordCloud(background_color="white").generate(text2)
            
            # Display the generated image:
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.show()
            st.pyplot()
            
            
        else: 
            
             st.write("""
            choose the type of comment you want to see!
            ***
            """)
       
    return video

#channel_with_more_trending_videos(n)

#st.set_page_config(layout="wide") 

 
st.write("""
#### How the viewer feel about your videos
#""")


viewer_sentiments = ploting_viewer_sent_per_video(videoid)
#st.text(channel_choise)
st.table(viewer_sentiments)


   