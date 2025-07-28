from fastapi import FastAPI
from pydantic import BaseModel
from schemas import ClientData
from predict import predict_churn
import pandas as pd

app = FastAPI()

@app.post("/predict")
def client(client: ClientData):
        df = client.dict()
        df = predict_churn(df)
        return df
