import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

st.title("Quotes")

def background_image(topic):
    if topic=='love':
        bimg = st.markdown(
            f"""
                 <style>
                 .stApp {{
                     background-image: url("https://images.unsplash.com/photo-1517607648415-b431854daa86?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1034&q=80");
                     background-attachment: fixed;
                     background-size: cover
                 }}
                 </style>
                 """,
            unsafe_allow_html=True
    )
    elif topic == "life":
        bimg = st.markdown(
            f"""
                         <style>
                         .stApp {{
                             background-image: url("https://cdn.pixabay.com/photo/2018/02/27/17/17/gerbera-flower-3186015_960_720.jpg");
                             background-attachment: fixed;
                             background-size: cover
                         }}
                         </style>
                         """,
            unsafe_allow_html=True
        )
    elif topic == "humor":
        bimg = st.markdown(
            f"""
                         <style>
                         .stApp {{
                             background-image: url("https://images.unsplash.com/photo-1595280503243-a79c68afe418?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80");
                             background-attachment: fixed;
                             background-size: cover
                         }}
                         </style>
                         """,
            unsafe_allow_html=True
        )
    else:
        bimg = st.markdown(
            f"""
                                 <style>
                                 .stApp {{
                                     background-image: url("https://images.unsplash.com/photo-1625768106657-776a102757fe?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80");
                                     background-attachment: fixed;
                                     background-size: cover
                                 }}
                                 </style>
                                 """,
            unsafe_allow_html=True
        )
    return bimg
tag=st.selectbox("Choose a topic",['love','life','humor','inspirational'])
background_image(tag)
bt=st.button("Download as CSV")
if bt:
    st.write("Downloaded, thank you")
url=f"http://quotes.toscrape.com/tag/{tag}/"
#st.write(url)
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
#st.code(soup)
#st.write(soup.title, unsafe_allow_html=True)
quotes=soup.find_all('div', class_='quote')

quotes_dw=[]

for q in quotes:
    text=q.find('span',class_='text').text
    author=q.find('small', class_='author').text
    url=q.find("a")['href']
    link=f"http://quotes.toscrape.com{url}"
    st.markdown(f">{text}")
    #st.caption(author)
    st.markdown(f"Author: <a href={link}>{author}</a>",unsafe_allow_html=True)
    #st.code(f"http://quotes.toscrape.com/author/{author}")
    quotes_dw.append([text, author, link])

df=pd.DataFrame(quotes_dw)

if bt:
    try:
        df=pd.DataFrame(quotes_dw)
        df.to_csv("Quotes.csv",index=False, header=['Quote','Author','Link'], encoding='cp1252')
    except:
        st.write("loading...")

