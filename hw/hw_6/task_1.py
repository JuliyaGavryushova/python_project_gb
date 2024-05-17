"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
import sys


def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def is_valid_date(date_string):
    day, month, year = list(map(int, date_string.split('.')))
    check_days = {1: 31, 2: 29 if leap_year(year) else 28, 3: 31, 4: 30, 5: 31,
                  6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    max_day = check_days.get(month)
    if not max_day or (year < 1 or year > 9999) or (day < 1 or day > max_day):
        return False
    else:
        return True


if __name__ == '__main__':
    # print(is_valid_date('31.12.2024'))
    # print(is_valid_date('31.02.2020'))
    # print(is_valid_date('12.10.10000'))
    if len(sys.argv) < 2:
        print("Please provide a date in the format 'dd.mm.yyyy' as an argument.")
    else:
        date_to_check = sys.argv[1]
        if is_valid_date(date_to_check):
            print("The date {} is valid.".format(date_to_check))
        else:
            print("The date {} is invalid.".format(date_to_check))
