import math
from utilz.prime_utils import *


def carousel(num):
    multiplier = 10 ** (math.floor(math.log10(num)))
    result = (int((num - num % 10) / 10)) + (num % 10) * multiplier
    return result


def solution(upper_lim):
    counter = 0
    circular_primes = []
    for p in get_primes():
        if p > upper_lim:
            return counter
        else:
            if get_and_check_all_carousels(p):
                counter += 1
                print(p)


def get_and_check_all_carousels(num):
    digits_in_num = math.floor(math.log10(num) + 1)
    counter = 0
    all_carousels = []
    new_num = num
    while counter < digits_in_num:
        new_num = carousel(new_num)
        counter += 1
        all_carousels.append(new_num)
    result = all(is_prime(item) for item in all_carousels)
    return result


def run():
    # print(get_and_check_all_carousels(197))
    print(solution(1000000))
