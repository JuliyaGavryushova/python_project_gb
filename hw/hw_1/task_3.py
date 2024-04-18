"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT).
"""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def guess_number():
    randint_num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print('Программа загадала число от 0 до 1000. Угадайте его за 10 попыток')

    count = 0
    while count < 10:
        user_guess = int(input('Введите ваше предположение: '))

        if user_guess < randint_num:
            print('Больше')
        elif user_guess > randint_num:
            print('Меньше')
        else:
            print('Поздравляю, вы угадали число!')
            break

        count += 1

    if count == 10:
        print(f'К сожалению, вы использовали все 10 попыток. Загаданное число было {randint_num}.')


guess_number()