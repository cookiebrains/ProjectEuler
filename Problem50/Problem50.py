from utilz.prime_utils import *
import itertools


def list_big_primes():
    all_primes = []
    for i in range(950000, 1000000):
        if is_prime(i):
            all_primes.append(i)
    return all_primes


def add_consecutive_primes(lower_index, upper_index):
    total = 0
    while True:
        for p in itertools.islice(get_primes(), lower_index, upper_index):
            total += p
        return total


def generate_index_pairs(upper_lim):
    pairs = [(x, y)
             for x in range(upper_lim)
             for y in range((x + 1), (upper_lim + 1))
             ]
    return pairs


def do_work():
    for x, y in generate_index_pairs(550):
        if abs(x-y) > 540 and (add_consecutive_primes(x, y)) < 1000000 and is_prime(add_consecutive_primes(x, y)):
            print(x, y, x - y, add_consecutive_primes(x, y))


do_work()
