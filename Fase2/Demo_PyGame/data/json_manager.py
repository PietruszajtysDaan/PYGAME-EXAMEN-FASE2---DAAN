# File: data/json_manager.py
import json


class JSONManager:
    @staticmethod
    def load_data(filepath):
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []
        except json.JSONDecodeError:
            # If the file is corrupted, return an empty list
            return []

    @staticmethod
    def save_data(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)