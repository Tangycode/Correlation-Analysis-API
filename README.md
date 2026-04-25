# Khel AI Correlation Analysis API

## Purpose
Compute Pearson correlation between any two cricket metrics.

---

## Endpoint
POST /api/v1/correlation-analysis

---

## Input Schema
- match_id (string)
- innings_id (string)
- x_metric_name (string)
- y_metric_name (string)
- x_values (List[float])
- y_values (List[float])
- ball_events (optional)

---

## Output Schema
- correlation_value
- direction
- strength
- interpretation
- sample_size
- pairs_used
- warning

---

## Error Codes

| Code | Meaning |
|------|--------|
| MISMATCH_LENGTH | arrays not equal |
| INSUFFICIENT_DATA | < 2 values |
| NON_NUMERIC_VALUES | invalid type |
| ZERO_VARIANCE | constant array |

---

## Edge Cases Covered
- perfect positive correlation
- perfect negative correlation
- zero variance detection
- small sample warning

---

## Notes
- Uses Pearson correlation only
- Fully stateless
- Backend-only computation
- Strict validation enforced
