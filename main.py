from fastapi import FastAPI
from schemas import CorrelationInput, CorrelationResponse
from services import calculate_correlation

app = FastAPI()

@app.post("/correlation-analysis", response_model=CorrelationResponse)
def correlation_analysis(data: CorrelationInput):
    return calculate_correlation(data)
