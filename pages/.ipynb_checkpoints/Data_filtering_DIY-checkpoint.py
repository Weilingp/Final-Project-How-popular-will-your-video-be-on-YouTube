
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
pip install --upgrade streamlit

iris1 = pd.read_csv("GBvideos_col_centiment_analysis.csv")

iris = iris1[['video_id', 'trending_date', 'title', 'channel_title', 'views', 'likes', 'dislikes', 'comment_count','description', 'category_names','description_length', 'title_length', 'tag_length','category_names_length', 'channel_title_length', 'publish_date','Analysis_title', 'Analysis_tags','Analysis_descrp']]
st.title("🖱️ Interactive table app")
st.markdown("Here you can click and interact with data easily.Go ahead, click on a row in the table below!")


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


iris = iris1[['video_id', 'trending_date', 'title', 'channel_title', 'views', 'likes', 'dislikes', 'comment_count','description', 'category_names','description_length', 'title_length', 'tag_length','category_names_length', 'channel_title_length', 'publish_date','Analysis_title', 'Analysis_tags','Analysis_descrp']]
selection = aggrid_interactive_table(df=iris)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])