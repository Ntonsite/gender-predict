from pydantic import BaseModel

class PredictionRequest(BaseModel):
    age: int  # Mother's age
    month_of_conception: int  # Month of conception (1 - 12)
