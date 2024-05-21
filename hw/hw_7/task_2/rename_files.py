"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
import os


def rename_files(desired_name, num_digits, source_ext, target_ext):
    files = os.listdir("test_folder")
    count = 1
    for file in files:
        if file.endswith(source_ext):
            name = desired_name + str(count).zfill(num_digits) + "." + target_ext
            os.rename("test_folder/" + file, "test_folder/" + name)
            count += 1