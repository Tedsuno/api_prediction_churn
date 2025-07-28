import pickle as pk
import numpy as np
import pandas

def load_model():
    with open("../model/model.pkl",'rb') as f :       
        model=pk.load(f)
    return model

def predict_churn(data : dict):
    df=pandas.DataFrame([data])
    model=load_model()
    model.predict(df)