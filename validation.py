def validate_correlation_request(x_values, y_values):
    if not isinstance(x_values, list) or not isinstance(y_values, list):
        raise ValueError("NON_NUMERIC_INPUT")

    if len(x_values) != len(y_values):
        raise ValueError("MISMATCH_LENGTH")

    if len(x_values) < 2:
        raise ValueError("INSUFFICIENT_DATA")

    if any(not isinstance(i, (int, float)) for i in x_values + y_values):
        raise ValueError("NON_NUMERIC_VALUES")

    if len(set(x_values)) == 1 or len(set(y_values)) == 1:
        raise ValueError("ZERO_VARIANCE")
