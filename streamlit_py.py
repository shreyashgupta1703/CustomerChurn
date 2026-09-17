import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")
st.title("📊 Customer Churn Prediction")
st.caption("Enter customer details to estimate churn probability.")

# Load trained model artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# Customer inputs
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)

contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_type = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

# Build input dictionary using the same feature names as the training data
input_data = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract_Month-to-month": int(contract_type == "Month-to-month"),
    "Contract_One year": int(contract_type == "One year"),
    "Contract_Two year": int(contract_type == "Two year"),
    "InternetService_DSL": int(internet_type == "DSL"),
    "InternetService_Fiber optic": int(internet_type == "Fiber optic"),
    "InternetService_No": int(internet_type == "No"),
    "TechSupport_No": int(tech_support == "No"),
    "OnlineSecurity_No": int(online_security == "No"),
    "PaymentMethod_Electronic check": int(payment_method == "Electronic check"),
    "DeviceProtection_No": int(device_protection == "No"),
    "DeviceProtection_No internet service": int(device_protection == "No internet service"),
    "DeviceProtection_Yes": int(device_protection == "Yes"),
    "MultipleLines_No": int(multiple_lines == "No"),
    "MultipleLines_No phone service": int(multiple_lines == "No phone service"),
    "MultipleLines_Yes": int(multiple_lines == "Yes"),
}

# Match the exact feature order used during training
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Scale the input before prediction
scaled_input = scaler.transform(input_df)

if st.button("Predict Churn"):
    prediction = model.predict(scaled_input)[0]
    proba = model.predict_proba(scaled_input)[0][1]

    prediction_label = "Churn" if prediction == 1 else "No Churn"
    st.success(f"Prediction: {prediction_label}")
    st.info(f"Churn Probability: {proba:.2%}")
