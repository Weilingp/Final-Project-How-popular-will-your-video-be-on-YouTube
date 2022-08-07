import streamlit as st
from streamlit_option_menu import option_menu

# def main_page():
#     st.sidebar.markdown("# Welcome to my final project 🎈")

# def page2():
#     st.markdown("# Get lost on trending videos on Youtube? 🎬")
#     st.sidebar.markdown("# Position Your YouTube Channel 🎬")

# def page3():
#     st.markdown("Know how your audians feel your video 🎬")
#     st.sidebar.markdown("# Know your audian 🎬")
    
# def page4():
#     st.markdown("Prediction your videos on trending 🎉")
#     st.sidebar.markdown("# Preliminary predicting your video 🎉")

# page_names_to_funcs = {
#     "A problem solving project": main_page,
#     "Get lost on youtubing": page2,
#     "Understand your audian": page3,
#     "Predicting your video": page4,
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()





st.set_page_config(page_title = "Welcome to SteWei",page_icon='▶️')


video = ('Video_main_page.mp4')
st.title("Hi, beautiful people, welcome to my final presentation 🤗 ")
st.video(video)

st.markdown("""As of 2022, YouTube has 51+ million active channels<style>.big-font {font-size:100px !important;}</style>
""",unsafe_allow_html=True)


