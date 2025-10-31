import pickle
import uvicorn

from fastapi import FastAPI
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field

class Input(BaseModel):
    lead_source: Literal["paid_ads", "organic_search"]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)
    

class PredictResponse(BaseModel):
    lead_probability: float
    lead: bool

app = FastAPI(title = "lead_conversion")

with open('pipeline_v2.bin', 'rb') as f_in:
    model = pickle.load(f_in)

def get_prediction(input):
    prediction = model.predict_proba(input)[0,1]
    return float(prediction)

@app.post("/predict")
def predict(input: Input) -> PredictResponse:
    prob = get_prediction(input.model_dump())
    return PredictResponse(
        lead_probability = prob,
        lead = prob >= 0.5
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)