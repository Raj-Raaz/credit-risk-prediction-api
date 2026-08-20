# Credit Risk Prediction

Dataset: https://www.kaggle.com/datasets/laotse/credit-risk-dataset

An end-to-end Machine Learning application for predicting the credit default risk of borrowers. The application takes borrower and loan information as input, validates the data using Pydantic, prepares the required features, and uses a trained XGBoost model to predict default risk and probability of default.

The complete application is built with FastAPI and Flask, includes a Bootstrap-based web interface with JavaScript, and is containerized using Docker.

---

## Project Overview

Credit risk assessment is an important problem in lending and Buy Now Pay Later systems. The goal of this project is to identify borrowers who are more likely to default based on their financial and credit-related information.

The application uses features such as age, annual income, home ownership, employment length, loan intent, loan grade, loan amount, interest rate, previous default history, and credit history length. The loan-to-income ratio is calculated automatically from annual income and loan amount.

The model returns a binary prediction along with the estimated probability of default.

---

## Machine Learning

I evaluated Logistic Regression, Random Forest, and XGBoost models. XGBoost was selected and optimized using `RandomizedSearchCV`.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 93.77% |
| Precision | 95.67% |
| Recall    | 74.43% |
| F1 Score  | 83.72% |
| ROC-AUC   | 95.35% |

The preprocessing pipeline includes median imputation, Yeo-Johnson transformation, scaling for numerical features, and One-Hot Encoding for categorical features.

SHAP and feature importance analysis were also used to understand the model's predictions.

---

## Application Architecture

```text
User
 │
 ▼
Flask + Jinja2 Web Interface
 │
 ▼
JavaScript
 │
 │ POST /predict
 ▼
FastAPI
 │
 ▼
Pydantic Validation
 │
 ▼
Feature Preparation
 │
 ▼
XGBoost ML Pipeline
 │
 ▼
Prediction + Default Probability
 │
 ▼
Web Interface
```

---

## Tech Stack

**Machine Learning:** Python, Pandas, NumPy, Scikit-learn, XGBoost, SHAP

**Backend:** FastAPI, Flask, Pydantic, Uvicorn, Jinja2

**Frontend:** HTML, CSS, Bootstrap, JavaScript

**Deployment:** Docker

**Model Serialization:** Joblib

---

## Project Structure

```text
Credit-Risk-Prediction/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── templates/
│       └── index.html
│
├── Credit_risk_prediction.joblib
├── Credit Risk.ipynb
├── dataset.csv
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Run Locally

Clone the repository and install the dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/credit-risk-prediction-api.git
cd credit-risk-prediction-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Open `http://localhost:8000` in your browser.

---

## Run with Docker

Build the Docker image:

```bash
docker build -t credit-risk-predition-api .
```

Run the container:

```bash
docker run -p 8000:8000 credit-risk-predition-api
```

Open the application at `http://localhost:8000`.

FastAPI's interactive API documentation is available at `http://localhost:8000/docs`.

---

## API

### POST `/predict`

The prediction endpoint accepts borrower and loan information and returns the predicted class and default probability.

Example response:

```json
{
  "prediction": 0,
  "result": "Non-Defaulter",
  "default_probability": 0.1258
}
```

---

## Key Features

* End-to-end credit risk prediction
* XGBoost model with hyperparameter tuning
* Automated loan-to-income ratio calculation
* Pydantic input validation
* SHAP-based model explainability
* FastAPI prediction API
* Flask + Jinja2 web interface
* Bootstrap and JavaScript frontend
* Dockerized deployment
* Interactive API documentation

---

## Disclaimer

This project is developed for educational and portfolio purposes. The predictions should not be used as real-world financial or lending decisions without proper validation, fairness testing, regulatory compliance, and continuous model monitoring.

---

## Author

**Raj** — Data Science | Machine Learning | AI
