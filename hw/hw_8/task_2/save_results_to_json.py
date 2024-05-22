import json


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as file:
        json.dump(results, file)