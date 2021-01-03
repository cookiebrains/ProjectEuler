from utilz.prime_utils import *


def get_truncated_nums(num):
    truncated_str = []
    truncated_nums = []
    for i in range(1, len(str(num))):
        truncated_str.append((str(num)[:i]))
        truncated_str.append((str(num)[i:]))
    for i in truncated_str:
        truncated_nums.append(int(i))
    return truncated_nums


def solution(upper_lim):
    counter = 0
    trunctable_primes = []
    for p in get_primes():
        if p > upper_lim:
            return trunctable_primes
        else:
            if all(is_prime(item) for item in get_truncated_nums(p)):
                trunctable_primes.append(p)
                counter += 1


def run():
    x = 0
    a = (solution(1000000))
    for item in a:
        if item > 10:
            x += item
    print(x)
