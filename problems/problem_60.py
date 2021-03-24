import itertools as it
from utilz.prime_utils import get_primes
from utilz.sorted_set import SortedSet


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


def get_primes_up_to(limit):
    primes = []
    for p in get_primes():
        if p == 2:
            continue
        if p > limit:
            break
        primes.append(p)
    return primes


def concatenate_primes(n, m):
    return is_prime(int(str(n) + str(m))) and is_prime(int(str(m) + str(n)))


def prime_pairs(iterable):
    for n, m in it.combinations(iterable, r=2):
        if not concatenate_primes(n, m):
            return False
    return True


def get_solution():
    primes = get_primes_up_to(10000)
    for n in primes:
        for m in primes[primes.index(n):]:
            if concatenate_primes(n, m):
                for x in primes[primes.index(m):]:
                    if prime_pairs([x, n, m]):
                        for y in primes[primes.index(x):]:
                            if prime_pairs([y, x, n, m]):
                                for z in primes[primes.index(y):]:
                                    if prime_pairs([z, y, x, n, m]):
                                        return [z, y, x, n, m]


def run():
    a = get_solution()
    print(a)
    print(sum(a))
