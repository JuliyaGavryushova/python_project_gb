"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
import random


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        board = []
        while len(board) < 8:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            valid = True
            for c in board:
                if x == c[0] and y == c[1] and abs(x - c[0]) == abs(y - c[1]):
                    valid = False
                    break
            if valid:
                board.append((x, y))
        board_list.append(board)
    return board_list


if __name__ == '__main__':
    print(generate_boards())
