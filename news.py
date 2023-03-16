import streamlit as st
import requests
import pycountry
import streamlit_option_menu as option_menu

api='40a586919f194af3b9810a1fbaee7cd2'

st.set_page_config(page_title="News App", layout='wide')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2017/08/02/14/26/winter-landscape-2571788_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#rd=st.sidebar.radio("Navigation",['Country','Topic'])

rd2=option_menu.option_menu(None,options=['Country','Topic'],orientation ='horizontal', icons=['flag','search'])

if rd2 == 'Country':
    st.title("Top Headlines by Country")
    col1, col2=st.columns([3,1])
    with col1:
        user=st.text_input("Enter Country name")
    with col2:
        cat=st.radio("Select Category", ('business', 'technology','health','sports'))
        bt=st.button('Enter')

    if bt:
        country= pycountry.countries.get(name=user).alpha_2
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category={cat}&apiKey={api}'
        r=requests.get(url).json()
        articles=r['articles']
        for article in articles:
            st.header(article["title"])
            st.write(f"<b>Date: {article['publishedAt']}</b>", unsafe_allow_html=True)
            if article['source']['name']:
                st.markdown(f"Source-{article['source']['name']}")
            if article["author"]:
                st.markdown(f"<span style='background-color:coral; padding:5x; border-radius:20px;'>Author-{article['author']} </span>",unsafe_allow_html=True)
            if article['urlToImage']:
                st.image(article['urlToImage'])
            if article['description']:
                st.write(article['description'])
            st.markdown(f"Link to the article - {article['url']}")
            st.markdown("---")

if rd2 == 'Topic':
    st.title("Top Headlines by Topic")
    c1,c2 = st.columns([2,1])
    with c1:
        topic=st.text_input("Enter news topic")
    #with c2:
        #bt=st.button("Enter",use_container_width=True)
    if topic:
        url= f'https://newsapi.org/v2/everything?q={topic}&apiKey={api}'
        r=requests.get(url).json()
        articles = r['articles']
        for article in articles:
            st.header(article["title"])
            st.write(f"<b>Date: {article['publishedAt']}</b>", unsafe_allow_html=True)
            if article['source']['name']:
                st.markdown(f"Source-{article['source']['name']}")
            if article["author"]:
                st.markdown(
                    f"<span style='background-color:coral; padding:5x; border-radius:20px;'>Author-{article['author']} </span>",
                    unsafe_allow_html=True)
            if article['urlToImage']:
                st.image(article['urlToImage'])
            if article['description']:
                st.write(article['description'])
            st.markdown(f"Link to the article - {article['url']}")
            st.markdown("---")