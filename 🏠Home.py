import streamlit as st
st.set_page_config(page_title='Crop Yield Prediction',page_icon='🌾',layout='wide')
import base64

# Add custom CSS for background image
def set_background(image_file):
    with open(image_file, "rb") as img:
        img_data = img.read()
        # Encode image in base64
        img_base64 = base64.b64encode(img_data).decode()
    # Add background CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            height: 100vh; /* Full height of the viewport */
        }}
        
        /* Add a semi-transparent overlay */
        .stApp::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7); /* Black overlay with 50% opacity */
            z-index: -1;
        }}
        /* Text adjustments */
        .main .block-container {{
            color: white; /* Make text white */
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.7); /* Add text shadow */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background for home page
set_background("BG CYE.png")

with st.container():
    st.write('-----')
    with st.container():
        st.subheader('Welcome 🧑‍🌾 ')
        st.header('Crop Yield Estimator🤖')
    st.write('##')
    st.write('The Crop Yield Estimator App is a data-driven application designed to help farmers, agricultural experts, and policymakers accurately predict crop yields.'
             ' Leveraging advanced machine learning algorithms and real-time data inputs, the app provides valuable insights to enhance agricultural decision-making and optimize farm productivity.'
             'This app helps farmers to estimate their crop yield based on data which are temperature, rainfall, irrigation, fertilzer.'
             )
