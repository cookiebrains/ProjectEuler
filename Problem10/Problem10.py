from utilz.prime_utils import *


def get_sum_of_primes_under_limit(upper_bound):
    sum_of_primes = 0
    for item in get_primes():
        if item < upper_bound:
            sum_of_primes += item
        if item > upper_bound:
            break
    return sum_of_primes


def do_work():
    print(get_sum_of_primes_under_limit(2000000))


do_work()

# This solution took 6.44 seconds
