from loader.csv_loader import load_csv
from loader.json_loader import load_json
from saver.csv_saver import save_csv
from saver.json_saver import save_json
from transformers.filter_transformer import filter_data
from transformers.sort_transformer import sort_data
from transformers.missing_data_handler import handle_missing_data
from statistics.mean_calculator import calculate_mean
from statistics.median_calculator import calculate_median
from statistics.std_calculator import calculate_std
from utils import check_data_integrity

class DataProcessor:
    def __init__(self):
        self.data = []

    def load_data(self, file_path, file_type='csv'):
        if file_type == 'csv':
            self.data = load_csv(file_path)
        elif file_type == 'json':
            self.data = load_json(file_path)
        else:
            raise ValueError("Unsupported file type. Choose 'csv' or 'json'.")
        check_data_integrity(self.data)

    def save_data(self, file_path, file_type='csv'):
        if file_type == 'csv':
            save_csv(self.data, file_path)
        elif file_type == 'json':
            save_json(self.data, file_path)
        else:
            raise ValueError("Unsupported file type. Choose 'csv' or 'json'.")

    def filter_data(self, condition):
        self.data = filter_data(self.data, condition)

    def sort_data(self, key):
        self.data = sort_data(self.data, key)

    def handle_missing_data(self, strategy='fill', fill_value=None):
        self.data = handle_missing_data(self.data, strategy, fill_value)

    def calculate_mean(self, column):
        return calculate_mean(self.data, column)

    def calculate_median(self, column):
        return calculate_median(self.data, column)

    def calculate_std(self, column):
        return calculate_std(self.data, column)