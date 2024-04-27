"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
или из документации к языку.
"""
import re
from collections import Counter

text = ('В Python имена файлов, аргументы командной строки и переменные окружения представлены'
        ' с использованием строкового типа. В некоторых системах, перед передачей их операционной'
        ' системе необходимо декодирование строк в байты и обратно. Python использует кодировку'
        ' файловой системы для выполнения этого преобразования')


def get_top_10_words(txt):
    txt = re.sub(r'[^\w\s\']', '', txt).lower()
    txt1 = txt.replace("'", " ")
    words = txt1.split()
    words = [word for word in words if not any(char.isdigit() for char in word)]
    word_counts = Counter(words)
    top_10_words = word_counts.most_common(10)
    sorted_top_10_words = sorted(top_10_words, key=lambda x: (x[1], x[0]), reverse=True)
    return sorted_top_10_words


print(get_top_10_words(text))