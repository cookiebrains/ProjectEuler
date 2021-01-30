from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def get_primes():
    yield 2
    yield 3
    i = 5
    while True:
        if is_prime(i):
            yield i
        i += 2


def is_prime_factor(p, num):
    if is_prime(p) and num % p == 0:
        return True


def getLowestPrimeFactor(n):
    for p in get_primes():
        if p > n:
            return n
        if is_prime_factor(p, n):
            return p


def primeFactorization(n):
    factorization_list = []
    running_total = n
    while True:
        current_prime_factor = getLowestPrimeFactor(running_total)
        running_total = running_total / current_prime_factor
        factorization_list.append(current_prime_factor)
        if running_total == 1:
            break
    return factorization_list


def number_distinct_primes(num):
    i = 2
    distinct_primes = set()
    while i < sqrt(num) or num == 1:
        if num % i == 0:
            num = num / i
            distinct_primes.add(i)
            i -= 1
        i += 1
    return len(distinct_primes) + 1
