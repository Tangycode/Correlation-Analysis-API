def validate_lists(x, y):
    if len(x) != len(y):
        raise ValueError("Input lists must have same length")
