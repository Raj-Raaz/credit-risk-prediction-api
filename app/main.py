from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, render_template
from .schemas import CreditRiskInput


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "Credit_risk_prediction.joblib")

model = joblib.load(MODEL_PATH)



api = FastAPI(
    title="Credit Risk Prediction API",
    description="Machine Learning API for Credit Risk Prediction",
    version="1.0.0")


@api.get("/api")
def api_home():
    return {
        "message": "Credit Risk Prediction API is running"
    }


@api.post("/predict")
def predict(data: CreditRiskInput):

    input_data = data.model_dump()
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    result = ("Defaulter" if prediction == 1
        else "Non-Defaulter")

    return {
        "prediction": int(prediction),
        "result": result,
        "default_probability": round(float(probability), 4)
    }


flask_app = Flask(__name__, template_folder="templates")

@flask_app.route("/")
def index():
    return render_template("index.html")


api.mount("/", WSGIMiddleware(flask_app))

app = api