from fastapi import FastAPI
from pydantic import BaseModel
import joblib as joblib
import pandas as pd

# Load model and feature names
model = joblib.load('models/churn_model.pkl')
input_columns = joblib.load('models/input_features.pkl')

# Define input schema using Pydantic
class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    support_calls: int
    contract_type: str
    payment_method: str

# Categorical encoding (same as training)
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
payment_map = {'Bank transfer': 0, 'Credit card': 1, 'Electronic check': 2, 'Mailed check': 3}

# Init app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
 try:
    # Convert input to DataFrame
    input_data = pd.DataFrame([{
        'tenure': data.tenure,
        'monthly_charges': data.monthly_charges,
        'support_calls': data.support_calls,
        'contract_type': contract_map.get(data.contract_type, 0),
        'payment_method': payment_map.get(data.payment_method, 0)
    }])[input_columns]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(probability, 3)
    }
 except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}
        
