import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run () :
    #membuat judul
    st.title('USED CAR ANALYSIS')

    #menampilkan gambar
    img = Image.open('src/mobil-bekas.jpg')
    st.image(img)

    df = pd.read_csv('cardekho.csv')
    st.dataframe(df)

    #membuat bar plot
    st.write ('### Transmission')
    fig = plt.figure(figsize=(10,5))
    sns.countplot(x='transmission', data=df)
    st.pyplot(fig)

    st.write ('### Seller Type')
    fig = plt.figure(figsize=(10,5))
    sns.countplot(x='seller_type', data=df)
    st.pyplot(fig)

    st.write ('### Owner History')
    fig = plt.figure(figsize=(10,5))
    sns.countplot(x='owner', data=df)
    st.pyplot(fig)

    # #membuat histogram berdasarkan data input
    st.write('### Histogram berdasarkan input')
    option = st.selectbox('Pilih kolom untuk Histogram :', ('year','engine', 'mileage(km/ltr/kg)'), index=0)
    fig2 = plt.figure(figsize=(10,5))
    sns.histplot(data=df[option], bins=30,kde=True)
    st.pyplot(fig2)

    #membuat dengan plotly express
    st.write('### Price Vs Max Power')
    fig3 = px.scatter(df, x='selling_price',y='max_power', hover_data=['name','engine','year'])
    st.plotly_chart(fig3)

if __name__ == "__main__" :
    run()