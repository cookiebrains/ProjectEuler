from utilz.alphabet_values_dictionary import alphabet_values_dict as dict
import math


def get_words():
    with open('./input_files/p042_words.txt', 'r') as file:
        raw = ''.join([l.rstrip() for l in file])
    words = raw.split(sep=',')
    words = list(map(lambda word: word[1:-1].lower(), words))

    return words


def is_triangle(x):
    if is_square(8 * x + 1) and (8 * x - 1) % 2 != 0:
        return True
    else:
        return False


def is_square(x):
    root = math.sqrt(x)
    if root - int(root) == 0:
        return True
    else:
        return False


class Name:
    alphabetic_value = 0

    def __init__(self, name):
        self.name = name
        self.__init_alphabetic_value()

    def __init_alphabetic_value(self):
        value = 0
        for letter in self.name:
            value += dict[letter]
        self.alphabetic_value = value


def solution():
    counter = 0
    words = get_words()
    for word in words:
        if is_triangle(Name(word).alphabetic_value):
            counter += 1
    return counter


def run():
    print(solution())
