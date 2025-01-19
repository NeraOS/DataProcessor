def calculate_median(data, column):
    values = sorted([float(row[column]) for row in data if row[column] is not None and row[column] != ''])
    n = len(values)
    if n == 0:
        return 0
    if n % 2 == 1:
        return values[n//2]
    return (values[n//2 - 1] + values[n//2]) / 2