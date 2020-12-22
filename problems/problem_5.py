from utilz.prime_utils import *


def get_lowest_prime_factor(n):
    for p in get_primes():
        if p > n:
            return n
        if is_prime_factor(p, n):
            return p


def prime_factorization(n):
    factorization_list = []
    running_total = n
    while True:
        current_prime_factor = get_lowest_prime_factor(running_total)
        running_total = running_total / current_prime_factor
        factorization_list.append(current_prime_factor)
        if running_total == 1:
            break
    return factorization_list


def get_factorizations(upper_lim):
    lists_of_prime_factorizations = []
    for i in range(1, upper_lim + 1):
        lists_of_prime_factorizations.append(prime_factorization(i))
    return lists_of_prime_factorizations


def get_LCM_nums(a):
    list_of_lists = a
    instance_counts = {}
    for inner_list in list_of_lists:
        inner_instance_counts = {}
        for num in inner_list:
            if num not in inner_instance_counts:
                inner_instance_counts[num] = 1
            else:
                inner_instance_counts[num] += 1
        for num, count in inner_instance_counts.items():
            if num not in instance_counts:
                instance_counts[num] = 1
            else:
                if count > instance_counts[num]:
                    instance_counts[num] = count
    return instance_counts


def get_solution(counts_dict):
    solution = 1
    for num, count in counts_dict.items():
        solution *= (num ** count)
    return solution


def run():
    a = get_factorizations(20)
    b = get_LCM_nums(a)
    c = get_solution(b)

    print(c)
