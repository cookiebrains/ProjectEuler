from utilz.prime_utils import *
import math


def reduce_fraction(n, d):
    numerator_primes = primeFactorization(n)
    numerator_primes.append(1)
    denominator_primes = primeFactorization(d)
    for i in range(len(numerator_primes) - 1, -1, -1):
        numerator = numerator_primes[i]
        if numerator in denominator_primes:
            denominator_primes.remove(numerator)
            del(numerator_primes[i])
    return math.prod(numerator_primes), math.prod(denominator_primes)


def are_fractions_equivalent(a, b, c, d):
    j = reduce_fraction(a, b)
    k = reduce_fraction(c, d)
    if j == k:
        return True
    else:
        return False


def generate_candidates():
    for i in range(10, 100):
        for j in range(10, 100):
            if i % 10 != 0 and j % 10 != 0 and i < j:
                yield i, j


def check_for_solution(candidate):
    a, b = candidate
    c = int(a / 10)
    d = a % 10
    e = int(b / 10)
    f = b % 10
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    if c == e:
        if are_fractions_equivalent(a, b, d, f):
            return a, b
    elif c == f:
        if are_fractions_equivalent(a, b, d, e):
            return a, b
    elif d == e:
        if are_fractions_equivalent(a, b, c, f):
            return a, b
    elif d == f:
        if are_fractions_equivalent(a, b, c, e):
            return a, b
    else:
        return None


def run():
    for candidate in generate_candidates():
        if check_for_solution(candidate) is not None:
            print(candidate)
    print(reduce_fraction((16 * 19 * 26 * 49), (64 * 95 * 65 * 98)))
    # print(reduce_fraction(26, 65))
