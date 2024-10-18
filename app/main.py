from fastapi import FastAPI, HTTPException
from app.models import PredictionRequest
from app.utils import *

app = FastAPI()

@app.post("/gender")
def predict_gender_endpoint(request: PredictionRequest):
    # Call utility function to get the prediction
    predicted_gender = predict_gender(request.age, request.month_of_conception)
    
    return {
        "age": request.age,
        "month_of_conception": request.month_of_conception,
        "predicted_gender": predicted_gender
    }
