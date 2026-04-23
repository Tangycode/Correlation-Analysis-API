from pydantic import BaseModel, Field
from typing import List

class CorrelationInput(BaseModel):
    batting_scores: List[float] = Field(..., min_items=2, description="List of batting scores")
    bowling_scores: List[float] = Field(..., min_items=2, description="List of bowling scores")

class CorrelationResponse(BaseModel):
    success: bool
    correlation: float
    interpretation: str
