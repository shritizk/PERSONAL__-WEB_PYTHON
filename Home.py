import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


col1,emptycol,col2=st.columns([1.5,0.5,1.5])


with col1:
    st.image("images/photo.jpg",width=400)

with col2:
    st.title("SHRITIZ KUMAR")
    content="""
    Hey , I am shritiz . I am a bca student at sai nath uni , Rachi Jharkhand. 
    I am born and brought up in Delhi,India. 
    currently working on my self to work in software industry as a python developer."""

    st.info(content)

st.write("Below you will find my projects :-")

col3,emptycol2,col4=st.columns([1.5,0.5,1.5])


df=pd.read_csv("data.csv",sep=";")


n=int(len(df)/2)
print(n)

with col3:
    for index,row in df[:n].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")
with col4:
    for index,row in df[n:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")
