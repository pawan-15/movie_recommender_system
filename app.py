import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                '}?api_key=6b81d3f0dc3955afd9379bf1ee0b4376&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster =[]
    for i in movies_list1:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
movies_list = movies['title'].values
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
     'Tell me the latest movie you watched!',
     (movies_list))

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)
    with col1:
             st.text(names[0])
             st.image(poster[0])
    with col2:
             st.text(names[1])
             st.image(poster[1])
    with col3:
             st.text(names[2])
             st.image(poster[2])

    col4, col5 = st.columns(2)
    with col4:
             st.text(names[3])
             st.image(poster[3])
    with col5:
             st.text(names[4])
             st.image(poster[4])
