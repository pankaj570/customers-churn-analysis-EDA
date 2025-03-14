## 🎯 Project Objective:
Predict which customers are likely to churn (stop using the service) and send real-time alerts to the business team.

## 📦 Step-by-Step Project Structure:
1. Data Collection
- Use a sample telecom churn dataset (Kaggle) or simulate your own.
- Include features like:
- customer_id, tenure, monthly_charges, contract_type, support_calls, etc.

2. Exploratory Data Analysis (EDA)
- Identify trends in churned vs. retained customers.
- Visualize correlation between churn and other features.
    
3. Feature Engineering
- Encode categorical variables.
- Create new features like average_call_duration, late_payment_count.

4. Model Training
- Train a classification model (e.g. Random Forest).
- Evaluate with precision, recall, F1, confusion matrix.

5. Model Deployment with FastAPI
- Wrap your trained model in a FastAPI endpoint for prediction.
- Accept new customer data via API and return churn probability.

6. Real-Time Dashboard (Streamlit)
- Upload or simulate real-time customer activity.
- Display: Churn predictions
- Filters: contract type, region, tenure
- Alert status


## 🔧 Tools & Technologies:
- Python (main language)
- Pandas, NumPy, scikit-learn, XGBoost
- Seaborn, Matplotlib (for EDA/visualizations)
- Streamlit (interactive dashboard)
- FastAPI (serve the ML model)
- Excel to store results

## 🔧 Project Setup and Run:
1. Clone project at local machine
2. Install requied python librarry if not installed already
   - pip install pandas
   - pip install numpy
   - pip install fastapi uvicorn joblib pandas
   - pip install streamlit requests
3. Open Project in VS-Code
4. First Run 'notebooks/EDA_and_model_training.ipynb'
5. Run 'api/fastapi_app' using command 'uvicorn api.fastapi_app:app --reload'
6. Test API using swagger doc using Swagger file : http://127.0.0.1:8000/docs
   ```json
   URL POST http://127.0.0.1:8000/predict
   {
     "tenure": 12,
     "monthly_charges": 75.50,
     "support_calls": 3,
     "contract_type": "Month-to-month",
     "payment_method": "Credit card"
   }
8. Run streamlit file 'dashboard/streamlit_app.py' using command 'streamlit run dashboard/streamlit_app.py'
9. Open Streamlit dashboard using URL : http://localhost:8501/
