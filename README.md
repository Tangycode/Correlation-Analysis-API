# Correlation Analysis API

## Version
v1

## Base Endpoint
POST /api/v1/correlation-analysis

## Objective
Evaluates the relationship between batting and bowling performances using Pearson correlation.

## Input
```json
{
  "batting_scores": [1.2, 0.8, 1.5],
  "bowling_scores": [0.9, 0.7, 1.4]
}
