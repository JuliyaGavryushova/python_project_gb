"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
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


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")