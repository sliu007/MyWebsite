import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
#st.markdown(body, unsafe_allow_html=False)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.markdown('**<p style="font-size: 60px;"> Samuel Liu</p>**', unsafe_allow_html=True)
    content = """
    Hi, I am Sam! I am a python Programmer, karate instructor and 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!")
"""

st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")