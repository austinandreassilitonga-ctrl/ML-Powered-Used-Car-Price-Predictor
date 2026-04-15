import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA Page','Price Prediction Page'))

if page == 'EDA Page' :
    eda.run()
else  :
    prediction.run()