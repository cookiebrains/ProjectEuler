# Need to search products of primes that are between 2000 and 5000 and check to see if they are permutations of each other.

def is_permutation(a, b):
    return sorted(a) == sorted(b)


def phi(n):
    result = n  # Initialize result as n

    # Consider all prime factors of n and for every prime factor p, multiply result with (1 - 1 / p)
    p = 2
    while p * p <= n:

        # Check if p is a prime factor.
        if n % p == 0:

            # If yes, then update n and result
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    # If n has a prime factor greater than sqrt(n)
    # (There can be at-most one such prime factor)
    if n > 1:
        result = result * (1.0 - (1.0 / float(n)))

    return int(result)


def solution():
    ratio = 2
    answer = 0
    for num in range(2, 10000000):
        if is_permutation(str(num), str(phi(num))) and num / phi(num) < ratio:
            ratio = num / phi(num)
            answer = num
    return answer


def run():

    print(solution())




