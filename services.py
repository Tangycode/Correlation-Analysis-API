import math

def calculate_correlation(data):
    x = data.batting_scores
    y = data.bowling_scores

    n = len(x)

    if n != len(y):
        raise ValueError("Both input lists must have the same length")

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))

    denom_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    denom_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))

    if denom_x == 0 or denom_y == 0:
        raise ValueError("Correlation undefined when variance is zero")

    correlation = numerator / (denom_x * denom_y)

    # Interpretation bands
    if correlation >= 0.7:
        interpretation = "Strong Positive Relationship"
    elif correlation >= 0.3:
        interpretation = "Moderate Positive Relationship"
    elif correlation > -0.3:
        interpretation = "Weak or No Relationship"
    elif correlation > -0.7:
        interpretation = "Moderate Negative Relationship"
    else:
        interpretation = "Strong Negative Relationship"

    return {
        "success": True,
        "correlation": round(correlation, 2),
        "interpretation": interpretation
    }
