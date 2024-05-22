"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и
все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
-Для дочерних объектов указывайте родительскую директорию.
-Для каждого объекта укажите файл это или директория.
-Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results


def get_dir_size(direc):
    total_size = 0

    for path, dirs, files in os.walk(direc):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)

        for sub_dir in dirs:
            total_size += get_dir_size(os.path.join(path, sub_dir))

    return total_size


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as file:
        json.dump(results, file)


def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(results, file)


directory = 'C:\\Users\\User\\Desktop\\pythonProjectGB'
results = traverse_directory(directory)
print(results)
