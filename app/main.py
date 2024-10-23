from fastapi import FastAPI, HTTPException
from app.models import PredictionRequest
from app.utils import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/gender")
def predict_gender_endpoint(request: PredictionRequest):
    predicted_gender = predict_gender(request.age, request.month_of_conception)
    
    return {
        "age": request.age,
        "month_of_conception": request.month_of_conception,
        "predicted_gender": predicted_gender
    }
