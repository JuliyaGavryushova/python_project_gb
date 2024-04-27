"""
Напишите функцию для транспонирования матрицы
"""

matrix = [[4, 7, 3],
          [3, 9, 6],
          [1, 2, 9],
          [9, 8, 3]]


def transpose(mtrx):
    result = []
    for i in range(len(mtrx[0])):
        row = []
        for j in range(len(mtrx)):
            row.append(mtrx[j][i])
        result.append(row)

    return result


print(transpose(matrix))