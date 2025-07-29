from fastapi import FastAPI
from app.schemas import ClientData
from app.predict import predict_churn

# Utilisation de la bibliothèque FastApi pour créer l'application 
# pour le modèle


app = FastAPI()

# Création de la route predict et de la fonction 


@app.post("/predict")
def client(client: ClientData):
    df = client.dict()
    df = predict_churn(df)
    return df
