<<<<<<< HEAD
import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA Page','Price Prediction Page'))

if page == 'EDA Page' :
    eda.run()
else  :
=======
import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA Page','Price Prediction Page'))

if page == 'EDA Page' :
    eda.run()
else  :
>>>>>>> d8da3f7c96a527086599c221b4c3001a6b906bcc
    prediction.run()