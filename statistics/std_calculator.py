def calculate_std(data, column):
    values = [float(row[column]) for row in data if row[column] is not None and row[column] != '']
    if not values:
        return 0
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5