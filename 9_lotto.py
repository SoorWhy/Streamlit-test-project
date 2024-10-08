import streamlit as st
import random
import datetime



st.title(':sparkles:로또 생성기:sparkles:')
button = st.button('로또를 생성해주세요!')

if button:
    for i in range(5):
        number = random.sample(range(1, 46), k=6)
        st.subheader(f'{i+1}. 행운의 번호: :green[{sorted(number)}]')