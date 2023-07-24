import streamlit as st
import joblib
import pandas as pd

# Load the trained model
dt_model = joblib.load('Final_model.joblib')

# Add a title and subtitle
st.write("<center><h1>Sales Prediction App</h1></center>", unsafe_allow_html=True)

st.write("This app uses machine learning to predict sales based on certain input parameters. Simply enter the required information and click 'Predict' to get a sales prediction!")

st.subheader("Enter the details to predict sales")

# Create the input fields
input_data = {}
input_data['store_nbr'] = st.slider("store_nbr", 0, 54)
input_data['products'] = st.selectbox("products", ['AUTOMOTIVE', 'CLEANING', 'BEAUTY', 'FOODS', 'STATIONERY',
                                                   'CELEBRATION', 'GROCERY', 'HARDWARE', 'HOME', 'LADIESWEAR',
                                                   'LAWN AND GARDEN', 'CLOTHING', 'LIQUOR,WINE,BEER', 'PET SUPPLIES'])
input_data['onpromotion'] = st.number_input("onpromotion", step=1)
input_data['state'] = st.selectbox("state", ['Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura',
                                             'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
                                             'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
                                             'El Oro', 'Esmeraldas', 'Manabi'])
input_data['store_type'] = st.selectbox("store_type", ['D', 'C', 'B', 'E', 'A'])
input_data['cluster'] = st.number_input("cluster", step=1)
input_data['dcoilwtico'] = st.number_input("dcoilwtico", step=1)
input_data['year'] = st.number_input("year", step=1)
input_data['month'] = st.slider("month", 1, 12)
input_data['day'] = st.slider("day", 1, 31)
input_data['dayofweek'] = st.number_input("dayofweek, 0=Sun and 6=Sat", step=1)
input_data['end_month'] = st.selectbox("end_month", ['True', 'False'])

# Create a button to make a prediction
if st.button("Predict", key="predict_button", help="Click to make a prediction."):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data])

    # Make a prediction
    prediction = dt_model.predict(input_df)[0]

    # Display the prediction
    st.write(f"The predicted sales are: {prediction}.")
