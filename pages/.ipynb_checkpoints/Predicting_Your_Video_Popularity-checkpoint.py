# load model
import pickle
import pandas as pd
import streamlit as st
import re
import wordninja
from textblob import TextBlob
 
st.title("Views Prediction")
 
st.write("""
### Predicting the Views
let us help you predict the number of views you can have on youtube 
""")

loaded_model = pickle.load(open('models/trained_pipe_randomforest_views_prediction.sav', 'rb'))
 
#video_id = st.text_input("VideoId")
tag = st.text_input("Tag")
title = st.text_input("Title")
channel_title = st.text_input("Channel_title")
category_id = st.number_input("Category_id")
Description = st.text_input("Description")

channel_data = pd.DataFrame({
    #"video_id": [video_id],
    "tag": [tag],
    "title": [title],
    "category_id": [category_id],
    "channel_title":[channel_title],
    "description": [Description]
    #"views": [100000]
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
if st.button('Views Prediction'):
    
    prediction = loaded_model.predict(channel_features)
    st.write("the channel can have:", prediction, "als views")
    st.write("Our prediction is the number of 'VIEW PREDICTION' +/- '1,765,773 mean_absolute_error' ")

else:
     st.write('predict the views!')

#prediction = loaded_model.predict(channel_features)

#st.write("the channel can have:", prediction , "of views")