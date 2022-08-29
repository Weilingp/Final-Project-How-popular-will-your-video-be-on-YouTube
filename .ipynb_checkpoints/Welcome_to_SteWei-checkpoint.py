import streamlit as st
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import re
import wordninja
from textblob import TextBlob
import altair as alt
from streamlit_player import st_player
import seaborn as sns
import matplotlib.pyplot as plt


#############
#PAGE SET UP
#############
img=Image.open('youtube.png')
st.set_page_config(page_title="Welcome to YouTube Analytics Porta", 
                   page_icon= img,
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)

#########
#SIDEBAR
########
st.sidebar.header('YouTuber,you want to :crystal_ball:')

nav = st.sidebar.radio('',['Go to homepage', 'Predicting Your Video Popularity','Your Smart Comments Portal', 'Your Spam Comments Filter', 'Top YouTube Channels 2017_2018'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')


#CONTACT
########
expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn](https://www.linkedin.com/in/weilingp/) and [Twitter](https://twitter.com/mspengde) ")

#######
#PAGES
######

#HOME
#####

if nav == 'Go to homepage': 


    video = ('Video_main_page.mp4')
    st.title("Hi, beautiful people, welcome to my final presentation 🤗 ")
    """
    [![Star](https://img.shields.io/github/stars/dlopezyse/Synthia.svg?logo=github&style=social)](https://github.com/Weilingp)
    [![Follow](https://img.shields.io/twitter/follow/mspengde?style=social)](https://twitter.com/mspengde)
    [![LinkedIn](https://img.shields.io/badge/linkedin--yellow.svg?logo=linkedin&logoColor=orange&style=social)](https://www.linkedin.com/in/weilingp/)
    """
    st.video(video)
    st.markdown("""As of 2022, YouTube has 51+ million active channels<style>.big-font {font-size:100px !important;}</style>
    """,unsafe_allow_html=True)


#-----------------------------------------
#Predicting Your Video Popularity
##########    
if nav == 'Predicting Your Video Popularity':  
    # load model
    # Embed a youtube video
    st.title("Views Prediction")
    p_title('Get a preliminary prediction for your newly edit video')
    st.text('')
    st.write("""
    
    let us help you to predict the number of views you might get on YouTube. In our case study, Miguel's video marketplace is in category_id 19 (Trevell segment).Here we take this realy example from YouTube - A travel Vlog about African holiday.[Orignial link here]("https://youtu.be/m7emNoKgzYk")
    """)
    st_player("https://youtu.be/m7emNoKgzYk")
    st.write("""
    just fill up the box with your video featureas and then click "Views Prediction🤗"
    """)

    loaded_model = pickle.load(open('models/trained_pipe_randomforest_views_prediction.sav', 'rb'))

    #video_id = st.text_input("VideoId")
    tag = st.text_input("Tag","#visitseychelles")
    title = st.text_input("Title"," SEYCHELLES | EAST AFRICA TRAVEL VLOG ")
    channel_title = st.text_input("Channel_title","Being Neiicey")
    category_id = st.number_input("Category_id",19.00)
    Description = st.text_input("Description","Seychelles, East Africa Vlog! Wow... what an amazing trip, I got to meet such kind hearted, fun and intelligent black women. Beautiful beaches & scenery ... bucket list destination CHECK!Travel in Luxury w/ Chidi Ashley Travels https://luxetribes.com you won't regret it!! ")

    channel_data = pd.DataFrame({
        #"video_id": [video_id],
        "tag": [tag],
        "title": [title],
        "category_id": [category_id],
        "channel_title":[channel_title],
        "description": [Description]

    })
    category = pd.read_csv("category_names.csv")

    df = pd.merge(channel_data, category)


    df['tags_words'] = df['tag'].apply(lambda n: len(n.split(' ')))
    df['title_words'] = df['title'].apply(lambda n: len(n.split(' ')))

    df['title_length'] = df['title'].str.len()
    df['tag_length'] = df['tag'].str.len()
    df['channel_title_length'] = df['channel_title'].str.len()
    df['description_length'] = df['description'].str.len()
    df['category_names_length'] = df['category_names'].str.len()
    df['tag_length'] = df['tag'].str.len()



    def cleaning_colimns(text):

        cleaned = text.apply(lambda s: re.sub(r'[^A-Za-z0-9 ]+', ' ', str(s)))
        cleaned = text.apply(lambda s: ' '.join(wordninja.split(s)))

        return cleaned

    df["cleaned_tag"] = cleaning_colimns(df["tag"])
    df["cleaned_description"] = cleaning_colimns(df["description"])
    df["cleaned_title"] = cleaning_colimns(df["title"])

    def polarityfunc(text):
        return TextBlob(text).sentiment.polarity

    df["polarity_tag"] = df["cleaned_tag"].apply(polarityfunc)
    df["polarity_title"] = df["cleaned_description"].apply(polarityfunc)
    df["polarity_description"] = df["cleaned_title"].apply(polarityfunc)

    def getAnalysis(score):
        if score < 0:
            return "Negative"
        elif score == 0:
            return "Neutral"
        else:
            return "Positive"

    df['Analysis_title']= df["polarity_title"].apply(getAnalysis)
    df['Analysis_tags']= df["polarity_tag"].apply(getAnalysis)
    df['Analysis_descrp']= df["polarity_description"].apply(getAnalysis)

    #df.set_index('video_id')

    channel_features = df[["category_id", "tags_words", "title_words", "category_names",
                        "tag_length",
                        "description_length",
                        "title_length",
                        "category_names_length",
                        "channel_title_length",
                        "Analysis_title",   
                        "Analysis_tags",              
                        "Analysis_descrp"]]

    #tell once click let do the prediction
    # prediction
    if st.button('Views Prediction') and channel_features.shape[0] != 0:

        prediction = loaded_model.predict(channel_features)
        st.write("the channel can have between:", prediction - 1765773, " and ", prediction + 1765773, " views")
    else:
         st.write('predict the views!')

    st.markdown("<h4 style='text-align: center; color:grey;'>Know your enemy and know yourself, and you will never lose a battle. -The Art of War &#129302;</h4>", unsafe_allow_html=True)
    st.text('')

    
#-----------------------------------------
#Your Smart Comments Portal
##########    
if nav == 'Your Smart Comments Portal':  
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


#-----------------------------------------
#Your Spam Comments Filter
##########    
if nav == 'Your Spam Comments Filter':  
    st.title("Sentiments Analysis on Comments Per video")

    comments = pd.read_csv('spam_perc_by_videoid.csv')
    non_spam_comments = pd.read_csv("non_spam_comments.csv")

    df = comments[["video_id", "total_videos", "total_spam_comments", "perc"]]#.reset_index(inplace= True)

    good_comment = non_spam_comments.loc[non_spam_comments["true_values"]==0, :]

    #st.dataframe(df.head())
    #input the video we want to analyse

    video = st.text_input('Type The VideoID to view the percentage of spam comments', 'jt2OHQh0HoQ')

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

#-----------------------------------------
#Top YouTube Channels 2017_2018
##########    
if nav == 'Top YouTube Channels 2017_2018':  
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
            
