import streamlit as st
import pickle
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title='Crop Yield Prediction',page_icon='🌾',layout='wide')

def lottie_url(url):
    r= requests.get(url)
    if r.status_code!=200:
        return  None
    return r.json()

lottie_coding=lottie_url('https://lottie.host/7b3af45c-2477-4f02-83bf-42bb2cc9c51f/vv1l1CXlFG.json')

with st.container():
    st.header('Make Prediction')
    left_column,right_column=st.columns(2)
    with left_column:
        with st.container():
            crop = st.text_input('Crop', '')
            rainfall = st.text_input('Rainfall in mm', '')
            temperature = st.text_input('Temperature in Celsius', '')
            irr = st.radio('Irrigation used', ['Yes', 'No'])
            if irr=='Yes':
                irrigation=1
            else:
                irrigation=0
            fert = st.radio('Fertilizer used', ['Yes', 'No'])
            if fert=='Yes':
                fertilizer=1
            else:
                fertilizer=0
            features = [rainfall, temperature, fertilizer, irrigation]
            scaler = pickle.load(open('scaler.sav', 'rb'))
            model = pickle.load((open('model.sav', 'rb')))
            pred = st.button('Predict')
            if pred:
                result = model.predict(scaler.transform([features]))  # features is already within a []
                st.write(f'Estimated yield of {crop} is:')
                st.write(result)

    with right_column:
        st_lottie(lottie_coding, height=350, key='coding')