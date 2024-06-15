import streamlit as st

st.title('동물 이미지 😊')
title = st.text_input('영어로 동물 이름 입력: ')

if st.button('찾아보기'):
    url = 'https://edu.spartacodingclub.kr/random/?' + title
    st.image(url)