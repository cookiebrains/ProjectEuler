from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def get_primes():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def is_prime_factor(p, num):
    if is_prime(p) and num % p == 0:
        return True
