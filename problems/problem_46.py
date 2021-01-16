from utilz.prime_utils import *
from math import sqrt


def get_odd_composites():
    i = 9
    while True:
        if not is_prime(i):
            yield i
        i += 2


def solution():
    for number in get_odd_composites():
        for a in range(1, int(sqrt(number)) + 1):
            if is_prime(number - 2 * (a ** 2)):
                break
        else:
            return number


def run():
    print(solution())
