"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

a, b, c = map(int, input('Введите 3 стороны треугольника: ').split())


def triangle(n1, n2, n3):
    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        if n1 != n2 != n3:
            return 'Треугольник разносторонний'
        elif n1 == n2 == n3:
            return 'Треугольник равносторонний'
        else:
            return 'Треугольник равнобедренный'
    else:
        return 'Треугольника с такими сторонами не существует'


print(triangle(a, b, c))