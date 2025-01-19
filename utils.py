def check_data_integrity(data):
    if not data:
        raise ValueError("No data available.")
    keys = set(data[0].keys())
    for row in data:
        if set(row.keys()) != keys:
            raise ValueError("Data integrity error: Inconsistent columns.")
    return True