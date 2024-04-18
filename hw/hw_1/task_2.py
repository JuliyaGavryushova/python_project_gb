"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

number = int(input('Введите число: '))


def simple_or_compound_num(num):
    if num < 1 or num > 100000:
        return 'Число должно быть больше 1 и не превышать 100000'
    i = 1
    a = []
    while i * i <= num:
        if num % i == 0:
            a.append(i)
            if i != num // i:
                a.append(num // i)
        i += 1
    a.sort()
    if len(a) == 2:
        return 'Число является простым'
    else:
        return 'Число является составным'


print(simple_or_compound_num(number))