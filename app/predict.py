import numpy as np
import pandas as pd
import joblib

def load_model():
    model = joblib.load("../model/model.pkl")
    return model

def predict_churn(data: dict):
    df = pd.DataFrame([data])
    model = load_model()
    prediction = model.predict(df)
    return {"prediction": prediction[0]}

