from collections import Counter
import os
from sys import argv
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf8') as file:
        text = file.read()
    return text


def get_most_frequent_words(working_text, number_pop_words):
    try:
        return Counter(working_text.split()).most_common(number_pop_words)
    except AttributeError:
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit('Укажите путь к файлу')
    working_text = load_data(argv[1])
    if not working_text:
        exit('Укажите верный путь к файлу')
    number_pop_words = int(input('How much popular words in text you need?'))
    print(number_pop_words, "Most popular words in text(text, quantity): \n",
        get_most_frequent_words(working_text, number_pop_words)
    )
