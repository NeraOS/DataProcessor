import json

def save_json(data, file_path):
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)