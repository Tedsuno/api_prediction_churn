import pandas as pd
import joblib
import os

def load_model():
    base_path = os.path.dirname(__file__)  # le dossier "app/"
    model_path = os.path.join(base_path, "../model/model.pkl")
    model_path = os.path.abspath(model_path)  # convertir en chemin absolu

    model = joblib.load(model_path)
    return model

def predict_churn(data: dict):
    df = pd.DataFrame([data])
    model = load_model()
    prediction = model.predict(df)
    return {"prediction": prediction[0]}

