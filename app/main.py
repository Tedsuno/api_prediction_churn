from fastapi import FastAPI
from app.schemas import ClientData
from app.predict import predict_churn

app = FastAPI()


@app.post("/predict")
def client(client: ClientData):
    df = client.dict()
    df = predict_churn(df)
    return df
