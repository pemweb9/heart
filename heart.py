import pickle
import streamlit as st

model = pickle.load(open('heart.sav', 'rb'))

st.title('Heart Attack')

age = st.number_input('age')
sex = st.number_input('sex')
cp = st.number_input('cp')
trestbps = st.number_input('trestbps')
chol = st.number_input('chol')
fbs = st.number_input('fbs')
restecg = st.number_input('restecg')
thalach = st.number_input('thalach')
exang = st.number_input('exang')

predict = ''

if st.button('Heart Attack'):
    predict = model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang]]
    )
    st.write('Heart Attack: ', predict)