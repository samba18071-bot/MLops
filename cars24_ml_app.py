import pandas as pd
import streamlit as st
import pickle

# 1. Load the dataset for preview
cars_df = pd.read_csv("cars24-car-price.csv")

st.write(
    """
    # Cars24 Used Car Price Analyser    
    """
)


# 2. Cache model loading to avoid re-reading the pickle file on every interaction
@st.cache_resource
def load_model():
    with open("car_pred.pkl", "rb") as file:
        return pickle.load(file)

# 3. Model prediction function with the 13 required features
def model_predict(fuel_type, transmission_type, engine, seats):
    reg_model = load_model()

    # Construct dataframe with exact 13 features used during model training
    input_df = pd.DataFrame([{
        'year': 2018.0,
        'km_driven': 40000,
        'mileage': 19.70,
        'engine': float(engine),
        'max_power': 86.30,
        'seats': float(seats),
        'seller_type_Individual': True,
        'seller_type_Trustmark Dealer': False,
        'fuel_type_Diesel': True if fuel_type == 'Diesel' else False,
        'fuel_type_Electric': True if fuel_type == 'Electric' else False,
        'fuel_type_LPG': True if fuel_type == 'LPG' else False,
        'fuel_type_Petrol': True if fuel_type == 'Petrol' else False,
        'transmission_type_Manual': True if transmission_type == 'Manual' else False
    }])

    return reg_model.predict(input_df)

# 4. Streamlit UI Components
col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select Fuel Type", 
                           ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])

engine = col1.slider("Enter Engine CC", 500, 5000, step=100)

seats = col2.selectbox("No of seats", [4, 5, 6, 7, 8])

transmission_type = col2.selectbox("Select Transmission Type", 
                                   ['Manual', 'Automatic'])

# 5. Prediction execution
if st.button("Predict Price"):
    price = model_predict(fuel_type, transmission_type, engine, seats)
    st.success(f"Predicted Price of the Car is: {price[0]:.2f} Lakhs")
st.dataframe(cars_df.head(5))