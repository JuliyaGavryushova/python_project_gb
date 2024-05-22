"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы
с файлами разных форматов.
"""
import os


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