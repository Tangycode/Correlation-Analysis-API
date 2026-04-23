from pydantic import BaseModel
from typing import List

class CorrelationInput(BaseModel):
    batting_scores: List[float]
    bowling_scores: List[float]

class CorrelationResponse(BaseModel):
    correlation: float
    interpretation: str
