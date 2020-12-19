from utilz.prime_utils import *


def get_solution():
    counter = 1
    while True:
        for prime in get_primes():
            if counter == 10001:
                return prime
            counter += 1


print(get_solution())
