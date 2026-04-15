import streamlit as st
import pandas as pd
import pickle

#Load all files
with open('src/best_model.pkl', 'rb') as file:
    best_model = pickle.load(file)

def run() :
    with st.form('form_used_car'):
        name = st.text_input('Name : ', value='')
        brand = st.text_input('Brand : ', value='')
        km_driven = st.number_input('Kilometer : ', min_value =0, max_value = 999999, value =300000)
        year = st.slider('Year : ', min_value = 1900, max_value = 2026, value =2000)

        st.markdown('-----')

        seller_type = st.selectbox('Seller Type : ', ('Individual','Dealer','Trustmark Dealer'), index=0)
        fuel = st.selectbox('Fuel Type : ', ('Diesel','Petrol','CNG', 'LPG'), index=1)
        transmission = st.selectbox('Transmission : ', ('Manual','Automatic'), index=1)
        owner = st.selectbox('Owner Type : ', ('Test Drive Car','First Owner','Second Owner','Third Owner','Fourth & Above Owner'), index=0)

        st.markdown('-----')
        mileage = st.number_input('Mileage (km/ltr/kg) : ', min_value = 8, max_value = 35, value = 16)
        engine = st.number_input('Engine(cc) : ', min_value = 700, max_value = 2000, value = 1200)
        max_power = st.number_input('Max Power(HP) : ', min_value = 60, max_value = 200, value = 80)
        seats = st.number_input('Seats : ', min_value = 2, max_value = 7, value = 5)
    
        submitted = st.form_submit_button('Predict')
    
    data = {
        'name': name,
        'year': year,
        'km_driven' : km_driven,
        'fuel' : fuel,
        'seller_type' : seller_type,
        'transmission' : transmission,
        'owner' : owner,
        'mileage' : mileage,
        'engine': engine,
        'max_power' : max_power,
        'seats' : seats,
        'brand' : brand
}

    data_inf = pd.DataFrame([data])
    st.dataframe(data_inf)
    
    #Inference
    if submitted :
        # Predict using Model
        target_pred_inf = best_model.predict(data_inf)
        st.write (f'### Price : {str(int(target_pred_inf))} INR')

if __name__ == "__main__" :
    run()  