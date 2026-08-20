# Credit Risk Prediction API

A machine learning web application that predicts the credit default risk of a loan applicant. The project combines a **FastAPI** backend serving an **XGBoost** classification model with a **Flask**-rendered HTML form for interactive predictions, and is containerized with **Docker**.

## Features

- REST API endpoint (`/predict`) that returns a default prediction and default probability for a loan applicant
- Simple web UI (`/`) built with Bootstrap 5 for submitting applicant details and viewing results
- Input validation via Pydantic, including an auto-computed `loan_percent_income` field
- Trained `scikit-learn` Pipeline (with XGBoost classifier) serialized as a `.joblib` file
- Dockerized for easy deployment

## Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI |
| Frontend | Flask (mounted as WSGI app) + Bootstrap 5 |
| ML Model | XGBoost, scikit-learn Pipeline |
| Data | pandas, NumPy |
| Serialization | joblib |
| Server | Uvicorn |
| Containerization | Docker |

## Dataset

Model trained on the [Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) from Kaggle, which contains applicant demographic, income, employment, and loan information along with the historical default outcome.

## Project Structure

```
credit-risk-prediction-api/
├── app/
│   ├── main.py                          # FastAPI + Flask app, /predict endpoint
│   ├── schemas.py                       # Pydantic input schema & validation
│   └── templates/
│       └── index.html                   # Frontend prediction form
├── Credit Risk.ipynb                    # Model training / EDA notebook
├── Credit_risk_prediction.joblib        # Trained sklearn Pipeline (XGBoost)
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Reference

### `GET /api`
Health check.

**Response**
```json
{ "message": "Credit Risk Prediction API is running" }
```

### `POST /predict`
Returns a credit risk prediction for a loan applicant.

**Request body**

| Field | Type | Required | Notes |
|---|---|---|---|
| `person_age` | int | Yes | 18–100 |
| `person_income` | float | Yes | > 0 |
| `person_home_ownership` | string | Yes | `RENT`, `OWN`, `MORTGAGE`, `OTHER` |
| `person_emp_length` | float | No | 0–60 years |
| `loan_intent` | string | Yes | `PERSONAL`, `EDUCATION`, `MEDICAL`, `VENTURE`, `HOMEIMPROVEMENT`, `DEBTCONSOLIDATION` |
| `loan_grade` | string | Yes | `A`–`G` |
| `loan_amnt` | float | Yes | > 0 |
| `loan_int_rate` | float | No | 0–100 |
| `loan_percent_income` | float | Auto-computed | `loan_amnt / person_income` |
| `cb_person_default_on_file` | string | Yes | `Y` or `N` |
| `cb_person_cred_hist_length` | int | Yes | >= 0 |

**Example request**
```json
{
  "person_age": 28,
  "person_income": 60000,
  "person_home_ownership": "RENT",
  "person_emp_length": 5,
  "loan_intent": "EDUCATION",
  "loan_grade": "B",
  "loan_amnt": 10000,
  "loan_int_rate": 11.5,
  "cb_person_default_on_file": "N",
  "cb_person_cred_hist_length": 4
}
```

**Example response**
```json
{
  "prediction": 0,
  "result": "Non-Defaulter",
  "default_probability": 0.0812
}
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip
- (Optional) Docker

### Local Setup

```bash
git clone https://github.com/Raj-Raaz/credit-risk-prediction-api.git
cd credit-risk-prediction-api

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The app will be available at:
- Web UI: `http://localhost:8000/`
- API docs (Swagger): `http://localhost:8000/docs`

### Run with Docker

```bash
# Build the image
docker build -t raj2903/credit-risk-prediction-api:latest .

# Run the container
docker run -d -p 8000:8000 --name credit-risk-app raj2903/credit-risk-prediction-api:latest
```

Then visit `http://localhost:8000/`.

### Pull from Docker Hub

```bash
docker pull raj2903/credit-risk-prediction-api:latest
docker run -d -p 8000:8000 raj2903/credit-risk-prediction-api:latest
```

## Model

The model is a `scikit-learn` `Pipeline` wrapping preprocessing steps and an XGBoost classifier, trained on the Kaggle Credit Risk dataset and serialized with `joblib` as `Credit_risk_prediction.joblib`. See `Credit Risk.ipynb` for the full training and evaluation workflow.

## License

This project is available for educational and portfolio purposes. Add a license of your choice (e.g., MIT) if you intend to distribute it.

## Author

**Raj** — [GitHub](https://github.com/Raj-Raaz) · [LinkedIn](https://www.linkedin.com/in/iitmraj)
