from collections import Counter
import os
from sys import argv
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding="utf8") as file:
        lines = file.read()
    return lines


def get_most_frequent_words(python_object, number_pop_words):
    try:
        return Counter(python_object.split()).most_common(number_pop_words)
    except AttributeError:
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit('Укажите путь к файлу')
    python_object = load_data(argv[1])
    if not python_object:
        exit("Укажите верный путь к файлу")
    number_pop_words = int(input("How much popular words in text you need?"))
    print(get_most_frequent_words(python_object, number_pop_words))
