from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import CorrelationRequest
from services.correlation_service import (
    pearson_correlation,
    interpret_correlation,
    sample_risk
)
from helpers.validation import validate_correlation_request

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Khel AI Correlation Service Running"}

# ---------------- CORRELATION API ----------------
@app.post("/api/v1/correlation-analysis")
def correlation_api(payload: CorrelationRequest):

    try:
        x = payload.x_values
        y = payload.y_values

        validate_correlation_request(x, y)

        r = pearson_correlation(x, y)

        direction, strength = interpret_correlation(r)

        n = len(x)

        return {
            "formula_name": "Pearson correlation",
            "correlation_value": round(r, 4),
            "direction": direction,
            "strength": strength,
            "interpretation": f"{strength} {direction} relationship between {payload.x_metric_name} and {payload.y_metric_name}",
            "sample_size": n,
            "pairs_used": n,
            "x_metric_name": payload.x_metric_name,
            "y_metric_name": payload.y_metric_name,
            "warning": sample_risk(n)
        }

    except ValueError as e:

        error_map = {
            "MISMATCH_LENGTH": "x_values and y_values must have equal length",
            "INSUFFICIENT_DATA": "Minimum 2 values required",
            "NON_NUMERIC_VALUES": "All values must be numeric",
            "ZERO_VARIANCE": "Zero variance detected in input",
            "NON_NUMERIC_INPUT": "Invalid input type"
        }

        err = str(e)

        return HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "error_code": err,
                "message": error_map.get(err, "Validation error"),
                "expected_format": "List[float]"
            }
        )
