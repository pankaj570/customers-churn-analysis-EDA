## 🎯 Project Objective:
Predict which customers are likely to churn (stop using the service) and send real-time alerts to the business team.

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
