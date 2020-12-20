from math import sqrt


def getPrimes():
    i = 2
    while True:
        if isPrime(i):
            yield i
        i += 1


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def isPrimeFactor(p, num):
    if isPrime(p) and num % p == 0:
        return True


# def primeFactorization(n):
#     factorization_list = []
#     running_total = n
#     while True:
#         for p in getPrimes():
#             if isPrimeFactor(p, n):
#                 factorization_list.append(p)
#                 running_total = running_total / p
#         if running_total == 1:
#             break
#     return factorization_list

def getLowestPrimeFactor(n):
    for p in getPrimes():
        if p > n:
            return n
        if isPrimeFactor(p, n):
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



def doWork():
    n = 600851475143 
    prime_factors = primeFactorization(n)
    print(prime_factors)
    total = 1
    for factor in prime_factors:
        print(factor)
        total *= factor
    print(f'total: {total}')


doWork()
