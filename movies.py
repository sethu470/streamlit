import streamlit as st
import requests

api='da0da510'
#st.set_page_config(page_title="Movie Search App", layout='wide')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/reserve/D9xlw7UxTBqQw5sLf8cJ_reef%20insp-72.jpg?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.title("Movie Search App")
title=st.text_input("Enter Movie name and press enter")
#bt=st.button("Click here")

if title:
    try:
        url=f'http://www.omdbapi.com/?t={title}&apikey={api}'
        r=requests.get(url).json()
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(r['Poster'])
        with col2:
            st.markdown(f"### {r['Title']}")
            st.write(f"Released: {r['Released']}")
            st.write(f"Runtime: {r['Runtime']}")
            st.write(f"Genre: {r['Genre']}")
            st.write(f"Director: {r['Director']}")
            st.write(f"Actors: {r['Actors']}")
            st.markdown(f"Plot: {r['Plot']}")
            st.write(f"IMDB Rating: {r['imdbRating']}")
            st.progress(float(r['imdbRating'])/10)
    except:
        st.error("No movie found with given title")

