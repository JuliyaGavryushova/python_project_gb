"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""

list_things = {
    'tent': 3.0,
    'pot': 0.7,
    'compass': 0.3,
    'lighter': 0.1,
    'products': 3.0
}

max_weight = 2.0


def pack_backpack(lst, max_w):
    current_weight = 0
    backpack = {}

    for key, value in lst.items():
        if current_weight + value <= max_w:
            backpack[key] = value
            current_weight += value

    return backpack


print(pack_backpack(list_things, max_weight))
