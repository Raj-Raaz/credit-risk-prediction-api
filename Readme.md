Dataset: https://www.kaggle.com/datasets/laotse/credit-risk-dataset


# Credit Risk Prediction

An end-to-end Machine Learning application for predicting the credit default risk of borrowers.

The project takes borrower and loan information as input, validates the data using Pydantic, performs the required feature preparation, and uses a trained Machine Learning model to predict whether the borrower is likely to default.

The trained model is exposed through a FastAPI endpoint and integrated with a Flask + Jinja2 web interface. The complete application is containerized using Docker.

---

## Project Overview

Credit risk assessment is an important problem in lending and Buy Now Pay Later systems. The objective of this project is to build a Machine Learning solution that can identify borrowers who are more likely to default on their loans.

The application accepts borrower and loan-related information such as:

- Age
- Annual Income
- Home Ownership
- Employment Length
- Loan Intent
- Loan Grade
- Loan Amount
- Loan Interest Rate
- Previous Default History
- Credit History Length

The model then produces:

- Credit risk prediction
- Default / Non-Default classification
- Probability of default

---

## Application Architecture

```text
                    User
                     │
                     ▼
             Flask + Jinja2 UI
                     │
                     │ JSON Request
                     ▼
                  FastAPI
                     │
                     ▼
                 Pydantic
              Data Validation
                     │
                     ▼
             Feature Preparation
                     │
                     ▼
              ML Prediction Model
                     │
                     ▼
              Prediction Result
                     │
                     ▼
                 FastAPI
                     │
                     ▼
             Flask / Web UI
