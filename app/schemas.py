from pydantic import BaseModel, Field, model_validator
from typing import Literal


class CreditRiskInput(BaseModel):
    person_age: int = Field(..., ge=18, le=100, description="Age of the borrower")
    person_income: float = Field(..., gt=0, description="Annual income of the borrower")
    person_home_ownership: Literal["RENT", "OWN", "MORTGAGE", "OTHER"]
    person_emp_length: float | None = Field(default=None, ge=0, le=60, description="Employment length in years")
    loan_intent: Literal["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    loan_grade: Literal["A", "B", "C", "D", "E", "F", "G"]
    loan_amnt: float = Field(..., gt=0, description="Loan amount")
    loan_int_rate: float | None = Field(default=None, ge=0, le=100, description="Loan interest rate")
    loan_percent_income: float | None = Field(default=None, ge=0,le=1, description="Loan amount as a fraction of annual income")
    cb_person_default_on_file: Literal["Y", "N"]
    cb_person_cred_hist_length: int = Field(..., ge=0, description="Credit history length in years")

    @model_validator(mode="before")
    @classmethod
    def calculate_loan_percent_income(cls, values):
        if (
            isinstance(values, dict)
            and values.get("person_income") is not None
            and values.get("loan_amnt") is not None):

            values["loan_percent_income"] = (
                values["loan_amnt"] / values["person_income"])

        return values