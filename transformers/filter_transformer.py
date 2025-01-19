def filter_data(data, condition):
    if not callable(condition):
        raise ValueError("Condition must be a callable function.")
    return [row for row in data if condition(row)]