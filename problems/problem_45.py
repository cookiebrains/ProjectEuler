import math


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


def is_pentagonal(x):
    if is_square(24 * x + 1) and (1 + math.sqrt(24 * x + 1)) % 6 == 0:
        return True
    else:
        return False


def is_hexagonal(x):
    if is_square(8 * x + 1) and (1 + math.sqrt(8 * x + 1)) % 4 == 0:
        return True
    else:
        return False


def solution():
    i = 144
    while True:
        result = i * (2 * i - 1)
        if is_pentagonal(result):
            return result
        i += 1


def run():
    print(solution())
