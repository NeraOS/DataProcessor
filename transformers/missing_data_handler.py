def handle_missing_data(data, strategy='fill', fill_value=None):
    if strategy == 'fill':
        for row in data:
            for key, value in row.items():
                if value == '' or value is None:
                    row[key] = fill_value
    elif strategy == 'remove':
        data = [row for row in data if all(value is not None and value != '' for value in row.values())]
    else:
        raise ValueError("Invalid strategy. Choose 'fill' or 'remove'.")
    return data