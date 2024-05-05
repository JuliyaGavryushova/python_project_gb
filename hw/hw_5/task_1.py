"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(f_path):
    path_end_index = f_path.rfind("/")
    path = f_path[:path_end_index + 1]
    extension_start_index = f_path.rfind(".")
    name = f_path[path_end_index + 1:extension_start_index]
    extension = f_path[extension_start_index:]
    result = (path, name, extension)
    return result


print(get_file_info(file_path))
