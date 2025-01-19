import json

def load_json(file_path):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data