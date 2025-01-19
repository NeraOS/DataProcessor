import csv

def save_csv(data, file_path):
    if not data:
        raise ValueError("No data to save.")
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)