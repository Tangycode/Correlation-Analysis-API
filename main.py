from fastapi import FastAPI, HTTPException
from schemas import CorrelationInput, CorrelationResponse
from services import calculate_correlation
import logging

app = FastAPI(title="Correlation Analysis API", version="1.0")

logging.basicConfig(level=logging.INFO)

@app.post("/api/v1/correlation-analysis", response_model=CorrelationResponse)
def correlation_analysis(data: CorrelationInput):
    try:
        logging.info("Received correlation analysis request")
        return calculate_correlation(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
