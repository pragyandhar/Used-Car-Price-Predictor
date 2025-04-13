# Step 9: Create a simple Streamlit GUI to predict car price
# Save this as a separate script (e.g., app.py) and run it using: streamlit run app.py
import pickle
import streamlit as st
import numpy as np

st.title("🚗 Used Car Price Predictor")

# Input fields
year = st.number_input('Year of Purchase', min_value=1990, max_value=2025, value=2015)
present_price = st.number_input('Current Ex-Showroom Price (in Lakhs)', value=5.0)
kms_driven = st.number_input('Kilometers Driven', value=30000)
owners = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])

# Convert to dummy variables manually
fuel_diesel = 1 if fuel_type == 'Diesel' else 0
fuel_petrol = 1 if fuel_type == 'Petrol' else 0
seller_individual = 1 if seller_type == 'Individual' else 0
trans_manual = 1 if transmission == 'Manual' else 0

# Load model
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create input array
input_data = np.array([[year, present_price, kms_driven, owners, fuel_diesel, fuel_petrol, seller_individual, trans_manual]])

if st.button('Predict Price'):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Selling Price: ₹{prediction:.2f} Lakhs")
