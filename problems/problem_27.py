from utilz.prime_utils import *


def quadratic_prime_generator(a, b):
    counter = 0
    for num in range(100):
        candidate = num * num + a * num + b
        if is_prime(candidate):
            counter += 1
        else:
            return counter


# b has to be prime
def get_b_list():
    list_b = []
    counter = 1
    while True:
        for prime in get_primes():
            list_b.append(prime)
            if prime > 1000:
                return list_b
            counter += 1


# a has to be even
def get_a_list():
    list_a = []
    for num in range(-1000, 1000):
        if num % 2 != 0:
            list_a.append(num)
    return list_a


def run():
    solution_list = []
    a = get_a_list()
    b = get_b_list()
    for x in a:
        for y in b:
            # print(f'checking {x, y}'
            if quadratic_prime_generator(x, y) > 70:
                solution_list.append((x * y))
    print(solution_list)
