import streamlit as st
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
    st.subheader('Information: ')
with st.container():
    st.write('-----')
    left_column,right_column=st.columns(2)
    with left_column:
        st.write('##')
        st.write('🌱Efficient Yield Predictions: Our app leverages advanced data analysis to estimate crop yield based on key factors like rainfall, temperature, and soil type.')
        st.write('🌱Empowering Farmers: Gain insights to optimize harvests and make informed decisions for sustainable agriculture.')
        st.write('🌱Tailored Insights: Visualize trends, compare variables, and track factors influencing productivity with intuitive charts.')
        st.write("[Dataset used for Machine Learning Model Building🔍](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)")
    with right_column:
        st_lottie(lottie_coding,height=350,key='coding')