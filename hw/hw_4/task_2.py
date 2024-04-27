"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def key_params(**args):
    result = {}
    for key, value in args.items():
        if value.__hash__ is None:
            value = str(value)
        result[value] = key

    return result


print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))