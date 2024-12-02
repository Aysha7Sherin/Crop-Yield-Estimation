import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import pymysql
import warnings
st.set_page_config(page_title='Crop Yield Prediction',page_icon='🌾',layout='wide')

warnings.filterwarnings('ignore')
con=pymysql.connect(host='localhost',user='root',password='root',database='database_may_24')
query='select * from crop_yield'
df=pd.read_sql(query,con)

st.header('Analysis of Crop Yield data')
x=st.selectbox('Choose x axis:',['Crop','Soil_Type','Region','Weather_Condition','Fertilizer_Used','Irrigation_Used'])
if x:
    # Group data and calculate average yield
    grouped_data = df.groupby(x)['Yield_tons_per_hectare'].mean().reset_index()

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(grouped_data[x], grouped_data['Yield_tons_per_hectare'], color='#7e791b')
    ax.set_title(f"Average Yield by {x}")
    ax.set_xlabel(x)
    ax.set_ylabel('Average Yield (tons per hectare)')
    ax.set_xticks(range(len(grouped_data[x])))
    ax.set_xticklabels(grouped_data[x], rotation=45, ha='right')  # Rotate labels for readability

    # Render the plot in Streamlit
    st.pyplot(fig)

with st.container():
    x1 = st.radio('Choose a feature:',
                  ['Rainfall_mm', 'Temperature_Celsius', 'Days_to_Harvest'])
    if x1:
        # Create a scatter plot
        fig, ax = plt.subplots()
        ax.scatter(df[x1], df['Yield_tons_per_hectare'], color='#7e791b', alpha=0.7, edgecolor='k')
        ax.set_title(f"Scatter Plot of {x1} vs Yield")
        ax.set_xlabel(x1)
        ax.set_ylabel('Yield (tons per hectare)')

        # Render the plot in Streamlit
        st.pyplot(fig)
