import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("Real-Time Customer Churn Predictor")

st.markdown("Fill in customer details below to check churn probability.")

# User inputs
tenure = st.slider("Tenure (months)", 1, 72, 12)
monthly_charges = st.slider("Monthly Charges ($)", 20.0, 120.0, 75.0)
support_calls = st.slider("Support Calls (last 3 months)", 0, 10, 2)

contract_type = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox("Payment Method", ['Credit card', 'Bank transfer', 'Mailed check', 'Electronic check'])

# Predict button
if st.button("🔮 Predict Churn"):
    input_data = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "support_calls": support_calls,
        "contract_type": contract_type,
        "payment_method": payment_method
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            churn_prob = result['churn_probability']
            churn_pred = result['churn_prediction']

            st.success(f"🔁 Churn Probability: **{churn_prob * 100:.2f}%**")
            if churn_pred == 1:
                st.error("High risk of churn!")
            else:
                st.info("Low risk of churn.")
            
        else:
            st.error("API Error. Please try again later.")
    except:
        st.error("Failed to connect to FastAPI server. Is it running?")

