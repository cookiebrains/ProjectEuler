from utilz.prime_utils import *


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


def solution():
    j = 210
    while True:
        if number_distinct_primes(j) == 4:
            j += 1
            if number_distinct_primes(j) == 4:
                j += 1
                if number_distinct_primes(j) == 4:
                    j += 1
                    if number_distinct_primes(j) == 4:
                        return j - 3
                        break
        j += 1


def run():
    print(solution())
