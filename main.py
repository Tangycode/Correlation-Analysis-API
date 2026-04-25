from pydantic import BaseModel, Field
from typing import List, Optional

class CorrelationRequest(BaseModel):
    match_id: str = Field(..., min_length=1)
    innings_id: str = Field(..., min_length=1)

    x_metric_name: str
    y_metric_name: str

    x_values: List[float]
    y_values: List[float]

    ball_events: Optional[list] = []
