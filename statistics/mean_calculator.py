def calculate_mean(data, column):
    values = [float(row[column]) for row in data if row[column] is not None and row[column] != '']
    if not values:
        return 0
    return sum(values) / len(values)