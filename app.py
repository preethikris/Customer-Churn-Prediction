import streamlit as st
import numpy as np
import pickle

# Load files
model = pickle.load(open('model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))
defaults = pickle.load(open('defaults.pkl', 'rb'))

st.title("Customer Churn Prediction")

MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")
tenure = st.number_input("Tenure")

PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Other"])
InternetService = st.selectbox("Internet Service", ["Fiber optic", "Other"])

# Encode categorical
Payment_Electronic = 1 if PaymentMethod == "Electronic check" else 0
Internet_Fiber = 1 if InternetService == "Fiber optic" else 0

# Create full input
input_data = defaults.copy()

input_data['MonthlyCharges'] = MonthlyCharges
input_data['TotalCharges'] = TotalCharges
input_data['tenure'] = tenure
input_data['PaymentMethod_Electronic check'] = Payment_Electronic
input_data['InternetService_Fiber optic'] = Internet_Fiber

# Convert to array in correct order
data = np.array([[input_data[col] for col in features]])

# Predict
if st.button("Predict"):
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer likely to churn ❌")
    else:
        st.success("Customer likely to stay ✅")