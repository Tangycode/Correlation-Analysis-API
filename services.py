import math


def pearson_correlation(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denom_y = sum((y[i] - mean_y) ** 2 for i in range(n))

    if denom_x == 0 or denom_y == 0:
        raise ValueError("ZERO_VARIANCE")

    return numerator / math.sqrt(denom_x * denom_y)


def interpret_correlation(r):
    if r == 1:
        return "positive", "perfect positive"
    if r == -1:
        return "negative", "perfect negative"

    if r > 0:
        direction = "positive"
    elif r < 0:
        direction = "negative"
    else:
        direction = "neutral"

    abs_r = abs(r)

    if abs_r >= 0.8:
        strength = "strong"
    elif abs_r >= 0.5:
        strength = "moderate"
    elif abs_r >= 0.2:
        strength = "weak"
    else:
        strength = "very weak"

    return direction, strength


def sample_risk(n):
    if n < 5:
        return "high risk (very small sample)"
    if n < 10:
        return "moderate risk"
    return None
