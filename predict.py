import pickle
from typing import Literal
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
import xgboost as xgb

app = FastAPI(title="nitrogen-volume-prediction")

# Define request schema
class PipelineInput(BaseModel):
    pipeline_length: float = Field(..., ge=0)
    inner_diameter: float = Field(..., ge=0)
    target_residual_conc: float = Field(..., ge=0)
    operating_pressure: float = Field(..., ge=0)
    temperature: float = Field(..., ge=0)
    num_bends: int = Field(..., ge=0)
    ambient_temperature: float = Field(..., ge=0)
    num_purge_cycles: int = Field(..., ge=0)
    safety_factor: float = Field(..., ge=0)
    pipeline_volume: float = Field(..., ge=0)

# Define response schema
class PredictResponse(BaseModel):
    nitrogen_volume_needed: float

# Load model and vectorizer
with open("model.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)

# Prediction logic
def predict_single(pipeline_input: dict) -> float:
    X = dv.transform([pipeline_input])
    dmatrix = xgb.DMatrix(X, feature_names=dv.get_feature_names_out().tolist())
    prediction = model.predict(dmatrix)
    return float(prediction[0])

# API endpoint
@app.post("/predict", response_model=PredictResponse)
async def predict(pipeline_input: PipelineInput) -> PredictResponse:
    result = predict_single(pipeline_input.model_dump())
    return PredictResponse(nitrogen_volume_needed=result)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)