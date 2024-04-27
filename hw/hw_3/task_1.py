"""
Дан список повторяющихся элементов.Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [2, 2, 5, 8, 5, 5, 0, 1, 6, 6]


def duplicate_elements(lst_n):
    unique = set()
    duplicates = []

    for item in lst_n:
        if item in unique:
            if item not in duplicates:
                duplicates.append(item)
        else:
            unique.add(item)

    return duplicates


print(duplicate_elements(lst))