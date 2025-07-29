import pandas as pd
import joblib
import os

# Fonction qui permet de charger le modèle pkl via joblib


def load_model():
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, "../model/model.pkl")
    model_path = os.path.abspath(model_path)

    model = joblib.load(model_path)
    return model

# Fonction qui permet d'utiliser le modèle et de
# prédire le churn


def predict_churn(data: dict):
    df = pd.DataFrame([data])
    model = load_model()
    prediction = model.predict(df)
    return {"prediction": prediction[0]}
